---
name: AEM Experience Hub project context
description: EH-only after Phase 2 vault split (2026-05-03). Surface, contribution model, Sorin team, O2 personalization KRs. AAI work in sister file.
type: project
originSessionId: 298c09b0-7372-4e27-9660-87019bb7d26c
---

> **Phase 2 vault split landed 2026-05-03.** AAI content (agent reporting, AO 2.0 liaison, Loni+JM May 11 deck, three-tier reporting, Felix/Rubin/Varun threads, Apoorva punch-list, KR3/4/5/6) lives in `project_aem_agents_intelligence.md`. This file is EH surface, contribution model, Sorin team, O2 personalization KRs only.

AEM Experience Hub is the unified home screen / landing page for AEM Cloud Service at experience.adobe.com. Launched August 2024. Previously named AEM Home and AEM Launchpad. Not a replacement for existing AEM UIs. An action-oriented entry point that surfaces the right tools per persona.

**Current PM:** User (took over from Shankari March 2026.)

**Org:** User → Bertrand (Senior Director PM) → Loni (VP PM for AEM)

**Obsidian vault root:** `/Users/pedrofer/Library/CloudStorage/GoogleDrive-maprilpedro@gmail.com/My Drive/ObsidianVault/020 Professional/Adobe/Projects/2026/Experience Hub/`

---

## 2026 Yearly Review Goals (drafted with Bertrand, April 2026)

**G1 — Agent Intelligence & Reporting (now AAI scope):** see `project_aem_agents_intelligence.md`. Listed here for completeness — built and owned via the AAI surface.

**G2 — EH Platform Integration:** Own Experience Hub's integration with AEP and Adobe DX, including AO 2.0 migration and the new agent prompting surface. Ensure EH remains a reliable and current entry point as the underlying platform evolves.

**G3 — Experience Hub Adoption & Growth:** Establish Experience Hub as the measurable driver of AEM practitioner adoption growth, with data and narrative that leadership can point to at any level. Document and attribute EH's contribution to AEM monthly active user growth. Deliver the contribution model and user profiling that make EH contextual and extensible, and enable other teams to surface their work through EH as a shared platform.

File: `AEM EH - Key Files/Experience Hub - 2026 Yearly Review Goals.md`

---

## Team and Capacity (confirmed April 1, 2026 Sorin 1:1)

Pedro is PM of record. Team: Sorin Slavic (lead engineer), Eugene Bannykh (UX, US timezone), Mircea Salan (engineer, internship project lead), Anna Maria (intern).

Effectively 1 engineer. Sorin split across multiple projects. Anna Maria cannot contribute meaningfully near-term. Mikhail and Anastasia departed around the same time she arrived. Hiring pipeline open: best case May 1 first hire, June 1 second. Worst case: summer or positions closed. Roadmap declares 3 (1 + 2 in progress) for planning. Headcount minimum for roadmap: 5. EH bundled under Growth and Adoption.

Sorin's framing: "We are not a big house, but we are a proud house."

**Eugene Bannykh's manager:** Silvia Mulet Ferre (Sr Product Design Manager, Adobe Design, Austin) → Guliz Sicotte → Archana Thiagarajan → Eric Snowden (SVP Adobe Design) → David Wadhwani. Adobe Design is a separate VP chain, NOT AEP — relevant for cross-org coordination on EH UX.

---

## 3 Product Priorities for 2H2026

**Priority 1 — Skills + MCP surface**
Replace generic prompt grid with skills-aware, MCP-connection-aware chat surface. AO 2.0 lands May–July — right moment to redesign. Bertrand brief drafted (`EH as the Skills and MCP Surface - Bertrand brief.md`). Hold until Eugene's design view reviewed and MCP current state confirmed with Sorin.

**Priority 2 — Contribution Model / UX AI Framework**
Full alignment Pedro + Eugene + Sorin (April 1). Sorin independently drafting — main focus for 2 open reqs (UX + AI). Pilot mechanism: +Add Extension (App Builder, React SPA, IMS identity). Mircea Salan demoed March 27 — not production-ready. Known gaps: feature flag not activated, App Registry instability, stage-to-prod manual command, iframe context injection limited to user profile only, wizard needs simplification.

**Priority 3 — Customer Profiling**
5 profiles (General, Content Author, Asset Librarian, Developer, Admin). Bertrand deprioritized. Pedro's reframe: profiling is the mechanism that makes Priority 1 contextual, not a standalone ask. Don't raise until Skills+MCP is validated.

---

## 2H Roadmap

