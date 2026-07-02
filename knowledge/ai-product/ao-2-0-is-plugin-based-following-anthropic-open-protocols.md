# AO 2.0 Is Plugin-Based, Following Anthropic Open Protocols

_Section: Measuring AI Features — part of `ai-product/`; router = README.md._
- **Date identified**: 2026-04-07
- **Source**: Sergey Generalov email (April 2, 2026) forwarded via Shankari → Bertrand → Pedro. Bertrand 1:1 April 7.
- **Insight**: Agent Orchestrator 2.0 is extensible through plugins using Anthropic's open protocols (same underlying model as MCP). The pattern: install AO locally → create a plugin repo from a marketplace template → add your marketplace to AO settings → iterate on plugins and skills. AO 2.0 is also going open-source with a maintainer/contributor model — teams can send PRs and senior members can become closer contributors.
- **Why it matters for EH**: (1) EH's Skills surface (Priority 1) should evaluate whether to source skills from registered AO plugins rather than a separate mechanism. (2) The plugin/marketplace contribution model may be a cleaner path than the App Builder/iframe approach Mircea demoed March 27. (3) AO 2.0 lands May–July — the timing aligns with the Skills surface redesign window.
- **Key distinction**: Manas Garg = AO engineering lead. Sergey Generalov = PM adjacent to the AO orchestrator (partial ownership). Conrad is the architecture lead. For PM-level AO 2.0 questions, the right contacts are Conrad, Ian Boston, Carsten Ziegeler, and Sergey Generalov — not Sorin (EH engineering).
- **Caution**: AO 2.0 goes deeper than UI. Bertrand's framing: "it's about the underlying reasoning logic." It's not just a frontend upgrade. Form a point of view before presenting to leadership.
