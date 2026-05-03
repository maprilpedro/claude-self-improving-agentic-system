# Memory Index

## References
- [Claude improvement tools](claude-improvement-tools.md) — Recommended MCP servers, skills, editor extensions, and architecture improvements for the PM knowledge system
- [Splunk MCP usage dashboard](reference_splunk_mcp.md) — Bertrand's source for MCP adoption metrics. Paired with CM UI activity data (owner TBD) for ratio metric.
- [OKR structure — O1 AI Agent Intelligence](reference_okr_structure.md) — Location and current KR composition. KR1 Apoorva punch-list, KR3 Loni+JM presentation, KR4 Priority Consolidation view, KR SLA planning, etc.
- [Atlassian MCP — JIRA + Confluence](reference_atlassian_mcp.md) — Tool surface for fetching real JIRA / Confluence content from Adobe corp instances (only way in, since they're internal-only).
- [AEM Agent Ownership Matrix](reference_aem_agent_ownership.md) — Canonical PgM/PM/Eng/JIRA for the 10 AEM agents per slide 44 of H2'26 AEM & Agentic Web Planning deck.
- [Power BI — Token usage per org](reference_powerbi_token_usage.md) — Adobe corp Power BI report. Token consumption per org. Ties to FinOps (Jaclyn) + AO 2.0 pricing/SKU risk (Bertrand April 29).
- [CLI binaries playbook](reference_cli_binaries.md) — When to reach for yq/comby/sd/scc/difft/shellcheck/ast-grep. Workhorses for memory + knowledge ops.
- [Obsidian vault canonical paths](reference_obsidian_paths.md) — Correct Adobe project folder paths. EH lives at `Experience Hub/`, AAI scaffold at `AEM Agents Intelligence/`. Memory file edits via GitHub repo path, not symlink target.

## User
- [Pedro's favorite calls](user_calls.md) — 6 quotes he uses as thinking lenses. Apply them in analysis and writing.

## Feedback
- [Save screenshots to project folder](feedback_screenshots.md) — Always save screenshots to /screenshots in the project repo so they persist across sessions
- [Session setup commands](feedback_session_setup.md) — Remind user to run /color orange and /rename ADBE-PM-ASSISTANT (UI commands, user must run them)
- [No meeting setup help](feedback_no_meeting_setup.md) — Never offer to help schedule or set up meetings
- [Session start behavior](feedback_session_start.md) — Always pick up where we left off on Experience Hub when starting a conversation
- [Transcript room mic attribution](feedback_transcript_attribution.md) — "CR" room labels in Teams transcripts are conference room mics, not people. In the March 23 2026 session, all CR lines = Loni Stark
- [Update trio after every meeting analysis](feedback_update_trio.md) — After every analysis, always update Stakeholder Map, State of the Project, and Questions for Next 1-1 with Sorin in the Obsidian vault
- [Knowledge folder update cadence](feedback_knowledge_updates.md) — Always update knowledge/, INDEX.md, and README.md when asked and proactively at least once every 2 days. Commit with learn: prefix.
- [Memory consolidation includes learning reflection](feedback_memory_consolidation.md) — "consolidate memory" triggers both memory updates AND knowledge reflection. Never do one without the other.
- [Brief summary after document updates](feedback_document_updates.md) — After every document update, give a short summary of what changed and why.
- [Task vs progress log distinction](feedback_task_vs_progress_log.md) — "Track this" = forward-looking task (checkbox + due date), NOT a past-tense progress log entry. Progress log is for what already happened.
- [Conversation link optional when none exists](feedback_conversation_link_optional.md) — Ask for link per Status & Todo rule, but accept "no link, date/time is enough" for internal-only meetings without an external artifact.
- [Rich task format — companion section pattern](feedback_rich_task_companion_section.md) — When user asks for tasks "with max info and hints," split into one-liner tasks + companion H2 section with full prep. Never dump multi-paragraph content into the task line.
- [Mirror tasks across Status & Todo files](feedback_mirror_tasks_across_status_files.md) — When agent-reporting work spans surfaces, duplicate the tasks into both EH and AI-Assistant Status files. Don't split.
- [Detect stale Status sections before adding tasks](feedback_refresh_stale_status_sections.md) — Scan Current Status + Focus dates first; offer to refresh when >2 weeks behind reality.
- [Overwhelm usually means miscalibrated priority list](feedback_overwhelm_calibration.md) — When Pedro says overwhelmed, audit red-tagged items first. Too many 🔴 = triage broken, not effort.
- [Read existing KR notes before drafting artifacts](feedback_read_kr_before_drafting.md) — Check `/120 Projects/Work/OKRs/` before drafting anything tied to a KR. The plan is usually already there.
- [Status files are roll-ups not task trackers](feedback_status_rollup_not_tracker.md) — Focus sections link to KR notes. Detailed tasks live in KR notes with Todoist IDs. Don't duplicate.
- [Fetch JIRA via MCP before opining](feedback_jira_mcp_before_opining.md) — When Pedro mentions a JIRA item, use Atlassian MCP to read actual content. Title-based inference is wrong often enough to matter.
- [Defuse vs defer](feedback_defuse_vs_defer.md) — Scope clarity reroutes work, doesn't eliminate it. Frame moved items as deferred (still owed, sourced elsewhere), not defused.
- [Response window for exec questions](feedback_response_window_for_exec_questions.md) — When Bertrand/Loni asks for input ahead of a meeting tonight, the window is 30 min, not 90. Lead with 5-sentence answer matching their literal frame. Deep analysis is for the second window.
- [One artifact per ask — don't proliferate vault files](feedback_one_artifact_per_ask.md) — When Pedro asks for one document, that is the artifact. Don't spawn slide drafts / spec outlines / supporting files. Add sections to the canonical doc instead.
- [Concise plan reminder when user forgets context](feedback_concise_reminder_when_forgotten.md) — When Pedro asks "what was the plan again?", give the move + exit line + 3 questions in 5 sentences max. Not a full restatement.

## Projects
- [AEM Experience Hub](project_experience_hub.md) — Full project context: what it is, team, org, state, risks, top priorities, Obsidian vault location
- [Adobe AEM PM org](project_adobe_org.md) — Reporting chain: User → Bertrand (Sr Director) → Loni (VP PM for AEM)
