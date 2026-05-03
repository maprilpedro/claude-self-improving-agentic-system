---
name: Mirror tasks rule retired (Phase 2 vault split 2026-05-03) — route by project
description: After EH/AAI vault split, agent-reporting tasks live in AAI Status & Todo only. Do not mirror into EH file.
type: feedback
---

Rule (post Phase 2 split, 2026-05-03): tasks route by project, not by mirror. Agent reporting / AO 2.0 liaison / Felix / Apoorva validation / Rubin / report-to-JIRA / AEM agent intelligence layer → `AEM Agents Intelligence - Status and Todo.md` (canonical AAI status). EH-only items (surface, contribution model, prompting/skills, profiling, Sorin team) → `Experience Hub - Status and Todo.md`. Cross-cutting items go in the project they primarily serve, never both.

**Why:** The original mirror rule (April 23 2026) treated agent-reporting work as cross-surface. Phase 1 split (May 3) carved AAI as its own project. Mirroring is now duplication that drifts. Each file owns one project's task surface clean.

**How to apply:** When the user asks for next-actions and you'd previously have asked "mirror to AI-Assistant Status?" — instead, classify the task to AAI or EH and write to that one file. If genuinely cross-cutting (rare), pick the project that owns the *outcome* and add a one-line cross-reference in the other file pointing to the canonical task. Never duplicate the row text.

The legacy `AI-Assistant - Status and Todo.md` file is deprecated (2026-05-03 banner). Do not edit it. Phase 2 archives it.
