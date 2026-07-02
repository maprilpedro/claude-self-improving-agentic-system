# Three-Tier Tag Taxonomy for Agent Interaction Reports

_Section: AI Agent Reporting Patterns — part of `patterns/`; router = README.md._
- **Source**: AEM agent reporting system (Felix Delval + Pedro), tag review April 7, 2026
- **Date**: 2026-04-07
- **Pattern**: Agent interaction reports become actionable when tags are structured in three distinct tiers:
  1. **request_type** — what the user was trying to accomplish (4-6 per agent). These are the intents. They define the surface area of the agent's use cases.
  2. **custom** — behavioral patterns, edge cases, and context flags (5-7 per agent). These explain how interactions played out, not what was asked.
  3. **value-realization** — confirmed successful outcomes (2-3 per agent). These are the wins — what the agent actually delivered.
- **Anti-patterns to avoid**: (1) Tags that track failures at the orchestrator level (e.g. wrong-agent-routed) belong to the routing layer, not individual agent reports. (2) Value-realization tags that are just past-tense versions of request_type tags add no signal. (3) Input format tags (user provided an ID, user referenced by position) are operational noise for PM purposes. (4) Capability tags ("CF model retrieved") are not value outcomes — something has to land for a tag to be value-realization.
- **When it applies**: Any AI agent or LLM-powered product where you want to understand usage patterns, measure outcomes, and communicate performance to product leadership.
