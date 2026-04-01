---
name: AEM Experience Hub project context
description: Full context on the Experience Hub project - what it is, who owns it, team, org, state, risks, top priorities, Obsidian vault location
type: project
---

AEM Experience Hub is the unified home screen / landing page for AEM Cloud Service at experience.adobe.com. Launched August 2024. Previously named AEM Home and AEM Launchpad. Not a replacement for existing AEM UIs. An action-oriented entry point that surfaces the right tools per persona.

**Current PM:** User (took over from Shankari in March 2026 — ~3 weeks in as of April 1, 2026.)

**Org:** User → Bertrand (Senior Director PM) → Loni (VP PM for AEM)

**Obsidian vault:** /Users/pedrofer/Library/CloudStorage/GoogleDrive-maprilpedro@gmail.com/My Drive/ObsidianVault/020 Professional/Adobe/Projects/2026/Experience Hub

---

## Two Workstreams

**Workstream 1 — Experience Hub (fully owned)**
Pedro is PM of record. Team: Sorin Slavic (lead engineer), Eugene Bannykh (UX, US timezone), Mircea Salan (engineer, internship project lead), Anna Maria (new intern, started April 1 — cannot contribute meaningfully near-term).

**Workstream 2 — Agent Assistant (contributor, not PM)**
AEP AI Assistant is built and owned by the AEP team. PM of record: `hanessia`. QI DRI: Ilya Grafutko (Sr PM, AEP Agent Orchestrator Platform). AEM AI Assistant is program-managed by WEM. Pedro is not in any ownership chain. His role: EH surface integration (integrating the AEP prompt bar), AEM agent reporting contributor, EH as the hero surface for AEM agents. Pedro must confirm this framing with Bertrand.

---

## Team Capacity (confirmed April 1, 2026 Sorin 1:1)

Effectively 1 engineer. Sorin is split across multiple projects. Anna Maria (new intern) cannot contribute meaningfully near-term. Mikhail and Anastasia departing around the same time she arrived.

Hiring pipeline: technical interview April 2 for one replacement. Best case: May 1 first hire, June 1 second hire. Worst case: summer, or positions closed. Roadmap must reflect this — declare 3 (1 + 2 in progress) for planning purposes. Headcount minimum for roadmap: 5. EH is bundled under Growth and Adoption.

Sorin's framing: "We are not a big house, but we are a proud house."

---

## 3 Product Priorities for 2H2026

**Priority 1 — Skills + MCP surface**
Replace generic prompt grid with skills-aware, MCP-connection-aware chat surface. AO 2.0 lands May–July — right moment to redesign. Bertrand brief drafted (`EH as the Skills and MCP Surface - Bertrand brief.md`). Not yet sent — hold until Eugene's design view reviewed and MCP current state confirmed with Sorin.

**Priority 2 — Contribution Model / UX AI Framework**
FULL ALIGNMENT across Pedro + Eugene + Sorin (April 1). Sorin was independently drafting this — it's the main focus for 2 open reqs (UX + AI roles). Email thread between Sorin and Eugene exists — Pedro needs to be added. Pilot mechanism: +Add Extension (App Builder, React SPA, IMS identity). Mircea Salan demoed March 27 — not production-ready. Known gaps: feature flag not activated, App Registry instability, stage-to-prod manual command, iframe context injection limited to user profile only, wizard needs simplification.

**Priority 3 — Customer Profiling**
5 profiles (General, Content Author, Asset Librarian, Developer, Admin). Bertrand deprioritized. Pedro's reframe: profiling is the mechanism that makes Priority 1 contextual, not a standalone ask. Don't raise until Skills+MCP is validated. Win Priority 1 first.

---

## 2H Roadmap

Working draft: `Home 2H2026 Roadmap - Experience Hub EH.md`. Two carry-over buckets from 1H (Personalization + Adoption) plus contribution model / agentic framework. Real H2 breakdown starts June 1. Pedro to draft items this week, send to Sorin, then session to define epics. Pedro still needs to find the Canva roadmap planning doc and share with Sorin.

---

## Data Compliance — CONFIRMED RISK (Ian Boston, April 1, 2026)

