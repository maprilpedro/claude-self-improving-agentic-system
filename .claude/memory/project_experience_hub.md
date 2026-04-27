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

## 2026 Yearly Review Goals (drafted with Bertrand, April 2026)

**G1 — Agent Intelligence & Reporting:** Build and own the agent intelligence layer that gives every AEM agent PM a clear view of what customers need, where agents fall short, and where they create measurable value. Drive improvement in Technical Success Rate and Value Realization across the AEM agent portfolio.

**G2 — EH Platform Integration:** Own Experience Hub's integration with AEP and Adobe DX, including AO 2.0 migration and the new agent prompting surface. Ensure EH remains a reliable and current entry point as the underlying platform evolves.

**G3 — Experience Hub Adoption & Growth:** Establish Experience Hub as the measurable driver of AEM practitioner adoption growth, with data and narrative that leadership can point to at any level. Document and attribute EH's contribution to AEM monthly active user growth. Deliver the contribution model and user profiling that make EH contextual and extensible, and enable other teams to surface their work through EH as a shared platform.

File: `AEM EH - Key Files/Experience Hub - 2026 Yearly Review Goals.md`

---

## Two Workstreams

**Workstream 1 — Experience Hub (fully owned)**
Pedro is PM of record. Team: Sorin Slavic (lead engineer), Eugene Bannykh (UX, US timezone), Mircea Salan (engineer, internship project lead), Anna Maria (new intern, started April 1 — cannot contribute meaningfully near-term).
Scope: EH product priorities (Skills+MCP surface, Contribution Model, Customer Profiling), Brand Concierge Summit light-up, Experimentation page integration, report hosting (CDN + Okta).

**Workstream 2 — Agent Assistant (contributor, not PM)**
AEP AI Assistant is built and owned by the AEP team. PM of record: `hanessia`. QI DRI: Ilya Grafutko (Sr PM, AEP Agent Orchestrator Platform). AEM AI Assistant is program-managed by WEM. Pedro is not in any ownership chain. His role: EH surface integration (integrating the AEP prompt bar), AEM agent reporting contributor, EH as the hero surface for AEM agents. Pedro must confirm this framing with Bertrand. Sorin asked directly in the April 1 refinement sync — still unresolved.

**AEP AO / AI Assistant role split** (per Ilya Grafutko Slack 2026-04-27, screenshot at `screenshots/20260427-ilya-ao-aiassistant-ownership-slack.png`):
- **AO Platform PM:** `@sgeneralov` (core, integrations) + `@igrafutko` (quality tooling / safety / compliance)
- **AI Assistant PM:** `@hanessia` (Adoption) + `@namitak` Namita (Dashboards, AI Integration, AI quality)
- **AO v2 (coworker):** `@sgeneralov` + `@igrafutko`
- **AO v2 — AIA extensions:** `@namitak` + `@hanessia`

**For AEP Grafana dashboard issues (Agents traffic):** ping Namita (`@namitak`). Specific dashboard Pedro tracks: `r2d2-ewewfsdgh4bpbhf7.eus2.grafana.azure.com/d/bfbjp58xxc9hcb/ai-assistant-on-ao-trial-cust...` (AI Assistant on AO trial customers). Open issue as of 2026-04-27 — task added to AI-Assistant Status & Todo.

**AI Assistant vs AOP — Pedro's mental model** (canonical source: `Experience Hub/AEM Experience Hub - Project Folder/AI Assistant AOP/AI Assistant vs AOP.md`, dated 2026-04-27):

- **AI Assistant** = the **conversational, generative AI layer**. The "brain." Natural-language interface, in-product copilots, chat UI. Interprets user intent, generates content, suggests actions. Designed for human interaction. Uses LLMs — fuzzy / open-ended / can hallucinate.
- **AOP** = **Adobe Orchestration Platform**. The "hands." Backend orchestration for workflows, multi-step processes, cross-system automation. API- and configuration-driven. Designed for system-to-system interaction. Deterministic — executes only defined workflows / rules.
- **They work together:** AI Assistant interprets the user's request → translates to structured intent → AOP receives that and orchestrates execution across services.
- **Short version:** AI Assistant = interprets and suggests. AOP = coordinates and executes.

**AOv2 architecture (open-source / plugin model)** — per Sergey Generalov / Manas Garg email thread April 2-4, 2026 (file: `AI-Assistant/AOP 2.0/AOP 2.0.md`):

