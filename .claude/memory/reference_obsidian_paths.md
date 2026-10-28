---
name: Obsidian vault canonical paths
description: Correct paths for Adobe project folders in the Obsidian vault. Avoids repeated path-not-found errors.
type: reference
---

# Obsidian Vault Canonical Paths

Vault root: `/Users/pedrofer/ObsidianAdobeVault/`

## Adobe Project Folders (under `020 Professional/Adobe/Projects/2026/`)

- **Experience Hub:** `Experience Hub/AEM Experience Hub - Project Folder/` — folder name is `Experience Hub`, NOT `AEM Experience Hub`. The `AEM Experience Hub - Project Folder/` is the inner folder. Key files at `AEM EH - Key Files/`.
- **Coworker Lead (ex AEM Agents Intelligence, AAI):** `Coworker Lead/Coworker Lead - Project Folder/` — created 2026-05-03 as `AEM Agents Intelligence/AAI - Project Folder/`, **renamed 2026-10-28** (folders by filesystem `mv`, because the CLI `move` refuses folders; notes renamed through the CLI so wikilinks followed). Key files at `Key Files/` (`Coworker Lead - Stakeholder Map.md`, `- State of the Project.md`, `- Questions for Next 1-1 with Yanira/Namita.md`). Status at `Status and Roadmap/Coworker Lead - Status and Todo.md` (+ three ARCHIVE siblings renamed the same way). Board `Coworker Kanban.md` in the project folder. MOC `Coworker Lead/🎯 Coworker Lead MOC.md`.
- **Release Management (created 2026-10-28):** `Release Management/` — `Release Management - Status and Todo.md`, `🎯 Release Management MOC.md`, plus the notes moved in that day (Rotary 2.0, Rotary - Reduction of Release Validation Effort, FaaS - RV Plugin, Gargantua). ⚠️ `Rotary 2.0` and `Rotary - Reduction…` also exist in `020 Professional/🎯 adobe/` with the same names: link them by full path.
- **Security Health (created 2026-10-28):** `Security Health/` — `Security Health - Status and Todo.md`, `🎯 Security Health MOC.md`.
- **Top index:** `Adobe Projects MOC.md` at the `2026/` level carries a "Main Projects 2026" table with the four MOCs and Status files.
- **Projects Panel** (`120 Projects/Work/📊 Projects Panel.md`, also embedded in `⭕️ 000 — Index`): one card per project folder, read by a dataviewjs view whose format rules are in `120 Projects/Work/_panels/projects/CONTRACT.md` (source of truth `~/GitHub/obsidian-UI/panels/projects/CONTRACT.md`). A card leads with the newer of the `etat` / `etat-date` front matter of the Status and Todo and the newest `## Headline State (YYYY-MM-DD — Title)` of the State of the Project; actions come from the Kanban Doing lane, else the newest `### Focus — YYYY-MM-DD` block. ⚠️ **Learned 2026-10-28:** a block that moves to another project must lose its `Headline State` / `Focus` heading in the old file (renamed "Moved <date> — …"), or the old project's card keeps showing it. Release Management and Security Health have no State of the Project; their cards lead with the `etat` line.
- **Meeting Notes:** `Meeting Notes/` — moved 2026-05-13 from `Experience Hub/AEM Experience Hub - Project Folder/Adobe Projects 2026 Meeting Notes/` to neutral `2026/` level. Shared across EH + AAI + cross-cutting (Bertrand, Felix, Namita, Ian, Yanira, Sorin, Eugene, Fu-Chi, Rubin, Shankari, Loni Meetings, EH Demo, EH Team Sync, Own Reflections).
- **AI-Assistant (retired 2026-05-13):** archived snapshot moved to `Experience Hub/AEM Experience Hub - Project Folder/_archive-2026-05-state-of-project-snapshots/AI-Assistant - Status and Todo_archived_2026-05-03.md`. Top-level `AI-Assistant/` folder deleted.

## Memory Files

- **Symlink works:** `/Users/pedrofer/GitHub/claude-self-improving-agentic-system/.claude/memory/`
- **Direct path fails:** `/Users/pedrofer/.claude/projects/-Users-pedrofer-GitHub-claude-self-improving-agentic-system/memory/` returns "File does not exist" on Read despite symlink.
- **Always use the GitHub repo path** for memory file edits.

## OKR Notes

- `120 Projects/Work/OKRs/O1 - AI Agent Intelligence/` — AAI KRs.
- `120 Projects/Work/OKRs/O2 - EH Migration to Personalized/` — EH KRs.
- `120 Projects/Work/OKRs/O3 - Release Management Agentification/` — Release Management since 2026-10-28 (EDA / Visual Comparison).
- `120 Projects/Work/OKRs/O4 - Ship Quiet Hours/` — Release Management since 2026-10-28 (Quiet Hours via Agents).
- `120 Projects/Work/OKRs/O5 - EH Security/` — Security Health since 2026-10-28 (ASO-Security + permissions auto-optimize).
- `120 Projects/Work/OKRs/O6 - Aging Customers Cleanup/` — Release Management since 2026-10-28 (90% aging customers cleanup).
- `120 Projects/Work/OKRs/Operations/` — recurring weekly pipelines.
