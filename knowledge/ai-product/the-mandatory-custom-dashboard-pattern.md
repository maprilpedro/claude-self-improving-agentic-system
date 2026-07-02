# The Mandatory + Custom Dashboard Pattern

_Section: Agent Measurement Infrastructure — part of `ai-product/`; router = README.md._
- **Date identified**: 2026-03-25
- **Source**: Felix Delval's aem-agent-reports platform analysis; Bertrand 1:1 notes March 24; Conrad/Gilles Slack March 24.
- **Insight**: Cross-agent measurement works when there is a shared mandatory baseline (same metrics, same definitions, same format across all agents) plus a custom section per agent (the unique signals that matter for that specific agent's use case). The mandatory layer enables comparison. The custom layer enables depth.
- **Mandatory baseline should include**: Technical Success Rate, Value Realization Rate, weekly funnel (interactions → customers → users), week-over-week trend, top failure patterns, top customer orgs.
- **Custom layer examples**: For EPA — file upload success rate, content change acceptance by content type. For Governance — rules/access intent breakdown, "cannot help" pattern analysis.
- **Why this matters**: Without the mandatory layer, no one can compare agents or spot cross-agent patterns. Without the custom layer, the report doesn't serve the agent team.