- **AO** is the actual platform / codebase: `github.com/Adobe-Experience-Platform/ao`.
- **AOv2** = new version with **plugin and marketplace architecture**, following Anthropic open protocols for extending agentic harnesses.
- Pattern: install AO locally → create own marketplace git repo (template: `OneAdobe/ao-plugin-extensions-template`) → develop plugins / skills → install marketplace into AO.
- Internal docs: `aep-ao.pages.adobeitc.com/getting-started/` and `/plugin-development/`.
- Manas Garg leading AOv2 dev experience push. Trent Davies, Ken Russell, Sergey Generalov, Akash Maharaj, Alexander Falca on the core AO team.
- "Open source" framing — Adobe-internal but with maintainer/committer/contributor model; teams can send PRs to ao repo. CJA team already engaging via Josh Butikofer.
- This is the "harness" Conrad described April 14: distributed responsibility, contributed skills.

**AEM in this stack:** AEM Agents (EPA, Discovery, Governance, Content Optimization, EDA, Onboarding) are the workloads orchestrated by AOP. EH is the AEM landing page where the AEP AI Assistant prompt bar appears. So the user clicks in EH → enters AI Assistant → AOP routes / orchestrates → an AEM Agent runs → result back through AI Assistant → EH.
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

## Active Actions (updated April 14, 2026)

### TOP PRIORITY — Answer Loni's Question
- 🔴 **Loni's unanswered question (April 13):** "Do we have a view of what percentage of the top requests and stuff are making it into the agent?" Bertrand said no. Pedro's JIRA pipeline + priority consolidation view answers this. Goal: package it so Bertrand can take it back to Loni. This is the visibility move.
- 🔴 **Apoorva review outcome (April 16) — NOT validated yet. Punch list found.** Meeting with Apoorva + Ankur Arora (senior filter) + Varun Kalra (technical validator on her team) revealed blocking issues. Validation NOT secured. Must close the punch list before taking answer to Bertrand/Loni. Notes: `Adobe Projects 2026 Meeting Notes/Agent Owner Alignement/20260416 - Review Agent Report.md`.
- 🔴 **Apoorva fix list — BLOCKING:**
  1. **50-60% data gap vs Grafana.** Varun CSV: ~800-900 interactions for a week where report shows 1400-1500. Source is same (AEP Co-Pilot). Issue in tagging logic, window, or filtering. Investigate with Felix.
  2. **TSR counts "no result found" as success.** Apoorva: "this is then not a great metric to reflect." Redefine or split. For Discovery Agent, result-found rate is the right signal.
  3. **Tag classification bleeding across agents.** Discovery page showing pipeline troubleshooting (EDA), content update, brand validation (Governance). Per-agent tag filtering broken. Needs Lara + Felix on taxonomy.
- 🔴 **Apoorva fix list — HIGH PRIORITY:**
  4. **First Useful Result Rate missing.** This is the value realization metric Apoorva explicitly named for Discovery Agent (column N in her Excel). "We don't want users to do multi-turn prompts to be able to get to the right asset." GIFT from the meeting — maps directly to Loni's adoption framing.
  5. **Content-type breakdown for Discovery Agent:** assets / pages / content fragments / forms. Each has different team ownership. Without split, gaps can't be routed.
  6. **Aggregated metrics transparency.** Pedro admitted "aggregating things that don't make sense." Split or remove. Flag which are North Star vs operational/mature.
