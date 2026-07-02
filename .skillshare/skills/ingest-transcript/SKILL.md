---
name: ingest-transcript
description: Ingest a meeting transcript into the PM knowledge system — extract dated signals, update the right project's canonical Status & Todo + project memory, reconcile predicted-vs-actual dates, reflect into knowledge/ when pattern-grade, then commit. Use this whenever Pedro hands over a transcript, meeting notes, or 1-1 recording (a path under "Meeting Notes/", or text pasted in chat) and asks to "review and update", "ingest", "process this transcript", "update doc and memory from this", or after any meeting analysis where the output should land in the vault. Strongly prefer this over ad-hoc editing — the value of this system is that every meeting compounds, and the routing/reconcile/commit steps are easy to do inconsistently by hand.
disable-model-invocation: true
---

# Ingest Transcript

Turn one meeting transcript into durable, correctly-routed knowledge. This is the most-repeated workflow in this repo; doing it by hand drifts (wrong project, stale predicted dates, forgotten commit, prep sections that strand wikilinks). The skill exists to make the compounding reliable, not to replace judgment — read the transcript and think like the PM, then route.

`ARGUMENTS` = transcript path (optional). If empty, find the most recently modified file under the vault `Meeting Notes/` tree and confirm it with the user before ingesting.

## Before anything: orient

1. Read `CLAUDE.md` in the repo root if not already in context. The **"Common PM Tasks Routing → By project"** table is authoritative for which project owns the outcome (EH vs AAI), which memory file, which canonical Status & Todo, which trio. Do not guess routing from the filename — a Bertrand 1-1 transcript can carry both EH and AAI signals.
2. Load the relevant project memory file(s) from `.claude/memory/` (`project_experience_hub.md`, `project_aem_agents_intelligence.md`). These hold predicted future events ("call lands Tue May 19") that this transcript may resolve or contradict — you need them to reconcile.
3. Note today's date (system context). Convert every relative date in the transcript ("yesterday", "next week") to absolute before writing anything.

## Step 1 — Read the transcript

**Load `reference_transcript_glossary.md` first** (canonical names/terms + known Otter garbles). De-garble on extraction using it; when you resolve a NEW garble this ingest, add it to the glossary — that's its maintenance model. Verbatim quotes stay original; the analysis uses canonical names.

If the file is **> ~2000 lines or > ~100K characters**, do not read it linearly. Spawn 3-5 parallel `transcript-extractor` subagents on contiguous line ranges — that agent returns a tight dated structured extract (decisions, action items with owner, new stakeholders, bankable verbatim, risks, reconcile candidates) and reads only its range. Synthesize from the structured extracts only. This is the `feedback_big_file_parallel_chunk_extract` memory rule — it keeps the main thread's context clean.

For normal-size transcripts, read it whole. Transcripts are often sparse (long screen-share gaps, "mhm/yeah/okay" turns). If more than ~40% of turns carry no substance, the meeting content is partly reconstructed from one-sided turns — say so explicitly in the notes and tag the memory entry as a low-fidelity source so later synthesis doesn't over-trust it.

Attribution care: "CR <ROOM>" labels in Teams transcripts are conference-room mics, not people, and map per-meeting not per-person (see `feedback_transcript_attribution`). Resolve speakers by content, flag uncertainty.

## Step 2 — Extract and route

Pull out, with dates and verbatim where it matters:

- **Decisions** (something is now settled — and by whom; a Slack position is not a decision, see `feedback_proposal_vs_decision`)
- **Action items** — forward-looking, owner-tagged, due-dated. These become checkbox tasks, never past-tense log lines (`feedback_task_vs_progress_log`).
- **New stakeholders** — name, role, why-relevant.
- **Quotes worth banking** — exec verbatim, especially VP. Audit the grammatical subject before promoting a quote to promotion-grade narrative (`feedback_dont_overread_vp_quotes`).
- **Reconcile** — anything the transcript resolves or contradicts vs the project memory you loaded (a predicted date that moved, a hypothesis confirmed/killed, a "still owed" item now closed).

Route each item to the project that **owns the outcome** (CLAUDE.md table). The mirror rule is retired — do not duplicate across EH and AAI. Cross-cutting 1-1s (Bertrand) split by surface: EH signals to EH, AAI signals to AAI.

## Step 3 — Update the canonical Status & Todo

The Status & Todo files are roll-ups, not task trackers (`feedback_status_rollup_not_tracker`). Edit the canonical file for the owning project (path in CLAUDE.md table).

Surface-edit only what changed. Prefer the `obsidian-cli` skill for these writes when the Obsidian app is running — writes go through the running app and avoid sync conflicts; filesystem `Edit` is acceptable for precise section edits but bypasses the index. Either way, never blanket-rewrite a canonical file.

