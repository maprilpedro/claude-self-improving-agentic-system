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
- **AI-Assistant (legacy, will deprecate Phase 2):** `Experience Hub/AI-Assistant/AI-Assistant Status and Roadmap/`. Source for Status & Todo copy → AAI.

## Memory Files

- **Symlink works:** `/Users/pedrofer/GitHub/claude-self-improving-agentic-system/.claude/memory/`
- **Direct path fails:** `/Users/pedrofer/.claude/projects/-Users-pedrofer-GitHub-claude-self-improving-agentic-system/memory/` returns "File does not exist" on Read despite symlink.
- **Always use the GitHub repo path** for memory file edits.

## OKR Notes

- `120 Projects/Work/OKRs/O1 - AI Agent Intelligence/` — AAI KRs.
- `120 Projects/Work/OKRs/O2 - EH Migration to Personalized/` — EH KRs (NOT `O2 - Experience Hub/` — that path does not exist).