HOME-832 in JIRA (created April 1, 2026) — four H2 initiative descriptions: AI Assistant Integration Improvements, Collaboration Model Implementation, User Profiling Research, Supporting Teams and Promotional Surface. Working draft: `Home 2H2026 Roadmap - Experience Hub EH.md`. Canva roadmap planning doc still to be located and shared with Sorin.

---

## EH as MAU Driver — Claim to Own

Bertrand quote in April 13 Loni meeting: *"I would like to think that what we did with Experience Hub has been a key driver in expanding the number of monthly active users for AEM."* >60% customer base. Pedro's product. Surface this claim explicitly — own it, back it with data, make it a narrative Pedro controls. Stable metrics deck (KR5) is one vehicle. Grafana access obtained April 8 — cross-check vs Felix reports outstanding.

---

## EH Surface Integrations

### Brand Concierge Light-up — Summit Deadline (April 19-22, 2026)

Three options discussed in April 1 refinement sync. Sorin confirmed full production implementation is too late. Eugene designed wizard ~1 month ago. Bertrand contributed to shaping. Content AI indexing takes hours — can't be faked on customer side. Cloud Manager micro frontend PR (Peter's team) still open. Decision sent to Bertrand + Peter. Effective answer deadline April 2.

### Experimentation Page Integration (Jim Stoklosa's team)

Experimentation page is a full-screen landing page + sub-pages, not a widget. True to Eugene's mockups. Not all customers get it — contextual experimentation is an extension, not a default entitlement. Available across all AEM flavors.

EH responsibility: feature flag + navigation button visibility logic. Business logic (which tenants see it) defined by experiments team via API condition — EH maintains it but cannot define it alone. Micro frontend implementation: experiments team's responsibility (same model as security team). Sub-pages: experiments team must declare them so EH can manage pathing. Recent widget: experiments team should onboard their noun to unified shell recent service.

Jim's team: Dereje Dilnesaw (required), Julien Ramboz (required), Sanjeev Verma (optional). Slack sent April 1; Dereje responded April 8.

### Prompt Search (April 2 EH Demo)

Unified search for assets via AI assistant prompt (click +) is almost done. Returns results from first production repository user has access to — same as semantic search in AEM Assets. Bug confirmed: pulls from first prod repo only (context bug). Working with CJ analytics team on tracking gap between displayed and recorded prompts. Search still only covers assets — pages, content fragments, experiments, launches not included. Context bug (multi-environment users default to first prod env) still open.

### Adoption Data (April 2 EH Demo)

- Growth stable but stuck — Sorin: "stuck at 85%"
- Return users stable at ~62%
- New user count is dropping
- Prompt suggestions: steady views. "Content or knowledge" prompts most used.
- Analytics tracking bug: gap between what's shown and what's recorded — working with CJ analytics team

---

## Fu Chi (AEP Personalization) — EH-side personalization owner

Fu Chi (AEP team) built the personalized prompt recommendation pipeline. Weekly 1:1 with Pedro. Shankari was invited to first sessions.

**Architecture she owns:**
- Pipeline: user prompts → clean → embeddings → K-means clustering → topic reports
- Signal blending: user history (primary) → org signals (fallback) → global signals
- Output: CSV/table of user IDs + ranked prompt recommendations
- EH owns prompt bar + buttons. AEP owns right rail.
- Prompt library is centralized — agent owners can enrich it

**Already exists in her data:** behavioral cluster analysis (content authoring, asset focus, cloud manager usage) — raw material for Priority 3 (Customer Profiling). Real, not hypothetical.

**Workflow-aware recommendations** (suggest next action based on prior steps) on her roadmap, not yet prioritized.

**Open actions with Fu Chi:**
- Fu Chi to share prompt recommendation file
- Fu Chi to share Analytics DB wiki page for widget recommendation analysis
- Fu Chi to send draft email + spreadsheet for agent owner prompt review (March 25 ask — status unclear)
- Fu Chi to share Workfront persona use case (March 25 ask)
- Pedro to review prompt file with Sorin + schedule follow-up

---

## Cross-VP — Prompt Library Platform (O2 KR `EH consumes prompt library not wiki`)

Added April 28, 2026:

