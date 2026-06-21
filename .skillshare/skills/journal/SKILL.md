---
name: journal
description: Build Pedro's work journal — roll up the vault notes he touched in a period (today/yesterday/weekly/lastweek) into one structured entry: what happened, decisions vs proposals, open follow-ups, and the Senior-Director so-what. Default engine = Claude (fuses fresh vault reads + Pedro's project memory + this session). Switch to a fully-local Qwen/Ollama engine for sensitive content with --qwen or words like "local"/"privé"/"sensible". Use whenever Pedro says "journal", "end of day", "wrap up my day", "what happened today", "daily/weekly rollup", or runs /journal. The entry bakes in Pedro's rules (decisions ≠ proposals, forward-looking follow-ups, position-over-merit lens).
disable-model-invocation: true
---

# Journal

End-of-day rollup. Finds the notes Pedro touched today and distills them into one private journal entry, so the day is captured without re-reading everything. Structure is fixed:

- **What happened** — 3-6 bullets, the day's substance
- **Decisions & positions** — decided vs proposed (does NOT promote proposals)
- **Open follow-ups** — forward-looking only, checkbox + owner + due
- **So-what** — what today changed for the Director→Senior-Director positioning

## Periods (the invocation)
`/journal <period>` — four presets, default `today`:

| Invocation | Window | Output file |
|---|---|---|
| `/journal` or `/journal today` | midnight today → now | `2026/Journal/<YYYY-MM-DD>.md` |
| `/journal yesterday` | the full previous day | `2026/Journal/<YYYY-MM-DD>.md` |
| `/journal weekly` | current week, Monday → now | `2026/Journal/<YYYY>-W<NN>.md` |
| `/journal lastweek` | the previous Mon–Sun week | `2026/Journal/<YYYY>-W<NN>.md` |

Maps to `journal_local.py --period <today|yesterday|weekly|lastweek>`. Weekly entries group by theme/thread, not by single meeting.

## Defaults (Pedro)
- **Language: English by default**, `--lang fr` (or any) to override.
- **Source:** `.md` files whose modified-time falls inside the period window, scanned across the whole `2026/` tree (the generator's own output folders — Journal/Digests/Podcast Scripts — are excluded). Bypass scanning with explicit `--sources "a.md,b.md"`.
- **Output:** see table; re-running the same period overwrites that file.
- **⚠️ Google Drive caveat:** the vault lives in Google Drive CloudStorage — a file's modified-time can reflect a *sync* event, not Pedro's edit. If a period pulls in too many/few notes, fall back to `--sources`, and always tell Pedro which notes got picked up.

## Engine (claude ⇄ qwen) — transparent switch

Same command, same output file + structure either way. Pick the engine:
- **claude** (default) — richest, current.
- **qwen** — when Pedro adds `--qwen` / `--engine qwen`, or says "local" / "privé" / "sensible".

| Engine | Brings | Cost |
|---|---|---|
| **claude** (default) | This session + project memory + synthesis, on top of fresh vault reads | Content goes to Anthropic |
| **qwen** | Fresh vault reads only, 100% local | No Claude context, lower quality |

Every output's header line states which engine produced it (`engine: claude` / `engine: qwen`) so the difference is never hidden.

### claude engine (default) — read fresh, fuse, write
1. Get the period's file selection by running the script in list-only mode (so both engines pick the SAME files):
   ```bash
   python3 <skill-dir>/journal_local.py --period <today|yesterday|weekly|lastweek> --list-only
   ```
   (or use `--sources "a.md,b.md"` if Pedro named specific notes.)
2. **Read those files live** — never journal from memory alone. Fresh reads = up to date.
3. **Fuse** the fresh notes with (a) Pedro's project memory and (b) what happened in THIS session (events not yet written to a note). Where memory and a fresh note disagree, the note wins for facts — flag the discrepancy.
4. Write the 4-section entry yourself (Claude quality), header `> engine: claude · <period> · <N> notes`, save to the period's output file.
5. If many notes (a week), group What-happened by theme/thread, not per meeting.

### qwen engine (`--qwen`) — local, private, metadata only
Launch the standalone builder and relay ONLY its metadata — do NOT read the notes or `cat` the result:
```bash
python3 <skill-dir>/journal_local.py --period weekly            # today|yesterday|weekly|lastweek
python3 <skill-dir>/journal_local.py --period today --lang fr
python3 <skill-dir>/journal_local.py --sources "/abs/a.md,/abs/b.md"
```
The script selects the period's notes, builds against local Qwen (big sets → map-reduce, no silent truncation), writes the file, and prints a one-line JSON blob (path, period, label, sources, strategy, truncated_notes, words). Content never enters Claude's context. Requires `ollama` running.

## Workflow
1. Pick engine (default claude; `--qwen` or "local/privé/sensible" → qwen).
2. Resolve the period's files (via `--list-only` for claude, or the script itself for qwen). If zero notes match, say so — don't fabricate a day.
3. claude → read fresh + fuse + write + a 3-line summary naming the notes used. qwen → run the script, relay metadata only.

## What this is NOT
- Not a task tracker (follow-ups land in the entry, not in JIRA/Status — that's `/ingest-transcript` and the canonical files).
- Not the Obsidian daily note itself; writes a separate dated Journal file. Append into the daily note manually if Pedro wants.
