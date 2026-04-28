---
name: Fetch JIRA via MCP before opining on overlaps or parents
description: When Pedro mentions a JIRA item, use Atlassian MCP to fetch the actual content rather than reasoning from titles. Title-based inference is wrong often enough to matter, especially for cross-org coordination questions.
type: feedback
---

When Pedro mentions a JIRA item, **fetch it via Atlassian MCP** (`mcp__Atlassian-MCP__jira_get_issue`) before drawing conclusions. Title-based inference misses critical scope details.

**Why:** April 28, 2026 session. Pedro asked about overlaps with AEMEO-9508 (Data Advisory Agent — Shweta Dua's). I started reasoning from the title alone — "telemetry-to-recommendations agent" — and produced a generic overlap analysis. Pedro then pointed out I have JIRA MCP. After fetching, the actual scope was much more concrete: explicitly P42-aligned, Phase 1 includes a "Value Realization" skill (which is exactly what Pedro is building), persona explicitly includes Product Managers, framing positions against "static dashboards" (Pedro's reports), uses MCP Layer (architectural overlap with Pedro's Skills+MCP brief). Title-based reasoning got the rough shape; JIRA-fetched detail got the actionable specifics.

**How to apply:**

- Default to JIRA MCP for any item Pedro mentions in a planning, coordination, or overlap context.
- For batch parent-relationship lookups, use `jira_search` with JQL `key in (...)` then individual `jira_get_issue` calls in parallel for full `issuelinks` data.
- "Implements" relationships (link type ID 10600) outward to DX-XXXX issues identify the H2 initiative parent.
- Confluence MCP (`mcp__Atlassian-MCP__confluence_get_page`) likewise — fetch by `space_key` + `title` or by `page_id` from URL.
- The data is canonical; trust it over inferred or guessed content.

**When to skip:**

- If the item is mentioned tangentially and full detail isn't load-bearing for the response, a quick title-only mention is fine.
- For very simple confirmations (this exists, this person owns it), the search/get can be overkill.
