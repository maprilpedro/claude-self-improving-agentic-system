#!/usr/bin/env python3
"""Keep active project-memory files Read-able in one shot; shard the archive by ISO week.

The active project-memory files (`.claude/memory/project_*.md`) are loaded at every
session start. Past ~25K tokens they truncate on read and the durable reference at the
bottom gets silently cut (the 2026-07-01 incident). This tool enforces a token cap by
moving the OLDEST event blocks into weekly archive shards, and keeps a generated index
so old context is still findable by grep. Never deletes — moves only.

Structure per project memory file `<stem>.md`:
  <stem>.md                          active: RESUME + recent events + living reference
  <stem>_ARCHIVE_<ISOyear>-W<wk>.md  one shard per ISO week of archived events
  <stem>_ARCHIVE_reference.md        long-form reference sections moved out (non-dated)
  <stem>_ARCHIVE_misc-pre-...md      undated / pre-structured blocks (catch-all)
  <stem>_ARCHIVE_INDEX.md            GENERATED map week->file->date-range->topics

Modes:
  --check <memfile>       print token estimate; exit 1 if over CAP. Read-only.
  --dry-run <memfile>     show what active-file archiving would move. No writes.
  <memfile>               archive event blocks older than RETENTION_DAYS until under TARGET.
  --migrate <archivefile> one-time: shard an existing monolithic _ARCHIVE.md by week.
  --split <memfile>       split any weekly shard over the cap into lettered parts (W25 -> W25a/b).
  --reindex <memfile>     rebuild the _ARCHIVE_INDEX.md from existing shards.

Archiving and migration auto-split oversized weeks; --split is the standalone pass.

Token estimate = bytes / 4 (same proxy the dashboard uses). stdlib only.
"""
import sys, re, os, glob, datetime, pathlib

CAP_TOKENS = 20_000       # archive if the active file is over this
TARGET_TOKENS = 18_000    # stop archiving once back under this
RETENTION_DAYS = 14       # keep event blocks at least this recent in the active file
TODAY = datetime.date.today()

DATE_RE = re.compile(r"20\d\d-\d\d-\d\d")
BQ_HEADER = re.compile(r"^> #{2,3} ")     # blockquoted event header  "> ### ..."
REF_HEADER = re.compile(r"^## ")          # non-blockquote living-reference section
BANNER = re.compile(r"📦|^> \*\*")         # archive banners / scaffolding, not content


def tokens(text):
    return len(text.encode("utf-8")) // 4


MONTHS = {m.lower(): i for i, m in enumerate(
    ["January", "February", "March", "April", "May", "June", "July", "August",
     "September", "October", "November", "December"], 1)}
PROSE_RE = re.compile(r"\b(" + "|".join(MONTHS) + r")\s+(\d{1,2})(?:,?\s+(\d{4}))?\b", re.I)


def block_date(line):
    """Date of a block header. Handles ISO (2026-06-30) and prose (April 22, 2026 /
    May 6). Prose year defaults to 2026 (all legacy archive events are 2026)."""
    m = DATE_RE.search(line)
    if m:
        try:
            return datetime.date.fromisoformat(m.group())
        except ValueError:
            pass
    pm = PROSE_RE.search(line)
    if pm:
        try:
            return datetime.date(int(pm.group(3) or 2026), MONTHS[pm.group(1).lower()], int(pm.group(2)))
        except ValueError:
            return None
    return None


def shard_name(stem, d):
    iso = d.isocalendar()
    return f"{stem}_ARCHIVE_{iso[0]}-W{iso[1]:02d}.md"


def split_active(lines):
    """Return (preamble, event_blocks, living_ref).
    event_blocks = list of (block_lines, date|None, is_resume). Living ref = from the
    first non-blockquote '## ' header onward, kept intact."""
    live_start = next((i for i, l in enumerate(lines) if REF_HEADER.match(l)), len(lines))
    first_ev = next((i for i, l in enumerate(lines[:live_start]) if BQ_HEADER.match(l)), live_start)
    preamble = lines[:first_ev]
    region = lines[first_ev:live_start]
    living = lines[live_start:]
    blocks, cur = [], []
    for l in region:
        if BQ_HEADER.match(l) and cur:
            blocks.append(cur); cur = [l]
        else:
            cur.append(l)
    if cur:
        blocks.append(cur)
    out = []
    for b in blocks:
        is_resume = "RESUME" in b[0]
        out.append((b, block_date(b[0]), is_resume))
    return preamble, out, living


def append_block(path, block_lines, header=None):
    new = not os.path.exists(path)
    with open(path, "a") as f:
        if new and header:
            f.write(header + "\n\n")
        f.write("\n".join(block_lines).rstrip() + "\n\n")


