---
name: AEM Experience Hub project context
description: Full context on the Experience Hub project - what it is, who owns it, team, org, state, risks, top priorities, Obsidian vault location
type: project
originSessionId: 298c09b0-7372-4e27-9660-87019bb7d26c
---
AEM Experience Hub is the unified home screen / landing page for AEM Cloud Service at experience.adobe.com. Launched August 2024. Previously named AEM Home and AEM Launchpad. Not a replacement for existing AEM UIs. An action-oriented entry point that surfaces the right tools per persona.

**Current PM:** User (took over from Shankari in March 2026 — ~3 weeks in as of April 1, 2026.)

**Org:** User → Bertrand (Senior Director PM) → Loni (VP PM for AEM)

**Obsidian vault:** /Users/pedrofer/Library/CloudStorage/GoogleDrive-maprilpedro@gmail.com/My Drive/ObsidianVault/020 Professional/Adobe/Projects/2026/Experience Hub

---

## Two Workstreams

**Workstream 1 — Experience Hub (fully owned)**
Pedro is PM of record. Team: Sorin Slavic (lead engineer), Eugene Bannykh (UX, US timezone), Mircea Salan (engineer, internship project lead), Anna Maria (new intern, started April 1 — cannot contribute meaningfully near-term).
Scope: EH product priorities (Skills+MCP surface, Contribution Model, Customer Profiling), Brand Concierge Summit light-up, Experimentation page integration, report hosting (CDN + Okta).

**Workstream 2 — Agent Assistant (contributor, not PM)**
AEP AI Assistant is built and owned by the AEP team. PM of record: `hanessia`. QI DRI: Ilya Grafutko (Sr PM, AEP Agent Orchestrator Platform). AEM AI Assistant is program-managed by WEM. Pedro is not in any ownership chain. His role: EH surface integration (integrating the AEP prompt bar), AEM agent reporting contributor, EH as the hero surface for AEM agents. Pedro must confirm this framing with Bertrand. Sorin asked directly in the April 1 refinement sync — still unresolved.
Scope: Felix's reporting pipeline, report-to-JIRA project, data compliance (Bertrand accepted risk April 1), report hosting (CDN + Okta path with Quentin).

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

## Prompt Search (updated April 2 EH Demo)

Unified search for assets via AI assistant prompt (click +) is almost done. Returns results from first production repository user has access to — same as semantic search in AEM Assets. Bug confirmed: pulls from first prod repo only (context bug, already known). Working with CJ analytics team on separate tracking gap between displayed and recorded prompts.

Remaining gaps: search still only covers assets. Pages, content fragments, experiments, launches not included. Context bug (multi-environment users default to first prod env) still open.

## Adoption Data (April 2 EH Demo)

- Growth stable but stuck — Sorin described it as "stuck at 85%"
- Return users stable at ~62%
- New user count is dropping
- Prompt suggestions: steady views. "Content or knowledge" prompts are most used.
- Analytics tracking bug: gap between what's shown and what's recorded — working with CJ analytics team

---

## Open Outreach (updated April 2, 2026)

| Person | Topic | Status |
|---|---|---|
| Ilya Grafutko | QI program synergy | Responded April 2 — open to meeting, Teams call week of April 7 |
| Ian Boston | Regional data aggregation | Responded April 1 — confirmed two legal risks |
| Raul Hudea | Regional data aggregation + VRR tier definition | Sent April 1 — awaiting response |
| Bertrand | Data compliance | Accepted risk April 1 — continue with Felix. Closed. |
| Peter Klassen | Brand Concierge light-up option | Responded April 2 — shared full product Confluence proposal. Bertrand also answered. Waiting on Sorin's feedback on Summit-viable scope. |
| Jim Stoklosa + team | Experimentation page onboarding call | Dereje responded April 8 — open early next week. Pedro to confirm. |
| Philippe Kapfer | Report-to-JIRA feedback | Responded April 2 — positive, pipeline rules confirmed |
| Corey Dulimba | Demo prompt regeneration | Responded April 2 |
| Apoorva Gupta | Demo prompt regeneration (Discovery agent) | Chased April 2 |

