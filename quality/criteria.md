# Quality Criteria — PM Knowledge System

Testable checks run before marking any task complete. Cut anything that never triggers. Promote anything that triggers 3+ times to "always check."

---

# Category: Stakeholder tracking
## Criteria:
- New person named in conversation → verified they exist in Stakeholder Map, added if not
- Outreach sent → logged with date, channel, and "awaiting response" status
- Response received → status updated from "awaiting" to resolved, next step noted
- Role or context corrected → old entry replaced, not duplicated alongside it
## Severity: blocking
# Source: Session pattern — contacts added mid-conversation, outreach sent but not tracked
# Last triggered: 2026-04-01 (Ilya, Ian, Raul outreach tracking)

---

# Category: Cross-document consistency
## Criteria:
- Any fact that appears in multiple docs updated in all of them, not just one
- State of Project, Stakeholder Map, and Questions docs treated as a trio — if one changes, check the others
- MOC updated when a new file is created or moved
## Severity: blocking
# Source: Session pattern — Austria/Australia correction needed in 2 files; Mircea added to proposal but not to map initially
# Last triggered: 2026-04-01

---

# Category: Action item attribution
## Criteria:
- Every action from a meeting transcript has an owner (Pedro / Sorin / other — not "we")
- Items awaiting external response marked "awaiting" not "done"
- Urgent items flagged 🔴 and appear in the open asks section of State of Project
## Severity: warning
# Source: Session pattern — actions sometimes left unattributed or marked done prematurely
# Last triggered: 2026-04-01 (demo regeneration status corrected)

---

# Category: Decision scope
## Criteria:
- Before acting on anything that affects more than today's task, grep /decisions/ first
- Decisions about *how Claude behaves in this system* → log in /decisions/ with "system" tag
- Decisions about *what Pedro decided on EH or other projects* → log in /decisions/ with "product" tag
- A decision that reverses or supersedes a prior one → Supersedes field filled in, prior file not deleted
## Severity: blocking
# Source: CLAUDE.md Decision Log rule + reflection on scope ambiguity
# Last triggered: never

---

# Category: Session close
## Criteria:
- At natural session end: confirm /decisions/ was checked for any multi-task decisions made
- At natural session end: confirm quality criteria were applied, note any new failure patterns
- Any new failure pattern found → propose new criterion, don't add silently
## Severity: warning
# Source: Reflection — rules only work if there's a forcing function to run them
# Last triggered: never
