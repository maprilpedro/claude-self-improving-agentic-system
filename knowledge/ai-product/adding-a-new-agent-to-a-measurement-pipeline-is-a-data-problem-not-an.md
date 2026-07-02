# Adding a New Agent to a Measurement Pipeline Is a Data Problem, Not an Engineering Problem

_Section: Agent Measurement Infrastructure — part of `ai-product/`; router = README.md._
- **Date identified**: 2026-03-25
- **Source**: Felix Delval's aem-agent-reports architecture (agents.yaml, loader.py).
- **Insight**: Once a measurement platform exists with a defined schema, onboarding a new agent is about getting the right data in the right format — not building new engineering. Felix's platform adds an agent with 2 lines of YAML + a CSV in the right schema. The bottleneck is always data access, not code.
- **Application**: When advocating for cross-agent measurement standardization, the question to ask each agent team is: "Can you export your interaction data in this format?" That's it. If yes, the report is days away. If no, that's the gap to close.

---
