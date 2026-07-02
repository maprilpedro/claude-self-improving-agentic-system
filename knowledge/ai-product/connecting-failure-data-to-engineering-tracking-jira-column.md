# Connecting Failure Data to Engineering Tracking (JIRA Column)

_Section: Agent Measurement Infrastructure — part of `ai-product/`; router = README.md._
- **Date identified**: 2026-03-30
- **Source**: Bertrand de Coatpont's response to W13 agent reports, March 30.
- **Insight**: A failure report that doesn't say whether the failure is already tracked is incomplete for an engineering stakeholder. Bertrand's ask: add a JIRA column (number if tracked, "not tracked" if not). This closes the loop between product observation and engineering action.
- **Important caveat**: This column cannot be automated from interaction data alone. It requires a human step — agent PMs mapping known failures to existing JIRAs. Build the column structure first, fill it manually, then automate as tracking matures.
- **Application**: Design failure tables with a JIRA column from the start, even if empty. An empty column signals awareness that tracking is expected. A missing column signals it hasn't been thought about.
