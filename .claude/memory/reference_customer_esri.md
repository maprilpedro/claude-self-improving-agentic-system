---
name: reference-customer-esri
description: Esri as an AEM Assets + Coworker customer — the 09-15 "AEM product team sync" notes (Pierre Tager), the credit-governance complaint Corey escalated 09-19, Bertrand's answer (Rubin per-org dashboard, Horia), the 150K-credit Experience Modernization pilot. Read before any Esri or "credit attribution" conversation.
metadata:
  type: reference
---

# Esri (the customer) — what memory holds

Saved 2026-09-22 from the email thread *"ESRI feedback on CW"* Pedro pasted (Corey Dulimba → Tina Ngo, Cedric Huesler, Bertrand, Pedro, cc Pierre Tager, 2026-09-19 00:32; Bertrand 09-20 23:12; Pierre 09-22). Source notes: Pierre Tager's AI-generated minutes of the Tuesday 2026-09-15 *AEM product team sync* (series he set up 2025-02-26 "to discuss how Adobe can help making ESRI successful using AEM Assets"), sent 09-18 15:53 PT. Org: `ED8D65E655FAC7797F000101@AdobeOrg`, region `va7` (from Bertrand's Rubin link). **In `20260820-AEM_COHORTS.xlsx` (Cohorts tab, 09-22 lookup):** cohort `Cohort_AEM_WF_INT`, reason `workfront-explorer`, **audience External**, Workfront customer = Yes, Target customer = Yes, CW activated **Ad Hoc** ("Already Provisioned - Ad Hoc; Workfront Customer"), TBYB activation date **2026-02-10**, agentic path Try Before You Buy, AEMCS-licensed, program present, ECCID 21275, GenAI status "Providing the Service Only (Oct 25 Rider)", industry Software & IT Services. Also on the *Opt-In Requests* tab: ESRI, requested by Corey 2026-08-26, "ASAP", via `cx-coworker-questions@adobe.com`. ⚠️ The `audience` column is the workbook's copy of Raul's classification, not the README itself (VPN-only).

## The complaint, verbatim substance (Jeff Troccoli, Esri, 09-15)

- **Credits burn fast, nobody can say who or why.** Esri at **91% of available credits**; one spike of **~4,000 credits** with no user, activity or business value attached. Andy Petersen: "Coworker credits are being used very quickly."
- **Governance gap.** Adobe's monitoring "does not provide sufficient granularity to restrict access, identify who consumed credits and why, or connect actions to measurable outcomes"; credits sit in "a shared pool", so targeted purchases cannot be justified.
- **The Copilot comparison.** With Microsoft Copilot "access requires justification, usage can be monitored, and problematic access can be audited and disabled." Esri does not have that problem there.
- **ROI they can estimate:** Experience Modernization and metadata management (developer and page-author time savings). What they cannot do: link specific actions → credit consumption → value. Pierre: Adobe "may need to connect usage and value more directly… a broader shift from usage-based AI pricing toward outcome-based models."
- **Purchase:** PO justification done for **150,000 credits** for the Experience Modernization Agent pilot (~900 pages, discounted credits, per the 09-14 agenda); PO approved on Esri's side, credits not yet visible in the account as of 09-15 (Sam Davis to confirm receipt; order carried a 09-25 expiration).
- Pierre's own action item: *"Investigate options for restricting, attributing, and reporting Coworker and Adobe AI credit consumption so Esri can connect usage to business value and ROI."*

## What Adobe did with it

- **Corey 09-19** forwarded it as "continued concerns on access control and credit usage" — *continued*, so not the first time.
- **Bertrand 09-20:** "I'll bring this up with Horia and team — this must be a very generic ask across all Coworker customers." And to Pierre: the Rubin **agent-usage dashboard filtered per org** (`rubin.adobe.io/dashboard/agent-usage-dashboard?org_id=…&region=va7`) "gives a good idea of where credits were spent for ESRI. Maybe share to the customer?"
- **Pierre 09-22:** "great report… will definitely share some of it with Esri in our next meeting."
- **Pedro:** cc'd throughout, no reply on the thread. The per-org usage view is the reporting layer he owns (G1); the answer went from Bertrand to a customer-facing TAM without passing through him.

## Same ask, four customers in three weeks (the pattern to watch)

| Date | Who | Customer | Ask | Answer on record |
|---|---|---|---|---|
| 09-02 | Mike Tilburg | VW, Centene | per-user credit visibility | Pedro: "not possible today" |
| 09-15/19 | Jeff Troccoli via Pierre / Corey | Esri | attribute credits to users and actions, restrict access, show value | Bertrand → Horia; Rubin per-org dashboard |
| 09-17 | Nina Mokoosio | UHG, Capital Group | program- or user-group-level access control to AEM agents and Coworker | Yanira: clone into `AEMAGT-2818` |
| 09-21/22 | Fabian Lotz / Stefanie Schnee | Infineon | how credits are computed for multi-step tasks and refinements; the doc says "estimated" | Pedro → Tina; Tina sent the licensing deck; Fabian: wrong question answered |

Two objects wearing one word again: **access control** (who may use it, per program / user group) and **credit attribution** (who spent what on which action, and what it returned). Esri asks for both; UHG asks for the first; Infineon and VW ask for the second. Related: [[reference_powerbi_token_usage]] (FinOps side, Jaclyn), [[reference_tbyb_sku_entitlement]], [[project_aem_agents_intelligence]] 2026-09-22 block.

## The rest of the 09-15 sync (Assets lane, not Pedro's; kept for context)

- **Usage rights / DRM (John Tapley):** licence extraction with confidence score, licence status, multi-licence support; handwritten agreements at ~50% accuracy (OCR two-step proposed); capability becoming a portable service (deterministic APIs · MCP skills · UI) usable from Workfront and Frame; content authenticity / C2PA provenance follow-up.
- **Coworker automation (Andy Petersen):** metadata and asset-review rules (contributor vs email lists → team tags; industry detection → market tags); many rules are deterministic if-then, not LLM work; **Brand-Aware Metadata** is a separate Assets capability (Srikanth Paladugu pointed them to it, enabled on stage); Pierre to check whether Coworker gets **Fusion skills** for deterministic automation.
- **Workfront connector** (Jennifer Verink, `E-002369068`), **Content Hub migration** (collections access), **Optel connection migration** (Clint Goudie-Nice, pending), **Federated guest access pilot** (Matt Pilgrim, NZ distributor / Eagle Technologies), **Experience Workspace demo** (Sam Davis, Pierre), **EDS migration** targets = sections of esri.com (case studies, long-form), translation management the blocker; Asset View feature requests (My Workspace customisation, versioning on multi-upload, Asset View ↔ Content Hub UI alignment).

## People

Esri: **Andy Petersen** (day-to-day lead), **Jeff Troccoli** (credits, PO, ROI), **Matt Pilgrim** (federated access, scratch assets), Sukesh Kasireddy, Jennifer Verink (Workfront), Harikrishna Alapati, Kishore Cikka. Adobe: **Pierre Tager** (runs the sync, owns the credit-governance action), Deke Smith, James Cornish, **John Tapley** (usage rights), Nick Whittenburg, Clint Goudie-Nice, Sam Davis (commercial), Jeffrey Herrington, Corey Dulimba, Kerry Nelson; cc Shankari Panchapakesan, Apoorva Gupta, Siddharth Sahni, Mohit Arora, Anton Heras, Aman Kumar Gupta, Jeff Jobe.