---

## Interpersonal Watch

| Person | Dynamic | Notes |
|---|---|---|
| Philippe Kapfer | Senior PM under Bertrand. Scope: Governance Agent + Security. Arrived 2 years after Pedro. Took security perimeter from Pedro. Potential promotion competitor — actively building Loni visibility (Governance Agent / Enterprise Context getting named in Loni meetings, backed by Michael Marth). | Agreed privately on report-to-JIRA filtering process, then pushed back on the same point once Bertrand was on the email thread. Pedro retracted publicly — bad move. Philippe's tactic: agree 1:1, create dissent in front of the boss. His tactic worked once (April 2). Pattern to break: hold position under public pressure, don't retract. Recovery path: reintroduce tracking concern at implementation as a technical requirement, not a debate. Pedro also tends to use Philippe as first go-to for new trials (report-to-JIRA, new report sections) — stop this. Use Corey Dulimba as first testeur instead. Giving Philippe early access to unpolished work hands him the weak points. Post-divorce, very focused on women / social life — side-chats heavily during meetings. Per Pedro's own framing: "friends obsessed with girls will drop you for whatever is good for them in the moment." Treat as a colleague, not an ally. Second pattern confirmed April 2: uses Pedro as a real-time mirror — gets Pedro to validate his positioning in side-chat during a Loni meeting. Pedro said "very much on dirait hein cool!" on governance/enterprise context, Philippe closed with "C'est gentil mon loulou." Pedro became an active supporter without realising it. He doesn't attack — he makes you applaud him. Pedro confirmed April 2: Philippe is positioning for promotion. Treat as a competitor, not just a colleague. |

---

## Agent Owners (AEM)

| Agent | Owner |
|---|---|
| Experience Production | Corey Dulimba |
| Governance | Philippe Kapfer (PM) — devs: Alejandro Ramirez Cheves, Cornel Isbiceanu |
| Discovery | Apoorva Gupta |
| Content Optimization | Greg Klebus |
| Development / EDA | Brian Chaikelson |
| Onboarding | Nick Whittenburg |
| Modernization | Gabriel Walt / Mike Tilburg |

Demo regeneration: message sent April 1 to all owners + Mark Szulc (based in Australia). Philippe responded. Reminder set for April 2 noon to chase the rest.

---

## Fu Chi (AEP Personalization)

Fu Chi is a female AEP team member who built the personalized prompt recommendation pipeline. Regular 1:1 with Pedro (weekly sync set up). Shankari was invited to first sessions.

**Architecture she owns:**
- Pipeline: user prompts → clean → embeddings → K-means clustering → topic reports
- Signal blending: user history (primary) → org signals (fallback) → global signals
- Output: CSV/table of user IDs + ranked prompt recommendations
- EH owns prompt bar + buttons. AEP owns right rail.
- Prompt library is centralized — agent owners can enrich it

**Already exists in her data:** behavioral cluster analysis (content authoring, asset focus, cloud manager usage) — raw material for Priority 3 (Customer Profiling). This data is real, not hypothetical.

**Workflow-aware recommendations** (suggest next action based on prior steps) on her roadmap, not yet prioritized.

**Open actions with Fu Chi (as of April 8):**
- Fu Chi to share prompt recommendation file (April 7 ask)
- Fu Chi to share Analytics DB wiki page for widget recommendation analysis (April 7 ask)
- Fu Chi to send draft email + spreadsheet for agent owner prompt review (March 25 ask — status unclear)
- Fu Chi to share Workfront persona use case (March 25 ask)
- Pedro to review prompt file with Sorin + schedule follow-up call

---

## Active Actions (updated April 8, 2026)

