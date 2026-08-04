---
name: aem-agents-intelligence-aai-project-context
description: "Full context on the AEM Agents Intelligence project — agent reporting platform, AO 2.0 liaison, Loni+JM May 11 deck, three-tier reporting, agent ownership, AAI stakeholders. Sister file to project_experience_hub.md."
metadata: 
  node_type: memory
  type: project
  originSessionId: 5f12dcf1-db3b-44ce-bf6c-50e0a17cb9e9
---

> **Two-project split — Phase 2 structurally complete (2026-05-13).** AAI vault folder at `2026/AEM Agents Intelligence/AAI - Project Folder/`. Companion `project_experience_hub.md` covers EH. Meeting Notes moved to neutral `2026/Meeting Notes/` (2026-05-13). AI-Assistant legacy folder retired. No legacy folders remain.

> **📦 Archive discipline (weekly shards; last restructure 2026-07-01).** Old context lives in per-ISO-week shards `project_aem_agents_intelligence_ARCHIVE_<year>-W<wk>.md` (+ long-form reference in `..._ARCHIVE_reference.md`), mapped by `..._ARCHIVE_INDEX.md`. **To find old context: read the INDEX first (dates + topics per shard), then `rtk proxy grep` the shard — never full-Read a shard.** This active file = hot state (currently **the 2026-08-03 session only**; everything 07-15 → 07-27 archived to W29/W30 on 08-03) + the compact durable reference below. ⚠️ **The archiver moves dated blocks but does NOT move RESUME pointers — check the pointer still resolves after every run.** **Cap rule, enforced by `scripts/archive_memory.py` (run in `/consolidate` Step 5): keep this file < ~20K tokens / one-shot-readable; event blocks older than ~2 weeks auto-archive to their weekly shard + the index rebuilds.**

