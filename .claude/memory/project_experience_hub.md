---
name: AEM Experience Hub project context
description: EH-only after Phase 2 vault split (2026-05-03). Surface, contribution model, Sorin team, O2 personalization KRs. AAI work in sister file.
type: project
originSessionId: 298c09b0-7372-4e27-9660-87019bb7d26c
---

> **Phase 2 vault split landed 2026-05-03.** AAI content (agent reporting, AO 2.0 liaison, Loni+JM May 11 deck, three-tier reporting, Felix/Rubin/Varun threads, Apoorva punch-list, KR3/4/5/6) lives in `project_aem_agents_intelligence.md`. This file is EH surface, contribution model, Sorin team, O2 personalization KRs only.

> ## ▶️ 🔴🔑 2026-07-15 — AEP ASKED FOR EH'S REAL ESTATE, BY NAME. *"Where are all the placements in AEM that we can take over?"*
> Source: the Rachel + Namita rollout sync, 07-15 (full read AAI-side). ✅ Attribution clean — Pedro alone in the room.
> - **Rachel Hanessian showed a Miro board of the customer-facing transition** — *"the experience changes that we are expecting. **This is what Cole is driving with the UI team**"* — and it lands **on EH's surface**. The states: **today** = left-nav item + homepage entry + full screen + rail · **next** = a **banner** (*"CX Enterprise Coworker is coming soon. It's an evolution of AI assistant"*) **+ a Gainsight popup** (she asked *"do you guys use gainsite in AEM?"*; Pedro: *"we do, yeah"*) · **then** = the same banner with **"Try now"** → opens **full screen**, *"you won't open the rail because **we don't have the rail yet**"* · **eventually** = the Coworker rail.
> - **🔴🔑 THE ASK, VERBATIM:** *"we should work with you on like where, because I don't know, **do you have this type of banner in AEM, or where are all the placements in AEM that we can take over?**"* → **AEP is asking AEM which of its surfaces they may occupy, and EH is the surface with 14K weekly users and a 79% return rate.** **This is the most direct ask on Pedro's own product anyone has made in this migration, and it arrives as an open question rather than a fait accompli.** → **Answer it deliberately: EH's entry routing is the thing Pedro has spent two months arguing EH must own** ([[Selection and Cross-Surface Consistency Are a PM Mandate]]). **A banner + Gainsight popup placed by another team, on the EH front door, is exactly the silent replacement decision #2 exists to prevent.**
> - **⏳ Rachel owes the Miro/mural.** **Get it — it is the customer-facing message, already drawn, for a surface Pedro owns.** ⚠️ Naming wobble she caught herself: *"that should not say coworker chat… that should just say **coworker**."*
> - **🔴 Rachel is out ~07-16 → ~07-29; Pedro is out from 07-20.** If the placements conversation does not happen this week, **it happens without either of them.**

