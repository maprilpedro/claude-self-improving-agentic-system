---
name: feedback_separate_facts_from_proposals
description: "In architecture/strategy artifacts, keep as-is facts and Pedro's proposals in separate diagrams/notes; never let a bet read as a fact."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 3e3672fd-917a-4a1a-8ba1-3639ebfba122
---

When building any architecture or strategy artifact (diagrams, decks, maps), keep **what exists (facts)** and **what Pedro proposes (bets)** physically separate — separate diagrams, ideally separate notes/pages. Within a diagram, encode the distinction visually: **color = ownership**, **dashed border = proposal or inferred**. Tag a real-but-unbuilt thing `[to rebuild]`, a live ticket `📌`, an inferred/undecided item `🔶` — but never paint a proposal in the same solid style as a sourced fact.

**Why:** Pedro repeatedly caught the mix in the 2026-06-17 Coworker diagrams — light/deep model, "EH claimable", `skills.yml`-as-index were rendered like sourced facts. At exec speed a reader (Bertrand, Manas, Felix) can't tell a bet from reality, and a proposal mistaken for a fact destroys credibility. This is the artifact-level twin of [[feedback_voice_drafts_mark_inference]] (mark inference in his-voice drafts) and [[feedback_confirm_ask_before_producing]] (don't characterize a source unread).

**How to apply:** Default to a two-part structure — "as-is (facts only)" + "enhancements (proposals)". Make the facts half shareable broad; keep the proposals half for sponsor + close allies ([[feedback_position_over_merit]] — control the narrative, don't broadcast the full hand). State a one-line convention at the top so the reader knows what dashed/color/emoji mean. Sourced metrics (e.g. adoption %) belong in their own context, not pasted into an architecture diagram.