def rebuild_index(memfile):
    p = pathlib.Path(memfile)
    stem = p.stem
    d = p.parent
    shards = sorted(g for g in glob.glob(str(d / f"{stem}_ARCHIVE_*.md"))
                    if not g.endswith("_INDEX.md"))
    def is_banner(h):
        core = h.lstrip("> #").strip()
        return bool(BANNER.search(h)) or core.startswith(
            ("Archive shard", "Long-form reference", "Undated"))

    def clean(h):
        return re.sub(r"^[>#\s🟢🔴🔵🟡🚨🆕📊📐🔧🤝📣🌟🚀🔑▶️📦]+", "", h)[:55]

    rows = []
    for s in shards:
        txt = pathlib.Path(s).read_text()
        blocks, cur = [], []
        for l in txt.split("\n"):
            if (BQ_HEADER.match(l) or REF_HEADER.match(l)) and cur:
                blocks.append(cur); cur = [l]
            else:
                cur.append(l)
        if cur:
            blocks.append(cur)
        heads = [b[0] for b in blocks if b and not is_banner(b[0])]
        dates = sorted(d for d in (block_date(h) for h in heads) if d)
        rng = f"{dates[0]} → {dates[-1]}" if dates else "—"
        topic = "; ".join(clean(h) for h in heads[:5]) or "—"
        rows.append((os.path.basename(s), rng, tokens(txt), topic))
    idx = pathlib.Path(d / f"{stem}_ARCHIVE_INDEX.md")
    lines = [f"# Archive index — {stem}", "",
             "> GENERATED by `scripts/archive_memory.py` — do not hand-edit. Archives are"
             " load-on-demand (grep, never Read whole). Find the shard by date/topic here,"
             " then `rtk proxy grep` it.", "",
             f"_Last rebuilt {TODAY.isoformat()}. {len(shards)} shard(s)._", "",
             "| Shard file | Dates | ~tokens | Topics (first blocks) |",
             "|---|---|---|---|"]
    for name, rng, tok, topic in rows:
        lines.append(f"| `{name}` | {rng} | {tok//1000}K | {topic} |")
    idx.write_text("\n".join(lines) + "\n")
    return idx, len(shards)


def split_oversized(memfile):
    """Split any un-lettered weekly shard over CAP into lettered parts (W25 -> W25a/W25b),
    each under TARGET. Blocks are kept whole. Returns [(week, n_parts), ...]."""
    p = pathlib.Path(memfile)
    stem = p.stem
    d = p.parent
    week_re = re.compile(re.escape(stem) + r"_ARCHIVE_(\d+-W\d+)\.md$")
    done = []
    for s in sorted(glob.glob(str(d / f"{stem}_ARCHIVE_*.md"))):
        if s.endswith("_INDEX.md"):
            continue
        m = week_re.search(os.path.basename(s))
        if not m:                                  # only un-lettered week shards
            continue
        txt = pathlib.Path(s).read_text()
        if tokens(txt) <= CAP_TOKENS:
            continue
        blocks, cur = [], []
        for l in txt.split("\n"):
            if (BQ_HEADER.match(l) or REF_HEADER.match(l)) and cur:
                blocks.append(cur); cur = [l]
            else:
                cur.append(l)
        if cur:
            blocks.append(cur)
        if blocks and "Archive shard" in blocks[0][0]:   # drop old banner, re-added per part
            blocks = blocks[1:]
        label = m.group(1)
        parts = [[]]
        for b in blocks:
            cur_sz = tokens("\n".join(x for bb in parts[-1] for x in bb))
            if parts[-1] and cur_sz + tokens("\n".join(b)) > TARGET_TOKENS:
                parts.append([])
            parts[-1].append(b)
        for i, part in enumerate(parts):
            letter = chr(ord("a") + i)
            hdr = f"> ## Archive shard — {stem} — {label}{letter} (split {i + 1}/{len(parts)} for size)"
            body = "\n".join(x for b in part for x in b).rstrip()
            (d / f"{stem}_ARCHIVE_{label}{letter}.md").write_text(hdr + "\n\n" + body + "\n")
        pathlib.Path(s).unlink()
        done.append((label, len(parts)))
    return done


def do_check(memfile):
    t = tokens(pathlib.Path(memfile).read_text())
    over = t > CAP_TOKENS
    print(f"{os.path.basename(memfile)}: ~{t//1000}K tokens (cap {CAP_TOKENS//1000}K) "
          f"{'OVER — archive due' if over else 'ok'}")
    return 1 if over else 0


