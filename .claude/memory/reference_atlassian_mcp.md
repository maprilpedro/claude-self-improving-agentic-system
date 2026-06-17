---
name: atlassian-mcp-jira-confluence-tools-available
description: "Pedro's environment has the Atlassian MCP server connected. Use it to fetch real JIRA + Confluence content (Adobe corp instance, internal-only)."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 3e3672fd-917a-4a1a-8ba1-3639ebfba122
---

**Tools available** via the `mcp__Atlassian-MCP__` namespace:

**JIRA:**
- `jira_get_issue` — fetch by key, with `fields` parameter (use `*all` for everything; specific list to limit; default = essentials). Returns description, status, assignee, reporter, labels, components, **issuelinks**, custom fields. Use `comment_limit: 0` to skip comments.
- `jira_search` — JQL queries. `key in (...)` for batch lookups. Default fields are basic; pass `fields="*all"` for full data.
- `jira_get_issue_links`, `jira_get_transitions`, `jira_create_issue`, `jira_update_issue`, `jira_add_comment`, etc. — full CRUD if needed.

**Confluence:**
- `confluence_get_page` — fetch by `page_id` (preferred, from URL) or by `space_key` + `title`. Set `convert_to_markdown: true` for clean text. Default fetches metadata + content.
- `confluence_search` — CQL queries.
- Full CRUD: create_page, update_page, add_comment, etc.

**Adobe-specific notes:**

- JIRA instance: `jira.corp.adobe.com` — internal, not reachable from public-internet tools, MCP is the only way.
- Confluence instance: `wiki.corp.adobe.com` — same constraint.
- "Implements" relationship (link type ID 10600) is how H2 roadmap items map to DX-initiative parents.
- DX-XXXX numbers are H2 2026 initiatives (DX-1217 Sites Optimizer, DX-1218 Run The Business, DX-1220 Agentic Web, DX-1222 Product Adoption, DX-1223 Operations & Efficiency, DX-1233 S&O Strategy & Comm, DX-1219 Security, DX-1221 Customer Success).
- Some items have stale parents in JIRA — e.g. LLMO-4141 has JIRA parent DX-1134 (Closed) while Slack source doc places it under LLMO-4023.
- **🔴 `confluence_create_page` has NO view-restriction parameter** (takes only `space_key` + `title` + `content` + optional `parent_id`/`content_format`/`emoji`). The MCP **cannot make a page private.** To publish something sensitive: create it in Pedro's **personal space** (restricted to him by default), or set view-restrictions **manually in the Confluence UI** right after creation. Never assume an MCP-created page in a team space is private. (Surfaced 2026-06-17 publishing the Coworker proposals page.)
- **Token expires** — `confluence_search` / page calls return `401 Authentication failed` when the connector token lapses. Fix = re-auth the Atlassian connector (claude.ai → Connectors), not retry. Hit 2026-06-17.

**How to apply:**

- Default to fetching when Pedro references a JIRA / Confluence URL or key.
- For overlap analysis or parent lookups, JIRA MCP > guessing from titles. See `feedback_jira_mcp_before_opining.md`.
- Tools are deferred — load schema via `ToolSearch` first if not already in context.
