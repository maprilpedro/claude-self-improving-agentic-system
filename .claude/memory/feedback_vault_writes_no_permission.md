---
name: feedback_vault_writes_no_permission
description: Pedro granted permanent permission to update his Obsidian vault (2026-09-27). Do not ask before vault writes.
metadata:
  type: feedback
---

**Pedro, 2026-09-27, verbatim:** *"I dont want you to ask me for permissions on updating my vault - grant them ok forever"*

Done in `~/.claude/settings.json`: `Edit(//Users/pedrofer/ObsidianAdobeVault/**)`, `Read(//Users/pedrofer/ObsidianAdobeVault/**)`, `Bash(obsidian *)`, and the vault added to `additionalDirectories` (needed because `blockReadsOutsideWorkingDirectories` is on). Backup of the prior file at `~/.claude/settings.json.bak-20260927`.

**Why:** the prompts on every Status & Todo / State of the Project append slowed consolidation.

**How to apply:** write to the vault without asking. This covers permission only, not content judgment. The content rules still hold: flag stale sections instead of rewriting them ([[feedback_refresh_stale_status_sections]]), no checkboxes ([[feedback_no_obsidian_task_checkboxes]]), close a note open in Obsidian before editing it ([[feedback_obsidian_reload_after_write]]).
