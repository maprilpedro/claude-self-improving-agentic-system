#!/usr/bin/env python3
"""
Local podcast-script generator — runs the two-stage chain (outline -> per-segment
transcript) entirely against a local Ollama model. The orchestrator (Claude) never
reads the source or the script: this script prints ONLY metadata to stdout, so
sensitive Adobe-internal content never enters Claude's context / never leaves the mac.

Usage:
  python3 generate_local.py --source <path> [--profile solo_brief] [--lang fr]
                            [--out <dir>] [--model qwen3:30b-a3b-instruct-2507-q4_K_M]
                            [--briefing "extra steer"] [--title "Short Title"]

Reads profiles from episodes.json / speakers.json next to this file.
Writes a markdown script to --out and prints a one-line JSON metadata blob.
"""

import argparse, json, os, sys, datetime, re, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
OLLAMA = os.environ.get("OLLAMA_HOST", "http://localhost:11434") + "/api/chat"
NUM_CTX = 65536  # 64K — safe on 48GB (weights ~18GB + KV ~8GB); Qwen3 ceiling is 262K


def die(msg):
    print(json.dumps({"ok": False, "error": msg}))
    sys.exit(1)


def ollama_chat(model, prompt, force_json=False, temperature=0.7):
    body = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
        "options": {"temperature": temperature, "num_ctx": NUM_CTX},
    }
    if force_json:
        body["format"] = "json"
    req = urllib.request.Request(
        OLLAMA, data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=1200) as r:
            data = json.loads(r.read().decode("utf-8"))
    except Exception as e:
        die(f"Ollama call failed: {e}")
    return data["message"]["content"]


def parse_json_obj(text, key):
    """Robustly pull {key: [...]} out of a model response."""
    try:
        obj = json.loads(text)
        if key in obj:
            return obj[key]
    except Exception:
        pass
    m = re.search(r"\{.*\}", text, re.DOTALL)
    if m:
        try:
            obj = json.loads(m.group(0))
            if key in obj:
                return obj[key]
        except Exception:
            pass
    die(f"Could not parse '{key}' from model output")


def speakers_block(speakers):
    return "\n".join(
        f"- **{s['name']}**: {s['backstory']}\n  Personality: {s['personality']}"
        for s in speakers
    )


def lang_name(code):
    return {"fr": "French", "en": "English"}.get(code, code)


def build_outline_prompt(briefing, context, speakers, num_segments, language):
    return f"""You are an AI assistant specialized in creating podcast outlines. The outline will be used to generate the podcast transcript.

Briefing:
<briefing>
{briefing}
</briefing>

Context (source material for this episode):
<context>
{context}
</context>

Speakers:
{speakers_block(speakers)}

IMPORTANT LANGUAGE INSTRUCTION: Generate ALL content (segment names, descriptions, every word) in {lang_name(language)}. Do not use another language unless the source itself contains foreign terms.

Create exactly {num_segments} segments covering the full scope of the briefing.
- Each segment: a catchy, informative name + a detailed description (key points and questions to discuss, drawn from the context). The transcript writer uses the description to design the dialogue.
- Match content to speaker expertise.
- Segments flow logically. Do not reintroduce speakers each segment — segments are just topic markers.
- First segment = introduction. Last segment = conclusion / wrap-up.
- Tag each segment "size": "short", "medium", or "long".

Return ONLY a JSON object with a "segments" key:
{{"segments":[{{"name":"...","description":"...","size":"short"}}]}}"""


def build_transcript_prompt(briefing, context, speakers, outline, transcript_so_far,
                            segment, is_final, turns, language, speaker_names):
    final_note = ("\nThis is the FINAL segment: wrap up the conversation and land a conclusion.\n"
                  if is_final else "")
    sofar = (f"\nTranscript so far (continue naturally, do NOT repeat it):\n<transcript>\n{transcript_so_far}\n</transcript>\n"
             if transcript_so_far else "")
    return f"""You are writing the transcript for ONE segment of a podcast. Other passes handle the other segments — stay inside this segment.

Briefing:
<briefing>
{briefing}
</briefing>

Context (source material):
<context>
{context}
</context>

Speakers:
{speakers_block(speakers)}

IMPORTANT LANGUAGE INSTRUCTION: Write ALL dialogue in {lang_name(language)}. Do not switch languages except to quote specific foreign terms.

Full outline (for continuity):
<outline>
{outline}
</outline>
{sofar}
Write dialogue for THIS segment ONLY:
<segment>
{segment}
</segment>
{final_note}
Format requirements (strict):
- Use the real speaker names: {', '.join(speaker_names)}.
- Choose who speaks by personality, backstory, and topic fit.
- At least {turns} turns between speakers.
- Balanced exchanges, no long monologues. Natural transitions. Conversational, not a lecture.
- Do not reintroduce speakers/topics; the segment is just a topic marker.

Return ONLY a JSON object with a "transcript" key:
{{"transcript":[{{"speaker":"<real name>","dialogue":"..."}}]}}"""


