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
