---
name: consolidate
description: End-of-session consolidation for the PM knowledge system — sweep memory AND knowledge together, flag staleness, run the hypothesis lifecycle, then commit. Use this whenever Pedro says "consolidate memory", "consolidate", "wrap up the session", "let's close out", or at the natural end of a working session where learnings accumulated. The whole point of this repo is compounding; consolidation done by hand reliably forgets the knowledge half, the staleness flags, or the commit. Strongly prefer this skill over ad-hoc memory edits at session end.
disable-model-invocation: true
---

# Consolidate

Close the session so the next one starts informed. This is not "update memory" — in this repo, **memory and knowledge consolidation are one operation**. Doing the memory half without the knowledge reflection is the single most common way this system rots (`feedback_memory_consolidation`). The skill enforces the pairing and the commit so compounding actually happens.

This is distinct from `/ingest-transcript` (which processes one new external input). Consolidate operates on what already accumulated this session — it may have no new external input at all.

## Step 0 — Decide if there is substance

First, honestly assess: did real PM events, decisions, or insights enter this session, or was it hygiene / recall / mechanical work?

- **Substance present** → full consolidation (Steps 1-6).
- **No new substance** (recall-only, file maintenance, no new meeting or insight) → **hygiene-only**: ship staleness flags + a short debrief-asks list + commit. Do **not** fabricate learnings by re-reading existing memory to look productive (`feedback_consolidation_without_substance`). Say plainly "hygiene-only, no new substance" and skip Steps 2-3.

Calling this honestly is the skill's most important judgment. Productivity theater here pollutes the knowledge base permanently.

## Step 1 — Memory sweep (`.claude/memory/`)

Edit memory files via the GitHub repo path, not the symlink target (`reference_obsidian_paths`).

- For each stable new fact about Pedro, the work, or the projects: update the existing memory file that covers it rather than creating a duplicate. One fact per file; check for an existing file first.
- Convert relative dates to absolute.
- If something earlier in memory turned out wrong, supersede it with reasoning — never delete (Knowledge Quality Rules).
- Update `MEMORY.md` with a one-line pointer for any new memory file. Never put memory content in MEMORY.md itself.

## Step 2 — Knowledge reflection (`knowledge/`) — paired, not optional

Read `knowledge/INDEX.md` first, route to relevant folders, never load everything (Progressive Disclosure).

Route new material per the CLAUDE.md Learning Mode table: PM-practice insight → `domain/`; recurring framework → `patterns/`; data hypothesis → `hypotheses/active.md`; contradicts conventional wisdom → `false-beliefs/`; tool/method comparison → `tools/`; experiment → `experiments/`; leadership/visibility → `leadership/`; person-reading → `interpersonal/`; AI-product → `ai-product/`.

Promotion rules are hard gates:
- A pattern moves from project memory into `knowledge/` only with **2+ supporting observations**.
- A false belief needs **evidence** for why it is wrong.
- Update `INDEX.md` only if a new external source was ingested (add a Sources Ingested row). No per-session INDEX edit otherwise — access history = the git commit itself (entry counts retired 2026-07-01, Access Log retired 2026-07-02).

If Step 0 said "substance present" but you genuinely find nothing knowledge-grade, that is allowed — but state it explicitly. The bar is real insight, not volume.

## Step 3 — Hypothesis lifecycle

