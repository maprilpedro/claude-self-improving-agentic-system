---
name: simple-local-reminders-over-automation
description: For recurring needs, default to a tracked cadence Claude surfaces at session start — not a cloud /schedule routine (remote agents can't see the local vault).
metadata:
  type: feedback
---

For recurring / check-in needs, Pedro prefers a **simple local reminder** — a cadence tracked in `state.md` or the Status file that Claude surfaces at session start — over a cloud scheduled robot. 2026-05-27 he picked this for both the monthly System Review and the weekly Saar-memory check, after I explained a remote routine can't read his local vault.

**Why:** (1) simpler, nothing to manage; (2) a cloud/remote agent runs with only a git checkout — it CANNOT see his Google-Drive Obsidian vault, so any vault-dependent check is half-blind; (3) he wants to run reviews together, locally, with full vault + repo access.

**How to apply:** when a recurring task surfaces, default to tracking the cadence + next-date in `state.md`/Status and surfacing it at session start when due. Reach for `/schedule` (cloud routine) only if he explicitly asks for automation AND the task is repo-only (no vault dependency). Related: [[reference_roadmap_dashboard]].
