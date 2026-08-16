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

**URL (full, saved by Pedro 2026-06-30):**
`https://splunk.or1.adobe.net/en-GB/app/TA-aem_skyline/aem_mcp_usage?form.global_time.earliest=-30d%40d&form.global_time.latest=now&form.server_tok=aem&form.server_tok=content&form.server_tok=content-readonly&form.threshold_tok=100&form.regular_days_tok=3&form.new_since_tok=-30d%40d&form.scope_tok=external`

Same Splunk app (`TA-aem_skyline`), different dashboard (`aem_mcp_usage`) = the **One AEM MCP server** usage report. **Internal Splunk — Adobe VPN + SSO required; not fetchable by Claude's web tools.** Filter params: `server_tok` = **aem + content + content-readonly** (the 3 MCP servers tracked), `scope_tok=external` (IMS-org external/internal filter on all tables), `threshold_tok=100`, `regular_days_tok=3` (a "regular" user = active ≥3 days), `global_time`/`new_since` = last 30 days.

**Owners (resolved 2026-06-30 MCP Reporting Strategy meeting):** **Christian Meyer** (= @meyer; owns the dashboard + the external/internal IMS lookup) + **Jabran Asghar** (eng). **Tanju Erinmez** owns the one AEM MCP server itself + the business-reporting skill.

**Architecture (sourced):** two data sources joined **manually** — **AWS logs** (MCP server runtime; carries **tool execution / tool consumption**) + **Splunk** (the corresponding API calls). No automatic AWS→Splunk import yet (Jabran exports ~30 days from AWS as a Splunk lookup). The external/internal IMS-org list = a manual lookup built from "the tool Felix recommended, from Cloud Manager" — **same manual source as Pedro's agent reports** (→ [[reference_skyline_p42_orglist]] fragility).

