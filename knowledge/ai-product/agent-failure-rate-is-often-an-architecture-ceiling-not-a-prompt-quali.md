# Agent Failure Rate Is Often an Architecture Ceiling, Not a Prompt Quality Problem

_Section: Measuring AI Features — part of `ai-product/`; router = README.md._
- **Date identified**: 2026-03-23
- **Source**: Loni's AEM PM Virtual Working Session I (Agents, March 23). Cedric Huesler confirmed.
- **Insight**: A 40-50% agent failure rate can look like a prompting problem. It often isn't. If agents route to a solution without reasoning through one, there is a structural ceiling on quality that no amount of prompt tuning will raise. In AEM, the current architecture routes — it doesn't reason. AO 2.0 adds agent loop reasoning. Until it lands, the failure rate has a floor.
- **Why it matters for PMs**: If you frame a quality problem as a prompting problem, you will burn cycles on the wrong fix and fail to communicate the real root cause to leadership. Framing it as an architecture ceiling does two things: it stops wasted effort, and it sets a realistic timeline (the fix arrives with AO 2.0, not the next sprint).
- **How to communicate it**: "The current agents route to a solution — they don't reason through one. This is a structural ceiling, not a prompt quality problem. AO 2.0 addresses the root cause. Expected: May at earliest, June-July realistic."
