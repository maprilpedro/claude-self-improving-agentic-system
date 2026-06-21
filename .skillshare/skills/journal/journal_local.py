#!/usr/bin/env python3
"""
Local end-of-day journal — rolls up the notes Pedro touched today into a private
journal entry, entirely against a local Ollama model. The orchestrator (Claude)
never reads the source notes or the entry: prints ONLY metadata, so sensitive
Adobe-internal content never enters Claude's context / never leaves the mac.

Default: scan a root folder for .md files modified in the last --hours, summarise
them into a structured journal entry. Or pass explicit --sources.

Usage:
  python3 journal_local.py [--root <dir>] [--sources "a.md,b.md"] [--hours 24]
                           [--lang en] [--out <dir>] [--model ...] [--date YYYY-MM-DD]
"""

import argparse, json, os, sys, datetime, re, time, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
OLLAMA = os.environ.get("OLLAMA_HOST", "http://localhost:11434") + "/api/chat"
NUM_CTX = 65536  # 64K — safe on 48GB (weights ~18GB + KV ~8GB); Qwen3 ceiling is 262K

VAULT = ("/Users/pedrofer/Library/CloudStorage/GoogleDrive-maprilpedro@gmail.com/"
         "My Drive/ObsidianVault/020 Professional/Adobe/Projects/2026")
DEFAULT_ROOT = VAULT  # whole 2026 tree — his recent work lives in project folders, not just Meeting Notes
# Folders to skip when scanning (this skill's own outputs + sibling generators)
EXCLUDE_DIRS = {"Journal", "Digests", "Podcast Scripts", ".obsidian", ".trash"}


def die(msg):
    print(json.dumps({"ok": False, "error": msg}))
    sys.exit(1)


def ollama_chat(model, prompt, temperature=0.4):
    body = {"model": model, "messages": [{"role": "user", "content": prompt}],
            "stream": False, "options": {"temperature": temperature, "num_ctx": NUM_CTX}}
    req = urllib.request.Request(OLLAMA, data=json.dumps(body).encode("utf-8"),
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=1200) as r:
            return json.loads(r.read().decode("utf-8"))["message"]["content"]
    except Exception as e:
        die(f"Ollama call failed: {e}")


def lang_name(code):
    return {"fr": "French", "en": "English"}.get(code, code)


def resolve_period(period):
    """Return (start_ts, end_ts, label, fname, period_word) for a named window."""
    now = datetime.datetime.now()
    td = datetime.timedelta
    today0 = now.replace(hour=0, minute=0, second=0, microsecond=0)
    if period == "today":
        start, end = today0, today0 + td(days=1)
        label = start.strftime("%Y-%m-%d"); fname = label; word = "today"
    elif period == "yesterday":
        start, end = today0 - td(days=1), today0
        label = start.strftime("%Y-%m-%d"); fname = label; word = "yesterday"
    elif period == "weekly":
        start = today0 - td(days=today0.weekday())
        end = start + td(days=7)
        iso = start.isocalendar()
        rng = f"{start.strftime('%b %d')}-{(end - td(days=1)).strftime('%b %d')}"
        label = f"{iso[0]}-W{iso[1]:02d} ({rng})"; fname = f"{iso[0]}-W{iso[1]:02d}"
        word = "this week"
    elif period == "lastweek":
        start = today0 - td(days=today0.weekday()) - td(days=7)
        end = start + td(days=7)
        iso = start.isocalendar()
        rng = f"{start.strftime('%b %d')}-{(end - td(days=1)).strftime('%b %d')}"
        label = f"{iso[0]}-W{iso[1]:02d} ({rng})"; fname = f"{iso[0]}-W{iso[1]:02d}"
        word = "last week"
    else:
        die(f"Unknown period '{period}'. Use today | yesterday | weekly | lastweek")
    return start.timestamp(), end.timestamp(), label, fname, word