- PM: Cole Connelly (Principal PM, NY)
- EM: Joshua Hailpern. Lead engineers: Somya Biswari, Zeus Courtois.
- Org chain: Cole → Stephen Gould (GPM, SF) → Tim Lott (Director, Lehi) → Daniel Sheinberg (Sr Director) → **Sunil Menon (VP, Experience Cloud Portfolio, SJ)** → Amit Ahuja → Anil Chakravarthy.
- **Sunil Menon = peer of Loni Stark at VP level** under Amit Ahuja. Prompt Library Platform sits in his tree, NOT in AEM/Loni's.
- Right ladder: tactical Pedro→Cole, strategic Pedro→Stephen Gould (also Pedro's existing DX/Unified Shell contact), portfolio decisions Loni→Sunil at VP layer.
- Org-chart screenshots: `screenshots/20260428-org-*.png`.

---

## Interpersonal Watch (cross-cutting, kept EH-side)

| Person | Dynamic | Notes |
|---|---|---|
| Philippe Kapfer | Senior PM under Bertrand. Scope: Governance Agent + Security. Arrived 2 years after Pedro. Took security perimeter from Pedro. Potential promotion competitor — actively building Loni visibility. | Tactic: agree 1:1, create dissent in front of the boss (April 2). Pattern to break: hold position under public pressure, don't retract. Recovery path: reintroduce concerns as technical requirements, not debates. Use Corey Dulimba as first testeur for unpolished work, NOT Philippe. Treat as competitor, not ally. He doesn't attack — he makes you applaud him. |

---

## Sorin Workstream — Active Threads

### Data Compliance — Risk accepted (Bertrand, April 1, 2026)

Ian Boston (April 1) confirmed two legal risks with the agent reporting pipeline (data residency cross-region pull, governance/deposition risk). **Bertrand's decision (April 1):** "Ian's comments are important but not critical. We continue with Felix." Decision logged in `/decisions/2026-04-01-data-compliance-continue-felix.md`. Pipeline ownership lives AAI-side now; EH carries the surface implication only — the EH integration does not introduce additional compliance scope.

### Open Outreach (April 2, 2026 baseline)

| Person | Topic | Status |
|---|---|---|
| Ilya Grafutko | QI program synergy | Met April 14 |
| Ian Boston | Regional data aggregation | Confirmed two legal risks April 1 |
| Bertrand | Data compliance | Risk accepted April 1 — closed |
| Peter Klassen | Brand Concierge light-up option | Responded April 2 (full proposal) |
| Jim Stoklosa + team | Experimentation page onboarding call | Dereje responded April 8 |

---

## EH Status & Todo (Obsidian) + Key Files

All paths relative to: `/Users/pedrofer/Library/CloudStorage/GoogleDrive-maprilpedro@gmail.com/My Drive/ObsidianVault/020 Professional/Adobe/Projects/2026/Experience Hub/AEM Experience Hub - Project Folder/`

- Status & Todo: `Status and Roadmap/Experience Hub - Status and Todo.md` (renamed from `EH - Status and Todo.md` 2026-05-03)
- Bertrand 1-1 questions: `AEM EH - Key Files/Experience Hub - Questions for Next 1-1 with Bertrand.md` (cross-cutting, kept EH-side)
- Sorin 1-1 questions: `AEM EH - Key Files/Experience Hub - Questions for Next 1-1 with Sorin.md`
- State of Project: `AEM EH - Key Files/Experience Hub - State of the Project.md`
- Stakeholder Map: `AEM EH - Key Files/Experience Hub - Stakeholder Map.md`
- 2H Roadmap draft: `Roadmap/Home 2H2026 Roadmap - Experience Hub EH.md`
- EH Evolutions proposal: `202603 - EH Evolutions proposal.md`
- Bertrand brief: `EH as the Skills and MCP Surface - Bertrand brief.md`
- MOC: `🎯 AEM Experience Hub MOC.md`
- Meeting notes folder: `Adobe Projects 2026 Meeting Notes/` (renamed from `EH Meeting Notes/`)

---

## Slack Channels (EH-relevant)

`#experience-hub`, `#experience-hub-ai-assistant`, `#aem-home-platform-team`, `#aem-home-core-team`, `#temp-experiencehub-dxue`, AEM experience hub extension builder.

---

## Reporting chain

Pedro → Shankari Panchapakesan (Group PM, SJ) → Bertrand (Sr Director PM, Basel) → Loni Stark (VP AEM & Commerce, SJ) → Amit Ahuja → Anil Chakravarthy → Shantanu Narayen. Arrangement temporary — Shankari moving to report directly under Loni on a 6-month trial. Pedro's check-ins go directly to Bertrand. Loni's actual title: **VP, AEM & Commerce** (PM + Product Marketing).

---

## Sister project

`project_aem_agents_intelligence.md` — agent reporting platform, AO 2.0 liaison, three-tier reporting, Loni+JM May 11 deck, H-005 resolved, Felix/Rubin/Varun threads, Apoorva punch-list, KR3/4/5/6, AEMEO-9508 Data Advisory Agent overlap watch, Vaishnav PMM signal, broadcast-rep muscle.
