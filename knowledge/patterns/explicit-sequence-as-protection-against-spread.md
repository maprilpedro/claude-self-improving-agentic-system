# Explicit Sequence as Protection Against Spread

_Section: Anti-Patterns — part of `patterns/`; router = README.md._
- **Date identified**: 2026-04-02
- **Source**: Pedro's decision to sequence AI Assistant workstream items rather than run them in parallel, April 2, 2026.
- **Observations**: (1) Pedro had 10+ active items across the AI Assistant workstream — Felix integration, hosting, JIRA pipeline, MCP tracking, Ilya sync, VRR definition, etc. (2) Explicit decision: "I don't want to spread too thin." Defined four items in order: Felix changes → hosting → JIRA pipeline → MCP reporting. (3) MCP tracking explicitly parked: "not before items 1–3 are done."
- **Pattern**: Having priorities is not enough. Having a sequence is what prevents spread. A list of 10 orange items all looks equally urgent. A numbered sequence with an explicit "not before X" rule creates a forcing function — you know what to say no to right now, not just in general.
- **Why this matters for Senior Director visibility**: A PM who shows up to every conversation with a clear sequence and a clear "not this yet" signal operates differently than one who is responsive to every new request. Sequence is a form of strategic communication. "We're doing X, then Y, then Z — this new ask is after Z" is a leadership statement, not a deflection.
- **Application**: For any workstream with more than 5 active items, write the sequence explicitly. Not a priority ranking — an actual order. Then apply "not before [previous item]" to everything that isn't at the top.
