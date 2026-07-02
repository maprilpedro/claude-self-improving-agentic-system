# Early MCP Adoption Is Developer-Tool-Led, Not AI-Assistant-Led

_Section: AI Product Risks — part of `ai-product/`; router = README.md._
- **Date identified**: 2026-04-02
- **Source**: AEM Splunk MCP API Analytics Dashboard — odin/{} server, production, last 24h as of April 2, 2026.
- **Data**: 139,068 invocations in 24h. Client breakdown: Unknown 82% (113,772), Cursor 15.6% (21,617), exc_app 2.2% (2,990), Claude 0.5% (670), ChatGPT 0.01% (19). All through one MCP server (odin/{}). 99% US traffic.
- **Insight**: In the current phase of MCP adoption for AEM, developer tools (Cursor IDE) generate 30x more identified invocations than AI assistants (Claude + ChatGPT combined = 689). The dominant use case is developers integrating AEM capabilities into their coding environment, not end users asking AI assistants to act on AEM. The 82% unknown category is the most important measurement gap — identifying it could completely reshape the picture.
- **Performance flag**: P95 latency of 61 seconds on odin/{} is severe. Average is 5,791ms. One in twenty requests takes over a minute — this will limit developer adoption at scale.
- **401 pattern**: ~2,500 unauthorized errors per hour, stable over 24h. Likely misconfigured clients or token expiry — not a spike, a structural issue.
- **Application**: Don't design MCP measurement assuming AI assistants are the primary consumers. As of April 2026, developers are. Track client breakdown over time — when/if AI assistants overtake developer tools is a leading indicator of MCP reaching mainstream use.
- **Terminology note (2026-05-27 review)**: this entry uses the source dashboard's raw word "invocations." For AEM agent/MCP *reporting*, the locked counter-unit is **"Tool Calls"** (never "invocation"/"interaction") — see memory `reference_mcp_terminology`. Different surfaces: this is an external developer-tool-adoption snapshot, not the customer-facing reporting metric. Also: the 139K/24h figure is a single April-2 snapshot — treat as point-in-time, not a trend.