**Caveat (Pedro + Tanju):** the dashboard leads with **requests** (an HTTP/layer-7 concept) — request counts overstate adoption (~80-90% session setup); the real signal = **tool calls** (locked term → [[reference_mcp_terminology]]). A huge request number can map to ~2 actual tool calls (Pedro's governance example).

**Coordination channel:** ping Jabran on `#am-mcp` (engineering) for data/cells. Full context in `project_aem_agents_intelligence.md` 2026-06-30 MCP Reporting Strategy entry.

---

## 🔑 THE CANONICAL PAIR — Jabran's 2026-07-08 post, re-pointed to Pedro on 07-24

> **Source of record:** Jabran Asghar, `#aem-mcp` `C098RGRNYHW`, 2026-07-08 16:02, ts `1783519340.160459` → https://adobe.enterprise.slack.com/archives/C098RGRNYHW/p1783519340160459
> **Re-sent 2026-07-24 18:24** in group DM `C0BE2P6J00M` (Pedro + Christian + Jabran) → https://adobe.enterprise.slack.com/archives/C0BE2P6J00M/p1784910259601649, verbatim: *"BTW, You are using an older dashboard, these are the ones that you should be using."*

⚠️ **`correct:` — `aem_mcp_usage` (the URL above, saved 06-30 and labelled "the newer dashboard") IS THE OLD ONE.** Jabran superseded it on 07-24. **Use the two boards below.**

**1. AEM Sites MCP — Business value, usage, customers** (the management dashboard; source of the validated 07-24 number set)
`https://splunk.or1.adobe.net/en-GB/app/TA-aem_skyline/aem_mcp_-_management_dashboard_value_usage_customers?form.global_time.earliest=-30d%40d&form.global_time.latest=now&form.server_tok=aem&form.server_tok=content&form.server_tok=content-readonly&form.threshold_tok=100&form.regular_days_tok=3&form.new_since_tok=-30d%40d&form.scope_tok=external`

**2. AEM Sites MCP — Per-customer deep dive**
`https://splunk.or1.adobe.net/en-GB/app/TA-aem_skyline/aem_sites_mcp_-_per-customer_deep_dive?form.customer_tok=*&form.global_time.earliest=-30d%40d&form.global_time.latest=now&form.server_tok=aem&form.server_tok=content&form.server_tok=content-readonly`

**Access:** both live under the `TA-aem_skyline` app in Splunk, available to all — if they do not appear, switch the app selection in Splunk (Jabran to Hiroyuki Miyata, 07-09). VPN + SSO required; not fetchable by Claude.

🔴 **THE STALENESS TRAP, AND IT IS THE ONE THAT BITES BEFORE A REPORTING CYCLE.** The AWS→Splunk import is **manual** — Jabran uploads the last 30 days as lookup data by hand. On 2026-07-24 he said *"I haven't done that in last few weeks"*, which is what produced Pedro's phantom "345k → 48k collapse" and the "32 → 445 orgs" jump. **Before pulling any number for a status, a video or a deck, ping Jabran to refresh the lookup first.** Automation tracked in `LOGREQ-16791`.

⚠️ **Two more handling rules, both Jabran's own words (07-24):** wait for the **blue spinning circles** on every panel to disappear before treating a number as final, and **use the 30d window only** — *"found a bug in some panels not respecting the time filter, will fix that next week"*. **No fix confirmation since**, so re-verify before trusting any other window.

📎 **Two PDF snapshots exist in the 07-08 thread** — the full management report (`F0BFQTHNUR5`, 07-09 09:49) and an Eli Lilly per-customer deep dive (`F0BFW2N6CPP`, 07-08). ⚠️ Snapshot dated windows, not live.

**✅ 2026-07-24 — THE VALIDATED MCP NUMBER SET (use these; earlier same-day partials were wrong-filter/transient).** Source = the management dashboard `aem_mcp_-_management_dashboard_value_usage_customers` ("AEM Sites MCP — Business value, usage, customers"), last 30d, external, aem+content+content-readonly. Pedro's decision: "on part sur ces données validées."

| Metric | Value |
|---|---|
| Authenticated requests (reach/transport) | **1,603,452** |
| Total tool calls (actions) | **95,898** |
| **Specific (value-bearing) tool calls** | **~67K (~70% of tool calls)** — read off the class bar; hover for exact |
| Generic tool calls | ~29K (~30%) |
| Active IMS orgs | **1,202** (1,091 on One AEM MCP) |
| New customers (first-seen 30d) | **679** |
| Regular customers (active ≥3 days) | **857** (82% regular share of active orgs) |

**The clean funnel:** 1.6M requests → 95,898 tool calls → ~67K specific value calls (~17 requests per tool call = setup/polling overhead; then 70% of tool calls are named value actions). MCP client mix ≈ overwhelmingly **Claude**. Top orgs by requests: TORC Robotics 11,767 · Kawasaki Motors Europe 10,075 · Capella 8,241 · Canon Medical 7,645. Per-customer intent varies: Eli Lilly 64% read / 21% discovery / 14% write · Air India 32/36/30 · Fabletics 89% write · NBC Universal 95% read.

⚠️ **The 1.6M is authenticated + successful requests — a legitimate reach number, NOT raw all-status noise** (an earlier read of this claim was wrong and is corrected here). The overhead lives in the ~17:1 request→tool-call ratio (session setup/polling), not in rejected traffic. **⚠️ DISCARD earlier same-day screenshots (47,307 req / 530 orgs; 34,936 req / 22 orgs / 9 regular)** — transient partial-filter states; the management-dashboard set above is the validated one (95,898 tool calls + 679 new were stable across every read). **Cards show no WoW/MoM → no valid delta this cycle; the validated instrument's baseline starts here, deltas begin next cycle.** **Still do NOT compare to the "~345k Content-MCP invocations / 152 customers" from the 6/24 status** — that is Christian Meyer's separate Content-MCP number (relayed by Gilles, 06-24 DM), a different instrument, layer, and scope. Value-metric-migration play banked in knowledge/leadership/ [[migrate-leadership-from-a-volume-metric-to-a-value-metric-without-a-cliff]].

**Dashboard URLs (internal Splunk, VPN+SSO):** value/usage/customers = `.../aem_mcp_-_management_dashboard_value_usage_customers` · raw usage = `.../aem_mcp_usage` (both `TA-aem_skyline`, same filter params).
