---
name: feedback-no-obsidian-task-checkboxes
description: Pedro does not use Obsidian tasks. Never write `- [ ]` / `- [x]` checkbox lines into the vault (journals, notes, Status files). Plain bullets, dates in words. Ruled 2026-09-22.
metadata:
  type: feedback
---

# No Obsidian task checkboxes in the vault

**Rule (2026-09-22):** *"je n'utilise pas les tasks dans obsidian, donc il faut clean tout ce que tu y avais [mis]"*. Claude never writes `- [ ]`, `- [x]`, or Tasks-plugin emoji syntax (`📅 2026-…`, `✅ 2026-…`) into vault notes. Follow-ups are plain bullets with owner and date in words.

**Why:** the checkboxes were Claude's habit, not his. He has no Tasks plugin, does not query them, and the `Day planner` lines in daily notes are the only checkboxes he owns (the day-planner plugin's template). 313 checkbox lines across 37 journal entries were converted to plain bullets on 2026-09-22; the `/journal` skill (repo `.skillshare/skills/journal/`, deployed global via `cron/deploy_skills_global.sh`) was patched the same day so the scheduled runs stop producing them.

**How to apply:**
- Journal, digest, meeting-note, memory-to-vault writes: `- <action> — owner — due <date>`, never a checkbox.
- The two Status & Todo files carry ~200 `- [ ]` / `- [x]` lines in their Todo sections; whether those convert too is Pedro's call (asked 2026-09-22, pending).
- Leave the `# Day planner` checkboxes in `050 Sources/daily notes/` alone.

Related: [[feedback_task_vs_progress_log]] · [[feedback_status_rollup_not_tracker]] · [[reference_local_ai_toolkit]]
