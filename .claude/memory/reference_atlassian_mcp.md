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
- 🔴 **2026-08-17 — THE CONFLUENCE HALF CAN DIE WHILE JIRA KEEPS WORKING, AND ITS ERROR MESSAGE LIES.** `confluence_get_page` returned *"There is no content with the given id, or the calling user does not have permission to view the content"* for **every** id tried, including `3815569799` (Brand Concierge), which this file records as previously readable. `confluence_search` returned **HTTP 404**. In the same session `jira_get_issue` worked normally. → **the whole Confluence side was down, not one page's permissions.**
  - **Diagnose in this order, it takes 30 seconds.** (1) hit any *known-good* page id, not only the one asked for; (2) run `confluence_search` — a **404 means the Confluence endpoint itself, not a permission**; (3) call a JIRA tool to see whether the connector is authenticated at all.
  - **Read the error literally and do not repeat it to Pedro as "you don't have access to that page".** It is Confluence's generic 404/403 string and it says nothing about that page.
  - **Network is a separate axis.** `curl` on `wiki.corp.adobe.com` returned **302 → `login.action?...&permissionViolation=true`**, i.e. host reachable, request simply anonymous. **A reachable host plus a working JIRA plus a dead Confluence = connector config, not VPN and not the page.**
  - ⚠️ **Retro-suspect earlier "no-permission" notes** — the `4003355459` OBO-options wiki was banked in `watches.md` as *"Confluence MCP no-permission"*. That may have been this same failure, misdiagnosed at the page level.
  - **Fallback while it is down:** ask Pedro to paste the page or an export. Do not present the wiki as unreachable in principle.

**How to apply:**

- Default to fetching when Pedro references a JIRA / Confluence URL or key.
- For overlap analysis or parent lookups, JIRA MCP > guessing from titles. See `feedback_jira_mcp_before_opining.md`.
- Tools are deferred — load schema via `ToolSearch` first if not already in context.
