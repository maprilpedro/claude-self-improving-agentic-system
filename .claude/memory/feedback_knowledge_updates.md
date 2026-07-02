---
name: Knowledge folder update cadence
description: Always update knowledge/, INDEX.md, and README.md files when asked, and proactively at least once every 2 days
type: feedback
---

Always update the following when new learnings are available:
- `knowledge/` — relevant domain folders (domain/, patterns/, false-beliefs/, hypotheses/, leadership/, ai-product/, etc.)
- `knowledge/INDEX.md` — sources ingested only (entry counts retired 2026-07-01, access log retired 2026-07-02 — git is the log)
- Root `README.md` — sources ingested, folder list if new folders added
- `projects/adbe-experience-hub/README.md` — keep current with latest project state

**Why:** User explicitly set this as a standing rule. Knowledge compounds over time only if it's kept current. Stale knowledge is worse than no knowledge — it creates false confidence.

**How to apply:**
- When asked to analyze any meeting, document, or session: update knowledge/ as part of the task, not as an afterthought.
- At the start of any session: check the last knowledge commit date (`git log -1 --format=%cd -- knowledge/`). If more than 2 days have passed, proactively update knowledge/ with anything material from recent work before proceeding with the user's request.
- Always git commit after knowledge updates with a `learn:` prefix message.
