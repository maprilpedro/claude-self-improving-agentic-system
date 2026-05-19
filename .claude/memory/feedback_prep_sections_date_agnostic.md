---
name: prep-sections-date-agnostic
description: Name meeting prep companion sections date-agnostic so a reschedule doesn't strand the wikilink anchor
metadata:
  type: feedback
---

When creating a prep companion section inside a Status & Todo file (or any vault note) for an upcoming meeting, name the heading **date-agnostic**: `## <Person> call prep — next`. The inbound task wikilink uses the same anchor: `[[#<Person> call prep — next]]`.

On ingest of the actual meeting, rename the section to `## <Person> call notes — <actual date>` and update the one inbound wikilink to match.

**Why:** Meeting dates move. The Corey call was logged as "May 19" in prep heading + memory + wikilink, then actually landed May 14. Every date-anchored heading + `[[#... May 19]]` link had to be hand-reconciled, and a dangling anchor is easy to miss. A date in a heading is a guess; the anchor should not depend on a guess holding.

**How to apply:** Forward prep sections → `— next`. Reconcile to `— notes — <held date>` only when the meeting actually happens. Past/completed prep sections kept for the record (e.g. Namita 1-1 prep — 2026-05-06) stay as-is — the convention is forward-looking, don't retro-rename closed records. Related: [[feedback_task_vs_progress_log]] (prep = forward, notes = what happened), [[feedback_one_artifact_per_ask]].
