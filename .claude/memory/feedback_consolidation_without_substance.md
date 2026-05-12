---
name: Consolidation request without new substance = hygiene-only output
description: When Pedro asks "consolidate memory" but no new PM events were captured in chat since last consolidation, do hygiene + staleness flags only. Do not fabricate "learnings" from re-reading existing memory.
type: feedback
originSessionId: 8f95b02f-3cd0-4ac9-9348-93f57d663769
---
When Pedro asks "consolidate memory + create session summary" but the session content has been pure recall (no new meeting notes, no Slack drops, no decisions, no fresh observations beyond what was already in memory), the right output is:

1. **Brief session summary noting the gap.** State clearly: hygiene-only session, no new substance captured. List what was re-read, what was checked for movement (git log, vault file timestamps, screenshots), and what was found (nothing new).
2. **Staleness banners on Status & Todo files** if dates have drifted.
3. **Past-due task list grouped by date** to prompt Pedro debrief.
4. **No new memory entries from re-reading.** Re-loading context is not learning.
5. **MEMORY.md untouched** unless a genuine cross-cutting insight emerged.

**Why:** Pedro's feedback rule `feedback_memory_consolidation.md` requires reflection. But reflection without input = invented narrative. The honest move is to mark the gap and request debrief, not to manufacture insights from existing memory.

**How to apply:** Before writing memory or knowledge entries during a "consolidate" trigger, ask: "What did Pedro say in chat this session that I did not already know?" If the answer is "nothing," skip the memory writes and ship hygiene + summary + debrief asks instead.

**Anti-pattern to avoid:** Padding session summary with restatements of prior memory ("Pedro shipped MOC May 6, Bertrand acked..." — already in memory from May 6). Distinguishable from real synthesis because synthesis names a NEW pattern across multiple new inputs.

Origin: 2026-05-12 session — Pedro said "recall" then "review and consolidate." Memory + Status files already covered through May 8. No vault movement between May 8 and May 12. Honest output = brief hygiene summary + staleness flags + past-due asks for Pedro.