- 🟡 **Felix reports** — live with PM section + updated tags (April 8). Under review. Corey Dulimba validation sent. Awaiting response.
- 🔑 VISIBILITY PATH TO LONI: (1) Felix reports live with PM section + updated tags, (2) Pedro validates with Corey, (3) Bertrand shows reports to Loni. Do not skip Corey step.
- 🟡 **Report hosting** — Certificate approved by Shankari (April 9). Felix and Quentin now configuring. CDN + Okta path unblocked. Target: early next week.
- 🟡 **JIRA pipeline** — tested with Governance agent, works. Update script once PM section live, then package as skill for other PMs next week.
- 🟠 **Priority consolidation view** — Bertrand ask April 7. Top 5-10 gaps with closure status. Build once reports live.
- 🟠 **Stable metrics deck** — Bertrand ask April 7. 2-3 slides, same format monthly. Draft with approximate values first.
- 🟢 **Grafana access** — obtained April 8 via IAM group GRP-AEP-GENAI-METRICS-VIEWER (Sweta). Cross-check against Felix reports still to do.
- 🟠 **AO 2.0 engagement** — engage Conrad, Ian Boston, Carsten, Sergey Generalov (not Sorin). Form a point of view on plugin/skills model for EH.
- 🟠 **Ilya Grafutko call** — responded April 2, open week of April 7. Schedule. Bertrand also meeting Ilya separately.
- 🟠 **Fu Chi deliverables** — await prompt file + Analytics DB wiki page. Then review with Sorin.
- 🟠 Other PMs on tags — next week after reports validated
- 🟠 Get on Sorin + Eugene email thread on UX AI framework
- 🟠 Get VRR tier definition from Yanira's wiki
- 🟠 Find owner of CM UI activity metrics — try #dx-product-measurement
- 🟠 Join "AEM experience hub extension builder" Slack channel
- 🟠 Find Canva roadmap doc → share with Sorin
- ✅ Tag review — done April 7, feedback provided to Felix
- ✅ Data compliance — Bertrand confirmed April 2. Closed.
- ✅ Brand Concierge — better defined between Peter and Sorin. No action needed.

## Logistics (updated April 9, 2026)
- April 8: Cloud Foundation sync — NOT Loni's call (Loni's is PM leads only)
- Check-in with Bertrand: next week — Bertrand away the week after
- Org reporting: still under Shankari on paper for 6 months, but check-ins go directly to Bertrand
- Ilya Grafutko call: booked for next Tuesday (week of April 14)

## H2 Planning — Agents (April 9, 2026)

Jaclyn Eckersley (planning/finance) asked @lebescon @pedrofer about HC tracking for Agent Investment for H2 — flagged as absolute requirement, needed it for H1 same day. Also asked who is presenting Agents in the H2 planning session.

Bertrand's response:
- Agents are covered within individual team presentations (Forms, Sites, Assets, Cloud) — no dedicated Agents team
- HC/capacity IS in their slide (to be created, or Canva for now) — Jaclyn can aggregate across teams
- Bertrand's guidance: dedicated slides only needed for **external dependencies** (AO, AI Assistant)
- Conrad W cc'd on the thread

Action for Pedro: ensure EH capacity is reflected in Bertrand's slide. External dependency slides needed for AO and AI Assistant.

---

## Status & Todo Files (Obsidian)

- EH: `AEM EH Status and Roadmap/EH - Status and Todo.md`
- AI Assistant: `AI-Assistant/AI-Assistant Status and Roadmap/AI-Assistant - Status and Todo.md`
- Both files: rolling status, todo with person + date captured, key dates, key people, conversations + links, session log.
- CLAUDE.md rule: always ask for conversation links when updating these files.

---

## Key Meetings / Documents

All paths relative to: `/Users/pedrofer/Library/CloudStorage/GoogleDrive-maprilpedro@gmail.com/My Drive/ObsidianVault/020 Professional/Adobe/Projects/2026/Experience Hub/AEM Experience Hub - Project Folder/`

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
- Meeting notes folder: `Adobe Projects 2026 Meeting Notes/` (renamed from `EH Meeting Notes/`)

---

## Slack Channels

\#experience-hub, \#experience-hub-ai-assistant, \#aem-home-platform-team, \#aem-home-core-team, \#temp-experiencehub-dxue, \#dx-product-measurement, \#tmp_aem_missing_prompt_library, AEM experience hub extension builder (new)
