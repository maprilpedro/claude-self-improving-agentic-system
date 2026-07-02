# Technical Success Rate vs Value Realization Rate — They Are Not the Same

_Section: Measuring AI Features — part of `ai-product/`; router = README.md._
- **Date identified**: 2026-03-24
- **Source**: EPA vs EGA report cross-analysis; Felix Delval's measurement infrastructure; Bertrand 1:1 March 24; Conrad/Gilles Slack March 24.
- **Insight**: Two agents in the same org can report 9% and 75% success rates and both be telling the truth — because they're measuring different things. EPA measures whether a user accepted a proposed content change (behavioral, hard bar). EGA measures whether the agent returned non-empty content (content signal, lower bar). These numbers are not comparable without context. Cross-agent comparison without a shared definition of success creates a false picture.
- **TSR (Technical Success Rate)**: Did the agent complete the requested action without an error? Binary. Easy to compute. Low bar. Tells you the system worked. Doesn't tell you if it was useful.
- **VRR (Value Realization Rate)**: Did the user actually get value? Higher bar. Requires behavioral signal (user accepted, acted on, returned to use again). Harder to define and measure. The metric that matters to customers and leadership.
- **Application**: Any cross-agent measurement standard must agree on TSR and VRR definitions before publishing numbers. Without this, comparing agents misleads everyone, including the agents' own teams.
