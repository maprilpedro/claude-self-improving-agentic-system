---
name: Session start behavior for this project
description: When starting a conversation in this project, pick up where we left off across Pedro's four projects (Coworker Lead, EH, Release Management, Security Health; set 2026-10-28)
type: feedback
---

When starting any conversation in this project, immediately pick up where we left off — no need to ask. Read repo memory + key Obsidian files to orient, then give a concise status update covering the four projects, then ask what to work on.

**Why:** Pedro's work spans four projects since 2026-10-28 (his call, "J'ai 4 projects principaux"): **Coworker Lead** (ex AEM Agents Intelligence, AAI), **AEM Experience Hub (EH)**, **Release Management** and **Security Health**. Before that it was two (EH + AAI, split 2026-05-03). Starting fresh creates friction and forces Pedro to repeat himself. Which project currently leads shifts over time — read it from state.md + the Status files, don't hardcode a tilt.

**How to apply:** On every session start in this project:
1. Load the four project memory files from `.claude/memory/`: `project_aem_agents_intelligence.md` (Coworker Lead, filename kept), `project_experience_hub.md`, `project_release_management.md`, `project_security_health.md`.
2. Pull current state from the canonical Status & Todo files (vault paths under `020 Professional/Adobe/Projects/2026/`): `Coworker Lead/Coworker Lead - Project Folder/Status and Roadmap/Coworker Lead - Status and Todo.md` (+ the board `Coworker Kanban.md` in the same project folder), `Experience Hub/AEM Experience Hub - Project Folder/AEM EH Status and Roadmap/Experience Hub - Status and Todo.md`, `Release Management/Release Management - Status and Todo.md`, `Security Health/Security Health - Status and Todo.md`.
3. Present 1-3 lines per project + open threads, then ask which to work on. For Coworker Lead, use the priorities order Adoption, Commercials, AEM on Coworker, Marketing, Coworker roadmap ([[project_aem_agents_intelligence]] 2026-10-28 block).
4. If one project currently leads (per state.md / Status files), lead with it and keep the others brief — but derive that from current state, not a fixed date.