Ian confirmed two legal risks with Felix's pipeline:

1. **Data Residency (contractual breach):** Cross-region pull (VA, NLD2, AUS5, CAN2, GBRS, IND1) breaks contractual requirements for some customers — storage and processing must stay in region.
2. **Data Governance (deposition risk):** Datasets not registered in Data Governance Catalog — legal exposure if called to provide a deposition. AI class action risk explicitly named.

Felix extracts from AEP Co-pilot Report. Lara Nonino also extracts from AEP Co-Pilot Report for Governance Agent — same source, not a different platform. Same compliance problem. Other agent self-reports may have the same issue.

Ian's warning: someone outside AEM BU could shut this down and AEM loses the right to handle prompt data — 100% dependent on AEP. His framing: "prompt data is the most valuable output of everything in P42."

Proposed path escalated to Bertrand April 1: scope blast radius (how many orgs have residency requirements, are they active users?), accelerate DAS to build compliant infrastructure using Felix's pipeline as the spec.

---

## Open Outreach (as of April 1, 2026)

| Person | Topic | Status |
|---|---|---|
| Ilya Grafutko | QI program synergy | Sent April 1, 11:24 AM — awaiting response |
| Ian Boston + Raul Hudea | Regional data aggregation | Sent April 1 — Ian responded; Raul awaiting |
| Raul Hudea | VRR multi-tier definition | Sent April 1 — awaiting response |
| Bertrand | Data compliance escalation | Sent April 1 — awaiting response |

---

## Agent Owners (AEM)

| Agent | Owner |
|---|---|
| Experience Production | Corey Dulimba |
| Governance | Philippe Kapfer |
| Discovery | Apoorva Gupta |
| Content Optimization | Greg Klebus |
| Development / EDA | Brian Chaikelson |
| Onboarding | Nick Whittenburg |
| Modernization | Gabriel Walt / Mike Tilburg |

Demo regeneration: message sent April 1 to all owners + Mark Szulc (based in Australia). Asked for 1-2 prompts per agent by end of week / early next week.

---

## Active Actions This Week

- 🔴 Draft 2H roadmap items + find Canva → send to Sorin
- 🔴 Follow up on demo prompts from agent owners (deadline end of week)
- 🔴 Resolve Brand Concierge AEM light-up — get Peter/Bertrand to confirm EH scope
- 🟠 Get on Sorin + Eugene email thread on UX AI framework
- 🟠 Review Eugene's design view on Skills/MCP before going to Guliz
- 🟠 Sync with Felix early week of April 7 on JIRA integration
- 🟠 Get VRR tier definition from Raul / Yanira's wiki
- 🟠 Give Jim Stoklosa experimentation team feedback (after EH refinement session)
- 🟠 Clarify Agent Assistant PM role with Bertrand next 1:1
- 🟠 Join "AEM experience hub extension builder" Slack channel

---

## Key Meetings / Documents

- Bertrand questions: `AEM EH - Key Files/Experience Hub - Questions for Next 1-1 with Bertrand.md`
- Sorin questions: `AEM EH - Key Files/Experience Hub - Questions for Next 1-1 with Sorin.md`
- State of Project: `AEM EH - Key Files/Experience Hub - State of the Project.md`
- Stakeholder Map: `AEM EH - Key Files/Experience Hub - Stakeholder Map.md`
- 2H Roadmap draft: `Roadmap/Home 2H2026 Roadmap - Experience Hub EH.md`
- EH Evolutions proposal: `202603 - EH Evolutions proposal.md`
- Bertrand brief: `EH as the Skills and MCP Surface - Bertrand brief.md`
- Ian's compliance response: `AEM Experience Agent Reports/20260401 - Ian Issues on Felix Report data localisation.md`
- AI Assistant findings: `../AI-Assistant/AI-Assistant-Findings.md`
- MOC: `🎯 AEM Experience Hub MOC.md`

---

## Slack Channels

\#experience-hub, \#experience-hub-ai-assistant, \#aem-home-platform-team, \#aem-home-core-team, \#temp-experiencehub-dxue, \#dx-product-measurement, \#tmp_aem_missing_prompt_library, AEM experience hub extension builder (new)
