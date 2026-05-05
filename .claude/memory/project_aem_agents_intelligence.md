---
name: AEM Agents Intelligence (AAI) project context
description: Full context on the AEM Agents Intelligence project — agent reporting platform, AO 2.0 liaison, Loni+JM May 11 deck, three-tier reporting, agent ownership, AAI stakeholders. Sister file to project_experience_hub.md.
type: project
---

> **Two-project split — in progress (2026-05-03).** Phase 1 scaffold landed. AAI vault folder at `2026/AEM Agents Intelligence/AAI - Project Folder/`. Companion file `project_experience_hub.md` covers EH product. EH content remains in EH file until Phase 2 trim completes.

AEM Agents Intelligence (AAI) is the agent-portfolio reporting and strategy work Pedro owns inside the AEM PM org. It is distinct from Experience Hub (EH, the AEM home-screen product). AAI maps to G1 (Agent Intelligence & Reporting). EH maps to G2 + G3.

**Pedro's role:** PM of record for AEM agent intelligence reporting. Named PM liaison AEM ↔ AO (Bertrand, April 14, 2026). Drives Felix reports, Priority Consolidation view, Portfolio Monthly Briefing, AEM-AO SLA. Owner of AAI surface for the May 11 Loni + Jean-Michel deck.

**Counterparts:** Yanira Castaneda (PgM AO-tracked agents — Pedro's PgM counterpart). Apoorva Gupta (Discovery Agent PM, validation gate). Felix Delval (data engineer, report pipeline). Lara (taxonomy + Governance reporting). Varun Kalra (Discovery validator). Karthik Penikalapati (Rubin technical lead). Conrad Woltge (Sr Principal Architect, AO liaison). Trent Davies + Ken Russell (AO eng). Sergey Generalov (AO PM). Jaclyn Eckersley (FinOps, AEM Eng VP-side).

**Org chain:** Pedro → Shankari → Bertrand (Sr Director PM) → Loni Stark (VP AEM & Commerce). Bertrand also reports laterally with Jean-Michel Pittet (VP Eng AEM, Basel) on agent strategy.

**Obsidian vault:** `/Users/pedrofer/Library/CloudStorage/GoogleDrive-maprilpedro@gmail.com/My Drive/ObsidianVault/020 Professional/Adobe/Projects/2026/AEM Agents Intelligence/AAI - Project Folder/`

**OKR home:** `/120 Projects/Work/OKRs/O1 - AI Agent Intelligence/` (KRs already AAI-correct: Apoorva punch-list, Loni+JM presentation, Priority Consolidation, agent owner sign-offs, monthly metrics deck, AEM-AO SLA, BVR Discovery methodology).

---

## 2026 Yearly Goal — G1

**G1 — Agent Intelligence & Reporting:** Build and own the agent intelligence layer that gives every AEM agent PM a clear view of what customers need, where agents fall short, and where they create measurable value. Drive improvement in Technical Success Rate and Value Realization across the AEM agent portfolio.

Canonical full doc: `2026/Experience Hub/AEM Experience Hub - Project Folder/AEM EH - Key Files/Experience Hub - 2026 Yearly Review Goals.md` (covers G1+G2+G3 — leave canonical, cross-link).

---

## Agent taxonomy

**Pedro's reporting scope (6 agents):** experience_governance_agent, governance_agent, aem_experience_development_agent (EDA), aem_experience_production_agent (EPA), discovery_agent, content_optimization_agent.

**experimentation_agent OUT** (decision April 16, 2026). Rationale: not in the AEM agent intelligence narrative for Loni. Don't pull into reports / validation / Bertrand+Loni+JM updates.

**Rubin tagging list (7 agents — broader than Pedro's reporting):** above 6 + experimentation_agent. Locked with Karthik Penikalapati April 16.

**Agent owners (AEM):**

| Agent | Owner |
|---|---|
| Experience Production (EPA) | Corey Dulimba |
| Governance | Philippe Kapfer (PM) — devs Alejandro Ramirez Cheves, Cornel Isbiceanu |
| Discovery | Apoorva Gupta |
| Content Optimization | Greg Klebus |
| Development / EDA | Brian Chaikelson |
| Onboarding | Nick Whittenburg (out of Pedro's 6) |
| Modernization | Gabriel Walt / Mike Tilburg (out of Pedro's 6 — but funded under AEMAGT-538) |

Site Advisory Agent (AEMAGT-2, Laurentiu Odoleanu PM, Remus Stratulat ENG) is customer-facing, integrated with Brand Concierge, runs on Content AI — NOT in Pedro's 6. Reference page at `2026/AEM Agents Intelligence/AAI - Project Folder/Site Advisory Agent (AEMAGT-2).md` (move target Phase 2).

---

## Three-tier reporting architecture (locked May 1, 2026)

**Tier 1 — QBR.** PMM-led (Tina Nicu / Akin / Vaishnav Gorur). Quarterly. Senior leadership audience. Reference: `/Users/pedrofer/Downloads/AEM Agents QBR_Feb2026_SP.pdf`.

**Tier 2 — Portfolio Monthly Briefing.** Pedro-led. Monthly. Senior management audience. AEM-only. v0 shipped April 30, 2026 at `https://main--aem-agent-reports--aem-epa.aem.page/reports/portfolio/2026-04/briefing`. 4 of 6 sections substantive (Executive Summary, MAU per agent 6-month line, Retention 71.6% EPA / 71.5% Discovery monthly orgs, Reach 767 active orgs / 59.7% cross-agent). Quality WIP banner. Sections 5-6 placeholder pending Indicator #8 (May 17). Spec at `aem-agent-data/PORTFOLIO-MONTHLY-BRIEFING-SPEC.md`.

**Tier 3 — per-agent reports (Felix).** Weekly. Agent PM audience. EPA pipeline LIVE.

Bertrand named the architecture. Pedro owns Tier 2. Yanira QBR ownership ask sits in Tier 1.

---

## Felix reports + report pipeline

**LIVE for EPA.** Shared with Bertrand April 9. Bertrand named Pedro and the dashboard in Loni's H2 planning meeting April 13 — public sponsorship at VP level. Conrad validated in Agent Owner alignment same day. Jim Stoklosa feedback incorporated April 13.

**Report-to-JIRA pipeline.** Tested with Governance Agent. Validated by Varun (April 22): useful IF end-to-end inside same UI; not useful as separate skill. Need JIRA column with ticket + end date per action item. MCP idea (Gilles Knobloch) — parking lot.

**Report hosting.** Certificate approved by Shankari April 9. Felix + Quentin configuring CDN + Okta path. Unblocked.

**Jim Stoklosa role:** prepares EPA reports for Corey Dulimba. Validation role = data accuracy + feature behavior. Corey = PM owner sign-off (lighter ask, but required for Loni path).

**Audit Sprint April 30:** 9 of 16 audit items closed in single day. 10 PRs. Wave 1 Tier 1 (5 trust-hygiene), Wave 2 Tier 2 (4 visible-commitment), 2 of Tier 3 early. Plus 2 Important Indicators (#4 No-Results Triage, #5 Owner column on Capability Gap Map). Plus monthly retention shipped (PR #55) revealing **45% weekly orgs vs 71.2% monthly orgs stickiness gap** on Discovery W17.

---

## Apoorva validation punch-list (KR1)

**Status:** items 2/3/5/6 deadline compressed April 23 from 2026-05-09 → 2026-04-27 (Monday). Item 1 closed April 20-22 (Varun: org-to-org-type assignment fix, AEP scorecard CSV match, Claude delta below 3%, Copilot API as source of truth). Item 4 (First Useful Result Rate) in progress. Ankur Connect May 9 = post-close checkpoint.

**Items (April 16 meeting with Apoorva + Ankur Arora + Varun Kalra):**

1. **50-60% data gap vs Grafana.** ✅ closed April 22 (Varun fix).
2. **TSR counts "no result found" as success.** Redefine — for Discovery, result-found rate is the right signal.
3. **Tag classification bleeding across agents.** Discovery showing pipeline troubleshooting (EDA), content update, brand validation (Governance). Per-agent tag filtering broken.
4. **First Useful Result Rate missing.** Apoorva's named VR metric for Discovery. Maps to Loni's adoption framing.
5. **Content-type breakdown for Discovery:** assets / pages / content fragments / forms.
6. **Aggregated metrics transparency.** Split or remove. Flag North Star vs operational.
7. (Medium) Promo SKU + Try-Before-You-Buy credit utilization view.
8. (Medium) Calculation logic documentation per metric.

**Walk-in line for Bertrand/Loni:** "Apoorva's team stress-tested, found gaps, we're closing them. First Useful Result Rate incorporated. Report credible for Loni path after fixes." NOT "Apoorva validated."

---

## Varun Kalra Discovery sync (April 22, 2026) — strategic signal

**Platform legitimacy signal:** Varun voluntarily offered to retire his own wiki and consolidate into Pedro's platform. Quote: *"I want to get away from it because you're already doing a lot of work on this. I want to streamline and finalize on how we can ensure that there's only one way we are creating the final reports."* First peer agent-owner team to choose Pedro's platform as canonical. Senior Director-level scope signal.

**Measurement reframe — intent-level, not interaction-level.** Varun's correction on Apoorva's 3 VR metrics: First Useful Result Rate, Query Unsuccessful Rate, Remaining Prompts Rate sum to 100% **only at intent level**, not interaction/chat level. One intent can span multiple interactions. Rules:
- Intent returned nothing → Query Unsuccessful
- Intent returned results, no follow-up within ~2 minutes → First Useful Result
- Intent required follow-up refinements → Remaining Prompts

2-minute window is Apoorva-hypothesis, needs confirmation.

**"No results found" is a product gap, not a legitimate answer.** Varun's framing: in agentic UX, "no results" = failure to engage. Correct minimum response = clarifying question or suggestion. Discovery uses single response for unsupported queries / content doesn't exist / search-quality failures — collapses triage. Governance Agent's "I cannot help with this" is the better model.

**Varun's deep skill — to absorb into Pedro's platform.** Multi-source analysis for zero-result Discovery queries. Combines prompt + code + Splunk logs + live AEM instance. Categorizes zero-results: standard/semantic search, page searches, forms, content fragments, custom metadata, unsupported. Per-agent custom block in Pedro's platform. Pfizer "Cephalon" typo case = exemplar.

**Report UI feedback:** weekly trends to top, externals count at top (externals > internals surprised Varun), graphs interactive (good), repeat-users 1-week window OK for now.

---

## Rubin — CXO-wide AI Assistant Usage Dashboard

**Owner:** Angela Han (Sr Data Scientist Manager, Customer Engineering, San Jose). NOT in AEP PM chain — Data Science / Engineering. URL: https://rubin.adobe.io/dashboard/login

**Source confirmed April 16 (Karthik):** AEP AO chats DB. Different pipeline from Felix but same AEP infrastructure neighborhood. *"We are ingesting all the AI prompt / response events, so regardless of their origin, if they touch AEP AO -> we should have it in Rubin."* Contradicts Silvia's earlier "EH entry only" framing — Rubin is platform-wide, not EH-scoped.

**The inversion — Rubin needs something AEM has:** AEP provisioning API doesn't return org status (COMMERCIAL, NFR) for AEM-only orgs. Rubin can't cleanly count commercial AEM users. Felix has a local Prod orgs list. Karthik wants this scaled into AEP provisioning. **Felix's artifact = cross-org leverage.** Pedro's move: own the contribution, position AEM as the team that closes an AEP gap. Senior Director-level cross-org contribution.

**Contacts:**
- **Angela Han** — Rubin owner. Reports Richard Maraschi → Shivakumar Vaithyanathan (VP Platform Eng).
- **Karthik Penikalapati** — Rubin tech lead. Reports to Angela.
- **Silvia Mulet Ferre** — Sr Product Design Manager, Adobe Design (Austin). Eugene Bannykh's manager. Chain: Guliz Sicotte → Archana Thiagarajan → Eric Snowden → David Wadhwani.
- **Uma Subbu** — Sr Product Designer, Adobe Design (Chicago). Reports to Silvia. Co-investigating AEM AI Assistant + Agent usage with Felix's report + Rubin. UX hypotheses + UX Suggestions.

---

## AO 2.0 strategy + AEM-AO liaison

**Pedro named PM AEM-AO liaison April 14, 2026.** When Jaclyn asked "who's responsible for AO, the connection with AO?", Bertrand: **"It's Pedro."** Sergey on AO side. Public, in front of Conrad, Jaclyn, Yanira. Significant visibility.

**AO 2.0 = different product, not backward-compatible** (per Conrad April 14):
- AO 1: central orchestration, central code base, central team incorporating all changes.
- AO 2.0: harness. Different surfaces. Different build model. Plugin / marketplace architecture. Anthropic open protocols. Small subsets, run in Adobe environment or customer cloud. Teams contribute skills + take responsibility.
- V1 stays operational in parallel — no forced migration.

**AOv2 architecture:** AO codebase = `github.com/Adobe-Experience-Platform/ao`. AOv2 = plugin/marketplace. Pattern: install AO local → create marketplace git repo (template `OneAdobe/ao-plugin-extensions-template`) → develop plugins/skills → install marketplace into AO. Internal docs: `aep-ao.pages.adobeitc.com/getting-started/` and `/plugin-development/`. Manas Garg leads dev experience push. Core AO team: Trent Davies, Ken Russell, Sergey Generalov, Akash Maharaj, Alexander Falca. CJA team engaging via Josh Butikofer.

**Conrad on AO 1 adoption:** *"Widely not flying based on usage data. Nobody's using really heavily except maybe EPA. And EPA has JIRA surface and not even orchestrator."*

**Loni's frame (via Jaclyn, KR review + April 21):** *"We cannot just be at the mercy of somebody else. We need to have our own strategy of what we want to do."* AEM owns its agent strategy, not following AEP by default. Durable frame for May 11 deck.

**April 29 strategy session outcome.** 2-hour block, Bertrand + Conrad + Yanira + Jaclyn + Ian + Carsten + Trent + Ken. Notes at `Adobe Projects 2026 Meeting Notes/Agent Owner Alignement/20260429 - Alignment_ AEM Agents & AOv2.md`.

**Status (corrected 2026-05-04 by Bertrand post-meeting):** AOv2 as AEM's forward agent path was **discussed, not decided.** Do NOT present as locked decision. Bertrand explicitly flagged this when Pedro began drafting Yanira's introduction.

**What was actually agreed (directional, not commitment):**
- AEM A2A servers decommissioned — removes parallel infra (agreed in principle, timeline not set).
- Internal-open-source engagement model with AO team (PRs, forks) — preferred working mode.
- Scope split direction: AEM owns use cases + practitioner experience + customer co-innovation + agent definitions. AO 2.0 owns harness + runtime + orchestrator. Treat as direction, not contract.
- Bertrand framing line (his words, usable as quote): *"I would prefer us, AEM, to focus on the AEM use cases rather than building technology if there's a dedicated team for the infrastructure around it."*

**Open / unresolved (do NOT close in Yanira intro):**
- Forward-path commitment to AOv2 — open.
- AO 1 → AO 2.0 backward compatibility — open since April 14.
- AEM-AO SLA scope (KR6) — Pedro liaison, scoping in progress.
- A2A decommission timeline — open.

**AI Assistant vs AOP — Pedro's mental model** (canonical: `AAI - Project Folder/AO 2.0/AI Assistant vs AOP.md`):
- **AI Assistant** = conversational/generative AI layer. The "brain." LLM-powered. Fuzzy / open-ended.
- **AOP** = Adobe Orchestration Platform. The "hands." Backend orchestration, deterministic execution.
- AI Assistant interprets request → AOP orchestrates execution.

**AEP AO / AI Assistant role split** (per Ilya Grafutko Slack 2026-04-27):
- AO Platform PM: `@sgeneralov` (core, integrations) + `@igrafutko` (quality / safety / compliance)
- AI Assistant PM: `@hanessia` (Adoption) + `@namitak` Namita (Dashboards, AI Integration, AI quality)
- AO v2 (coworker): `@sgeneralov` + `@igrafutko`
- AO v2 — AIA extensions: `@namitak` + `@hanessia`

For AEP Grafana dashboard issues (Agents traffic): ping Namita (`@namitak`).

**AEM-AO SLA scope (KR6).** Pedro PM liaison since April 14. Jaclyn ask triggered by recent AO CSO (response too slow). Open question: defined SLAs AEM-AO as internal vendor? Conrad + Trent + Sergey are AO-side counterparts. AO 2.0 backward compatibility unresolved (April 14 — Bertrand + Yanira + Jaclyn + Conrad in room, none could confirm). SLA-level commitment to push: "AO 2.0 will not break AEM agents A, B, C without N weeks notice."

---

## Loni + Jean-Michel meeting (week of May 11, 2026)

**Was week of May 4, rescheduled May 1 to week of May 11.**

**JM = Jean-Michel Pittet, VP Engineering AEM (Basel)** — confirmed April 16. Engineering-side VP peer to Loni (VP AEM & Commerce PM). Top AEM leadership pair — Pedro's highest-visibility moment to date.

**JM org (separate from Loni's):** Shantanu → Anil Chakravarthy → Sridhar Gantimahapatruni → Jean-Michel.
**Loni's org:** Shantanu → Anil Chakravarthy → Amit Ahuja → Loni.

**JM's team:** Alexander Saar (VP Eng AEM Remote Germany — Ian Boston, Jaclyn Eckersley, Carsten Ziegeler under him). Michael Marth (VP AEM Eng Basel — Gilles Knobloch, Felix, Mihai Corlan under him). Conrad Woltge (Sr Principal Architect direct report). Gitesh Malik. Mitch Nelson. Philipp Koch.

**Framing decided April 14:** Show report as-is. Be transparent — not compliant, to be handed off to DaaS team once formalized. Don't hide compliance gap. Right position for VP audience.

**Bertrand review of Portfolio Briefing:** Monday May 4 AM, before agent sync 4pm. Pending Bertrand confirmation. Pedro Slacked Bertrand the Briefing link + 71% retention finding May 1 night (in French, friendly tone).

**Senior Director moves status (as of May 1, unchanged May 3):**
- **SD-1** Haresh Slack drafted, not sent. Goal: confirm Vaishnav Gorur PMM + intro request. Plan: Mon May 4. Confirmation due Wed May 6.
- **SD-2** JM warm-up Claude project — in progress, not shipped. Due May 8. Loads: Felix report, Priority Consolidation view, HC rollup, Apoorva punch-list status, AO 2.0 lite context, 7-agent portfolio list. Seeded queries (10 pre-computed). Slack to JM with link Monday May 12 (CC Jaclyn).
- **SD-3** $500K P42 cost trace — not started. Due May 8.
- **KR4** Priority Consolidation view — April 24 draft. Due May 8.
- **Yanira QBR ownership ask** — task for Mon May 4.

**Vault gap (still open):** No canonical pre-meeting strategic brief next to KR3 note. Should draft week of May 5. Sections: strategic frame, what we present, what we don't, expected questions + pre-staged answers, exit definition.

---

## H2 Planning + HC Rollup (April 28)

Canvas at `Roadmaps/H2 2026 Planning - Initiatives and Roadmaps.md` (EH folder, cross-link from AAI). Full extraction + analysis at `Roadmaps/H2 2026 HC Rollup for AI agents.md` (move to AAI Phase 2).

**Three-table HC Rollup:**
1. **Direct Agentic Web Items (DX-1220)** — 9 items + Pedro-promoted (HOME-832 + AEMAGT-538 placed for narrative even though canonical parent is DX-1222). ~98+ HC.
2. **AI related but not in AEM Agents P42** — 3 items (WRKSP-1223 Fluffy Jaws V2, AEMEO-9508 Data Advisory Agent, AEMSRE-3429 P42 ORR). All under DX-1220 in JIRA but NOT in 6-agent reporting taxonomy. 14 HC.
3. **Agent-related Items in OTHER Initiatives** — DX-1222, DX-1223, DX-LLMO. 17 HC after AEMAGT-538 promotion.

**Slack Parent vs JIRA Parent dual columns** added per Pedro. Reveals LLMO-4141: Slack Parent = LLMO-4023 (current source doc) vs JIRA Parent = DX-1134 "Adobe LLM Optimizer / Project Elmo" which is **Closed**. Real-world data quality issue.

**Slide 40 draft mapping (gaps to flag Bertrand):**

| Pedro's reporting agent | H2 funded match | Status |
|---|---|---|
| Experience Production (EPA — Corey) | NOT directly named | ⚠ gap |
| Discovery (Apoorva) | NOT directly named | ⚠ gap |
| Governance (Philippe) | AEMAGT-856 — 11 HC | ✅ matched |
| Content Optimization (Greg) | possibly Content AI Support GRANITE-66359 (15 HC) | ⚠ confirm |
| Development / EDA (Brian) | AEMAGT-1282 — 16 HC | ✅ matched |
| Onboarding (Nick) | NOT directly named (Site Advisory ≠ Onboarding) | ⚠ gap |
| Modernization (Mike Tilburg / Gabriel Walt) | AEMAGT-538 — 33+ HC | ✅ matched |

Half of 6-agent taxonomy not visibly funded.

**Most consequential overlap:** **AEMEO-9508 Data Advisory Agent** (Shweta Dua, IceBox/Unassigned). 5-way overlap with Pedro: both P42, "Value Realization" explicit Phase 1 skill of Shweta's, persona includes "Product Managers" (Pedro's audience), framing positions vs "static dashboards" (Pedro's reports), MCP Layer overlap with Skills+MCP brief. IceBox = window to influence scope. Need Slack Shweta + Yanira this week.

---

## P42 Status — April 21 (Jaclyn + Yanira + Pedro)

**New dedicated leadership Slack channel (April 21):** Pedro + Yanira + Jaclyn + Conrad + Ian + Bertrand. Purpose = keep decisions tight, avoid broader forums.

**Jaclyn's asks:**
1. **Headcount rollup per agent** for slide 40. Foundation pattern: ~20% heads onto agents.
2. **Profitability framing** — revenue vs cost per agent. Not urgent, on radar. Yanira's PMM guess for EPA: Melissa Tao or Tina Nicu.
3. **$500K P42 pre-prod dev/workflows/cloud infrastructure cost** flagged on finance slide. Origin unclear ("the other Shweta," not Shweta Dua, asked for cost centers). Jaclyn suspicious: *"we have nobody using these agents, how could it be a half a million cost?"* JM has seen the number. Questions will come.
4. **Summit survey — agent-perspective analysis via Claude.** Jaclyn called the AEM survey version "mind blowing." Pedro committed to try.
5. **Claude project for Loni/JM exec self-query.** Jaclyn's tip — she gives other VPs Claude projects so they can self-query.

**Yanira Monday Agent Alignment agenda:** open forum for Summit readouts. Unstructured dump. Not the meeting to push new material.

**Compliance question Jaclyn raised (unresolved):** *"Just close them and then we're compliant or what does that mean? Does AEM need to be compliant? Does AO need to be compliant?"* Compliance ownership AEM-AO not clearly scoped. Future agenda.

---

## Yanira Slack consolidation (April 30)

Yanira Slack ("AEM Agents Usage at high level"), CC Jaclyn — feedback that current report's WoW data is "too transactional." Pedro confirmed co-innovation classification already in pipeline (just not surfaced). **Yanira ask + Bertrand KR5 Stable Monthly Metrics Deck + May meeting high-level summary all converged into the same artifact: AEM Agent Portfolio Monthly Briefing.** "Portfolio" naming locked April 30 (matches Jaclyn's frame from April 21 P42).

---

## BVR — Governance Agent (April 23)

**2 candidate BVR (Business Value Realization) metrics from Philippe review:**
1. **Number of brand checks performed per month**
2. **Number of permission audit requests performed via agent per month**

Ownership split:
- Validation with Philippe (PM Governance)
- Implementation with Lara (parallel reporting track)

Source: [AEM Agentic Success Definition Compliance Framework](https://wiki.corp.adobe.com/spaces/WEM/pages/3774169978/AEM+Agentic+Success+Definition+Compliance+Framework) (WEM Confluence space).

**Capability-level monthly usage** = first concrete application as headline value metric (distinct from TSR / VR / VRR). Headline material for Loni + JM.

---

## Priority Consolidation View (KR4)

Draft saved April 24 at `AAI - Project Folder/Agent Reports/20260424 - Priority Consolidation View.md` (Phase 2 move target). Answers Loni's April 13 unanswered question (*"what % of top requests are making it into the agent"*).

Structure:
1. Answer to the Question
2. Top 10 Gap Categories table (classified measurement / product gap / value realization, with status + owner + ETA)
3. Closure Mechanism (Governance Agent AEMAGT-1240 as proof point)
4. What's New Since March (intent-level measurement, "no results found" as product gap, capability-level monthly usage as adoption narrative, voluntary platform consolidation)
5. What We'd Want Next (3 asks)
6. What This Is Not

Volumes + unowned routing pending Apoorva validation close. KR4 ship date moved May 1 → May 8.

---

## H-005 RESOLVED (May 3, 2026)

**First ever resolved hypothesis.** *"Owning Cross-Agent Measurement Standardization Creates Structural Cross-Org Influence for the Experience Hub PM."* Proposed March 26.

**Confirmed with 7 evidence lines (Apr 13 → May 1):**
1. AEM-AO liaison naming (Apr 14 — Bertrand named Pedro publicly).
2. Felix reports named at VP level (Apr 13 — Bertrand to Loni).
3. Loni prompt-to-roadmap question Pedro answers (Apr 13).
4. Varun voluntary consolidation of Discovery wiki into Pedro's platform (Apr 22).
5. Karthik / Rubin definition acceptance (Apr 16 — 7-agent list locked in tools).
6. Three-tier reporting architecture locked, Pedro owns middle tier (May 1).
7. Portfolio Monthly Briefing v0 shipped (Apr 30).

**Lesson:** original test design ("count agent teams that adopt a TSR/VRR standard") was Director's test. Actual confirmation came at Senior Director's test (*"are you in the room when the architecture is being decided?"*). Both true now. **Cross-org influence accrues to owner of data substrate before any literal "standard" ships — don't gate role claim on standard's maturity.**

---

## Stakeholder shortlist (AAI lane)

**AEM Agent PMs:** Apoorva Gupta (Discovery), Corey Dulimba (EPA), Philippe Kapfer (Governance), Greg Klebus (Content Optimization), Brian Chaikelson (EDA), Nick Whittenburg (Onboarding), Gabriel Walt / Mike Tilburg (Modernization).

**Agent PgMs:** Yanira Castaneda (AAI counterpart), Pritie Sharda, Robert Guthrie, Marius Duta, Amit Arora, Prashant, Georgeta Vladescu-Viezure, Juliana Campbell.

**AO / AEP:** Conrad Woltge (Sr Principal Architect), Trent Davies (eng, AO), Ken Russell (eng, AO), Sergey Generalov (PM, AO), Ian Boston (compliance), Manas Garg (AOv2 dev experience).

**Data / Reporting:** Felix Delval (data eng, EPA pipeline), Lara (taxonomy + Governance), Varun Kalra (Discovery validator, Apoorva's team), Karthik Penikalapati (Rubin tech lead), Angela Han (Rubin owner).

**Design (Adobe Design lane):** Silvia Mulet Ferre (Eugene's manager), Uma Subbu.

**Leadership:** Loni Stark (VP AEM & Commerce), Jean-Michel Pittet (VP Eng AEM), Jaclyn Eckersley (FinOps, AEM Eng VP-side), Bertrand de Coatpont (Sr Director PM, manager), Shankari Panchapakesan (Group PM, transitional).

**PMM:** Tina Nicu, Akin (PMM for AEM survey), Vaishnav Gorur (new PMM AEM agents — pending confirm Wed May 6), Haresh Kumar (chain to Vaishnav).

**Cross-VP peer (Sunil Menon tree):** Cole Connelly (Principal PM, Prompt Library Platform). Tim Lott → Daniel Sheinberg → Sunil Menon (peer to Loni at VP level under Amit Ahuja). Strategic backstop = Stephen Gould.

**Special:** Jim Stoklosa (dual — EH for Experimentation surface, AAI as report contributor for EPA).

---

## Interpersonal — Philippe Kapfer (competitor frame)

Senior PM under Bertrand. Scope: Governance Agent + Security. Arrived 2 years after Pedro. Took security perimeter from Pedro. **Potential promotion competitor — actively building Loni visibility** (Governance Agent / Enterprise Context getting named in Loni meetings, backed by Michael Marth).

**Pattern (April 2):** agreed privately on report-to-JIRA filtering, then pushed back on the same point once Bertrand was on the email thread. Pedro retracted publicly — bad move. **Tactic:** agree 1:1, create dissent in front of the boss.

**Pattern to break:** hold position under public pressure, don't retract. Recovery: reintroduce tracking concern at implementation as technical requirement, not debate. Stop using Philippe as first go-to for new trials (report-to-JIRA, new report sections) — use **Corey Dulimba** as first testeur instead. Giving Philippe early access to unpolished work hands him weak points.

**Second pattern (April 2):** uses Pedro as real-time mirror — gets Pedro to validate his positioning in side-chat during a Loni meeting. Pedro said *"very much on dirait hein cool!"* on governance/enterprise context, Philippe closed with *"C'est gentil mon loulou."* Pedro became active supporter without realising. He doesn't attack — he makes you applaud him.

Per Pedro's own framing: *"friends obsessed with girls will drop you for whatever is good for them in the moment."* Treat as colleague, not ally. Treat as competitor.

---

## Pedro's session-named development gap (May 1 self-diagnosis)

*"i have a bias for delivery and poor communication skills strategically."*

**Reframe:** broadcast frequency, not skill issue. May 1 night Slack to Bertrand was first rep on the muscle. Stack 3 reps a day for a month and the diagnosis stops being true.

---

## Status & Todo files (Obsidian)

**AAI canonical (post Phase 1 — 2026-05-03):** `2026/AEM Agents Intelligence/AAI - Project Folder/Status and Roadmap/AEM Agents Intelligence - Status and Todo.md`

**EH:** `2026/Experience Hub/AEM Experience Hub - Project Folder/AEM EH Status and Roadmap/EH - Status and Todo.md`

**Old `AI-Assistant - Status and Todo.md`** — DEPRECATED 2026-05-03, banner points to AAI canonical, frozen pending Phase 2 retirement.

**Mirror rule retired 2026-05-03.** Tasks live in their owning project's Status & Todo. Cross-link in dependent project's Focus if blocking.

**CLAUDE.md rule:** ask for conversation links when updating these files. Accept "no link, date/time" for internal-only meetings.

---

## Slack channels

`#dx-product-measurement`, `#tmp_aem_missing_prompt_library`, leadership-tight channel (Pedro+Yanira+Jaclyn+Conrad+Ian+Bertrand, created April 21).

---

## Open vault gaps (still tracked)

- Stakeholder Map Vaishnav entry (held until Wed May 6 confirmation)
- Pre-meeting strategic brief for May 11 Loni + JM (draft week of May 5)
- Briefing v0 sections 5-6 (pending Indicator #8 on May 17)
