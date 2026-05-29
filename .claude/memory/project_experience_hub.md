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
- **2026-05-19 bridge:** Joshua Hailpern (EM here) also leads AIA UI / Mithril / Fruitbar; Somya Biswari + Zeus Courtois are lead engineers on both. Prompt Library Platform and Mithril/Fruitbar = same engineering galaxy under Sunil Menon's tree. Full note in `project_aem_agents_intelligence.md` "May 19 — Engineering bridge".

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

- Status & Todo: `AEM EH Status and Roadmap/Experience Hub - Status and Todo.md` (renamed from `EH - Status and Todo.md` 2026-05-03)
- Bertrand 1-1 questions: `AEM EH - Key Files/Experience Hub - Questions for Next 1-1 with Bertrand.md` (cross-cutting, kept EH-side)
- Sorin 1-1 questions: `AEM EH - Key Files/Experience Hub - Questions for Next 1-1 with Sorin.md`
- State of Project: `AEM EH - Key Files/Experience Hub - State of the Project.md`
- Stakeholder Map: `AEM EH - Key Files/Experience Hub - Stakeholder Map.md`
- 2H Roadmap draft: `Roadmap/Home 2H2026 Roadmap - Experience Hub EH.md`
- EH Evolutions proposal: `202603 - EH Evolutions proposal.md`
- Bertrand brief: `EH as the Skills and MCP Surface - Bertrand brief.md`
- MOC: `🎯 AEM Experience Hub MOC.md`
- Meeting notes folder: **moved out of EH folder 2026-05-13** → `/2026/Meeting Notes/` (neutral, shared with AAI and other projects). Previously `Adobe Projects 2026 Meeting Notes/` under EH project folder. Rename + move applied because folder content (Bertrand, Felix, Namita, Ian, Yanira 1-1s) was cross-cutting, not EH-specific.

---

## Slack Channels (EH-relevant)

`#experience-hub`, `#experience-hub-ai-assistant`, `#aem-home-platform-team`, `#aem-home-core-team`, `#temp-experiencehub-dxue`, AEM experience hub extension builder.

---

## Reporting chain

Pedro → Shankari Panchapakesan (Group PM, SJ) → Bertrand (Sr Director PM, Basel) → Loni Stark (VP AEM & Commerce, SJ) → Amit Ahuja → Anil Chakravarthy → Shantanu Narayen. Arrangement temporary — Shankari moving to report directly under Loni on a 6-month trial. Pedro's check-ins go directly to Bertrand. Loni's actual title: **VP, AEM & Commerce** (PM + Product Marketing).

---

## May 5 Bertrand 1-1 — EH-side drop-ins

Source: `Meeting Notes/Bertrand 1 1/20260505 - Bertrand Pedro 1 1_otter_ai_transcript.txt`. AAI signals in sister memory file.

**Mithril / Coworker (Joshua Hailpern team).** AI Assistant V2 with "mode rail" (observer + suggestion). Launching ~late May (T-25 days). **AEM Sites NOT included** — repeat exclusion pattern (also Modernization Agent + Experience Workspace). Bertrand asked Sorin + Eugene to do Mithril review. Pedro saw UI via night Slack May 4. Bertrand: *"Ça va être un point important pour la migration AOv2 si on y va."* Bertrand actioned: chase Guliz on XD/Adobe-Design loop visibility.

**Marcus Räck (Experience Workspace creator).** Declined Pedro's unified-chat ask: *"je pense qu'il faut chaque solution ait son propre tchat."* 4 chats now (Experience Workspace, Modernization, Slick, Rosetta=Manager Services). ⚠️ **"Slick" + "Rosetta" = low-confidence names** — from a garbled May 5 Otter auto-transcript (*"sleek… le chat dans Rosetta qui est la version manette services"*, Unknown Speaker; "manette services" = mis-heard "Manager Services"). Pedro didn't recall the names 2026-05-28, will verify later. Don't assert as canonical until confirmed. Pedro pushing common substrate (history, context). Bertrand views chat unification as AOv2-migration-relevant.

