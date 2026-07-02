# Peer Review Is Audit, Not Validation — Plan Accordingly

_Section: Stakeholder Communication Patterns — part of `patterns/`; router = README.md._
- **Date identified**: 2026-04-16
- **Source**: Apoorva Gupta agent report review (April 16, 2026). Pedro expected validation; got a punch list instead (50-60% data gap vs Grafana, TSR counting "no result found" as success, tag classification bleeding across agents, missing First Useful Result Rate, no content-type breakdown).
- **Pattern**: When you bring an artifact to a peer PM with a data team (Ankur, Varun), the meeting will almost always be an audit, not a rubber stamp. Their delegates will stress-test numbers, question metric definitions, and find gaps. That's the norm, not the exception. Calling it "validation" before the review sets you up to misreport the outcome to your manager.
- **Anti-pattern**: Walking out of a peer review telling your manager "I got it validated" when in reality you got it audited and now have a punch list. That framing sets a false expectation and damages credibility when the gaps surface.
- **How to apply**: Before any peer review with a data-capable team, plan for audit outcomes:
  1. Name internally (and to yourself) that this is an audit, not a rubber stamp. You are inviting stress-testing.
  2. Calibrate what a successful outcome looks like — specific gap findings, concrete metric improvements, clear next steps. Not a yes/no.
  3. Report the outcome to your manager in audit language: "X's team stress-tested, found gaps, we're closing them." Not "X validated."
  4. The peer who did not push back and said "looks good" either did not engage seriously or has a lower quality bar than your eventual audience. Prefer engaged audit over polite rubber stamp.
- **Senior Director framing**: Director says "I got feedback." Senior Director says "Their team stress-tested the report end to end, found specific gaps, and handed us the exact metric our target audience actually wants." Same meeting, two different framings. Use the second when reporting upward.
