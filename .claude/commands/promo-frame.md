---
description: Take a tactical event (a meeting, a Slack reply, a JIRA update, a stakeholder move) and reframe it through the Senior Director promotion lens. Routes to pm-strategic.
---

Invoke the **pm-strategic** subagent for the following task.

User's request: $ARGUMENTS

Steps:
1. Read `knowledge/INDEX.md` to route.
2. Read `leadership/` (Senior Director patterns) and `interpersonal/` if a person is named.
3. Read `hypotheses/active.md` and test the event against whichever hypotheses are currently active — don't assume which ones; the roster changes at each System Review.
4. Read `.claude/memory/project_experience_hub.md`, `project_aem_agents_intelligence.md`, and `project_adobe_org.md` for current project + org context.
5. Reframe the event:
   - What altitude does it actually live at (tactical / strategic / political)?
   - Does it advance, stall, or threaten the Senior Director track?
   - Is there a recurring pattern? (If yes — flag for promotion to `patterns/` after 2+ observations.)
   - What's the move?
6. If the event represents new evidence for an active hypothesis, propose updating it.
7. If it contradicts a pattern or false-belief, propose demoting / annotating.
8. End with a one-line tactical follow-up if action is needed: "Tactical follow-up: invoke pm-tactical to [X]."

Do not edit JIRA, Status files, or KR notes. Strategic agent works at the frame, not the task layer.