> ## ▶️ RESUME HERE — left off **2026-08-04** (skills-grooming session, spanning 08-03 evening → 08-04)
>
> **The live artifact is Pedro's Slack canvas `F0BNF9LDKMW` "AEM Skills Naming Convention — WIP"** — convention, meta fields, one marketplace, plugin naming. Its state and the remaining fix-list are in the **2026-08-04 SKILLS GROOMING block at the end of this file**. **Clint Goudie-Nice was the agreed next item and was not started.**
>
> **Pedro was on PTO from the evening of Fri 2026-07-24 to the morning of 08-02/03.** The return-queue state of play is the **2026-08-03 FULL SLACK SWEEP block further down this file** (search `2026-08-03 — FULL SLACK SWEEP`) — read it with the PTO caveat at its head. Dated follow-ups are in `watches.md`, which is the single registry.
>
> **The four things waiting on him**, in order: **Clint Goudie-Nice** (5 days unanswered in his own `#aem-agent-owners-alignement`, Gartner demo + customer onboarding this week, admin-only-skill gating + co-innovation-only scoping) · **Tina Ngo** (blocked: wants GA timelines for all Coworker skills, says customers can't use Coworker until AEM skills are GA) · **Alejandro Moratinos** (asked 07-30 what the AEM skill-naming convention is, after Bertrand wrote *"there's urgency"*; unanswered, channel silent since) · **Ramon Bisswanger** (waiting to sync the Security Health internal Go-Live; he holds the 74%-vs-28% remediation numbers). Plus **Philippe Kapfer's 08-03 DM** offering to update the canvas and reporting a Foundation-Internal prod problem, and **Hemanta Gupta's Rubin finding** (no ingress for non-AEP teams — threatens the port).
>
> ⏳ **Open with Gilles Knobloch:** Pedro asked him 08-03 whether the KR 1e video played in full or as the broken 1-second version. Awaiting reply.
>
> **Prior sessions:** 07-27 OKR-review prep → shard **W30**; 07-20/21/22 rollout, marketplace + TBYB blocks → shard **W30**; 07-16/17 Manas → **W29**. Read `..._ARCHIVE_INDEX.md`, then grep the shard.
>
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

**✅ 2026-07-24 — THE WEEKLY KR STATUS SHIPPED (KR 1e "Aggregate Value Realized", OKR-review format).** Final content: Agents (665 orgs −2.3% / 1,668 users +2.1% / returning 90 / cross-agent 49.8% +3.5pp, trailing-4w basis; headline "The Summit spike is behind us", retention bullet chart-backed only), MCP (new-data-source flag + 1.6M requests / 96k tool calls 70% specific / 1,202 orgs / top customers incl. Eli Lilly value profile + the closing line "Requests show traffic. Specific tool calls show what customers really do - that is the number we will report from now on" = the cycle-1 plant of [[migrate-leadership-from-a-volume-metric-to-a-value-metric-without-a-cliff]]), Experience Modernization (1,522 +13% MoM / 658 +12% / 27,094 pages +31% / partners 81/10 stable — W30 window; ⚠️ the dashboard had silently stayed on Jun 15–21, caught before reporting). **Playground section dropped from this cycle's status** (single-org instrument view; full-view numbers not pulled). KR sheet context: Q2 VR 19.5% At Risk, Q3 28.5% On Watch. Session pattern: every headline number today (MCP ÷35, 847-vs-539, playground "failure", Modernization stale window, my own −19%) was a measurement artifact until scope/window/basis was pinned — including one I produced myself (the −19% cross-basis diff, corrected same evening).

**Agentic Playground = AEM Sites Trial (confirmed by Gilles, 06-24 DM, "Oui").** The aem.now playground runs on the single `aemsitestrial` tenant, so the playground usage dashboard showing **"External Orgs: 1"** is BY DESIGN, not a classification bug. That dashboard is **Pedro's own `aem-agent-reports` program report** (`.../reports/programs/aem-sites-trial/...`) — Felix Delval built it, Pedro added the Value Realization level (04-23 `#franklin-crosswalk-playground`). ⚠️ Its auto-generated "Executive Summary" (*"critical failure mode… no real customer validation"*) is a **miscadrage** — a playground is not a customer-adoption metric; do not paste it into a KR status. Report the playground from the **same instrument as the 6/24 status** (the full-playground view with the Customers/Partners/Adobe/Personal split), never the external-only single-org cut. **Meta-finding (2026-07-24 KR-update session):** three reporting instruments in one day (MCP clean-start, agents 847-vs-539, playground single-org) each produced a misleading headline until scope/window/classification were pinned — the measurement layer needs hardening before any number headlines. Ties [[H-009]]. Retention finding banked in [[project_checkin_2026]] (orgs return 41-65%, users only 12-27%, bigger agent worse *user*-retention).

---

## Felix reports + report pipeline

> **Moved to `project_aem_agents_intelligence_ARCHIVE_INDEX.md` on 2026-07-01** to keep this active file Read-able in one shot. Load the archive on demand when working this lane. Current state is carried by the RESUME event blocks above + the durable facts below.

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

> **Moved to `project_aem_agents_intelligence_ARCHIVE_INDEX.md` on 2026-07-01** to keep this active file Read-able in one shot. Load the archive on demand when working this lane. Current state is carried by the RESUME event blocks above + the durable facts below.

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

## Stakeholder shortlist (AAI lane)

**AEM Agent PMs:** Apoorva Gupta (Discovery), Corey Dulimba (EPA), Philippe Kapfer (Governance), Greg Klebus (Content Optimization), Brian Chaikelson (EDA), Nick Whittenburg (Onboarding), Gabriel Walt / Mike Tilburg (Modernization).

**Agent PgMs:** Yanira Castaneda (AAI counterpart), Pritie Sharda, Robert Guthrie, Marius Duta, Amit Arora, Prashant, Georgeta Vladescu-Viezure, Juliana Campbell.

**AO / AEP:** Conrad Woltge (Sr Principal Architect), Trent Davies (eng, AO), Ken Russell (eng, AO), Sergey Generalov (PM, AO), Ian Boston (compliance), Manas Garg (AOv2 dev experience).

**Data / Reporting:** Felix Delval (data eng, EPA pipeline), Lara (taxonomy + Governance), Varun Kalra (Discovery validator, Apoorva's team), Karthik Penikalapati (Rubin tech lead), Angela Han (Rubin owner).

**Design (Adobe Design lane):** Silvia Mulet Ferre (Eugene's manager), Uma Subbu.

**Leadership:** Loni Stark (VP AEM & Commerce), Jean-Michel Pittet (VP Eng AEM), Jaclyn Eckersley (FinOps, AEM Eng VP-side), Bertrand de Coatpont (Sr Director PM, manager), Shankari Panchapakesan (Group PM, transitional).

**PMM:** Tina Nicu, **Tina Ngo** (Principal PMM, AEM agents GTM + customer-trial pitches — added NYL + State Street to a TBYB cohort 05-27 w/ Namita Krishnan; pricing/packaging angle. **DM'd Pedro 07-07 22:12 + 07-08 pre-attributing the coworker-migration lane** — "i hear you're leading the efforts for coworker migration across all aem agents… is there a standard weekly meeting you own"; Pedro pointed her to GA canvas F0BD4RALNHF. = comms-lane PMM counterpart to Akin, natural fold-in for the weekly / comms-plan. ⚠️ **NOT Tina Nicu** — two Tinas in PMM. `tinan@adobe.com`, U0284AYUX99), Akin (PMM for AEM survey + TBYB comms owner), Vaishnav Gorur (new PMM AEM agents — pending confirm Wed May 6), Haresh Kumar (chain to Vaishnav).

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

---


> ### 🔴 2026-08-03 — FULL SLACK SWEEP (16 channels + all DMs/group-DMs, window 07-24→08-03, 4 parallel readers + a direct DM search).
>
> > ## ⚠️⚠️ FRAMING CORRECTED SAME SESSION — **PEDRO WAS ON PTO FOR ESSENTIALLY THIS ENTIRE WINDOW.** Read the block below with that in front of it.
> >
> > This block was first written with the headline *"three decisions moved without him and he is invisible on every decision surface."* **That framing was wrong and it was my error, not a finding.** Pedro's PTO ran **from the evening of 2026-07-24** (confirmed by him 08-03; corroborated by Andres Bott 07-29 *"had a quick chat with Pedro before his PTO"* and Ramon Bisswanger 07-29 *"enjoy your PTO"* / 07-30 *"don't look at it during the PTO"*). **Of the ~10 days audited, only 07-24 was a working day, and it was his last one before leaving.** Almost every "unanswered ask" below arrived 07-28→08-03 and is simply an inbox after a holiday.
> >
> > **The evidence was in my own hands** (three separate PTO references in the material I read) **and I fitted a fortnight of holiday into a behavioural narrative I was already carrying** from the Workday feedback and the H-007 resolution. That is the exact failure the 08-03 System Review named — a hypothesis that keeps finding its own confirmation. **Rule: establish the subject's working days BEFORE reading silence as behaviour.**
> >
> > **What survives the PTO explanation (short list):** the 07-24 marketplace audit was never posted *on a day he was working and had named it as his pre-weekend commitment*; the MCP instrument warnings; Security Health shipping; the roster/method corrections. **What does NOT survive:** "seven unanswered asks", "his posts died", "invisible on every decision surface". Those are holiday, not behaviour.
> > ✅ **PTO WINDOW CONFIRMED BY PEDRO 2026-08-03: from the EVENING of Friday 2026-07-24 until his return this morning.** (He said *"du 24 au soir a aujourd'hui 2 aout ce matin"*; today's system date is 08-03, so the return day is 08-02/08-03 — one-day ambiguity, not load-bearing.) **The earlier memory note "PTO starts 07-27" was wrong — it was 07-24 evening.**
> >
> > **→ Two consequences.** (1) **2026-07-24 was his LAST WORKING DAY**, which is why the marketplace audit was on that day's list at all ("close or hand off before Monday"). It slipped on the way out the door — ordinary, and n=1. (2) **The audited window contains ZERO normal working days.** Every dated item below is either his last-day wrap-up or something that happened while he was off.
> >
> > **🔑 HE WORKED ON FOUR SEPARATE DAYS OF HIS OWN HOLIDAY** — 07-27 (evening, Tracy Seibel / video for the KR status), 07-29 (Security Health docs), 07-30 (wrote + shipped the release-notes paragraph through to publication with Guillaume Carlino; Ramon DM; the Aditi/Pierre-Tager reply), 07-31 (release-ceremony check with Victor Mirica + Emil Serban; the `@here` in #aem-p42-leadership). **Note it as a fact about how he takes time off, and do not treat any of those days as evidence of availability.**
> >
> > **✅ RESOLVED 2026-08-03 — THE OKR REVIEW FORMAT WAS A RECORDED VIDEO.** Pedro recorded and submitted KR 1e **from his holiday** and **Gilles Knobloch presented it**. So the 07-27 date and the PTO window are both correct and not in conflict. The artifact: `AEM Prio 1e  Agents Status v2.mov`, **4:47**, emailed 07-27 to **Tatyana Kozachek + Gilles Knobloch**.
> > **🔴 But it did not upload cleanly and was never confirmed fixed** — the copy in the review folder streamed as **0:01**; Tracy Seibel reproduced it four times and the only fix on record is *"download it from the video folder… added a comment with instructions"*. **See `watches.md` — the debrief now leads with "did it play in full?", and that question gates everything else about the 07-27 outcome.**
> > **🔑 Worth naming for the promotion case, without moralising:** the speaking notes were rewritten in his own spoken voice, he recorded a 4:47 video on his own holiday, and **someone else carried it into the room**. That is credit-attached (his voice, his artifact) but it is not VP-facing presence — relevant to the check-in finding that VP-direct visibility has been thin since the May-11 deck ([[project_checkin_2026]]).
>
> **🔴🔴 CORRECTION FIRST — the 07-24 marketplace audit was NEVER POSTED.** See the corrected block in `watches.md`. Verified three ways (full thread read `1784720330.787079` = 5 replies ending at Pedro's 07-22 hedge; `from:@Pedro in:#p42-architecture after:2026-07-22` = zero; channel sweep = zero). **It was banked ✅ DONE on the day it was planned and never checked against Slack.**
>
> **THE THREE DECISIONS THAT MOVED WHILE HE WAS AWAY** (⚠️ *while he was away*, not *without him* — the 07-28→07-30 timing is holiday. Only the un-posted 07-24 audit is his.)
> 1. **Marketplace consolidation — DECIDED 2026-07-28 by Satya Deep Maheshwari + Carsten Ziegeler.** Satya opened *"One AEM skills repo: Starting this thread to collect what all is needed to proceed"*; Carsten: *"Lets use github.com/Adobe-AEM-Foundation/aem-aia-extensions"* → *"I'll create the teams and CODEOWNERS"* → PR `aem-aia-extensions#65`. Satya moved the Forms plugins over 07-30. Wiki **`3983883638` "20260728 AEM Coworker Manifest Marketplace Topology"** published 07-30, *"Looking fwd. for inputs"*. **Carsten cross-posted it to `#aem-agent-owners-alignement` 07-30 as *"Reposting the decision to use one AEM wide skill repository (for coworker) for more awareness"*.** Six days after Gilles asked Pedro to own it from a PM point of view. ⚠️ **Raul Hudea proposed renaming the repo to `aem-plugins-marketplace`** (Carsten: *"eventually yes"*) — open, and it is Pedro's naming lane. **Corey's *"do we have a decision and go forward plan? If not, when will we?"* is still unanswered 12 days on.**
> 2. **🔴🔑 SKILL NAMING — BERTRAND DECLARED URGENCY AND THE QUESTION DIED ON THE FLOOR.** In `#aem-agent-experience-governance` 07-30, Bertrand: *"when i do so in Coworker, the 'governance' skills are not bubbled up… I wonder if we should start following the AEM naming conventions for these skills (aem-brandgovernance-…)"* → *"ok they are not following the naming convention that was decided"* → *"**there's urgency in getting all of that renamed/resrtructured**"*. **Alejandro Moratinos, 07-30 09:03: *"I can change it. What should be the naming convention?"* — UNANSWERED, and that is the LAST message in the channel. Silent 4+ days.** Meanwhile **the convention is being invented by engineers in a group DM Pedro sits in** (Brian Chaikelson *"always 4 tokens (separated by a dash)"* → `aem-cloudmanager-release-update_schedule-management`; Sergiu, Emil, Marius; PR `aem-aia-extensions#63` merged 07-30). **Emil Serban's direct question — *"should we also update the plugin names?"* — is unanswered by Pedro.** Sergiu also *"hidden the internal skills/plugins"* 07-31 (`aep-ai#8835`, `aem-aia-extensions#76`).
> 3. **Co-innovation pods process — Yanira cc'd Pedro AND Bertrand explicitly to drive a decision** (`#aem-agent-owners-alignement` 07-27, *"please post Feedback, Questions, Concerns on this thread so we can drive towards a decision"*). Brian Chaikelson posted a full counter-model (*"more validation than co-innovation"*, 5 steps); **Tina Ngo posted the substantive pricing/positioning answer 07-30** (one SKU, 10k trial credits carry over, **intro rate 25 credits per prompt**, *"our skills are not GA in coworker. aep team needs our skills to be GA"*). **No decision. Neither Pedro nor Bertrand replied.**
>
> **🔴 HE WAS REMOVED FROM THE WAR ROOM'S NEW HOME.** 2026-07-28 19:41, **Yelena Doliner removed Pedro from `#aep-coworker-core`** (search confirms he can no longer see it). **Same day, Yelena moved the substantive traffic there**: *"lets use our other channel for the details on optin/out and other eng, product and PMM related items"* → *"its used to be our trial channel, now changed name"* → *"**aep-coworker-core**"*. `#aia_coworker_convergence` has been silent since 07-30 01:57 as a result. ⚠️ **Fact, not motive — do not infer intent.** Memory context: Manas handed convergence closure to Yelena on 07-20.
>
> **SEVEN ASKS WAITING IN HIS INBOX** (⚠️ all landed 07-29→08-03, i.e. during PTO. **This is a return-from-holiday queue, not a responsiveness finding.** Kept because the *content* matters.)
> - **Tina Ngo, DM 07-30 20:07** (blocking, PMM): *"can you please send over ga timelines for all the skills in coworker? **we cant let customers use coworker since our skills arent in there yet** (this is what aep tells me)"*. She also said publicly 07-30: *"i've asked pedro to invite me to any agent alignment meeting but havent seen it yet"* — **Yanira forwarded the series herself 6 min later and cc'd Pedro.**
> - **Hemanta Gupta, `#aem-agent-reports-pilot` 07-29** (⚠️ the channel memory recorded as *dormant since 05-27* — **it is not; Pedro's own 07-15 thread is live**): a full Rubin code investigation — *"the etl pipeline is a walled-garden intended for internal use by AEP… **does not seem to provide any hooks/extension points** for non-AEP teams to plug in their own data sources"*, AO1 and AO2 land in **separate tables (`interactions_v2` / `interactions_ao2`) with no unification in the Rubin app**. Ask: *"If you have a direct contact within their team, could we get the above confirmed?"* 🔑 **This is hard evidence on [[H-009]] and it says the port Pedro is planning may have no ingress.** Also unanswered: **Satya Deep Maheshwari 07-24** *"depends if Rubin is the central place to gather _all_ agentic usage or just the coworker parts. @Pedro Ferreira wdyt?"*
> - **Sergiu Coman, group DM 07-31:** *"From the reports DB would it be possible to extract a table with top users for a specific agent? Do you store such data?"*
> - **Emil Serban** (plugin naming, above) · **Delhibabu Vengam bhanumoorthy 07-31**: *"I do not see the full year rotary schedule. when do you think it will be published?"* (Robert Guthrie in-thread) · **Jennifer Randle** (Sr TAM) 07-30: *"I've replied to you over email"* · **Philippe Kapfer, DM TODAY 08-03 10:47-10:50**.
> - **🟢 PHILIPPE KAPFER IS OFFERING TO DO PEDRO'S WORK, TODAY.** *"Salut l'ami… Voilà le message que je voulais donner à Yanira, mais **je crois que c'est toi qui gères le status de la migration vers AOV2**"* + a status ready to paste (*"We are onboarded in Co-worker for 3 weeks now, **except in Foundation Internal where someone has replace skills with One AEM MCP and this is not working well!**"*; Governance incl. Enterprise Context available; DRM ported by Discovery team; content-hub permissions with Mohit Arora, moving H2) + *"**Ou est le canvas que je pourrais mettre à jour pour te simplifié la vie ?**"* ⚠️ Read with the competitor frame, but the ask is real, the offer is free labour, and **it concedes that Pedro owns the AOv2 migration status.** Note the concrete prod incident inside it.
>
> **BERTRAND ASKED TWO QUESTIONS IN PEDRO'S LANE — BOTH LANDED DURING HIS PTO, BOTH STILL WORTH ANSWERING ON RETURN**
> - **07-29, `#p42-architecture` (public):** *"Our target is not one AEM manifest: It's a set of AEM plugins… **Who owns "fixing" this and making sure we (AEM) are also represented properly in the other official manifests?**"* — never answered by name. Carsten/Ankush debated mechanics instead; **Ankush: *"There is no default even if naming conventions make you believe so, segments map an org or users in an ims org to manifest."***
> - **🔑 07-28, group DM with Yanira + Aditi Patwardhan (Principal PM, Experience Cloud):** *"**I think Pedro did some of this analysis in the past aem-agent-reports.corp.adobe.com, but I don't think we ever got to actionable insights, e.g. verifying alignment in between the questions and the skills and tools.**… customers are asking things like 'what the last 5 pages that were published'… **would we be covered for this kind of question now?**"* **That is a mild, written critique of Pedro's own G1 deliverable in front of a new Principal PM — and the "missing" piece he names IS Pedro's skills-disambiguation initiative, which Bertrand does not connect.** Aditi answered with her plan; **Pedro's last message in that DM is 07-21.** Bertrand also: *"I woud like more structured reporting and analysis on this, AEM-wide"* (07-30, Pierre Tager DM) — Pedro replied only *"Indeed and participated already"* about her meeting attendance.
> - ⚠️ **Aditi Patwardhan is now researching customer agent usage using Pedro's own reports**, coordinating "with Yanira and Pedro", plan = *"look at AI assistant history and make sure we have all the skills needed to answer the questions"*. **That is the skills-vs-questions alignment audit.**
>
> **His own two posts got no replies** (⚠️ one is a Friday `@here` before a weekend, the other landed as he went off — weak signal, do not read as a visibility failure): `#aem-p42-leadership` 07-31: *"@here Please send me your topics for Agents Alignment Meeting next Monday please"* → **zero replies, and it is the ONLY message in that channel in 10 days.** `#aem-agent-owners-alignement` 07-24: *"@Philippe Kapfer - you mentioned co-innovation difficulties… anything you want to share here?"* → **zero replies** (Philippe posted in the channel 07-29 on another thread).
>
> **🔴 THE BIGGEST UNANSWERED ASK IN HIS OWN FORUM.** **Clint Goudie-Nice, `#aem-agent-owners-alignement` 07-29 23:19 — ZERO replies in 5 days.** Ian Reasor routed him there. Asset Sourcing Portal + Content Supply Chain Agent, PR `aep-ai#8220` installs both plugins at 0.2.0 **into the shared `aem-aia` manifest across local/dev/stage/prod**. His two questions: *"How do we ensure these skills participate in selection only for the specific customer IMS orgs currently co-innovating with us?"* and *"How do we prevent an admin-only skill from being selected for a user before we have validated that the user is actually an AEM administrator?"* — plus *"I dont see how the AEM administrator can be reliably inferred from product-profile name"*, PLAT-290634 filed for a remote permission-provider. **Next-week needs: Asset Sourcing customer onboarding + a Gartner demo.** 🔑 **This is the customer-facing plugin-boundary question, asked in Pedro's forum, with a deadline.** Same shape: **Gerald Prendi 07-29** on `required_entitlements` gating for the Governance plugin in the default `cx-coworker` manifest (*"How could we navigate this?"*) — also unanswered, incl. by Philippe.
>
> **🟢 WHAT ACTUALLY WENT WELL (do not lose this in the reaction)**
> - **SECURITY HEALTH SHIPPED AND THE RELEASE NOTES PUBLISHED 07-30.** Pedro wrote the paragraph, Guillaume Carlino put it under the Foundation section, published that afternoon. Docs live 07-28 (Ramon toggled the feature live *"yesterday morning after the docs were published"*). Penetration Tests doc also published.
> - **🔑 RAMON'S GO-LIVE DRAFT CARRIES NUMBERS PEDRO SHOULD BE USING:** *"**74% of LA customers remediated vulnerabilities, vs. just 28% across all AEM customers — visibility drives action**"* (20 LA customers); *"**914 production programs currently carry 51,101 open third-party library vulnerabilities**"*. Target `#one-aem-team-announcements` + manager emails; Ramon aligned with "Vali" on an internal Go-Live story, sync when Pedro is back. **That 74-vs-28 is the single best EH-adoption proof point available and it is a contribution-model receipt.**
> - **The security-skill POC works.** Eugene Bannykh + Andres Bott + Ramon: WebMCP hit limits (not on prod, no findings on stage) → pivoted to a **Skill** returning findings + a link; Ramon added `securityHealthId` to the MCP tool result for routing to `/experiencemanager/security/health/detail/<id>`; deployed to prod 07-29; Eugene *"Works perfectly!"*. New repo seen: `Adobe-AEM-Foundation/Starfish-marketplace`. **Andres's plan (07-29, EGA channel): expose Starfish security via the EGA marketplace for Coworker + via One AEM MCP for 3rd party; *"had a quick chat with Pedro before his PTO"*.** Tuicu concurs; only concern is business-side bundling under Brand Governance.
> - ✅ **Resolves the 07-24 watch ambiguity: the UI-vulnerabilities POC group is Eugene Bannykh · Andres Bott · Valentin Olteanu · Ramon Bisswanger (+ Yanira, Pedro).** "Andres Valentin" was two people. Group DM `C0BKK3HTC4W`.
> - **Pedro caught and publicly self-corrected a bad MCP number in 8 minutes** (07-24, `#aem-mcp`): flagged Content MCP ~345k → 48k, Gilles asked if it was One-AEM-MCP rise, Pedro: *"My bad - was using a deprecated dashboard"* + posted the valid one. Clean, fast, credible.
>
> **🔵 MCP INSTRUMENT WARNINGS — READ BEFORE QUOTING ANY NUMBER**
> - **Jabran Asghar, 07-24: *"only use 30d time frame for now … found a bug in some panels not respecting the time filter, will fix that next week."*** No fix confirmation posted. Also: wait for the blue circle before reading stats.
> - **🔴 TERMINOLOGY DRIFT, LIVE AND UNDECIDED.** Tanju's report now uses the unit **"operation"**. **Christian Meyer challenged it 07-28**: *"I suppose that one only makes sense in context of code-mode; hence this would also mean going back to "tools" I suppose?"* Tanju: *"if we add the content mcp operations map nicely to tool calls."* **No decision.** The locked term is **Tool Calls** ([[reference_mcp_terminology]]) — Pedro owns this lock and it is slipping.
> - **Report v3 redefines "Unknown" into three named buckets** (result-status undetermined / category unclassified / org could not be attributed).
> - **Attribution is broken in two ways, both unanswered:** unresolvable IMS orgs (`127B272369BC84400A495C0A@AdobeOrg`, 19,922 requests — Jabran: *"It might be that AEM trial envs are playing a part"*), and **Eli Lilly present in the management dashboard but absent from the per-customer deep-dive** (Brian Chaikelson 07-31, no reply). ⚠️ **Eli Lilly is in the OKR-review speaking notes.**
> - **Tanju, 07-25 — why Content MCP dwarfs One AEM MCP:** Content MCP carries EPA + Discovery service traffic; *"Going forward, the Content MCP Server will not be used in CoWorker. As a result, both traffic and customer attribution are expected to shift toward the One AEM MCP Server."* One AEM MCP gets an Experience League announcement + release-notes mention.
> - **Pedro's own definitional question got only an emoji:** *"active = using MCP, right ? not just enabled"* → `yes-` reaction, no written answer.
>
> **🔵 MIGRATION STATE**
> - **Cohort 1B enables 2026-08-04 (tomorrow).** Criteria explicitly exclude AEM: *"AEP + Apps stand alone customer (no AEM or Workfront)"*. Timeline was 7/28 draft → 7/29 opt-outs → 7/30 final list → **8/4 enable**. ⚠️ No message confirms the 7/30 final list was produced.
> - **Ian Boston, 07-31: *"CoWorker is not enabled for AEM customers yet (info from Raul Hudea)"***, and on evals: *"CoWorker executes evals, but they focus on skill selection more than results. Teams are running evals independendtly."* (answering Bertrand's 07-30 *"do we have evals (executed periodically)…?"*).
> - **EPA bug bash: wiki title says "Content Creation Update **Aug 4th 2026**"** (`3985075861`). Slipped from 07-30 by the per-IMS-org LaunchDarkly flag (`FT_AEMAGT-2299`) being global-only; Carsten's PR `aem-ai-agent-orchestrator#381` fixed it on stage 07-31. **Corey: *"who is participating in the bug bash?"* — unanswered.** Felix: *"a little bit surprising that our LD integration never worked… wondering how we tested on stage"*.
> - **EDA: bi-weekly bug-bash series agreed** (Marius Duta + Brian, 07-30), no dates in channel. EDA security review with Lars scheduled "when he comes back from PTO", no date. Threat-model owners assigned per skill (Florin Florescu ×2, Ioana Marcu + Nicu Melcioiu, Christian Schneider, Abhishek Garg, Abhishek Dwevedi, Akanksha Jain).
> - **Coworker extensibility (Ken Russell, 07-28):** admins can upload plugins + add marketplaces, on stage for all orgs, prod "later this week", **system/product admins only**; internal repos no longer listed in the Marketplace UI. **Blocker: *"customers can currently only add public marketplaces… customers would need to add 200+ Ethos IPs to their Enterprise GitHub to allow it which is a non-starter."***
> - **Manifest confusion is general.** Corey: *"the AEM manifest we aligned on is AEM AI Assistant"* / *"AEM AI Assistant is what **I believe** AEM aligned on"* (belief, not record). Felix Delval: *"There are two manifest to test currently: AEM AI Assistant (only AEM) [and] CX Coworker One Adobe Demo… There are still discussion pending from #p42-architecture that has not yet reached a conclusion."* Felix also: *"If we were to enable a customer that is not assigned an explicit manifest, would he see AEM skills? The answer to that is No."* Mohit Sharma hit `cxe-aia` overriding the Maruti manifest (UI-side bug, fix "by tom", prod release Tue).
> - **Bertrand tested Coworker himself 07-24 and liked it:** *"it's feels so 'natural' (frankly it wasn't in AO/AIA…). Great progress by all teams… the 'killer' demo I was waiting for is almost there."* Greg Klebus and Luca Pellerei (Sr Solutions Consultant) both posted strong unprompted praise; Luca: *"in AO1 i used to get 'No image found'… 80% of the time, while here it really pushes hard to achieve what i ask"*.
> - **Horia Galatanu, 07-25:** *"very strong adoption in just a few days (~15%), across all use cases. And 3 power users"* ⚠️ **he flagged it himself two messages earlier: *"not validated by our Data Science team"*.** Do not quote as validated.
> - **Rendering:** Apoorva — *"custom card renderer in Coworker for discovery skill is WIP, hopefully mid Aug"*. **Mihai Copae replied in the Manish Bansal thread and contradicts the premise Pedro was writing a guardrail for**: *"I'm not sure it is possible to have a a2ui component that fires an API call… Agent → UI → User Action → Agent → UI"*, wiki `3979219149` (Garage Week Cloud Manager component). **Pankaj Kumar Sangra never answered Pedro's end-goal question.** ✅ Also corrected: `C0BCKG35NFP` is **#cxue-coworker-**panel**-hybrid-collaborators** (not "rail"); `C08U50NRA01` was **renamed 07-29 by Ken Russell** from `#aep-agent-orchestrator-collaboration` to **`#coworker-eng-collaboration`**.
> - **Customer issues in flight:** Air India experimental-scope 403 (fixed 07-30 by Christian Meyer allowlisting the client ID); DIGICERT — **Claude's per-tool "Blocked" toggle does not reach the MCP server**, delete succeeded anyway (Jabran: *"client-side control and are never transmitted to the MCP server"*; only server-side OAuth scope enforces); Heineken wants an MCP onboarding call (*"who would be best placed to help?"* — unanswered by name); Keysight + Gov of Canada want the Localization Agent on AMS (roadmap late Q4/early Q1); Kaiser Permanente asking about HIPAA (**Klaasjan: *"Adobe will be working to make Coworker HIPAA Ready"*, no timeline**).
> - **Sony:** first successful UI-test run in their QA2 pipeline 07-29 (Ramon).
>
> **🔎 KNOWLEDGE (P6):** [[Say the Sentence That Obliges — the Hedge Transfers the Ask]] — ⚠️ **I first logged this sweep as "field validation at scale" for that rule. Withdrawn.** A holiday is not a hedge. The only on-axis item is the 07-24 audit he named and did not post before going off; n=1, already covered by the 07-22 instance. **Do not cite this sweep as evidence for that entry.** [[An Undefined Gate Is a Date Nobody Can Give]] (Alejandro's *"What should be the naming convention?"* is the gate, unwritten, with Bertrand's urgency on it). [[Lead the Slide With the Honest Read of Your Own Metric]] (Horia's unvalidated ~15%; the Eli Lilly cross-dashboard gap). [[feedback_ai_phrasing_workday_2026]] (Felix Delval's "more public visibility" ask is measurable in this record). [[feedback_proposal_vs_decision]] (Carsten calling the 07-28 thread "the decision"). **No new entry — corroboration.**

> ### 🔑 2026-08-04 — SKILLS GROOMING: THE NAMING CANVAS, THE AUDIT RE-RUN, AND THE PLUGIN DECISION THAT WAS ROUTED TO PM AND SETTLED WITHOUT ONE
>
> **📤 THE ARTIFACT: Slack canvas `F0BNF9LDKMW` — "AEM Skills Naming Convention - WIP", Pedro's, written by him across the session.** Sections: convention + application table (all rows marked `proposed`, not `validated` — corrected after the first draft over-claimed), Skill Meta Fields (`domain` / `when-to-use` / `when-NOT-to-use`), One Marketplace, Plugins. **Not posted yet.**
> **⏳ FIX-LIST STILL OPEN ON IT:** the audit number + report link (still absent, though the canvas says *"this is the part that moves the number"*); the invented examples `form-edit` / `forms-plan-ntb` and a "Bad" example that is a `description` compared against a `when-to-use`; the missing facts under Plugins (Forms version divergence, EPA monolith); `lifecycle` and entitlements (which together close Clint); One Marketplace should say **monorepo 1A decided by Ian Boston**, not "one marketplace"; a rename date for Alejandro; owner + date on the Tina note; both markdown tables have their separator row in position 2 so row 1 renders as the header; the title under-describes the scope. **`"based on the first skills token"` is wrong — the application is the SECOND segment.**
> **🔴 CAUGHT AND REMOVED: Pedro had written "(Claude Code search)" into the canvas.** Flagged against [[feedback_keep_claude_private]] — and the July Workday AI-phrasing round makes it costlier than usual, since the same readers are in that channel.
>
> **📊 AUDIT RE-RUN (`GitHub/adbe-skill-audit`, fetch + naming + overlap + STATUS, data was 07-14 / graded 07-21 → refreshed 2026-08-03).** 105 → **107 skills**. Whole catalogue: conform 1 → **7**, warn 18 → **15**, fail 86 → **85**. ⚠️ **Never publish the 79% — 61 of the 85 fails are excat**, EDS developer tooling referenced by no manifest, the same distortion as the 34.3% `when-to-use` figure ([[reference_aov2_marketplace_manifest]]).
> **🔑 THE HONEST NUMBER IS SMALLER AGAIN, BECAUSE OF A MECHANISM NOBODY HAD FACTORED IN.** Skills can carry `user-invocable: false` in their SKILL.md header — they vanish from the picker and only the plugin's orchestrator calls them. **10 of the 46 customer-facing skills are internal.** On the 36 genuinely user-visible: **conform 7 · warn 12 · fail 17.** → **"17 mal nommées sur 36 visibles" is the publishable figure.** Sergiu applied it from 07-31 (PR `#76`).
> **→ This also dissolves the underscore fight.** All 7 underscore-named fails are `user-invocable: false`. Ian Reasor proposed underscores for multi-word tokens in Bertrand's thread, Sergiu implemented it, and it only ever landed on skills the customer never sees. **The live question is not punctuation, it is whether the convention applies to internal skills at all.**
> **🔴 THE AUDIT'S VOCABULARY IS PEDRO'S OWN AND WAS NEVER RATIFIED** — `APPLICATIONS` in `scripts/audit_naming.py` = all/assets/cloudmanager/commerce/content/edge/forms/sites. **Bertrand approved `cloudservice` on 07-31 and the audit rejects it.** Apoorva contested `assets` in-thread. `commerce` and `edge` come from the audit, not from anyone in the group. Instance of [[Success Definitions Must Be Agreed Before Metrics Are Scaled]].
> **🔴 THE AUDIT IS BLIND TO BERTRAND'S OWN COMPLAINT** — `governance-agent-marketplace` is not in the fetch list, so Alejandro's and Gerald's skills (the ones Bertrand flagged 07-30) are invisible. Also absent: onboarding (Reasor), content-fragments, guides. **Adding them is a list edit in `fetch_skills.py` + a re-run; Pedro has not asked for it yet.**
> **🟢 TINA VALIDATED THE CONVENTION** (relayed by Pedro): *"ok avec le vôtre, on rajoutera peut-être quelque chose avant AEM-"*. ⚠️ **She said "quelque chose", not `dx-`** — the canvas first invented `dx-`, now says `XX-`. A prefix ahead of `aem-` would invalidate the rule as coded (motif #1 = "missing the aem- prefix", 76 skills).
> **Token decisions Pedro made:** `brandgovernance` over `governance`; `da`/`eds` dropped as "je m'en fiche". Evidence says `workflow`, `replication` and `onboarding` are **features, not applications** — Reasor's own plugin is `aem-onboarding-workflow` (workflow as feature) and he wrote in-thread he would reclassify to `aem-assets-onboard`.
>
> **🔴🔑 THE PLUGIN-GRANULARITY DECISION WAS EXPLICITLY ROUTED TO PM, TWICE, AND SETTLED BY AN ARCHITECT.** `#p42-architecture` thread `1784580015.006749`: Ian Reasor 07-21 *"Since this is customer-facing, perhaps this shouldn't be an engineering decision… Do we need to bring this decision to PM?"* → Carsten 07-22 *"yes, right — this should not be an engineering decision"* → **Corey tags Pedro directly** (*"@Pedro Ferreira ^"*) → Corey again **07-24 14:36** *"It would be great to get to a resolution on this quickly as we are starting to onboard customers and use in demos. @Pedro Ferreira / @Yanira Castaneda can you help?"* → 07-27 **Yanira redirects it to Ian Boston** → **07-28 Ian Boston decides**. ⚠️ **07-27/28 was PTO; only 07-22→24 was Pedro's window. Do NOT log this as an instance of [[Say the Sentence That Obliges — the Hedge Transfers the Ask]]** — it is confounded and n=1 inside a working window of two days.
> **🔑 CARSTEN'S PRINCIPLE, the load-bearing quote for anything Pedro writes here (07-21):** *"Plugins are a mechanism for distribution — with that these are customer facing. We have to find the right granularity that makes sense for our customers, and not reflect our org/team structures. Right now, I would rather go with coarse grained plugins."* → **Pedro's first canvas draft argued "one team per plugin" + "aligned with CODEOWNERS", i.e. the two criteria Carsten had ruled out, and its Minus ("more plugins, longer manifest") was inverted against its own proposal.** Corrected: proposal is now **one plugin per application**, matching the convergence Reasor named 07-22 (*"separate plugins per solution, but all served from a single monorepo"*) and Ankush (*"solutions would map perfectly to plugin boundaries"*). The Why block was deleted rather than rewritten — **the proposal currently ships with no rationale.**
> **DECISIONS IN THAT THREAD (Ian Boston 07-28, endorsed by Carsten + Reasor, wiki `3983883638` by Satya):** **1A = monorepo** for skills and plugins, his reasoning *"CoWorker will likely live and die on its ability to select the right skill"*. **2A = skill entitlements, "mandatory"** (`skill-entitlements.md`) — ⚠️ **this is half the answer to Clint's admin-scope question**, with Carsten's caveat that it only holds inside Coworker, not in Claude/ChatGPT. **3B** for Coworker context.
>
> **PLUGIN INVENTORY (read 2026-08-03).** `aem-aia-extensions` 12 plugins (9 practitioner / 3 system) 27 skills · `epa-experience-generation-extensions` **1 plugin `experience-generation` carrying 17 skills** · `aemforms-aia-extensions` 1 plugin 2 skills · onboarding (Reasor, unaudited) 2 plugins 12 skills. **No naming convention at all** — three shapes coexist, and `aem-cloudmanager-api` sits beside `aem-cloud-manager-ops` **in the same repo and the same CODEOWNERS file**.
> **🔴 THE CONSOLIDATION'S FIRST CONCRETE DEBT: Forms is duplicated and already diverging** — `adaptive-forms-authoring` is **v0.1.37** in the consolidated repo vs **v0.1.41** in its source repo, one week after Satya copied it (PRs `#71`/`#72`, 07-30). The source repo was never emptied. Same two skill *names* now exist in two marketplaces. ⚠️ Catalogue-level duplication verified; **manifest co-presence NOT verified**.
> **CODEOWNERS (PR `#65`, Carsten, merged 07-29, proposed by Satya 34 min earlier).** 12 lines, one `@Adobe-AEM-Foundation/aem-p42-*` team per plugin folder. **GitHub's own validator reports exactly one error — line 1, `aem-p42-forms` = "Unknown owner"** → **PRs on the Forms plugin have no automatic reviewer today.** ⚠️ Could not list team membership (token lacks `admin:org`), so an existing-but-empty team would look fine and behave the same. **EPA and Governance are not in CODEOWNERS at all.**
> **🔑 THE MAPPING QUESTION, SETTLED WITH DATA:** skill names can never carry the agent. **One agent spans several applications** (EPA = content 7 / edge 4 / sites 3); **one application spans several agents** (`aem-assets` = Discovery + Content Optimization). `aem-cloudmanager` is clean only by accident. **And `domain` does not rescue it** — Forms, the only team that filled it, wrote `aem-forms / form authoring (structure)`, i.e. an application, not an owner. **Of 12 plugins, 11 declare `author: "AEM Team"`; only Forms declares itself.** → new knowledge entry [[A Packaging Unit Is a Customer Taxonomy — Ownership Needs Its Own Record]].
>
> **🔴 PHILIPPE'S "ANY PLUGIN REMOVAL HITS EVERYONE" IS A RELAY DISTORTION — see `watches.md` for the full correction.** Gerald Prendi actually wrote *"a delete or an addition of an **MCP server**, even manual is **per ORG** and might have impacted us. **This would need to be confirmed.**"* Three deltas: MCP server ≠ plugin, per-ORG ≠ everyone, and it is an unconfirmed hypothesis (question 3 of 5 on **AEMAGT-2435**, Major, Jabran Asghar, **untouched since 07-30**). The real bug is that **Coworker does not discover the Brand Governance MCP transitively via One AEM MCP while Claude and ChatGPT do** — which contradicts what Ramon told Bertrand on 07-30. Instances of [[feedback_proposal_vs_decision]] + [[feedback_dont_conflate_pattern_with_object]].
>
> **🔴🔑 VISIBILITY LOSS, CONFIRMED BY READING: `#aia_coworker_convergence` is dead since 2026-07-28 19:36.** Two minutes earlier Yelena wrote *"lets use our other channel for the details on optin/out and other eng, product and PMM related items"*; at 19:41 the same evening **Pedro was removed from `#aep-coworker-core`**. → **Six days of cohort / opt-out / provisioning traffic have happened where he cannot see.** Last visible state is the 07-28 Cohort 1B plan (draft 7/28 → opt-outs 7/29 → final list 7/30 → **enable 8/4**), with **no message confirming the 7/30 final list**, and criteria that exclude AEM (*"AEP + Apps stand alone customer (no AEM or Workfront)"*). Most recent AEM statement: **Ian Boston 07-31, *"CoWorker is not enabled for AEM customers yet (info from Raul Hudea)"***. **Cheapest fix: ask to be re-added, or go direct to Yelena / Namita.** ⚠️ Fact, not motive.
> **COWORKER UI — NO DELIVERY SIGNAL.** Last dated statement is still Pedro's own 07-21 post (Josh's team, stable UI + panel, target EOM) and the GA canvas still carries it as a red gate. Josh Hailpern has posted nothing visible since 07-25. The only panel-channel message since 07-28 is **Gael Mouello 07-29** listing 4 AJO panel invocation points and asking whether they auto-invoke — unanswered, and it is Eugene's question in AJO clothing. **07-31 code-complete passed unconfirmed and unredated.**
>
> **🔎 KNOWLEDGE (P6):** 1 new entry — [[A Packaging Unit Is a Customer Taxonomy — Ownership Needs Its Own Record]] (ai-product). Cited live: [[Success Definitions Must Be Agreed Before Metrics Are Scaled]] (the unratified vocabulary), [[Lead the Slide With the Honest Read of Your Own Metric]] (79% vs 17-of-36), [[An Undefined Gate Is a Date Nobody Can Give]] (Alejandro's rename question, the Tina prefix, the repo rename), [[Govern a Consistency Layer Over Primitives You Don't Own]], [[feedback_keep_claude_private]], [[feedback_proposal_vs_decision]], [[feedback_dont_conflate_pattern_with_object]], [[feedback_edit_the_span_not_the_artifact]].