> ## ▶️ 🔑 2026-07-15 — THE RAIL IS NO LONGER MANDATED. THE EH ENTRY FORK IS AEM'S OWN CALL, AND AEP SAID SO.
> Source: the Coworker demo to the AEM agent team (07-15, Horia Galatanu + Manas Garg + Rachel Hanessian; full read AAI-side, `project_aem_agents_intelligence.md` 07-15 block). ⚠️ Room-mic transcript, three people on one label — see [[reference_transcript_glossary]] before quoting.
> - **🟢 Horia Galatanu (AEP, Sr Dir PM), verbatim:** *"there's been a slight change in philosophy where… **We don't want to necessarily mandate that, hey, it has to be a right [rail]**… We're asking the applications to kind of take the lead and figure out how it works for them. For [some] application, it makes more sense to have some sort of a **floating bar**… for others, the **right rail** still makes total sense… it becomes **a bit more of a product by product thing**… the goal is more around **interacting with the page and being able to take actions on that page** versus performing exactly what you would be doing in the full screen."* **Manas Garg confirmed:** *"from this point onwards, these are application concerns."*
> - **→ THE SORIN-vs-EUGENE FORK WAS NEVER AEP'S TO DECIDE.** Sorin leaned rail, Eugene leaned full-screen, both waiting on Josh. **The platform owner has now said the pattern is the application's choice, per surface.** Pedro's **destination-agnostic handoff-contract** position and the **EH-owns-the-entry-routing** thesis are backed by AEP, in front of Bertrand. Decisions #1 and #2 (keep the centre bar, repoint the handoff) are **AEM's to make and defend, not to wait for.** Clean corroboration of [[Selection and Cross-Surface Consistency Are a PM Mandate]] and of [[There Waiting Has Two Forms — Consistent Chat or (Often) Invisible]] — Horia independently reached the entry's exact claim (form follows the surface; floating bar here, rail there).
> - **🔴 THE COST, AND NOBODY IN THE ROOM NAMED IT.** *"You're holding the keys to your destiny"* also means **the EH chat surface is now AEM's build, on AEM's estimate.** If the entry pattern is an application concern, **EH inherits UI work that is in no plan and no headcount** — with Sorin at ~1 effective engineer plus two June hires. **Do not celebrate the autonomy without pricing it.**
> - **🔴 THE RAIL DATE SLIPPED, FROM THE ROLLOUT OWNER. Rachel Hanessian:** *"the **context awareness piece is there**. The rail is **still being kind of retrofitted**… a version to be tested… **in like 2 weeks**… **code complete would be end of month. I expect it to be a few more weeks after that till we get it polished and out.**"* → **07-31 is code-complete, not availability.** Testable ≈ 07-29, out ≈ **mid-to-late August**. **Everything EH-side planned against "the rail ships 07-31" needs re-dating.** Context awareness already exists — that half is not the blocker.
> - **📤 This sharpens the Silvia message already owed** (watches, due before 07-20): Eugene's condition is met (the harness sees and acts on the page), full-screen survives, **and now the rail-vs-full-screen choice is explicitly AEM's** → **unblock Eugene's sketch and let him and Silvia make the call.** That is their lane ([[user_ui_cx_gap]]), and it is now formally open.

