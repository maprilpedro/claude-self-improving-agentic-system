---
name: consolidate
description: End-of-session consolidation for the PM knowledge system, in two modes. Light (the default during the day) rewrites the RESUME, updates watches and commits. Full (end of day, on request, or when no full pass ran since yesterday) also sweeps knowledge, runs the hypothesis lifecycle, syncs the vault, flags staleness and regenerates the dashboard. Use this whenever Pedro says "consolidate memory", "consolidate", "wrap up the session", "let's close out", or at the natural end of a working session where learnings accumulated. The whole point of this repo is compounding; consolidation done by hand reliably forgets the knowledge half, the staleness flags, or the commit. Strongly prefer this skill over ad-hoc memory edits at session end.
disable-model-invocation: true
---

# Consolidate

Close the session so the next one starts informed. This is not "update memory" — in this repo, **memory and knowledge consolidation are one operation**. Doing the memory half without the knowledge reflection is the single most common way this system rots (`feedback_memory_consolidation`). The skill enforces the pairing and the commit so compounding actually happens.

This is distinct from `/ingest-transcript` (which processes one new external input). Consolidate operates on what already accumulated this session — it may have no new external input at all.

## Pick the mode first

Pedro runs this several times a day, and a full pass every time is slow. So the day is split in two.

- **Light, the default.** Step 0, Step 1, then the commit (Step 6.3). It keeps the next session informed and leaves the knowledge, vault and staleness work for later.
- **Full.** Every step. Run it when Pedro asks for it ("full", "complet", "fin de journée", "wrap up the day"), or when no full pass has run since yesterday. Check with `rtk git log --since="yesterday 00:00" --grep="Consolidate: full" --oneline`. If it returns nothing, run full and say so in one line.

Light defers the knowledge half, it does not drop it, so the pairing rule still holds (`feedback_memory_consolidation`). The catch is that the full pass may run in a later session that never saw this conversation. So the deferral has to be written down. A light pass ends Step 1 with an **"Owed to the full pass"** line in the RESUME of each project it touched. A full pass starts by reading those lines in all four project files and treats them as part of the session's substance.

## Step 0 — Decide if there is substance

First, honestly assess: did real PM events, decisions, or insights enter this session, or was it hygiene / recall / mechanical work?

- **Substance present** → full consolidation (Steps 1-6).
- **No new substance** (recall-only, file maintenance, no new meeting or insight) → **hygiene-only**: ship staleness flags + a short debrief-asks list + commit. Do **not** fabricate learnings by re-reading existing memory to look productive (`feedback_consolidation_without_substance`). Say plainly "hygiene-only, no new substance" and skip Steps 2-3. In a full pass Step 1b still runs, because a recurring workflow can run in a session with no new substance. Both modes can be hygiene-only.

Calling this honestly is the skill's most important judgment. Productivity theater here pollutes the knowledge base permanently.

## Step 1 — Memory sweep (`.claude/memory/`)

Edit memory files via the GitHub repo path, not the symlink target (`reference_obsidian_paths`).

- For each stable new fact about Pedro, the work, or the projects: update the existing memory file that covers it rather than creating a duplicate. One fact per file; check for an existing file first.
- Convert relative dates to absolute.
- If something earlier in memory turned out wrong, supersede it with reasoning — never delete (Knowledge Quality Rules).
- Update `MEMORY.md` with a one-line pointer for any new memory file. Never put memory content in MEMORY.md itself.
- **Rewrite the RESUME of each project file you touched.** Today's state in 5 lines at most: what moved, what waits on whom and by when, what is late, the main risk, and after a light pass the "Owed to the full pass" line. In a full pass, keep the Owed lines you found until Step 6 removes them. Replace the old text instead of adding in front of it. The archiver moves dated blocks but never the RESUME, so anything stacked there stays for good: by 2026-10-28 the Coworker Lead RESUME had grown into a ~6,000-character chain of "Earlier:" pointers and pushed the file to its cap. Keep the word `RESUME` in the block's first line, because `scripts/archive_memory.py` protects the block by that word. The detail goes in a dated block directly under the RESUME (the layout invariant at the top of each project file). If the RESUME still carries an old chain, first move that text verbatim to a dated section at the end of the project's `_ARCHIVE_reference.md` (create the file with a one-line header if there is none).
  - Owed line format, one per project: `> - **Owed to the full pass.** knowledge: <candidate, and the entry it may be an instance of>; findings: <workflow, lesson>; vault: <Status Focus, Kanban cards, etat>.`
