---
name: reference-aem-licensed-customers
description: Where to get the list of licensed AEM customers (IMS org, SKUs, contract status) — the DashDiscovery AEMLicensedCustomers dashboard on DaaS, how to get access, and the other lists that are NOT it.
metadata:
  type: reference
---

**The official source for "licensed" AEM customers is DaaS** (Bertrand, `#aem-mcp`, 2026-06-08: "our official reference for 'licensed' customer (those that we can resolve to a contract)"). The self-service way into it is a Tableau dashboard, not an API.

- **Dashboard:** `AEMLicensedCustomers` in DashDiscovery
  - Overview: https://dashdiscovery.corp.adobe.com/#/views/AEMLicensedCustomers/MainOverview?%3Aiid=1
  - Export view: https://dashdiscovery.corp.adobe.com/#/views/AEMLicensedCustomers/LicensingExploration?:iid=1 (Andre Cascais posted it, `#aem-...` C04MQCRHLBY, 2026-03)
  - Export to XLSX reportedly includes customer, IMS org, tenant, region, solutions, SKUs, contract dates, contract status (FluffyJaws summary, `#aem-data-services-informed`, 2026-08-06; not checked by Pedro yet).
- **Access:** request in EDA Insights, https://edainsights.corp.adobe.com/web/access-request-tile/?id=272&echo=true. Approvers Lydia Puric / Andre Cascais. Sync every ~4h. ✅ **Pedro already has access** via group `TAB_AEM_ENGINEERING_OPERATIONS_EU` (confirmed 2026-10-20). (Thread: https://adobe.enterprise.slack.com/archives/CN6EQPBLK/p1763396158108079)
- **Owners / people:** Andre Cascais (go-to for access), Lydia Puric, Jean-Claude Jung (AEM Data Services). Pedro asked JC + Andre for a named list 2026-08-20, no reply.
- **🆕 The raw tables, named by Sunidhi Azad (DaaS / DPaaS) for Karthik Penikalapati, 2026-10-23** (thread opened by Karthik 10-07 to get AEM org status into Rubin; Pedro defined the three criteria 10-22; https://adobe.enterprise.slack.com/archives/C0BMVMA7DJS/p1791386551198319):
  - **Licensed AEM customers:** `aemds_licensing_gold.aem_licensed_customers`, filter `aem_licensed_customers_is_active = true` (IMS org ID, tenant, SKU, contract dates).
  - **TBYB:** same table, SKU `AEM SITES: CLOUD SERVICE TRIAL` (also `AEM FORMS: CS EDGE DELIVERY TRIAL`).
  - **AI Credits SKU (CX-wide, not AEM-only):** `aemds_licensing_bronze.contract_tenant`, SKU `AEP:OD AGENTS: AI CREDITS`, "about 60 orgs have it in effect today" (10-23). Possibly the same population as Ian's 57 in the denominator list; not confirmed.
  - Access: Genie One (plain-language questions over the data), DPaaS AI onboarding "about 5 minutes", needs VPN. 10-28 16:32 Karthik's Databricks notebook (other workspace) got a 403 IP ACL block; Sunidhi looking at it.
- **Alternatives:** Data Advisory Agent (DAA) can export active AEMCS and AMS customers. Raw tables live in DPaaS / DaaS Next (e.g. `athena_extracts.consolidated_consumption_contract_year_to_date`).

**Lists that are NOT the licensed list** (don't mix them up):
- Raul's Skyline P42 README = classification External / Internal / TBYB / SKU, hand-maintained ([[reference_skyline_p42_orglist]]).
- Paul Midura's rollout files = his "customer list" + exclusion tags (Cat 5, No GenAI, Sensitive Industry, Workfront); AEM CS membership from https://aemcs-workspace.adobe.com/one-customer. He has no Commercial/NFR tag (said so 2026-10-19).
- Shankar Muthan's `DX org details.xlsx` = AEP-entitlement view with an "internal" column; same tool behind the disputed 811.

Related: [[reference_tbyb_sku_entitlement]] (the 24 / 90 / 335 / ~3K denominators).
