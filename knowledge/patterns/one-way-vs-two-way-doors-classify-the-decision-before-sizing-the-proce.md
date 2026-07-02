# One-Way vs Two-Way Doors — Classify the Decision Before Sizing the Process

_Section: Decision Patterns — part of `patterns/`; router = README.md._
- **Date identified**: 2026-06-18
- **Source**: Chris Dunlop, *Amazon's Secret Weapon: The One-Door vs. Two-Door Decision Framework* (Cub Think Tank), quoting Bezos 2015 Shareholder Letter. Read 2026-06-18.
- **Pattern**: Decisions split into two kinds. **One-way doors** (Type 1) are irreversible or nearly so — made slowly, methodically, with deliberation and consultation. **Two-way doors** (Type 2) are reversible — made fast, by a high-judgment individual or small group, then iterated. The classification step comes *before* the process choice. Match the weight of the process to the reversibility of the door, not to the apparent size of the topic.
- **The real insight is the error asymmetry, not the taxonomy**: people are risk-averse by default, so almost no one makes *too many* one-way decisions. The systemic waste is the opposite — treating two-way doors as one-way. Too many stakeholders, too many 15-30 min meetings, too much deliberation on reversible calls. Bezos's phrasing: "death by a thousand cuts." So the lever is almost always *empower more fast two-way decisions*, rarely *slow down*.
- **Two-way doors people wrongly treat as one-way** (from the article): brand name (Backrub→Google, AuctionWeb→eBay), pricing (adjustable, iterate to market). The "feels permanent" instinct is usually wrong.
- **PM application (Pedro / AEM)**:
  - The visible leadership move is not making the right call — it's *classifying out loud*. In a room that over-deliberates, the person who says "this is a two-way door, we decide now and adjust" is the one leading. That classification skill is a Director→Senior Director signal, and it gives the whole room velocity (Bertrand prefers concrete velocity levers over concepts).
  - Inversion (Pedro's principle): don't ask "what decision should I make." Ask *which of my open items am I treating as one-way that are actually two-way?* Those are the hidden velocity blocks. Unblocking them frees deliberation budget for the genuine one-way doors.
  - Maps to the overwhelm/red-tag triage rule (`feedback_overwhelm_calibration`): a too-large 🔴 pile is often two-way doors mis-tagged as one-way. Reclassify and the pile shrinks — overwhelm is a classification failure, not a capacity failure.
  - P42 instinct already used this: "only Anil can stop-AIA" isolated the true one-way door and deflated the rest to reversible. Name it as a method, not a one-off.
- **Three extensions the Bezos frame misses (carry into AEM decisions)**:
  1. **The "nearly irreversible" gap** is where judgment lives. Platform/reporting choices (Rubin port), public commitments to a customer, a reorg — reversible on paper, costly to undo in practice. Set the seam deliberately.
  2. **One-way by accumulation.** A single two-way is trivial; a thousand two-ways pushed the same direction (architecture choices stacked, tech debt) harden into a de-facto one-way. The frame doesn't cover compounding.
  3. **Political reversibility ≠ technical reversibility.** Reverting a call burns credibility, especially in front of VPs. Some technically-reversible decisions are politically one-way in your org. Audit which.
- **When it applies**: Any decision-sizing moment. Roadmap forks, tool/process adoption, who-decides delegation, meeting-load triage, empowering reports to act without escalation.
- **When it fails**: When reversibility itself is genuinely contested (the "nearly" cases above) — then it's a `What Would Have to Be True?` question, not a snap classification. When the cost to reverse is non-obvious and you classify by topic size instead of measured undo-cost.
- **Related**: Calibration Audit, Reverse-Engineering Strategy ("What Would Have to Be True?"), `feedback_overwhelm_calibration`, `feedback_bertrand_concrete_first`
