---
name: Don't promote proposals to decisions
description: Slack threads = surfacing positions, not commitments. Decisions land via designated venues (Conrad directive, Bertrand+Conrad+Teams collegial Phase 4). Don't write "officially abandoned" / "consolidated" / "resolved" without explicit decision signal.
type: feedback
originSessionId: c3970bb1-0fc5-47cd-80ee-cd157b1b93c6
---
**Rule.** When a senior architect / engineer / PM posts a position in Slack, capture it as **proposal** or **position**, NOT as **decision** / **consolidated** / **resolved** / **officially X**.

**Why:** Pedro corrected 2026-05-06 after Claude wrote "A2A officially abandoned" / "MCP-vs-skills tension fully resolved" / "consolidated position" off Carsten Ziegeler's workshop thread message. The message was *"Focusing on MCP/API … seems to be the way forward"* — explicit proposal language ("seems to be"). Decisions in this org land via:
- **Conrad directive to all agent owners** (week of May 12)
- **Phase 4 (Decide) collegial Go/No-Go** — Conrad + Bertrand + Teams
- **Architect call decisions** convened by Conrad (Monday cadence)
- **Bertrand explicit decision** logged

Slack threads / workshop threads are surfacing positions to inform those decisions, not the decisions themselves.

**How to apply:**
- "Carsten proposed" / "Felix's position is" / "Ian's framing" — not "Carsten decided" / "consolidated stance."
- "Direction emerging" / "convergence visible" / "alignment forming" — not "consensus" / "alignment achieved" / "resolved."
- "Slide 3 fork direction = closed (per Carsten's workshop proposal, pending Conrad directive)" — preserve the conditional.
- Quote anchors for May 11 deck: still candidates from positions, NOT validated AEM commitments.
- When in doubt: write "as of [date], [name]'s position is X." Avoid declarative "X is closed."

**Self-check before declarative language:** Was there a directive, a logged decision, a Bertrand-named close? If not, downgrade to "proposal / position / direction emerging."

**Repeat instance 2026-06-01 (CX Coworker).** Claude built a dependency-map artifact labelling Bertrand's May-1 message ("AOv2 is AO+AI Assistant in one box, foundation for CX Coworker … maybe keep AOv2 internal … ?") as **"SETTLED"** facts, and "GA June 11" (Bertrand "I also heard…") as real. Both are framing/hearsay — the source message literally **ends in "?"**. Pedro caught it. Fix applied across map + memory + State of Project (→ "Bertrand's framing, to confirm"). Extra angle this time: also did not establish **who chose the name** before asserting "CX Coworker = AOv2 customer-facing" — the only naming *decision* on record (Amit, drop it from BV demos) cut the other way. **Lesson reinforced:** an exec's casual architecture/naming sentence in chat is a proposal; building a confident artifact on it manufactures false certainty. Mark provenance + "to confirm" on artifacts built from unconfirmed exec framing. Pairs with [[feedback_confirm_ask_before_producing]].
