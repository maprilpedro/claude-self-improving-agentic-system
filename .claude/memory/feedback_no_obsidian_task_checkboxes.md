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
- The two Status & Todo files were converted the same day on his go (119 + 78 lines → plain bullets; done items keep their `✅ <date>` marker). The ARCHIVE Status files were left as they are.
- Leave the `# Day planner` checkboxes in `050 Sources/daily notes/` alone.
- **Second exception, 2026-10-28, Pedro's choice (option B): the Kanban plugin board** `Coworker Lead - Project Folder/Coworker Kanban.md` (plugin `obsidian-kanban` v2.0.51, installed the same day). The plugin stores cards as `- [ ]` / `- [x]` under `## Todo`, `## Doing`, `## Done`; that format is required there and only there. Card text: `<branch> · <action>, <date>`, branches from the priorities map (Adoption, Commercials, AEM on Coworker, Marketing, Coworker roadmap). Doing holds 3 cards at most.

Related: [[feedback_task_vs_progress_log]] · [[feedback_status_rollup_not_tracker]] · [[reference_local_ai_toolkit]]