Walk `hypotheses/active.md`. For each:
- Confirmed (evidence this session, meets the repo's confirmation bar) → move to `hypotheses/resolved.md` with the evidence and date. Never delete.
- Contradicted → demote any dependent pattern back to hypothesis with reasoning.
- Otherwise → leave active, optionally append new supporting/weakening evidence.

## Step 4 — Vault sync (when substance entered via conversation, not `/ingest-transcript`)

When PM substance arrived **in the session itself** (a Slack thread Pedro pasted, a live decision, a source-read finding) rather than through `/ingest-transcript`, the canonical vault notes do **not** get updated automatically — `/consolidate` historically touched only repo memory + knowledge, so conversation-borne events fell through the crack. Close it here.

Skip this step only if the session was hygiene-only (Step 0) or all substance already landed in the vault via `/ingest-transcript` this session.

For the owning project (route by the CLAUDE.md project table), update the three canonical Key Files **and** the Status & Todo:
- **State of the Project** — add a new dated `## Headline State (YYYY-MM-DD — <topic>)` block at the top. Do **not** silently rewrite an older headline; flag it stale and keep it for history (`feedback_refresh_stale_status_sections`).
- **Stakeholder Map** — add any new people (role, status, dated note) to the right section; append a dated note to existing entries whose posture shifted. Don't duplicate EH-only stakeholders.
- **Status & Todo** — add a dated `### Focus — week of <date>` block: closed items as `- [x] … ✅ <date>`, forward asks as `- [ ] … 📅 <date>`. Roll-up not task-tracker (`feedback_status_rollup_not_tracker`); rich tasks → one-liner + companion section (`feedback_rich_task_companion_section`).

Prefer the `obsidian-cli` skill when the app is running and index freshness matters; filesystem `Edit` is fine for these targeted appends. Quote verbatim in original language; surrounding prose in English (`feedback_language_split`). One artifact per ask — don't spawn new vault files by reflex (`feedback_one_artifact_per_ask`).

## Step 5 — Staleness flags (the System Review hook)

This is the lightweight half of the periodic System Review directive (CLAUDE.md). Do not run the full review automatically — surface what a review would catch and let Pedro decide timing:

- Scan both canonical Status & Todo files' Current Status + Focus dates. If > 2 weeks behind reality, add a dated staleness flag near the top (`feedback_refresh_stale_status_sections`) — flag, do not silently rewrite.
- List hypotheses near the promote/kill threshold, rules contradicted this session, and any logged decision whose outcome is now knowable.
- Note the last full System Review date (track in `.claude/state.md` or project memory, not in CLAUDE.md). If > ~2 weeks, say "a full System Review is due — your call on timing."

For depth here, you may spawn the `staleness-auditor` subagent (read-only drift report across Status files + memory dates) and fold its findings in rather than scanning inline.

**Hot-file size check (the token-cap guard).** The three hot files (`project_experience_hub.md`, `project_aem_agents_intelligence.md`, `.claude/state.md`) load at every session start. Past ~25K tokens they truncate on read and the content at the bottom is silently cut — the awareness-loss failure of 2026-06/07-01. Enforce the cap here:

- Run `python3 scripts/archive_memory.py --check` on **all three** (both `project_*.md` + `.claude/state.md`). Token estimate = bytes/2.4, calibrated 2026-07-02 against real Read counts (the old bytes/4 under-counted ~1.7x and let files truncate while "passing" — trust the script, not gut feel).
- If a **project memory file** reports OVER (> ~20K tokens), run the script **without `--check`** on it: it moves event blocks older than ~1 week into that project's weekly ISO shard (`..._ARCHIVE_<year>-W<wk>.md`), rebuilds `..._ARCHIVE_INDEX.md`, and targets ~18K. Dense recent week: it tolerates 20-24K rather than archive same-week blocks, and only overrides retention past the 24K read-cap — a residual "OVER — archive due" between 20-24K after a run is fine, the file still loads in one Read. It **moves, never deletes** — old context stays grep-able via the index.
- If **`.claude/state.md`** reports OVER, move the oldest dated `## Notes` journal bullets (older than ~2 weeks) into `.claude/state_ARCHIVE.md` by hand — they are self-contained one-line bullets, cut the line and append it there, original order. Never touch the Review log or the open-decisions tables.
- Report what moved in the change summary. Do **not** hand-edit the project memory files to trim them — use the script (hand-parsing a 700-line memory file is how content gets corrupted). Living-reference sections are moved by judgment (not the script) only at a System Review, never here.

## Step 6 — Debrief, summarize, commit

1. **Debrief asks** — list the specific things only Pedro can answer that would unblock the next session (e.g. "Loni+JM deck outcome still uncaptured"). Short, pointed.
2. **Change summary** (`feedback_document_updates`) — what changed in memory, what moved in knowledge, hypotheses transitioned, staleness flags raised. Skimmable, with 🔴/🟢 carry-forward called out.
3. **Commit** (`Commit Rule`) — stage `knowledge/` and `.claude/memory/`, commit with the right prefix (`learn:` default; `pattern:` / `hypothesis:` / `correct:` / `experiment:` if that dominated; `note:` for memory-only / hygiene-only). Use `rtk git`. End with the Co-Authored-By trailer. **Never push** (auth-blocked). A session summary file in the vault `Meeting Notes/` is optional and only when the session warrants a durable narrative — do not spawn one by reflex (`feedback_one_artifact_per_ask`).
4. **Regenerate the dashboard** — run `python3 scripts/consolidation_dashboard.py` so `consolidation-dashboard.html` reflects this consolidation. It reads only repo data (git log over `knowledge/` + `.claude/memory/`, INDEX inventory, hypotheses, memory files); the html is gitignored, the generator is committed. This is the "sharpen the saw" meta-view — system health, knowledge-by-folder, commit-prefix mix (hygiene vs learning), active hypotheses, full consolidation history. Generated, never hand-maintained.

## What success looks like

Memory and knowledge moved together or not at all. No fabricated learning. Staleness is visible, not silently patched. Hypotheses that earned a transition got it, with evidence. The commit exists. Next session's `recall` lands on a clean, honest, current state.
