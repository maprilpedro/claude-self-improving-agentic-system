---
name: aem-agents-intelligence-aai-project-context
description: "Full context on the AEM Agents Intelligence project — agent reporting platform, AO 2.0 liaison, Loni+JM May 11 deck, three-tier reporting, agent ownership, AAI stakeholders. Sister file to project_experience_hub.md."
metadata: 
  node_type: memory
  type: project
  originSessionId: 5f12dcf1-db3b-44ce-bf6c-50e0a17cb9e9
---

> **Two-project split — Phase 2 structurally complete (2026-05-13).** AAI vault folder at `2026/AEM Agents Intelligence/AAI - Project Folder/`. Companion `project_experience_hub.md` covers EH. Meeting Notes moved to neutral `2026/Meeting Notes/` (2026-05-13). AI-Assistant legacy folder retired. No legacy folders remain.

> ## ▶️ RESUME HERE — left off 2026-06-05
>
> ### 🟢 2026-06-05 — Friday arch session HELD (Ian + Felix + Pedro). Critical-vs-flexible list co-built; engine NOT decided; Pedro owns the wiki.
> The session the cockpit prepped happened. Pedro opened by naming the elephant (one harness vs many), built the critical-vs-flexible list live with Ian + Felix, left the engine open. **Pedro walked away owning the definition artifact** (closed with "I'll capture that in a wiki page"). Full outcome + locked/open items in the dated section under "Felix reports + report pipeline" → "2026-06-05 — Friday arch session HELD". Transcript: `Agent Owner Alignement/20260605 - Ian Felix Pedro.md` (file was misnamed 0505).
> **Wiki PUBLISHED 2026-06-05** — "One AEM, Many Harnesses: What Must Be Common, What Each Team Decides", Confluence `3913168459` (space `~pedrofer`), v2 (reformatted: fixed escaped-bold paste artifacts, removed dup H1, added link to Felix's Agent Skills & Harness guidance `3908069301` under the Skills item). Critical list + flexible list + parked harness open-question (owner = engineering, no mandate + resolving evidence). **Pedro posted to Ian + Felix** (Slack thread `C0B8J3Z6Z42`) thanking them, pointing to the page, inviting co-edit — Pedro = owner of the definition, in front of both principals. **INDEX page PUBLISHED + broadcast to leadership 2026-06-05** — "AEM Agents: Start Here — A Reading Map", Confluence `3913885986` (space `~pedrofer`). Novice-facing reading map, descriptive paragraphs, ordered narrative: (1) Ian's Agentic North Star (`3894002388`, ~boston blog) → Pedro's "From North Star to There Waiting" (`3901747358`); (2) One AEM def (`3913168459`); (3) AEM AI Mapping surface map (`3907904901`) + EW/Slicc/AO2 intakes; (4) the open harness debate (Felix RFC `3907905649` + #aem-agents thread); (5) Felix skills guidance (`3908069301`). **Pedro broadcast it: direct to Ian + Felix, then to `#aem-p42-leadership`** = the map landed in a LEADERSHIP channel → Pedro now visible as owner-of-the-map (the whole agent-surfaces conversation) at the P42 leadership level, not just to peers. Promotion-grade visibility, directly on the self-promotion gap.
> **Also done 2026-06-05:** the One AEM def page (`3913168459`) now carries a black/blue distinction (v4, storage format) — black = agreed in the session (traceable to transcript), blue = added afterwards (the Felix-guidance link + the open-question "what would resolve it" criteria); legend at top.
> **Remaining:** (a) decide when to open the One AEM def page wider; (b) integrate if Felix adds; (c) get Felix's link with his additions (he said he'd send one).
> Prep cockpit + drill (still valid as reference): `AAI - Project Folder/Friday Arch Session — Facilitation Sheet.md` + `Friday Arch Session — Drill.md`.
>
> ### 🟢 2026-06-05 (#2) — Silvia DM (3-layer governance model) + harness doc expanded + DRAFT Confluence page + EW-no-AEM-licence
> **Silvia DM → 3-layer governance correction (2026-06-05, before 16h meeting):** Silvia's DM reply corrected Claude's framing of "explicit skills" as user curation. The correct model = **3 nested layers, non-competing**: **(1) Governance** (AI admin / Center of Excellence sets the **allowed skill set** — what exists, which users/roles can access it, approval required before publication); **(2) Surface** (auto-loads context-appropriate skills based on persona/context); **(3) User** (curates their own list **within** the governance boundary). Distinct from Row 7 of the harness requirements (AEM's governance vis-à-vis the platform vendor). → **One AEM def page updated to v5** (Confluence `3913168459`): governance layer added as item 7 in blue (post-session addition), legend updated. **Harness requirements vault doc** (`AAI - Project Folder/What We Expect From a Harness — Draft v1.md`) updated with **rows 8-11**: (8) code execution in sandbox [AOv2-can't vs Codex-can gap from Ian's test]; (9) cost discipline (tools→APIs→MCPs, harness enables cheaper-rung preference); (10) **customer-side skill governance + entitlement** (Silvia's 3-layer model above); (11) identity + memory seeding (continuity across surfaces). **DRAFT Confluence page published** (`3913886537`, "What AEM Expects From a Harness (Draft)", emoji 📝, DRAFT status macro, bandeau "for review not final", links to One AEM + Felix guidance). **Reading map `3913885986` updated to v2**: harness requirements added as section 2 companion.
> **🔴 EW-no-AEM-licence bombshell (Bertrand, 16h EH-EW-Skills alignment meeting):** Bertrand revealed at the meeting: **EW does NOT require an AEM licence** → EW serves non-AEM customers. This **breaks "one entry, two depths" (C1) for the non-AEM segment**: EH→EW hub-and-spoke only works when user has AEM. Non-AEM EW users have no EH. C1 still valid for AEM customers; non-AEM EW users need EW as their own entry point (EW-side home). Not yet resolved. Pedro's read: "pas mal" with Guliz overall. **Transcript NOT YET INGESTED**: `Agent Owner Alignement/20260605 - ExpHub, WE, Skills design alignement .md`. Ingest next session. Full impact on EH model in EH project memory.
>
> ### 🟢 2026-06-04 (#3) — #aem-agents fragmentation thread evening (replies 17-24): Tanju's middle path, Ian convergence, Reasor friction-pushback, the consume-vs-fork resolution
> **Source:** thread `C09KKLW1N86` ts `1780439097.735939`, replies 17-24 (6/3 23:25 → 6/4 19:23). New since the 6/3-evening capture. **The fork went from 2 poles to 3, and a rough consensus is emerging — matters for Friday's session.**
> - **🆕 Tanju Erinmez = a 3rd pole: "middle path / start from a shared base" (reply 17, got a -thank-you react).** Thesis: whichever way teams go, each ends up taking AgentSDK + rebuilding the same missing pieces (state, sessions, the loop, dynamic config, marketplace contribution) — so the choice isn't freedom-vs-platform, it's **where you start the build.** Leans to **fork/clone AOv2 as a baseline** (own it, diverge where it doesn't fit, upstream the useful) for 2 reasons: (a) **quality** — vibe-coding a system that scales works only if the team knows what to look for; teams that don't → costly redesign; shared base "raises the floor without capping the ceiling"; (b) **Adobe-specifics** — IMS orgs, tenants, overrides, IMS authz = cross-cutting; AgentSDK gives none, AOv2 already does = headstart on the hardest part. Reframes independence as **portability, not avoidance** ("if teams want to move off later, what does that mean — persistence, switchover").
> - **🟢 Ian Boston converges on the middle path (reply 20): "The middle path is exactly what I have always proposed. Teams choose."** BUT his AOv2 knock: *"a contribution-only model, 1 production instance, secrets in vault, dependencies to duplicate… open source in name only… not Apache httpd."* (+ posted the contribution-analysis PDF, reply 21; updated gist with issues + SKILL.md PRs, reply 24.)
> - **🔴 Ian Reasor — first-hand friction PUSHBACK on Ian Boston (reply 22).** *"We're using AOv2 for onboarding, Discovery too. No need to fork. Biggest upside = no infra to run. I really don't agree with your assessment of the friction. Manifest with just our agent, set as default for our test org + co-innovation customer's. Changes to AO usually merged within a week. Using what's provided should be the DEFAULT unless a compelling reason."* Ian conceded (23): *"others were not so lucky."*
> - **🔑 THE RESOLUTION (Pedro's facilitation lever for Friday) — the Ian-vs-Reasor "friction" disagreement is NOT a contradiction; they're testing two different things:** Reasor **consumes the single hosted AOv2 instance** (Onboarding/Discovery) → works, no infra, weekly merges. Ian **tried to fork/run his own** → hard, AEP-controlled, "open source in name only." → **AOv2-as-hosted-service = viable today** (for teams whose needs it meets); **AOv2-as-forkable/portable-platform = not yet.** Both true. Dissolves the debate AND maps onto Pedro's One-AEM Q#3 (is the harness open enough to contribute to / portable). The emerging consensus (Ian + Tanju + Reasor): **shared base as default/option, teams free to diverge, no mandate** = Pedro's accidental-vs-essential + critical-vs-flexible. The room is already mid-way to Pedro's synthesis → his job Friday = NAME it, not create it.
> - **🆕 Build-vs-Operate (Felix↔Ian, on the RFC + thread) = a critical-vs-flexible item.** Ian "build is cheap" + Felix "operate is hard (ops readiness, scaling, operations) → harness = a platform function" = **two different layers, both true.** Real Q = does the operating cost justify forcing one engine? Answer = accidental-vs-essential, per surface. A shared operated harness = an **option** (Felix's value) without a **mandate** (Ian's red line); catch = the platform-harness must actually be operable → AOv2 isn't yet (consume-vs-fork).
> - **🆕 Protocol question resolved (Felix RFC comments + Carsten + the thread).** UI→harness session-config protocol = **manifest** (AOv2) for config + **WebSockets (+ A2A)** for transport (AOv2 spec, confirmed Felix). For Pedro's split: the **declaration contract = CRITICAL** (harness-independent — a non-AOv2 surface declares the same way, per Felix's own "skills are harness-independent"); the **manifest implementing it = FLEXIBLE** (a candidate, not THE answer). = the handshake between Pedro's declaration layer and Felix's harness (#1/#2). Felix linking Pedro's "One AEM" proposal from his RFC Non-Goals = the stack-not-overlap landed publicly.
> - **🟡 "Enforcement group" signal now PUBLIC (reply 18).** Ian posted it himself: *"work in a group of principals to enforce standards that will ban all other forms of deployment and force engineers into tightly controlled git repositories. AO is part of this trend."* + Ethos/AEM-non-compliance history (AEM-CS = why Adobe moved to K8S from DCOS). No longer private (was flagged private in the facilitation sheet) — but still not to brandish in the room.
> - **Pedro's posture: did NOT post in the evening (correct).** The thread moved to an Eng-level harness/AOv2-maturity debate (Tanju/Ian/Reasor) = the harness question Pedro already said isn't his to adjudicate. He's deputized + posted his frame (reply 10-15). Over-posting the night before would pre-empt his own Friday session. Brings the consume-vs-fork resolution + emerging consensus to the room instead.
>
> ### 🟢 2026-06-04 (#2) — Silvia + Ian + Eugene + Pedro call (consistency layer + memory layers — high-fidelity EN transcript)
> **Source:** `AEM Agents Intelligence/Agent Owner Alignement/20260604 - Ian Silvia Eugene Pedro.md`. The Thursday design call (Eugene back). Pedro's consistency-layer + check/drift mechanism reviewed live with the architecture sponsor + Adobe Design. **This is the call that de-risks Friday's arch session.**
> - **🟢 Pedro's check/drift mechanism — Ian endorsed on record.** Pedro posed: definition → implementation → **check for drift of each UI against the definition** (feedback loop; "we define the UI or an LLM creates the UI, then we check the created UI vs our definition"). Ian: *"each team should be doing that"* — team gets the spec, asks Claude *"does my UI match, fix discrepancies"* + **central oversight** + idea of *"driving Playwright across multiple solutions to record where there are discrepancies."* So the check = team self-check + central governance. = the strongest validation yet of the check half of Pedro's layer, from the sponsor.
> - **🟢 Where the definition lives + governance (the open square Eugene named).** Ian: **both markdown AND Figma** (markdown = easiest for AI to read; Figma/other AI-readable form for the visual), needs **central oversight**, must be **collaborative across CX** (all of Adobe, mostly CX). The hard problem Ian named = *"how do we talk to the various other UX teams across CX and gain alignment so we have consistency in the design before it goes near the implementation teams."* AO v1's failure mode: everyone could agree the chat UI was wrong, but changing it meant going into AO v1 UI code → roadmap → blocked by Summit → never done. Fix = move that conversation to a higher level (behavior/design first → unified spec → flows down to teams).
> - **🔴 Real constraint on Pedro's layer (Silvia, sharp).** AEM UX team owns AEM **visualizations**, but **depends on the common elements (the chat itself, the side rail) which come from the AO two UX team** — and that governance is *not clear*. In AO v1 they had too many dependencies (file upload = "a pain"), want to detach. **Silvia's real worry is NOT the UX collaboration (her team is well-connected, knows the UX people) — it's the implementation layer / the common technical library and who governs it.** → Pedro's consistency layer can own the AEM-side definition + the check, but the shared chat components are an AO-two-UX-team dependency he must navigate, not own outright.
> - **🟢 Ian's memory model = 3 levels (distinct axis from the skill-origin hierarchy in Pedro's harness doc — don't conflate).** (1) **Individual** memory/skills, follows the user, tied to IMS identity (Loni's core desire = creative memory for every IMS identity across all platforms, kept in Adobe → leaving is painful → retention moat); (2) **Organization** memory, IMS-org, Adobe-wide, **can't be split**; (3) **Solution** memory, per-surface (AEM), relative to the customer/env (brand, project, do's/don'ts). Ian: *"some of those collected together are not just memories, they're actually skills"* + EW's create/curate/share skill list is *"more memory than skills."* Ian is pushing the other principals to agree the **IMS identity + IMS-org memory cannot be split** and to get the IMS org to expose them as APIs (ties to the Saar VP memory-alignment track).
> - **🟢 Enterprise Context located (Eugene/Silvia question, Ian answered).** = an **independent object under the IMS org**, reference data ("this is our brand, that's where you find it"), isolated by IMS org but not part of it; the **skill** = *how do you find the brand + is it relevant in this context.* A shared memory many solutions can reference (Gen Studio + EW + Workfront solution-memories all reference the enterprise memory). **🆕 Silvia + Eugene meet Bertrand + Shankari (Friday, "tomorrow") on the EH + Workspace shared catalog** — how a skill declares it uses an Enterprise Context object (e.g. "this skill only creates pages for [brand] North America"); Silvia will share that presentation. ⚠️ Confirm this Friday Bertrand+Shankari shared-catalog meeting is separate from Pedro's Ian+Felix arch session.
> - **🔴 The harness decision is expected to land Friday.** Ian, verbatim: *"Conrad, four weeks ago, delegated the decision to me. I made a decision. It hasn't quite stuck yet. Pedro and me have got a conversation with some other folks tomorrow, and hopefully we'll get to a decision, a compromise, probably by end of day tomorrow."* → Friday's arch session is not just "name the open question" — Ian is treating it as the venue to reach a **compromise decision EOD Friday.** Pedro's parked-elephant facilitation plan should account for Ian wanting closure, not just framing.
> - **🟢 Harness framing — Pedro + Ian aligned, stated cleanly.** Pedro: AO v1 pushed teams to one orchestrator, operating poorly → the evolution gives teams **more freedom** (not dictating a harness technology), opens an architecture + concepts to **accept multiple harness technologies**, ensures **skills stay interoperable** if a team later switches (Claude/ChatGPT/AOv2), each team selects for itself. Ian confirmed + gave the history (P42 Nov force-decision failed; teams went their own way; no-credit-for-revenue grievance; one leader refuses to invest in AOv2). Ian's convergence path: let teams innovate now; **if in 6 months harnesses converge on the same need → then discuss merge/optimize to one service** — premature now.
> - **🟢 Ian's AOv2 contribution analysis restated live (matches the PDF from earlier today):** **1.1% non-AEP contributions, zero core modifications, "a really immature open source project that doesn't know how to accept contributions,"** suspects no one can run it without re-implementing infra (not an Apache HTTPD you download-configure-run, very opinionated toward AEP). Git shows **~3 customers** (Craig Mathis/Workfront on manifests + 2 others, 1 a contractor). *"It's not hard to implement a harness — I prompted Codex before this meeting, it's almost finished implementing one from scratch."*
> - **🟡 Field demand for AO two (Silvia's read):** Apoorva asking when to move; **EPA fails on AO v1 routing a lot → value delivered very low → Corey pivoting to 3rd-party (ChatGPT/Copilot)** to deliver value without the limitation; Discovery needs AO two; **Assets side (Mike — Pedro-confirmed): all AO v1 agents have H2 roadmap items to move to AO two.** Slicc + EW chose different (non-AOv2) harnesses because AOv2 isn't at their functionality level; EW (Martin + Markus) doesn't want to stay on Cloudflare (technical limits + don't want to self-administer infra), AOv2 on the table "when mature."
> - **🟢 "There waiting" + user-curation = two coexisting layers, confirmed with Silvia.** Pedro: skills are **pre-loaded into the harness via the surface/UI** — the customer doesn't select. Silvia agreed + extended: by context (you're in Workspace, you're this user-type → these skills) **plus** task-based suggestion **plus** the option to pull skills from outside your context. = Pedro's there-waiting base + EW's further customization stack (matches Ian's morning two-layer memory framing). No contradiction.
> - **Next week:** Silvia + Eugene share skills-catalog + skill-usage experience ideas + an "experience lab" measure-the-experience concept for Workspace; Eugene shares UI-in-AO-two learnings (how much UI freedom vs how much depends on the AO-two team) with Pedro + Ian. Silvia booking time.
>
> ### 🟢 2026-06-04 — Bertrand 1:1 (transcript ingested, Otter low-fidelity, Pedro-verified corrections applied)
> **Source:** `Meeting Notes/Bertrand 1 1/20260604 - Bertrand Pedro 1 1.md` (~25 min, very garbled Otter FR — Pedro reviewed + confirmed corrections before banking). Held 2026-06-04, before Friday's arch session (exact time not captured).
> - **🟢 Harness / skill-selection debate — Bertrand leans LLM-routing, not bloqué.** Pedro relayed Ian's two points: (1) hundreds of skills → how to select per user-context (Felix M's per-UI preselection = the good answer); (2) one single harness won't scale (too many skills, harness won't know which to pick). Bertrand's instinct: *"l'impression qu'on ne fait pas confiance au LLM dessous… il va comprendre que la question est AEM donc il va prendre les skills AEM"* + *"le 'beaucoup' pour moi c'est arbitraire… le principe du harnais c'est que le LLM sera capable de déterminer."* Pedro: Ian's worry = it becomes routing again (the AO-open routing problem). Bertrand closed: **"ça se teste, ça se valide. Je ne saurais pas dire s'il a raison — on va regarder comment ça avance avec les équipes."** = open, empirical, not blocking. Bertrand also floated the **prompt library** as a partial mechanism (gives example prompts + the context/attachments that make a prompt work).
> - **🟢 Pedro showed the consistency layer + his harness doc → Bertrand "oui, tu l'as montré"** (= acknowledged having seen it before, NOT an endorsement/validation — the "tu l'as montré" at 8:47 refers to work Pedro had shown earlier, and precedes Pedro's fuller 9:04 elaboration; don't read it as Bertrand validating the mechanism). Pedro framed: many harnesses → many UIs; Felix's model = many UIs on one harness; **above that = a consistency layer (graphic definition, Adobe tone, branding, Adobe→customer) Pedro owns with Silvia + Eugene under Guliz, sitting above AI Assistant so it's coherent across surfaces.** Pedro also wants an **AEP stakeholder map** (define mutual points of contact — "a l'air compliqué chez eux"). **CORRECTION (Pedro-confirmed):** the **3-level skill-origin hierarchy** (Adobe-product skills / customer-adds-for-its-users / user-adds-for-self à la EW + "ça devient une scale", marketplace-recoupement-with-AOv2 question) = **content of Pedro's own "what we expect from a harness" doc**, NOT a Bertrand proposal (Otter mis-split the speaker). Pedro: *"je te le partage quand tu auras fini de parler au CXO."*
> - **🟡 Bertrand's two levels of "mutualisation":** (1) at minimum, **AEM-internal** something we can share/reuse — even if not AOv2 — so we don't rebuild the same thing 50×; (2) if it aligns with Adobe CXO, even better. He likes AOv2 in principle (*"j'ai bien aimé AOv2 au début, c'est pas mal"*) but *"ils sont tellement pas clairs entre eux sur ce qu'ils veulent faire que c'est pas hyper rassurant."*
> - **🟡 Coworker / AOv2 timeline — still no date.** Monday Manas call gave no date; Pedro re-pinged, no reply, will re-push (Yanira doing same). **CORRECTION (Pedro-confirmed):** **Raj Patel is NOT a confirmed contact** — Bertrand contacted **Rachel** (sales-enablement contact from last year) for the latest CX Coworker deck; Rachel routed him to **Raj (Patel/Battle — surname garbled), Sr Director PM** who **"m'a gentiment pas répondu"** (politely didn't reply). Pedro: several Patels exist, Manas had pointed him at one. So the coworker-deck path is stuck. Bertrand also heard (garbled, low-confidence) that *"le concept de [AI Assistant?] pourrait carrément dégager dans coworker"* — unverified, consistent with Manas' "AI Assistant fate = open."
> - **🟡 EMA + Slicc — Bertrand recommends Pedro test both for a 360 view.** EMA = a quasi-harness; **Gabriel "complètement sous le volet"** — the published 138-slide roadmap doesn't include EMA at all (Gabriel frustrated, got the generic mailout). **CORRECTION (Pedro-confirmed):** Bertrand tested **Slicc** (git clone + make, runs local; now carries the **"audience of one"** demo = site migration decomposed into steps, each step its own skill to reverse-engineer the site design) → **results "pourris"** even on Claude-built sites. Not "intéressant" — poor quality, but worth testing.
> - **🆕 SEMrush is now a real, shipped data integration in EMA** — as a trend-event-detection data source ("vraiment mis en place"). Org-positioning game between EMA and SEMrush (two different businesses) — Bertrand watching.
> - **🆕 Sergei AOv2 cross-agent demo (~2 weeks ago, Friday-PM demo slot)** — RT-CDP agent detects 5000 customers about to cancel Photoshop (customer data — transcript says "Bicom", possibly a garbled customer name) → event emitted → a campaign agent (transcript "hgeo", **inferred AJO** — not stated) auto-builds a targeted campaign with tailored content. **Stops there.** Bertrand: *"dommage si on pouvait continuer avec les agents AEM"* = explicit cross-agent plug-in opening for Pedro's AEM agents. (Watch the Friday-PM demo channel — Bertrand attends remotely, recommends Pedro do too.)
> - **🆕 Next-week presentation = the Bucharest workshop keynote — Pedro takes over Peter Parker's slot (Pedro-confirmed).** Week of June 9. 56 people, mixed knowledge levels (matches the Bucharest audience already in memory — this IS Bucharest, not a separate presentation). Pedro's plan: quick AO V1 history + status, the routing/quality problems (a few graphs), then the direction + remaining challenges (modernization). Pedro shares draft to **Bertrand + Yanira** ("Yann" = Yanira, Pedro-confirmed — NOT Ian). **Bertrand leaves Thursday after 12h that week (it's his birthday)** → get the draft to him before then. (Distinct from the Flywheel session below, which Pedro also runs — Christian Meyer / ML part.)
> - **🆕 Bertrand strategic-posture signal (workshop):** least comfortable with the *"3 milliards en 3 ans"* objective — *"je ne pense pas que notre objectif doit être un objectif financier… il y a un objectif financier qui vient avec, mais."* Useful read on how Bertrand frames strategy upward (Loni was at the workshop).
> - **Reports asks from Bertrand:** (a) **Aubin** — Bertrand saw it in a meeting last week, didn't know it existed; asks Pedro to check if it's **redundant** with Pedro's reports / should merge / is reusable for other view types. (Aubin = a thing/tool, not confirmed person.) (b) **MCP live report** — Bertrand unclear whether a live MCP-activity report exists ("activité MCP depuis les apps, via agent orchestrator"); Pedro to send a few words on Slack. Pedro has Governance-Agent MCP reporting + wants to sit with **Tanju + Mark Pfaff** so Tanju offers the same for his MCP. (c) **Corey has an open request "un truc pour Loni"** (reports). (d) **Rubin** — Pedro torn: Rubin's interactive part is good but doesn't replace the reports, and Rubin needs the AEP platform (AOv2) for data — *"si on ne prend pas AOv2, je n'aurai pas les données à l'intérieur."* Pedro could sit with **Angela** to push report data into Rubin.
> - **🆕 Explorer → TBYB classification check (Bertrand ask, route via Raoul):** are all formerly-Explorer customers fully migrated to Try-Before-You-Buy in the classification? Pedro to check Raoul's latest list.
>
> ### 🟢 2026-06-03 — AEM AI Mapping surface map LAUNCHED (Confluence) + EW Slack deep-read + Felix M's single-harness North Star on record
> **Surface map built, owner-fillable (a position move).** Created Confluence parent **AEM AI Mapping** (`3907904901`, space `~pedrofer`) + 3 intake child pages: **Experience Workspace** (`3907904872`), **Slicc** (`3907904952`), **AO 2.0 / AIA** (`3907904956`). Each = neutral intake (surface / capabilities + **maturity** [Concept→In dev→Alpha→Beta→GA — Martin's "production-ready" ask] / skills & UI / ownership / where it lands on the 6 architecture divergences). Owners fill their own row = **consolidation-into-Pedro's-platform** (Varun "voluntary consolidation = legitimacy" pattern) + Pedro owns the canonical definition. **Martin Buergi + Markus Haack enthusiastic** about the EW intake. Personal live-capture HTML versions (with Pedro's private playbook — goal / opening / signal / must-ask) live in `AAI - Project Folder/*Surface Intake*.html` (3 files). **Strip rule:** Confluence pages carry NO Pedro strategy (no "get access" / "signal to give" / "my lane"); the HTML keeps it. Bertrand heads-up drafted (FR — surface map sits under his public "thousand flowers garden" concern, feeds the JM workshop), Pedro to paste. Full reference: [[reference_aem_ai_mapping]].
> **EW Slack deep-read (sourced, #aem-agents + #experience-workspace, 1-2 Jun):** Markus Haack — EW = **Cloudflare Worker agent loop** (DA-focused; NOT Slicc, NOT AOv2). **Markus believes AOv2 is "discontinued" = a misread** (reality = minimal-invest, not dead) → **the opening**: Markus WANTS AOv2 (personal skills + schedules EW can't do today), repeatedly asks AEM's AOv2 plans (*"the sooner we decide the better"*) → Pedro corrects the misread + brokers via Manas = access earned. Correction line drafted (no AOv2 date). **Natalia Venditto** = EW skills owner (git-repo skill import = *"not today, exploring"*) AND Felix M's Mithril-2.0 partner — **surname confirmed** (was TBD). EW = **end-user-authored skills** (the differentiator), Alpha ~1wk, **56 users / 236 sessions** (Buergi 29 May). **Satya Deep Maheshwari** asking for an **EW↔AOv2 interop analysis** = concrete next-step Pedro can offer.
> **Felix Meschberger — his 2 North Star comments banked (public position).** (1) North Star = **ONE single global harness** (RFC "Agents and Tools", `github.com/Adobe-AEM-Sites/aem-sites-architecture`); adds **system prompt must be registered** (alongside skills/tools) + **"bring your own skill" → a marketplace, `exchange.adobe.com`**. (2) **Standardized chatbox UI as a micro frontend**, per-session config (system prompt + tools) = his answer to skill-to-session; end-state = many UI *instances* / one UI *implementation* / **one harness service** (API POST+SSE). = strongest in-house advocate for BUILD + SINGLE-harness (both forks). **Play (arch-alignment session):** enroll him as **co-author** (his micro-frontend = the build-side reference for the consistency layer), hold the frame neutral on single-vs-distributed, flag `exchange.adobe.com`-vs-git-declaration as an open governance question. Full capture in AAI Status & Todo "Felix Meschberger — his 2 latest comments" section. **`exchange.adobe.com` = 2nd data point for the skill-provenance/trust lane** (after the Ian skillshare-vs-skills.sh thread, 2 Jun) → lane firming, watch for promote. [[feedback_co_author_dont_answer_over]] still applies with Felix.
> **Slicc spelling = canonical `Slicc`** (Sliccy = brand, sliccy.com; **Karl Pauls** + Trilove team; **Horia Galatanu** = AOv2 platform PM). Normalized Slick/Slicky → Slicc across 9 derived vault notes; raw Otter transcripts (`20260427`, `20260429`) left as-is (source integrity — Pedro can override). Rosetta still unverified.
>
> ### 🟢 2026-06-03 (#2) — Felix M working session: single-harness proposal sharpened + he opened the door to Ian
> Pedro working session w/ **Felix Meschberger + Martin Buergi + Markus Haack + Andrei (Tuicu, likely)** (a 5th attendee unidentified — skipped per Pedro). Felix's proposal, now concrete: **(1)** one harness, **one team** administers it; **(2)** many UIs all run on that one harness; **(3)** each UI **declares its own skill list** per session → keeps skills-per-session small (the context-budget problem everyone has); **(4)** asks if per-session skill-config is **on AOv2's roadmap** + whether AOv2 is an **open-source model AEM can contribute code to**; **(5)** Felix is **open to discuss with Ian** → unblocks the arch-alignment session Pedro owns.
> **Evaluation (don't pick a side, own the frame).** Part 1 (per-UI skill list) = **CONVERGENCE** — same structure as Ian Reasor's "per-UI skill sets," answers Ian Boston's context-budget worry ("1000 skills, nothing left"), and = the engineering form of Pedro's own published "there waiting." Felix + both Ians + Pedro already agree → amplify it + enroll Felix as **co-author** ([[feedback_co_author_dont_answer_over]]). Part 2 (one engine / one team) = the **genuine fork, already contradicted by facts** (EW built its own Cloudflare harness, not AOv2; Slicc a third) → an **engineering cost/ownership question, NOT product-consistency.** Pedro's layer (definition + surface map + check) is invariant to it; Pedro must NOT adjudicate (that's where he loses Ian or alienates Felix). Part 3 (AOv2 roadmap + open-source) = **already the Apr-29 agreed direction** (internal-open-source, Conrad "we can send you PRs") → route to **Manas / Raj Patel**, drop both questions onto the AO 2.0/AIA intake (`3907904956`, rows skill-to-session + marketplace-vs-git already exist). **Sharpest line:** the harness count — one or many — is *below* Pedro's layer; either way AEM still needs one definition, one surface map, one check, and not being invested in any engine is exactly what lets Pedro hold the room while the engine question stays open.
> **Page edits (3908567486).** 4 paste-ready blocks drafted, **Pedro applies** (his by-line): (A) per-UI-skill-list as the "there waiting" mechanism + context-budget; (B) shared-engine as a 2nd build-side path — **purely additive, Ian's credit untouched** (Pedro's explicit constraint, [[feedback_additive_not_corrective]]); (C) harness-count named as a separate open axis, layer invariant, **title unchanged**; (D) 3rd group-question routing AOv2-roadmap + open-source to the AO team. "Vanessa" skipped. **PUBLISHED to live page v3 2026-06-03** (`3908567486`) after a position-vs-Ian de-risk pass: the first-draft edits had drifted toward Felix/single (line 51 softened "single fails," line 55 reopened the count, line 57 predicted "most converges") — reworked so the post leans distributed (Ian-aligned) + credits Ian's check as durable core + presents single-engine as *reopened not won* ("I am not taking that trade") + accidental-vs-essential as a *test not a verdict* + line-18 "fails" → "has long looked like it fails." Net: Pedro sits ABOVE both forks (build-vs-check + one-vs-many), no switch-of-camps read. **Arch-alignment session = Friday** (Felix confirmed he can do Friday w/ Ian; pending Ian's yes). Ian + Felix DMs drafted (propose/lock Friday + live post link).
>
> ### 🟡 2026-06-03 (#3) — EW ready to move to AOv2 "when ready" → the accidental-vs-essential reframe for harness count
> **Signal (conditional, NOT a decision — [[feedback_proposal_vs_decision]]):** Markus Haack + Martin Buergi told Pedro their **current EW (Cloudflare) implementation does NOT solve all their problems**, and they're **ready to move to AOv2 as soon as it's ready.** Corroborates the earlier "prefer reuse over build, would take AOv2 for EW (personal skills + schedules)" — now an explicit move-intent from both leads. **⚠️ Conditional:** AOv2 = minimal-invest, migration plan "secondary" (Trent), no date (Manas dodges async timeline) → "when ready" may be far. Intent ≠ convergence; don't deck it as "EW migrating to AOv2." Loni's "can't be at the mercy of someone else" applies.
> **Correction to prior framing:** EW's Cloudflare was treated as a runtime *choice* ("Cloudflare because DA is Cloudflare") — this signal reframes it as a **stopgap** (built because AOv2 wasn't ready / lacked skills+schedules), not a permanent runtime divergence. (Pedro flagged Claude's own prior example used the same wrong assumption — corrected.)
> **The durable analytical tool this unlocks — accidental vs essential N.** The harness question is NOT 1-vs-N; it's **how much of today's N is accidental** (own engine only because AOv2 wasn't ready → wants to converge: **EW = accidental**) **vs essential** (genuine architectural requirement → stays separate: **Slicc = browser-resident, client-side, zero-server = likely essential**). This is the live test of Pedro's owned criterion ("no new harness without a distinct requirement") — for each surface ask: real requirement, or just "AOv2 not ready"? Modernization / Forms / Mithril = untested, don't generalize from EW. **Result Pedro can hold:** most converges (Felix's win) WITH an essential residue that stays separate (Ian's win) → Pedro owns the **accidental/essential distinction**, stays above the fork. **Political guard:** this data strengthens Felix / dents Ian's "divergence can't be corrected" — do NOT weaponize it against the sponsor; present as accidental-vs-essential (honors both).
>
> ### 🟢 2026-06-03 (#4) — Ian publicly deputized Pedro as consistency owner (#aem-agents fragmentation thread) + Pedro posted the neutral frame + Felix offered to consolidate
> **The thread (`C09KKLW1N86`, ts `1780439097.735939`, June 3).** Ian Reasor raised the fragmentation worry (teams building own harnesses → disjointed customer experience). **Ian Boston's reply = a public deputization of Pedro (promotion-grade visibility):** *"You should not be concerned… it is being explicitly addressed by design teams… **Pedro Ferreira, Silvia Mulet Ferre, Eugene Bannykh are all working on this aspect to provide guidance.** Others, please engage with that work rather than against it."* + Ian planted his own flag: *"**One harness does not fit all, at least not yet, and to commit to one would be foolish**"* (last committed framework obsolete in <6mo). Apoorva seconded (route-to-Claude risk; AEM **Assets** most impacted, needed in Sites + AEP apps = new cross-app scope). Bertrand engaged in-thread asking *"list what we expect from a harness — would EW chat UI qualify?"* (= the definitional question = Pedro's lane).
> **Felix escalated publicly:** *"building a harness adds no value"* + *"mid/long-term move ALL skills/MCPs/tools to hosted AOv2"* + posted his own RFC **"Single AEM Agent Harness"** (`3907905649`) and a skills-migration guidance page (`3908069301`, "temporary harness = AOv2"). So Felix has a **public flag pro-AOv2-single** now, not just "making the case." Both poles (Ian-distributed / Felix-single) planted in the same thread, same day = the fork is public.
> **Pedro's move (posted ~12:34-12:38):** public reply that (a) builds on Ian's hand-off ("Thanks Ian, agree"), (b) accepts the consistency-owner role, (c) plants the **neutral above-the-fork frame** (definition + surface map + check, invariant to harness count), (d) points to AEM AI Mapping + the One AEM post, (e) answers Apoorva + Bertrand, (f) ends with a call-to-action (own a surface → fill your intake). **Critically: NO meeting announced** (Pedro's catch — announcing an unconfirmed Friday session = hostage to Ian no-showing / Felix souring). The public neutral frame **recontextualizes the earlier private DM** (which had carried the EW-converge point + leaned single) → in public Pedro = neutral broker, not Felix's water-carrier. *"harness count is an engineering call and I am not trying to pick it."*
> **Felix offered to drop his page** for Pedro's (*"too much overlap, I am going to drop mine 😉"*) = **2nd voluntary-consolidation legitimacy signal after Varun.** Pedro's correct response (drafted) = **DON'T accept the drop** — they're different layers (Felix = the harness/engine, single proposal, backend; Pedro = the consistency layer above, harness-agnostic). Keep both, stack not overlap, bring both to Friday. Absorbing Felix's single-harness doc into Pedro's neutral doc would (a) cost Pedro's neutrality, (b) erase Felix's pole, (c) breed resentment ([[feedback_co_author_dont_answer_over]]). Titles "Single AEM Agent Harness" vs "One AEM, Many Harnesses" side-by-side = the open fork made honest, don't paper over.
> **Interpersonal note (Pedro's pattern):** Pedro read Ian's DM silence as a snub ("il fait le mort") hours after Ian publicly amplified him — recurring silence-as-threat misread. Counsel held: don't chase the DM; engage in the channel where Ian is active (the thread); Friday isn't hostage to Ian (can run w/ Felix + Silvia + Eugene). [[feedback_position_over_merit]].
> **Ian CONFIRMED Friday (DM, conditional).** Key intel from his DM: (1) **@ghita** (Mystique/Mysticcat, coal-face) dumped Crew.AI, now Claude Code + Claude SDK, *"building harnesses is trivial,"* Adobe doing another orchestrator pointless, *"AOv2 is the 3rd attempt and already falling behind"*; trying to persuade Felix that committing to AOv2 won't work. **@ashishc** same view, less experience. (2) **CloudFlare (EW's choice) is NOT viable** + deploying a harness at scale is non-trivial (EMA) → there must be **a pattern that works and stays current with Anthropic and Codex.** (3) **His condition:** *"Happy to have a genuinely collaborative session, but not if it turns into one where I am being lectured to by Felix as happened Monday… I do have time on Friday."* (4) **His mandate line (adopt verbatim):** *"Ultimately it doesn't matter what I think. No team in AEM is going to be told what they must do… Guidance on what is critical and flexibility on what is not is really what matters."* New names to add to Stakeholder Map (confirm): **Ghita** (Mystique/Mysticcat), **Ashish C** (@ashishc).
> **Friday session — plan banked.** Subject = **"AEM agent harnesses and one coherent experience — working session"** (names the harness so Felix isn't boxed; coherence reassures Ian; no single/distributed, no critical/flexible in the title). Invite body: names the harness question as the real one but **not voted on here** (engineering's call), nothing on trial, leave with the critical-vs-flexible list + open question; links both One AEM post + Felix's RFC as **inputs not conclusions**; closes *"Keeping it small, just the few of us closest to this. Come with what you think has to be common, not a case to win. I will keep us to the list and the open question."* Optional priming prompt (no pre-decide): *"think of one thing that has to be common no matter the harness, and one you'd keep each team's call."*
> **Facilitation design (Pedro's cockpit, NOT shared).** Open by **NAMING the elephant** (one shared harness vs many) — scoping ≠ avoiding; name it, say why it's not settled here (engineering's call + 4 people on a Friday won't close it), then run **critical-vs-flexible** + name the open question with owner + resolving evidence. **Do NOT pre-share the filled columns** (pre-placing "engine = flexible" boxes Felix in writing; makes Pedro author-of-answer not facilitator; invites people armed). Build the columns **empty, live, with the room** = shared ownership. Pre-seeded columns + pull-back kit (redirect / cut-monologue / **protect-Ian-by-giving-him-the-floor** / park) + watch-signals (engine-as-the-answer / monologue / relitigate-Monday / **Ian goes quiet**) + the Felix-RFC anti-collision points saved to vault: `AAI - Project Folder/Friday Arch Session — Facilitation Sheet.md`. Exit (max 3): critical list agreed / flexible named / harness open-question written w/ owner + evidence.
> **Felix RFC reviewed (`3907905649`, now filled-in) — 4 reads for Friday.** (1) **His Non-Goal explicitly scopes UI OUT** (*"front-end user interfaces are not part of this proposal… many chat boxes connect to the same harness"*) → his RFC (backend harness) and Pedro's post (experience layer) **do NOT overlap — his own doc proves it.** Lead with this to settle the "drop mine." (2) His **Known Challenges #1 (per-session skill subset, context overload) + #2 (chat box informs harness which skills)** = the convergence point + **where Pedro's layer plugs in** (the surface definition supplies the "which skills this surface needs" metadata) → offer the handshake. (3) **Collision risk:** the RFC is structured as **Decisions to commit to AOv2** (Phase 1 "Decide on AOv2", Decision #3, Phase 3 AEM-wide AOv2 + AEM fork) = Ian's "commit to one = foolish / no team mandated" tripwire → don't let Friday become ratify-Felix's-decisions; hold as inputs to the criterion. (4) **Lever (his own words):** the RFC concedes *"AOv2 mainline will be behind… we fork"* = same as Ghita/Ian "AOv2 falling behind" → it's a **bet on an immature base, not a settled fact** → keep open without dismissing Felix. Single signed paragraph drafted for the bottom of his RFC (NOT inline comments — Pedro's preference): affirm direction → Non-Goal means stack-not-overlap → offer #1/#2 declaration handshake → mark the AOv2 step "proposed not decided" (via his own fork-lags line) → close on Friday. Additive, neutral on engine, [[feedback_additive_not_corrective]]. **Attribution catch (Pedro's):** the RFC intro *"result of a discussion with Pedro…"* on a doc headlined "Decide on AOv2" tacitly enlists Pedro as endorsing the commit. Fix = **mark the step "proposed not decided," NOT de-attribute** (being in a discussion ≠ endorsing; removing the name looks petty + forfeits real contributor visibility). Pedro's protection = his visible distinct position in 3 places (neutral blog + neutral public thread + this signed paragraph) > one intro courtesy line. Final paragraph saved in the facilitation sheet.
> **Felix's 2nd page reviewed (`3908069301`, "Agent Skills and Harness guidance").** Tactical companion to the RFC — engineering how-to for converting agents → `SKILL.md` (Anthropic Agent Skills spec); capability-spec-first; AO runtime overlay (api_request / MCP / execute_code+PTC); "Temporary Harness" section = use the AOv2 repo for short-term + local dev, contribute back (softer than the RFC — AOv2 = "candidate," no org-commit pressure here). **Not Pedro's lane** (skill-authoring mechanics, backend) → no collision. **THE KEY LEVER for Friday (Felix's own words):** *"Skills are harness-independent — the same SKILL.md works in a temporary harness today or a platform harness later."* → **migrating to skills is DECOUPLED from committing to a harness.** Room can say YES to skills now without settling the engine. Maps the split: **skill format = CRITICAL/common · which harness runs them = FLEXIBLE/open** → Felix's own guidance backs Pedro's column. Protects Loni's "not at the mercy." Banked into the facilitation sheet.
> **Ian on record (2026-06-03) = architect backing for critical-vs-flexible.** *"No point in writing a northstar that specifies implementation detail, especially given that the lifetime of any implementation is shortening every week."* → durable = the definition of one AEM; the engine is ephemeral → don't pin it. This is the architecture sponsor handing Pedro the intellectual foundation of his split (critical/durable = definition; flexible/ephemeral = engine), and it independently backs the "proposed not decided" on Felix's RFC (committing to AOv2 = specifying implementation detail). **Pedro's private read — do NOT weaponize Ian against Felix** (don't cite Ian in the RFC paragraph). Pedro replied minimally ("Agreed — and that's the line I'll hold Friday") — no answer-over. **Ian reacted 👍 + 🙏 (thank-you)** = warm close, sponsor aligned + appreciative going into Friday.
>
> ### 🟢 2026-06-03 (#5) — evening #aem-agents posts: Ian Boston points at Pedro's proposal as THE direction; Ian Reasor demands direction
> Two evening replies on the fragmentation thread (`C09KKLW1N86`).
> - **Ian Reasor (18:24) = the live demand for direction (leans single-AOv2-via-manifests).** Argues you DON'T need multiple harnesses for multiple UIs or different per-UI skill sets — AOv2 supports multiple manifests (skills/marketplaces/MCPs/tools/settings per UI); `ao.adobe.io/chat` = a *reference* UI not THE UI, teams encouraged to build own UIs on AOv2. *"Even if not AOv2… we could align on a single harness configured differently per UI."* Real pain (his words): *"the biggest issue I'm facing is the lack of direction for our team… it feels like the strategy is 'go work something out for yourself'… we need to communicate WHERE teams should contribute and HOW we expose them in our UIs."* Concrete cross-agent gap: a user in EPA looks for an asset → no DAM capabilities; Tanju's OneAEM-MCP-as-skill would go to EW + EPA but Onboarding customers still wouldn't get it. **Reasor = customer of Pedro's output, NOT adversary** — his pain is what Pedro's layer addresses.
> - **Ian Boston (18:51) = firmly distributed/no-mandate + the harness inventory + points at Pedro's work as the direction.** *"It's not 'if' — some teams already write their own harness."* **Inventory (gold for the surface map):** EMA (multiple versions/18mo), **DAA** (codex, after trying AOv1→AOv2→codex), Mysticat/Mystique (Claude SDK harness built by Claude), **FluffyJaws v2** (Codex desktop + webapp), slicc/Pi (sandbox, not our infra), Experience Workspace (*"CloudFlare worker reaching its limits, looking for an alternative"* ← corroborates the EW-ready-to-move signal), EDS Skills (many). *"Hard to dictate thou shalt use AOv2… I'm not willing to tell a team they must, I got shot down by leadership last time on AOv1."* **The gold line for Pedro:** *"What has been proposed leaves you free to do that and to use skills from any other team if you need to, with the one fundamental ask, the UX complies with CXO application UX guidelines."* = Ian Boston pointing at Pedro's consistency layer as the **non-mandate direction** that answers Reasor's plea, AND naming the "one fundamental ask" = critical-vs-flexible (harness free, UX-compliance critical), AGAIN, in front of the group.
> - **🆕 "CXO application UX guidelines" exist** = a real artifact. Pedro's "definition of one AEM" must **reference + extend** them (agent-specific layer), NOT duplicate. Investigate what/where they are.
> - **Pedro's reply (drafted, his correction applied):** split honestly — the "where do I deploy / must I build my own harness" part = the harness question, NOT his to adjudicate, point to existing guidance (you don't have to build your own; shared-harness path exists) **without naming AOv2** and **without assigning ownership to Ian B** (Ian B *refuses* to own/mandate it — the deploy-owner is genuinely unowned, which IS Reasor's complaint); the part Pedro owns = **skills declared/discoverable across surfaces (the EPA-Assets gap) + UX consistency** = what Friday locks. **Lesson (Pedro's catch):** when a question's core is outside your lane, split it honestly — answer the part you own, name the part you don't, don't reframe-around the literal question (a frustrated asker reads reframe-around as another dodge). Parked candidate in state.md (1 instance).
> - New stakeholders for the map: **Ian Reasor** posture note (direction-demander, AOv2-via-manifests, EPA-Assets gap = Pedro's lane anchor); harnesses **DAA**, **FluffyJaws v2** to add to AEM AI Mapping.
> - **✅ Pedro posted the Reasor reply (2026-06-03 20:40)** — split honestly: owned skills-discoverable-across-surfaces + UX (the EPA-Assets gap), named the harness/deploy part as not-his + pointed to existing guidance (NO AOv2 named, NO Ian-B ownership — both per Pedro's corrections). Clean reactive-ownership + scope-honesty rep (H-007 3rd reactive success, prep-iterated). **Brian DM exchange also posted** (PoCs = the check is the cheapest PoC, captured-output-first; evals-vs-taste = LLM judges checkable rules / human judges craft; "I will coordinate" the check-PoC). **Brand-travel split acted:** behavioral brand (skill-carried, travels everywhere incl. plain text) vs visual skin (renderer-bound) — table split + "Claude→an LLM" neutralization done in vault, **v4 republish queued for next CC restart** (Confluence 401). **Silvia twice-lost** on the consistency story → bring a user before/after tomorrow (not prose); artifact `Silvia Followup — Consistency Before-After.md` + short DM drafted. Knowledge: ai-product "Rendering Contract Carries Structure Not Skin" refined (2-layer brand + check splits LLM-rules vs human-taste); [[user_ui_cx_gap]] +2nd instance (story too abstract for design → before/after).
>
> ### 🟢 2026-06-02 — Skill provenance/trust = a governance gap (Ian thread), extends the declaration-standard lane
> Pedro shared `runkids/skillshare` (OSS skill-sync across CLIs, MIT) with Ian. Ian asked if it's the same as `skills.sh/adobe/skills` (a registry that scrapes GitHub by tag, `npx skills add`) and flagged the supply-chain risk: *"people doing npm install without realising they could be opening a backdoor into their entire digital life… many startups wanting to be the next npmjs."* **The distinction matters for Pedro's lane:** skillshare = sync/distribution from sources you control + prompt-injection audit; skills.sh = central registry + npx = the backdoor risk. **This validates the git-native declaration thesis** (declare skills in trusted repos with tags, NOT a central marketplace → provenance stays with the source). **New adjacent lane candidate: skill provenance + trust = the governance layer none of the "next npmjs" startups solve — Pedro's to own for AEM.** 1 obs → parked in `state.md` (hold for 2nd). ⚠️ Interpersonal note: Pedro's first reply *answered-over* Ian (asserted his thesis as the rebuttal); leadership lesson captured in [[feedback_co_author_dont_answer_over]] — with the sponsor, validate + name shared gap + hand back, no damage-control.
>
> ### 🔴 2026-06-02 — Project Flywheel located + Pedro asked Gilles to get into the workshop
> **What it is.** **AEM Experience Flywheel** = AI closed-loop content system (SENSE → GENERATE → DISTRIBUTE → MEASURE), lives in Experience Workspace, "weeks → hours." Confluence `3884318971` (space AEMSites, v56 = very active) + POV page `3871768929` (Satya Deep Maheshwari space). NOT the ADAC/Openprise sales-lead "flywheel" nor Firefly 3D "flywheel" (different projects, ignore). Phases: SENSE=Nerve Center (4 signal layers: RUM/CWV telemetry, LLM Optimizer+CDN logs, Semrush, Commerce → proposals); GENERATE=Spellforge (dual WYSIWYG human+agent rendition; **Enterprise Ground Truth = 10-layer brand corpus exposed as a SKILL**; Learnings); DISTRIBUTE=Tokowaka (one URL → humans + AI agents at CDN); MEASURE (fast RUM/citation + deep CJA/revenue). **Skills = "load-bearing", "ship as skills first", deployable to Claude/ChatGPT as MCP tools** (3 tiers: System/Adobe, Ground-Truth+Learnings/Brand, Practitioner/Author; markdown at `/.da/skills/*.md`). 4 compounding learning loops. Maturity L0-L3 per content-type.
> **The workshop.** June 2026, **Basel office**, Mon-Fri. Kick-off "Intro & Goals", breakouts, Demos+Next Steps Fri, team dinner Wed (Fiorentina, **reserved under Gilles Knobloch = the organizer**). Slack `#tmp-experience-flywheel-workshop-june-2026` (`C0AS9BKU083`). "Learn" phase = Michael Marth; EW = Martin Buergi / Markus Haack. Objectives: E2E demo in EW / co-innovation readiness / support other AEM generations. **Governance plugs in** (Catalin Luta May 18: *"in two weeks we'll join the Flywheel workshop to plug it in with the other services"*) → **Philippe is in; Pedro was NOT.** Attendee table on the page is blank in export (no usable name list — confirm with Gilles).
> **Why it matters for Pedro (entry angle = position, not status).** The flywheel is the **convergence vehicle** for everything Pedro circles: skills (his declaration-standard lane, Ian-backed), EGT (Daniel Mrose/Philippe — confirmed a brick *below* his lane, a skill source, not a competitor — validates the May 29 correction), Experience Workspace (the surface + its chat UI / shared component lib in the EW PRs), and the **"One AEM" bridge problem** (two MCPs: DA MCP [Markus/Chris Millar, EDS] vs AEM Content MCP [Tanju Erinmez, AEM CS] — gknob+chuesler proposal for a Content API on Helix 6, **NOT decided** = unowned cross-cutting lane). Plus the MEASURE phase has **no cross-agent measurement substrate** — which Pedro owns (Felix pipeline, 3-tier). **His structural claim is stronger/more cross-cutting than Philippe's single-agent plug-in.**
> **⚠️ The workshop is LIVE NOW — June 1-5, Basel** (channel read 2026-06-02: kickoff June 1, Cedric "Day 2 starts" June 2). Not a future event. **Remote join is possible** (Catalin Grigore + Elena joining remote; Teams link requested for kickoff + the **Friday demo**). Structure = **workstreams**: Gilles (June 1) asked each to post `name / spokesperson / a plan for the week` → owning/attaching to a workstream is the entry mechanism, not "being added." Channel made public May 11 (anyone can join).
> **🔑 The entry hook = SENSE + LEARN.** Cedric (May 18, the framing voice): *"We got a lot of tech for 'generate' and 'reach' — I'd like us to focus on 'SENSE' and 'LEARN', these will make the difference."* **LEARN = the learning loops = measurement / value-realization = Pedro's owned substrate** (Felix pipeline, 3-tier). Leadership spotlighted the least-owned phase and it's exactly Pedro's lane. Enter as "I own the LEARN/measurement substrate," not "let me attend."
> **Inside allies (multiple routes).** **Corey Dulimba** is deep in it (built the e2e story + canvas + attendee list) = Pedro's EPA co-author = fastest warm intro. **Bertrand is in the channel since May 11; Jean-Michel Pittet since May 12** = backup is trivial (Bertrand is literally inside). Michael Marth (map topics → narrative, find gaps) = convergence ally. Daniel Mrose / Catalin Luta / Andrei Tuicu = EGT side. Origin: Gilles April 14 ("acceleration of Experience Flywheel for customer co-innovation; right now isolated concepts & demos, want e2e in a customer context"); merged with the EGT workshop.
> **The honest signal.** It started WITHOUT Pedro while Bertrand, JM, Corey, Philippe are all in → his reporting/measurement lane wasn't pulled in. Not malicious — but the SENSE+LEARN gap *they* flagged is exactly why he should be there. Turn the oversight into the entry.
> **Move taken + sharpened angle.** Pedro **Slacked Gilles 2026-06-02** to get in — value-first (cross-agent measurement + skills/consistency = One-AEM bridge), NOT "can I attend," NO mention of Philippe (status framing = suicide; don't reveal he tracks Philippe). **Sharpened next:** claim/attach a **"Measurement & Learning loops (cross-agent value-realization)" workstream** (spokesperson = Pedro) via the workstream thread; warm-intro through **Corey**; join the channel + get the **Friday demo** remote link; Bertrand in-channel = instant backup.
> **🟢 LANDED 2026-06-02 — Pedro chatted with Christian Meyer (Learning Machine spokesperson) and it converted.** Pedro proposed design features for the Learning Machine: *"first hypothesis, then confirmation/information"* (the loop leads with the hypothesis it's testing, not the answer); *"capture product gaps not only for the dev backlog but to tell the LLM about possible workarounds in the meantime"*; + others. **Christian noted all of it, said it was important**, and **asked Pedro for the link to his reports — specifically the Deep Chat Analysis part.** = the Learning Machine workstream pulling Pedro's reporting substrate in = the `[P]` landing (own the substrate, the workstream consumes it). Pedro recapped the features to Christian in writing to bank authorship (don't let ideas get absorbed unattributed). **Watch:** Lenard Palko (5-27) has a skill combining Chat Analysis + Splunk + Langfuse + Jira MCP to cluster failures into Jira — overlaps the same Learning-Machine space, ally-or-duplicate.
>
> ### 🟢 2026-06-01 (#4) — Manas call HELD (Bertrand + Pedro + Yanira + Manas): RESOLVES the CX Coworker uncertainty from (#2)
> **Source:** transcript `Agent Owner Alignement/20260601 - AEM Agents Sync with Manas .md` (filename was mislabeled `20260501` — Pedro corrected it to `20260601` on 2026-06-02; the June-10 GA content made May 1 impossible). This **is** the live AOv2-timeline call (#2) flagged as "being scheduled" — held June 1 (Ian was NOT in it, despite #2's expected roster). Manas Garg = AO dev-experience lead, the authoritative source. **This call converts most of (#2)'s "UNCONFIRMED / hearsay" into confirmed.**
> - **🟢 Coworker is REAL and CXO-level — no longer Bertrand's unconfirmed framing.** Manas: *"coworker becomes the Uber entity and everything else is aligned to coworker as the initiative… it's co-sponsored by Amit."* Still genuinely open whether Coworker is *"a brand or a SKU"* (Manas' words) — that part stays unsettled. The "CX" prefix Bertrand used: Manas just says "Coworker," framed at CXO level.
> - **🟢 GA = June 10, NOT June 11.** Manas: *"it's become June 10 now."* Corrects the (#2) "GA June 11 = hearsay." What goes GA June 10 = **Coworker Essential.**
> - **🟢 Two tiers (this is the real structure):**
>   - **Coworker Essential** = ex-**Project Halo** (mid-market, simplified). *"One full stack, a stripped-down version of everything."* **Standalone — NOT inside core product UIs** (no AJO/CJA/RTCDP). *"You don't buy AJO, you just buy coworker essential."* → **this is the June-10 GA.**
>   - **Coworker Enterprise** = ex-**AOv2** (Summit announcement). **AOv2 = the starting point/foundation.** Stacks merge *"at some point"* but **not by June 10.**
> - **🟢 Architecture relationship CONFIRMED (validates Pedro's dependency map).** Manas: *"coworker is a layered application on top of the agentic platform… AOV2 becomes the foundation on top of which the coworker is built, but coworker is an application. AOV2 is the agentic foundation."* Coworker isn't only agentic — it's the overall marketing/CX *workflow* experience. → the nested stack from (#2) holds: **Coworker (app) → AOv2 (agentic foundation) → AO + AIA.**
> - **🔴 AI Assistant fate = OPEN, and AEM was invited to help decide.** Manas: *"what happens to AI Assistant is not clear… I hear both positions — it stays / it doesn't stay / everything in between. Your product leadership, if they can help resolve this, that will be an important step."* → **direct influence opening for Pedro + Bertrand.** Ties to Pedro's consistency lane (where does the assistant route post-Coworker).
> - **🔴 Coworker = standalone UX OUTSIDE current apps — contested.** Manas: *"standalone user experience outside the current applications… different points of view whether it should be within the current experience or not."* This is frontally in tension with Bertrand's AEM goal: companion AI **in** every surface + context-sharing UI↔assistant.
> - **Bertrand's AEM frame (deck-grade, his words):** *"~100,000 practitioners… equip all the surfaces in AEM with a companion AI… we got that to some extent with AO 1.0 in side-by-side mode… really important to understand if AO 2.0 is the right foundation for a model all about sharing context between a conversation and an associated product UI."* + *"building this agentic CMS is not optional. We need to do that very quickly."* Frustration: the Agentic product review w/ Amit ~2 weeks prior was **cancelled** — he's "fishing" for the timeline/strategy source.
> - **🆕 New stakeholders (Coworker org) — added to Stakeholder Map:** **Raj Patel (Ramaraj Patel)** = Coworker **product lead = Pedro's product counterpart** (Manas: connect with him for June-10 docs — Pedro action); **Babu Ramaraj** = Coworker PgM (Yanira's counterpart); **Vineet Sharma** = Coworker eng lead (**⚠️ ≠ Vineet Barshikar** the AIA/A2UI architect — two Vineets); **Horia Galatanu** = PM lead for the **platform** tech (product detached to Coworker, platform stays Horia); **Joshua Hailpern** = eng capacity for the Coworker UI ("not his product"). Manas offered Bertrand a **weekly cadence**; Bertrand in San Jose the week of ~June 8.
> - **Impact on the architecture-session framing:** Q1 (single vs distributed) gains weight toward "AOv2 as foundation" at CXO level (Coworker Enterprise builds on AOv2, Amit-sponsored) — but the AI-Assistant decision is open and AEM was invited in = exactly Pedro's lane (consistency + where the assistant routes). Pedro's AOv2-timeline counterpart is **Raj Patel**, not Manas.
>
> ### 🔴 2026-06-01 (#3) — Agent Owners Alignment CALL (held): Pedro presented North Star blog + consistency extension LIVE; single-harness-vs-distributed tension went public
> **Source:** transcript `AEM Agents Intelligence/Agent Owner Alignement/20260601 - Agent Owner Alignement .md` (Yanira-hosted recurring call, ~33 min, **low-fidelity** — long screen-share gaps; the core North Star discussion 16:56–20:41 + Ian's framing words are NOT captured, only Pedro's). **Distinct artifact from the June 1 #aem-agents Slack thread and the post-2 review DM** (both also June 1, captured in #1/#2 above). This = the recurring Agent Owners call where Pedro presented, fulfilling the predicted "Pedro owns 2 of 3 items on the June 1 Agent Owners agenda (Northstar blog + Agent Report)" (May 29 note) → **RESOLVED: Pedro presented.** Attendees: Yanira (host), Bertrand (**back from PTO today** — minor reconcile vs "OOO until June 2"; he attended June 1 but flagged limited availability the next 3 days for Loni week + JM workshop), Gilles Knobloch, Pedro, Ian Boston, Felix Meschberger, Ian Reasor, Daniel Mrose (silent — EGT owner present), Philippe Kapfer (silent), Elham Chandler, + a DAS data voice ("Speaker 1", likely André Bedas).
> - **🟢 Metrics read (Gilles, deck-grade).** *"April was clearly a spike with Summit, not the new baseline"* → May numbers ≈ March. **Net usage down, BUT returning users trending UP across agents + value-realization trending UP.** Gilles' read: *"if they're coming back, it's probably because they get something out of it."* **Pedro confirmed nothing technical changed in the pipeline** — the movement is real, not an artifact. Sharpens the existing growth-down/retention-up spine for the Loni/JM deck: the decline has an innocent explanation (Summit base effect) + the quality signal (return + VR) is rising. Pair them; never present the decline naked.
> - **🟡 DAS reference-dataset lever for the internal/external classification problem (Bertrand → Speaker 1/DAS).** Bertrand: DAS has a 3–4-yr-old **reference dataset of IMS orgs by license status** (paying vs internal/non-licensed) — *"mix the usage data with this additional reference."* Concrete fix for the categorization risk (Status item G). **Caveat (Speaker 1/DAS):** for **P42**, IMS orgs can exist with **no AEM contract** (Cloud Manager) → the mapping must be *expanded* to cover those orgs. Pedro said classification work is in motion w/ Yanira + André (DAS) + AEP. → advances item G with a named source-of-truth + a known gap.
> - **EPA co-innovation 3-week cycle (Gilles; Corey absent — team in next-cycle planning).** Skillifying EPA on both axes (output production + skills to improve the agent). **~85% quality score** on AI-predicted customer issues → tracked as adoption-blocker tickets, prioritized. Low light: deployment + code-stability issues. **Baycom** use case: couldn't get it working programmatically → moved to a **skill**, validated e2e on stage, **deploying to prod this week.** = concrete proof of the "plug skills into AO V1, portable later" decouple lever (matches Gilles' earlier portable-skills demo). Customer outreach off AI-Assistant activity = low response, but good convos w/ **UHT + UPS**. Corey intends to send the deck more broadly.
> - **🔴 THE ARCHITECTURE TENSION WENT PUBLIC among agent owners — and a new senior voice dissents from Ian's North Star.** Pedro presented Ian's Agentic NorthStar + his own "From North Star to There Waiting" extension: skills **declared in GitHub repos with tagging (Skyline-style), NOT a marketplace/central repo**; consistency layer = *"guidance for teams to achieve consistent UIs per surface without imposing yet another central library of components"* (= Pedro has already absorbed Ian's anti-component-lib reframe into his **public** framing — consistent w/ #2 DM). Then the debate:
>   - **🆕 Felix Meschberger (NEW major stakeholder — AEM eng/architect, ≠ Felix Delval the data engineer).** Agrees: hit the customer where they are (chatbot in Universal Editor / Experience Workspace / admin); the out-of-context AI Assistant UI is *"a thing of the past."* Wants a consistent **pluggable UI** ("some would call it the micro front end"). **He + Natalia are already in contact with the "Mithril 2.0 team"** about exactly this → **potential overlap with Pedro's consistency lane — watch.** His **#1 question: how are skills assigned to a session?** (coming from an AJO UI, the session must declare its origin so AEM skills aren't loaded into AJO's context → **dynamic per-session skill selection = how you get scalability out of a single harness**). His **North Star position is a DISSENT from Ian's:** *"as a North Star, one single harness… harness A + harness B could be an intermediary step, but not a North Star."* And *"in fact we are there — every team migrates to skills and every team builds their own harness just to deploy into AOV1, because in AOV1 we do not have skills, we have agents we register with an agent card."* **= single-harness-is-the-endgame (1yr out) vs Ian Boston's distributed-many-harnesses North Star. Genuine, unresolved architectural fork, now aired in front of the agent-owner group.**
>   - **Ian Reasor** (Agentic DAM, already in memory): "multiple harnesses" ≠ AOv2/Claude/codex — it means multiple **configs/manifests** of a harness (AOv2 already has dozens); per-UI skill sets (assets chat rail vs Universal Editor) = different harnesses by the pattern. His balance point: AOv1 over-aligned-with-everything (bad) → now over-fragmenting / reinventing the wheel (also bad) → **happy ground = flexibility to hit business objectives + eventual agreement on direction.**
>   - **Ian Boston:** if AOv2 satisfied all teams he'd use it, but *"it hasn't proven that"*; **avoid an edict world** (forcing it "did damage"). Context-budget concern (consistent w/ his memory framing): too much UI↔backend context (1000 skills / 100 MCPs) *"you ain't got anything left"* for real work.
> - **🔴 Pedro OWNS the follow-on.** Closed the item: *"we will have to create some space to continue that discussion. Let me take that."* → **action: Pedro schedules + frames a dedicated architecture-alignment session** (single-harness-vs-distributed + skill-session-assignment + the consistency layer). Right senior move — park a multi-stakeholder fork to a real session, don't fake-resolve it in a status call. Yanira closed 2 min over.
> - **H-007 note:** the call was a **proactive** presentation rep (Pedro chose to present) with correct live-debate **deferral**, not a reactive trigger — does NOT add to the reactive thesis (the June 1 *Slack thread* reactive-success rep stands as logged in `active.md`). No hypothesis edit needed.
> - **New stakeholders for the Stakeholder Map:** **Felix Meschberger** (senior AEM eng/architect; single-harness-North-Star advocate; skill-session-assignment is his lead question; in contact w/ Mithril-2.0 team via Natalia — lane-overlap watch) + **Natalia** (his collaborator on the Mithril-2.0 UI conversation, surname TBD). Confirm "Speaker 1" = André Bedas (DAS).
>
> ### 🔴 2026-06-01 (#2) — post-2 review DM: Ian forks the consistency mechanism (build → check) + Pedro's lane moves up a level
> **The DM (group `C0B73G42S9J`: Pedro + Ian + Silvia Mulet Ferre + Eugene Bannykh).** Pedro shared the post-2 draft "One AEM, Many Harnesses" (wiki 3908567486) May 29 14:33 — four pieces: *portable rendering contract* + *shared component library* + *surface map* + *clear line on who owns what* + brand-travel honesty.
> - **🔴 Ian REJECTED the mechanism (May 29 16:16), proposed a different one.** Verbatim: *"I am not sure we should be trying to build components. 'A portable rendering contract' and 'A shared component library' are not resonating with me, but 'A surface map' does resonate. Consistency is still needed, but I feel that's best achieved with a definition (brand ground truth for the UI) … say to claude 'Make my UI compliant with <ground truth> url and report on inconsistencies'. … standards/components/frameworks slow progress (shared cross-team decision) and limit creativity (forced dependencies). A2UI and WebMCP are good competing standards … I feel we need to move faster than they allow … unless engineering teams decide to use them. My view is not to specify at that level."* **The fork: consistency by BUILDING shared components (Pedro's draft + Eugene/Silvia/Vineet's in-build A2UI work) vs by CHECKING each surface against a written definition with Claude (Ian).** Ian KEEPS "surface map" + "who owns what" = Pedro's real lane; rejects only the component mechanism.
> - **🟢 Pedro's lane EVOLVED (version A→B) — the session's biggest strategic move.** Old version A = *PM curates each surface* (picks which skills show where). **Version A is dead**: contradicted by EW end-user-curation (Ian's June 1 point) AND by Pedro's own published blog line *"skills curated by the PM, not the end user"* which Ian keeps citing. Surviving version B = **PM owns the rails, not the picking**: the definition of what "one AEM" looks/feels like + a shared way for any skill to declare itself & be found + the consistency check. Surfaces/users curate their own skills *inside* those rails. **B is more senior (own the system, not the content)** and is exactly what Ian validated. Take Ian's reframe as a gift: it makes the layer lighter + clearly product-owned (a definition + a map + a check), not an eng-owned component system Pedro would fight Vineet over.
> - **Precision locked — "there waiting" ≠ "users pick".** Two models: surface *proposes* its skills by default (= Pedro's there-waiting; user doesn't hunt) vs user *finds+curates* their own (= EW, Ian's June 1 flag). Pedro's reply must say "the surface decides its own skills, can let users add" — NOT "users pick their own skills" (that wording contradicts there-waiting). Either way Pedro isn't choosing the skills; he owns the definition + check = complementary to Ian's distributed view, not against it.
> - **✅ Pedro's reply DRAFTED (his voice, posted by him).** Affirms Ian's reframe → recasts what-we-own as definition + skill-declaration + check (not components) → cedes per-surface skill selection to surfaces/users → claims the one durable product job (who writes & keeps the definition current = the contribution/update loop, "I think it's ours") → keeps Eugene/Silvia's component work as the *reference the definition points at* → agrees not to specify A2UI vs WebMCP (eng's call) → holds publish, nothing to Gilles until aligned. **Drafting note:** "rails" / "own the rails that make self-curation feel like one product" = NOT Pedro's words (too metaphorical/clever) — see [[draft-in-pedros-voice]].
> - **🔴 RISK (sharpened, not new).** If Ian (architecture sponsor) drops the alignment work AND the culture is genuinely Helix-disrupt/no-coordinate (*"the divergence can't be corrected", "the Helix way is to ignore and disrupt"*), then even version B has no political buyer — Pedro holds a layer nobody funds. Watch + keep Ian engaged (don't contradict him) is the mitigation.
> - **TODO reconcile:** published blog still says *"curated by the PM, not the end user"* — contradicts the winning (user-curate) world. Evolve to "PM owns the definition/rails, surfaces+users curate within" in post 2 + a blog edit. Not in the DM reply.
> - **Ian's memory framing (May 30 DM, banked).** Two memory types: **Personal Memory** (bound to IMS identity, spans CXO + DMe, VP-level call who runs it, Ian already raised w/ Alexander Saar, maybe IMS owns it; Adobe Research under **Gavin Miller**, **Loni connected**, may become a standard; keyed by IMS token, simple GET /memory) vs **Team/Context memory** (per solution owner, harness-selected). MCPs to be avoided with skills (context bloat; Adobe burned tokens on Claude CLI rollout by enabling all MCPs). Compression event = end-user flow fails 100% → use larger context, never compress. **Silvia follow-up Thursday June 4** (Eugene back): personal memory, AEM Connectors MCP (centralized?), context-compression UX, signals/opportunities (nerve center/ASO), + UX-MVP needs: visualizations consistency, enterprise context access cross-harness, **centralized skill list for Center of Excellence users**.
>
> ### 🔴 2026-06-01 (#2) — CX Coworker = Bertrand's PROPOSED AOv2 customer-facing name (UNCONFIRMED); AOv2-timeline call being scheduled
> **✅ SUPERSEDED by (#4) above — the Manas call HELD June 1 confirmed it.** Net corrections: Coworker = real, CXO-level, Amit-sponsored (Uber product); AOv2 = the *foundation*, Coworker = the *app* on top; GA = **June 10** (not 11) = **Coworker Essential** (ex-Project Halo, mid-market, standalone); Coworker Enterprise = ex-AOv2. Still open: brand-vs-SKU + the fate of AI Assistant. The point-in-time caution below was correct *as of when written* — kept for the reasoning trail.
> **⚠️ Status correction (Pedro flagged 2026-06-01): what Bertrand says here = assumptions/framing, NOT confirmed. Don't treat as decided ([[feedback_proposal_vs_decision]]).** Source: Bertrand, May 1 #aem-agent-experience-production, a suggestion **ending in "?"**: *"AOv2 is AO+AI Assistant in one box - and the foundation for the CX Coworker - so maybe keep the AOv2 label internal, and have integrate with CX Coworker customer facing terminology?"* His **proposed** (not confirmed) model = nested: **CX Coworker** (customer-facing) → built on **AOv2** = **AO 2.0** (harness) **+ AIA 2.0** (chat UI). Bertrand June 1 also said AO 2.0 "has its own UI now, **different from AIA 2.0**" (also his claim, to verify) = potential two-UI-lineage coherence risk = Pedro's consistency lane.
> - **WHO CHOSE THE NAME = NOT established.** No source on the origin of "CX Coworker." The only naming *decision* on record cuts the OTHER way: **Amit decided "CX CoWorker" is NOT used in BV demos** (Apr 15, via Guliz #experience-workspace), "Coworker"→"Assistant" in the EW assistant header (Markus Haack: already changed). So the name may be contested/not-final, and the EW-header "Coworker" (April) may not even be the same thing as Bertrand's "CX Coworker for AOv2" (May). Don't assert "CX Coworker = AOv2 customer-facing" as fact.
> - **🔴 CX Coworker "GA June 11" = HEARSAY** (Bertrand "I also heard…", email June 1 — unconfirmed; first question for the call). Don't treat the date as real.
> - **Everything above is to CONFIRM at the call, not walk in asserting.** The dependency-map artifact was corrected 2026-06-01 to label the whole stack "Bertrand's framing — confirm", not "SETTLED".
> - **The call.** Email chain (Manas Garg via EA → Yanira/Bertrand/Pedro/Ian, May 29) + Slack thread `C0AB9GHQRD2` ts 1777902183.109989 (Corey Dulimba opened May 4: *"should not spend time in v1 but build with v2 in mind. WDYT?"*). Manas declines an async timeline → wants a **live call** (Bertrand + Pedro **[PM owner]** + Ian **[Architect]** + Yanira + Manas). Bertrand available "today". **Manas dodging async = AOv2 operational migration plan still immature** (consistent w/ Trent Apr 29 "migration secondary"). Don't expect a clean date.
> - **Ken Russell's 3 rollout milestones (May 5):** (1) 2 customers = Wells Fargo + Adobe via ai-pods (done/ongoing), (2) 10–20 customers FDE model asap (uses AO UI *outside* the CXO product; legal paperwork in progress), (3) 2k+ customers TBD. Sr Leadership *may* mandate a unified cross-product rollout. Yanira's open asks (May 21, unanswered): CA/PPC status + a Roadmap JIRA for CX Coworker integrations.
> - **AEM's anchor for the room:** Ian's May 12 decision (skills-first, harness-portable, adoption-gated, AOv1 manifests as-is to AOv2, A2A dead). This call = the *operational* timeline downstream, NOT a reopening. **Trap to avoid:** don't let the room pin a blanket AOv2 *migration date* on AEM — platform timeline is AO/Manas's; AEM's path is per-agent, usage-driven (protects Loni "not at the mercy of someone else").
> - **✅ Artifact built:** dependency map HTML (deck palette) at `AAI - Project Folder/CX Coworker — AO2 — AIA2 Dependency Map.html` — nested stack diagram + settled-vs-open table + milestones + AEM anchor + 6 questions to walk in with. **Move:** feed it to Bertrand before the Loni/JM workshop (June 2-3) = arm the sponsor. Email reply (yes to call + tease the map) still to draft.
> - **New stakeholders:** Manas Garg (AOv2 dev-experience lead, the call owner), Ken Russell (AO eng, rollout milestones).
>
> ### 🔴 2026-06-01 — #aem-agents thread (Ian-launched) + Pedro posted VP-visible reply
> **The thread (C09J94L2TAR, parent ts 1780302998.598319, June 1 10:36 CEST).** Ian Boston points to Experience Workspace (Martin Buergi's video, via Satya Deep Maheshwari) as *"very far advanced compared to the AOv2/harness work."* End-user-editable skills, governance agent (Andrei confirmed = same Governance Agent, demo glitch since fixed). Ian's provocation: *"I am wondering if it would not be better to not have an 'Agent Northstar' or make any attempt to align with other teams across CXO, given Experience Workspace will take off while the rest of us are trying to get alignment… Seems futile to have 2 competing teams inside the same BU. That's an Amazon culture."* Tagged Pedro + Bertrand for PM guidance.
> - **AOv2 status CLARIFIED (corrects any "discontinued" read).** Markus Haack wrote *"as this has been discontinued"* — that is a **misread** of Ian's "minimal investment" stance. Per Ian's North Star (3894002388, re-read 2026-06-01, verbatim): **not AOv2-only.** *"Reality is there are many. AOv2, Slicc, CAF and the many I am sure each team will build."* Direction = **skills-first + distributed-harness, any harness may be used.** The "adoption-gated support" clause ("support harnesses where customers show usage") is in the **May 12 Slack post only, NOT in the North Star** — do not attribute it to the blog.
> - **Experience Workspace = emerging winner.** Markus Haack (EW eng): it's a **Cloudflare Worker running an agent loop, NOT Slicc** (Cloudflare because DA services are Cloudflare; Slicc experiments also on their list). They considered AOv2, prefer not to run own infra, want to **reuse not reinvent** — Markus asked twice *"what is open on AEM site regarding AOv2? The sooner we decide the direction the better."* For EW he'd take AOv2 (personal skills + schedules = on their list, EW can't do today, AOv2 can).
> - **Bertrand named Pedro's consistency problem IN PUBLIC, in front of Ian.** *"multiple implementations of the chat UI principles (ExpMod, Exp Workspace, SLICC, Forms assistant, AI assistant, and even AO 2.0 has its own UI now, different from AIA 2.0)… each their own DB, own way to load skills, own memory… it would make sense to align on a common foundation - at a minimum at the AEM level - that solves the harder problems (auth, identity, compliance, data residency)… 'thousand flowers garden'… incoherent garden."* NOTE the framing: Bertrand's foundation = **hard enterprise problems (infra)**, NOT UI components. Pedro's UI-consistency angle is adjacent, not identical — do not conflate.
> - **Ian semi-DISENGAGING (risk to Pedro's sponsor).** *"Co-ordination, CA's, PPC's all add friction, but the divergence can't be corrected. This all feels like a repeat of 'architecture is irrelevant', which I am more than happy to accept if I don't have to do that work."* + *"Roundup will need to be applied"* + *"The Helix way has always been to ignore and disrupt."* Ian — Pedro's main amplifier/architecture sponsor — signals he may drop the alignment work. If he does, the foundation becomes a PM job by default (opening + risk: Pedro alone holding it). Ian also **cited Pedro's blog AGAIN** as counter-thesis to EW: *"In From North Star to There Waiting skills are curated by the PM, not the end user"* (vs EW's end-user-authored skills). Double-edged: visibility + enrolls Pedro's blog into the PM-curated-vs-end-user-skills fight. Pedro chose NOT to assume that camp alone.
> - **Bertrand handed Pedro the pen.** Bertrand DM: *"je vais pas être trop dispo ces 3 prochains jours (loni est là cette semaine et on a un workshop avec JM demain/mercredi)"* + "Yes" when Pedro said he was starting to reply. So Pedro = the PM voice on this thread this week, Bertrand OOO, **may surface at the JM/Loni workshop** (June 2-3).
> - **✅ Pedro POSTED a reply (VP-visible, reactive-ownership rep).** Common-foundation PM synthesis: not AOv2-only (sourced to North Star) / duplication is in the plumbing, value is in skills activating Sites-Assets-Forms / answer = thin common AEM foundation (auth, identity, compliance, residency + skill portability + some UI consistency) + freedom above + keeps **one customer experience** instead of a different AEM per surface / "Happy to help pull that together with you and Ian" (co-ownership, NOT solo). Answers Markus's direct question. **= an H-007 reactive-ownership SUCCESS rep** (Ian asked directly → Pedro led with ownership-framed PM synthesis, not data-dump; contrast the May 7 NYL miss).
> - **A2UI / Vineet discovery (recoupe le post 2).** Read AIA Platform Architecture (3878837092, Vineet Barshikar, May 2026) + ERD AIA+AO2.0 (3839553368). **A2UI is ALREADY the AIA rendering standard** (*"AO streams form data using the A2UI standard for AIA to render"*); Vineet's team is building `@adobe-dxue/a2ui-renderer-sdk` (unified contract) + `@adobe-dxue/renderers-core` (shared Spectrum components) + per-domain renderer packages on Artifactory, federated via Module Federation (5-phase roadmap, governance table). **So 2 of Pedro's 3 post-2 pieces (rendering contract + component lib) already exist/in-build — but coupled to AO 2.0, engineering-owned, AEP-scoped.** Pedro's real lane = make the consistency layer harness-independent + design-owned (works on surfaces NOT on AO 2.0). ERD also confirms Pedro's brand-travel table: *"AO 2.0 is packaged with a reference UI, goal is UI-agnostic format to accommodate Claude, Codex, or interfaces other than AIA."* Vineet = ally (builds the brick), not competitor. **Lesson re-applied:** don't propose A2UI/component-lib to Bertrand as new — Vineet's team already builds it; lead with the decoupling/ownership gap, place it defensively (Pedro's call: raise the risk + question, don't assert "detach").
> - **New stakeholders:** Markus Haack (Experience Workspace eng owner — Cloudflare/DA), Vineet Barshikar (AIA platform architect — owns A2UI renderer + component lib), Satya Deep Maheshwari (pointed Ian at EW). Add to AAI Stakeholder Map.
>
> ## ▶️ left off 2026-05-29
> 0. **🟡 TOP CARRY-FORWARD — Enterprise Ground Truth (2026-05-29, threat DOWNGRADED after side-by-side source read).** Ingested May 28 EGT workshop. EGT = brand-**context/data** layer (voice, design system, claims, guardrails; segmented by region; MCP+REST), built by **Daniel Mrose's "Customer Experience Orchestration"** Eng org (Basel, under Alexander Saar = SAME VP as Ian), born from Philippe's governance-agent co-innovation.
>    **⚠️ CORRECTION (2026-05-29) — EGT does NOT overlap Pedro's published blog.** Read both artifacts side by side this session: `From North Star to There Waiting.md` (the blog) vs the EGT transcript. **They are different layers.** Blog = **skills declaration standard + git discovery + surface-consistency layer** (how the right *skill* lands "there waiting" on a surface; shared service in the blog's diagram = Ian's Memory, not data). EGT = **brand-context data** agents consume. In the blog's own model EGT is just one MCP/data source a skill calls — a brick *below/feeding* Pedro's layer, not a competitor to it. Earlier "EGT = direct overlap with North Star / Philippe+Daniel own the substrate Pedro named" was **pattern-matching on phrasing** (Andrei said "live in the center place, consumed by all agents without re-implementing in every harness" = same architecture *sentence shape* as Pedro's "one product layer nobody owns" — but different *object*: data vs skills). Drop the lane-encroachment alarm for the blog.
>    **Where overlap IS real:** only Pedro's OLDER April-29 "AEM Context project" framing (the one Trent labeled "the North Star question") — that one was about context-for-agents and DOES recoup EGT. If Pedro still pursues that, it's the collision; the blog is not.
>    **EGT actually VALIDATES the blog:** Philippe's governance flow + EGT (asset → brand check → annotation → JIRA, no chat) is a live instance of the blog's "there waiting, sometimes no chat, form follows surface" pattern (blog line 28). Evidence Pedro's framing is right, not that it was taken.
>    **Scope reality check (Pedro's own catch):** EGT's "for all our agents" is Daniel's *narration*, not demoed state. Real consumers shown = (1) website-generation effort (Florian/Quentin, not one of Pedro's 6 agents) + (2) Governance Agent (Philippe). Of Pedro's 6-agent reporting portfolio, **only Governance touches EGT today.** Dogs that don't bark: no Discovery/EPA/EDA/Content-Opt/Modernization demo.
>    **Moves (revised):** (a) Bertrand — not "recadrer who owns context" but position the **skills + surface-consistency layer** (the blog's lane) as a recognized separate product job + ask to be in the **flywheel workshop next week** (Daniel announced it); (b) Ian — revised question is NOT "does EGT encroach on me" (it doesn't) but "is my skills+consistency layer a distinct product job, and am I expected at the flywheel workshop" (draft below in May 28 section); (c) the **contribution model / feedback loop** Cedric Huesler raised hard at the workshop is genuinely unowned — but it's the contribution loop for *context*, adjacent to Pedro's *skill-curation* convention; treat as related, not identical; (d) do NOT attack Philippe frontally. Michael Marth (VP Eng) = ally on converge-flows-into-skills (asked "why are flows not simply skills?" at the workshop, line 1218).
>    **Atlassian status:** JIRA + Confluence PATs **still 401 this session** (tested 2026-05-29, both fail). Swapped fresh in `~/.claude.json` 2026-05-29 (backup `~/.claude.json.bak-20260529`) but **env not reloaded — needs full Claude Code restart**, then run the Ground Truth Confluence/JIRA search to confirm official scope + owners. Full detail: "May 28 — Enterprise Ground Truth workshop" section below + [[cxo-org-daniel-mrose]].
>
> 0b. **🟢 Apoorva AOv2 entry-point Slack thread (May 28-29) ingested 2026-05-29.** Silvia named **"Ian Boston and Pedro Ferreira are working on the AEM strategy for the future of LLM harnesses"** (public, to agent PMs) + Ian cited Pedro's blog as the skill/harness composition decision reference (3rd citation) + Apoorva voiced the exact fragmentation/selection problem Pedro's blog answers + **16% of EH prompts are cross-agent (→Audiences)** = headline data + **Silvia consistency meeting May 29 (today) — confirm Pedro is in it.** Full detail: "May 28-29 — Apoorva AOv2 entry-point Slack thread" section below.
>
> 0c. **🔴 AOv2 DECIDED (Ian, May 12) + Slack veille set up (2026-05-29).** Conrad delegated AOv2 to Ian; Ian posted the decision (skills-first, harness-portable, adoption-gated harness support, minimal AOv2 invest until BU value, **A2A dead**). Closes the long-running "discussed not decided" caution. Full detail: "May 12 — Ian's AOv2 decision" section. **Loni joined #aem-p42-leadership May 22** (VP-visible). **Pedro owns 2 of 3 items on the June 1 Agent Owners agenda** (Northstar blog + Agent Report). Slack monitoring note created in vault (`AAI - Project Folder/Slack Channel Monitoring.md`) — channels #aem-agents `C09J94L2TAR` + #aem-p42-leadership `C0ASX6AJR8X`; Pedro will ask to re-check regularly.
>
> ## ▶️ NEW 2026-05-29 — Dominik Steinacher S&O Snippets (channel C03GH9KK073, weekly digest)
> **🔴 Experience Workspace Alpha launch imminent.** ~8 weeks dev, Alpha release imminent (2026-05-29 signal). Summit demo branch users must update config before discontinuation. Marcus Räck's product = one of the 4 fragmented surfaces in Pedro's convergence/surface-map lane. Alpha = convergence conversation more urgent. Link: https://cq-dev.slack.com/archives/C03GH9KK073/p1779457262684299
> **🟡 Modernization Agent new prod release.** Dynamic Media/Scene7 image support + header/footer migration skills live. https://aemcoder.adobe.io/ — Gabriel/Mike's agent. Note in next Agent Owners update.
> **🟢 "Context engineering" replacing prompt engineering** — AWS Summit external signal. Aligns with Loni's May 12 reframe. Deck-grade validation.
> **Source:** Dominik Steinacher, AEM Strategy & Operations. Track channel C03GH9KK073 for weekly digest.
> **🟡 Martin Buergi = Experience Workspace Alpha launch lead** (not Marcus Räck who declined unified-chat ask May 5). Pedro DM'd Martin 2026-05-29 15:15 CEST: surface-map intro, asked for 20-min walk-through of Alpha (surfaces/personas/harness). No reply yet. Questions channel for EW: #C0AJRM93BAN. Add Martin to Stakeholder Map.
>
> ## ▶️ NEW 2026-05-29 — Agent Owners Alignment Call page read (wiki.corp.adobe.com/pages/viewpage.action?pageId=3716634108)
> **Page owner: Yanira Castaneda** (all recordings in her OneDrive `castaned_adobe_com`). Version 20. She maintains it.
>
> **🔴 Slick = "Sliccy" CONFIRMED.** URL: https://www.sliccy.com/. Built by **Karl** (agent) + **Trilove** (team). Browser-based Chrome sandbox. Client-side execution (no server costs). Embedded DB + virtual machines. Skills optimized for browser. "Sprinkles" = UI generation layer. Memory had "Slick" as low-confidence from garbled May 5 Otter — now confirmed. "Rosetta = Manager Services" still NOT confirmed anywhere.
>
> **🔴 Onboarding Agent already on AOv2 — Ian confirmed (May 11 meeting).** Ian reported: immediate UX improvements, proactive recommendations, easier configuration, marketplace integration ready. First confirmed AEM agent live on AOv2 in prod. Promotion-grade deck proof point — AOv2 works in practice for AEM. Owner: Nick Whittenburg.
>
> **🟡 Sergiu** = active AOv2 practitioner to track. Runs AO 2.0 pipeline troubleshooting experiments: sandbox environments, Python scripts generated by Claude, automated fixes + PR creation for customer repos. Code execution visible in AO 2.0 UI. Add to Stakeholder Map.
>
> **🟡 Gabriel/Modernization — "Stardust" + "Snowflake" skills** = additional spin-off skills in progress beyond the main Modernization Agent. Hard requirement flagged: users must push changes to GitHub from the agent. Unresolved dependency.
>
> **🟡 CXO Roadmap Template (new 5-section format).** Bertrand introduced Adobe CXO template: agents / cloud / sites / assets / forms. Roadmap webinars **June 9 + June 10** — external dates. Roadmap send to design agency = NOT Pedro's task. **Bertrand OOO until 2026-06-02 (Monday).** Bertrand-gated items (Bertrand 1-1 agenda, convergence lane conversation, flywheel workshop ask) all shift to next week.
>
> **🟡 Open unclaimed action from May 11.** "Create a Wiki page documenting AO 1.0 vs AO 2.0 experiences, limitations, benefits for AEM use cases." Assigned to "the team." Nobody claimed it. **No existing page — this is a to-create artifact.** Pedro's reporting + Ian NorthStar position = natural owner. Visibility move if Pedro claims it.
>
> **🟡 CSO service model action still INCOMPLETE** on the page (May 11 follow-up task: "Define CSO / service model — agent vs umbrella"). Pedro has this as an open task. Still unresolved officially.
>
> **🟢 Co-innovation spreadsheet.** OneAEM SharePoint: "Co-innovation requests and prospects.xlsx" — linked from the page. Pedro hasn't referenced this. Worth checking which of the 6 agents appear.
>
> **🟢 Try Before You Buy clarity locked.** Cloud service customers = TBYB enabled. Managed services = playground only. Managed services agents not in H1; may land H2.
>
> ## ▶️ left off 2026-05-28 pm
> 1. ✅ **Blog publié + amplifié.** "From North Star to There Waiting" published 2026-05-28 (https://wiki.corp.adobe.com/spaces/~pedrofer/blog/2026/05/28/3901747358/From+North+Star+to+There+Waiting). Post-publish edits applied: deduped the two "nobody owns" into one **"one product layer"** thesis + scoped consistency to **one AEM** (not Adobe-wide). Conrad async FYI sent (Conrad out 1-2 wks). Ian pinged → replied *"Looks good, have referenced it to continue the conversation"* = amplifying on his feed. **Then edited his Agentic NorthStar post to point at Pedro's, verbatim: *"Pedro Ferreira has a response to this question, worth reading: From North Star to There Waiting."*** The architecture author publicly routing his audience to Pedro's product-layer answer = Senior-Director-grade visibility artifact. Bankable. RESOLVED.
> 2. **Philippe reaction = ❤️ on Pedro's Slack post** (after Pedro declined letting him annex the Bucharest keynote with his "workflow problem" thesis). Surface-friendly / de-escalating. Per competitor frame ("he doesn't attack, he makes you applaud him") a heart ≠ alignment — keep watching for a reframe-publicly move.
> 3. **Keynote Bucharest — round-4 pass still pending.** Prep note `Bucharest June Workshop — Skill Proliferation + Modernization.md` still says "registry"; needs registry → declaration-standard + git-discovery update before the session.
> 4. **NEXT THRUST — consistency layer.** The post developed the skill *declaration standard* (backstage, well-specced); the *consistency layer* (AEM surfaces feel like one AEM — same chat grammar, same "+", shared history/context) was left **asserted, no mechanism**. Pedro's chosen next piece. Working thesis (2026-05-28): consistency = a portable, **harness-agnostic, design-owned component lib + light contract**, NOT Mithril (Mithril likely AOv2-coupled today → "everyone on Mithril" = forced rewrite of the 4 existing chats: Experience Workspace / Modernization / Slick / Rosetta=Manager Services — ⚠️ "Slick" + "Rosetta" are low-confidence names from a garbled May 5 Otter auto-transcript, unverified, Pedro to confirm). Decoupling from the harness lets Pedro pursue it WITHOUT forcing the undeclared AOv2 decision = protects optionality (Loni: "can't be at the mercy of someone else"). **SEQUENCING (Pedro's call, politically careful):** Bertrand FIRST (read his vision on formalizing a consistency layer outside AOv2), Silvia today (design/pattern level only, harness-neutral, hedge AOv2 per May 12), **Tim Lynn / Mithril NOT yet** — asking the harness-coupling question = de-facto leak of AEM's AOv2 posture. Glimpse-for-Silvia drafted (harness-neutral). Open verify: does a shared chat component lib exist / is it feasible (Silvia's domain — do NOT assert Spectrum, that was an unsourced Claude import).
>    **Public-thread signals (2026-05-28, comments on Ian's NorthStar post):** (a) **Ian cites Pedro's post TWICE as the reference answer** — to Andrii Konosov (*"more detail on that here"*) and to Ian Reasor (*"In From North Star to There Waiting, the pattern is to ensure the UI and harness has precisely those skills necessary for that UI surface"*). Pedro's billet = canonical reference on UI consistency in a VP/architect thread. (b) **Ian on-record backing decoupling:** *"not all surfaces are the same and hence not all harnesses that support them will be the same"* → consistency can't come from one harness, must be the UI/pattern layer on top. **Citable to Bertrand** as architect support for the harness-independent thesis. (c) **Andrii Konosov** raised the UX fragmentation concern (scattered chatboxes = nightmare; wants purpose-built UIs not bolted widgets) — Pedro replied (posted), reconciling: purpose-built per surface + shared grammar + form-follows-surface (incl. no chat). (d) **NEW stakeholder Ian Reasor** — working on "Agentic DAM" strategy/architecture; validates the no-chat/inline layer (agentic workflows: asset QC, metadata enrich, licensing) + pushes customer-deployed-skills-alongside-Adobe's. Potential ally/contributor on consistency + skill portability. Ian Boston's P42 caution: don't let customers deploy their skills INTO Adobe harnesses (activation risk) — but customers using Adobe skills via API-first + MCP in their OWN harness is fine.
>    **CORRECTION (2026-05-28, after reading `AO 2.0/Mithril & Fruitbar - Crash Course (non-frontend).md`) — earlier "Mithril = the chat UI everyone adopts" was IMPRECISE:** Mithril is **not a chat UI**, it's the **wiring** (WebMCP-based) that lets the AO 2.0 brain **read / interact / write** on existing screens ("AI sees your screen and acts on it"). Coupled to AO 2.0. The actual chat = a **separate, portable, forkable** piece: **NextGen AIA UI** (repo `aia-ui-experience`, *"the chat, not the container, can live wherever you need it to"*). Fruitbar = AO 2.0 generates bespoke new screens. **The shared component library Pedro's consistency layer needs already EXISTS = Quarry** (Adobe-internal shared UI components, "any team already on Quarry" gets Mithril free; sits above/beside Spectrum). So the earlier "don't assert Spectrum" note resolves: the brick box = **Quarry**, not Spectrum directly. **Mapping consistency-layer needs → existing Adobe pieces:** chat grammar/controls/"+" → NextGen AIA UI; shared visual bricks → Quarry; inline help / no-chat (Silvia's "read UI don't interact" + form-follows-surface) → Mithril; history-follows-user → nothing ready, needs Ian's memory service. **THE REAL TENSION FOR BERTRAND:** the ready-made bricks (AIA UI + Quarry + Mithril) all sit **in AO 2.0's orbit** → cheapest consistency path = reuse them = **lean toward AO 2.0**; most harness-independent path = define/build own bricks = **more work**. Sharpened Bertrand question: "reuse the AO 2.0 bricks (lean AO 2.0) or stay independent and define our own?" Mithril doc people: Adam Thomson (arch lead), Tim Lynn (partnerships), Quarry integ = Somya Biswari + Rodson Clavel (Somya also on Prompt Library Platform = cross-link).

> ## ⏱ Consolidation checkpoint — 2026-05-19 (staleness flags, NOT new facts)
>
> Session summary: [[20260519 - Session Summary]] (May 18 Agent Owners Alignment ingested, Pedro hosted). Date-driven items now past — confirm outcomes, don't assume:
> - 🔴 **Loni + JM deck (week of May 11)** — meeting window passed. Outcome NOT captured. Debrief ask: did it happen, what landed, what's the follow-up. This is the single biggest open.
> - 🔴 **SD-1 / SD-2 / SD-3** (due May 6/8) + **KR4 Priority Consolidation** (due May 8) — all past due, status uncaptured. Reconcile.
> - 🟡 **Felix/Lara Langfuse Governance pipeline** — PR merge Fri May 15 → data due Mon May 18 (yesterday). Confirm landed + integration started.
> - 🔴 **Workshop Foundation facilitator** — captured as HIGH PRIORITY Bertrand 1-1 item (block in `Experience Hub - Questions for Next 1-1 with Bertrand.md`). Lead the next 1-1 with it. No longer "decide" — the decision is accept; the action is say-yes-to-Bertrand-with-the-May-18-link.
> - 🟢 **Ian North Star 1-pager — LANDED 2026-05-19** (was NOT started as of May 18). Ian published [Agentic NorthStar](https://wiki.corp.adobe.com/spaces/~boston/blog/2026/05/19/3894002388/Agentic+NorthStar) as a blog the day after the call Pedro hosted (where Pedro publicly named Ian owner). Gating artifact RESOLVED — escalation/forcing-function no longer needed. Pedro lane flips to respond + distribute. Full entry: "May 19 — Ian publishes Agentic NorthStar" below.
> - 🟡 **CCF / ISO 42001 — scope NARROWED (May 18).** No longer all AEM agents → **Discovery + Governance only** this year. Loni+Bertrand finalizing exact list. July 17 deadline holds. Bertrand: *"important but not urgent, not top of stack."* Downgrade from 🔴.
> - 🔴 **Roadmap deck restructure** — Bertrand cut date **Fri May 22** (snapshot → design agency), **final Fri May 29** (broad distribution). Per-agent overview + timeline + skill-detail slides. Pedro's 6 agents need coverage.
> - 🔴 **Greg Klebus customer escalation** — Rosh + Genentech, multi-IMS-org agent scope (AOv1 = 1 org limit). Ian pulled into customer arch conversations. Feed into requirements + North Star.
> - 🟢 **Corey call** — Tue May 19 (today). On track.
> - **Apoorva punch-list** April deadlines all past — confirm closed vs slipped.
>
> Apply: when Pedro references any of the above, ASK for current state before reusing the memory value. Memory is point-in-time; these are expired.

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

### 🟡 2026-05-05 — Reports → DaaS / evaluator migration call (Pedro + André + convener + Mark/Lara track) [backfilled 2026-06-05]

Source: `AEM Agents Intelligence/AEM Experience Agent Reports/20260505 - Agent reports move to Daas.md` (Otter). Call to align Pedro's weekly agentic report with the **in-region evaluator framework**.

- **André** = the evaluator builder. Framework: each agent pushes traces → **regional Delta table**; per-region/per-agent evaluators read raw prompts, run **LLM-as-judge** against PM-defined criteria **in region**, push a **score** → centralized **Databricks** table (cross-region/cluster/agent). Has a config app where teams define criteria + region (the fancy UI replacing git markdown). Uses in-region OpenAI. Wants Pedro's git + wikis to understand + recreate an existing metric as a test.
- **Convener (Speaker 1, governance/observability + supports Mark Pfaff)** = the push: **replace Pedro's manual stack with a NEW app**, everyone defines criteria once there, data in Databricks, then layer agents/MCP so senior mgmt can ask high-level questions. Governance agent = **customer zero**, then sell adoption to other teams. **JC/JCSR** want Pedro + governance aligned → present a **business story** so teams come to adopt. **Mark Pfaff + Lara** = evaluator metric definition on harder KPIs.
- **The legitimate migration driver = compliance.** Pedro on record: *"compliance is not a topic here, it should be"* — current pipeline = **Bedrock cross-region + cross-region aggregation ("which is bad, which I know")**. Evaluator = in-region, PII-compliant → closes Ian's data-residency risk + Michael's pushback. This is the clean reason to migrate off the manual SQLite/Bedrock pipeline.
- **Pedro's persona model (his framing, leadership-facing):** 3 personas — technical teams (Langfuse traces, stays), agent-owners/PMs (per-capability stats), senior mgmt (aggregated). Two report layers: **Python-calculable KPIs** + **Business Value Realization** (LLM-as-judge, one definition file per BVR block in git, refined with each PM). **Not done yet:** aggregate BVR into one number per agent + one overall number.
- **⚠️ Strategic guard (same move as the harness session):** don't own the engine (André's evaluator infra + Databricks = theirs), **own the definition** — the persona model, the BVR criteria files, the aggregation logic, the business story JC wants. Pedro *wants* to hand off the manual pipeline ("set me free") — fine, but the weekly report is his **visible leadership artifact**; if it's absorbed into an app owned by the convener + André, keep the definition/narrative layer as Pedro's so visibility doesn't migrate with the infra.
- **Ties:** Rubin needs AEP/AOv2 data (Bertrand 6/4) → this in-region Databricks = the source; Mark Pfaff (evaluator) = the MCP-report person Pedro wanted to sit with (+ Tanju). **Pedro action (taken):** share git/wikis/repos with André + test recreating one existing metric in his app. (Pedro was traveling the following week = Bucharest.)

### 🟢 2026-06-05 — Friday arch session HELD (Ian Boston + Felix Meschberger + Pedro): critical-vs-flexible list co-built live, engine NOT decided

Source: `AEM Agents Intelligence/Agent Owner Alignement/20260605 - Ian Felix Pedro.md` (Otter; file was misnamed `0505`, renamed `0605` — this is the **June 5 arch session itself**, not a May event; Speaker 1 = **Felix Meschberger**, relabeled; Speaker 2 = brief, unidentified). **This IS the Friday architecture session the cockpit prepped.** Pedro opened by **naming the elephant** (one harness vs many) — not in the capture, transcript starts mid-flow at 0:00. The room (just Pedro + Ian + Felix, as planned — Reasor was the Slack thread, not this room) **built the critical-vs-flexible list live in a wiki Pedro captures.** Clean execution of the cockpit: elephant named, engine left open, definition owned by Pedro. **The June fork developments (Tanju middle-path, consume-vs-fork, the public RFC) did NOT surface in-room** — they stayed at definition level (Ian: *"we're going too deep… these are conceptual guidelines"*).

**Ian's framing principle (open):** negotiate what's org-wide (identity) vs an abstract pattern that lets solutions innovate. *"If we stifle innovation, we stifle innovation."* All agreed: core UX must be consistent + some core APIs consistent (else duplication).

**Agreed CRITICAL (co-signed Ian + Felix):**
- **Common UX** — chat grammar + core controls + what "+" offers. Starts with **design/brand** ("what does the chat look like"), negotiated across all CX by those who normally do that work. Ian: *"common One Adobe, not One AEM."*
- **In-context, NOT "one touch point to rule them all"** (= the AI Assistant out-of-context mistake). Felix: a common UI dropped in everywhere, but in-context.
- **Core services:** memory (bits across all Adobe), IMS identity (**AIP** should drive — note AIP not AEP), compliance = Adobe policy compliance (CCF, SOC2, HIPAA, FSI). Ian reframes compliance as data-compliance/governance/access/identity properties, not the standards themselves.
- **Skills:** declaration + portability (markdown transportable; **Agent Skills** spec — capital-S = Anthropic skills). EW treats skills as content (markdown, no code).
- **Per-session scoping** of capabilities (skills/MCP/API/tools) **seeded by the surface** — two lines: what's in the surface, what enters the session.
- **Skill selection per surface** — teams have complete control over which skills are available (the AI v1 failure: "analyze my pages" → flips to analytics → "you're not licensed" → "it's my content").
- **Stays current with Anthropic/Claude + standards** = top-level critical. Standards stack: **Agent Skills (top) → Open API → MCP (bottom)**.

**Agreed FLEXIBLE / NOT critical:**
- **Implementation / shared components** (React? MFE?). 💥 **Ian's January experiment = the proof:** team told "make it Spectrum" → agents *found the Spectrum definition and wrote the CSS from scratch, accurate, zero imported code.* Ian: *"that's why I don't think we need the components — components add friction."* Felix conceded: *"critical for UX, not critical from an implementation perspective."* = Pedro's definition-not-components thesis, **proven by Ian, accepted by Felix, in the room.** The shared-component-library question was effectively closed here.
- **How the surface tells the harness which skills** — tag / prompt / semantic search (multiple ways). But Ian: non-deterministic search = uncomfortable → prefer a **curated, referenced, tested list** per surface (quality risk otherwise).

**Architecture nuances captured in-room:**
- **Drive functionality DOWN: tools > APIs > MCPs** (token footprint — Adobe burnt tokens enabling all MCPs). Heavy deterministic ops (roll out 100k pages) → behind an API/MCP, NOT in the harness. Harness executes short code (<20-50 lines, no external deps) in a sandbox.
- **Code execution = the AOv2 gap** Ian named: AOv2 couldn't "calculate pi to 100 figures"; Codex (his recent test) wrote + ran Python in a sandbox and did. (Ian: any harness implementer won't build from scratch — they take Claude/Codex/Pi → the engine question is below the list, left open.)
- **Skills authored dynamically "feel more like memory"** (personal to person/team) — ties Ian's two-layer memory framing (surface-base skills vs individual/team-learnt = memory).

**🟢 What Pedro walked away owning:** Pedro closed with *"I'll capture that in a wiki page so we can extend from there, and open up whenever we feel comfortable."* → **Pedro owns the definition artifact (the wiki).** Ian + Felix both contributed to *Pedro's* captured list = the consistency-layer ownership made concrete, three-way, without Pedro adjudicating the engine. Felix to send Pedro another link with his own additions.

**🟡 Still open / follow-ups:** (a) **engine/harness count = deliberately not decided** (good — matches the plan); the formal "open question with owner + resolving evidence" was discussed at principle level but **not written down as a parked item with an owner** → Pedro to formalize in the wiki. (b) Ian flagged **interpretation risk** (*"this wording will cause interpretation… conceptual guidelines, not directive"*) → the wiki wording needs care so teams don't read it as "model a SkillSelectionPerSurface object." (c) aggregate the captured list into the shareable wiki + decide when to open it up.

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

**April 29 strategy session outcome.** 2-hour block, Bertrand + Conrad + Yanira + Jaclyn + Ian + Carsten + Trent + Ken. Notes at `Meeting Notes/Agent Owner Alignement/20260429 - Alignment_ AEM Agents & AOv2.md`.

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

**April 29 deep transcript pass (added 2026-05-05).** 4160-line Otter transcript at `Agent Owner Alignement/20260429 - Alignment_ AEM Agents & AOv2.md` re-read in full. New signals beyond post-meeting summary:

*Architecture pivot (V1 → V2):*
- **Thin-orchestrator + fat-agents** (V1) **→ fat-central-agent + thin-agents** (V2). Fundamental rewrite. Implications for AEM agent harness ownership not yet drawn.
- Trent 1:23:07: AOv2 origin = reactive post-Opus-4.5 pivot. *"Suddenly behind, like our direction is completely wrong. And so we just completely pivoted. Migration plan has been secondary."* AOv2 NOT a stable platform yet — read carefully before betting AEM roadmap on it.
- Skills > MCP. Trent (head of AO) at 43:xx: *"in my personal use of agents, I find that I don't use mcp hardly at all."* Ken: *"mcp is a special tool"* (40:03) — demoted from layer to tool. Bertrand defended MCP-first 44:21 — *"I'm just a bit worried in the back of my mind that mcp becomes like the Swiss knife."* AEM has invested heavily in MCP-on-top-of-agents — re-evaluate posture given AO leadership skepticism.
- Marketplace = **per-team repos**, not central monorepo. Wells Fargo precedent: per-customer marketplace. AEM may be expected to ship its own.
- AOv2 lives at `ao.adobe.io` **side-by-side** with V1, not unified-shell-first (Trent 1:43:32). Counter to assumed unified-shell integration.
- Conrad 1:42:51 translation rule: *"weeks is translated into years in AM market landscape. So when you say 4 weeks, then people hear it's like 4 years."*

*Decisions landed (verbatim-anchored):*
- **V2 = direction.** Conrad 1:48:42: *"V2 is something we want to pursue and will replace what we have in V1."* But: 1:55:39 Bertrand BASL close: *"A meeting where we end with more questions than answers is a very good meeting."* — Pedro's "discussion not decision" framing holds.
- **A2A decommission for AEM specifically.** Conrad → Carsten 1:39:16: *"decision is yours, decommission and done."* Note nuance: AOv2 still supports A2A federation (Trent 1:20:39) — AEM's own A2A layer is what gets retired.
- **MCP confirmed primary AEM-into-AOv2 channel** by Carsten 1:12:53. EPA = canonical use case ("experience production main use case around mcp").
- **Reuse existing AEP-AO collab Slack channel** — Pedro suggested 1:12:12, Conrad agreed 1:12:18. No new channel.
- **AEM contribution path = PRs into AOv2 repo.** Trent 1:46:39: *"fork it, push, push PRs, file issues, complaints, feature requests."* Conrad commits 1:46:51: *"we know the code base, we can send you PRs."* Internal-open-source contribution model formalized.
- **Conrad's directive lands "next week"** to all agent owners (1:54:30). Forcing function. Trent disclaimed authority 1:22:37 (*"I won't presume to say that I can tell you what it should be"*) — Conrad is the actual decision-maker.

*Pedro's contributions (chunk 3 = his hour, full verbatim record):*
- 1:15:28 — surfaced **AEM Context project**. Trent labeled it *"the North Star question"* (1:16:11). Strong positioning win — flagged at AO leadership level. Lever for May 11 deck.
- 1:21:27 — pushed AOv2 vs A2A vs native-skills decision pressure. Critiqued Discovery Agent native-skills approach (Raul's experiment): *"felt very developer-centric… exposing way too much of the underlying implementation for what I think a practitioner would expect from an agent."* Flag — careful using this in front of Apoorva/Raul.
- 1:26:10 — convergence ask: **Experience Workspace** (3-panel UI for AEM Sites — AI coworker / admin UI / preview) should be AOv2, not yet-another-assistant.
- 1:27:32 — full convergence framing: *"Slicky… Experience Workspace… Experience Modernization Agent (cloud code on Ethos)… all aim at solving one thing, running a harness somewhere properly. I'd love to see them converge, and if AO 2.0 is the thing, I'd love that to be possible."*
- 1:28:17 — **the framing line, in Pedro's voice**: *"I would prefer us, AM, to focus on the AM use cases rather than building technology if there's a dedicated team for the infrastructure around it."* Use this as walk-out line — sourced to Pedro, not retrofitted to Bertrand.
- 1:29:11 — *"I don't think anyone has decided anything… we all learning about it."* This is Pedro's discussion-not-decision frame in real time. Holds.
- 1:29:42 / 1:30:51 — pressed Trent on **manifest customer-exposure configurability**: can AEM hide parts of marketplace UI from customers? Unresolved.
- Action item Pedro accepted: provide **Experience Workspace demo** to Conrad — Gilles or Michel (Knobloch) candidate demoer; Pedro to share recording.

*Bertrand's framing (full):*
- MCP-as-Swiss-knife concern (44:xx) — defended AEM's MCP-first investment vs Trent's MCP-skeptic posture. Tension still open.
- Multi-role / product-profile model for AOv2 admin (1:32:39, 1:33:01) — sys admin vs practitioner profile in admin console.
- **Pricing / SKU bombshell** 1:49:46–1:52:57: per-agent credit model + dedicated AI SKU may not survive AOv2 (skills collapse the per-agent unit). 1:52:32: *"didn't realise the consequences go to market-wise and pricing-wise before this meeting."* **Bertrand self-assigned to answer.** Adds AEM AI SKU risk to the May 11 conversation.
- BASL close 1:55:39: *"A meeting where we end with more questions than answers is a very good meeting. I have no problem with that. I think we achieve something."* Conrad concurs 1:55:49: *"We have much better questions now."*

*Felix:* did NOT speak in April 29 transcript. Felix's critique — that low-level agent owners had not been involved — surfaces in the **May 4** meeting, not here.

*Other speakers — Trent's signature concession on evals:*
- **Skill-level evals = UNSOLVED** in AOv2. Trent 1:37:56: *"I don't think we have that fully fleshed out the way you're describing Ian yet… it's a hard problem to solve, given how skills work, because the agent may or may not load any number of skills."* **Pedro's three-tier reporting platform has no AOv2 skill-granularity counterpart.** Position as gap AEM helps close — leverage for May 11 deck.

*New open items (add to AAI tracking):*
- Manifest customer-exposure configurability (Pedro's open ask 1:29:42 / 1:30:51) — follow up with Trent / Manas.
- AEM Context project ↔ AOv2 skills-and-tools layers — Trent labeled North Star, no joint workstream defined. Define one.
- Convergence ask: Slicky / Experience Workspace / Modernization-agent / AOv2 — no owner, no decision. Pedro is the convergence advocate; needs Bertrand alignment.
- Slick + AOv2 coexistence — Trent action item ("I'll have to think about Slack"), watch for resolution.
- Pricing / SKU under skills model — Bertrand self-assigned. AEM AI SKU + credit-tracking system may not survive.
- AEM AOv2 contribution path opened — pick first PR target (small one, low cost, high signal).
- Skill-level evals gap — frame as opportunity, not blocker.
- AOv2 mandatory or optional for AEM — Trent declined to legislate; Conrad directive next week is the forcing function.

*Quote bank (May 11 deck-ready):*
- Pedro framing line: *"I would prefer us, AEM, to focus on the AEM use cases rather than building technology if there's a dedicated team for the infrastructure around it."*
- Trent on AEM Context: *"the North Star question."*
- Conrad on V2: *"V2 is something we want to pursue and will replace what we have in V1."*
- Conrad on agentic monetization: *"you cannot sell any product in a short future if it is not AI enabled. So the skill harness might be a mandatory thing to sell AEM at all"* (1:53:19) — Bertrand's pricing question in the room.
- Bertrand BASL close: *"A meeting where we end with more questions than answers is a very good meeting."*
- Conrad summary: *"We have much better questions now."*
- Loni durable frame (April 21, still relevant): *"We cannot just be at the mercy of somebody else."*

**May 4 Agent Owners Alignement update (Pedro delivered).** Notes: `Agent Owner Alignement/20260504 - Agent Owners Alignement.md`. Pedro delivered the cautious framing in front of agent owners (Bertrand + Conrad off): *"There was no decision taken during the meeting... future discussions and synchronizations between Bertrand, Conrad, and the various teams, although early feedback from Conrad was pretty positive on V2."* Held the line — no pre-emption of Conrad's directive.

**New signals from May 4 meeting:**
- **Corey Dulimba (EPA) urgency:** *"This is becoming relatively urgent because we all have H2 roadmaps."* Asked for timeframes. Pedro deferred — Bertrand + Conrad off, won't commit dates on their behalf. **H2 roadmap risk if directive slips past mid-May.**
- **Felix Delval critique:** *"discussion that involved the low level, like all of the agent owner. And from my perspective, very little has been done at this level."* Wants per-agent migration validation to start **NOW**, not post-directive. *"the moment we decide it's a go live, we will have like weeks before we should all migrate."*
- **Raul Hudea status:** team has started on easier agents — auth gaps surfacing as first migration friction. Validates Felix's framing.
- **Yanira action:** *"I'll start a thread in AEM agents and then you guys can jump and see who might, how we can get started."* AEM agents Slack thread for AOv2 owner-level migration scoping. Watch for thread, contribute Pedro angle.

**ISO 42001 / Tech GRC compliance audit (NEW, May 4 — Robert Guthrie raised).** Brand-new compliance controls for AI services based on **ISO 42001**. ~12-13 tickets, similar to Nov-Dec CCF compliance work. **Audit starts June. Evidence due July 17.** Robert: *"I never saw this work on any of the roadmap discussions"* — trying to reach Loni, JM, Bertrand. **May force H2 roadmap changes across all agents.** Source: Amit. Track in Status & Todo as 🔴 — surface to Bertrand before May 11 deck (this is exactly the kind of "I want to make sure that Lonnie and everybody above is understanding" Robert flagged).

**CSO process split — Pedro action item (May 4).** Felix flagged need to separate business agent CSO vs technical agent CSO. Brian: each CSO must map to actual oncall team (don't wake wrong team). Pedro accepted action: *"Yeah, I'll take the point."* Status & Todo task created.

**Reporting demo (May 4) — landed:** Pedro showed Governance monthly retention (4-week return, increasing) + Philippe's brand-checks BVR metric implemented in reporting. Next: ping Brian + Corey for their BVR metrics. Pattern of contribution model working in practice — Philippe's team contributed metric directly.

**Corey + Gilles post-summit lab (May 4 opener).** EPA workbook with pluggable AEM playground instance — fills variables automatically. Highlights Discovery + Governance too. Open invitation for other agents to add labs. Possible asset for Loni+JM May 11 (customer-getting-started narrative).

**AI Assistant vs AOP — Pedro's mental model** (canonical: `AAI - Project Folder/AO 2.0/AI Assistant vs AOP.md`):
- **AI Assistant** = conversational/generative AI layer. The "brain." LLM-powered. Fuzzy / open-ended.
- **AOP** = Adobe Orchestration Platform. The "hands." Backend orchestration, deterministic execution.
- AI Assistant interprets request → AOP orchestrates execution.

**AEP AO / AI Assistant role split** (per Ilya Grafutko Slack 2026-04-27):
- AO Platform PM: `@sgeneralov` (core, integrations) + `@igrafutko` (quality / safety / compliance)
- AI Assistant PM: **Rachel Hanessian** (`@hanessia`) (Adoption) + `@namitak` Namita (Dashboards, AI Integration, AI quality)
- AO v2 (coworker): `@sgeneralov` + `@igrafutko`
- AO v2 — AIA extensions: `@namitak` + **Rachel Hanessian** (`@hanessia`)

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

## May 28 — Enterprise Ground Truth workshop (EGT = adjacent layer, NOT blog overlap)

Source: `Meeting Notes/Entreprise Group/20260528 - Entreprise Ground Truth Workshop May 2026 - Demos .md` (full transcript re-read 2026-05-29). Org chart: `screenshots/20260529-daniel-mrose-cxo-org-*.png`.

**Enterprise Ground Truth (EGT)** = structured/readable representation of a brand (voice, design system, claims, guardrails), segmented by region/country/market, exposed via **MCP + REST**. Daniel Mrose's framing (line 36): *"the contextual layer for all of our agents."* Separate service, own storage → consumable by every AEM vertical (Edge Delivery → on-prem) **and non-AEM customers = acquisition funnel** (Unilever wants to serve context to its agencies, line 460). MCP tools: `get_segments`, full context, vertical context (just voice / just design system), **research-context-for-use-case** (agentic loop infers segments). Demo: US→imperial, France→red becomes blue + euros + FR translation (Quentin, lines 562-598).

**Build org = Daniel Mrose's "Customer Experience Orchestration"** (Basel Eng, under Alexander Saar — SAME VP as Ian Boston). Full roster in [[cxo-org-daniel-mrose]]. Workshop roles: Andrei Stefan Tuicu (tech lead), Florentin Sardan (MCP), Alejandro Moratinos + Mark J. Becker (data model / nerve-center), Gerald Prendi + Lara (ingestion), Ramon Bisswanger + Michal (Philippe's flow integration), Catalin Luta (co-presenter), Florian Froese + Quentin Vecchio (website-generation consumer).

**✅ CORRECTED READ (2026-05-29) — EGT ≠ Pedro's blog. Earlier "🔴 lane-encroachment" was WRONG.** Side-by-side source comparison done this session:
- **Pedro's blog** (`From North Star to There Waiting.md`) builds the **skills declaration standard + git discovery + surface-consistency** layer. Its shared service = Ian's Memory. It is about *skills* and *surfaces*, not data. Pedro's claimed-vacant phrase: *"one product layer between the harnesses and the surfaces, and it is the part nobody owns today."*
- **EGT** builds the **brand-context data** layer agents consume.
- These are **different layers.** In the blog's own diagram, EGT = one of the MCP/data sources a skill calls (the "unique APIs and MCPs built on the data our customers entrust to us"). EGT is a **brick that feeds** Pedro's layer, sitting below it — not a competitor.
- Why it *looked* like overlap: Andrei said (line 424) *"this functionality can live in the center place... consumed by all the other agents without being re-implemented in every single harness"* = the SAME architecture sentence-shape as Pedro's "one product layer nobody owns." Same *pattern* (centralize, consume everywhere, don't duplicate per harness), different *object* (data vs skills). Don't pattern-match phrasing onto object-level overlap. See [[feedback-dont-conflate-pattern-with-object]].

**The real overlap is the OLD April-29 "AEM Context project"** (the one Trent labeled "the North Star question"), which was context-for-agents → that recoups EGT. The published blog does not. Pedro confirmed 2026-05-29 he means the blog when he says "what I presented" → so for the blog, no conflict.

**EGT VALIDATES the blog.** Philippe's governance flow + EGT (asset upload → brand check via context → annotation → JIRA ticket, no chat, demoed live lines 674-770) is a working instance of the blog's "there waiting, sometimes no chat, form follows surface" pattern (blog line 28). Proof Pedro's framing is right.

**Scope reality (Pedro's catch, confirmed in transcript).** "For all our agents" = Daniel's narration (line 52), not demoed. Real consumers demoed = (1) **website-generation** (Florian/Quentin — a content-gen effort, NOT one of Pedro's 6 agents) + (2) **Governance Agent** (Philippe). Of Pedro's 6-agent portfolio, **only Governance touches EGT today.** No Discovery/EPA/EDA/Content-Opt/Modernization integration shown.

**Contribution-model gap = genuinely unowned (Cedric Huesler, lines 1030-1162).** Cedric pushed hard: who manages the context, and where's the feedback loop from consumers back to the source — *"the risk of not providing a feedback loop is that customers will fork it... think of Git... branch it off... the context is not a static thing, it's a living thing."* Room answered vaguely (anonymous CR-BASL voice, "yeah I fully agree"), nobody claimed it as a product lane. NOTE: this is the contribution loop for *context* (EGT's gap), adjacent to but not identical to Pedro's *skill-curation* convention in the blog. Related lever, not the same thing.

**Skills-vs-flows debate (Pedro's fragmentation concern, live).** Michael Marth (VP Eng Basel) challenged Philippe (line 1218): *"why are flows not simply skills? Otherwise 2 concepts, 2 implementations for the same thing."* = Michael Marth = natural ally for Pedro's converge-on-a-standard position. Philippe defended flows as a distinct layer (skills costly, let customer choose, lines 1376-1392). Cedric Huesler (line 1400): *"don't conflate UI with execution"* — NL to describe, execution optimizable to Python. BCN-room customer-facing eng (line 1356): customers don't want wizard-style workflows.

**Moves (revised 2026-05-29):**
- **Ian** — drop "does EGT encroach" (it doesn't). Ask instead whether the skills + surface-consistency layer is a recognized *distinct product job*, and whether Pedro's expected at the flywheel workshop. Draft (Pedro's plain EN, Slack, neutral): *"Quick one on your North Star. Is Enterprise Ground Truth supposed to be the single context layer all AEM agents use, or one source among many? And is making every agent consume context the same way one job, or a separate layer on top of EGT? That second part looked like nobody owns it yet."*
- **Bertrand** — position the blog's lane (skills declaration + surface consistency) as a separate product job; ask to be in the **flywheel workshop next week** (Daniel announced it, line 56).
- Do NOT attack Philippe frontally (competitor frame: he makes you applaud — work via Ian/Bertrand).

---

## May 12 — Ian's AOv2 decision (Conrad delegated) — DECISION-GRADE, closes "discussed not decided"

Source: #aem-agents (`C09J94L2TAR`) Ian Boston post 2026-05-12 08:18 CEST. Aligned with Carsten Ziegeler. cc Jaclyn Eckersley, Yanira Castaneda. *"Conrad has delegated a decision on AOv2 to me."* This is the Conrad forcing-function directive memory had been awaiting since Apr 29 ("V2 = direction, discussion not decision"). **Now decided** (Conrad → delegated to Ian → Ian posted + Carsten-aligned = decision signal per [[feedback-proposal-vs-decision]]).

**The decision (verbatim-anchored):**
1. **Skills-first.** Develop skills first; create MCPs only if required by the skills; create agents only where a skill cannot achieve what's required.
2. **Harness-portable.** Aim to run skills in any harness; do not limit to a single harness.
3. **Adoption-gated harness support.** Support the harnesses customers show usage of for AEM agents; invest effort in a harness only where there's proven AEM-agent usage.
4. **Minimal AOv2 investment until proven BU value.** *"Until there is proven value to AEM BU we should not invest more effort than making the AOv1 agent manifests available as is to AOv2."*
5. **A2A dead.** *"We should not invest further in A2A since no customers have leveraged it."*

**Resolves prior open items:**
- Forward-path commitment to AOv2 — was open → now: skills-first, harness-agnostic, AOv2 support adoption-gated (not a blanket bet).
- A2A decommission — was "direction/timeline open" → now: no further A2A investment, confirmed dead.
- MCP-vs-skills tension — resolved toward **skills primary, MCP subordinate** (Trent's Apr 29 skepticism wins over Bertrand's MCP-first).
- The decision-maker question — Conrad delegated to **Ian** (not Trent, who disclaimed authority Apr 29).

**Strategic read for Pedro:** the decision is the architecture floor his blog sits on. "Skills run in any harness" + "support harnesses where customers show usage" = exactly why the selection + consistency layer (his lane) matters: if skills are portable and harnesses are adoption-driven and plural, someone must make the right skill be there-waiting and keep surfaces consistent. Ian's directive validates the premise; Pedro's blog answers the consequence. Cite it that way to Bertrand.

---

## May 28 — Eugene + Silvia DM: the consistency MECHANISM surfaces (A2UI + a2ui-components)

Source: 3-way group DM Eugene Bannykh + Silvia Mulet Ferre + Pedro (`C0B6MF94L3V`), Eugene 2026-05-28 20:41 CEST. Pedro has NOT replied yet. Ingested 2026-05-29.

**Eugene's message (reacting to Pedro's blog + Ian's North Star):**
- Validates the distributed direction: *"a sober direction, since AEM teams want to move fast and don't want to give autonomy away."*
- Insists consistency must hold in **both UI/UX and skills/memory**.
- **The mechanism:** decouple the chat components from AO into their own monorepo, e.g. `@adobe/a2ui-components`; each harness takes it as a dependency.
- **Distributed harnesses adopt the A2UI spec as a common protocol** → testable, guarantees the design system is implemented identically. Example: an Asset card renders the same in Experience Workspace and in Content Hub.
- Design team is already prototyping with AO chat components + skills, exploring how designers influence agentic output and **could own the components + contribute to that shared repo**.
- Ends *"What do you think?"* → open ask to Pedro.

**Why this matters — resolves the "consistency = asserted, no mechanism" open verify.** Pedro's blog asserted "every chat must feel like the same chat" with no mechanism; the May 28 consistency-layer working thesis hypothesized "portable, harness-agnostic, design-owned component lib + light contract." Eugene just named it: **`a2ui-components` (the shared lib) + A2UI spec (the light contract)**, explicitly **decoupled from AO** = harness-neutral, protects optionality (Loni "not at the mercy of someone else"). Reconciles with the earlier brick-box note: Quarry = general shared UI components; **a2ui-components + A2UI = the agent/chat-specific layer on top**. Also connects to Guliz's "new A2UI components" mention in the Apoorva thread (reply 1) — A2UI is becoming the shared design-side answer.

**Division of labor crystallizing:** Design (Eugene/Silvia) builds the component contract (a2ui-components + A2UI); Pedro owns the product framing (surface inventory/map, which surfaces, which skills, what we tell customers — the lane he claimed publicly the same day). Clean split, not overlap. Eugene/Silvia asking "what do you think" = they want Pedro as the product owner of this.

**A2UI = confirmed (researched 2026-05-29).** **Agent-to-User-Interface — Google's open standard**, launched ~Dec 2025, v0.9 by 2026. Agent emits a declarative JSON describing components + data model; the client app renders with its OWN native components (React/Angular/web components/Flutter/SwiftUI). Three independent layers (structure / state / rendering). Security: no executable code sent, only JSON → client renders local components (anti-injection, full appearance control). **Framework-agnostic + portable by design.** Competes with MCP-UI / MCP Apps (Anthropic) and ChatKit (OpenAI) — "agent UI standards are multiplying." Adobe-internal framing: Cedric Huesler (2025-12-18, #aem-agents) flagged A2UI + MCP-UI as the rendering standards big public LLMs would adopt by mid-2026. Guliz (Apoorva thread) = design team already building "new A2UI components." Repo: github.com/google/A2UI.

**Strategic implications:**
- A2UI is **harness-neutral by nature** (open standard, any client renders) → confirms Eugene's proposal = the harness-agnostic light contract Pedro hypothesized. The "is it tied to AO" question is moot.
- **Portability answers Apoorva's "customers ditch us for Claude" fear:** if AEM agents describe UI via A2UI, the brand/design consistency travels into external harnesses (Claude/ChatGPT/Gemini) too. The component contract is what keeps the experience consistent when a skill runs anywhere. Strongest argument for owning this layer.
- **Real product question = standard selection, not neutrality:** A2UI (Google) vs MCP-UI/MCP Apps (Anthropic). Customers run AEM skills in Claude (Anthropic/MCP) → betting only on A2UI may miss the MCP-UI surface. Bet on A2UI, support both, or wait? = the sharper question for Eugene.

**Post 2 draft written (2026-05-29):** `AAI - Project Folder/One AEM, Many Harnesses.md` — follow-up to "From North Star to There Waiting", develops the consistency layer with the mechanism (A2UI-or-MCP-Apps rendering contract + design-owned shared component lib + product-owned surface map + contribution loop). Held as PROPOSAL, A2UI-vs-MCP-Apps open. Status: draft. **Review crew before publish:** Silvia + Eugene (mechanism), Bertrand + Gilles + Ian (the 2 open calls: contract choice + one-surface-vs-several). Plan: share as unpublished Confluence draft (Pedro creates — Confluence PAT still 401 for Claude), fold reviewer input, publish before June 1 Agent Owners agenda. Pedro promoted post 1 in #aem-p42-leadership as June-1 pre-read + teased post 2 (with Silvia/Eugene named) 2026-05-29.

**⏳ OWED:** reply to Eugene + Silvia (drafted + posted 2026-05-29) — affirm the decoupled shared-components + light-contract direction, connect to the surface inventory Pedro claimed publicly, make the portability-answers-Apoorva point, and ask the standard-selection question (A2UI vs MCP-UI, bet/both/wait) + the contribution-model question (who reviews/merges the designer-owned component repo — parallels the skill-curation contribution loop). Pedro pastes himself ([[feedback-never-send-slack]]).

---

## May 28-29 — Apoorva AOv2 entry-point Slack thread (Pedro publicly named harness-strategy owner)

Source: Slack `cq-dev` #C09J94L2TAR thread, parent ts 1779983847.809839 (Apoorva Gupta → Bertrand, 2026-05-28 17:57 CEST, 16 replies through 2026-05-29 10:26). cc Guliz Sicotte, Prashant Jain, Ankur Arora. Ingested 2026-05-29.

**The ask (Apoorva):** *"what is the approach agent teams are taking on AO v2... I was told AI Assistant may just continue being on v1, and v2 will be on a newly built separate UI (marketplace of skills). Where are AEM agent teams supposed to pursue their investment? v1 or v2? AI Assistant or this new UI?"* The undeclared-AOv2-posture problem (memory passim) surfacing as open confusion among agent PMs.

**🟢 VISIBILITY ARTIFACT — Pedro named as harness-strategy owner, in public, next to the architect.** Silvia Mulet Ferre (reply 3): *"Ian Boston and Pedro Ferreira are working on the AEM strategy for the future of LLM harnesses."* Said to Apoorva + Guliz + Prashant + Ankur. Senior-Director-grade — Pedro positioned as co-owner of the AEM harness strategy by a peer (Adobe Design manager), unsolicited. Bankable for promotion narrative.

**🟢 Ian cites Pedro's blog as the decision reference (3rd public citation).** Ian (reply 13), on how to handle a skill that depends on another skill: *"1. Add the skill to the harness. (PM decision, see @Pedro Ferreira's blog post)."* The architect routes a live product decision to Pedro's billet. Adds to the May 28 Ian-cites-blog-twice record — blog is now the canonical reference on skill/harness composition.

**🔴→opportunity DEMAND SIGNAL — Apoorva screams the exact problem Pedro's consistency/selection layer answers.** Reply 6: *"'harness where we see adoption' is very broad and a chicken/egg scenario... Many AEM agents/skills require interop with other CXO agents/skills, and if every CXO app is driving adoption on a different harness + conversational surface, how will customers even decide where to go, shouldn't it be aligned at CXO level? they may just ditch us (our UIs) in frustration, and leverage our skills via Claude directly."* This is the customer-fragmentation + selection problem Pedro's blog scopes. A peer PM voicing the demand = pull for Pedro's lane, not push.

**Headline data point (Silvia, reply 14) — cross-agent usage is real and measured.** Analyzing real AO1 usage in AEM: *"Users naturally prompt cross-agent workflows and intents. For example AEM users on EH prompt asking about Audiences (16%)."* 16% of EH prompts are cross-agent (Audiences = AEP/CDP domain). Hard evidence for cross-product skill interaction + the consistency layer. Usable EH and AAI, deck-grade.

**Meeting on Pedro's exact topic — May 29 (today).** Silvia (reply 14): *"as we are meeting tomorrow we can discuss keeping experience and UI consistency across 'the different adobe harnesses' and 'cross-product skills interaction.'"* Posted May 28 → meeting = May 29. ⚠️ OPEN: is Pedro in this meeting? It is literally his consistency-layer lane. Confirm + get in if not.

**Ian's distributed-model reinforcement (replies 13, 16) — cost/accuracy argument against monolithic harness.** *"The problem with a monolithic CXO-wide harness that knows everything is the same problem causing low quality for most AOv1 agents and poor performance... determining intent falls in accuracy very fast."* Plus token-cost: *"Adding lots of MCPs/A2A agents to a reasoning loop is 10-100x more expensive... compaction is lossy."* Refs his Claude-token-costs blog (wiki 3894008282). Backs the distributed-harness + context-specific-skills model = the foundation Pedro's consistency layer sits on. Ian: *"Skills are transportable between harnesses."* Skill-dependency options: (1) add skill to harness [PM decision = Pedro's blog], (2) call over A2A.

**Other voices:**
- **Guliz Sicotte:** not investing design capacity on v1; reusing patterns in v2 + new A2UI components; Silvia working with CXUE. v2 = UIs generated at runtime based on task/intent, not rigid renderer forms (but still wants guidelines to control visual expression — aligns with Pedro's consistency layer).
- **Gilles Knobloch:** EPA = moving to skills (AOv2-ready) while plugging into AOv1 agent. Concrete migration pattern. AI Assistant still the UI, no v2 ETA.
- **Ian:** not aware of any AEM agents in "AI Pods"; AI Assistant not heard to be moving to v2; "a number of projects working on a UI decoupled from AOv2."
- **Andreea Miruna Moise:** confirms divergent entry-point paths; roadmaps need to accommodate; pick what advances faster. Reinforces the alignment gap Apoorva raised.

**Moves:** (a) confirm attendance at Silvia's May 29 consistency meeting — this is Pedro's lane being defined without confirmation he's in the room; (b) the 16% cross-agent EH→Audiences stat → pull into May 11 deck + EH narrative; (c) Apoorva's "ditch our UIs, use skills via Claude" = quote-anchor for why the consistency/selection layer matters (adoption-protection framing, ties Loni "not at the mercy of someone else"); (d) Silvia naming Pedro+Ian as harness-strategy owners = log toward promotion evidence.

**🟢 FOLLOW-UP — Pedro replied + claimed the lane publicly (2026-05-29, posted ~11:30 CEST).** After Apoorva pushed back (skills-selection "not the big deal"; the real gap = fragmented UIs / entry points; "who in AEM Product drives UI convergence or even an inventory of all the UIs"), Pedro posted (pasted by hand — see [[feedback-never-send-slack]]):
- Reframed convergence as the *open product question* (one surface vs several depends on personas/use-cases — decide deliberately, don't assume), NOT a verdict.
- **Claimed the lane in public before Bertrand:** *"This is the piece I think AEM is missing, and honestly it probably sits with me given Experience Hub. I'd start by pulling the surfaces and entry points into one map... working from the teams since no single person has that view today. @Bertrand, if you agree it's mine to drive, I'll take it."*
- Skills-per-harness = no fixed number, shared call between architecture (Ian) + each team, budget not a hard cap.
**= PROMOTION MARKER.** Pedro publicly volunteered to own the cross-surface map/convergence lane, in front of Bertrand, in a Loni-adjacent channel — broadcast-rep + cross-surface scope claim. Log to Promotion Strategy ([[reference-promotion-strategy]]). Turned "I don't have the info / pas trop envie" into the rationale (nobody has the consolidated view = the gap = H-005 substrate logic).
**⏳ OWED DELIVERABLE (conditional on Bertrand confirming ownership):** a first-cut **inventory/map of AEM agent surfaces + entry points** (Experience Hub, Experience Workspace, Modernization, Coworker, Fruitbar, AI pods, ...) — what each is for, where each agent shows up, what we tell customers. Pedro framed it as "first cut" / convening the teams, not a finished artifact he already has data for. Watch for Bertrand's reply blessing/assigning ownership before committing build effort. Ties directly to the consistency layer (`Consistency Layer — Working Note.md`) and EH-as-selection+consistency-layer narrative.

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

## May 6 — MCP MOC report shipped to Bertrand (acked)

Pedro shipped first MCP report MOC 2026-05-06. Slack to Bertrand: *"starting to work on MCP reporting with @fdelval. Aiming for a report what would look like this. Still refining on my side, but gives you the direction. Once I'm fine, will review with stakeholders/agent owners. NB — those are numbers Claude invented for the report template based on the splunk data. Not connected, not validated."*

**Bertrand acked.** Direction validated.

**What it confirms:**
- Pedro's report-design lane (Felix May 6 split: Pedro = design, Felix = Splunk extraction)
- "Tool Calls" terminology landed via MOC layout
- Iterative MOC-first posture (same pattern as Briefing v0 April 30)
- Stakeholder/agent-owner review GATED on Pedro refinement + Felix real-data connection

**Next:** Felix + Tanju Splunk extraction → replace Claude placeholders → review with Yanira / agent PMs / Conrad TBD.

---

## May 6 Namita 1-1 — Mapping owners + Langfuse path + master-list signal

Source: `Meeting Notes/Namita 1 1/20260506 - Namita Pedro 1 1 .md`. ~14 min EN. 5 of 5 walk-outs hit.

**Material signals:**

1. **AEM Grafana mapping = Jabin (creator) + Raul (editor), manual SQL.** Closes NYL data-freshness diagnosis. Pedro lane: refresh + automation.

2. **Internal-user exclusion = "technical accounts, copilot engine"** — Namita pasted in chat. Add to Felix Postgres filter.

3. **V2 reporting path = Langfuse + Claude skill bridge.** Ilya's team building skill to join V1 (Rubin / analytics DB) ↔ V2 (Langfuse). V2 data substrate ≠ V1. Access via Ilya or Alex (TBD — Saar or AEP eng).

4. **🚨 Customer master-list gap = org-wide.** Namita verbatim: *"Nobody seems to have that golden source of truth. Lists for AEP somewhere, lists for AEM. That consolidated list — something we need to nail sometime."* Same diagnosis as NYL thread. **Senior-Director-grade lane** if Pedro proposes consolidated source — cascades to NYL + Felix mapping + Rubin + Namita TBYB list.

5. **Rubin (Namita) = passive posture.** Data Science team builds. Open to AEM custom on request.

6. **Connection warm.** Slack DM open, *"happy to be in the loop"* on V2 reporting.

**Implications:**
- NYL Bertrand 9 AM Slack May 8 sharpens with Jabin+Raul + master-list framing.
- Ilya focused 1-1 needed (Langfuse access + V1↔V2 bridge + Rubin V2 future).
- Felix loop on Langfuse layer (missing piece for V2 internal traces).
- Master-list 1-pager = candidate Senior-Director-grade artifact for pre-May-11 Bertrand pitch.

---

## May 6 Yanira Slack thread — AEM Agents AOv2 Migration Workshop

Source: Slack thread launched by Yanira Castaneda 2026-05-06 18:03. Channel TBD (likely AEM agents broad). Pedro CC'd. Tag groups: @agent-owners-engineering, @agent-architects, @agent-owners-pgm, @agent-owners-product.

**Material content:**

1. **Workshop = Phase 2 (Evaluate) operationalized.** Reinforces 5-phase plan validity. Fills AC42 alt-forum void (Felix Delval exited AC42 May 5).

2. **Felix Meschberger (NEW high-signal voice):** *"agents should migrate to Skills+API and leave the build-out and operation of the agent harness to someone else — in AEM or AOv2 TBD."* 100% aligned with Pedro's Slide 2 ownership boundary. **Quote anchor candidate for Slide 2.** Asked Yanira for workshop content/success criteria. Distinct from Felix Delval. TBD title/org — confirm with Bertrand.

3. **Carsten Ziegeler shifted** from MCP-first (Bertrand 1-1 May 5) to skills+API alignment (Yanira thread May 6: *"Right, fully agree"*). MCP-vs-skills tension resolving toward skills-direct-API.

4. **A2A decommission direction reinforced.** Conrad (April 29) + Felix Meschberger (May 6) converging: A2A integration is "fragile path." Slide 3 fork moves from "open" to "directional."

5. **Felix Delval workshop framing:** register current agents AS-IS on AOv2, observe. **No evals in AOv2 ATM** → AEM eval-surface lever reinforced.

6. **Timing:** early PST proposed (Ankur Arora India + Jason Weaver DRM both asked). Early next week.

**Implications for May 11 deck:**
- Drop "Felix vs Carsten" tension narrative — consensus emerging.
- Replace with: skills+API consensus + workshop next week = visible momentum.
- Slide 2 quote anchor consideration: Felix Meschberger as alternative to Bertrand line.
- Slide 1 Phase 2: reframe from "EPA staging test (Felix-led)" → "AEM Agents AOv2 Migration Workshop (Yanira-led, all agent teams)" — broader, all-agent.

**Continuation (Ian Boston + Felix Delval, 2:02 PM onwards):**

- **Ian Boston conditional pro-MCP:** if AOv2 = one of many harnesses, MCP has OAuth-onboarding adoption advantage vs API bearer-token friction. Re-opens MCP-vs-skills tension on different axis: skills = build path consensus, MCP = exposure surface for external harnesses. Both can hold.
- **2-5% conversion data point (NEW)** — Ian: *"At the current levels of adoption we are seeing 2-5% conversions of most agents input funnels resulting in use."* Headline-grade for May 11 deck. Adoption-first reframe: *"unless AOv2 can change that, we should be looking at eliminating friction blocking inputs to the funnels."* Aligns with Loni's "we cannot be at the mercy of somebody else."
- **Yanira routes architect decision to Monday Architects call (Conrad-led).** Distinct venue from migration workshop. Ian misses (Basel SR workshop). Carsten + Conrad attending.
- **Felix Delval AOv1-unworkable brief:** staging hard to test, local deployment unmanageable, agent paraphrases user prompts, no local E2E for UI components. Plus product push to move forward. Plus *"AO2 also takes care of Orchestration, I don't think we have looked into AO2 with the prism of orchestrating the current functionality."* New evaluation lens: AO2-as-orchestration. Add to Phase 2 workshop scope.

**Refined deck implications:**
- 2-5% conversion = potential headline number (confirm w/ Ian + Yanira pre-deck)
- MCP friction-elimination angle holds alongside skills consensus
- AOv1 unworkability = Phase 4 Go-vote ammunition
- AO2-as-orchestration = new Phase 2 dimension

**Continuation — Carsten proposal (2:41 PM, NOT decision):**
- *"AOv1 has most likely not the future, no customer showed interest in A2A, nearly no relevant AI product supports A2A out of the box. Continuing with A2A does not make sense. It complicates our setup and does provide zero value. Focusing on MCP/API to provide the required basics and then adding - if required - skills on top seems to be the way forward."*
- **Proposes A2A retire + AOv1 sunset + MCP/API base + Skills-on-top layered model.** Decision pending — gated on Conrad directive + Phase 4 collegial.
- AOv2 + Claude + other AI products support MCP/API per Carsten → ecosystem-fit argument.
- **Direction emerging across architects** (Felix Meschberger + Carsten + Ian + Felix Delval positions converging in workshop thread). NOT alignment achieved. Capture as "direction emerging, pending decision venues."

---

## May 6 Felix 1-1 (~25-min FR sync)

Source: `Meeting Notes/Felix Pedro 1 1/20260506 - Felix Pedro 1 1.md`. Felix + Pedro.

**Material signals:**

1. **MCP scope CLARIFIED.** Customer use of MCP on **non-Adobe surfaces (ChatGPT / Claude)** = reaction to AEM agents. NOT internal AEM agents calling MCP. Felix forced clarification: *"MCP je suis allergique à ce mot là."*

2. **Pedro ↔ Felix MCP work split.** Pedro = report design (manual first on EDS, validate, automate later). Felix = Splunk extraction layer via Splunk MCP server → side Postgres DB.

3. **Apples-vs-oranges rule for Loni/JM (terminology locked Pedro 2026-05-06):**
   - Use **"Tool Calls"** — NOT "interaction" or "invocation" — for MCP. Pedro chose this from Felix's hit/tool-call options.
   - Cannot compare agent interactions vs MCP Tool Calls on same chart
   - Cannot do per-agent MCP breakdown — tools tagged, not agents
   - Felix: *"Pour moi le seul truc qui doit être clair quand tu le montres à Loni c'est que tu compares des oranges et des pommes."*

4. **Splunk 90-day window** = constraint. Felix dumps to side DB to maintain history beyond ~2026-02-06.

5. **Multi-turn flow breakage = NEW EPA product gap** 🔴. Surfaced via Amine (Felix eng) auto-categorizing weekly CSVs with Claude. Many at Summit hit it.

6. **Amine pattern = reusable per-agent value indicator pipeline.** CSV → Claude auto-categorization → ticket creation. Extends Lara/Governance pattern. Candidate for Tier-2 reuse (Brian / Greg / Apoorva).

7. **DB redesign:** SQLite → **Postgres + LLM-as-Judge layer**. Engineers connect to central DB this week.

8. **VPC / Ethos IP-range blocker** — Felix's range marked in-use months. Ethos cleanup ticket created. Pedro to share Ethos contacts if any.

9. **AOv2 — Felix at 8/10–9/10 going.** *"Ce n'est pas le problème, c'est la gravité."* AEM has no own-orchestration eng team, management won't fund one → AOv2 evident. Question = when (2 weeks vs 2 years), not if.

10. **Reporting strategy:** Felix recommended manual report first → automate later. Reverse-engineer from desired report.

**Risk flags:**
- R1 🔴 Apples-vs-oranges. Deck must enforce hit-not-interaction rule.
- R2 🟡 Splunk 90-day window time-sensitive — backfill needs to start now.
- R3 🟡 Per-agent MCP breakdown impossibility. Bertrand asked for client + agent split. Manage expectation. Confirm w/ Namita tonight.
- R4 🟢 Felix takes MCP extraction layer.
- R5 🟡 Multi-turn breakage = real EPA pain.
- R6 🟢 AOv2 8/10–9/10 reinforces 5-phase frame.

---

## May 5 Bertrand 1-1 (~20-min FR sync)

Source: `Meeting Notes/Bertrand 1 1/20260505 - Bertrand Pedro 1 1_otter_ai_transcript.txt`. Two named speakers (Pedro + Bertrand), rest Unknown — attribution by content.

**Material signals:**

1. **AOv2 5-phase plan VALIDATED 🟢** (Bertrand 8:27 verbatim): *"AoV2 a l'air prometteur. Plutôt pour faire une évaluation. On demande aux équipes de faire des évaluations de migration et de workload. On collecte. Puis après on décide collégialement."* Matches Pedro's 5-phase exactly. Slide 1 + Slide 2 boundary content validated.

2. **Slide 2 (Ownership) — Bertrand additions to AOv2-owns column:** Telemetry + UI. Slide framing preference: *"plus une guidance que d'une finition pure et dur."* PPTX + KR3 deck note updated.

3. **MCP workstream → Bertrand owner.** *"Je vais m'occuper des MCP."* Closed from Pedro's plate. Pedro tracks but doesn't own.

4. **MCP-in-reports — new ask cluster.** OKR review yesterday: JM + Loni "particulièrement en forme." Contrast surfaced publicly: agents low usage vs MCP high usage. 170K April calls flagged. Bertrand wants client-level breakdown — internal vs external, customer names. Same depth as agent-level reports. **Tomorrow Namita 1-1 = direct lever** (she owns AI Assistant Dashboards / AI Integration / AI quality + AOv2 AIA extensions). Briefing v0 sections 5-6 candidate.

5. **Customer-level use-case reverse-documentation — new analytics direction.** Bertrand: *"Microsoft utilise des outils A et B → use case probablement X. Est-ce qu'on peut rétro-documenter?"* Push beyond macro consolidation. Identify top-3 engaged customers ("3 clients qui ont vraiment mordu à l'hameçon"). Method TBD with Felix.

6. **Mithril / Coworker — NEW SURFACE launching ~late May (T-25 days).** Joshua Hailpern's team. "Mode rail" = AI Assistant V2 (observes screen, suggests). Pedro saw via night Slack May 4. **AEM Sites NOT in Mithril** — repeat exclusion (also Modernization, Experience Workspace). Bertrand: *"Ça va être un point important pour la migration AOv2 si on y va."* Bertrand surprised no XD / Guliz in loop — actioned: chase with Guliz. Marcus Räck (Experience Workspace creator) declined Pedro's unified-chat ask. 4 chats now (Experience Workspace, Modernization, Slick, Rosetta). Pedro got Cédric Huesler annoyed via Slack push.

7. **MCP vs skills-direct-API tension.** AOv2 platform agents rewritten WITHOUT MCP. Felix pro-skills-direct-API. Carsten pro-MCP. Conrad "modérément…" Pedro: *"Si entre Carsten, Félix et Ian ils pouvaient au moins être d'accord."* Bertrand handles. Critical for May 11 deck.

8. **Felix EXITED Architecture Committee 42** 🔴 — *"P42 ça se passe je vais même plus parce qu'on n'avance pas."* Cross-agent leadership void Pedro flagged today now operationalized as forum disengagement.

9. **June Bucharest workshop (Alex Saar host)** — Bertrand 1h opener, prep pending, agenda on wiki. Adjacent venue for Pedro coordination role since AC42 stuck.

10. **Loni+JM May 11 agenda** — Bertrand still working out structure ("il faut refaire l'ancien weekly"). Pedro can propose section ordering.

11. **EH-side drop-ins:** Bertrand asked Sorin + Eugene to do **Mithril review**. **Sylvia Mulet Ferre launching auto-fix-prompt initiative for EH** — Bertrand skeptical: *"je sais pas trop où elles vont venir avec ça."* Customer migration: 1-year migration pattern, decouple "platform update" vs "platform move." Nico's content-repo migration waking customers up.

**Risk flags:**
- R1 🔴 Felix exited AC42 — cross-agent leadership void worse than Pedro knew this morning.
- R2 🔴 Mithril launches T-25 days WITHOUT AEM Sites. Repeat AEM-exclusion pattern.
- R3 🟡 MCP vs skills-direct-API: Felix + Carsten + Ian + Conrad don't agree. AEM platform agents written WITHOUT MCP contradicts AEM's MCP-first investment.
- R4 🟡 Bertrand customer-level reverse-doc ask = scope-expanding. Felix already stretched.
- R5 🟢 Pedro gained ground: 5-phase plan validated, MCP off plate, boundary slide validated with 2 additions.

---

## May 5 Felix 1-1 (33-min FR sync)

Source: `Agent Owner Alignement/20260505 - Felix Pedro 1 1.md`. All "Unknown Speaker" — attribution by content. Felix in self-described "cahier de doléances" mode.

**Material signals:**

1. **BVR critique — must add banner before May 11 deck.** *"BVR à 100% veut rien dire, BVR à 0% veut dire quelque chose."* Treat like temperature/pH (relative, not %), NOT comparable across agents OR across BVR categories. Calibration baseline: week-before-Summit (near-100% internal `am-sitestrial` tests) vs Summit week (real users). Self-aware: *"si ça monte je demande promo, si ça monte pas je montre autre métrique."* Felix adds banner to Value Realization section. Per-agent custom indicator pattern (Lara/Governance brand-checks/month) extends to EPA + Discovery.

2. **AOv2 — pro-V2 via staging test, anti-V2 via blind trust.** *"Tous les agents owners il n'y a personne qui se fie de l'équipe d'AEP. Gilles se fit pas, moi je me fie pas, Corey se fie pas."* Conrad/Trent/Carsten "hors sol." Conrad "enthousiaste" to V2. Ken Russell team NOT prod-ready, IS staging-ready. Felix recommendation: launch staging migration test AS OF TODAY on real AEM agent. *"Tant qu'on n'a pas fait ça en staging, on n'a pas fait grand chose."* Risk of moving = maigre. Risk of NOT moving = bigger.

3. **Gradial competitor on EPA — NEW signal.** *"Beaucoup de gens vont nous voir: vous implémentez pas ça rapidement, on passe sur Gradial."* First explicit competitor name in AAI lane. Speed argument for V2. **Confirm with Corey + Yanira before May 11 deck commits to it.**

4. **Cross-agent technical leadership void — Felix's main grievance.** Conrad/Trent/Carsten "hors sol." Different repos / archis / observability (Splunk vs Longfuse). "Agents owners vont pas dans meetings d'autres agents." *"AOA est mort parce que l'orchestration est nul à chier."* Felix ask: non-mandatory best-practice guidelines by architects seeing multiple projects. Repeats 22:10: *"il manque du leadership technique sur les agents."* Felix invites Pedro to co-sponsor with Bertrand. **Senior Director-grade move if Pedro picks up. Frame as PM coordination layer, NOT architecture.**

5. **Infrastructure moves this week.** OneAdobe repo migration — Felix grants Pedro access tonight US-time. Domain move next week. VPC for DB next (bureaucratic, slow). PR merging this morning — AEM-agents-report extraction tool, separate weekly DB, env-var configurable.

6. **Loni/JM endorsement.** Felix: *"Je crois qu'il faut qu'on fasse un rapport pour Loni Jean-Michel pour la semaine prochaine avec plein de chiffres."* Offered to recheck numbers.

7. **Namita validation.** Felix on Namita: *"elle parle l'humain comparé à certaines personnes."* Validates Wed May 6 1-1 bet.

**Risk flags:**
- R1 BVR % in Briefing v0 = interpretability risk. Banner before May 11 deck.
- R2 Pedro-as-AO-liaison exposure. Don't argue AEP framing in front of agent owners — route through Bertrand.
- R3 Gradial unverified — confirm Corey/Yanira pre-deck.
- R4 Cross-agent leadership void = real opportunity. Don't overstep Conrad/Bertrand turf.

---

## Open vault gaps (still tracked)

- Stakeholder Map Vaishnav entry (held until Wed May 6 confirmation)
- Pre-meeting strategic brief for May 11 Loni + JM (draft week of May 5)
- Briefing v0 sections 5-6 (pending Indicator #8 on May 17)

---

## May 12 — Mithril Silvia ↔ Tim Lynn exchange + Pedro outbound DM

**Event.** Silvia Mulet Ferre (Eugene's manager, Adobe Design / Guliz tree) opened a public thread with Tim Lynn (Mithril project owner) on Mithril clarifications. Three confirmations + one open ask Pedro can answer.

**Confirmations from Tim Lynn:**
- **Mithril = AO2 only.** Not AO1. *"we're aiming to have things wired up e2e by end of may. parts of the api have been committed to our new UI repo and AO, but the shell side is still WIP."*
- **Context-reading not default.** Use-case Silvia described (assistant reads open page + full context without manual user input) requires per-page/app tooling that registers itself with Mithril in the DOM-tools pattern. Reference demos = "edit schema" + "pueblo".
- **Skills authorship unclear.** Tim didn't know whether end-users or internal Adobe teams create skills — likely AO team question.

**Silvia's open ask (Pedro = answer):** *"with who can we connect (PM, eng) to make sure context-reading is part of AO2 & Mithril?"* for AEM.

**Pedro outbound DM 2026-05-12 (EN, Slack).** Identified self as AEM-AO PM liaison (Bertrand-named April 14). Confirmed alignment between Silvia's context-reading ask and EH foundational primitive. Proposed division: Silvia drives Adobe Design side (Tim + Guliz), Pedro drives AEM PM side (Sergey Generalov + Conrad Woltge). Joint ask = **context-reading as a Mithril primitive, not per-app re-implementation.** Asked for 15 min this week. Looping Eugene.

**Why this matters:**
- Bertrand May 5 action — *"chase Guliz on XD/Adobe-Design loop visibility"* — materializing. Silvia (Guliz tree) operating directly with Mithril. Loop visibility is happening; Pedro inserts as the AEM-PM pole.
- Pedro's AEM-AO liaison mandate now operational at PM-to-PM-counterpart level (Adobe Design Sr Manager → AEM PM) on a high-leverage primitive, not just at AO PM↔PM (Sergey).
- Context-reading = same primitive Pedro pushes on EH Priority 1 (Skills+MCP surface) with Eugene. Adobe Design + Pedro aligned ask = stronger together than either alone.
- End-of-May Mithril e2e wiring = T-19 days. Window to influence Mithril primitive list is now, not after launch.

**Posture (hedge — confirmed Pedro 2026-05-13):** AEM has **not yet committed to AOv2.** ~90% probable, **progressive**, internal resistance still active. Conrad directive imminent but not landed. Pedro's ask to Silvia is **purely architectural** (primitive vs per-app), **decoupled from AEM AOv2 commit timeline.** Architecture ask remains valid for any Mithril consumer regardless of when AEM moves. Knowledge entry promoted: leadership/ "Decouple the Architecture Ask from the Platform-Commit Timeline" 2026-05-13.

**Bertrand FYI Slack v2 (FR, drafted 2026-05-13, NOT YET SENT).** Adds hedge paragraph: *"je n'ai rien committé sur le timeline AEM. L'ask est purement architectural (primitive vs re-impl par-app), décorrélé de notre évaluation AOv2 en cours (workshop Yanira semaine prochaine, directive Conrad imminente)."* Send-or-wait gated on user confirm.

**Bertrand FYI Slack drafted (FR, not yet sent).** Quick informational note referencing his May 5 action, confirmations from Tim Lynn, Pedro's outbound move, division of labor. No ask. To send when user confirms.

**Open:**
- Awaiting Silvia reply on 15-min slot.
- Tim Lynn = new stakeholder (Mithril project owner, doc author). Org chain TBD — confirm.
- Skills authorship question (end-user vs internal-Adobe) still unresolved — route to Sergey when contact lands.

---

## May 14 — Corey 1-1 (call HELD; was scheduled May 19)

**Reconcile.** Earlier memory said "call lands Tue 2026-05-19." It actually landed **Thu 2026-05-14** (Corey rescheduled earlier; on Pedro's day off, ~23 min, EN). Source: `Meeting Notes/Corey 1 1/20260514 - Corey Pedro 1 1 .md`.

**What landed:**
1. **Decision — new from-scratch simple EPA report, not a retrofit of the multi-persona report.** Corey: define the 4 (up to 10) key metrics he wants, build clean, drop the old report if the simple one suffices. Pedro confirmed persona-scoped (Corey = key persona), Claude Code generates it (low effort). **Corey committed to send metrics in plain English same day (May 14).**
2. **Cosmetic principle:** drop tables that duplicate a chart's visual; hard-collapse.
3. **VR-per-agent loop set:** single DB (Copilot + external) across agents; Felix most advanced on Sites VR; other agents' use cases too spread for one number → split per agent, maybe umbrella later. **Corey workflow:** his team collects EPA VR defs → wiki → sync Pedro → integrate. Pedro accepts one plain-English high-level def to start.
4. **MCP double-count flag:** Corey said EPA uses the content MCP → Gilles' ~1.2M Splunk call number (shown Loni+JM) likely double-counts. Pedro continuing DAS/Databricks tool-call filtering (off noisy Splunk pings/responses). Not urgent for Corey but EPA scaling MCP focus going forward; usage low today; tool calls skew to lists not actions (governance).

**Prep targets NOT covered (still owed):** Gradial confirm/deny, multi-turn flow gap trajectory, EPA H2 roadmap timeline read, EPA lab as customer-getting-started asset. Carry to next Corey touchpoint (VR-wiki sync).

**Why it matters.**
- **First-testeur pattern** (post April-2 Philippe-as-mirror) now produced a concrete artifact, not just feedback — Corey moved from reviewer to **co-author** of a scoped EPA report. Operational, not theoretical.
- Aligns with H-005 (substrate-before-standard): Corey is the cross-agent customer of the data substrate Pedro owns.
- Two-step substrate move holds — ship simple report to Corey first, iterate, then harden for Philippe + Yanira + Conrad. Compounds with monthly Portfolio Briefing cadence.

**Doc.** Outcome section in AAI Status & Todo: **`## Corey call notes — May 14`** (replaced the prep section). Forward tasks tracked in the "From May 12 — Corey report feedback + call HELD May 14" To Do block.

---

## May 19 — Corey proof-of-utility + portfolio growth-vs-retention split + Agent Owners light version + Tanju External Agent Report

Source: Pedro chat update 2026-05-19 + External Agent Report screenshot (Returning Orgs/Users per Agent, trailing-4-week, latest week May 10).

**1. 🟢🚨 Proof of utility — Corey reused parts of Pedro's report to serve a Cédric request.** Not theoretical value: an EPA PM pulled from Pedro's substrate to answer a Cédric Huesler ask. Hard external-consumption evidence. Promotion-grade — direct H-005 (substrate-before-standard) confirmation, and the strategic counterweight to the bad growth numbers. Pair these two in any exec framing; never present the decline naked (FB-030, `feedback_first_reply_ownership_sentence`).

**2. New workstream — light report version for Agent Owners.** Pedro building a lighter External Agent Report variant scoped for the Agent Owners audience. Companion to the Corey "from-scratch simple EPA report" pattern (May 14) — same move: audience-scoped cut, not a retrofit of the multi-persona report.

**3. Tanju — augment External Agent Report (ex-MCP), started on Governance Agent.** Pedro + Tanju expanding the External Agent Report (locked name; "Agent Integration" was informal — do NOT relock). Governance Agent first. Ties Splunk MCP loop Pedro↔Felix↔Tanju + Lara Langfuse Governance pipeline.

**4. Portfolio growth numbers DOWN.** Latest portfolio report: **-10% external orgs, -30% external users** (growth/total). Concretizes the May 12 Bertrand "numbers descending" risk. Caveat holds: internal/external categorization (Raul list) still weighs on the number — treat as not-yet-hard signal, not raw truth.

**5. Retention (External Agent Report — Returning, trailing-4-week, latest week) — opposite story where it counts.** Returning **orgs** (count / % of agent's external orgs): Discovery 107 / 69%, Experience Production 94 / 68%, Experience Development 30 / 46%, Governance 19 / 47%, Content Optimization 7 / 30%. Returning **users**: Discovery 39 / 15%, Experience Production 38 / 21%, Experience Development 15 / 21%, Governance 10 / 22%, Content Optimization 2 / 8%. Trend curves: **Discovery + Experience Production rising strongly**; Development / Governance / Content Optimization flat-low. So the decline is **concentrated on the 3 low agents, not global** — the two flagships retain and grow. (Corrects the earlier verbal "flat for Discovery" — Discovery retains hardest.)

**6. 🆕 Sharp PM insight — org-level retention high, user-level retention low.** Orgs return (30–69%) but few individual users within them are repeat (8–22%). Org stickiness, shallow user-level engagement. The next question is user-level engagement, not acquisition. Connects to knowledge: repeating-users = primary value signal; measure at unit of user intent.

**Why it matters.** Two metrics must stay distinct in exec framing: growth (down, data-caveated) vs retention (up on the two flagships). The honest non-defensive story = "decline is concentrated + categorization-noisy; retention strong where it counts; substrate proven consumed (Corey/Cédric); here's the plan (Agent-Owners light version, Tanju Governance augmentation)." This is the May 11 Loni+JM deck spine and the Bertrand 1-1 point.

**Doc.** AAI Status & Todo: new tasks (Agent-Owners light version, Tanju External Agent Report Governance) + Current Status note on growth-vs-retention split. Bertrand 1-1: point 5.

---

## May 19 — Engineering bridge: Mithril/Fruitbar ↔ Prompt Library Platform (Hailpern / Somya / Zeus, Sunil tree)

Connective insight surfaced 2026-05-19 cross-referencing the two Hailpern announcements (Mithril Hybrid 2.0 + Fruitbar) against the EH-side "Cross-VP — Prompt Library Platform" memory.

- **Joshua Hailpern** is EM of the **Prompt Library Platform** (Cole Connelly's PM area, O2 KR "EH consumes prompt library not wiki") AND leads the **AIA UI / Mithril / Fruitbar** stack. Same person, both sides.
- **Somya Biswari** + **Zeus Courtois** appear on both: lead engineers on Prompt Library Platform (April 28 memory) and named in the Mithril announcement (Somya = Quarry Component integration lead; Zeus = "You Shall Not Pass" AI-generated-code-quality automation).
- Implication: **Prompt Library Platform and Mithril/Fruitbar/AIA-UI are the same engineering galaxy** — Hailpern + Somya + Zeus — and it sits under **Sunil Menon's VP tree (Experience Cloud Portfolio), NOT Loni/AEM's**. (Cole → Stephen Gould → Tim Lott → Daniel Sheinberg → Sunil Menon → Amit Ahuja.)
- Why it matters: when Pedro engages Mithril/Fruitbar (validation with Josh/Adam) or the prompt-library KR, it's the same org pole. Cross-org influence runs through Stephen Gould (strategic, also Pedro's DX/Unified Shell contact) / Cole (tactical), at VP layer Loni↔Sunil. Don't treat Mithril and Prompt Library as separate org problems — one tree, one set of people.
- See vault note `AAI - Project Folder/AO 2.0/Mithril & Fruitbar - Crash Course (non-frontend).md` + EH memory "Cross-VP — Prompt Library Platform".

---

## May 20 — close-out: Loni+JM reconcile, Aditi/Pierre Tager, Bertrand 1-1 prepped

**1. 🔄 Loni+JM deck reconcile — NOT yet held (pending), NOT a missed outcome.** Earlier framing across memory + AAI Status ("outcome NOT captured, single biggest open") was WRONG — Pedro confirmed 2026-05-20 the deck has not happened. KR3 is an upcoming *delivery*, not a debrief gap. The staleness-auditor's "single highest-leverage refresh" (debrief Loni+JM) was built on the wrong premise. Corrected in AAI Status (staleness flag + Focus item A). Next: confirm date/format with Bertrand (1-1 point 4), then finalize the deck. **Lesson for the system: a "missing outcome" flag can be a not-yet-happened event mislabeled — verify happened-vs-pending before calling something the biggest open.**

**2. Aditi (PM, reports to Pierre Tager in Bertrand's org) — meeting invite via Shankari's reference.** She wants AI-Assistant current state + what's next + what the liaison R&R looks like. **Pedro's read (2026-05-20): NOT a risk.** Aditi is new, doesn't know the Agents space; Pedro will help her onboard. The Shankari referral = recognition that Pedro is the AI-Assistant source/authority — a visibility signal, not displacement. Pedro IS the liaison (Bertrand-named April 14, not revoked); you don't send someone to learn a role from the person being replaced. Real (lighter) sub-point: the liaison R&R is *recognized but not written* — opportunity to formalize it (promotion-useful), not defend it. **Pierre Tager = new, scope unknown — confirm.** Captured in Bertrand 1-1 file Role-Clarification point 3 (FYI-light) + Stakeholder Map.

**3. Bertrand 1-1 (2026-05-20) — prepped, outcome = debrief-ask.** Agenda written into `Experience Hub - Questions for Next 1-1 with Bertrand.md` (FR, 5 points): (1) accept Workshop Foundation facilitator, (2) ✅ Mithril/Fruitbar UI correction ALREADY done with Bertrand before the 1-1, (3) escalate + offer to seed Ian North Star 1-pager, (4) confirm Loni+JM date, (5) growth-vs-retention non-defensive framing. **Outcome not yet captured — debrief next session: what landed on workshop role, Ian 1-pager, Loni+JM date, and the Aditi/liaison-R&R question.**

**Doc.** AAI Status: staleness flag + Focus item A reconciled; Aditi task added (From May 19 block). Stakeholder Map: Aditi + Pierre Tager to add.

---

## May 19 — Ian Boston publishes Agentic NorthStar (🟢 gating artifact RESOLVED)

Source: [Agentic NorthStar](https://wiki.corp.adobe.com/spaces/~boston/blog/2026/05/19/3894002388/Agentic+NorthStar) — Ian Boston, 2026-05-19. **Supersedes every "Ian 1-pager NOT started" flag** (consolidation checkpoint, May 12 P42 §, May 18 Agent Owners §5, May 20 close-out). It exists now.

**Format = deliberate blog, not a wiki page.** Ian: *"a view today that may be obsolete within a week... if this post proves to have a future, then it will evolve into a page."* Ends on a question — ***"Should this be our Agentic NorthStar?"*** → discussion artifact, not a locked spec. Matches Pedro's discussion-not-decision frame; safe to cite with Conrad in room as "the architect's North Star, in review." Anchored to the 2018 Skyline NorthStar.

**NorthStar statement (verbatim):** *"Focus on Skills backed by high value, unique APIs and MCPs driven by the data and content that our customers have entrusted to us, supporting our customers individual and institutional memory to ensure leaving Adobe will be a heartbreaking experience."* Three pillars: Skills (reasoning now commodity via Claude / Codex / Pi-OpenClaw SDKs) + unique APIs/MCPs (where value lives) + **memory as the moat** (institutional memory = lock-in).

**Architecture — distributed > single harness.** Ian rejects "one harness to rule all" (edge cases to the harness-owner = the essence to the skill-owner; a single instance can't specialise UI + context; high skill-cardinality kills reasoning — *"50% delivering 5% is not success"*). Lands on a **distributed harness**: each team owns its own UI + Skills + Session, specialised to its context — *"Each team that owns the context needs to be able to own the UI and specialise it. The skills for the context needs to be their skills."* **Memory is the exception: a shared service across harnesses**, explored by Adobe Research as **memory-as-MCP** (referenceable through a skill). Maps 1:1 to AEM's Slide 2 ownership boundary AND to Bertrand's May 18 "Adobe Harness" (memory + layered context provided by the foundational layer so AEM doesn't build it).

**Hard numbers (sourced to the architect):** AOv1 for AEM agents = **50% "ok", only 5% "exceptional"; explicit feedback 50% unworkable, 5% worse.** P42 adoption rapid, results disappointing. Requirements-first evidence — the bar AOv2 must clear. Pairs with Ian's 2-5% conversion (May 6).

**Two diagrams** on the blog (single vs decentralised) — recreated as Mermaid + slide-impact mapping in the KR3 deck note §"Ian Boston Agentic NorthStar (2026-05-19) — deck integration". Decentralised: UI-A→Harness-A and UI-B→Harness-B each with own Skills + Session, both wired to one central **Memory MCP**. Source PNGs = Confluence attachments 3894001962 (single) + 3894001966 (distributed).

**Strategic read.**
- Gating item flipped 🔴→🟢. Forcing-function escalation no longer needed.
- **Public-naming → delivery:** Pedro named Ian owner on the May 18 call he hosted; Ian shipped May 19. Bank the win — naming an owner publicly in a forum Pedro chairs produced the artifact.
- Pedro's lane = distributor / operationaliser (corrected role, NOT architect). Doc landing triggers: respond as first substantive voice (architecture-altitude visibility, reinforces resolved [[H-005]] substrate-before-standard), carry into agent teams as the requirements anchor, compile requirements back to AOv2.
- Deck fuel for Loni+JM: Slide 2 add Memory-as-shared-MCP; distributed-harness validation of the AEM/AOv2 boundary; 50/5 baseline (requirements-first, never naked); memory-as-moat spine line tying to Loni *"not at the mercy of somebody else."*
- Credit Ian as author on any slide. Don't weaponise the distributed model against Conrad/AO in room — frame as "architecture converging on distributed + shared-memory; AEM contributing requirements."

---

## May 22 — Ian NorthStar thread: outcomes (routing, memory→Saar, UX = PM-lead, consistency mandate)

Pedro engaged Ian's NorthStar as first substantive responder (Slack + wiki footer comment, May 19-22). High-value exchange — Ian answered every question and escalated. Source: wiki comments page 3894002388 + Slack. Also referenced: Ian's [Claude Token costs](https://wiki.corp.adobe.com/spaces/~boston/blog/2026/05/20/3894008282/Claude+Token+costs) blog.

**1. Routing answered — "the UI deciding which harness to call."** Ian (wiki reply, hedged "I think we are going to see"): harnesses loaded with the skills they need + the UI decides which harness to call, via **explicit or prompted selection, NOT automatic intent detection**. AOv1's orchestrated-intent-above-agents made reasoning weaker. AOv2 + FluffyJaws show explicit/prompted > auto. Also: a skill can be shared across harnesses, and harness-to-harness A2A calls are fine (FJ calls DAA over A2A) — distinct from AOv1 directed agent-to-agent (dead) and customer-facing A2A (retiring). **Implication: selection is a surface/product problem before an orchestration one → Pedro's lane.** ("UI decides" = Ian's forward prediction, not a locked spec.)

**2. UX/selection — "must be PM lead" (Ian, on record).** Pedro claimed the practitioner-UX read; Ian: *"UX, yes, absolutely, must be PM lead."* Architect-endorsed lane.

**3. 🆕 Consistency mandate.** Ian: *"Consistency will be vital so an Adobe user feels like it is the same surface regardless of the implementation details or UI engineering ownership."* In tension with distributed-UI-ownership → reconciling it = Pedro's job: own the **cross-surface consistency layer** across distributed agent surfaces. Architect-backed answer to the 4-chats fragmentation (Experience Workspace / Modernization / Slick / Mithril; Marcus refused unification). Backs Pedro's convergence push. Senior-Director-grade lane.

**4. Memory ownership → escalated to @asaar (VP).** Ian: who owns memory = tbd; partly user-bound, partly team/org, both with residency requirements; users span CXO + DMe → leadership question. Proposed identity-like model (central personal+org via IMS/AUP + common API/schema; product-specific memory with solution teams). **Ian escalated to Alexander Saar (VP Eng) for cross-Adobe alignment at his level.** → AEM needs requirements ready for that conversation. Doc drafted: vault `AO 2.0/What AEM Needs from a Central Memory Service.md`. Route via Bertrand (don't insert into the VP alignment directly). NOTE: Pedro asked Ian to write the official requirements ("would you put together…"); Ian routed it up to Saar. Pedro's doc = AEM's private *input*, not the official artifact. **Standing weekly checkpoint tracker** (5 checkpoints: doc exec-ready → hand to Bertrand → on Saar agenda → conversation held → outcomes fed back; next check 2026-06-01, then weekly) lives in AAI Status Focus — surface + update it weekly at session start.

**5. Moat — Ian loved + sharpened it.** Pedro's "open, portable, but heartbreaking to leave" → Ian: *"a great way of putting it"*, tied it to an early-March conversation with **@lkao + @gmiller**, said Adobe Research is working in the space. Refinement: **portable WITH EFFORT** + value-on-top = the moat (his Gmail-takeout analogy). Confirms moat = the data, not the mechanism; interface stays open (memory drawn as MCP). **Visibility: Pedro's phrasing now attached to a senior architecture conversation.** Confirm who @lkao + @gmiller are.

**6. Token economics** (Ian's Claude Token costs post + a ClaudeCode deep-dive screenshot). MCP server manifest = **~2K-15K tokens/turn even when unused** (5 MCPs ≈ 50-75K history budget lost permanently); Skill ~200-500; hook 0. Context window ~200K, conversation history = largest segment (40-60%), compaction trades quality for budget. → Argument for **skills-over-MCP** (reinforces Trent/Carsten/Felix-Meschberger consensus; mild tension with AEM's MCP investment + MCP-first posture). Sharpened memory-requirements doc req 6: a Memory MCP must keep its manifest lean + return ranked context only. Latent sharp question (unused): Ian's token-costs post argues against MCPs while his NorthStar draws memory AS an MCP — is memory the high-value exception, or skill/hook-backed?

**7. 🟢 Influence pattern (bank for Senior Director narrative).** Pedro's sharp questions at the right altitude triggered owner action twice: public-naming → Ian shipped the NorthStar (May 18→19); memory question → Ian escalated to Saar VP (May 22). Operating at architecture-conversation altitude, named-in-the-room, triggering motion above him. Reinforces resolved [[H-005]] (influence/substrate before standard). Promotion-frame = "operating at architecture-conversation altitude," NOT "I am the architect" (Ian = architect; Pedro = PM distributor + UX/consistency lead + requirements compiler).

**Process note:** Claude misread "would you put together…" as a self-delegation and pre-drafted the requirements doc; Pedro corrected (it was addressed to Ian). Claude also paraphrased the token-costs post before reading it. See [[feedback_confirm_ask_before_producing]].

---

## May 26-27 — Bucharest workshop framing + "everything is a skill" reframe

Pedro animates ~1h at the June Bucharest workshop (Saar-hosted; Bertrand opens 1h). Sync with Stefan (5/22) revealed the real constraint: **audience = 56 people, global, mixed (devs, mostly managers + senior managers, sales, PMs)** → NOT a brainstorm. Format = **keynote / teach-and-align**; the actual skills-vs-agents decision stays a small-group call. Very likely the **Workshop Foundation skill-proliferation facilitator role** Bertrand asked Pedro to take (May 12, re-aired May 18). Prep note: vault `AAI - Project Folder/Bucharest June Workshop — Skill Proliferation + Modernization.md`.

**Framework (Pedro owns the structure):** two gates — Gate 1 *Should it exist?* (competitive / persona / seamlessness = the modernization filter = Bertrand's "what's worth investing in" governance); Gate 2 *Which harness?* (see reframe). Plus a persona × context 2×2. Merge insight: proliferation (supply) + modernization (criteria) = one question — *where does agentic investment go, and how do we decide?*

**🆕 Conceptual reframe (Pedro caught it):** the org's "skills under existing agents vs new agents" framing is **partly outdated** under Ian's NorthStar. Reasoning is commodity → **everything is a skill**; the "agent" dissolves as a build unit into skills-in-a-harness (Ian: DAA = "a collection of Skills in a harness"). So Gate 2 isn't "skill vs agent" but **"everything's a skill — which harness?"** (existing by default; new harness only on a new persona+context boundary). Hold for the mixed room: agent dies as a *build* unit, survives as a *GTM/customer* unit (sales still sells "agents"). Knowledge captured: `ai-product/` "Everything Is a Skill". This upgrades Pedro's session from running the stale binary → teaching why the question changed = operationalizing Ian's NorthStar (his distributor role).

**Open / confirm:** outcome (decision rule + shortlist vs the binary); Stefan / Day-2 fit; pre-align the two gates with Bertrand before the room.

**Process note (vault):** prep note created via filesystem Write at the canonical deep path; clicking its `[[wikilink]]` before Obsidian indexed it spawned an empty stub at a root `AAI - Project Folder/` — deleted, canonical intact. Use obsidian-cli for new vault notes + wikilinks to avoid the index-lag stub. See [[feedback_confirm_ask_before_producing]].

---

## May 27 — Cross-Harness Skill Registry idea + "There Waiting" blog + Ian refinement

Bucharest-prep session pivoted into a new Pedro proposal, banked in two vault notes (English, filesystem Write): [[Cross-Harness Skill Registry — Gap Proposal]] (internal, dated, objection-handling) + [[From North Star to There Waiting]] (public blog draft, Ian-style, ends on a question).

**The idea (Pedro, 2026-05-27).** In the distributed-harness model (any harness: AOv2, Claude SDK, Codex, custom), nobody owns a curated, cross-harness, customer-facing way to find/reach the right skill. AOv2's marketplace = per-repo `marketplace.json` + `SKILL.md` (Anthropic format), dev-facing, install-time, no review gate, not aggregated. Gap is systemic (AOv2 included). Confluence grounding: "Beginner's guide to add a plugin/skills to AEP AO 2.0" (3851715892, V. Barshikar); AIA Platform Architecture shows `marketplace · catalog · installer` already forming.

**Scope.** Jobs = (a) discovery + (b) routing/selection (NOT (c) entitlement = AO+commerce, later). Curation gate at entry. **Schema = the moat** (what each harness declares to appear: id/owner/persona/context/lifecycle/harness/deployment) = definition-ownership = [[H-005]]. **Harness-agnostic — "which harness" is a metadata field, NOT the axis.** Pedro's own correction: don't make "in AOv2 / not in AOv2" the organizing axis (re-centers on an undecided platform, couples fate to it, leaks implementation into the customer view, breaks Ian's consistency mandate). The "in/not-in-AOv2" view is legit only as a separate internal migration tracker.

**Positioning.** Anchor "publish vs find" (dev publishes into a harness / customer finds across all). Avoid "plumbing" (denigrates AO/Ian) + "App Store" (implies entitlement). Lead positive; AOv2-contrast yes-and only if challenged.

**🆕 Ian refinement (Slack, 2026-05-27) — pre-align worked.** Pedro DM'd Ian the angle before publishing; Ian engaged (not blindsided). Ian: *"The customer should not have to find the right skill, it should be there waiting"* — a UI surface connects to a harness with all applicable skills present, "precise and complete"; skills defined once, used in many harnesses. **Not a rejection, a relocation:** "there waiting, precise and complete" REQUIRES Pedro's machinery (a registry that knows all skills across harnesses + curation that keeps each surface precise+complete as skills proliferate). **The move (banked): concede the front-end (browse = friction, Ian right), claim the back-end (registry + schema + curation = nobody owns it = the moat).** Don't litigate; forward-frame. Pedro sent the reply.

**Blog reshaped:** title "From North Star to **There Waiting**" (Ian's words = credit + co-shaped). Spine: browse is the wrong answer (GPT Store cautionary tale) → there-waiting (Ian) → backstage shared-declaration + curation → the one browse case = admin/buyer (storefront survives there) → close on the schema question ("what must each harness declare").

**Credit mechanics (SD visibility gap).** Write-to-own (Ian's model). Authorship banked dated. **Publish the blog (public/indexed/citable), NOT email** — email = megaphone to point seniors at the post, blog = venue. Pre-align gate: Ian ✅ → Bertrand + Conrad heads-up → publish as open question. Turf = the real risk (AIA Hailpern building catalog/installer; AO), NOT "PM not architect" (Ian: selection+consistency "must be PM lead"). Don't call it "officially mine" pre-landing.

**🆕 Ian round 2 (2026-05-27).** Two more corrections, adopted in the blog: (1) the **surface-owner PM composes the surface from the registry** (Ian verbatim: *"the UI surface and its harness are containers into which a PM adds the set of skills"*) — NOT the customer/admin; only commercial entitlement is customer-facing. The architect defined Pedro's lane = composer, registry = the source (strongest lane statement yet). (2) "harness-agnostic" = the registry is harness-neutral; harness deployments stay specialised per surface (only the registry + skill defs are shared). Blog section "The one place a customer does look" → replaced by "Who composes a surface".

**Keynote rebuilt (2026-05-27).** [[Bucharest June Workshop — Skill Proliferation + Modernization]] reworked from facilitated-decision-room → **56-mixed keynote** (teach-and-align, decision stays small-group): headline + 3 messages (everything-is-a-skill / two-gate rule / there-waiting registry as the open-direction "new thing"), Holy-Shit = the 4-chats fragmentation, run-of-show + spoken beats + audience tailoring (devs/managers/sales/PMs).

**Done this session:** gap note + blog ("There Waiting") + Saar requirement-block + blog rename + keynote rebuild. **Pending (Pedro):** publish blog after Ian's final + Bertrand/Conrad heads-up; pre-align Bertrand on keynote + the registry-as-open-direction.

**🆕 Ian round 3 (2026-05-28) — placement governed + form-per-surface + invisible.** Pedro asked who governs that a UI exists and where. Ian: **"governed"** (not per-team free) → confirms **Gap 2 / surface governance** (surface placed by persona + context, not org; default reuse; new surface only on new persona+context; a *surface map* = sibling of the skill registry). Plus a surface ≠ a chat window: *"the best assistants are almost invisible"* (authoring-on-brand = embedded real-time guidance, no chat). **Presence has two forms** — consistent chat (where chat fits) or invisible/embedded (often better); form follows surface; governance picks which. Consistency spec, concretely (Ian): every chat same controls, the "+" = same class of actions, messages same side, **learn-once-or-it's-a-fail**. **All three Pedro contributions now architect-validated across 3 rounds** (registry, consistency, surface-governance); Ian defined the lane in his own words ("selection must be PM led"; "the UI surface and its harness are containers a PM fills with skills"; placement "governed"). Artifacts: Gap 2 section + mermaid "The Picture" (Ian's decentralised + the 2 missing shared layers = registry + consistency) in [[Cross-Harness Skill Registry — Gap Proposal]]; blog [[From North Star to There Waiting]] carries the diagram (additive red-outline, NOT "MISSING") + the invisible/consistency points. **Anti-fragmentation framing locked:** *distributed engineering, unified experience* — the risk = three failures (juggling / incoherence / wrong-surface) → three PM-owned fixes (there-waiting / consistency / registry) = delivery / experience / supply. Knowledge entries added (ai-product ×2 + leadership ×1) this consolidation. Comms-craft: build on a senior's artifact additively, not correctively — [[feedback_additive_not_corrective]].

**🆕 Ian round 4 + publish gate CLEARED (2026-05-28).** Ian deflated "registry" → **not a central service; a consistent skill-declaration standard (format + metadata) + git-native discovery** (skills in open git repos, each harness takes a local copy, discovery = git labels + a pointer-list, curation = light convention). Ian: *"it becomes something to fight over, and there really is no need."* Pedro adopted it everywhere — the durable/ownable thing is now **the standard + curation convention** (definition ownership, [[H-005]]), the better political position (a standard ≠ turf-fight). Blog [[From North Star to There Waiting]] + Gap Proposal diagram updated (UI top → harness → session/memory/index → git repos bottom). Then Ian's verdict: *"largely aligned… I would post, then I can point to it on my blog feed."* = green light + **amplification** (owner → distributor of Pedro's work). Ian also read **Conrad** for Pedro (*"leans slightly to one-harness but knows it failed; what matters to him = connectivity + alignment across CXO and DMe, which memory delivers"*) = the AO-side check Pedro couldn't get directly (Conrad out). **Publish sequence (Pedro):** Bertrand heads-up sent → Conrad async FYI → publish **this afternoon (2026-05-28)**. Blog stripped to publishable (DRAFT banner removed, `status: ready-to-publish`). Bertrand timing porte-à-faux (told him "wait", now publishing) defused with a forward-framed update, not a silent edit. Knowledge: leadership Co-Author entry +amplification observation; the pacing = [[feedback_keep_claude_private]] (iterative human work — Pedro already showed v1 to Ian, so overnight-polish risk is moot).

**🆕 AOv2 cross-harness skill-sync = confirmed gap (2026-05-28).** Checked: AOv2's marketplace *is* git-native local-copy but **single-harness** (marketplace git repo → install into local AO, template `OneAdobe/ao-plugin-extensions-template`). What AOv2 does NOT address = the **cross-harness** layer the blog is about (one declaration standard across *different* harnesses + shared discovery index + curation). Skill-level evals also unsolved (Trent 4/29). Decision: **keep this OUT of the public blog** (naming an AOv2 gap publicly = corrective toward Conrad/Trent's team; additive-not-corrective). Lives in the internal [[Cross-Harness Skill Registry — Gap Proposal]] as a round-4 reserve line. Defensible rebuttal if challenged "AOv2 already does git plugins": *"Yes, within AO. My point is the layer above any single harness — the consistent declaration standard + cross-harness discovery. No single-harness marketplace gives you that."* Knowledge: ai-product "A Single-Harness Marketplace Is Not a Cross-Harness Standard — Publish vs Find".

**🆕 Philippe annexation attempt on the Bucharest keynote — DECLINED (2026-05-28).** Pedro had casually floated Philippe's "agent workflows" work as *"a good example"* for Pedro's session. Philippe banked it and came back proposing to **reframe the whole session** around his thesis (*"our customers don't have a tool problem, they have a workflow problem"*). Pedro declined: warm tone (matched his "Hello l'ami"), firm line, anchored the no to **scope settled with Ian + Stefan** (skill proliferation + modernization), refused the annexation (*"ton angle mérite son propre format, pas un bout du mien"*), no apology for the opening. Lesson = a competitor annexes your visibility surface through any opening; loose words are banked as a mandate (same mechanic as Agree-1:1-Reframe-Publicly). Knowledge: interpersonal "Don't Seat a Competitor's Thesis on Your Visibility Surface — and Loose Words Get Banked". **Bucharest keynote scope now locked with Ian + Stefan** — the keynote prep note still says "registry" in places and needs a round-4 pass (registry → standard + git-discovery) before the session.

**🆕 System infra: built `/system-review` skill (2026-05-28).** Monthly heavyweight sibling of `/consolidate` — spawns `staleness-auditor`, then *acts* on the drift (hypothesis lifecycle promote-3+/kill/demote, score decisions with knowable outcomes, prune quality criteria, regenerate dashboard, log review + reset cadence in `.claude/state.md`, commit). Was a CLAUDE.md directive + manual auditor run; now skillified via `/skill-creator`, source in `.skillshare/skills/system-review/`, synced, registered in the CLAUDE.md skills table. Next System Review due 2026-07-01.

---

## May 12 P42 Status Sync — Loni reframe + Ian = North Star architect

Source: `Meeting Notes/Yanira/20260512 - P42 Status Sync.md`. Bertrand + Ian Boston + Jaclyn (+ Pedro arriving). 112-line transcript cuts at 6:30 mid-handoff to Pedro.

**1. 🚨 Loni reframe verbatim (May 11, reported by Bertrand May 12).** Loni: *"No, that's not the question. Question is context, and how do we equip our agents with proper context."* Explicit rejection of AOv2 yes/no framing. Pivot = **context architecture** as the strategic axis. Bertrand: *"more than memory. Connecting content sources from different places and deciding which bits should be passed as actual content."* → Strategic anchor for May 11 deck. **Open the deck with this.**

**2. 🚨 Ian Boston = North Star architect for AEM agents AOv2 strategy.** Bertrand 6:30 verbatim: *"this looks like a new North Star architecture for Pedro."* — interpretation: Ian's architecture serves as **North Star *for* Pedro's work**, NOT Pedro is the architect. Ian = author. Pedro = consumer / operationalizer / PM distribution layer. **Ian self-assigned: one-pager for teams.** Watch for Ian deliverable.

**3. Ian's AOv2 requirements list (5 items — Ian-authored):**
   - Skill portability: skill must work everywhere (Claude SDK, codex, Claude AI, AOv2) without per-harness config.
   - URL auto-recognition: AOv2 recognizes registered Adobe APIs without lockdown config.
   - Properly open source — no private dependencies. Anyone in Adobe can fork + run own server.
   - Standards compliant — skill from any location works.
   - A2A retire confirmed (no customer interest).

**4. Forcing-function lever Ian named.** *"Any skills not using registered APIs that we recognize just won't work in AOv2... so make sure your APIs are good."* AEM-wide API quality = forcing function for cross-agent technical standards. Pedro's PM lane: drive this across agent teams.

**5. Skills/MCP/API hierarchy direction.** API first. MCP retained — wrap existing MCPs in skills. First skill iteration reuses MCPs. A2A out. Aligns with Carsten May 6 proposal.

**6. Governance Agent = prior art on global-context API.** Bertrand: *"that's exactly what AEM governance is working as well, on this global context."* Philippe's Governance has built context-API substrate. Reuse signal. **Tension:** Pedro needs Philippe's prior art for portfolio narrative — handle transactionally given competitor frame. Don't hand Philippe the framing of the cross-agent context story; cite Governance as a reference implementation while keeping the portfolio narrative under Pedro.

**7. "Burned from AOv1" — Jaclyn confirm (5:05).** *"They're so burned from ao of one."* AOv2 must clear a high bar. Reinforces Felix May 5 ("hors sol" critique) + Conrad April 14 ("widely not flying").

**Pedro's actual role here (corrected):**
- Not the architect — Ian owns that.
- Pedro = PM liaison + distributor + portfolio operator. Carries Ian's one-pager into agent teams. Compiles requirements + commitments + SLAs back to AOv2.
- Compounds with H-005 (substrate-before-standard) — Pedro owns the data substrate; Ian owns the architecture spec. Different lanes, mutually reinforcing.
- Still material for Senior Director path: being **named in the room** when VP architecture conversation lands. Promotion-frame is "operating at architecture-conversation altitude," NOT "I am the architect."

**May 11 deck implications (corrected):**
- Open with Loni context-reframe (verbatim).
- Requirements slide = Ian-authored, Pedro distributes. Credit Ian explicitly.
- Pedro's slide = PM operator / liaison / portfolio reporter — own substrate + distribution, not architecture.
- Mithril Silvia context-reading ask = visible expression of Loni reframe; same-day Pedro→Silvia hedge ("don't promise v2") consistent with Loni "context is the question."
- Governance Agent global-context callout (reference implementation reuse).

**Cross-links:**
- Mithril ↔ Silvia loop (May 12 EH-side memory) — context-reading primitive ask now has explicit VP-level (Loni) backing.
- Trent April 29 "AEM Context = North Star question" + Bertrand May 12 "North Star architecture" = compounding label around context-architecture as cross-Adobe primitive.

**Open / TBD:**
- Transcript cut at 6:30 (Bertrand: *"Two questions... Do you want to..."*) — Pedro's portion not in this file. Find Pedro segment if recorded separately or follow up with Bertrand on what was assigned.
- 🟢 **Ian one-pager LANDED 2026-05-19** (was NOT produced as of 2026-05-18). Self-assigned May 12, published as a blog May 19 — the day after the Agent Owners call where Pedro publicly named Ian owner. North Star requirements doc was the gating artifact for per-team AOv2 evaluation; now Pedro CAN reference + distribute it. See "May 19 — Ian publishes Agentic NorthStar" entry.
- Governance global-context API technical detail — schedule Philippe sync (carefully framed).

---

## May 13 — Felix + Lara + Pedro 3-way (External Agent naming lock, Langfuse pipeline, cost data)

Source: `Meeting Notes/Felix Pedro 1 1/20260513 - Felix Lara Pedro 1 1.md`. ~30 min EN.

**1. 🆕 "MCP report" → "External Agent Report" naming locked.** Felix: *"MCP je suis allergique à ce mot là."* MCP ambiguous (Tanju millions of internal tool calls true; ChatGPT-Copilot consumption near-zero also true). New architecture:
   - **AI Assistant Report** (internal AEM assistant usage)
   - **External Agent Report** (Adobe agents consumed via ChatGPT / Copilot / Claude — MCP integration layer)
   - **Umbrella high-level comparison report**
   - Companion to existing "Tool Calls" counter-unit lock (May 6). Both naming rules live for May 11 deck.

**2. Lara Langfuse pipeline for Governance.** PR in flight to send correct trace tags on Langfuse. Friday May 15 merge → prod → weekend backfill → Monday May 19 data → integrate into report. POC = manual CSV download from Langfuse → DB. Felix preferred long-term mechanism: push from agents → central DB via IMS user token.

**3. User metadata enrichment (Felix ↔ Bertrand from Playground team).** User table now has full_name / user_type (4 types) / email via API. Felix full sync script done — remote API-based, no longer local. Bridge between systems operational.

**4. Internal/external classification — Raul list = current gospel.** Raul updated list yesterday May 12 → Pedro processed → reports show org/user increase (explains anomaly in numbers). ~18-20 Raul-flagged-external orgs look internal (lab/sandbox). Felix heuristic catches 30-40 obvious-Adobe (Adobe Corp, Adobe Consulting marked external in Raul list). Pedro decision: stick with Raul until classification aligned, avoid display↔data divergence. Still pursuing API/MCP source vs github README.

**5. 🆕 Mark Pfaff = new contact.** ECP usage + tool calls cross-check on Databricks. Numbers align both platforms. Pedro started Governance External Agent report based on Mark's work — tool calls, users, repeated users. Add to Stakeholder Map.

**6. Portfolio report landing-page link shipped.** AEM report EDS landing page now has direct portfolio link. Layout = Gilles slide / Felix May 12 slide reproduced. Includes MAU retention (under hood for G&R sync, senior-management abstract).

**7. Rubin posture confirmed 🟢.** Pedro tested Rubin. Won't replace AAI substrate medium-term. Felix: **LLM-as-Judge = the moat.** Rubin has returning users/orgs, not the judge layer. Confirms H-005 substrate-before-standard.

**8. 🆕 Cost data — $2K/mo report generation.** ~30% LLM-as-Judge (heavy, accepted). Rest = per-block Opus call on every text block × many blocks × many pages. Lara push: most blocks should be static code, only key findings need LLM. Felix agreed, will streamline. $100-150 per report at full price. Governance agent prod cost: ~$100/mo. EPA/their agent: <$10/mo.

**9. MCP UI for engineers (Felix).** Lara + Pedro added. Slow (summary executed per request — Felix removing). Once API+MCP done, weekly EPA download for engineer problem-detection. aitools-flex slow PR cycle = blocker.

**10. Cadence.** Pedro off Thu+Fri. Lara works Fri. Next 3-way Monday May 18.

---

## May 12 — Bertrand 1-1 (FR, ~20 min)

Source: `Meeting Notes/Bertrand 1 1/20260512 - Bertrand Pedro 1 1.md`. Chronologically: this 1-1 → P42 Status Sync (same day) → Mithril Silvia (same day). Pedro got Loni reframe from Bertrand here, relayed to Silvia hours later, Bertrand re-stated at P42 to Ian.

**1. 🚨 May 11 deck framing locked.** Bertrand: *"Un point de vue AEM sur ao deux zéro. Qu'est ce qu'on va faire? C'est surtout pas la question. Faut pas dire deux zéro si les gens vont se braquer du fait de l'expérience pas terrible."* **Don't say "v2." Frame = requirements-first.** People defensive due to v1 experience. Action: document what AOv2 brings.

**2. Loni reframe — second layer (verbatim via Bertrand).** *"elle a remis une couche notamment sur la dimension contexte, est ce que dans la solution qu'on voudra utiliser pour nos agents, il faut pouvoir plugger proprement ce qu'on va construire pour gérer le contexte."* Context-management plug-in capability = requirement. AOv2 fits or not — TBD. Plus skills hierarchy structure open. **Loni reframe is layered + reinforced, not one-shot.**

**3. Friday softening signal.** Gilles + Felix + Michael talked Friday. Position softened to *"peut être quelque chose qu'on regarde"* — less categorical than Thursday. Direction-emerging frame holds.

**4. ⚠ R Cross-surface AI Assistant continuity vs Michael compliance.** Bertrand: *"il nous faut que toutes les surfaces, les interfaces AEM... qu'on puisse avoir des échanges assistants ui, ui assistance."* Bilateral UI↔Assistant + conversation continuity across surfaces. **Michael disagreed** — compliance: conversations must stay in same primary region as Cloud Service. Tension echoes Ian Apr 1 data-residency risk. Open.

**5. Skills vs context distinction (Bertrand mental model).** Skills = technical context (LLM request adds skills). Context (Bertrand sense) = closer to Governance Agent prior art — content + instructions. Skills possibly customer-contributed. Pedro: *"j'ai pas encore complètement digéré ce que c'est supposé faire."*

**6. Open architecture question (Pedro, unresolved).** One AI Assistant per agent / per domain? Or one global Assistant? If global: how differentiate skills + context per domain? Bertrand answer: **context-awareness routing** — *"Je suis dans page Editor donc les skills qui vont bien c'est ça."* Assumes Mithril team thought about this. Open.

**7. 🔴 Migration timeline — September unrealistic.** Pedro to Bertrand: *"il ne faut pas imaginer que la mise V c'est septembre et que tout le monde sera prêt en septembre."* Multi-month mixed-state window confirmed. Same point Pedro raised w/ Silvia same day.

**8. Silvia reported to Bertrand.** Pedro: Silvia "very actively" pushing for content-awareness via Tim. Coached: synchronize w/ Guliz BUT careful *"on n'a pas choisi avoué deux."* Bertrand confirms Gilles + Michael had AOv2-counterpart meeting with Manas + Ken — relayed "v1 was very complicated."

**9. 🆕 🟢 Workshop Foundation — Bertrand asked Pedro to facilitate skill-proliferation session.** Peter Parker dropped, had 2 agenda items. One item = *"comment on va gérer la prolifération ou la gestion des skills à l'échelle d'aem."* Bertrand: *"Je cherche un animateur pour cette session, tu n'en as pas parlé?"* — Pedro hasn't responded. **Opportunity. Same lane as Ian's API-quality forcing function.** Pedro action: accept facilitator role.

**10. 🔴 Usage numbers DESCENDING — Jaclyn asked for JM + Loni numbers.** Pedro pulled. Internal/external categorization still problematic → impacts numbers. **Numbers show usage going down.** Post-Summit partially explains. *"j'espère que les chiffres sont pas trop faux."* Working w/ Yanira + André Bedas + Raoul on single source of truth.

**11. 🟢 Grafana Bertrand presented Friday = "off completely" — Raul fix closes drift.** Pedro at 1-1: *"pas mal off"* because Bertrand pulled all orgs unfiltered + end-March → May Raul-list scorecard drift. **Raul has since fixed the list** — Namita banner no longer needed. JSON-config-too-large constraint may still need separate attention (Grafana stopped supporting), confirm before next exec demo. Pedro reports stayed approximately right throughout.

**12. JM/Loni first meeting structure.** 45 min - 1h. Pedro proposed deck order: status → inhibitors (slides updated) → credit usage UP → retention → MCP add-on if interested. Splunk MCP: lots of noise, little signal, few tool calls yet. Governance MCP report done, others in progress.

**13. Corey review confirmed in 1-1.** *"Pas mal de cosmétiques et d'utilisabilité."* Call held May 14 (see "May 14 — Corey 1-1" entry).

**Pedro action items from this 1-1:**
- Accept Workshop Foundation facilitator role for skill-proliferation session.
- Land JM/Loni deck order: status → inhibitors → credit-up → retention → (optional) MCP.
- Verify Grafana JSON-config-size issue separate from Raul-list drift; confirm Grafana refresh post-Raul-fix before next exec demo.
- Build credit-usage-up + customer-trust slides w/ Quiet-Hours-via-Agents 81-customer beta as concrete proof point (EH cross).

---

## May 12 — Mithril Silvia Eugene Pedro sync (EH/AAI cross-cutting)

Source: `Meeting Notes/Eugene/20260512 - Mythril Silvia Eugene Pedro Sync.md`. ~22 min EN.

**1. Pedro hedge confirmed in room.** Told Silvia: AEM teams not committed to AOv2. Sites pushing back hard. Don't promise v2 in upstream conversations. Use cautious language. Aligns w/ Decouple-Architecture-Ask knowledge entry.

**2. Loni reframe surfaced same day (pre-P42).** Pedro relayed to Silvia: *"Loney comes with: maybe v2 is not the correct question. Maybe we should ourselves list the requirements and then see how v2 would fit in."* Same Loni reframe Bertrand reported at P42 hours later → converging signal at VP level.

**3. AEM evaluation criteria (Pedro stated in room):** Skills > orchestrator. Portable skills (work w/ Claude / ChatGPT / AOv2). Open-source platform model (fork + PR). Output = requirements + commitments + SLAs to AOv2.

**4. 🆕 Silvia use case explicit:** *"We don't want AI to interact with UI. We want AI to read UI."* Mithril demo missed this — context-reading not in MVP. Will raise w/ Tim Lynn + Matthew tomorrow May 13.

**5. Silvia parallel work — Guliz-assigned.** Design POV on AOv2 for AEM. Analysis this week. Pedro action: send Silvia engineering-manager list per AEM agent team. She'll connect for UI/context portion.

**6. Eugene Mithril framing.** Current AI Assistant icon = dummy, opens same chat everywhere, no UI context. Post-Mithril = contextual per-surface (pipeline, etc.). Strategic surface rollout, not blanket.

**7. 🆕 Migration window UX problem (Pedro raised).** Multi-month window where some agents on v1, some on v2, some migrating. User won't know which has skills/Mithril vs which doesn't. Open product question. Silvia mitigation: in-app notification (*"version of LLM not supporting this data, stay tuned"*). Eugene: low risk, customers not workflow-dependent yet.

**8. 🆕 AI Assistant pricing question (Silvia raised).** Free or paid? Affects failure-tolerance UX. Pedro recalls: SKU exists post-Summit, token package, run out → purchase. **Action: confirm w/ Bertrand.** Ties to Bertrand April 29 pricing/SKU bombshell.

**9. Data instability flagged (Pedro→Silvia).** Org counts fluctuating morning vs evening due to Raul-list manual update. Beware numbers.

**10. 🆕 Matthew = new Mithril co-owner stakeholder.** Surname TBD. Tomorrow's Silvia + Eugene sync includes him + Tim Lynn. Pedro NOT invited.

**Pedro actions tracked:**
- Send Silvia engineering-manager-per-agent list.
- Check w/ Bertrand on AI Assistant SKU/pricing.
- Stay tuned for Silvia/Tim/Matthew sync outcome (May 13).

---

## May 18 — Agent Owners Alignment (Pedro HOSTED)

Source: `Meeting Notes` → `Agent Owner Alignement/20260518 - Agents Owners Alignement - .md`. ~32 min, EN. **Transcript now COMPLETE (gap 14:21→29:05 filled 2026-05-19) — items 4/5/8 revised + new signals 9-12 added.**

**1. 🆕 Pedro hosted the cross-agent forum (Yanira on PTO).** First time Pedro chairs the Agent Owners Alignment. Ran agenda, gave the AOv2 status himself, handed mic to Bertrand for roadmap process. Visibility / altitude data point — Pedro operating the standing cross-agent venue, not just contributing. Bank for Senior Director narrative; offer to be Yanira's standing backup host.

**2. 🆕 CCF / ISO 42001 scope NARROWED (Robert Guthrie).** Initial scope = all AEM agents. Now = **Discovery Agent + Governance Agent only** this year. Loni + Bertrand still finalizing exact list. Deadline **July 17** to be compliant (auditors collect evidence Aug-Oct, possibly into Oct). 10-12 CCF controls mapping to ISO 42001 international standard. Other teams may opt in if ready. **Bertrand (verbatim):** *"important, but not really urgent... not going to block any deal that we know of in the next two quarters... not top of stack at the moment."* Tech GRC may begin reaching out to Discovery + Governance teams. **Supersedes May 4 entry** (was ~12-13 tickets, all agents). Downgrade tracking 🔴 → 🟡.

**3. 🆕 Roadmap deck restructure (Bertrand, NEW format).** Timeline view of internal + GA dates → per-agent overview slide (production, modernization, development — Brian started development overview) → per-skill/job detail slide for any non-self-explanatory bullet. **Snapshot cut THIS Friday May 22** → handed to a design agency for refinement. **Final Friday May 29** → distributed broadly: roadmap webinars, field, customers, support. First time roadmap restructured this way. Bertrand: *"every word, every bit, every minute we spend on the deck is not wasting time, this is used a lot in the field."* Agent owners PM + eng asked to invest time this week. **Pedro lane:** as host + portfolio operator, ensure his 6 agents have timeline + overview coverage before May 22.

**4. AOv2 — Pedro framed publicly as host (the "introduce the request" already partly executed).** Pedro stated: confirming from Bertrand ("the architect") **green light for the EVALUATION of migrating current platform onto AOv2, NOT the decision**. *"There are still questions at senior management if [AO]V2 is the platform that we should move into."* Directions Pedro named to Ian: open-source model (fork + PR), moving into skills. Requirements-first framing landed verbally with agent owners. The drafted broadcast message becomes the written follow-up with criteria + AS-IS staging ask.

**5. 🟢 Ian North Star 1-pager — LANDED 2026-05-19** (verbatim May 18: *"I'm about to start... I haven't actually started it"* → published the very next day). Pedro publicly named Ian owner on this call; Ian shipped [Agentic NorthStar](https://wiki.corp.adobe.com/spaces/~boston/blog/2026/05/19/3894002388/Agentic+NorthStar) May 19. **Public-naming → delivery: a forcing-function win without the forcing-function Slack.** Gating artifact resolved. See "May 19 — Ian publishes Agentic NorthStar" entry.

**5b. 🆕 Ian "prove-it-first" posture (14:42-15:35).** AOv1 failure modes Ian named: hard/slow agent onboarding into AOv1, delays in license-usage reporting. North Star requirement = don't repeat these. Ian verbatim: *"AOv2 has got [to] prove itself, prove that it can deliver those things to us before we agree to commit to it. Now others may have different views."* This IS the requirements frame — AOv2 must prove delivery against AOv1 pain before AEM commits. Strong evaluation-not-decision anchor, sourced to the architect.

**5c. 🆕🚨 Bertrand "Adobe Harness" rename + multi-layer context/memory = the North Star content seed (17:09-19:05).** Bertrand sensing AO → **"Adobe Harness"** rename ("AO 2.0 will have a new name soon"), more than an agent orchestrator. The harness must provide, so AEM doesn't build it itself: **memory management** (Claude-Code-style compaction, project/state storage, short + long term), **context management** at org / app / user layers. Bertrand: *"content is context for AEM. Skills would be context as well. User preferences, what the user has been doing... different layers of context."* Skills alone = one piece of context only. **Bertrand's explicit ask: AEM must document what it needs from the foundational Adobe layer.** This is the actual scope seed for Ian's 1-pager — context mgmt + memory mgmt + multi-layer context, beyond skill files. Ties directly to Loni's context reframe.

**6. 🆕 Ian deploy-to-stage skill.** Ian: *"I have a skill to deploy these sort of things to a single pod in stage, which Claude will do for you."* Claude-driven single-pod stage deploy. Bertrand referenced developer console + I/O runtime as logical fit. **Enabling asset for the per-team AOv2 AS-IS staging evaluation** — reference it in the broadcast so teams have a deploy path.

**7. 🔴 Greg Klebus — customer escalation.** Rosh + Genentech want to go big on agents, deployed across **multiple IMS orgs**. AOv1 today **limits agent scope to 1 IMS org**. Greg asked Ian to join customer architect / implementation-partner conversations as eng/arch rep — future-proof deployment across **AEM + AJO + AEP**. Greg will summarize outcome. Expected to recur with larger customers. **Concrete customer-driven requirement** — feed into Ian's North Star input + Pedro's portfolio requirements lane. Track Genentech + Rosh as named drivers.

**8. Philippe demo (agent automation) — substance captured.** Governance Agent learning: customers don't just want better tooling, they want to **change the whole flow**. Demo: asset update → governance check → pass = one action, fail = create Jira bug with reasoning/suggestion/annotation on the asset. Triggers: asset change, Jira ticket events. Deterministic flow + can call MCP / start flow from an MCP code event. Built for an upcoming **Samsung demo**. Philippe's framing: shift from tooling to customer self-service, *"we are not scalable now,"* integrate at the CR start or push info back at the end. Pedro offered to share docs/pointers with the group; Philippe terse (*"Yeah, well, I'm sure you do."*) — competitor-frame caution holds.

**8b. 🆕 Bertrand reaction to Philippe demo — positioning unclear + proliferation-governance concern (25:40-27:35).** Bertrand: impressive ("power of web coding") BUT *"I'm not sure where it fits... this is a developer-centric tool... a UI like this could be in the Adobe Developer Console."* Target persona unclear. **Open PM concern (verbatim-anchored):** *"if all of us start coming up with things like that every other week, that's going to be very challenging to manage in product management... what should get attention, priority... lots of ideas can be implemented quickly and how do we sort that out? Where is our business going? What is it worth investing in business-wise beyond the technology?"* — Bertrand naming the **initiative/skill-proliferation governance gap in the open**. Direct tie to the Workshop Foundation skill-proliferation session Bertrand asked Pedro to facilitate (May 12 memory). Reinforces that ask publicly.

**9. 🆕🚨 Gilles Knobloch — skills-portable-NOW, decoupled from AOv2 (15:38-16:55).** Gilles asked his team: can we move into skills development WITHOUT waiting for AOv2? **Experience Production Agent team already did it** — defined skill files, plugged into **AO V1 with zero AOv2 dependency**, skill files portable later (move to AOv2, integrate in Experience Workspace). Motivation = team "stuck in velocity." Demo recording forwarded. *"A nice compromise — get benefits of the future architecture without having to wait for it."* Pedro committed: *"I'll take your demo, Gilles, and just see where we can spread it."* **Material: this operationalizes Decouple-Architecture-Ask-from-Platform-Commit-Timeline — skills work proceeds regardless of AOv2 commit. Distribute the demo across agent teams.**

**10. 🆕 Gilles NL-flow vision + localhost deploy gap (27:49-28:58).** Wants natural-language flow description (not box-connecting); checked Philippe repo, not obvious. Vision: customer meeting → transcript → auto-generate flow → next-day confirm with customer → functional demo. Deploy gap: Philippe tool runs localhost (*"do we deploy it to? I see localhost."*) → leads into Ian deploy-to-stage skill + Bertrand dev-console / I/O-runtime fit.

**Pedro proactive actions (revised post full transcript):**
- **Get Gilles' EPA portable-skills demo recording; distribute across agent teams.** Pedro committed in-room. This decouples skills work from AOv2 commit — high-leverage, unblocks velocity, aligns with the Decouple knowledge entry.
- **Seed Ian's North Star with now-rich content:** Bertrand's Adobe-Harness layered context + memory mgmt requirements + Ian's "avoid AOv1 onboarding/license-reporting failure modes" + Greg multi-IMS-org + EH context-reading. The seed is no longer thin — scaffold the doc and hand Ian a populated draft.
- Convert verbal AOv2 framing into written broadcast (evaluation not decision, AS-IS staging, Ian deploy-skill pointer, Gilles skills-portable-now path).
- Escalate Ian 1-pager via Bertrand forcing-function Slack.
- Drive roadmap-deck coverage for the 6 agents before Fri May 22 cut.
- Capture Greg multi-IMS-org + Genentech/Rosh as portfolio requirement; get Greg's summary.
- **Accept Workshop Foundation skill-proliferation facilitator role** — Bertrand's in-meeting proliferation-governance lament is the public reinforcement; the forum is the answer to his own concern.
- CCF reconcile: Discovery + Governance only, July 17, deprioritized.
- Bank host role; offer standing backup-host for Yanira.