- **Maintain `watches.md`** — the single registry of dated follow-ups: add any new "check X on date Y" the session created, ✅-close what resolved (move to its History), never leave a dated promise buried in an event block.

## Step 1b — Findings logs (recurring workflows, full pass)

In a light pass, skip this step and put the workflow and its lesson in the "Owed to the full pass" line.

A recurring workflow only gets better if each run leaves a lesson that the next run reads (`reference_findings_files`). Reading is wired in at recall through `MEMORY.md`. Writing is the half that gets forgotten, so it happens here.

- Open `.claude/memory/reference_findings_files.md`. For each workflow in its table that ran this session (a batch of usage stories went out, a draft in Pedro's voice was sent, a transcript was read), add one dated line to that workflow's findings file: what was done, and what you saw work or fail.
- Then ask Pedro for his part, one line per workflow. For the usage stories it is the two questions in the file's Run log: what Bertrand reacted to, and what Rachel or Gina reused. Write his answer in as he gives it. If he has no answer yet, mark the line "Pedro: pending" and add a watch for the next session. Do not fill his part yourself; an invented reaction poisons every later run.
- If a workflow repeated this session and has no findings file, propose one (a registry row plus the file). Do not create it by reflex.
- Nothing ran → skip silently.

## Step 2 — Knowledge reflection (`knowledge/`) — paired, not optional (full pass)

Start with the "Owed to the full pass" lines in the four project RESUMEs. They carry the knowledge candidates of the day's light passes, possibly from other sessions.

Read `knowledge/INDEX.md` first, route to relevant folders, never load everything (Progressive Disclosure).

**Retrieval first.** Before adding anything, name which existing entries the session's events are instances of — cite them as `[[entry title]]` in the memory block ("no new entry — instance of [[X]]" already does this; keep the citation literal so the retrieval audit can count it). If an entry applied but wasn't used during the live work, flag it ("next time, lead with [[X]]").

Route new material per the CLAUDE.md Learning Mode table: PM-practice insight → `domain/`; recurring framework → `patterns/`; data hypothesis → `hypotheses/active.md`; contradicts conventional wisdom → `false-beliefs/`; tool/method comparison → `tools/`; experiment-shaped material → `hypotheses/active.md` (a hypothesis with a resolution date); leadership/visibility → `leadership/`; person-reading → `interpersonal/`; AI-product → `ai-product/`.

Promotion rules are hard gates:
- A pattern moves from project memory into `knowledge/` only with **2+ supporting observations**.
- A false belief needs **evidence** for why it is wrong.
- Update `INDEX.md` only if a new external source was ingested (add a Sources Ingested row). INDEX.md carries no entry counts and no access log; the git commit is the access record.

If Step 0 said "substance present" but you genuinely find nothing knowledge-grade, that is allowed — but state it explicitly. The bar is real insight, not volume.

## Step 3 — Hypothesis lifecycle (full pass)

Walk `hypotheses/active.md`. For each:
- Confirmed (evidence this session, meets the repo's confirmation bar) → move to `hypotheses/resolved.md` with the evidence and date. Never delete.
- Contradicted → demote any dependent pattern back to hypothesis with reasoning.
- Otherwise → leave active, optionally append new supporting/weakening evidence.

## Step 4 — Vault sync (full pass; when substance entered via conversation, not `/ingest-transcript`)

When PM substance arrived **in the session itself** (a Slack thread Pedro pasted, a live decision, a source-read finding) rather than through `/ingest-transcript`, nothing else writes it to the canonical vault notes. This step does.

Skip this step only if the session was hygiene-only (Step 0) or all substance already landed in the vault via `/ingest-transcript` this session.

For the owning project (route by the CLAUDE.md project table), update the three canonical Key Files **and** the Status & Todo. Release Management and Security Health have no State of the Project or Stakeholder Map yet. For them, update the Status & Todo only and put new people in its Key People section. Do not create the missing files unless Pedro asks (`feedback_one_artifact_per_ask`). **One home per info:** session narrative → the memory RESUME block (once); tasks + event detail → Status & Todo; people → Stakeholder Map; State of the Project → headline only. Never write the same detail in two of them.
- **State of the Project** — **headline-only**: add a dated `## Headline State (YYYY-MM-DD — <topic>)` block of **3-5 lines max** + one link to the Status & Todo for the detail. No task lists, no event narrative here — that's Status & Todo's home. Do **not** silently rewrite an older headline; older headlines stay as history (`feedback_refresh_stale_status_sections`).
- **Stakeholder Map** — add any new people (role, status, dated note) to the right section; append a dated note to existing entries whose posture shifted. Don't duplicate EH-only stakeholders.
- **Status & Todo** — add a dated `### Focus — <date> (<topic>)` block directly under the Focus heading, in plain bullets: forward asks as `- <action> — due <date>`, closed items as `- <action> — done <date>`, undated ones as `— open`. Never checkboxes (`- [ ]`, `- [x]`) or Tasks emoji (`📅`, `✅`): Pedro does not use Obsidian tasks and had 313 of them cleaned out (`feedback_no_obsidian_task_checkboxes`). **Coworker tasks live on the board `Coworker Lead - Project Folder/Coworker Kanban.md`** (Kanban plugin, the one file where checkboxes are the required format): add new Coworker tasks to Todo, move finished ones to Done, keep Doing at 3 cards at most, and leave only events plus a link to the board in the Focus block. The Coworker Priorities Tree at the top of the Coworker Lead Status shows Pedro's five branches only, with no tasks, so the board stays the single home of Coworker tasks. Do not add task leaves to it; change it only when Pedro changes his branches. Roll-up not task-tracker (`feedback_status_rollup_not_tracker`); rich tasks → one-liner + companion section (`feedback_rich_task_companion_section`).
- **État line** in the Status & Todo front matter. Set `etat` to one or two sentences in French (what moved, what waits, on whom, by when) and `etat-date` to today as `YYYY-MM-DD`, replacing the previous values, in every Status & Todo you touched. The Projects Panel in the vault leads each project card with this line, so write it for Pedro glancing at four cards, not as a log entry. History stays in the Focus blocks. Example: `etat: "La réponse à RBI est partie ce matin, le call client est mardi 11-03."`
- **Panel contract.** The panel also reads the Headline State, the Focus heading and bullets, `due <date>` dates and the Kanban lanes. Their exact formats are in `120 Projects/Work/_panels/projects/CONTRACT.md`. Read it before changing any of those formats or moving a project folder, otherwise a card goes empty or missing without any error.

Prefer the `obsidian-cli` skill when the app is running and index freshness matters; filesystem `Edit` is fine for these targeted appends. Quote verbatim in original language; surrounding prose in English (`feedback_language_split`). One artifact per ask — don't spawn new vault files by reflex (`feedback_one_artifact_per_ask`).

## Step 5 — Staleness flags (the System Review hook, full pass)

This is the lightweight half of the periodic System Review directive (CLAUDE.md). Do not run the full review automatically — surface what a review would catch and let Pedro decide timing:

- Scan the four canonical Status & Todo files' Current Status + Focus dates (Coworker Lead, EH, Release Management, Security Health). If > 2 weeks behind reality, keep **one** staleness flag per file, at the top of its Current Status (`feedback_refresh_stale_status_sections`). If a flag is already there, update its date and count in place. Do not add a second banner and do not add flags inside Focus blocks. A flag repeated at every pass stops being read: by 2026-10-28 the EH Status carried six of them, the newest saying "fourteenth", and none had led to a refresh. Flag, do not silently rewrite, and list it in the debrief asks.
- In the same four files, check the `etat-date` front matter. Missing or older than 2 weeks means the panel card leads with stale text. List it in the debrief asks. Write a new État line only from this session's substance (Step 4), never by rephrasing the old one.
- List hypotheses near the promote/kill threshold, rules contradicted this session, and any logged decision whose outcome is now knowable.
- Read `Next review due` in `.claude/state.md` (the cadence is monthly and lives there, not in CLAUDE.md). On or after that date, say "a full System Review is due (<date>), your call on timing." Within 5 days of it, mention the date in the debrief.

For depth here, you may spawn the `staleness-auditor` subagent (read-only drift report across Status files + memory dates) and fold its findings in rather than scanning inline.

**Hot-file size check (the token-cap guard).** The hot files (`project_aem_agents_intelligence.md` = Coworker Lead, `project_experience_hub.md`, `project_release_management.md`, `project_security_health.md`, `.claude/state.md`) load at every session start. Past ~25K tokens they truncate on read and the content at the bottom is silently cut. Enforce the cap here:

- Run `python3 scripts/archive_memory.py --check` on **all five** (the four `project_*.md` + `.claude/state.md`). Trust the script's token estimate over a byte count or gut feel.
- If a **project memory file** reports OVER (> ~20K tokens), run the script **without `--check`** on it: it moves event blocks older than ~1 week into that project's weekly ISO shard (`..._ARCHIVE_<year>-W<wk>.md`), rebuilds `..._ARCHIVE_INDEX.md`, and targets ~18K. Dense recent week: it tolerates 20-24K rather than archive same-week blocks, and only overrides retention past the 24K read-cap — a residual "OVER — archive due" between 20-24K after a run is fine, the file still loads in one Read. It **moves, never deletes** — old context stays grep-able via the index.
- If **`.claude/state.md`** reports OVER, move the oldest dated `## Notes` journal bullets (older than ~2 weeks) into `.claude/state_ARCHIVE.md` by hand — they are self-contained one-line bullets, cut the line and append it there, original order. Never touch the Review log or the open-decisions tables.
- Regenerate the entity index: `python3 scripts/entity_index.py` (generated lookup for /reply — cheap, run it every consolidation).
- Report what moved in the change summary. Do **not** hand-edit the project memory files to trim them — use the script (hand-parsing a 700-line memory file is how content gets corrupted). Living-reference sections are moved by judgment (not the script) only at a System Review, never here.

## Step 6 — Debrief, summarize, commit

0. **No state.md journal** — do NOT append a session-journal bullet to `state.md` `## Notes`; the memory RESUME block is the single home for session narrative. `state.md` is touched only by `/system-review` (Review log row) or when a hypothesis/decision table row genuinely changes.
1. **Debrief asks** — list the specific things only Pedro can answer that would unblock the next session (e.g. "Loni+JM deck outcome still uncaptured"). Short, pointed. In a light pass, only the asks that block the next step.
2. **Change summary** (`feedback_document_updates`) — what changed in memory, what moved in knowledge, hypotheses transitioned, staleness flags raised. Skimmable, with 🔴/🟢 carry-forward called out. In a light pass, three lines at most, ending with what is owed to the full pass.
3. **Commit** (`Commit Rule`) — stage `knowledge/` and `.claude/memory/`, commit with the right prefix (`learn:` default; `pattern:` / `hypothesis:` / `correct:` / `experiment:` if that dominated; `note:` for memory-only / hygiene-only). Use `rtk git`. End with the Co-Authored-By trailer. Put `Consolidate: light` or `Consolidate: full` on its own line in the body, above the trailer, because the mode check in "Pick the mode first" searches for it. A light pass stages `.claude/memory/` only and uses `note:`. A full pass removes the "Owed to the full pass" lines it covered before committing. **Never push** (auth-blocked). A session summary file in the vault `Meeting Notes/` is optional and only when the session warrants a durable narrative — do not spawn one by reflex (`feedback_one_artifact_per_ask`).
4. **Regenerate the dashboard** (full pass) — run `python3 scripts/consolidation_dashboard.py` so `consolidation-dashboard.html` reflects this consolidation. It reads only repo data (git log over `knowledge/` + `.claude/memory/`, INDEX inventory, hypotheses, memory files); the html is gitignored, the generator is committed. This is the "sharpen the saw" meta-view — system health, knowledge-by-folder, commit-prefix mix (hygiene vs learning), active hypotheses, full consolidation history. Generated, never hand-maintained.

## What success looks like

Memory and knowledge moved together or not at all, within the day: a light pass leaves an Owed line for everything it deferred, and a full pass runs at least once a day. Each RESUME reads as today's state in five lines. Every recurring workflow that ran left a lesson in its findings file. No fabricated learning. Staleness is visible, not silently patched. Hypotheses that earned a transition got it, with evidence. The commit exists. Next session's `recall` lands on a clean, honest, current state.
