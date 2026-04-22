---
name: Task vs progress log distinction
description: When the user asks for a new task to be tracked, log it as a forward-looking task (not a past-tense progress entry). Progress log = what already happened; Tasks = what needs to be done.
type: feedback
originSessionId: f2f7afb5-77f7-464b-bde1-71b40503f09e
---
Rule. When the user says "track this" or "add a task" or "I need to do X," record it as an open task (checkbox, due date, priority). Do not write it as a progress log entry as if it were already a decided past event.

**Why.** On 2026-04-21 Pedro asked me to track a new action he wanted done that day (the Mike Tilburg link button). I wrote it as a progress log entry dated 2026-04-21 with narrative past-tense framing ("tracked as outside-sign-off agent-owner relationship. Implementing link button..."). Pedro corrected: "I asked for a new task to be done today, you logged it in progress log." The progress log is for things that already happened. Tasks are for things to do.

**How to apply.** When the user says to track an action.

- Add a `- [ ]` task line with priority icon, due date, and concise description. Put it in the Tasks section of the relevant doc.
- Do NOT add a narrative "tracked as X, implementing Y" line to the Progress Log until after the work is actually done.
- After the work ships, THEN add a progress log entry summarizing outcome and lessons.

**Quick check before writing.** Is this thing I'm about to write describing the past or the future? If future, it's a task. If past, it's a progress log entry. Don't mix.