def collect_window(root, start_ts, end_ts):
    if not os.path.isdir(root):
        die(f"Root not found: {root}")
    hits = []
    for dirpath, dirnames, files in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
        for fn in files:
            if fn.endswith(".md"):
                p = os.path.join(dirpath, fn)
                try:
                    if start_ts <= os.path.getmtime(p) < end_ts:
                        hits.append(p)
                except OSError:
                    pass
    return sorted(hits)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--period", default="today",
                    choices=["today", "yesterday", "weekly", "lastweek"])
    ap.add_argument("--root", default=DEFAULT_ROOT)
    ap.add_argument("--sources", default="", help="Comma-separated explicit file paths (overrides period scan)")
    ap.add_argument("--lang", default="en")
    ap.add_argument("--out", default=os.path.join(VAULT, "Journal"))
    ap.add_argument("--model", default="qwen3:30b-a3b-instruct-2507-q4_K_M")
    ap.add_argument("--list-only", action="store_true",
                    help="Print the period's file selection as JSON and exit (no generation). "
                         "Used by the Claude engine so both engines select identical files.")
    args = ap.parse_args()

    start_ts, end_ts, label, fname, period_word = resolve_period(args.period)
    if args.sources.strip():
        paths = [p.strip() for p in args.sources.split(",") if p.strip()]
        paths = [p for p in paths if os.path.isfile(p)]
    else:
        paths = collect_window(args.root, start_ts, end_ts)

    if args.list_only:
        print(json.dumps({"ok": True, "period": args.period, "label": label,
                          "fname": fname, "count": len(paths), "files": paths},
                         ensure_ascii=False))
        return

    if not paths:
        die(f"No .md notes touched {period_word} ({label}) under {args.root}. "
            f"Nothing to journal — or pass --sources explicitly.")

    # Read notes, capping any single note so one map call always fits the ctx window
    PER_NOTE_CHARS = 200000       # ~50K tokens — fits any single note in the 64K window (biggest vault note ~37K tok)
    SINGLE_PASS_CHARS = 180000    # ~45K tokens: below this, one pass; above, map-reduce
    notes, truncated = [], []
    for p in paths:
        try:
            with open(p, encoding="utf-8") as f:
                txt = f.read()
        except Exception:
            continue
        if len(txt) > PER_NOTE_CHARS:
            txt = txt[:PER_NOTE_CHARS]
            truncated.append(os.path.basename(p))
        notes.append((os.path.basename(p), txt))
    if not notes:
        die("No readable notes in the selected set")

    total_chars = sum(len(t) for _, t in notes)
    if total_chars <= SINGLE_PASS_CHARS:
        strategy = "single-pass"
        context = "\n\n".join(f'<note name="{n}">\n{t}\n</note>' for n, t in notes)
    else:
        # MAP: condense each note within budget, then REDUCE into the journal
        strategy = "map-reduce"
        condensed = []
        for n, t in notes:
            mp = (f"Condense the following note into at most 10 bullets capturing only the "
                  f"substance useful for a work journal: what happened, decisions vs proposals, "
                  f"open follow-ups, named people. Write in {lang_name(args.lang)}. No preamble.\n\n"
                  f'<note name="{n}">\n{t}\n</note>')
            condensed.append(f"### {n}\n{ollama_chat(args.model, mp).strip()}")
        context = "\n\n".join(condensed)

    span_n = "3 to 6" if args.period in ("today", "yesterday") else "5 to 9"
    prompt = f"""You are writing Pedro's private work journal for {period_word}, built from the notes he touched ({label}): meetings, 1-1s, working sessions. Pedro is a Director of Product Management at Adobe working toward Senior Director.

Write the entry in {lang_name(args.lang)}, in this exact structure, plain language, no preamble:

## What happened
{span_n} bullets — the real substance of {period_word} across the notes. For a week, group by theme or thread, not by single meeting.

## Decisions & positions
What got decided vs merely proposed. Do NOT promote a proposal to a decision — mark proposals as such. Name the owner where known.

## Open follow-ups
Forward-looking items only (not a log of what already happened). Checkbox format: '- [ ] <action> — owner: <name or unassigned> — due: <date or no date>'.

## So-what
1 to 3 lines: what {period_word} changed for Pedro's positioning toward Senior Director (visibility, ownership, narrative). Position over merit — good work alone does not move him up.

NOTES ({period_word}):
<notes>
{context}
</notes>

Return only the journal entry in markdown."""

    result = ollama_chat(args.model, prompt)

    header = (f"# Journal — {label}\n"
              f"> engine: qwen (local, private) · {args.period} · Langue: {args.lang} · "
              f"Modèle: {args.model} · {len(notes)} note(s)\n\n")
    note = header + result.strip() + "\n"

    os.makedirs(args.out, exist_ok=True)
    out_path = os.path.join(args.out, f"{fname}.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(note)

    words = len(re.findall(r"\w+", result))
    # METADATA ONLY — note contents never cross back to the orchestrator
    print(json.dumps({
        "ok": True, "path": out_path, "period": args.period, "label": label,
        "lang": args.lang, "model": args.model, "sources_count": len(notes),
        "sources": [n for n, _ in notes], "strategy": strategy,
        "truncated_notes": truncated, "words": words,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
