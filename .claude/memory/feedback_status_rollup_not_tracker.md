---
name: Status files are roll-ups, not parallel task trackers — applies to both projects
description: EH and AAI Status & Todo files are roll-ups. Detailed tasks live in KR notes (Todoist IDs). Focus sections link to KR notes, never re-enumerate tasks.
type: feedback
---

The Focus — Do in This Order section of each Status & Todo file is a roll-up, not a task tracker. Detailed tasks (with Todoist IDs and dates) live in the KR notes at `/120 Projects/Work/OKRs/`. Duplicating tasks into Status files creates drift.

**Phase 2 split (2026-05-03) — KR note locations:**
- AAI tasks → `O1 - AI Agent Intelligence/` KR notes (Apoorva punch-list KR1, Loni+JM KR3, Priority Consolidation KR4, AEM-AO SLA KR6, etc.)
- EH tasks → `O2 - EH Migration to Personalized/` KR notes (slot already populated; do not create new O2 folder)

**Why:** April 24, 2026 session. First pass at the Focus rewrite inlined full task descriptions. After discovering KR notes — each with a Tasks section containing Todoist-backed `<!-- tid:... -->` entries — Focus was duplicating work the KR notes owned better. Realignment: Focus columns are Item + KR link + Status + Due, not a task list. The KR note is the single source of truth.

**How to apply:**
- When editing either Status & Todo Focus section (EH or AAI), each row should be one load-bearing theme with a `[[KR Note|KR#]]` backlink.
- Do not copy individual tasks from KR notes into Status files.
- When in doubt about Status vs KR placement: detail in KR note, roll-up label in Status.
- Status session logs are still valuable for narrative continuity. KR progress logs are for KR-specific milestones. Both matter.
- Route Status work by project: AAI Status → O1 KR notes, EH Status → O2 KR notes.
