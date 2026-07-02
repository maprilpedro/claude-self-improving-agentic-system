#!/usr/bin/env python3
"""Retrieval audit (P6, 2026-07-02): which knowledge entries actually get used?

Capture was never the system's problem — retrieval is. This reports, per knowledge
entry, whether it is ever cited from working memory (`.claude/memory/**` including
archive shards, `.claude/state*.md`). Cited = the entry's title (or an unambiguous
prefix) appears in a memory file, [[wiki-style]] or plain.

Output: the never-cited list, oldest-first — the /system-review Step 4 retrieval
audit reads this. Flag-only: entries are candidates for Pedro's judgment (still
believed → keep; dead weight → mark outdated with reasoning). Never auto-delete.

Usage: retrieval_audit.py [--all]   (--all also prints cited entries with counts)
"""
import pathlib, re, sys, unicodedata

ROOT = pathlib.Path(__file__).resolve().parent.parent
KNOW = ROOT / "knowledge"
SPLIT_FOLDERS = ["leadership", "ai-product", "patterns"]
SINGLE_FILES = ["domain/README.md", "interpersonal/README.md",
                "false-beliefs/catalog.md", "tools/decision-matrix.md"]


def norm(s):
    s = unicodedata.normalize("NFKD", s)
    s = re.sub(r"[—–]", "-", s)          # em/en dash -> hyphen
    s = re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()
    return s


def entries():
    out = []  # (folder, title, where)
    for f in SPLIT_FOLDERS:
        for p in sorted((KNOW / f).glob("*.md")):
            if p.name == "README.md":
                continue
            first = p.read_text().split("\n", 1)[0]
            if first.startswith("# "):
                out.append((f, first[2:].strip(), p.name))
    for rel in SINGLE_FILES:
        p = KNOW / rel
        if not p.exists():
            continue
        for l in p.read_text().split("\n"):
            m = re.match(r"^###? (.+)$", l)
            if m and not m.group(1).startswith(("FB-", "Sources", "Folder", "Routing", "Access")) \
               and m.group(1).strip() not in ("Why This Matters", "How to Use This Catalog", "Format"):
                out.append((rel.split("/")[0], m.group(1).strip(), rel))
    return out


def memory_corpus():
    texts = []
    for p in (ROOT / ".claude" / "memory").glob("*.md"):
        texts.append(p.read_text())
    for p in (ROOT / ".claude").glob("state*.md"):
        texts.append(p.read_text())
    return norm("\n".join(texts))


def main():
    corpus = memory_corpus()
    never, cited = [], []
    for folder, title, where in entries():
        key = norm(title)
        # unambiguous prefix: first 6 normalized words (titles are long; cites shorten)
        probe = " ".join(key.split()[:6])
        n = corpus.count(probe) if len(probe) > 12 else corpus.count(key)
        (cited if n else never).append((folder, title, n))
    print(f"knowledge entries scanned: {len(never) + len(cited)}; "
          f"cited from memory: {len(cited)}; never cited: {len(never)}\n")
    print("## Never cited from working memory (retrieval-audit candidates)")
    for folder, title, _ in never:
        print(f"  [{folder:14}] {title}")
    if "--all" in sys.argv:
        print("\n## Cited")
        for folder, title, n in sorted(cited, key=lambda x: -x[2]):
            print(f"  {n:3}x [{folder:14}] {title}")


if __name__ == "__main__":
    main()
