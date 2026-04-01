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
AEP AI Assistant is built and owned by the AEP team. PM of record: `hanessia`. QI DRI: Ilya Grafutko (Sr PM, AEP Agent Orchestrator Platform). AEM AI Assistant is program-managed by WEM. Pedro is not in any ownership chain. His role: EH surface integration (integrating the AEP prompt bar), AEM agent reporting contributor, EH as the hero surface for AEM agents. Pedro must confirm this framing with Bertrand. Sorin asked directly in the April 1 refinement sync — still unresolved.

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

HOME-832 created in Jira (April 1, 2026) — four H2 initiative descriptions captured: AI Assistant Integration Improvements, Collaboration Model Implementation, User Profiling Research, Supporting Teams and Promotional Surface. Sent to Sorin April 1. Working draft: `Home 2H2026 Roadmap - Experience Hub EH.md`. Pedro still needs to find the Canva roadmap planning doc and share with Sorin.

---

## Data Compliance — CONFIRMED RISK (Ian Boston, April 1, 2026)

Ian confirmed two legal risks with the reporting pipeline:

1. **Data Residency (contractual breach):** Cross-region pull (VA, NLD2, AUS5, CAN2, GBRS, IND1) breaks contractual requirements for some customers — storage and processing must stay in region.
2. **Data Governance (deposition risk):** Datasets not registered in Data Governance Catalog — legal exposure if called to provide a deposition. AI class action risk explicitly named.

AEP Co-Pilot Report provides per-region data — the source is clean. Felix and Lara both extract from it and then aggregate across regions on their side. The compliance breach is in the aggregation step, not at the AEP source. Both pipelines have the same behavior. The fix is a shared compliant aggregation layer, not an AEP platform change. Other agent self-reports may have the same aggregation pattern.

Ian's warning: someone outside AEM BU could shut this down and AEM loses the right to handle prompt data — 100% dependent on AEP. His framing: "prompt data is the most valuable output of everything in P42." Ian strongly prefers fixing this quietly before it surfaces to legal.

**Anonymization does not solve residency** (confirmed by Ian, April 1): as long as a prompt is readable it remains customer data, and residency obligations follow it. Anonymizing to the point it's no longer customer data breaks data lifecycle (can't delete on customer termination). Operational data classification loophole exists but restricts use to service uptime only — useless for evaluation.

**Bertrand's decision (April 1, 2026):** "Ian's comments are important but not critical. We continue with Felix." Pedro escalated correctly with Ian's confirmation and a proposed path. Bertrand made the call to accept the risk and continue. This decision belongs to Bertrand, not Pedro. Pedro's escalation is on record. Decision logged in `/decisions/2026-04-01-data-compliance-continue-felix.md`.

---

## Brand Concierge Light-up — Summit Deadline (April 19-22, 2026)

Three options discussed in April 1 refinement sync. Sorin confirmed full production implementation is too late. Options:
1. Full implementation for all customers — too late.
2. Mock wizard on a preview link for Summit only (Bertrand's instance). Doable. Not production-ready. Remove after Summit and rebuild.
3. Static announcement card redirecting to URL — 1 day if static, more if conditions/permissions needed.

Eugene designed the wizard ~1 month ago. Bertrand contributed to shaping it. Content AI indexing takes hours — can't be faked on customer side. Cloud Manager micro frontend PR (Peter's team) still open, not in current release.

Message sent to Bertrand + Peter asking which option. Effective deadline for answer: tomorrow (April 2).

---

## Experimentation Page Integration (Jim Stoklosa's team)

From April 1 refinement sync:
- Experimentation page is a full-screen landing page + sub-pages (not a widget). True to Eugene's mockups.
- Not all customers get it — contextual experimentation is an extension, not a default entitlement. Available across all AEM flavors.
- EH responsibility: feature flag + navigation button visibility logic. Business logic (which tenants see it) must be defined by experiments team via an API condition — EH maintains it but cannot define it alone.
- Micro frontend implementation: fully experiments team's responsibility (same model as security team).
- Sub-pages: experiments team must declare them so EH can manage pathing.
- Recent widget: experiments team should onboard their noun to unified shell recent service.
- Unified search: currently only assets (Content AI semantic search). Doesn't know about experiments, pages, content fragments, etc. Gap to address separately.

Jim's team: Dereje Dilnesaw (required), Julien Ramboz (required), Sanjeev Verma (optional).
Slack sent April 1 to @stoklosa @dilnesaw — invited to call, walked through open questions, set micro frontend ownership expectation.

---

## Prompt Search Gaps (identified April 1 refinement sync)

1. Search only works for assets (Content AI semantic search). Doesn't search pages, content fragments, experiments, launches, etc. Needs: identify what nouns exist, what teams own them, what search APIs are available.
2. Context bug: search doesn't pass current environment context into the search API. For multi-environment users, defaults to first production environment found — wrong results possible. Known gap, not blocking initial iteration.

---

## Open Outreach (as of April 1, 2026)

| Person | Topic | Status |
|---|---|---|
| Ilya Grafutko | QI program synergy | Sent April 1, 11:24 AM — awaiting response |
| Ian Boston + Raul Hudea | Regional data aggregation | Sent April 1 — Ian responded; Raul awaiting |
| Raul Hudea | VRR multi-tier definition | Sent April 1 — awaiting response |
| Bertrand | Data compliance escalation | Sent April 1 — Bertrand suggested anonymization; Ian confirmed it doesn't fix residency; face-to-face response pending |
| Bertrand + Peter | Brand Concierge light-up option | Sent April 1 — awaiting response (deadline tomorrow) |
| Jim Stoklosa + team | Experimentation page onboarding call | Sent April 1 — awaiting response |
| Philippe Kapfer | Demo prompts | Responded April 1 |

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

Demo regeneration: message sent April 1 to all owners + Mark Szulc (based in Australia). Philippe responded. Reminder set for April 2 noon to chase the rest.

---

## Active Actions This Week

- 🔴 Report hosting — create AEM EDS program for aem-agent-reports, then work with Quentin to add CDN front + Okta auth. Sidekick requirement is a deal breaker for Loni. Current URL: https://main--aem-agent-reports--aem-epa.aem.live/ — Bertrand directed this on April 1.
- 🟡 Report to JIRA pipeline — project started: `/Users/pedrofer/GitHub/adbe-agent-report-to-jira`. First trial complete: PROCEDURE.md written, EGA epic AEMAGT-1240 created and updated (description + Philippe Kapfer as assignee), two stories auto-generated (AEMAGT-1241, AEMAGT-1242). Agent-Owner-Epic-Mapping.md at `/setup/`. Email sent to Philippe + Bertrand for feedback. Next: incorporate feedback, expand to other agents.
- 🔴 Brand Concierge: get Bertrand + Peter answer on option (deadline April 2)
- 🔴 Data compliance: deliver anonymization response to Bertrand face-to-face
- 🔴 Follow up on demo prompts — reminder set April 2 noon (Philippe answered, chase the rest)
- 🟠 Get on Sorin + Eugene email thread on UX AI framework
- 🟠 Review Eugene's design view on Skills/MCP before going to Guliz
- 🟠 Sync with Felix early week of April 7 on report-to-JIRA pipeline progress
- 🟠 Get VRR tier definition from Raul / Yanira's wiki
- 🟠 Clarify Agent Assistant PM role with Bertrand next 1:1
- 🟠 Join "AEM experience hub extension builder" Slack channel
- 🟠 Find Canva roadmap planning doc → share with Sorin
- 🟠 Address prompt search gaps (assets only + context bug) — add to backlog

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