> ## ▶️ 2026-07-03 — EH chat entry vs AIA decommission: Pedro's DECISIONS (URGENT, end-of-July deadline)
> The shell drops AIA 1.0 end of July → Coworker rail replaces it ("AIA 2.0"); the EH center bar currently opens AIA = loses its target. Full model + decisions in vault [[EH Chat Entry — AIA Decommission Impact and Decisions (2026-07-03)]]; Sorin agenda in the 1-1 questions file. **Pedro's calls (07-03):** (1) handoff barre→rail = investigate two-track (Sorin EH-side + Josh/Rodson platform-side 07-08); (2) **KEEP the center bar** — repoint its handoff, don't let the rail silently replace EH's owned entry; (3) **suggested prompts (Fu Chi feed): pause/remove NOW** — inform Fu Chi at the weekly; (4) fallback state for non-provisioned orgs = define with Sorin (most orgs have no rail on Aug 1 — no dead bar on a 14K-weekly front door); (5) prompt-search survival = Sorin check. Sorin pilots the Experience Home dev; candidate first workstream for the 2 new hires. Position: the two-entries transition = the selection/consistency lane made literal — EH must own the entry routing, not the platform.
> **🆕 07-03 (aft) — Ian Boston's CustomerDataReporting pattern names the EH team.** Deliverable 3 of his CustomerDataReporting-20260622 diagram = "Deploy App into Experience Shell with end user telemetry (**Experience Hub team**)"; the example report = Activation Reports = Sylvia's 06-24 DAM-metrics ask arriving from a second direction. Question 7 added to the Sorin 1-1 file: slot the Reports App into the contribution model (EH owns the surface slot, owning teams build the reports). Full diagram read AAI-side (`project_aem_agents_intelligence.md` 07-03 13:17 block).
> **📤 EMAIL SENT 2026-07-03** (Silvia + Sorin + Eugene, Bertrand @-mentioned "please chime in shall you see it differently"): the 3 calls + 5 Sorin bullets + Eugene one-entry sketch ask + Bertrand provisioning teaser ("full picture in a separate note" = the Day-After Map, delivery owed ~07-08). Pedro's edits vs draft: Silvia direct recipient (not relayed via Eugene), Bertrand chime-in slot, "I believe"/"I would like" hedges, Guliz added to the prompts-pause inform list (voice deltas banked in [[feedback_draft_in_pedros_voice]]). Watches set: Sorin reply + stage test before Wed; Guliz+Fu Chi inform; Bertrand note.
> **📥 EUGENE REPLIED 2026-07-07 15:49** (reply-all to Silvia + Sorin + Bertrand + Pedro; email, EN). **He contests Pedro's call #1 on UX grounds — "rail as the destination" is probably wrong, full-screen redirect is more likely.** His argument (design POV, [[feedback_co_author_dont_answer_over]] — Eugene co-authoring in his lane; [[user_ui_cx_gap]] = route the spatial UX detail to him): a rail *earns its place* only when the user keeps working on something visible **while** consulting the assistant — the value is spatial, you read the answer against on-screen content in real time. **EH is a dashboard** — cards, launch points, metrics, nothing gets manipulated while chatting "at least yet" → a rail adds nothing here *unless* Coworker acts on the dashboard directly (pull data into view, highlight cards, change what's on screen based on the conversation). Counter-cost he names: **redirecting to Coworker full-screen loses EH + AEM-app context, primarily navigation** — "there are pros of using the rail too" (he holds both sides, doesn't decide). **Actions:** ask Josh Wed alongside the pre-fill question; **holding the sketch until the destination is known**; will probably **update the PR** to show the new-bar interaction so we can see how it behaves; offered a call before Wed. **Read for Pedro:** (1) the Josh fork just gained a UX axis — not only "manifest repoint vs rail replace" but **rail vs full-screen, gated on whether Coworker can act on the EH dashboard**; the answer decides whether call #2 (keep+repoint the center bar) resolves to a live handoff or a launch-button-to-redirect. (2) Eugene's "full-screen loses EH/AEM context" is actually an **argument for Pedro's thesis** (selection+consistency lane, Ian NorthStar): it says EH owns context/navigation a naked redirect throws away → the fix is the **handoff contract carrying context** (session ref + prompt + nav context), not a bare redirect. Feeds today's Josh meeting directly + the EH prompt-bar → Coworker-rail handoff-contract question already on the 07-08 agenda. **📤 PEDRO REPLIED SENT 07-08** (EN, reply-all): validated Eugene's spatial read, crystallized the one Josh question ("can the Coworker rail read/act on the EH dashboard, or only redirect? — that picks rail vs full-screen"), held the destination-agnostic position (the bar must pass session + prompt + nav context, not open Coworker cold), yes on updating the PR, offered a call before the Josh meeting.
> **🔴🟢 RECONCILE 2026-07-08 (Coworker-surface working session, Josh present — AAI memory 07-08 block + [[EH Chat Entry — AIA Decommission Impact and Decisions (2026-07-03)]] resolutions):** (1) **AEM is deliberately NOT in the first Coworker cohort** (CDP/AJO/CJA first, AEM/Workfront deferred until the panel ports AEM's critical rail features) → the EH center bar does NOT lose its target Aug 1; the Aug-1 cliff is softened for EH's 14K users. (2) **Full-screen is KEPT** — it becomes Coworker at the same URL + 302 redirect → **overrides the "drop full-screen" line in Pedro's 07-08 email**; the center-bar full-screen path survives. (3) **Suggested-prompts pause (decision #3) needs reconcile** — Josh's side (Zeus) says keep + feed AEM content into the AO2 recommendation system now; decide pause-vs-keep before informing Fu Chi. (4) WebMCP rail-acts-on-surface confirmed → rail direction holds. Naming = "coworker chat"/panel; rail release 2026-07-31, decoupled from product readiness ("release ≠ migration").

> ## ▶️ 2026-07-08 — Sorin 1-1 (held; EH-side; screen-share-heavy, medium-fidelity — Sorin narrating the stage UI live). Notes in EH Status & Todo.
> Purpose = reconcile the 07-03 chat-entry email before Josh tonight + Sorin's flag investigation. Key outcomes:
> - **🟢 SORIN'S RAIL RECOMMENDATION (EH-side half of decision #1/#2 lands):** the switch mechanism = **overriding the coworker flag turns the right rail into the Coworker rail; "they will turn on AI Assistant v2 for ALL tenants"** (a global flag flip). For EH it's **transparent** — a prompt meant for the right rail opens in the right rail whether it's the old or Coworker one; **only the FULL-SCREEN (top-bar) prompt path needs a fix.** Sorin's call: **switch the prompt bar to open the RIGHT RAIL** (same pattern EH already ships for the site-trial widget + failed-pipelines button — click opens in the sidebar), NOT a full-screen redirect. Rationale: *"I don't really think we had a great experience where you write a prompt and go to a different page and wait."* → concretizes decision #2 (keep the bar, repoint the handoff = open the rail). ⚠️ **Divergence to surface at Josh: Sorin (EH eng) leans RAIL; Eugene (design) leaned FULL-SCREEN more likely.** Both agree it's the question for Josh tonight.
> - **🔴 Coworker full-screen may not be ready:** Sorin doesn't know the full-screen Coworker URL; on stage it "looks silly, missing the unified-shell top bar"; and **no rail→full-screen "continue" button** exists anymore (he couldn't find it). = concrete evidence for the Josh availability question. If full-screen isn't there, the rail is the only viable target anyway.
> - **🔁🔑 GEM STACK — re-surfaced (Pedro said "it's not in my reader", but it WAS documented since the March handover: State of Project "~300 orgs still on old gem stack, Dan's team owns it, route via Raul/Adi not Dan"). A known-but-forgotten item now colliding with the Coworker cutover:** **Gem Stack = the original AI Assistant that only knows PRODUCT KNOWLEDGE, no agents** — Dan's team's pre-agent/pre-orchestrator implementation. Some customers may still be on it via feature flags; the reason = **Managed Services** (product knowledge, no agents acting). Opens 4 questions that gate the comms/migration list (ask **Dan / the AI Assistant Team** + a second eng, name garbled "will/wool"): (1) how many customers use NO AI flavor, (2) how many need migrating to Coworker, (3) who's still on Gem Stack + why, (4) **how do no-agent (product-knowledge-only) customers work on Coworker — do they get any skills, or only product knowledge?** = a real hole in the Day-After Map: the base isn't just "provisioned vs not", there's a product-knowledge-only tier.
> - **🔴 Coworker's native UI alters the sites experience (finding):** Sorin drove Coworker's default UI, told it to edit a page — **it did it ITSELF (not via the EPA agent) and opened its own "workspace"** (the agent's canvas / artifact view, like Claude's — NOT Experience Workspace), with its own dashboards/files. Concern: *"I'm not sure the sites team truly understands how the Coworker UI alters their existing experience"* — it may conflict with the EPA custom page-preview handler the sites team supports. **Pedro action: screenshot + ping the sites team (Jill + others) on the align channel.**
> - **Suggested prompts:** disable via feature flag (confirmed doable — they're already flag-gated). Sorin opens stories to validate. Open sub-Q for Josh: does the prompt library survive in the Coworker context.
> - **AI Assistant nav item:** where should it route post-cutover (also lives in Cloud Manager UI + elsewhere)? → Coworker if enabled; question for Josh's team (Coworker UI). Sorin to note it.
> - **Date:** Sorin confirms Pedro's read — AEP has **3 UI branches merging into one**, planned fully merged 07-15 but critical bugs remain → they're now "freaking out" because 2000 TBYB + 300+ SKU customers are watching. Plan: **work to the worst case (end of July)**; little work on EH's side, "the worst thing we can do is nothing, and even then nothing crashes." Numbers Pedro stated in-room: **~2000 TBYB + 300-something SKU** (aligns with the 2,483/318 pending-Raul split).
> - **Renderers:** **🆕 Rebecca Yonezcu** (Sr Product Designer, NEW — Discovery + Content Optimization agent design; back from PTO, pinged Pedro, wants to move the renderer discussion forward). Sorin confirms EH stays involved. Mihai + Adrian's Garage-Week work = a POC only; heavy lifting sits with the teams owning each implementation. Action: Sorin re-pings the content-hub team + asks Mihai for a step-by-step wizard guide to share; Pedro opens align-channel threads (discovery + the sites/EPA renderer finding).
> - **Reconcile:** Sorin owes the reply to the 07-03 chat-entry email (Eugene+Silvia) — he investigated the flags, will send after this 1-1 (was the 07-06 watch). Sorin's Josh questions tonight: full-app vs sidebar, prompt-library survival, nav destination, automations survival (all → Josh). Pedro also to ask Bertrand the full-app-vs-sidebar implications. No new knowledge entry (execution + open questions; [[project_experience_hub]] selection/consistency lane = the frame, the rail-choice IS the entry-ownership call).

> ## ▶️ 2026-06-24 — Sorin 1-1: EH-side asks (contribution model in action)
> Full renderer/Coworker-migration content from this 1-1 is AAI-side (`project_aem_agents_intelligence.md` 2026-06-24 Sorin entry). EH-relevant slices:
> - **🔴 Sylvia's activation-report ask (ETA owed):** review + give an ETA on enabling the **DAM-metrics activation report navigation in Experience Hub behind a feature flag** (JIRA "DAM magic 21 days" / ~AEM-21 / 629; one ask via Slack, one via email — confirm they're the same). **🟢 Sorin's contribution-model play: it is NOT EH adding the nav — the owning (assets) team contributes + adds it themselves**, EH does code review + helps. Ping **Del / Holly / Babu** (Sylvia's pointers). = the EH contribution model working as designed (teams surface their work *through* EH, EH doesn't build it for them). Pedro agreed.
> - **Mihai / contribution-model dashboards:** Mihai "vibe-coding" dashboards; Sorin unsure they want full pages in front of EH (may already live in Experience Workspace / the assets workspace). Watch, don't duplicate.
> - **Central nav item** (minor): Sorin shared notes with Mihai — "doable, just a navigation item."
> - **Capacity:** Vale (assets renderer) is off; Sorin pulling in **Mihai (Copae)** for implementation-requirements depth.

## About Experience Hub

AEM Experience Hub is the unified home screen / landing page for AEM Cloud Service at experience.adobe.com. Launched August 2024. Previously named AEM Home and AEM Launchpad. Not a replacement for existing AEM UIs. An action-oriented entry point that surfaces the right tools per persona.

**Current PM:** User (took over from Shankari March 2026.)

**Org:** User → Bertrand (Senior Director PM) → Loni (VP PM for AEM)

**Obsidian vault root:** `/Users/pedrofer/ObsidianAdobeVault/020 Professional/Adobe/Projects/2026/Experience Hub/`

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

All paths relative to: `/Users/pedrofer/ObsidianAdobeVault/020 Professional/Adobe/Projects/2026/Experience Hub/AEM Experience Hub - Project Folder/`

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

**3. 🆕 Two new EH hires start beginning of June.** ✅ CONFIRMED started 2026-06-01 (Pedro, 2026-07-03) — the System Review "did they start?" flag is closed; onboarding plan still open. Resolves Bertrand May 5 *"2 personnes remplacées pour EH"* note. Profiles:
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
