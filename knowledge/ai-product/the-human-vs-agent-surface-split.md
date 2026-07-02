# The Human vs Agent Surface Split

_Section: Surface Strategy for AI Products — part of `ai-product/`; router = README.md._
- **Date identified**: 2026-03-23
- **Source**: Pedro's contribution in Loni's Session I (March 23), validated by Conrad Woltge. Reinforced in Session IV (March 26).
- **Insight**: AI products need two fundamentally different interaction surfaces: (1) human practitioners who need a guided, visual, discoverable UI; (2) agents and technical users who need direct MCP/API access. Conflating these creates products that serve neither well.
- **Design implication**: Build for humans through hero surfaces (Experience Hub, AI Assistant UI). Build for agents through MCP and API. Don't build a UI that tries to be both. The human surface and the agent surface should be designed independently with callability between them — any capability surfaced to humans should also be reachable via MCP.
- **Connected concept**: Hero surfaces strategy (see below).
