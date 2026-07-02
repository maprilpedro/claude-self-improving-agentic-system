# Grafana vs LangFuse — Two Different Measurement Jobs

_Section: Agent Measurement Infrastructure — part of `ai-product/`; router = README.md._
- **Date identified**: 2026-03-16
- **Source**: Agent Owner Alignment March 16, 2026. Felix, Conrad, Bertrand discussion on tool selection for AI measurement.
- **Insight**: These tools answer different questions and should not be conflated.
  - **Grafana** = usage metrics. Interaction volume, active users, returning users, weekly trends. Good for answering "are people using it?" and "is usage growing?" Does not measure quality.
  - **LangFuse** = quality measurement. LLM-as-judge scoring, prompt clustering, failure mode analysis, multi-turn conversation evaluation. Answers "is the agent doing the right thing?" and "what types of prompts are failing?"
- **The gap**: Neither tool alone is sufficient for a PM-facing agent health view. Grafana tells you how much. LangFuse tells you how well. You need both — and each team must define their own success criteria before either tool produces meaningful signal.
- **Brian's addition**: LangFuse can cluster prompts to understand which categories of prompts are going unanswered or incorrectly answered — this is a direct roadmap input. Unsupported prompt clusters = capability gaps to address.
- **Application**: When building AI measurement infrastructure, decide upfront which tool answers which question. Don't ask Grafana to evaluate quality. Don't expect LangFuse to replace usage dashboards.