def do_archive(memfile, dry):
    p = pathlib.Path(memfile)
    stem = p.stem
    lines = p.read_text().split("\n")
    preamble, blocks, living = split_active(lines)
    keep, moved = [], []
    cutoff = TODAY - datetime.timedelta(days=RETENTION_DAYS)

    def assemble(kept):
        return "\n".join(preamble + [x for b in kept for x in b[0]] + living)

    # move oldest datable non-recent blocks until under TARGET (oldest first)
    datable = sorted([b for b in blocks if b[1] and not b[2] and b[1] < cutoff],
                     key=lambda b: b[1])
    recent = [b for b in blocks if b not in datable]
    kept = list(blocks)
    for b in datable:
        if tokens(assemble(kept)) <= TARGET_TOKENS:
            break
        kept.remove(b); moved.append(b)
    keep = kept

    print(f"{os.path.basename(memfile)}: {tokens(p.read_text())//1000}K -> "
          f"{tokens(assemble(keep))//1000}K tokens; moving {len(moved)} block(s)")
    for b in moved:
        print(f"  -> W{b[1].isocalendar()[1]:02d}  {b[0][0][:80]}")
    if dry or not moved:
        return
    for b in moved:
        append_block(str(p.parent / shard_name(stem, b[1])), b[0],
                     header=f"> ## Archive shard — {stem} — ISO week {b[1].isocalendar()[0]}-W{b[1].isocalendar()[1]:02d}")
    p.write_text(assemble(keep))
    split_oversized(memfile)
    rebuild_index(memfile)


def do_migrate(archivefile):
    """Shard a monolithic _ARCHIVE.md by ISO week. Ref sections -> _reference, undated -> misc."""
    p = pathlib.Path(archivefile)
    # stem = drop the trailing _ARCHIVE
    stem = re.sub(r"_ARCHIVE$", "", p.stem)
    lines = p.read_text().split("\n")
    # split into blocks at any header (blockquote event OR non-bq ref section)
    blocks, cur = [], []
    for l in lines:
        if (BQ_HEADER.match(l) or REF_HEADER.match(l)) and cur:
            blocks.append(cur); cur = [l]
        else:
            cur.append(l)
    if cur:
        blocks.append(cur)
    routed = {"reference": [], "misc": [], "shards": {}}
    for b in blocks:
        h = b[0]
        d = block_date(h)
        if d and not BANNER.search(h):
            routed["shards"].setdefault(shard_name(stem, d), []).append(b)
        elif REF_HEADER.match(h):        # dateless '## ' section = true reference
            routed["reference"].append(b)
        else:
            routed["misc"].append(b)     # banners, undated, preamble
    print(f"MIGRATE {p.name}: {len(blocks)} blocks -> "
          f"{len(routed['shards'])} weekly shards, {len(routed['reference'])} ref, "
          f"{len(routed['misc'])} misc")
    for name in sorted(routed["shards"]):
        print(f"  {name}: {len(routed['shards'][name])} block(s)")
    if "--execute" not in sys.argv:
        print("(dry run — pass --execute to write)")
        return
    d = p.parent
    for name, bs in routed["shards"].items():
        for b in bs:
            append_block(str(d / name), b,
                         header=f"> ## Archive shard — {stem} — {name.split('_ARCHIVE_')[1][:-3]}")
    for b in routed["reference"]:
        append_block(str(d / f"{stem}_ARCHIVE_reference.md"), b,
                     header=f"> ## Long-form reference sections moved out of {stem}.md (load on demand)")
    misc_body = [x for b in routed["misc"] for x in b if x.strip() and not BANNER.search(x)]
    if any(l.strip() for l in misc_body):
        append_block(str(d / f"{stem}_ARCHIVE_misc-pre-2026-06.md"),
                     [x for b in routed["misc"] for x in b],
                     header=f"> ## Undated / pre-structured blocks from {stem} (catch-all)")
    p.unlink()  # monolith fully distributed
    sp = split_oversized(str(d / f"{stem}.md"))
    if sp:
        print("split oversized weeks:", sp)
    idx, n = rebuild_index(str(d / f"{stem}.md"))
    print(f"wrote {n} shards + {idx.name}; removed {p.name}")


def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__); sys.exit(2)
    if a[0] == "--check":
        sys.exit(do_check(a[1]))
    if a[0] == "--dry-run":
        do_archive(a[1], dry=True); return
    if a[0] == "--migrate":
        do_migrate(a[1]); return
    if a[0] == "--reindex":
        idx, n = rebuild_index(a[1]); print(f"rebuilt {idx.name} ({n} shards)"); return
    if a[0] == "--split":
        sp = split_oversized(a[1]); rebuild_index(a[1])
        print(f"split oversized weeks: {sp or 'none'}"); return
    do_archive(a[0], dry=False)


if __name__ == "__main__":
    main()
