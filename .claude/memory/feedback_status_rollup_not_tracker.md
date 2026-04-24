---
name: Status files are roll-ups, not parallel task trackers
description: Pedro's Status & Todo files are roll-up views. Detailed task tracking lives in KR notes (with Todoist IDs). Focus sections should link to KR notes, not re-enumerate tasks.
type: feedback
---

The Focus — Do in This Order section of each Status & Todo file is a roll-up, not a task tracker. Detailed tasks (with Todoist IDs and dates) live in the KR notes at `/120 Projects/Work/OKRs/O1 - AI Agent Intelligence/`. Duplicating tasks into Status files creates drift.

**Why:** April 24, 2026 session. My first pass at the Focus rewrite inlined full task descriptions. When I discovered the KR notes — each with a Tasks section containing Todoist-backed `<!-- tid:... -->` entries — the Focus section was duplicating work the KR notes already owned better. Realignment: Focus columns are Item + KR link + Status + Due, not a task list. The KR note is the single source of truth.

**How to apply:**
- When editing a Status & Todo Focus section, each row should be one load-bearing theme with a `[[KR Note|KR#]]` backlink.
- Do not copy individual tasks into Status files if they exist in a KR note.
- When in doubt about whether something belongs in Status vs KR note: put the detail in the KR note, put the roll-up label in Status.
- Status session logs are still valuable for narrative continuity. KR progress logs are for KR-specific milestones. Both matter.
