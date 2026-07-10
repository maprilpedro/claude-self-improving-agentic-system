---
name: aem-agents-intelligence-aai-project-context
description: "Full context on the AEM Agents Intelligence project — agent reporting platform, AO 2.0 liaison, Loni+JM May 11 deck, three-tier reporting, agent ownership, AAI stakeholders. Sister file to project_experience_hub.md."
metadata: 
  node_type: memory
  type: project
  originSessionId: 5f12dcf1-db3b-44ce-bf6c-50e0a17cb9e9
---

> **Two-project split — Phase 2 structurally complete (2026-05-13).** AAI vault folder at `2026/AEM Agents Intelligence/AAI - Project Folder/`. Companion `project_experience_hub.md` covers EH. Meeting Notes moved to neutral `2026/Meeting Notes/` (2026-05-13). AI-Assistant legacy folder retired. No legacy folders remain.

> **📦 Archive discipline (weekly shards; last restructure 2026-07-01).** Old context lives in per-ISO-week shards `project_aem_agents_intelligence_ARCHIVE_<year>-W<wk>.md` (+ long-form reference in `..._ARCHIVE_reference.md`), mapped by `..._ARCHIVE_INDEX.md`. **To find old context: read the INDEX first (dates + topics per shard), then `rtk proxy grep` the shard — never full-Read a shard.** This active file = hot state (last ~1 week of events, currently **07-08→07-09**) + the compact durable reference below. **Cap rule, enforced by `scripts/archive_memory.py` (run in `/consolidate` Step 5): keep this file < ~20K tokens / one-shot-readable; event blocks older than ~2 weeks auto-archive to their weekly shard + the index rebuilds.**

