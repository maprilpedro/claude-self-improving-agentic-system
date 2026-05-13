---
name: MCP terminology — "Tool Calls"
description: Locked term for MCP usage measurement on AEM reports + decks. Use "Tool Calls" — never "interaction" or "invocation."
type: reference
originSessionId: c3970bb1-0fc5-47cd-80ee-cd157b1b93c6
---
**Locked 2026-05-06 by Pedro.**

**Use:** `Tool Calls` (capitalized as proper noun in chart labels, narration, slide text).

**Do NOT use:** `interaction`, `invocation`, `hits`, `MCP usage` (when the unit is the metric).

**Why:** Felix flagged 2026-05-06 that "interaction" misleads — apples-vs-oranges with agent interactions. 1 agent interaction = 50K internal calls. 1 Tool Call = 1 tool use. 1 user query may generate 10 Tool Calls. Felix offered two options: "hit" or "tool call" / "tout le call." Pedro chose **Tool Calls**.

**Critical pairing rules (also locked):**
- Do NOT compare agent interactions vs MCP Tool Calls on the same chart.
- Do NOT show per-agent breakdown for MCP (tools tagged, not agents — Discovery uses Content API which sits in Content MCP, attribution ambiguous).
- MCP scope = customer use of MCP on **non-Adobe surfaces** (ChatGPT / Claude). NOT internal AEM agents calling MCP.

**Walk-out line for Loni/JM (May 11 deck):** *"MCP usage is reaction to AEM agents from non-Adobe surfaces. We measure it as Tool Calls, separately from agent interactions, because the units don't compare."*

**Source:** `Meeting Notes/Felix Pedro 1 1/20260506 - Felix Pedro 1 1.md`. Felix verbatim: *"Hit. Je mettrais hit tout simplement. C'est vraiment une API pour agent. Si tu dois faire 3 recherches pour avoir ton truc, c'est 3 hits, tout le call."*
