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

> ## ▶️ RESUME HERE — left off 2026-07-14
>
> ### 🟢🔑 2026-07-14 — THE POD DECK LANDS, AND IT CONTAINS A ROLE NOBODY HAS CLAIMED FOR AEM
> Pedro got `CoWorker_Enablement_Workshop.pdf` (10 July, Anjul opens it). Full read banked in **[[reference_coworker_pods]]**. Three things.
> - **It gives AEP's own vocabulary to the coexistence argument.** Type B = *"Customer Co-Innovation AI Pod — time-boxed co-innovation sprint."* A POD customer is **co-innovating, not migrating**, by the program's own definition. The ask to Rachel stops being an exception request and becomes "treat these orgs as what your own program calls them."
> - **🔑 The Named Generalization Owner is unclaimed for AEM.** Gate G2 of the Contribution Review asks literally *"Has a product owner accepted ownership?"*, and kickoff requires a *"Named Generalization Owner — PM from the relevant AEP/App area."* **AMEX is In Build. Coke is coming. Both produce artifacts that land in AEM. Nobody is named.** Same figure as the parity list — **claim it, do not request it.** Without it, the contribution fails G2 and AEM inherits a fork it did not choose.
> - **"No Snowflakes — Extend the Core Product"** is Pedro's manifest position written by AEP (*"contribute it back"*, ARB approval for exceptions). Backs Felix's *"have the different teams contribute their marketplace."*
> - **AMEX is a formal POD, "In Build", target "by July 2026"**, and AEP's own slide already lists its learnings as *"Engineering pace of execution"* and *"New Requirements"*. Thursday's onsite is a POD milestone, not a discovery call. **Klaasjan Tukker = Coworker PMM Lead** (more central than we had him). **Raj Patel = Overall Coworker Product Lead.**
>
> ### 🔴 2026-07-14 — THE EXCLUSION AMBIGUITY GETS TWO CLIENT NAMES, AND PEDRO ASKS IN THE ROOM WHERE THE LIST IS BEING REVIEWED
> **SENT 10:14**, Lianne Ramos's cohort-1 list-review thread (`#aia_coworker_convergence`, `1783960516.070839`), in front of Rachel + Namita + Klaasjan + Paul Midura: does *"Exclude: AEM cloud service and WF"* exclude **the customer** or only **the AEM surfaces**? Grounded on **Paul Midura's own app check** (07-13 22:49) — **ESRI has Sites + Assets as PAID licences**, **LeapPoint has AEM provisioned**. **The flags are per IMS org**, so a kill switch on a mixed AEP+AEM org takes AIA away on the AEM surfaces too, and those customers have nothing to fall back to. Pedro's read marked as his own in the post. **Ask, do not accuse** — Namita's check may itself BE the exclusion check.
> - **The third instance did not come from the field. It came from AEP's own list.** Watch the answer: it closes Apoorva's public question and tells us whether the AEM protection is real at org level or only written on a slide.
> - ⚠️ **Cohort-1 subset enablement is being discussed as 7/21, not 7/15, and Akin sends the system-admin emails.** AEM is excluded either way, so **the date does not move AEM** (Pedro's own call, and he is right — do not chase it). Akin owning the enablement email confirms the comms split.
>
> ### 🔴🔑 2026-07-14 — TWO USE CASES, NOT ONE. Pedro corrected me, and the correction is the finding.
> I collapsed Sergiu's backend ask into the co-innovation coexistence ask. **Pedro split them: *"il y a 2 use cases je pense. Un sans coworker UI (Sergiu) et un potentiellement avec (Coke, AZ, AMEX)."*** He is right, and separating them shows **they do not need the same mechanism**.
> - **(1) Backend only.** EDA + EPA built **proxies / a V1→V2 bridge**. Sergiu Coman, 07-14 10:51: *"The angle we want is not to enable customers for co-innovation in Coworker but rather to **enable all TBYB customers** so that we can provide better results in existing surface (old AIA)… we are not planning to use the Coworker UI anyway in the first phase."* **Coworker as engine, AIA as face.** Live instance of [[reference_aia_vs_coworker_axes]] — **Pedro spent a week arguing about the UI swap while his own engineers already did the backend migration.**
> - **(2) Coworker UI, deliberately.** AMEX, Coke, AstraZeneca. The customer *uses* Coworker. Coexistence is real, Mark's UX objection applies.
> - **🔑 THE MECHANICAL QUESTION THAT ROUTES BOTH.** Ken's runbook has two objects — the **git segment on `ao`** and the **Unified Shell flags**. **If the bridge needs only the segment, use case 1 is silent, creates no coexistence, needs no exception, and goes to Ken rather than Rachel.** If it needs the shell flag and the flag shows an entry point, **Coworker appears in front of the whole TBYB base with no comms — Pedro's lane.** ⚠️ **Felix and Sergiu contradict each other and neither noticed** (Felix: *"if the TBYB customer had **access to the Coworker UI**… we would be able make them use the bridge"*). **Asked in-thread 10:24** ([permalink](https://cq-dev.slack.com/archives/C0BARAMM89Z/p1784019870846209)) — quoting both, no fight staged.
> - **And he conceded to Sergiu in public, which planted his own distinction:** *"On being blocked, I agree with you for the backend path. The parity and cohort debate protects the customer's UI. If you are not using the Coworker UI, it does not gate you."* **Activation ≠ migration, proved by his engineers, said by him, in his channel.**
> - **Consequence for Rachel:** the ask shrinks back to **use case 2 only** — the co-innovation coexistence exception. Small, named, bounded. Sergiu's case leaves the perimeter and becomes a mass-provisioning question with a different owner.
>
> ### 🔴 2026-07-14 — THE CONTRADICTION NOBODY HAS RESOLVED: does the rail become Coworker on July 31 regardless of cohort?
> **Sorin Slavic** read the flag as *"they will turn on AI Assistant v2 for ALL tenants"* (07-08, a global flip). **Joshua Hailpern** says the July-31 rail release is *"a separate orthogonal question"* from migration. **Mark Doten** says the kill switch is transitional, needed only *"a couple weeks while the coworker rail gets set up."* → **The exclusion protects the DEPRECATION of AI Assistant. It is not established that it protects the RAIL'S APPEARANCE.** If the rail flips globally on 07-31, AEM customers see Coworker in their rail before their cohort. **Two different events, treated as one. Resolve before quoting either.** Written into the status doc as an open contradiction, not a claim.
>
> ### 📤 2026-07-14 — SENT: the pre-check to Mark Doten that may kill Pedro's own ask
> DM `D0AP5N5H87J`, 10:17 ([permalink](https://cq-dev.slack.com/archives/D0AP5N5H87J/p1784017034924929)): with flag 1 on and flag 2 off, **what does the customer actually SEE** — two entry points side by side, or Coworker somewhere separate? Pedro said in the DM that if they do not collide, *"there is nothing to fix and I drop it."* **Conceding that his own ask may be unnecessary is why he will get a fast answer.**
> - **The Rachel draft is written and HELD.** Sequence agreed: **Mark answers → one line to Bertrand → group DM Rachel + Mark (Yanira cc) → post the RESULT in `#aem-agent-owners-alignement`.** Not the war room: a public exception request in AEP's own room, the week they flip cohort 1, reads as AEM going around the plan, and a public "no" kills the coexistence position with witnesses.
> - **Apoorva and Felix stay OUT of the ask and IN the outcome.** Apoorva is the requester (her presence makes it field pressure, not an AEM product position); Felix is the executor (he maintains the co-innovation list, he needs to know once granted). **The result post solds three public debts at once** — Apoorva's Coke ask, her four operational questions, and Ankur's staged-support question — under Pedro's name in his own channel.
>
> ### 🔴 2026-07-14 — WHAT THE 15-CHANNEL SWEEP TURNED UP (window 07-13 → 07-14)
> - **EPA manifest live in prod Wednesday 07-15** — Bertrand's understanding, **not confirmed by Felix**.
> - **AMEX: Cedric Huesler proposes the phase-1 shape** (07-13 23:37, a **proposal**): *"we would load these 'react' based offers in Universal Editor and make them editable there… Coworker would produce a deep-link into UE"*; phase 2 = *"bring UE into Coworker - or bring Coworker into UE."* = Josh's hybrid path. **Sunish: full requirements doc *"by thursday"*** — the day of the onsite.
> - **🔑 A REAL GAP UNDER "SKILLS PORTED":** **Andreea-Daniela Balan** (07-14): *"the direct MCP tools are used directly, not a workflow we orchestrate. The LLM usually chooses the simplest way… I am not aware of any way to make it prioritise skills over MCP tools yet in AOv2."* **The LLM routes around the skills.** Porting a skill does not mean it gets used.
> - **Rodson Clavel opens a Coworker Panel bug bash (Wed)** *"focusing on cases that need to land for the July 31 cutover"*, with **a wiki where each team drops its test cases**. → **A second, open door for writing the parity list.** Cheap.
> - **Corey Dulimba** pushes AEMAGT-2319 (the false-success bug, Gilles reproduced twice) to high priority — *"that seems like an issue that is going to affect all chats"* — and files three more Coworker bugs. Readiness material arriving unbidden.
> - **Catalina Dumitru** (⚠️ a THIRD Catalin/a — not Catalin Luta, not Catalina Preda; she owns the CF Discovery agent): metadata **not supported** on 6.5 LTS **nor on Coworker**; refactoring CF Discovery with metadata search as phase 1.
> - **Yanira is organizing an AEM-wide agent bug bash in Coworker for Wed 07-22** and asks for scope / IMS orgs / **which manifest** — **that is Pedro's call, and it lands while he is on PTO.**
> - **Brian Chaikelson, unanswered:** should the bridge manifests be **common or per-agent**? Pedro's lane.
> - **Still zero** Production Readiness dates from any agent owner. **Ankur's staged-support question: zero replies in five days.** Apoorva's four operational questions: unanswered.
> - Nothing new on the MCP HOLD (Christian), on `ao#5773`, on ADR 001 / Tim Lynn. `#aem-p42-leadership` silent since 06-22.
>
> ### 🔴🔑 2026-07-13 (soir) — THE RETRIEVAL FAILURE, CAUGHT LIVE. Bertrand sent an ADR we had already banked.
> Bertrand, DM 17:08: *"on connait ca?"* + the link to `Adobe-dxue/coworker-ui-experience/docs/adr/001_a2ui_renderer_extensibility.md`. **The answer was YES. It has been in [[A Rendering Contract Carries Structure, Not Skin]] since 2026-06-19.** It was not retrieved. The session re-derived it from scratch by fetching the source with `gh api`, and my draft reply told Bertrand *"je ne l'avais pas lu"*. **Pedro cut that line himself** and replaced it with *"On travaille sur cette base avec Sorin, Eugene"*, which is both true and stronger.
> - **This is [[the P6 retrieval rule]] failing in the open.** Capture worked. Retrieval did not. The knowledge base held the answer and the live work went around it. **Fix, applied: when an architecture doc is named, grep `knowledge/ai-product/` BEFORE fetching the source.**
> - **And the banked entry was wrong on two facts**, now corrected at the source: the ADR is **Tim Lynn's** (`owner: tlynn_adobe`), status **`proposed`**, dated 2026-06-09 — not "shipped", not "merged by Josh Hailpern's team". ([[feedback_proposal_vs_decision]].)
>
> ### 🔑 2026-07-13 (soir) — THE RENDERER PICTURE, FINALLY COHERENT (and my two over-statements corrected)
> **Pedro caught both.** (1) I wrote "custom renderers no longer exist" — Josh's actual words carry a qualifier: renderers *"as they existed before, **with deep/complex workflows embedded in them**"* were removed, along with *"direct connections to agents"*. (2) I told him this was news; **it was not** — that AEM's renderers need rework has been on the list since June. **The real delta:** for the *workflow-bearing* renderers there is **no target to port into**. It stops being a port and becomes a redesign into one of Josh's three mechanisms (hybrid page beside the panel · tools and skills · generative UI). **And choosing between them is a design decision, not an engineering one** — which puts it on Silvia and Eugene's table, not Sorin's.
> - **The ADR reconciles it.** A2UI renderers **do** exist and **any team can add one** (*"the core chat UI team is not a gatekeeper"*, registry-based). What Josh removed is a different object. **Four tiers, in order: SVG via markdown data-URI → SSR React via A2UI → compose from existing platform renderers → custom client renderer as a last resort, with the PR obliged to document why the other three failed.** Rationale, and it is Pedro's own argument written by someone else: *a custom client renderer only works in the Coworker frontend; SVG reaches Claude.ai, ChatGPT, Slack, email.*
> - **🔑 THE FINDING WORTH CARRYING: the prop-schema contract is a SKILL FILE.** *"There is no machine-readable schema shared between AO and the frontend. Instead, the `visual-artifacts` skill document in `ao` is the authoritative description of each component's expected props."* → **a renderer does not start on the frontend, it starts as a contribution into AEP's `ao` repo**, and that PR must land first. ⚠️ **NOT the manifest** ([[feedback_dont_conflate_pattern_with_object]]) — the manifest decides which skills a customer gets; this decides what the LLM may render. Same mechanism, different object. Sent to Bertrand.
> - **Open: the ADR predates the harness redesign** (06-09 vs Josh's Friday message). Pedro told Bertrand he is verifying with **Tim Lynn** that the four tiers still hold. Tim is already in `#aem-aep-coworker-rendering`.
>
> ### 🔴 2026-07-13 (soir) — MARK DOTEN'S FOLLOW-UP: the kill switch EXISTS TO PREVENT coexistence, and Rachel owns the call
> After confirming the flags are technically independent, four more messages (17:00-17:01, DM `D0AP5N5H87J`):
> - **Who decides: *"Probably @Rachel Hanessian."*** → the ask is now small, specific and addressed to a named owner, and Rachel is already the recipient of half the status doc's annex.
> - **He is willing: *"I'm happy to do it, just don't wanna get in the way of their rollout plans and such."*** The blocker is neither technical nor personal.
> - **🔴 BUT: *"I'm pretty sure the kill switch only lasts a couple weeks while the coworker rail gets set up… So users aren't using coworker and the old AO v1 rail."*** → **The kill switch is not an oversight. It is the mechanism AEP built to PREVENT the coexistence state Pedro wants.** It is transitional: the window closes when the Coworker rail ships (~07-31), because then the rail *is* Coworker and there are no longer two assistants to prevent.
> - **The counter-argument, and it is strong:** AEP's reason for killing AIA is to avoid two assistants **while migrating someone**. Pedro's co-innovation customers **are not migrating**. Removing their AI Assistant takes away the assistant they actually use to give them a partial one — literally the catastrophe AEP invented the cohorts to avoid. **Ask Rachel: Enable Coworker without the kill switch, for AEM co-innovation orgs, until AEM's cohort.** Time-boxed, scoped, grantable.
> - ⚠️ **Honesty to hold:** two assistants in one shell IS bad UX, and Pedro has seen it on the EH home. Do not deny it; argue it is the lesser evil, bounded. **Open question for Mark:** with flag 1 on and flag 2 off, what does the customer actually SEE in the shell — two entry points side by side, or Coworker somewhere separate? If it is one, Mark's objection dissolves and no exception is needed.
>
> ### 🔑 2026-07-13 (soir) — AMEX: the preview they want is of THEIR OWN rendering, and Adobe does not run it
> **Sunish Verma, `#tmp-coworker-amex-aem` 16:11:** *"that is correct so we will have both channels - For immediate purposes we need to integrate with **AMEX owned channels which have the template** and leverage AEM Content fragments."*
> → Read their own brief again: the channels are AMEX's, the page templates are AMEX's, the runtime tokenization is AMEX's. **Adobe supplies the content fragments and nothing else.** So *"preview at runtime, reflecting what's actually delivered"* means previewing **the output of AMEX's system**. Neither Adobe nor Naehas can produce that from their own side — **which is exactly why Naehas only shows a simulation. It is not a Naehas weakness, it is structural.**
> - **The question that decides Thursday:** does the AMEX channel expose a **preview/render endpoint** we can call with a given content-fragment variant, reachable from Coworker? **If yes → it is a skill** (Josh's path #2), buildable, and genuinely shows what gets delivered. **If no → nobody can build it**, and that should be said before the onsite, not during it.
> - Internal call Mon 21:00 CEST (Martin Buergi) + another set up by Sunish. **Onsite Thu 07-16 with AMEX exec leadership.** Pedro is on PTO from 07-20.
>
> ### 🟢 2026-07-13 (soir) — Felix answers the manifest fork, and names the convergence direction
> On Apoorva's Coke request: ***"The would be to have them mapped explicitiely to the AEM-AIA manifest and have the different team contribute their marketplace."*** → the fork is resolved (Coke goes on the central manifest, she gets Discovery), **and Felix has just named the default path as the other teams' marketplaces folding INTO the central manifest.** That is Pedro's curation lane, stated by someone else as the obvious route. [[Definition Ownership Is the Moat on Shared Data Infrastructure]].
>
> ### 🔴🔑 2026-07-13 — THE MANDATE WAS MIS-RELAYED. The Saar note was never a note to Saar.
> **Jaclyn Eckersley, email 15:00, verbatim: *"So I made an ask that leaders should have an update on progress."*** Not Saar. Yanira relayed it to Pedro on 07-09 as *"comms that can be sent to @asaar"* and he spent two sessions writing a letter to a VP he has never approached. **Bertrand widens it further: *"+1, I think it would benefit a lot of people - not just leaders 😉"***
> → The artifact is a **running status for the agent teams + leadership**, not a one-shot escalation. **This is a better position**, and it survives his vacation: a letter is read once; a status everyone consults makes Pedro the person who defines the state of the world ([[Govern a Consistency Layer Over Primitives You Don't Own]]). But it needs a real artifact this week — he is off from 07-20.
> - **Clean 2nd instance of [[Don't Let Program Managers Carry Your Liaison Relationship]]** — same PgM, same shape as the April/Conrad episode: the mandate reached Pedro *through* Yanira and arrived distorted. **The lesson to apply next time: go to the source of the ask before producing** ([[feedback_confirm_ask_before_producing]] — the rule existed and was not fired; the tell was "requested by Yanira" sitting in the note's own frontmatter for four days).
> - **v4 REWRITTEN on Bertrand's structure** (vault, same file): surfaces first · **Dimension A** = agent→skill/manifest migration, one row per agent (the empty cells ARE the ask to the owners) · **Dimension B** = rollout to customers on a time axis · provisioning as two objects · what's open. Bertrand killed "Josh's UI" as a label, correctly.
>
> ### 🟢🔑 2026-07-13 — THE TWO FLAGS. "Enable Coworker" ≠ "AI Kill Switch". This one fact settles Ankur AND Apoorva.
> **Mark Doten, verbatim, `#aia_coworker_convergence` 07-08 19:33 (`1783532019.450579`):** *"Unified Shell has 2 feature flags: 1. Enable Coworker (they would need to be removed from this) 2. AI Kill Switch to remove AIA (they would need to be removed from this)"*
> - **→ ACTIVATION IS NOT MIGRATION.** A customer can be enabled on Coworker while keeping AI Assistant. Deprecation is the *second* flag. This is the technical substrate under the whole comms lane, and it was sitting unread in a thread for five days.
> - **⚠️ THE ONE OPEN CONDITION:** Mark named two flags; he never said they are **independently settable**. Pedro asked him 07-13. **Two sentences of the email Pedro already sent to Bertrand/Yanira/Jaclyn depend on the answer.** (Root cause = my failure, now a rule: [[feedback_lead_with_the_condition]].)
> - **It resolves Ankur Arora's 4-day-old attack on the hard dependency** (*"can support be added in a staged manner?"*): **staged ACTIVATION yes, staged DEPRECATION no.** Cohort 3 is where the fallback disappears; EH exposes every agent on one bar, so there is nowhere to fall back to. **Pedro's original "ALL agents before ANY customer" was over-broad — the precise version is more defensible, not less.** A hard dependency stated too widely invites attack.
>
> ### 🔴 2026-07-13 — THE MANIFEST FORK BITES: Discovery is NOT in the EPA manifest.
> Verified in Pedro's own `adbe-skill-audit/data/skills.json` (07-13): **central `aem-aia-extensions` = 22 skills incl. `discovery`** · **`epa` = 18 skills** (`multi-cf-edits`, `aem-content-update`, `content-create`, `brand-governance`, `da-page-edit`…) · **`forms` = 2** · **`excat` = 60**. **No content-fragment skill in the central manifest. No `discovery` in EPA.** And **one manifest is active per customer.**
> - **Consequence, and nobody else saw it:** Felix's **EPA co-innovation org list** (`ao#6444`, 07-10) is *"currently mapped to the EPA Manifest"*. **Apoorva wants Coke on Coworker for Discovery.** If Coke rides that list she gets EPA skills and **no Discovery**. She would have raised the provisioning request and found out in two weeks.
> - Same fork on the AMEX side, inverted: AMEX's ask is content-fragment (swap/edit/preview) → EPA manifest, which is exactly where those skills live. **"EPA for now" is right for AMEX and wrong for Coke.**
> - Instance of [[Definition Ownership Is the Moat on Shared Data Infrastructure]] — the manifest map is Pedro's lane and it is the thing that makes the difference between a working activation and a wasted one.
>
> ### 🔑 2026-07-13 — BERTRAND'S REVIEW: the entitlement/provisioning conflation, twice in five days
> His review of the note (email 13:39, cc Yanira + Jaclyn): two dimensions (adopted) · *"Not sure what 'AIA is deprecated' actually means. i.e. not there, there but hidden, there in coexistence with Coworker?"* (**answered by the two flags — all three states are real**) · **and: *"I commented on 'provisioning' last week -> why is there anything related to provisioning ? All AEM customers have access to the AEM agents"***
> - **He is conflating two objects, and Pedro flagged the same conflation on 07-09.** The **AEM agents entitlement** (default-on, opt-out — Bertrand is right) is NOT **Coworker per-org access** (git segment + Mark Doten's flag — Ken Russell's runbook).
> - **The receipt, from Bertrand's own team:** Felix, 07-09, on adobe.com — *"I see that they are currently not mentioned in any segment on ao."* An Adobe org, with AEM, with the agents entitled, **and invisible in Coworker.** Pedro sent it. **If AEM believes there is no provisioning, nobody chases the trial SKU and 2,600 customers stay behind one git file and one human.**
> - **NEW, unsourced, owed:** Bertrand references *"the decision to use Coworker in headless mode for Experience Workspace."* Pedro has never seen it. Get the source.
> - Bertrand also **answered a question in Pedro's own thread** again (Corey's provisioning question, 07-09) and **made the AMEX call in DM** rather than routing it to Pedro. Third instance this month. [[feedback_position_over_merit]].
>
> ### 🟢 2026-07-13 — AMEX lands, and Bertrand green-lights activation without answering who decides
> Bertrand created **`#tmp-coworker-amex-aem`** (private, 08:04) off Cedric Huesler's relay of **Sunish Verma's** email. **The ask:** AMEX exec leadership (Hass, VP marketing; Karthi, VP eng) want a stronger **content-preview** POV in Coworker before **Thursday's onsite**, positioned as an upgrade over **Naehas**. AMEX needs to swap content fragments, edit content and styles, discover fragments within template constraints, and **preview at runtime**. Three workflows (Offers · Prospect campaigns · Customer campaigns); July = the prove point.
> - **Pedro posted the two things nobody else had** (12:58, 12:59): across all 102 skills **nothing does a runtime preview**, and a swap-fragment UI in chat **is a renderer**, which Josh removed. Then handed the "what does AMEX mean by preview at runtime" question back to Cedric/Sunish and +1'd moving the CF/AJO plumbing to `#project-huginn`. **He cut my manifest paragraph as a restatement of Gilles — correct call, and Bertrand raised "manifest par client" himself 3 hours later.**
> - **Bertrand's DM (13:26):** *"dans coworker, il y a la notion de pod et de manifest par client. avec les skills EPA qui arrivent cette semaine. pour moi ca aurait du sens de les activer sur un projet reel."* = a green light, **not a decision** ([[feedback_proposal_vs_decision]]). He did **not** answer Pedro's "qui décide ?" — which is itself the answer: nobody, and he does not think it needs deciding.
> - ⚠️ **"pod"** — Bertrand uses it as an established Coworker notion. **Unknown term. Do not use it before asking Felix or Tanju.**
> - **🔴 THE REAL RISK:** two named logos in three days (AMEX + Coca-Cola) asking to be on Coworker despite the AEM exclusion. **The first breach of the cohort protection will not come from AEP. It will come from Adobe's own field, with the best intentions.** The counter is the distinction, held publicly: **activation ≠ migration.** Watch for a third instance.
>
> ### 🟢 2026-07-13 — 15-CHANNEL SLACK SWEEP: the answer to Eugene's 6-day-old question was in Pedro's own channel
> **🔑 Joshua Hailpern, `#aem-aep-coworker-rendering` (Pedro's channel), 07-10 16:23-16:39, answering *Sorin*, not Pedro:** *"that is no longer how the new coworker harness functions; there are no more 'direct' connections to agents"* · *"nor do we have 'renderers' as they existed before, with deep/complex wrokflows embeded in them"* · *"these were removed by the coworker team when they reinvisinoed how the harness would work"*. Then, unprompted, the three paths: **hybrid** (*"the coworker harness has visibility onto the page and can interact with the page that is open"*), **tools/skills** (*"a conversational experience, not a point and click"*), **generative UI** (early, "prioritized by leadership"). His preference is marked as his own: *"Personally, #1 is i think a short term solution with #2 being where you likely need to end up."*
> - **→ Eugene's question since 07-07 is ANSWERED: the panel sees and acts on the page.** The EH centre bar stays a live handoff, not a launch button. Sorin (rail) was right; Eugene (full-screen) was wrong; Pedro's destination-agnostic handoff-contract position survives both.
> - **→ AND THE RENDERER AUDIT IS OBSOLETE.** The Rebecca/Sorin/Eugene/Harsh meeting owed since 07-01 is about an object that no longer exists. Re-scope before booking it.
> - **The dog that didn't bark:** it landed in Pedro's own channel on a Friday evening and sat unread for three days, and it was *Sorin* who asked the question.
> - **Other sweep findings:** Corey posted a **Coworker false-success bug** (07-10) — the agent claimed it added a component and did not; **Gilles reproduced it twice** (07-13) and **Felix filed AEMAGT-2319**. Raw material for the readiness definition, arriving unbidden. · **Tanju: One AEM MCP is in the ChatGPT store** (07-10); Brian Chaikelson documents + GAs it with the July release. · **Lianne Ramos:** if Klaasjan Tukker has not reviewed the three comms docs by **EOD Mon 07-13**, the external + internal comms **do not go out on 07-15.** · Governance channel (Philippe) **silent since 07-10**.
>
> ### 📌 2026-07-13 — housekeeping
> **The Obsidian vault moved to `/Users/pedrofer/ObsidianAdobeVault`** (simple relocation; the Google Drive path is dead). 11 stale references repointed across memory, the `pm-research` agent, and the journal/digest/podcast skills. ⚠️ **Obsidian's editor buffer overwrites disk writes** — close a note in the app before I edit it, or the app replays its cached version.
> **Two quotes verified at the source (07-13):** Josh's *"AEM and Workfront have both done stuff with the rail that have critical features"* **holds** — and he is groping for the word in the transcript (*"what's the word, mirrored, ported"*), which is *why* no list exists. **Horia's did NOT hold**: the verbatim is *"Yeah, **I think** that's official, Pedro"* — a hedge, not the confirmation the v1 note claimed. Removed; nothing needs it, the exclusion is written on the slide. **Titles corrected:** **Horia Galatanu = Sr. Dir, PM, AEP GenAI/Agentic AI — NOT a VP.** **Rachel Hanessian = Group Product Manager.**
>
> ### 🔑 2026-07-10 — SAAR NOTE REWORK (superseded 07-13 by the mandate correction — kept for the org-chart reasoning)
> Reviewed the DRAFT through the Director→SD lens after Pedro flagged Saar as a **VP** (⚠️ he first said SVP then corrected to VP in-session; memory had "VP Eng AEM Remote (Germany)" — that stands), *"relativement tranchant"*, low padding tolerance. The note is well-sourced and audited but has one structural miss: **9 asks, all routed to Rachel/Josh/Akin/Ken/Manas/Horia, none to Alex.** It reports; it does not convene. A Director informs the VP; an SD tells the VP which decision is his.
> - **🔑 THE HARD FACT THAT RESHAPES THE ASK: none of the three unowned artifacts sit in Saar's org.** Parity list = Josh Hailpern (Stephen Gould's tree). Trial SKU = AEP Provisioning (Ken/Akin/Shankar). Coworker AI-Ethics review = Coworker team. So "name owners" is a request Saar **cannot grant** — he would rightly answer "not my teams." Spending the first-ever Saar contact on an ungrantable ask is the failure mode ([[read-the-org-chart-before-you-need-it]]; Munger invert = what makes this note fail is not its content, it is landing before Bertrand and asking for the impossible).
> - **What Saar CAN actually do, the three moves that replace "name owners":** (1) **peer-escalate** the trial SKU + Coworker review to his AEP-VP counterparts (a Director cannot, a VP does it in one message); (2) **task his OWN org** on the one piece he owns — a threat-model-scope date from Daniel Mrose's team (the security review is staffed Lars Krapf→Catalin Luta→Daniel Mrose→Saar); (3) **cover the later date** when it slips past AEP's written EOAug — a VP who saw it coming defends it, a VP who learns it late hunts blame.
> - **🔴 THE PARITY LIST IS THE INVERSE ERROR — DO NOT ASK SAAR TO OWN IT, CLAIM IT.** Pedro wrote twice this week that whoever writes the parity list sets AEM's migration date. Asking Saar to name its owner hands away the one lever Pedro wants. Correct move = **declare** it: "the list does not exist, I am compiling it from the agent owners and will publish it; telling you because whoever writes it sets our date." = [[Get Leadership's Name Alongside Yours]] + [[use-the-forum-to-manufacture-the-deliverable-and-pre-load-its-consumer]] + default-and-veto (inform, give the VP room to object; silence = it is yours with his knowledge). Corey already handed Pedro entry #1 (UE rail integration, 07-09).
> - **Form cuts for a sharp VP (one page, not three):** lead with the three-unowned-artifacts observation (it is the only thing in the note nobody else saw — Pedro's, not a readout) and END it on the ask to Alex; move "what we've already closed" (legal + security) ABOVE the risks (credit-first); 9-row table → 3 blockers + an annex that goes to Rachel separately; drop the self-naming "I am calling that Production Readiness" (state the definition, use the term); add three numbers (6 agents, ~2,600 customers, one person flipping the flags); add one invert line (the real failure = reaching cohort 3 with skills ported and nothing else ready).
> - **🔴 THE GATE ON SENDING (unchanged, now sharper): Bertrand must see it first.** Sending an AEM→Coworker escalation to a VP in another branch, asking him to peer-escalate, when Pedro's own Sr Director has not carried it, invites "what does Bertrand think?" — to which the answer would be "he hasn't seen it." [[Validate with N Before Sharing to N+1]]. Plus the who-sends-it call ([[Don't Let Program Managers Carry Your Liaison Relationship]], the April/Conrad shape).
> - **Open question Pedro owes himself before the re-draft:** what does he actually want from Saar — peer-escalate at Anjul level / name owners in his own org / cover the later date? He picked **name owners in his own org**, which resolves to move (2) above: a threat-model-scope date from Daniel Mrose's team, the only one Saar cleanly controls. The other two artifacts get the peer-escalate ask, not the name-an-owner ask. **Knowledge:** no new entry; clean instances of [[read-the-org-chart-before-you-need-it]], [[Get Leadership's Name Alongside Yours]], [[Validate with N Before Sharing to N+1]]. Note for next time: **lead with [[read-the-org-chart-before-you-need-it]] when drafting any cross-VP ask** — the "who can actually grant this" check should precede the wording, not follow it.
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

