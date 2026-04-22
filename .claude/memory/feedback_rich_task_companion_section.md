---
name: Rich task format — companion section pattern
description: When the user asks for tasks "with max info and hints," produce one-liner tasks in the Tasks section + a dedicated companion section with full prep (context, opening frames, questions, anti-patterns, logistics, vault links). Never dump multi-paragraph content into the task line itself.
type: feedback
originSessionId: f2f7afb5-77f7-464b-bde1-71b40503f09e
---
Rule. When the user asks to create tasks "with the maximum of info and hints," split the work:

1. **One-liner tasks** in the Tasks section. Standard format with priority icon, due date, short description, and a pointer to the companion section ("See '[name]' section below").
2. **Companion section** (new H2 in the same file) with one H3 block per task containing full prep context.

**Why.** Todoist syncs tasks line-by-line from checkbox format. Multi-paragraph content breaks the sync and clutters task lists. But one-liners alone lose all the preparation value. Split the artifact: one-liners for execution tracking, companion section for strategic prep. Pedro explicitly asked on 2026-04-21 to "rajoute le maximum d'infos et de hint que tu aie" when creating three Senior Director pre-meeting tasks — he wants both the tight tracking AND the rich preparation, not one at the expense of the other.

**What goes in the companion section per task.**

- Why this matters (strategic framing, not restating the task)
- Who / what is the target (stakeholder context, org chain, history)
- Opening frame or script (exact words to use)
- Questions to ask, in priority order
- What to bring to the conversation
- Anti-patterns to avoid
- Logistics (timing, CC list, delivery format)
- Links to related vault docs (Stakeholder Map, State of Project, other KRs)
- The "exit line" or sentence the user should leave with, if applicable

**Senior Director-framed tasks get a prefix like SD-1, SD-2, SD-3** so they're recognizable as strategic scope claims vs tactical execution tasks. Pedro appreciated this distinction when I used it for the pre-May 4 Loni+JM prep.

**Anti-pattern.** Dumping the full rich context INSIDE the task line as a multi-paragraph bullet. Breaks Todoist sync, makes the task list unreadable, and forces the user to scroll through prep content when they just want a task view.