- 🟡 **Apoorva fix list — MEDIUM (track, don't commit):**
  7. **Promo SKU + Try Before You Buy credit utilization view.** Apoorva asked; not today's scope.
  8. **Calculation logic documentation per metric.** Apoorva asked how VR, SR, Adoption Blockers compute. Answers were thin.
- 🟠 **Next actions from Apoorva meeting (by end of week):**
  - ✅ Share repo + Python scripts with Ankur and Varun (done April 16)
  - ✅ Slack Lara + Felix into a dedicated channel with Ankur/Varun's team for taxonomy + data validation (done April 16)
  - 🔴 Kick off data discrepancy investigation with Felix (50-60% gap root cause first) — NEXT
  - 🟠 Schedule next Connect with Ankur's team next week (they asked)
- 🟠 **Priority consolidation view** — Bertrand ask. Top 5-10 gaps with closure status. Serves Loni's question.
- 🟠 **JIRA pipeline** — tested with Governance agent, works. Package as skill for other PMs once validation done.
- 🔴 **Calibrate Loni path expectation.** Apoorva's team has NOT signed off. Do not walk into Bertrand with "Apoorva validated." Walk in with "Apoorva's team stress-tested, found gaps, we're closing them. First Useful Result Rate incorporated. Report credible for Loni path after fixes."
- 🟡 **Greg Klebus** — mentioned needing an agent report (April 14). Watch — could be natural entry point for expanding pipeline to Content Optimization Agent.
- 🟡 **Ilya Grafutko 1:1 (April 14):** Compliance came up as a side note. Full notes pending.

### SECOND PRIORITY — EH as MAU Driver
- 🔴 **EH = key MAU driver (Bertrand, April 13 Loni meeting):** Bertrand said "I would like to think that what we did with Experience Hub has been a key driver in expanding the number of monthly active users for AEM." >60% customer base. This is Pedro's product. Surface this claim explicitly — own it, back it with data, make it a narrative Pedro controls not just a line Bertrand said once.
- 🟠 **Stable metrics deck** — Bertrand ask. 2-3 slides, monthly format. Now also the vehicle to substantiate the MAU driver claim. P2.
- 🟢 **Grafana access** — obtained April 8. Cross-check vs Felix reports still to do. Needed to back the MAU narrative.

### In Progress
- 🟢 **Felix reports** — LIVE. Shared with Bertrand (April 9). Jim feedback incorporated (April 13). Bertrand named Pedro and the dashboard in Loni's H2 planning meeting (April 13) — public sponsorship at VP level. Conrad also validated in Agent Owner alignment call same day.
- 🟡 **Report hosting** — Certificate approved by Shankari (April 9). Felix and Quentin configuring. CDN + Okta path unblocked.
- 🟠 **Agent reports W1 upgrade** — Quick wins in progress (April 13). Two-audience split (Exec PM vs Agent Owner), P0-P3 priorities, W1-W4 wave roadmap defined. File: `adbe-agent-dashboard-validation/20260413 - Agent Reports Upgrades.md`.
- 🟠 **Expand to all agent owners** — after Corey/Jim validation. Include: how to read reports, JIRA pipeline access.
- 🟢 **Grafana access** — obtained April 8. Cross-check vs Felix reports still to do.
- 🟠 **AO 2.0 engagement** — Conrad, Ian Boston, Carsten, Sergey Generalov. Loni confirmed AO 2.0 is a different stack (April 13 Loni meeting) — she pushed for modular architecture. This engagement is now more urgent.
- 🟠 **AO CSO (April 13)** — File attachments broke due to AO deploying breaking change with no proper notification (private channel, no lead time). Felix diagnosis: organizational failure, not technical. Follow-the-sun coverage also failed (bank holiday in Bucharest). Adds to trust deficit Bertrand mentioned at VP level.
- 🟠 **Greg Klebus 1:1** — Greg at Summit this week + next. Schedule for week of April 28. Agenda: review reports + test H-006 (ask: who is using Content Optimization Agent and what triggered their first use?).
- 🟠 **Ilya Grafutko call** — Tuesday April 14.
- 🟠 **Fu Chi deliverables** — prompt file + Analytics DB wiki page.
- 🟠 Other PMs on tags — after validation
- 🟠 Get on Sorin + Eugene email thread on UX AI framework
- 🟠 Get VRR tier definition from Yanira's wiki
- 🟠 Find owner of CM UI activity metrics — #dx-product-measurement
- 🟠 Join "AEM experience hub extension builder" Slack channel
- 🟠 Find Canva roadmap doc → share with Sorin
- 🟠 H2 planning — confirm with Bertrand what EH owns on external dependency slides (AO, AI Assistant)
- ✅ Reports live and shared with Bertrand — April 9
- ✅ Status deck built and shared with Bertrand — April 9
- ✅ Slack sent to Bertrand, agent owners, Ian, Yanira — April 9
- ✅ Tag review — done April 7
- ✅ Data compliance — Bertrand confirmed April 2. Closed.
- ✅ Brand Concierge — better defined between Peter and Sorin. No action needed.

## Jim Stoklosa — Report Contributor (Experience Production Agent)

Jim Stoklosa prepares reports on the Experience Production Agent for Corey Dulimba. Called April 9. Very talkative — good ideas but needs filtering. Provided feedback that drove PRs #20-#24 and the show-agent-answer feature. 

Validation role: Jim = data accuracy and feature behavior. Corey = PM owner sign-off (lighter ask, but required for Loni path).

## Try-Before-You-Buy Scoping (confirmed April 13, 2026)

Cloud Service + EDS customers = eligible (minus HIPAA / AI gen waiver exclusions). Managed Services = playgrounds only, not hooked up. Scope reports and validation accordingly.

## Loni + Jean-Michel Meeting (week of May 4, 2026)

**Jean-Michel = Jean-Michel Pittet, VP of Engineering AEM (Basel)** — confirmed April 16, 2026. He is the engineering-side VP peer to Loni (VP AEM & Commerce PM). The meeting is the top AEM leadership pair — Pedro's highest-visibility moment to date, not a generic "Loni meeting."

Jean-Michel's chain is separate from Loni's: Shantanu → Anil Chakravarthy → Sridhar Gantimahapatruni → Jean-Michel. Loni's chain: Shantanu → Anil Chakravarthy → Amit Ahuja → Loni.

Jean-Michel's team includes the full AEM Engineering leadership: Alexander Saar (VP Eng AEM Remote Germany, Ian Boston + Jaclyn Eckersley + Carsten Ziegeler under him), Michael Marth (VP AEM Engineering Basel, Gilles Knobloch + Felix + Mihai Corlan under him), Conrad Woltge (Sr Principal Architect direct report), Gitesh Malik, Mitch Nelson, Philipp Koch.

Present: state of agents + Project 42 status. High-visibility moment — first time Pedro presents directly to Loni on this work.

**Framing decided (April 14):** Show the report as-is. Be transparent — not compliant, to be handed off to DaaS team once formalized. Don't hide the compliance gap. This is the honest position and the right one for a VP audience. Priority consolidation view also to be ready.

**Timing update (April 14 AO 2.0 meeting):** The Loni + Jean-Michel meeting is now sequenced after a 2-hour internal strategy session on AO 2.0, planned for Wednesday afternoon the week after Summit (likely April 29). Loni + Jean-Michel follows the week after that (week of May 4). Pedro's ~April 28 date was an earlier estimate.

---

## AO 2.0 Strategy Meeting — April 14, 2026

Attendees: Bertrand, Conrad, Jaclyn, Yanira, Pedro (+ Speaker 1, likely Yanira's colleague).

### MAJOR: Pedro named PM of record for AEM–AO connection

When Jaclyn asked "who's responsible for AO, the connection with AO?", Bertrand answered: **"It's Pedro."** Sergei is PM on the AO side. Scope expansion beyond EH — Pedro is now the AEM-side PM liaison to AO. Explicit, public, in front of Conrad, Jaclyn, Yanira. Significant visibility signal.

### AO 2.0 — What it actually is (per Conrad)

Not backward-compatible in the way Bertrand initially described. It is a fundamentally different product.
- AO 1: central orchestration, central code base, central team trying to incorporate all changes.
- AO 2.0: a harness. Different surfaces. Different build model. Small subsets, can run in Adobe environment or customer cloud. Teams contribute skills and take responsibility for making them work.
- Usage pattern changes. Central orchestration assumption goes away.
- V1 stays operational in parallel — no forced migration, no time bound.

Bertrand's initial read ("we can plug our agents, it's compatible") is partially right on technical level but misses the strategic shift Conrad is flagging.

### Conrad's view on AO 1 adoption

"Widely not flying based on usage data. Nobody's using really heavily except maybe EPA. And EPA has JIRA surface and not even orchestrator — or it does not need orchestrator or assistant in core." Strong internal claim that AO 1 hasn't landed with customers. Important context for how aggressive AEM should be about reshaping strategy around AO 2.0.

### Loni's position (via Jaclyn, from KR review)

"We cannot just be at the mercy of somebody else. We need to have our own strategy of what we want to do." AEM must own its agent strategy, not follow AEP by default. This will be the frame for the Loni + Jean-Michel meeting.

### Decisions made

1. No update to Loni/Jean-Michel in the meantime. Communication line: "We are revisiting the impact of AO 2.0 and the opportunities it opens, after Summit."
2. Architects have the task to readout the impact of AO 2.0 on their agents. Call out 2 weeks ago, reinforced yesterday. Readout after Summit.
3. 2-hour strategy block Wednesday afternoon, week after Summit (likely April 29). Pedro + Conrad draft agenda; Bertrand + Conrad review by end of this week.
4. Then Loni + Jean-Michel meeting week after (week of May 4).

### Jaclyn's SLA ask (triggered by recent AO CSO)

The CSO response from AO was too slow. Pedro to clarify: do we have defined SLAs between AEM and AO as an internal vendor? What are they? This becomes Pedro's second scope item as AO liaison, alongside AO 2.0 strategy.

### Post-Summit AO call — attendees

Conrad: "I try to keep it small so we can actually think. We don't need more opinions, we need contributions to the goal."
- Yes: Pedro, Conrad, Bertrand, Ian Boston (check capacity — on SAM Rush), Trent Davis (engineering, preferred over Ken Russell), Sergei (AO PM).
- Excluded: Raul ("not sure we need Raul"), Apoorva (no), Shankari (Bertrand: "that's not the guidance she's getting from me or Loni").

### Pedro's actions (this week)

- Align with Sergei Generalov on AO 2.0 — understand functionally and technically what it means for AEM.
- Draft post-Summit agenda with Conrad. Review with Bertrand + Conrad by end of week.
- Schedule calendar invites once aligned on attendees.
- Pull together AEM–AO SLA picture.

### New contacts

- **Trent Davis** — engineering, AO side. Conrad's preferred technical contact for AO 2.0 conversations.
- **Ken Russell** ("the Scottish guy") — engineering, AO side. Bertrand's suggestion; Conrad prefers Trent Davis.

---

## Rubin — CXO-wide AI Assistant Usage Dashboard (April 15-16, 2026)

Angela Han owns Rubin. Silvia Mulet Ferre (AEP coordinator) reached out asking Pedro to help tag AEM users. URL: https://rubin.adobe.io/dashboard/login

**Rubin's actual source (confirmed April 16 by Karthik Penikalapati):** AEP AO chats DB. Not AEP Co-Pilot Report. Different pipeline from Felix but same AEP infrastructure neighborhood. Karthik: "we are ingesting all the AI prompt / response events, so regardless of their origin, if they touch AEP AO -> we should have it in Rubin." This directly contradicts Silvia's earlier "EH entry only" framing — Rubin is not designed as EH-scoped, it's platform-wide.

**Two lists, keep them distinct (scoping decision April 16, 2026):**

**(A) Rubin tagging list — all AEM-owned agents in AO chats DB (7):**
- experience_governance_agent
- governance_agent
- aem_experience_development_agent
- aem_experience_production_agent
- discovery_agent
- content_optimization_agent
- experimentation_agent

This is what was shared with Karthik on April 15 and confirmed April 16. Answers "which agents in AEP AO chats DB belong to AEM." Stays at 7 for completeness of AEM platform footprint.

**(B) Pedro's agent intelligence reporting scope (6):**
- experience_governance_agent
- governance_agent
- aem_experience_development_agent
- aem_experience_production_agent
- discovery_agent
- content_optimization_agent

**experimentation_agent is OUT of scope for Pedro's reporting.** Decision made April 16, 2026. Rationale: experimentation is not in the AEM agent intelligence narrative Pedro is building for Loni. Jim Stoklosa runs the Experimentation team, but the experimentation_agent doesn't fit the reporting work. Don't pull it into agent intelligence, don't include it in reports to Bertrand / Loni / JM, don't validate it with agent PMs.

Karthik on April 16: "yes, we have these agents you gave above." Definition layer landed in one exchange — Rubin tagging remains on the 7. Pedro's internal reporting runs on the 6.

**The inversion — Rubin needs something AEM has:** Karthik flagged that the AEP provisioning API doesn't return org status (COMMERCIAL, NFR, etc.) for AEM-only orgs. Rubin can't cleanly count commercial AEM users. Angela confirmed Felix has a local Prod orgs list. Karthik explicitly wants "a scalable way... it would be great, if this can flow into AEP provisioning." Felix's artifact = cross-org leverage.

**Angela's ask before the sync (April 16):** "Check out the Digest tab in Rubin and create a report on the My Digest tab. Would love to get your feedback on if you're able to configure the data sufficiently or need more AEM specific tweaks." That's an invitation to co-shape Rubin's AEM view. Pedro to configure and evaluate before the sync.

**Pedro's move (April 15):** Replied asking if Rubin pulls from Co-Pilot Report (source question), shared the agent list, proposed 30 min sync framed around "two different AEM user counts landing in leadership views." Soft scope question tucked in: "understand what Rubin is ultimately meant to tell us about AEM — helps make sure tagging and breakdowns fit what you're trying to show."

**Parallel FYI to Bertrand (April 15):** Slack using AO liaison scope frame. "Reporting back after."

**Strategic intent:** Pedro owns G1 (Agent Intelligence) and AO liaison role. Definition ownership is the moat on shared-data infrastructure — the 7-agent list is now locked in both tools. Next move is the Prod org list contribution, positioning AEM as the team that closes an AEP provisioning gap. That's Senior Director-level cross-org contribution, not extraction defense.

**Next steps:**
- Felix sync April 16 AM: brief on Rubin thread, plan Prod org list contribution
- Configure Digest + My Digest tab in Rubin before the sync (Angela's ask)
- Book 30 min sync with Angela, Silvia, Karthik (bring Felix)
- Follow-up Slack to Bertrand post-sync: definition alignment landed + AEM contributing provisioning fix

**Contacts:**
- Angela Han — Rubin owner. Senior Data Scientist Manager, Customer Engineering (San Jose). Reports to Richard Maraschi → Shivakumar Vaithyanathan (VP Platform Engineering). NOT in an AEP PM chain — she's Data Science / Engineering. This is why her tone is collaborative.
- Karthik Penikalapati — Rubin technical lead, Software Development Engineer, SJ. Reports to Angela Han. Ingests from AEP AO chats DB. Flagged provisioning API gap.
- Silvia Mulet Ferre — **Sr Product Design Manager, Adobe Design (Austin). NOT AEP.** Chain up: Guliz Sicotte → Archana Thiagarajan → Eric Snowden (SVP Adobe Design) → David Wadhwani. **She is Eugene Bannykh's manager.** Her reach into Rubin comes from her team having designers working across products.
- Uma Subbu — Sr Product Designer, Adobe Design (Chicago). Reports to Silvia Mulet Ferre (same team as Eugene). Emailed Pedro and Felix April 16: she and Silvia have been investigating AEM AI Assistant and Agent usage data using Felix's AEM Agent Report AND Rubin. They have UX hypotheses + UX Suggestions to present at the sync. This reframes the sync as also a UX research review, not just data alignment.

---

## Varun Kalra Discovery Agent Report Sync — April 22, 2026

58-minute working session on the Discovery Agent report validation. Major strategic signal + concrete measurement corrections.

### Platform legitimacy signal

Varun opened the meeting by voluntarily offering to retire his own wiki (the Discovery Agent repeat-usage + trends analysis he maintains for Apoorva) and consolidate into Pedro's reporting platform. Quote: "I want to get away from it because you're already doing a lot of work on this. I want to streamline and finalize on how we can ensure that there's only one way we are creating the final reports." First time a peer agent-owner team has chosen Pedro's platform as the canonical surface. This is a Senior Director-level scope signal.

### Data gap closed

Item 1 of the April 16 Apoorva punch-list (50-60% data gap vs Grafana) is resolved. Root cause was org-to-org-type assignment — the filter between internal / external wasn't working because orgs weren't properly mapped to their org types (Explorer, Try Before You Buy, Internal, Partner). Fix: AEP scorecard CSV export matched against org list from AEP. Pedro ran Claude delta checks, now below 3%. Source of truth confirmed as Copilot API. Varun will do formal validation pass.

### Measurement reframe — intent-level, not interaction-level

Varun's correction on Apoorva's 3 VR metrics (First Useful Result Rate, Query Unsuccessful Rate, Remaining Prompts Rate): they only sum to 100% if measured at **intent level**, not at interaction or chat level. One intent can span multiple interactions (user refines same goal). Splitting at interaction level produces buckets that never reconcile. Intent-level rules:
- Intent returned nothing → Query Unsuccessful
- Intent returned results, no follow-up within ~2 minutes → First Useful Result
- Intent required follow-up refinements → Remaining Prompts

2-minute window is an Apoorva-hypothesis that still needs confirmation. Pedro to loop Apoorva on: her actual calculation prompt/logic, exact window definition, whether intent continuation counts across or only within a single chat.

### "No results found" is a product gap, not a legitimate answer

Varun's framing: in agentic UX, returning "no results found" means "I can't do anything for you" — a failure to engage. Correct minimum response is a clarifying question or a suggestion. Discovery Agent returns "no results found" uniformly for (a) unsupported queries, (b) content doesn't exist, (c) search-quality failures. Collapsing all three into one response breaks triage. Governance Agent's "I cannot help with this" (distinguishable from empty match) is the better model. This is itself a Discovery Agent product gap, separate from the search-quality gaps.

### Varun's deep skill — to be absorbed into Pedro's platform

Varun has built a multi-source analysis skill for zero-result Discovery queries. It combines: the prompt, the code, Splunk logs, and live AEM instance state. Categorizes zero-results into: standard/semantic search, page searches, forms, content fragments, custom metadata, unsupported, miscellaneous. For standard semantic further splits by cause: content doesn't exist, semantic search disabled, user access issue, token expired, wrong filter, invalid AEM URL, timeout. Pfizer "Cephalon" typo case — skill identified user typed wrong product name. Varun wants this logic INSIDE Pedro's platform, per-agent custom block. Fields per gap entry: category name, prompt count, companies impacted, conversation IDs, example prompts, action items + JIRA links + end dates.

### Report UI feedback

1. Move weekly trends to the top (current week + trend visible together, not spread across the page).
2. Add externals count at the top (Varun surprised external interactions > internal).
3. Graphs as interactive (already good, confirmed).
4. Repeat users on 1-week window is fine for now (Apoorva has final say).

### Report-to-JIRA pipeline validated

Varun confirms usefulness IF end-to-end inside the same UI. Not useful if he has to feed data into a separate skill. Report should have a JIRA column with ticket + end date per action item. Exactly what Bertrand has been asking for. Alignment.

### Next Pedro actions

1. Loop Apoorva on the VR metrics: get her exact prompt/logic, confirm 2-min intent window, confirm intent-level aggregation.
2. Reorder report layout: weekly trends at top, current-week numbers below.
3. POC per-agent custom product gap block for Discovery — start with "standard semantic search" category using Varun's skill logic.
4. Get Varun's skill shared (pending his cleanup).
5. Build JIRA column into report template.

---

## P42 Status Meeting — April 21, 2026 (Jaclyn + Yanira + Pedro)

Short meeting, high signal. Jaclyn's frame runs the agenda — FinOps + portfolio investment discipline layered onto agent strategy.

### AO 2.0 session — confirmed on for next week

2-hour block. Agenda drafted by Pedro + Yanira. Conrad and Bertrand approved. AO side: Ken Russell AND Trent Davis both accepted (earlier Conrad-preference for Trent over Ken didn't play out as exclusion — both are in). Attendees: Pedro, Yanira, Jaclyn, Conrad, Ian Boston, Bertrand + Ken, Trent, Sergey on the AO side.

**New dedicated leadership Slack channel** created April 21: Pedro + Yanira + Jaclyn + Conrad + Ian + Bertrand. Purpose = keep decisions tight, avoid broader forums.

### Loni + Jean-Michel meeting — confirmed week of May 4

Jaclyn: week after Summit is "dead time" (people hammered). Target is the week after → week of May 4. Pedro to send a **light status summary next week** (week of April 28) to keep Jean-Michel warm before the big meeting. Doesn't need details — "even feedback from someone" works. JM needs education on AO 2.0 and "what it means for us" (AEM autonomy frame).

### Jaclyn's new asks of Pedro

1. **Headcount rollup per agent** for planning deck slide 40. Work with agent PMs to estimate HC per agent — rough is fine (50% allocations OK). Next planning session next week. Portfolio investment framing: Foundation did ~20% of heads onto agents; pattern to replicate.
2. **Profitability framing** for agents. Revenue expectations vs cost per agent — "at what point are we making money?" Not urgent, but on radar. Nobody remembers who PMM was for agents. Yanira's guesses: **Melissa Tao** or **Tina Nicu** for EPA.
3. **$500K P42 pre-prod dev/workflows/cloud infrastructure cost** flagged on a finance slide. Origin unclear — Jaclyn says "the other Shweta" (not Shweta Dua) who asked for cost centers. Jaclyn suspicious: "we have nobody using these agents, how could it be a half a million cost?" Jean-Michel has seen the number from finance; questions will come. Pedro to keep on radar and check if real.
4. **Summit survey — agent-perspective analysis via Claude.** Jaclyn: she did this for the AEM survey, called it "mind blowing." Pedro committed to try.
5. **Claude project for Loni/JM exec self-query** — Jaclyn's tip, she's giving other VPs Claude projects with analysis loaded so they can query themselves.

### Yanira — Monday Agent Alignment agenda

Open forum for Summit readouts. Unstructured data dump. Not the meeting to push new material.

### Strategic frame reinforced

Loni (via Jaclyn): "We don't want to be tied into whatever somebody else is delivering." Same line as April 14. This is the durable frame for AO 2.0 positioning in the Loni + JM meeting. AEM owns its agent strategy — not reacting to AEP.

### Compliance question Jaclyn raised (unresolved)

"Just close them and then we're compliant or what does that mean? Does AEM need to be compliant? Does AO need to be compliant?" Compliance ownership between AEM and AO is not clearly scoped. Future agenda item.

### Side item (not Pedro scope)

AEM Forms disabled for Summit (updating stopped) — re-enables automatically after Summit. Pedro confirmed.

---

## April 23, 2026 Session — Status File Maintenance + BVR Metric Framing

### Deadline compression
Apoorva validation punch-list deadline moved from **2026-05-09 → 2026-04-27 (Monday)**. Pedro's call, driven by the week-of-April-28 JM warm-up and the May 4 Loni + JM meeting. Item 1 (data gap) closed April 20-22. Items 2 / 3 / 5 / 6 must close by Monday. Item 4 (First Useful Result Rate) in progress. Ankur Connect remains scheduled for May 9 as a post-close checkpoint.

### Philippe review done — comments in progress
Pedro did a report review with Philippe (Governance Agent PM). Implementing Philippe's comments — mostly **per-capability filtered view**. In progress. Note: Philippe remains competitor-class per prior memory; this is him contributing signal Pedro needs, not a relationship reset. Keep the work tight, don't share unfinished views.

### 2 BVR metrics identified for Governance Agent
Philippe review surfaced 2 candidate BVR (Business Value Realization) metrics:
1. **Number of brand checks performed per month**
2. **Number of permission audit requests performed via agent per month**

Ownership split:
- **Validation with Philippe** (PM Governance Agent): confirm definitions match capability
- **Implementation with Lara** (parallel reporting track for Governance Agent): instrument the pipeline

Test this week. Source: [AEM Agentic Success Definition Compliance Framework](https://wiki.corp.adobe.com/spaces/WEM/pages/3774169978/AEM+Agentic+Success+Definition+Compliance+Framework) (WEM Confluence space).

First concrete application of **capability-level monthly usage** as the headline value metric (distinct from TSR / VR / VRR). Headline material for Loni + JM meeting.

### Status file maintenance
Both Status & Todo files (EH + AI-Assistant) updated with 5 Varun next-actions + 2 Philippe-review tasks. AI-Assistant file Current Status + Focus sections refreshed — they had been frozen at April 2 while reality had moved to April 22. New working rule: mirror tasks across both files when work spans surfaces; scan for stale sections before adding new tasks.

---

## April 24, 2026 Session — Priority Recalibration + Priority Consolidation Draft + OKR Alignment

### Priority recalibration (overwhelm diagnosis)
Pedro reported overwhelm with ~25 live threads and 12 items tagged 🔴 across EH Status file. Diagnosis: calibration failure, not capacity failure. Recalibrated to 5 load-bearing items for May 4 (Apoorva punch-list by April 27, JM warm-up week of April 28, AO 2.0 session April 29, Priority Consolidation view to prod May 1, May 4 deck). Everything else demoted to "Parked past May 4" with explicit label. Pedro confirmed: "I agree with the 5 top priorities."

### JM warm-up decision locked — Claude project, not email
Initial direction drifted into drafting an email warm-up. Pedro pushed back ("not sure I want to send this"). Vault audit revealed the KR3 note (`Deliver Loni + Jean-Michel presentation.md`) already contained a full SD-2 plan: "Ship the JM Warm-up as a Claude Project, not a Deck" — including what to load (Felix report, Priority Consolidation view, HC rollup, Apoorva punch-list status, AO 2.0 lite context, 7-agent portfolio list), seeded queries (10 pre-computed), delivery message draft, and CC strategy (Jaclyn). **Decision: Populate Claude project by Friday April 25, Slack link to JM Monday April 28, CC Jaclyn.**

### Priority Consolidation view — draft saved
New artifact at `AEM Experience Hub - Project Folder/AEM Experience Agent Reports/20260424 - Priority Consolidation View.md`. Answers Loni's April 13 unanswered question ("what % of top requests are making it into the agent"). Structure: Answer to the Question → Top 10 Gap Categories table (classified measurement / product gap / value realization, with status + owner + ETA) → Closure Mechanism (Governance Agent AEMAGT-1240 as proof point) → What's New Since March (intent-level measurement, "no results found" as product gap, capability-level monthly usage as adoption narrative, voluntary platform consolidation) → What We'd Want Next (3 asks) → What This Is Not. Feeds KR4 (ship May 1) and KR3 (core exhibit May 4). Volumes + unowned routing pending Apoorva validation close April 27.

### OKR structure discovered and documented
Full OKR structure exists at `/120 Projects/Work/OKRs/O1 - AI Agent Intelligence/` with KR Board (kanban) + individual KR notes containing Todoist-backed task IDs. KRs In Progress: Close Apoorva validation punch-list (KR1), 3 agent owners signed off on report, Deliver Loni + Jean-Michel presentation (KR3), Ship Priority Consolidation view (KR4). Planning: Stable monthly metrics deck, Define SLA for AEM Agents with AEP. Not Started: Update Reports weekly, Validate AI Intelligence Numbers with 3 agent owners by mid-may, BVR - Discovery Agent Methodology. New working rule: Status file Focus sections roll up to KR notes via `[[KR Note|KR#]]` backlinks, not via duplicated task tracking.

### Focus section rewrites
Both Status & Todo files now have unified Focus tables: 5 load-bearing items, same order, same KR backlinks. Each row = Item + KR link + Status + Due. Items beyond the 5 moved to "Parked past May 4" visual demotion. Session log entries added to both files.

---

## Logistics (updated April 16, 2026)
- April 8: Cloud Foundation sync — NOT Loni's call (Loni's is PM leads only)
- Check-in with Bertrand: next week — Bertrand away the week after
- **Reporting chain clarified April 16** (from org browsing screenshots): Pedro → Shankari Panchapakesan (Group PM, SJ) → Bertrand (Sr Director PM, Basel) → Loni Stark (VP AEM & Commerce, SJ) → Amit Ahuja → Anil Chakravarthy → Shantanu Narayen. Arrangement is **temporary** — Shankari is moving to report directly under Loni on a 6-month trial. Pedro's check-ins already go directly to Bertrand.
- Loni's actual title: **VP, AEM & Commerce** (not just AEM). Her team spans PM + Product Marketing.
- Ilya Grafutko call: held April 14 (week of April 14)

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
