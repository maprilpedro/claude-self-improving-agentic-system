---
description: Sync a JIRA item — fetch via MCP, reflect changes in the corresponding KR note + Status file. Optionally update fields / add a comment. Routes to pm-tactical.
---

Invoke the **pm-tactical** subagent for the following task.

User's request: $ARGUMENTS

Steps:
1. Parse $ARGUMENTS for JIRA ID(s) and the requested action.
2. Read the JIRA item via Atlassian MCP (`jira_get_issue`). Don't infer from title.
3. If $ARGUMENTS includes an update (status change, comment, field edit), apply it via MCP.
4. Read `.claude/memory/reference_okr_structure.md` to find the relevant KR note.
5. Read the KR note. If the JIRA item maps to a task or progress entry, update the KR note accordingly.
6. Read the relevant Status & Todo file (EH or AAI — pick by the project that owns the outcome).
7. If the work touches both projects, route the task to the owning project only and add a cross-reference in the other file's Focus — never duplicate rows (mirror rule retired 2026-05-03, per `feedback_mirror_tasks_across_status_files.md`).
8. End with a 2-line summary: what changed in JIRA + what changed in the vault.

Do not load the `knowledge/` folder. If the request implies strategic framing (positioning, narrative), stop and tell Pedro to use `/promo-frame` instead.