**Prep → notes reconcile (the date-agnostic rule, `feedback_prep_sections_date_agnostic`):**
- If a prep companion section exists for this meeting (e.g. `## <Person> call prep — next`), convert it to `## <Person> call notes — <actual held date>` and update the one inbound task wikilink to match.
- If the predicted heading carried a date that turned out wrong, fix it and say so in the change summary — a stranded `[[#... <wrong date>]]` anchor is easy to miss.
- Mark the meeting task `[x]` with `✅ <held date>`, add a one-line outcome, and add forward tasks for anything newly owed.
- Prep targets that were planned but **not covered** in the meeting are still owed — list them explicitly as carry-forward, don't silently drop them (`feedback_defuse_vs_defer`).

Before adding tasks, scan the Current Status + Focus dates. If they are > 2 weeks behind reality, offer to refresh the stale sections (`feedback_refresh_stale_status_sections`) rather than appending onto a stale base.

When you touch a Status & Todo file, ask once whether there are conversation links to add (Teams meeting, Slack thread, email, Confluence) for the Conversations section, per CLAUDE.md's Working Relationship rule. Accept "no link, the date/time is enough" for internal-only meetings with no external artifact (`feedback_conversation_link_optional`) — the transcript itself often is the artifact.

## Step 4 — Update project memory

Edit the owning project's memory file under `.claude/memory/` (use the GitHub repo path, not the symlink target — `reference_obsidian_paths`).

- Add a dated section for the meeting (`## <Date> — <Meeting> (held)`), with outcomes, why-it-matters, and a pointer to the Status & Todo notes section.
- If memory predicted this event with a different date, rewrite the entry with an explicit reconcile note rather than leaving the old prediction to rot. Never delete superseded knowledge — supersede it with reasoning.
- Fix any other stale cross-reference to the old predicted date elsewhere in the file (grep for it).
- Keep verbatim quotes in their original language; the surrounding write is English even when chat is French (`feedback_language_split`).

## Step 5 — Knowledge reflection (only when it earns it)

**Retrieval first (P6, 2026-07-02).** Before reflecting anything new OUT, pull existing knowledge IN: name which existing `knowledge/` entries apply to this meeting's situations (route via the folder READMEs, cite as `[[entry title]]` in the memory block), or state plainly "none apply". If an entry applied but the live work didn't use it, say so in the summary ("next time, lead with [[X]]") — a rule that never gets retrieved at decision time is dead weight, and the citation is what the retrieval audit counts.

This is a Learning-Mode repo: when the transcript carries a genuine PM insight, pattern, hypothesis, false belief, or tool comparison, update `knowledge/` without asking — route via `knowledge/INDEX.md`, never load everything. Promotion rules from CLAUDE.md hold: a pattern needs **2+ supporting observations** before it moves from project memory into `knowledge/`; a hypothesis flips to resolved only with evidence. Update INDEX.md only if a new external source was ingested (Sources Ingested row) — entry counts and the Access Log are retired; the git commit is the access record.

If the meeting produced no new PM-pattern substance (a status sync with no insight), do **not** invent a learning to look productive — hygiene-only is a valid outcome (`feedback_consolidation_without_substance`). Say so.

## Step 6 — Summarize, offer trio, commit

1. **Brief change summary** (`feedback_document_updates`): what changed in the doc, what changed in memory, what knowledge moved, and the substantive meeting takeaways — short, skimmable, with the 🔴/🟢 carry-forward items called out.
2. **Offer the trio** — do not auto-write it. After a meeting analysis the project's trio (Stakeholder Map / State of the Project / Questions for next 1-1) often wants updating. The EH/Sorin trio rule (`feedback_update_trio`) is EH-specific; the AAI trio is different. Name the specific trio for the owning project and ask if Pedro wants it synced (State of the Project = headline-only, 3-5 lines + a Status & Todo link — one home per info, P4 2026-07-02), unless this transcript introduced a new stakeholder (then flag the Stakeholder Map gap directly).
3. **Commit** (`Commit Rule`): stage `knowledge/` and `.claude/memory/` and commit with the right prefix (`learn:` for meeting ingest, `pattern:` / `hypothesis:` / `correct:` if that was the dominant change). Use `rtk git` per the global RTK rule. End the commit message with the Co-Authored-By trailer. **Never push** — this repo's push is auth-blocked. Vault files (Status & Todo, trio) live outside the repo and are not committed here; OneDrive/Obsidian sync carries them.

## What success looks like

The next session can `recall`, read memory, and know exactly what happened in this meeting, what is still owed, and where it landed — without re-reading the transcript. Predicted dates match reality or carry an explicit reconcile note. No stranded wikilink. The commit exists. If a promotion-grade signal surfaced, it is framed through the Director→Senior Director lens, not buried in a task line.