**Cédric Huesler — repair contact.** Pedro got him annoyed via Slack push on AOv2 + contribution model May 5 morning. Tactical contact for Experience Workspace + AOv2-on-Sites discussions.

**Sylvia Mulet Ferre auto-fix-prompt initiative for EH.** Sylvia (Eugene's manager, Adobe Design / Guliz tree) launching: hypothesis = users come once and stop because request too complicated from start. Bertrand skeptical: *"je sais pas trop où elles vont venir avec ça."* Track scope + intersection w/ Eugene.

**Customer migration pattern.** 1-year migration deadline approach. Decouple "platform update" vs "platform move." Nico's content-repo migration initiative waking customers up — many need re-migration with hard deadlines.

**EH headcount note.** *"On va avoir 2 personnes qui sont remplacées pour Experience Hub. On va être de trop"* (Bertrand).

---

## May 12 — Bertrand 1-1 EH-side drop-ins

Source: `Meeting Notes/Bertrand 1 1/20260512 - Bertrand Pedro 1 1.md`. AAI-side content in sister memory.

**1. 🆕 Quiet Hours Update via Agents — beta launching.** Activated on ID. Customers run **Quiet Hours-Update via the chatbot/agent** (free). Beta cohort: (customers who previously used Quiet Hours Update) ∩ (customers w/ AI) = **81 customers** to activate. Expect dozens of feedback. **Ties O4 (Ship Quiet Hours).** Concrete proof point for May 11 deck "customer trust increase" slide. Companion to Bertrand customer-trust slide (Pedro to add quote-worth slots).

**2. 🆕 Breaking changes manager — name rename needed.** Raspberry team finds "breaking changes" too negative. Concept stays: central repo declaring breaking changes w/ dates, impacted customers, procedures, docs. For ~120 customers internal use + customer-facing awareness. Pedro action: source new name.

**3. 🆕 Two new EH hires start beginning of June.** Resolves Bertrand May 5 *"2 personnes remplacées pour EH"* note. Profiles:
- One ex-AEP.
- One full-stack AI engineer (*"qui fait pas mal d'AI"*).
- Bertrand: *"ça peut vous aider à coder plein de trucs."* Capacity inflection for EH eng (Sorin = 1 effective today).

**4. Customer update push state — O6 lever.** ~120 customers behind on Content Fragments / content freshness. ~100 still behind. **Aldi (7-8 programs) + Volkswagen + Americans** = key targets. Plan: propose manual update first → automatic update later. **1-year window option:** customer commits to test impl + monthly platform updates while staying off auto-update. CSM one-by-one outreach. Mostly positive responses to progressive migration. Ties to O6 Aging Customers (slipped end-March KR).

**5. AOv2 + skills + context framing.** EH-relevant fragments: cross-surface AI-Assistant continuity Bertrand wants (chat history retrievable across surfaces); Michael compliance pushback (data residency primary-region constraint). Open product question for EH surface = where does the AI Assistant icon route post-Mithril (per-surface context vs global Assistant). Full AOv2 framing in AAI memory.

**6. Sylvia auto-fix-prompt initiative status.** Bertrand May 5 flagged. May 12 update: Sylvia "very actively" in contact with Tim Lynn (Mithril). Pedro coached her to synchronize w/ Guliz but hedge on AOv2. Bertrand: Gilles + Michael had AOv2-counterpart meeting with Manas + Ken — relayed *"v1 was very complicated."*

**Pedro action items from EH side:**
- Slot Quiet-Hours-via-Agents 81-customer beta into May 11 deck customer-trust slide.
- Find rename for "Breaking changes manager."
- Verify Grafana JSON-size issue post-Raul-list-fix before next exec demo (cross-cutting, also AAI).
- Confirm AI Assistant SKU/pricing model w/ Bertrand (cross-link Mithril Silvia pricing question).
- Onboard plan for 2 June hires.

---

## May 12 — Mithril Silvia Eugene Pedro sync (EH-side anchor)

Source: `Meeting Notes/Eugene/20260512 - Mythril Silvia Eugene Pedro Sync.md`. Full notes in AAI memory. EH-side anchor:

- Silvia use case = **context-reading, not UI-interaction.** *"We don't want AI to interact with UI. We want AI to read UI."* Mithril MVP misses this.
- Eugene framing: post-Mithril, AI Assistant icon becomes contextual per surface (pipeline, etc.). Pre-Mithril = dummy shortcut everywhere.
- 🆕 **Matthew** = Mithril co-owner alongside Tim Lynn. Surname TBD. Tomorrow May 13 Silvia + Eugene + Tim + Matthew sync. Pedro not invited — Silvia reports back.
- 🆕 Migration window UX problem: multi-month window with mixed v1/v2/migrating agents. User confusion on which has skills/Mithril. Mitigation = in-app notifications (Silvia). Eugene: low risk currently.
- 🆕 Pricing question: AI Assistant free or paid? Affects failure tolerance. Pedro action: confirm w/ Bertrand.
- Pedro→Silvia: relayed Loni reframe (*"maybe v2 not the correct question, list requirements"*) — same Loni reframe Bertrand reported at P42 hours later. Converging signal.

**EH action:** send Silvia engineering-manager-per-AEM-agent list (Guliz-assigned design POV on AOv2).

---

## May 12 — Cross-cutting Loni reframe (full content AAI-side)

Loni reframe verbatim — *"No, that's not the question. Question is context, and how do we equip our agents with proper context."* Strategic anchor at VP level. Connects EH (Mithril context-reading primitive ask) ↔ AAI (Ian's North Star architecture for AEM agents AOv2). Same axis, two surfaces. Full context in AAI memory; EH-side relevance = context-reading on Mithril is the **visible UI expression** of the strategic context-architecture pivot.

---

## May 22 — EH's role in the distributed-harness model (Ian NorthStar exchange)

Ian Boston's Agentic NorthStar + the May 19-22 thread reshape how EH should be positioned. Full AAI-side record in `project_aem_agents_intelligence.md` "May 22 — Ian NorthStar thread".

In the distributed-harness model **the UI decides which harness/agent to call** (Ian: explicit/prompted selection, not auto intent-detection), and **cross-surface consistency is vital + PM-led** (Ian: *"an Adobe user feels like it is the same surface regardless of implementation details or UI engineering ownership"*).

**This makes EH (and the agent surfaces) the selection + consistency layer for AEM agents — not just a launchpad.** EH's job grows into: (a) the surface where practitioners select / are prompted toward the right agent (the selection UX Pedro now PM-leads, Ian on record), and (b) the consistency layer that makes distributed, independently-owned agent UIs feel like one Adobe surface (the answer to the 4-chats fragmentation: Experience Workspace / Modernization / Slick / Mithril).

Ties to: EH Priority 1 (Skills+MCP surface), the contribution model, Eugene's per-surface contextual AI Assistant icon, Mithril context-reading (Silvia — context-reading powers good prompted selection), and Pedro's convergence push (now architect-backed). Strategic upgrade to EH's narrative: **EH = the practitioner-facing selection + consistency layer in Adobe's distributed agent architecture.**

---

## Sister project

`project_aem_agents_intelligence.md` — agent reporting platform, AO 2.0 liaison, three-tier reporting, Loni+JM May 11 deck, H-005 resolved, Felix/Rubin/Varun threads, Apoorva punch-list, KR3/4/5/6, AEMEO-9508 Data Advisory Agent overlap watch, Vaishnav PMM signal, broadcast-rep muscle. **+ May 12 Loni reframe + Ian = North Star architect + Ian one-pager deliverable + May 13 Felix/Lara 3-way (External Agent naming, $2K/mo cost data, Mark Pfaff).**