def slugify(s):
    s = re.sub(r"[^\w\s-]", "", s).strip().lower()
    return re.sub(r"[\s_]+", "-", s)[:60]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True, help="Path to source note/file")
    ap.add_argument("--profile", default=None)
    ap.add_argument("--lang", default="fr")
    ap.add_argument("--out", default=".")
    ap.add_argument("--model", default="qwen3:30b-a3b-instruct-2507-q4_K_M")
    ap.add_argument("--briefing", default="", help="Extra one-line steer merged into the profile briefing")
    ap.add_argument("--title", default="", help="Short title for filename + header")
    args = ap.parse_args()

    if not os.path.isfile(args.source):
        die(f"Source not found: {args.source}")
    with open(args.source, encoding="utf-8") as f:
        context = f.read()
    if not context.strip():
        die("Source is empty")

    with open(os.path.join(HERE, "profiles", "episodes.json"), encoding="utf-8") as f:
        episodes = json.load(f)
    with open(os.path.join(HERE, "profiles", "speakers.json"), encoding="utf-8") as f:
        speaker_cfgs = json.load(f)["speaker_configs"]

    prof_name = args.profile or episodes.get("default", "solo_brief")
    if prof_name not in episodes["profiles"]:
        die(f"Unknown profile '{prof_name}'. Available: {list(episodes['profiles'])}")
    prof = episodes["profiles"][prof_name]
    speakers = speaker_cfgs[prof["speaker_config"]]
    speaker_names = [s["name"] for s in speakers]
    num_segments = prof["num_segments"]
    turns = prof.get("turns", 6)
    briefing = prof["default_briefing"] + (f"\n\nAdditional steer: {args.briefing}" if args.briefing else "")

    # Stage 1 — outline
    outline_raw = ollama_chat(args.model,
        build_outline_prompt(briefing, context, speakers, num_segments, args.lang),
        force_json=True)
    segments = parse_json_obj(outline_raw, "segments")
    outline_str = json.dumps({"segments": segments}, ensure_ascii=False)

    # Stage 2 — per-segment transcript, carrying running transcript
    rendered = []          # list of (segment_name, [(speaker, dialogue), ...])
    transcript_flat = ""   # running plain text fed back into each call
    for i, seg in enumerate(segments):
        is_final = (i == len(segments) - 1)
        raw = ollama_chat(args.model,
            build_transcript_prompt(briefing, context, speakers, outline_str,
                                    transcript_flat, json.dumps(seg, ensure_ascii=False),
                                    is_final, turns, args.lang, speaker_names),
            force_json=True)
        turns_list = parse_json_obj(raw, "transcript")
        rendered.append((seg.get("name", f"Segment {i+1}"), turns_list))
        for t in turns_list:
            transcript_flat += f"{t.get('speaker','')}: {t.get('dialogue','')}\n"

    # Render markdown
    title = args.title or os.path.splitext(os.path.basename(args.source))[0]
    md = [f"# {title}",
          f"> engine: qwen (local, private) · Profile: {prof_name} · Langue: {args.lang} · "
          f"Modèle: {args.model} · Source: {os.path.basename(args.source)}", ""]
    for name, turns_list in rendered:
        md.append(f"## {name}")
        for t in turns_list:
            md.append(f"**{t.get('speaker','')}:** {t.get('dialogue','')}")
        md.append("")
    script_md = "\n".join(md)

    date = datetime.date.today().strftime("%Y%m%d")
    fname = f"{date} - {slugify(title)}.md"
    os.makedirs(args.out, exist_ok=True)
    out_path = os.path.join(args.out, fname)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(script_md)

    words = len(re.findall(r"\w+", script_md))
    # METADATA ONLY — no source, no script content crosses back to the orchestrator
    print(json.dumps({
        "ok": True, "path": out_path, "profile": prof_name, "lang": args.lang,
        "model": args.model, "segments": len(segments),
        "segment_names": [s.get("name") for s in segments],
        "words": words, "read_min": round(words / 150),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
