---
name: reference-tbyb-sku-entitlement
description: What TBYB and SKU customers are, who is eligible, the counts and their confidence, and the entitlement contradiction that has never been resolved. Read before quoting any TBYB/SKU figure or defining a comms audience.
metadata:
  type: reference
---

# TBYB vs SKU — entitlement, eligibility, counts

## The definitions

- **TBYB** = Try Before You Buy. Agent access without buying the Agentic SKU.
- **SKU** = the Agentic SKU, purchased.

## Eligibility — SOURCED 2026-08-12, and it has a third category

Source: **Agent Owners Alignment call, 2026-04-13**, recorded on the wiki page `3716634108` → https://wiki.corp.adobe.com/pages/viewpage.action?pageId=3716634108 (owner Yanira Castaneda). Corey asked what to tell Summit lab attendees; **Bertrand gave the eligibility detail and Conrad summarised it.** Verbatim from the page:

> *"AEM cloud service customers are now enabled for 'try before you buy,' while managed services customers are limited to playground access, **with some customers excluded due to contractual or regulatory reasons**."*
> *"Conrad summarized that cloud service customers can use 'try before you buy,' **including edge delivery service customers**, while managed services customers should use playgrounds, and advised Corey to direct further questions to customer success managers."*

So: **Cloud Service (incl. Edge Delivery) → TBYB · Managed Services → playground only · a third, unsized set excluded for contractual/regulatory reasons.**

⚠️ **This supersedes the thinner line in `project_aem_agents_intelligence_ARCHIVE_2026-W22.md:44`** ("Try Before You Buy clarity locked…"), which was banked 2026-05-29 from the same page with no speaker attached and the word "locked" added by Claude. The facts match; the provenance is now real. Attribute to **Bertrand + Conrad, 2026-04-13**, never to "the wiki".

⏳ **Managed Services agents were "not in H1; may land H2"** — and it is now H2. Elham and Yanira discussed the *likelihood* of MS agent support being in the H2 roadmap; that is a discussion, not a decision ([[feedback_proposal_vs_decision]]). **Re-check with Yanira before repeating the playground-only line.**

⚠️ **The field deck contradicts itself on the same axis:** the Governance prerequisite reads *"AEM Assets/Sites on AEM CS"* while its own table shows Brand Governance supported on MS.

## The counts — ✅ NOW PEDRO'S OWN, 2026-08-12

He joined the loaded Skyline P42 list ([[reference_skyline_p42_orglist]], hand-maintained by Raul Hudea) to his own traffic DB. ⚠️ **Approximate — he said the extract re-runs later the same day.**

| Category | Orgs listed | Orgs with traffic | Interactions |
|---|---|---|---|
| TryBeforeBuy | **2,484** | 1,224 (49%) | 41,796 |
| SKU | **335** | 171 (51%) | 20,363 |
| Explorer | 31 | 26 | 5,022 |
| Partner | 19 | 17 | 2,110 |
| Internal | 141 | 83 | 49,305 |
| uncategorized | — | 116 | 2,133 |

**What the table says, and each line is usable:**
- 🔑 **The split itself is the win.** Yanira, Andre (DAS team) and Angela Han had all said SKU vs TBYB could not be separated without a root provisioning API. It can, from the classification list plus traffic.
- **Activation rate is the same both sides** — 49% TBYB, 51% SKU. Paying does not make an org more likely to use it.
- **Intensity differs 3.5×** — 119 interactions per active SKU org against 34 per active TBYB org. That is the value story, not volume.
- 🔴 **Internal is 41% of all interactions** (49,305 of 120,729), more than all TBYB combined, off 83 orgs. **Any headline that does not exclude Internal is mostly Adobe talking to itself** — [[Raw Call Volume Is Mostly the Agent Talking to Itself — Classify Before You Headline]].
- 🔑 **Corey's "~1,500 TBYB" probably reconciles at last** — he was quoting orgs *using* it (1,224), not orgs listed (2,484). The old "do not reconcile publicly" caution can be retired once the extract is final.
- **116 orgs with traffic are in no category.** Report them as unclassified, never redistribute them — Raul's list lags.
- **Explorer still exists: 31 orgs, 26 active.** This answers Bertrand's May question about whether all Explorer customers had migrated to TBYB in the classification. **They have not.**

⚠️ **Terminology:** "Interactions" here is not the MCP-side locked term. [[reference_mcp_terminology]] locks **"Tool Calls"** and bans "interaction" for MCP. If both land in one report, define each column head or the lock breaks.

**Superseded:** Pedro's 2026-07-08 read of 318 SKU / 2,483 TBYB (2,819 total, 18 internal gated out), which was never double-checked by Raul. **It was essentially right.**

## The contradiction that gates the comms audience — STILL OPEN

Two dated statements that cannot both be true:

- **The field's H2 roadmap slide** ("AEM Agents Availability by Skills", updated Apr 2026, sent by Craig Hugo): *"Entitlements: Try-Before-You-Buy (TBYB) or Agentic SKU"* + **"Enrollment required"** per agent.
- **Bertrand, 2026-07-09 17:08:** *"all customers with an AEM cloud (CS/AMS) license should be enabled with agents by default - with the ability to opt-out… So there isn't really any provisioning steps related to the Agents SKU being licensed or not."*

Pedro emailed Bertrand on 07-14 asking him to pick, framed from his own perimeter. **No answer on record.** If TBYB-or-SKU → the migration message goes to the ~318 SKU orgs and the Pedro=SKU / Akin=TBYB ownership split holds. If default-on → the audience is every AEM cloud customer and the split collapses.

## Operationally, the split cannot be measured

SKU vs TBYB **cannot be separated in reporting today.** Provisioning data is AEP-side; **Andre (DAS team) says there is no quick indicator**; Angela Han's bar is a **root provisioning API**, not a weekly spreadsheet. Interim from Venkatesh: two digests, one filtered to the TBYB org list, one to the paid list. This blocks Namita's cohort ordering.

⚠️ **Before quoting any credit figure:** expired promo $0 SKUs were never returned, so those orgs still show unlimited credits. Namita: *"for reporting purposes, it's a little wrong."*

## Dates on the record

Canvas `F0BMUV76DHU` "AEM Agents Road to GA" → https://adobe.enterprise.slack.com/docs/T02CAQ0B2/F0BMUV76DHU — **Coworker onboarding TBYB 2026-08-26 · SKU 2026-09-14.** Both carry a date and **no owner**.

## Other sources

- AEP-side canonical TryBuy artifacts: [[reference_aep_trybuy_artifacts]].
- Classification list: [[reference_skyline_p42_orglist]] (Explorer → TBYB migration completeness never confirmed).

Knowledge: [[Success Definitions Must Be Agreed Before Metrics Are Scaled]] · [[Definition Ownership Is the Moat on Shared Data Infrastructure]].
