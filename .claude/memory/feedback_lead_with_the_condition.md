---
name: feedback-lead-with-the-condition
description: When a draft or recommendation depends on something unverified, state the condition FIRST — before the deliverable, never in a caveat at the bottom or the last row of an evidence table.
metadata:
  type: feedback
---

When an answer is "X, provided Y", **open with Y.** The condition goes above the deliverable, not below it, and not in the last row of a provenance table.

Format: what is unverified · what breaks if it turns out false · the cheapest way to close it. One short block. Then the draft.

**Why:** Pedro reads top-down and acts on what he reads first. A condition placed after the artifact arrives after the decision. 2026-07-13, the Coworker session: the claim that "Enable Coworker" and the "AI Kill Switch to remove AIA" flags can be set **independently** was an inference — Mark Doten named two separate flags but never said they were independently settable. I buried that warning in the final row of a provenance table, underneath a ready-to-send email draft. Pedro sent the email to Bertrand, Yanira and Jaclyn before the one-line question to Mark went out. Two sentences of that email now depend on an unconfirmed fact, in front of his manager and his manager's peers.

The failure is not that the inference existed. Marking inference is already the rule ([[feedback_voice_drafts_mark_inference]], [[feedback_audit_outward_artifacts]]). The failure is **placement**. A correctly-labelled caveat in the wrong position is an uncommunicated caveat.

**How to apply:**
- Load-bearing condition → first line of the response, before any draft.
- If the condition can be closed cheaply (one Slack line, one file read), say so and offer to close it *before* handing over the artifact.
- Reserve the bottom-of-response evidence table for provenance that does **not** change the action. Anything that changes the action moves to the top.
- Applies to chat feedback, reply drafts, and vault artifacts alike.

Related: [[feedback_confirm_ask_before_producing]], [[feedback_proposal_vs_decision]], [[feedback_dont_overread_vp_quotes]].
