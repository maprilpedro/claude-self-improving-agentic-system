---
name: Splunk MCP usage dashboard
description: Splunk dashboard tracking MCP API usage in AEM — Bertrand's go-to for MCP adoption metrics
type: reference
---

Splunk dashboard tracking MCP tool usage in AEM production environments.

**URL:** https://splunk.or1.adobe.net/en-GB/app/TA-aem_skyline/api_router_-_mcp_usage

**What it tracks:** MCP call volume via the API router, filterable by environment type (prod) and MCP server.

**Why it matters:** Bertrand shared this April 2, 2026 as the source for the MCP side of his adoption ratio ask (MCP edits vs. Content Management UI edits). When MCP adoption metrics come up, start here — no new instrumentation needed.

**Paired metric needed:** Content Management UI activity (authoring edits — pages, content fragments, assets). Owner unknown as of April 2 — try #dx-product-measurement or ask Sorin.

---

## One AEM MCP usage report (the newer dashboard — 2026-06-30)

**URL (saved by Pedro 2026-06-30, query string partly truncated in source):**
`https://splunk.or1.adobe.net/en-GB/app/TA-aem_skyline/aem_mcp_usage?form.global_time.ea[…]_tok=3&form.new_since_tok=-30d%40d&form.scope_tok=external`

Same Splunk app (`TA-aem_skyline`), different dashboard (`aem_mcp_usage`) = the **One AEM MCP server** usage report. Filters seen: `scope_tok=external` (the IMS-org external/internal filter applied to all tables), `new_since_tok=-30d@d` (last 30 days).

**Owners (resolved 2026-06-30 MCP Reporting Strategy meeting):** **Christian Meyer** (= @meyer; owns the dashboard + the external/internal IMS lookup) + **Jabran Asghar** (eng). **Tanju Erinmez** owns the one AEM MCP server itself + the business-reporting skill.

**Architecture (sourced):** two data sources joined **manually** — **AWS logs** (MCP server runtime; carries **tool execution / tool consumption**) + **Splunk** (the corresponding API calls). No automatic AWS→Splunk import yet (Jabran exports ~30 days from AWS as a Splunk lookup). The external/internal IMS-org list = a manual lookup built from "the tool Felix recommended, from Cloud Manager" — **same manual source as Pedro's agent reports** (→ [[reference_skyline_p42_orglist]] fragility).

**Caveat (Pedro + Tanju):** the dashboard leads with **requests** (an HTTP/layer-7 concept) — request counts overstate adoption (~80-90% session setup); the real signal = **tool calls** (locked term → [[reference_mcp_terminology]]). A huge request number can map to ~2 actual tool calls (Pedro's governance example).

**Coordination channel:** ping Jabran on `#am-mcp` (engineering) for data/cells. Full context in `project_aem_agents_intelligence.md` 2026-06-30 MCP Reporting Strategy entry.
