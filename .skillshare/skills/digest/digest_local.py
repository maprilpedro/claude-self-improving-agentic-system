#!/usr/bin/env python3
"""
Local digest generator — applies a reusable PM extraction template to a source,
entirely against a local Ollama model. The orchestrator (Claude) never reads the
source or the output: this prints ONLY metadata, so sensitive Adobe-internal
content never enters Claude's context / never leaves the mac.

Usage:
  python3 digest_local.py --source <path> [--template exec] [--lang fr]
                          [--out <dir>] [--model qwen3:30b-a3b-instruct-2507-q4_K_M]
                          [--title "Short Title"]

Templates live in templates.json next to this file.
Writes a markdown note to --out and prints a one-line JSON metadata blob.
"""

import argparse, json, os, sys, datetime, re, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
OLLAMA = os.environ.get("OLLAMA_HOST", "http://localhost:11434") + "/api/chat"
NUM_CTX = 65536  # 64K — safe on 48GB (weights ~18GB + KV ~8GB); Qwen3 ceiling is 262K


def die(msg):
    print(json.dumps({"ok": False, "error": msg}))
    sys.exit(1)


def ollama_chat(model, prompt, temperature=0.4):
    body = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
        "options": {"temperature": temperature, "num_ctx": NUM_CTX},
    }
    req = urllib.request.Request(
        OLLAMA, data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=900) as r:
            return json.loads(r.read().decode("utf-8"))["message"]["content"]
    except Exception as e:
        die(f"Ollama call failed: {e}")


def lang_name(code):
    return {"fr": "French", "en": "English"}.get(code, code)


def slugify(s):
    s = re.sub(r"[^\w\s-]", "", s).strip().lower()
    return re.sub(r"[\s_]+", "-", s)[:60]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True)
    ap.add_argument("--template", default=None)
    ap.add_argument("--lang", default="en")
    ap.add_argument("--out", default=".")
    ap.add_argument("--model", default="qwen3:30b-a3b-instruct-2507-q4_K_M")
    ap.add_argument("--title", default="")
    args = ap.parse_args()

    if not os.path.isfile(args.source):
        die(f"Source not found: {args.source}")
    with open(args.source, encoding="utf-8") as f:
        context = f.read()
    if not context.strip():
        die("Source is empty")

    with open(os.path.join(HERE, "templates.json"), encoding="utf-8") as f:
        cfg = json.load(f)
    tname = args.template or cfg.get("default", "exec")
    if tname not in cfg["templates"]:
        die(f"Unknown template '{tname}'. Available: {list(cfg['templates'])}")
    tmpl = cfg["templates"][tname]

    prompt = f"""You apply a fixed extraction template to a source document and return ONLY the structured result.

TASK:
{tmpl['prompt']}

LANGUAGE: Write the entire output in {lang_name(args.lang)}. Do not switch languages except to quote specific foreign terms.

SOURCE:
<source>
{context}
</source>

Return only the structured output in markdown. No preamble, no explanation of what you did."""

    result = ollama_chat(args.model, prompt)

    title = args.title or os.path.splitext(os.path.basename(args.source))[0]
    header = (f"# {title} — {tmpl['label']}\n"
              f"> engine: qwen (local, private) · Template: {tname} · Langue: {args.lang} · "
              f"Modèle: {args.model} · Source: {os.path.basename(args.source)}\n\n")
    note = header + result.strip() + "\n"

    date = datetime.date.today().strftime("%Y%m%d")
    fname = f"{date} - {slugify(title)} - {tname}.md"
    os.makedirs(args.out, exist_ok=True)
    out_path = os.path.join(args.out, fname)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(note)

    words = len(re.findall(r"\w+", result))
    # METADATA ONLY — source and output never cross back to the orchestrator
    print(json.dumps({
        "ok": True, "path": out_path, "template": tname, "label": tmpl["label"],
        "lang": args.lang, "model": args.model, "words": words,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