> ## ▶️ RESUME HERE — left off 2026-07-09
>
> ### 🔑 2026-07-09 (soir) — THE COHORT THREAD RUNS TO 20 REPLIES: Bertrand answers for Pedro, Ankur attacks the hard dependency, and the parity list starts writing itself
> Thread `1783584402.501589`. Read in full 07-09 evening. What is new since the 4-reply read banked earlier the same day:
> - **🔑 BERTRAND, 17:08 (`1783609683.591049`), unprompted, answering Corey's "what part does AEM provide in provisioning?":** *"all customers with an AEM cloud (CS/AMS) license should be enabled with agents by default - with the ability to opt-out if they decided to do so. So there isn't really any provisioning steps related to the Agents SKU being licensed or not."* → **Two different objects, keep them apart.** This is the **AEM agents entitlement** (default-on, opt-out). Ken Russell's runbook is **Coworker provisioning per org** (git segment + two Unified Shell LD flags). ⚠️ **Consequence for the comms lane:** if agents are default-on for every AEM cloud licence, the audience is not "the 318 SKU orgs" — the SKU/TBYB ownership-split hypothesis with Akin needs re-testing against this. **Also: Pedro's manager answered a question addressed to Pedro's own thread, 2h after it was posted.** Same shape as the manifest question. [[feedback_position_over_merit]].
> - **Ian Boston, 17:28 (`1783610937.049229`)**, on Bertrand's opt-out: *"We need a customer friendly opt out eventually that is enforced everywhere. Currently, its not clear and requires a customer support ticket. It should be bullet proof and self service, probably in Adobe Admin Console."* = a new production-readiness requirement, stated by the architect, in Pedro's thread. Add to the readiness bar.
> - **🔴 ANKUR ARORA, 15:33 (`1783603985.601399`), UNANSWERED: *"Do all AEM agents need to be supported from the outset, or can support be added in a staged manner as individual agents become available?"*** → **This is a frontal question to Pedro's hard dependency** ("ALL agents must port before ANY AEM customer migrates", his stated position to Rachel 07-08, rationale = EH exposes all agents on one bar). That dependency is his defense against Horia's counter-pressure. If staged support is allowed, AEM migrates earlier and the protection weakens. **Answer it deliberately; do not let it drift** (the manifest question drifted 2 days).
> - **🟢 THE PARITY LIST STARTS WRITING ITSELF. Corey Dulimba, 15:03: *"For UE we have an integration with the rail but believe we need to do work there to support the new ui."*** = the **first concrete entry** in Josh's undefined "critical rail features mirrored onto the panel" list. Shankari: *"None of this is available yet"* (2 facepalms) then *"ready by Cohort2 timeframe."* → Ask each owner for theirs, compile, publish. [[An Undefined Gate Is a Date Nobody Can Give]] (parked).
> - **⚠️ THE RAIL: "BECOMES" vs "LINKS TO" — an open contradiction, not yet resolved.** Shankari posted `CurrentTransitions_deprecations.png` (`F0BG4APMYHK`, 13:04) from the AEP PMs. Old surfaces carry two different labels: **"BECOMES COWORKER"** on the full-screen ones, **"LINK TO COWORKER"** on the one with a right-hand panel. **⚠️ The label-to-screenshot mapping is an inference from layout, not from readable product chrome — do not act on it as fact.** Pedro had told Apoorva 40 min earlier (12:22:56) *"the rail becomes the Coworker chat panel, same place, same behaviour."* **Likely reconcile (unverified): two states, not two theses** — cohort 1 has "no in app rail experience exists", so the interim can only link out; the panel replaces the rail at cohort 2 (Shankari's own "ready by Cohort2 timeframe"). Corroborating signal: **Sorin on stage 07-08 could not find a rail→full-screen continue button.** **PEDRO'S CALL 07-09: route it to Eugene + Sorin** (Sorin has stage access — he can look rather than ask). Do not post publicly, and do not write it into the Saar note, until they report. Decides Eugene's question: does the panel read/act on the page, or does the entry point degrade to a launch button.
> - Shankari also answered Prashant/Apoorva-adjacent questions; Pedro's **TBYB question from Apoorva (`1783587171.680399`) is still unanswered** at end of day.
>
> ### 🟢 2026-07-09 — THE SAAR NOTE WRITTEN + AUDITED (vault: `AAI - Project Folder/AEM to Coworker — Note for Alexander Saar (2026-07-09).md`, status DRAFT)
> Commissioned by Yanira (group DM `C0AUP306D0V` w/ Jaclyn Eckersley, `1783601859.437939`). Structure: the wrong working assumption → the cohort facts (screenshot, not a retyped table) → three real risks (an estimate became a date · the parity gate has no definition · porting ≠ ready) → **what AEM has already closed** (legal, security) → **9 asks with owner + date needed** → the pattern (three artifacts nobody owns) → what AEM owes back.
> - **🔑 PEDRO ASKED "est-ce que tout est sourcé ?" AND THE AUDIT CAUGHT THREE DEFECTS** ([[feedback_audit_outward_artifacts]] working exactly as designed): (1) "Security is **booked**" was an overstatement at the time of writing (Pedro had posted "setting up"; he confirmed after that the meeting is set — **Tue 2026-07-14 with Lars, Catalin Luta, Yanira**); (2) the threat-model requirement was carried as a fact but sourced to one engineer's passing Slack line — **Pedro chose to drop the attribution and own the claim himself**, which is a deliberate exposure, not an oversight; (3) "Ian… asked me about the switch-off" was a paraphrase — replaced with his verbatim.
> - **✅ THE COHORT SLIDE IS NOW VERIFIED FIRST-HAND** (`F0BG027END9` opened directly, not quoted from notes). Everything the note cites holds: the three "Exclude: AEM cloud service and WF" rows (cohorts 0/1/2), cohort 1 = JUL 15 + *"Product UI ('josh's UI') full screen only (no in app rail experience exists)"*, cohort 3 = AEP/RTCDP/AJO/CJA **+ AEM, WF** ~1500 with **no date (TBD)**, cohort 4 = all ~2600, and *"AEM agent to skill migration is tentatively scheduled for EOAug"* sitting in cohort 3's **"Parity gaps?"** row while the same column's **"What happens to AIA?"** row reads *"AIA is deprecated."* **⚠️ ONE NUANCE TO CARRY:** *"Full parity, no gaps"* is a **status cell in a "Parity gaps?" row**, not an explicit gate clause. Reading it as AEM's protection is **Pedro's interpretation** — defensible, and now labelled as such in the note's source table.
> - **Added after the audit:** a 9th ask on **sandboxes** (the Coworker runbook assumes an AEP sandbox; net-new AEM orgs have none — Anurag's unanswered question; "who creates it and at whose cost" = Pedro's framing), and a clause separating **Coworker per-org provisioning** from **Bertrand's AEM agents entitlement**, so Saar cannot read the ask as already answered by his own Sr Director.
> - **⚠️ TWO LINES STILL QUOTED FROM NOTES, NOT RE-READ:** Josh's *"AEM and Workfront have both done stuff with the rail that have critical features"* and Horia's *"that's official, Pedro."* Callout left in the file. Saar's org is where Pedro will be held to them.
> - **🔴 BLOCKED ON TWO DECISIONS ONLY PEDRO CAN MAKE:** (1) **who sends it** — [[Don't Let Program Managers Carry Your Liaison Relationship]], the April/Conrad shape with the same PgM; recommendation Pedro sends, Yanira cc. (2) **Bertrand sees it first** — [[Validate with N Before Sharing to N+1]]; Saar is a VP outside Pedro's chain, Jaclyn (in the commissioning DM) reports to Saar, and the note carries Pedro's own EOAug estimate.
>
> ### 🔴🔑 2026-07-09 — COWORKER / EPA CREDIT MAPPING SYNC (HELD, ~42 min; transcript `Meeting Notes/Pricing/20260709 - Coworker - EPA Credit Mapping Sync.md`, 2950 lines, ingested via 4 parallel extractors). ⚠️ **ATTRIBUTION: the `CR BASL 05 / WALENSEE VC (4)` mic = PEDRO** (Yanira: "Pedro, you did start the canvas, right?"; Satya's "thanks, Peter" = Otter garble of Pedro). Attendees: Pedro, Yanira Castaneda, Corey Dulimba, Felix Delval, Mayank Agarwal (Forms), Satya Deep Maheshwari (Forms), Natalia Venditto, Gilles Knobloch, Andreea Miruna Moise.
> **= THE HEADLINE, and it is worse than "Bertrand hasn't decided the model yet": THE CREDIT METRIC HAS NO TECHNICAL SUBSTRATE. Nothing is tracked. Nobody ever looked.**
> - **🔴 Corey Dulimba, the EPA owner, 00:06:08, verbatim: *"I have no idea what we're doing with credits. I've never tracked them. I've never looked at them."*** And 00:07:35: *"How that has actually been working in real life. I have no idea. No one's ever asked me and I have not looked at it."* **Felix Delval:** *"I believe nothing has been tracked from a technical perspective on the usage apart from actual [token] usage."* The existing weights (a content update "50 credits", a brand Experience agent "25") are **November token estimates by small/medium/large** that Felix calls *"probably completely wrong."* → **Legal's GTM gate ([[reference_coworker_faq]] lane, Ellis 07-09) is not waiting on Bertrand's decision. It is waiting on a measurement that does not exist.** Escalate the ask accordingly.
> - **🔑 COREY SPLITS THE AXES (bank the frame, it sharpens Pedro's own):** *"this is the value realization discussion… and not credits, because I think those are two completely separate things. There's the monetary aspects and then there's a value realization aspect."* Pedro's VR = operations delivered (held against Christian 07-08) survives; what does **not** survive is treating credits as the same object. The realized-operations→credit-weights deliverable is a **bridge between two axes**, not one metric.
> - **🔴 PUBLICATION IS THE VALUE EVENT AND IT IS NOT TRACKED.** Felix: *"Publication is the real value delivery, but it's hard for us to track it down."* Corey: *"That publishing right now is like a manual task… doesn't have anything to do with the agents. So we would need to tie those events together somehow as the ultimate form of value that they've actually used this AI."* **🟢 THE WORKING PRECEDENT EXISTS — Mayank Agarwal (Forms): *"we embed a GCL property in the published forms, and from there we get to know that this form is converted through the AI Agent."*** = a shipped attribution pattern to borrow. Easy on JCR, harder on DA.
> - **Two objections that kill a naive token→credit weight.** **Natalia Venditto:** *"Sometimes it's more expensive to run a pure LLM conversion on content than something that seems a lot more complex… a one-to-one mapping to tokens may not be very realistic to the side of the customer, at least in perception"* → proposes clustering / flow-based value; Pedro called it "an interesting way forward". **Felix, the leakage case:** customers ran Forms skills on **their own harness**, then moved them back to Adobe *because Adobe discounted the price* → *"does [charging] have to be bound on the action, does it have to be bound on the usage?"* Charging basis is **open**.
> - **🔑🟢 THE METERING POINT IS PEDRO'S EXISTING LANE.** **Satya Deep Maheshwari:** *"there's a mention of our MCP gateway for Coworker, wherein all MCPs to be accessed would go via the gateway… that would be the point where some metering would be put into place."* **Pedro, same axis:** *"we are starting to push the teams to unify behind the One AEM MCP… [as a] central point of not only interfacing, but also measure and login."* → **the manifest/One-AEM-MCP consolidation work Pedro already owns is the place credits get counted.** Instance of [[Definition Ownership Is the Moat on Shared Data Infrastructure]] + [[Govern a Consistency Layer Over Primitives You Don't Own]]. Do not let this be discovered by someone else.
> - **🔴🔑 COREY HANDS PEDRO THE RECIPROCAL OF HIS OWN MORNING ASK, and he is right.** Pedro's 10:06 post asked every agent owner for an honest date + a Production Readiness date. Corey, 00:37:38: *"How can we provide a date when we're going to be ready if we don't know what we need to do to be ready?"* and 00:37:54: *"So you guys need to give us the information on what these need. And then once we understand that, then we can give you a date."* The cells he means: **security ORR, Langfuse traces, business reports.** Plus 00:34:43: *"This is becoming the V1 all over again. It's a complete nightmare."* → **the readiness dates Pedro is collecting are blocked on a requirements doc Pedro owes.** The `Production Readiness` ask is only a lever if it ships with the definition of each cell. See [[feedback_defuse_vs_defer]] — this is owed, not deflected.
> - **Pedro said `Production Readiness` here too, WITH security in it** (00:33:37): *"Ready for me does not only mean that we have migrated the skills, but also that we have sorted out the security auditing or security review for coworker… nothing is in place today, that the legal is also ready… So I call that the production readiness."* → the public 07-09 post omitted **security**; his spoken definition includes it. **Fix the public one.**
> - **Yanira relays Legal:** *"we met with Ellis yesterday [07-08], and from his side, he doesn't see it as a delta… there's no need for anything like PLA."* ⚠️ Two distinct threads — **migration paperwork** (no delta, closed) vs **the licensing metric that gates GTM** (open, and now known to have no substrate). Do not collapse them.
> - **🔴 COREY'S MIGRATION-ORDER POSITION (a position, not a decision — [[feedback_proposal_vs_decision]]):** move the **TryBuy customers first** ("that's already stood up, has 1500 customers using it… we need to get those try before you buy customers into the latest and greatest. That's why we're building the bridge, because there's people that are falling off"), **SKU customers later.** Pedro read it back: *"migration of the try before you buy customers, and then eventually a later migration of the SKU customers, right? That's what I'm hearing."* Corey: *"that's just my opinion. I'll do whatever people told me to do."* → **converges with Klaasjan Tukker's don't-migrate-twice proposal** and **inverts the assumed comms sequence.** ⚠️ Corey's "1500 TBYB" ≠ Pedro's 2,483 (pending Raul) — do **not** reconcile publicly.
> - **Cohorts relayed by Pedro in-room:** the rollout team acknowledged *"it will be catastrophic for those customers if they migrate into coworker by July 15th. So they went into that cohort approach"* → *"We will migrate you guys when you guys are ready. Whatever that means."* Corey's counter: nobody has given dates for the rail, onboarding or provisioning.
> - **Actions:** Corey → send Pedro the experience-lead doc with the "25 credits" figure + verify on a real customer dashboard whether a content update truly deducts 50. Felix → **get AEP Langfuse access** (blocked; gates Coworker token/VR tracing). Pedro → raise the credit breakdown with **Tina** (⚠️ likely **Tina Ngo**, PMM, owns the field-readiness deck with customer-facing credit info — *not* Tina Nicu; confirm) · check with **Tanju** what Coworker can trace customer-facing · update the GA-readiness canvas · get **Daniel**'s team the docs to scope the security review (⚠️ likely **Daniel Mrose** — Eng director, security + governance agent — *inference, confirm*) · **write the per-cell readiness requirements Corey is waiting on.** EPA: skills in Coworker "next week" (~w/o 2026-07-13).
> - **New stakeholders:** **Mayank Agarwal** (Forms — the GCL-property attribution precedent), **Natalia Venditto** (token-cost≠perceived-value; clustering proposal), **Toby** (readiness/infrastructure, Yanira met him), **Ovidiu** (ORR — "nothing needed from their side"), **Anurag** (supplied Forms indicators), **Arneh** (cited re the harness discount case).
> - **Knowledge:** no entry promoted. Cited + applicable: [[Definition Ownership Is the Moat on Shared Data Infrastructure]], [[Govern a Consistency Layer Over Primitives You Don't Own]] (the MCP gateway = the metering point), [[Metric Definition Ownership — PM Validates, Reporting Track Owner Implements]] (Corey/Felix implement, Pedro validates), [[feedback_proposal_vs_decision]] (Corey's TBYB-first = opinion), [[Raw Call Volume Is Mostly the Agent Talking to Itself — Classify Before You Headline]] (the token-count trap Natalia restates from the customer side). **New parked candidate:** "An Undefined Gate Is a Date Nobody Can Give" (2 independent instances: Josh's parity list 07-08, Corey's checklist cells 07-09).
>
> ### 🔑🔴 2026-07-09 — THE COWORKER PROVISIONING RUNBOOK EXISTS, AND IT STOPS AT AEM'S BORDER (Ken Russell, `#aia_coworker_convergence` thread `1783531819.764259`, his msg 07-08 22:32 `1783542769.756389`)
> Found while looking for "how do we onboard customers onto Coworker". Namita opened the thread on **contingency/revert planning for the July-14 cohort-1 rollout**; the provisioning process fell out of it. **This is the only written Coworker provisioning procedure that exists today.**
> - **The documented path (Ken, confirmed by Soumya Sharma's recap):** (1) **one git provisioning request per cohort** using the template at `github.com/Adobe-Experience-Platform/ao/issues`, which enables the org in a **segment in git** (`config/aep-aia/environments/prod/segments`); docs = `github.com/Adobe-Experience-Platform/ao/blob/main/config/README.md`. (2) **A Slack message to Mark Doten** to flip the Unified Shell **LaunchDarkly flags**. There are two: **"Enable Coworker"** and **"AI Kill Switch to remove AIA"** (Mark Doten). Order matters: "enable customers in advance of the launch darkly feature flag."
> - **De-provisioning (the escalation path):** same git template with the content deleted, marked as de-provisioning ("I'm hoping this is rare enough that it doesn't warrant a template"), **plus a Slack message to Mark Doten** — "we can handle how we currently do for try/buy, just a slack message is fine." Lianne Ramos captured it as an **"Escalation Process" tab** in the channel. **Flag backups if Mark is OOO: Stephen Gould + Mikaela Symanovich.**
> - **🔴 THE CAVEAT NOBODY IN THE THREAD PICKED UP — Ken, 22:33, verbatim:** *"Please note: this will not address enabling any additional CJA data views, or hydration of data stores etc. **We are assuming these customers have that already in place with AIA.**"* → **the procedure is written for AEP customers who already have the data plumbing.** It is silent for **AEM-only / net-new AEM orgs with no AEP sandbox** = Anurag's Q2, now stated as a declared limit of the runbook by the engineer who wrote it, not an AEM worry. **This is the sharp end of the provisioning ask.**
> - **🔑 There is no bulk path, there is a file and a human.** A git ticket per cohort + a Slack message to one person, whose backup Namita had to ask for. Fine for 200 customers. Unasked for AEM's ~318 SKU + ~2,483 TBYB. **Ken wants to retire step (1) via a "trial" SKU in AEP Provisioning** — Namita asked who is building it (Akin/Shankar?), **nobody answered. The trial SKU does not exist.** Stephen Gould's open question: once the Coworker SKU exists, is it provisioned through Authorization Platform? Ken: once it exists, **Rubin will need the union of the SKU + the discovery service** (ties the Angela/Rubin lane).
> - **Reframes the Saar ask #7** from "give us a bulk provisioning path" (Ken would answer: it is documented) to **"the documented path is a git ticket plus a Slack message to one person, and it declares that it assumes AIA-era data plumbing our AEM-only orgs do not have. What replaces it at AEM scale, and when does the trial SKU exist?"** Also partially answers the mid-July-trigger condition (a): Victor's "bulk operations for IMS org Ids" = the segment file, not an end-to-end path. **Knowledge:** none promoted. Instance of [[feedback_confirm_ask_before_producing]] (read the source before asking for what already exists).
>
> ### 🟢🔑 2026-07-09 15:55→16:04 — AEM-SIDE SECURITY REVIEW SET UP, AND IT SURFACES AN UNNAMED READINESS ITEM (Slack, screenshot `screenshots/20260709-security-review-threat-models.png`)
> Pedro: *"Security Review for AEM Coworker now becomes how — shall i organize a sync meeting inc. Lars monday next week."* Participants: **Lars** (⚠️ NEW, surname unknown, security-side, no memory entry yet), **Catalin Luta** (AEM eng — ⚠️ NOT Catalina Preda, the AEP evals/golden-set owner; two Catalins in this migration), **Yanira Castaneda**. Lars is out Mondays → **Tuesday 2026-07-14**, which is also AEP's cohort-1 flip day.
> - **🔑 THE FINDING, dropped in passing by Catalin: *"all the teams have to redo their Threat Models."*** Nobody in the thread reacted. **This is a per-team, per-agent deliverable triggered by the execution surface changing**, and it appears on **none** of Pedro's lists (GA readiness canvas, Day-After Map, the Saar asks, the public `Production Readiness` definition). → **The public definition needs one more word: skills ported + provisioning + legal + SECURITY + onboarding.** Corey Dulimba asked in-thread the same morning (`1783602012.888049`) *"what part does AEM provide in provisioning, legal, onboarding?"* — the threat-model rework is a concrete, sourced answer for the security half.
> - **🔴 The confusion Yanira describes is real and inside AEM eng.** Catalin, an AEM eng lead: *"what's AEM coworker?"* then *"ok, pfew. I thought we have yet another implementation."* = a live, dated, in-org instance of the exact confusion the Saar note exists to kill. Better evidence than any abstract claim, and the concrete-scene register Bertrand prefers ([[feedback_bertrand_concrete_first]]).
> - **Position:** flips the Saar security row from "AEP's reviews do not exist" (a complaint) to "AEM's review is booked for Tuesday and has already produced a requirement; the Coworker-surface review and AI Ethics are still owed" ([[The Game Itself — Position Over Merit]] — show your half delivered, then invoice theirs). **Knowledge:** no entry. Watch for a 2nd instance of "the migration's real cost lands as rework in teams nobody consulted."
>
> ### 🟢🔑 2026-07-09 — LEGAL SYNC (HELD, ~25 min; Yanira organizer; transcript `Meeting Notes/Legal/20260709 - Legal: AEM Agents -> Coworker Sync.md`). ⚠️ **Medium fidelity — two recording gaps (0:44→4:41, 19:16→21:19).** Attendees: Pedro, Yanira Castaneda, **Ellis Dobkin** (Legal, works AEM agents w/ Yanira; did the Agent Orchestrator legal work + the P42 PLA), **Meredith Elder** (Legal, Ellis's team, product council, supports Commerce — NEW, first meeting with Yanira/Pedro).
> **= THE HEADLINE: legal is not the blocker. GTM/credits is.** Same morning Pedro publicly coined `Production Readiness` = skills ported + **provisioning + legal + onboarding**. By lunch one of the three came back green.
> - **🔑 AI rider = not an AEM concern (Ellis).** It is "provisioned at a higher level based on a SKU" and is a requirement for **the whole Coworker, not just the AEM agent**. Same **risk-based structure** already used for **LLM Optimizer** (free version inside AEM Sites, no additional paperwork) and on the AEP side. *"Should not be a concern."* **The gating function = the contract check at provisioning**, i.e. legal follows the SKU, not the feature. Pedro's framing that opened the door (his own words): Bertrand told him AEM and Coworker "share the same infrastructure… it's only skills and the files on the same infrastructure. They will be provisioned a similar way."
> - **🔑 NO NEW PLA is the EXPECTED outcome — not a decision** ([[feedback_proposal_vs_decision]]). Ellis: *"the likely outcome [is] there shouldn't be a PLA for it."* Rationale: **a PLA was already done for Project 42 and all the agents underneath it**; "if the answer is going to be the same for all of them, then no need to do the additional work." He still wants the **legal-intake questions** run to confirm + catch edge scenarios, formally by email.
> - **The two standing legal triggers** (Ellis, top-of-mind, applies to any change): (1) **does it change how customer data is processed**; (2) **new third-party technology / new LLMs**. Plus the standard third-party-licence / open-source check on any new code.
> - **🔴 AI ETHICS = a separate, UNSTARTED track.** Yanira has not spoken to AI Ethics. **Coworker is running its own AI-Ethics review at the surface level.** Ellis's recommendation: same workflow — one strategy for everything released *under* the Coworker surface. **Yanira's action: identify who the Coworker team works with on AI Ethics and confirm there is no delta for AEM.** = a hole in the readiness bar nobody had named.
> - **🔑 GTM IS THE REAL GATE, AND IT ROUTES THROUGH BERTRAND.** Ellis + Meredith cannot paper anything until the **licensing metric** is defined — "a different flavor than Agent Orchestrator… the credits and the agents consuming different amounts." Pedro: *"Bertrand is crystallizing his ideas right now on how to track and report to customers. I can ask him for a first draft."* Ellis: *"keep us posted and we'll help make sure it gets papered appropriately"* + *"as soon as we can start talking about the go-to-market piece, the better."* → **direct hook into the #aem-agents GTM credits thread (`1783420878.740519`) where Pedro already claimed the realized-operations→credit-weights mapping and committed the EPA reconciliation test.** Legal is now a *downstream consumer* of Pedro's deliverable. That raises its priority and gives it a second, non-Bertrand sponsor.
> - **GTM ownership question (Meredith, new to the space):** who is the GTM partner for agents? **Ellis: Kristal** was the primary driver of the GTM piece for Agent Orchestrator; Ellis's role = flush out the discussion at this level, then hand to Kristal once Bertrand's thinking firms. Give Kristal a heads-up. (Meredith supports Commerce; on her side of the legal team **Kristal** and **Jacqueline** do GTM. ⚠️ **"Jacqueline" here ≠ Jaclyn Eckersley (FinOps)** — do not merge; she co-wrote the intake checklist with Yanira and Ellis wants her in the deep-dive.)
> - **Scope confirmed by Yanira:** *"we don't have any new agents. It's really a migration from AOv1 to Coworker."* **Exception = the Onboarding agent** — never in the GA cohort, never on AOv1, straight to AOv2/Coworker, own track, already met with Pedro. Third independent confirmation of the Onboarding-agent exception (Rachel's call 07-08, Reasor's canvas row 07-07, here).
> - **Pedro's open question, unresolved:** the **other agents** that are Coworker-bound or customer-exposed but outside this migration (**Experience Workspace** named) — generalize or case-by-case? Ellis: they will have had separate legal reviews; what remains is **GTM + how the credit structure is documented**. Pedro conceded AEM needs its own clarity here and offered to draft the map.
> - **📤 PEDRO'S DELIVERABLE, committed in-meeting: a higher-level "world of AEM agents + what's planned for Coworker" WIKI for Legal.** Ellis asked for it directly ("some internal wiki that could help us understand… just to give us that visibility"); Yanira: the **GA readiness canvas is too detailed**, "we just need a higher level view." Flow: Pedro drafts → iterate with Yanira → then in front of Meredith. = a third audience for the readiness canvas material, and a legal-facing artifact with Pedro's name on it.
> - **Pedro's stated fear, on record:** *"my main fear is of starting too late and then having blockers that we did not anticipate."* Ellis's answer: no major blockers, PTO light on their side.
> - **⚠️ CLAUDE EXPOSURE ([[feedback_keep_claude_private]]).** Transcript line 461, Pedro: *"Maybe I can quickly ask **Claudia** to shoot me a wiki as a good basis to recap all of that."* "Claudia" is the known Otter garble of **Claude** (already in the glossary). If he said it as transcribed, he named his AI assistant in front of Adobe Legal and Yanira. Not fatal, and Legal is the least dangerous audience for it, but the transcript is now the artifact. Worth a conscious decision rather than a habit.
> - **Knowledge:** none promoted. **Candidate frame at n=1, do not force** ([[feedback_consolidation_without_substance]]): *"legal clears cheaply when the new thing inherits an existing SKU and an existing umbrella review — the gate then migrates to pricing/GTM."* Two clean legs here (AI rider inherits the SKU; PLA inherits P42's umbrella) but one meeting. Watch for a 2nd instance. Cited and applicable: [[feedback_proposal_vs_decision]] (the no-PLA expectation is not a decision), [[Metric Definition Ownership — PM Validates, Reporting Track Owner Implements]] (the licensing metric — Pedro validates the definition, Bertrand's GTM track implements), [[feedback_position_over_merit]] (the Legal wiki = a lane artifact requested, not volunteered).
>
> ### 🟢🔑 2026-07-09 10:06 — PEDRO POSTS THE COHORT HEADS-UP to `#aem-agent-owners-alignement` (`1783584402.501589`) — the comms lane's first outbound act as named owner
> Decided in-session: send the heads-up **before** the written confirmation lands. Rationale = two-way door ([[One-Way vs Two-Way Doors]]) — a wrong internal heads-up is one post to correct; silence while teams plan against July 15 is not. Sourced to **roles, not names** (Pedro's own call: "ils ne connaissent pas ces gens") — "the AEP team running the Coworker rollout" + "the team building the Coworker surface said the same thing independently." Attached the **WIP AEP Coworker Chat rollout plan screenshot** (`F0BG027END9`) + stated the base publicly as **"around 2k6 inc TBYB, SKU"** (rounded — the 318/2,483 split stays out, still pending Raul). cc: Bertrand, Yanira, Ian Boston, Corey, Philippe, Daniel Mrose, Apoorva, Shankari.
> - **🔑 THE MOVE: Pedro coined `Production Readiness` as a named ask** — *"That is not the day the skills are ported. It is the day the whole thing works for a customer, with provisioning, legal and onboarding done."* Nobody in the Rachel / Josh / Babu rooms had separated the two. He now owns the distinction **and** the request for the date. Second ask = agent owners re-state honest delivery dates ("A later date I can explain is much easier for me to carry than an early one we miss"). = the readiness bar being written by the person who benefits from writing it ([[The Game Itself — Position Over Merit]], "write the framework"; [[Govern a Consistency Layer Over Primitives You Don't Own]] instance shape).
> - **Framing held (Pedro's own, replacing my draft):** AEP decommissions in **cohorts**, sequencing takes AEM's readiness into account, *and* — the hinge — **"we should not slow down… AEP still has to give dates to their leadership… If we do not give them something we believe in, they will work with whatever they have."** He refused the reading where the cohort news buys slack. Consistent with Horia's counter-pressure (AEM = critical path, 07-08).
> - **⚠️ TWO UNANSWERED QUESTIONS SAT IN THIS CHANNEL WHEN HE POSTED OVER THEM:**
>   - **Bertrand, 07-07 15:08 — *"Seeing quite a few AEM manifests in Coworker today. Who owns what?"*** Two days unanswered, in Pedro's own channel, from his manager, on **exactly** Pedro's manifest-curation lane (Reasor collision list, `aem-aia.yaml` = only `aem-aia-extensions` installed, excat/epa/forms out). He has the answer cold. Answering it = the [[reference_aov2_marketplace_manifest]] correction delivered to the person who ranks him. **The dog that didn't bark.**
>   - **Corey Dulimba, 07-07 20:36 — *"Are there product demos that walkthrough the ins and outs of co-worker and its capabilities?"*** = the exact Coworker-demo action Pedro already secured from Horia at the Rachel call (Horia presents, brings Namita + Sergey, lands in Yanira's weekly). Answer = "yes, I'm organising it" — a one-line ownership reply, Corey = the first-testeur rule stakeholder.
> - **Knowledge:** no new entry. Instances cited: [[feedback_position_over_merit]] (the naming move), [[One-Way vs Two-Way Doors]] (send-before-confirmation), [[feedback_bertrand_concrete_first]] (screenshot + rounded number). Voice deltas → Calibration #4 in [[feedback_draft_in_pedros_voice]] (4 rejected drafts: aphorisms = the tell).
>
> ### 🔑🔴 2026-07-09 11:41→12:25 — THE COHORT POST GETS ANSWERED BACK: 4 replies, and Pedro's own estimate is already an AEP date
> Thread `1783584402.501589` (#aem-agent-owners-alignement). **The comms lane's first real test — agent owners now bring their customer questions to Pedro by name.**
> - **🖼️ THE DOC ITSELF (screenshot `F0BG027END9`, "ROLL OUT PLAN COWORKER CHAT — Documented Jul 6"). Read it before answering anything cohort-shaped.** Five columns. **Cohort 0 (Today)**: AEP/RTCDP/AJO/CJA ~20 customers · AO UI full screen · *"AEM & WF Skills not available"* · AIA "Can be accessed". **Cohort 1 — JUL 15**: same apps, "that are in the trial or have the sku", **~200** · **"Product UI ('josh's UI') full screen only (no in app rail experience exists)"** · AIA **deprecated**. **Cohort 2 (TBD)**: ~500 · full screen **& rail** · ***"Select a handful of AEM customers to fold in for testing"*** · AIA deprecated. **Cohort 3 (TBD)**: AEP/RTCDP/AJO/CJA **+ AEM, WF** ~1500 · **"Full parity, no gaps"** + ***"AEM agent to skill migration is tentatively scheduled for EOAug"*** · AIA deprecated. **Cohort 4**: all customers ~2600 · AIA deprecated across all customers. **Cohorts 0/1/2 all say "Exclude: AEM cloud service and WF, regulated industries that have lead time for approval."**
> - **🟢🔑 THE WRITTEN PROTECTION ALREADY EXISTS AND PREDATES THE ASK.** Dated **Jul 6** — two days before Pedro asked Rachel in the call for an official statement. It says AEM is out of cohorts 0-2 and that **AEM's cohort requires "Full parity, no gaps"** before AIA deprecation. He does not need a new statement so much as this table **shared, dated and owned**. Chase that, not a fresh sentence.
> - **🔴 THE BOOMERANG: Pedro's own hedged estimate is now AEP's written date.** He said "end of August" to Rachel in DM (07-07) and in her call (07-08). The Jul-6 doc's cohort-3 cell reads *"AEM agent to skill migration is tentatively scheduled for EOAug"* — in the same column that deprecates AIA. **Ian Boston read it exactly as written** (11:41): *"Looks like the tentative switch off of AI Assistant for AEM is end of August in the doc."* → **an estimate handed to the person who needs a date becomes their commitment, inside 48h.** This is precisely what the `Production Readiness` distinction exists to stop. **Knowledge candidate, n=1, do not force.**
> - **📤 PEDRO'S REPLIES (all SENT 12:13→12:25, posted as 7 chunked messages).** To **Ian** (`1783592029.207269`): *"the EOAug line sits in the cell labelled 'AEM agent to skill migration', which is the port… The same column also requires full parity and no gaps before AIA is deprecated, and cohort 3 itself carries no date. So EOAug is my estimate for the port. It is not a switch off date."* = the port-vs-readiness line held in public against the architect. To **Prashant Jain** (`1783592077`): no customer list published, only attributes; Rachel owns composition; will post it. To **Apoorva** (5 messages, `1783592546`→`1783592737`): entry point stays / rail becomes the Coworker panel / full-screen kept at same URL + redirect / **not "AIA with Coworker headless behind it"** but Coworker's own UI on the same endpoint / nav destination still argued inside Josh's team, check with Ryan Cobourn + Cole Connelly, "we're following up" / cohort 1 is full-screen-only, no rail — a large part of why AEM is not in it / on customers holding both: quoted the table verbatim, **named the ambiguity (does "exclude AEM cloud service" exclude the customer or the surfaces?)**, gave his read + its source (Horia), committed to Rachel's answer in-thread / SKU column is AEP-side, gates nothing for AEM.
> - **⚠️ STILL UNANSWERED: Apoorva's TBYB question** (*"what happens to the 1300 odd TBYB customers and their AIA user experience?"*). Pedro's reply stops at the SKU column. The table has **no row for AEM trial customers** — they are AEM cloud service, excluded until cohort 3, keeping AIA until then; the TBYB transition plan sits with **Akin**, and Klaasjan Tukker's open proposal is to move eligible trial customers straight to Coworker rather than migrate them twice. Also: the table's 1500/2600 do **not** reconcile with Pedro's own base read (318 SKU + 2,483 TBYB, pending Raul) — do not reconcile them publicly yet.
> - **Voice deltas (bank):** Pedro corrected my "Tuesday" → **"Wednesday"** (the Josh session was 07-08, a Wednesday; I had it wrong everywhere, and the **Bertrand message went out carrying "Tuesday"**). He softened my *"Nobody has said who decides"* → *"and we're following up"* — keeps the fact, drops the public ownership-vacuum verdict in front of Josh's team. He posts long answers as **chunked separate messages**, not one block.
> - **Knowledge:** [[feedback_position_over_merit]] (agent owners route customer questions to him by name), [[feedback_proposal_vs_decision]] (the table is a WIP doc, not a decision), [[feedback_voice_drafts_mark_inference]] (the exclusion read marked as his, sourced to Horia). No entry promoted.
>
> ### 🟢 2026-07-09 — WIKI PUBLISHED v4: the Josh minutes now carry BOTH sessions (`wiki.corp.adobe.com/pages/viewpage.action?pageId=3941701228`, retitled "…(2026-06-22) + Follow-up (2026-07-08)")
> Vault twin = `AAI - Project Folder/Coworker Rendering — AEM Working Session (2026-06-22).md`. Added: a top **Latest changes** summary, a **What changed since 06-22** delta table, 12 attributed topic rows, 9 actions, open questions, the "what this means for AEM" synthesis (labelled separate), and 12 stakeholders. Attribution resolved with Pedro: **the Basel mic = Pedro for the surface-selection exchange (00:17:18–00:18:40), Ashish for the starter-kit exchange (00:26:13+)**. "Pueblo" (prompt component) confirmed. "Brandon"/"Andy" (Coworker leadership) kept vault-only, off the wiki — surnames unknown, Otter spelling ([[feedback_audit_outward_artifacts]]).
> **The five deltas the page now records (all Josh, timestamped):** (1) naming — design says **panel**, leadership says **coworker chat**, "rail" retired; (2) **full-screen KEPT**, same URL + 302; (3) **hybrid/WebMCP REVERSED** — dead after Safari in June, now "hybrid is going to be everywhere", generic WebMCP tools already registered on every unified-shell page; (4) **Jul-31 = release ≠ migration** (verbatim, unprompted); (5) **AEM/Workfront not in cohort 1** (CDP/AJO/CJA), because "AEM and Workfront have both done stuff with the rail that have critical features". Plus: right-panel → **modal** by default; suggested prompts **survive**, Zeus owns the AO2 recommendation system + the AO1→AO2 prompt regression.
> **The white space Josh left:** *"critical rail features mirrored onto the panel"* is a phrase, not a list. Pedro's session-2 message asks the teams to fill it. Whoever writes the list sets AEM's migration date.
>
> ### 🟢🔑 2026-07-08 09:37 — CHRISTIAN MEYER gives detailed dashboard FEEDBACK (group DM C0BE2P6J00M, w/ Jabran): the traffic-review conversation is maturing into board design
> Jabran BUILT + shared the Splunk value/usage/customers dashboard (07-07 15:41, "aligned with the points in the wiki", + a PDF extract 07-08) → **Christian responded 07-08 09:37 with panel-level feedback** (constructive, engaged — the HOLD-era relationship is now co-designing the board):
> - **One AEM MCP traffic:** wants *# customers using One AEM MCP + top customers by usage* (this report now includes One-AEM-MCP traffic, not just Content MCP; ~340k HTTP monthly calls baseline).
> - **Value realization panels:** unsure about the first 3 — keep it simple: one panel = top customers ordered by calls; per-customer tool usage/intents → move to a *separate deep-dive board*; one = top tools by calls (already down below, bring it up).
> - **Overview:** use BOTH *HTTP requests AND Tool calls* as key metrics; **data-integrity flag — "not sure how to interpret New customers + Regular customers > Active IMS orgs, I'd expect New + Regular = Active IMS orgs"** (Pedro owes a read on this — either a definitional overlap or a counting bug); request-over-time not needed (lighten the board).
> - **Server-mix-per-customer:** unsure of value except maybe the overall split pie.
> = the CloudWatch-join watch (~07-08) advanced: Jabran engaged (built the board), Christian co-designing. **Pedro owes dashboard inputs** (Jabran asked 07-07; Christian's points 07-08). Still no upward numbers (HOLD holds until the traffic review is clean — Christian is literally still reviewing). Terminology intact ("Tool Calls" vs HTTP requests — Christian uses both as distinct metrics, matches [[reference_mcp_terminology]] + the [[Raw Call Volume Is Mostly the Agent Talking to Itself — Classify Before You Headline]] cut). **📤 PEDRO REPLIED SENT 07-08 (option A, firm):** accepted Christian's board cuts (both HTTP+Tool-calls headline, drop request-over-time, One-AEM-MCP # customers + top, server-mix → pie only) BUT **held the value-realization definition against the simplification** — Christian wanted VR = "top customers by calls" (= volume again); Pedro pushed back that VR must mirror his business reports = **operations delivered** (content updates accepted, pages created, forms created, permission changes, expired-asset searches), the specific tools read as operations, with by-calls customer/tool panels moved to the usage view. Reframed the "New+Regular>Active" flag as the open MAU-identity definition to close (2 likely causes named as inference: ≥100-call threshold on Active only / not-a-clean-partition), asked Jabran to confirm the exact definitions. = [[Metric Definition Ownership — PM Validates, Reporting Track Owner Implements]] held firm: defer to the data owner on layout, do NOT concede the value definition. Knowledge: no new entry (execution + a clean instance of holding the metric definition vs a data-owner simplification — watch for a 2nd before parking anything).
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

---

## Felix reports + report pipeline

> **Moved to `project_aem_agents_intelligence_ARCHIVE.md` on 2026-07-01** to keep this active file Read-able in one shot. Load the archive on demand when working this lane. Current state is carried by the RESUME event blocks above + the durable facts below.

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

> **Moved to `project_aem_agents_intelligence_ARCHIVE.md` on 2026-07-01** to keep this active file Read-able in one shot. Load the archive on demand when working this lane. Current state is carried by the RESUME event blocks above + the durable facts below.

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

