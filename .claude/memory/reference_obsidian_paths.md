---
name: Obsidian vault canonical paths
description: Correct paths for Adobe project folders in the Obsidian vault. Avoids repeated path-not-found errors.
type: reference
---

# Obsidian Vault Canonical Paths

Vault root: `/Users/pedrofer/Library/CloudStorage/GoogleDrive-maprilpedro@gmail.com/My Drive/ObsidianVault/`

## Adobe Project Folders (under `020 Professional/Adobe/Projects/2026/`)

- **Experience Hub:** `Experience Hub/AEM Experience Hub - Project Folder/` — folder name is `Experience Hub`, NOT `AEM Experience Hub`. The `AEM Experience Hub - Project Folder/` is the inner folder. Key files at `AEM EH - Key Files/`.
- **AEM Agents Intelligence (AAI):** `AEM Agents Intelligence/AAI - Project Folder/` — created 2026-05-03 during Phase 1 vault split. Key files at `Key Files/`. Status at `Status and Roadmap/`.
- **Meeting Notes:** `Meeting Notes/` — moved 2026-05-13 from `Experience Hub/AEM Experience Hub - Project Folder/Adobe Projects 2026 Meeting Notes/` to neutral `2026/` level. Shared across EH + AAI + cross-cutting (Bertrand, Felix, Namita, Ian, Yanira, Sorin, Eugene, Fu-Chi, Rubin, Shankari, Loni Meetings, EH Demo, EH Team Sync, Own Reflections).
- **AI-Assistant (retired 2026-05-13):** archived snapshot moved to `Experience Hub/AEM Experience Hub - Project Folder/_archive-2026-05-state-of-project-snapshots/AI-Assistant - Status and Todo_archived_2026-05-03.md`. Top-level `AI-Assistant/` folder deleted.

## Memory Files

- **Symlink works:** `/Users/pedrofer/GitHub/claude-self-improving-agentic-system/.claude/memory/`
- **Direct path fails:** `/Users/pedrofer/.claude/projects/-Users-pedrofer-GitHub-claude-self-improving-agentic-system/memory/` returns "File does not exist" on Read despite symlink.
- **Always use the GitHub repo path** for memory file edits.

## OKR Notes

- `120 Projects/Work/OKRs/O1 - AI Agent Intelligence/` — AAI KRs.
- `120 Projects/Work/OKRs/O2 - EH Migration to Personalized/` — EH KRs.
- `120 Projects/Work/OKRs/O3 - Release Management Agentification/` — EH (EDA / Visual Comparison).
- `120 Projects/Work/OKRs/O4 - Ship Quiet Hours/` — EH (Quiet Hours via Agents).
- `120 Projects/Work/OKRs/O5 - EH Security/` — EH (ASO-Security + permissions auto-optimize).
- `120 Projects/Work/OKRs/O6 - Aging Customers Cleanup/` — EH (90% aging customers cleanup).
- `120 Projects/Work/OKRs/Operations/` — recurring weekly pipelines.
