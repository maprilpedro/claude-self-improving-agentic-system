# Agentic Extensions Have a Token-Cost Hierarchy

_Section: Distributed-Harness Architecture (AOv2 / Agentic NorthStar) — part of `ai-product/`; router = README.md._
- **Date identified**: 2026-05-22
- **Source**: Ian Boston, *Claude Token costs* blog (wiki, 2026-05-20) + the ClaudeCode deep-dive token-economics breakdown he cites.
- **Insight**: Every active extension costs tokens **every turn, even when its tools are never called** — and the cost varies by an order of magnitude: hooks **0**, skills **~200-500**, plugins **~500-2K**, **MCP server manifest ~2K-15K**. Context window ~200K; conversation history is the largest segment (40-60%); compaction reclaims budget but trades information quality. Five MCP servers can permanently cost 50-75K tokens of history.
- **Implication**: architecture decisions are token-budget decisions. **Prefer skills (and hooks) over MCPs**; an MCP earns its manifest cost only for a high-value, unique capability (e.g. a shared memory service). A memory-as-MCP must keep its manifest lean and return ranked, relevant context, or it becomes the bloat it is meant to serve. Reinforces the skills-over-MCP consensus (Trent / Carsten / Felix Meschberger).
- **Cross-link**: [[Everything Is a Skill — the "Agent" Dissolves as a Build Unit]], [[Moat = the Data, Not the Mechanism]].
