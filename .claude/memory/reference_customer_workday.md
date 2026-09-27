---
name: reference-customer-workday
description: Workday, Inc. as an AEM customer — two AEMCS IMS orgs, a top-5 MCP user in June, the 09-15 Tina meeting with their engineer, the RT-CDP MCP logging ask. Read before any Workday conversation. Not the HR system.
metadata:
  type: reference
---

# Workday (the customer) — what memory holds

Not Workday the HR system (the check-in and the AI-phrasing feedback live there). Workday, Inc. is an AEM Cloud Service customer and, AEP-side, a "strategic customer".

- **Orgs (AEMCS licensed-customers export, 2026-08-20):** `0AB2768154D414A20A4C98A5@AdobeOrg` "Workday" and `D6FD298C63BC94730A495FC1@AdobeOrg` "workday-ilx-aem". Both in `20260820-AEM_COHORTS.xlsx`; `workday-ilx-aem` is in Paul Midura's Cohort 3B draft (09-09). Category `Other` in the P42 org list.
- **MCP usage, the only number on file (06-30 snapshot, Splunk `aem_mcp_usage`, 30 days):** "Workday ILX" and "Workday iLX Secondary" at 1,334 requests each on two servers, both in the top five orgs; the June note called the regular-user set "Workday-family heavy". No newer per-org figure exists in memory or the vault — checked 09-15, the 09-03 and 09-08 Rubin skills-usage exports do not contain the string.
- **AEP side:** 07-24, Sarah Dawson (TAM) relayed RT-CDP MCP logging questions from "strategic customer Workday" (which Splunk log, forwarding, metrics, redacted samples); Parag Awadhiya: exposing Splunk logs to a customer has downsides and there is no per-customer partitioning. Workfront: "Chris at Workday" used the WF MCP 08-20 and the change history showed API not MCP; Michael Burkhartsmeyer opened a support ticket.
- **2026-09-15 23:00 CEST meeting with their engineer**, Tina Ngo + Pedro. Tina's DM 19:56: "can you meet with a customer today at 2pm pt… workday… wants to learn about aem skills and coworker… today's meeting is with their engineer… i already did the pitch, i guess i did too good of a job… my goal is to just end it short and get them to use it." Pedro: "100% its a trap :)", asked for 15 minutes of context first; Corey unavailable. **Outcome not captured — debrief ask.**

**How to apply:** before quoting Workday usage, pull a fresh per-org cut (Rubin `filter by aem*`, or the Splunk MCP dashboard in [[reference_splunk_mcp]]); June is the only figure on file. Two orgs, name both.

Related: [[reference_tbyb_sku_entitlement]], [[project_aem_agents_intelligence]].

**2026-09-25 — usage check (AEM Champions list).** AOv1: 261 interactions / 78 users YTD, 12 since 08-18, last 09-08. Coworker (Rubin 08-18 → 09-24): org found, zero activity. Still on AOv1, not migrated. [[project_aem_agents_intelligence]] 2026-09-25 block.

**2026-09-27 — the 09-15 call outcome, and the MCP picture (Pedro, first-hand).** Call with Tina, Workday's architect and their project manager (no names on file). ⚠️ Date matched to the 09-15 meeting above from memory; Pedro confirmed "avec Tina", not the date. **Workday opted out of Coworker. Reason, stated by the customer: user rights management. They want to control who uses Coworker, what it can reach, read vs write.** They did not state a return condition; Pedro's read (his inference, not their words): all of it, above all who uses it and how to limit their rights. Ford, by contrast, is sequenced: migrates after the panel.
- **MCP explorer (CloudWatch prod, 04-26 → 09-20):** "Workday" org = **6,607 operations, 264 sessions, 99.9% via `aem-oauth-cursor`**, weekly since W24, peak ~1,600/week in W30-W31, still 75 in W38. **The #1 champion on AEM MCP.** Also "Community Workday" (11 ops). Not checked which of the two IMS orgs the explorer's "Workday" is.
- **Inference, unverified:** the Cursor path is user OAuth, so each engineer acts with his own AEM permissions; Coworker is enabled per org and every AEM user with it enabled gets the rail (Mark Doten 09-18). Workday rejected the one surface it cannot govern, not AI on AEM.
- **H-010 instance** — the first *decision* conditioned on access control (see `knowledge/hypotheses/active.md`). Ticket to attach Workday to: `AEMAGT-2818`.
