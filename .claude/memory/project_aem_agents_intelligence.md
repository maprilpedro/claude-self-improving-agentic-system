---
name: aem-agents-intelligence-aai-project-context
description: "Full context on the AEM Agents Intelligence project — agent reporting platform, AO 2.0 liaison, Loni+JM May 11 deck, three-tier reporting, agent ownership, AAI stakeholders. Sister file to project_experience_hub.md."
metadata: 
  node_type: memory
  type: project
  originSessionId: 5f12dcf1-db3b-44ce-bf6c-50e0a17cb9e9
---

> **Two-project split — Phase 2 structurally complete (2026-05-13).** AAI vault folder at `2026/AEM Agents Intelligence/AAI - Project Folder/`. Companion `project_experience_hub.md` covers EH. Meeting Notes moved to neutral `2026/Meeting Notes/` (2026-05-13). AI-Assistant legacy folder retired. No legacy folders remain.

> **📦 Archive discipline (weekly shards; last restructure 2026-07-01).** Old context lives in per-ISO-week shards `project_aem_agents_intelligence_ARCHIVE_<year>-W<wk>.md` (+ long-form reference in `..._ARCHIVE_reference.md`), mapped by `..._ARCHIVE_INDEX.md`. **To find old context: read the INDEX first (dates + topics per shard), then `rtk proxy grep` the shard — never full-Read a shard.** This active file = hot state (last ~1 week of events, currently **07-16 Bertrand 1-1 → 07-17 sweep**; the 07-15 demo/rollout + 07-16 Manas sync blocks archived to W29 on 07-20) + the compact durable reference below. **Cap rule, enforced by `scripts/archive_memory.py` (run in `/consolidate` Step 5): keep this file < ~20K tokens / one-shot-readable; event blocks older than ~2 weeks auto-archive to their weekly shard + the index rebuilds.**

> ## ▶️ RESUME HERE — left off 2026-07-22
>
> ### 🔴🔑 2026-07-22 — THE MARKETPLACE-CONSOLIDATION THREAD, AND A CORRECTION TO OUR OWN AUDIT NUMBERS THAT PEDRO CAUGHT.
> Threads: `#p42-architecture` `C09KKLW1N86` ts `1784720330.787079` (Felix opened 13:38) · prior granularity thread ts `1784580015.006749` (Ian Reasor, 07-20) · cross-post in `#aem-agent-owners-alignement` `C0BARAMM89Z` ts `1784720370.903769`. ✅ High-fidelity, Slack verbatim.
>
> - **🔑 FELIX PUBLISHED THE MARKETPLACE INVENTORY — 8 AEM marketplaces in Coworker** (`aem-aia-extensions`, `epa-experience-generation-extensions`, `aem-content-fragments-extensions`, `governance-agent-marketplace`, `assets-drm-extensions`, `aem-guides-extensions`, `ao-plugin-extensions-aem-onboarding`, `aemforms-aia-extensions`) **plus the RTCDP repo branched per customer** (`Adobe-Experience-Platform/rtcdp-aia-marketplace`). **He proposes all AEM migrate to one marketplace.** → **This is half the org→manifest artifact Bertrand has asked for three times. Do not let it stay a Slack message.**
> - **🔴🔑 AEM PLUGINS ARE ALREADY SHIPPING OUTSIDE THE AEM MARKETPLACES.** `air-india` carries **`aem-experience-production`**, `air-india-dev` carries **`aem-assets`**, in the RTCDP repo AEM does not own. ⚠️ **`tccc-dev` and `wells-fargo` carry NO AEM plugin — do not say "Coca-Cola and Wells Fargo", it is wrong.**
> - **🔑 TWO DECISIONS ARE BEING COLLAPSED IN ONE THREAD.** (1) **repo consolidation + admin/CODEOWNERS/merge path** — engineering, and **Felix + Ian Boston resolved it live 07-22** (Felix wants the repo under `OneAdobe` so each BU manages its own approvers; Ian: *"Can we fix the lacking admin and use codeowners to delegate?"* then posted the org admin list). (2) **plugin granularity = what the customer sees and selects** — **customer-facing, and nobody has decided it.** Carsten Ziegeler framed it 07-20 with three options and prefers **option 2, plugins selectable against what the customer purchased**; he also said *"this should not be an engineering decision"*; **Ankush Malhotra explicitly disagreed** (*"I also strongly disagree to this not being an engineering decision"*). Satya: a plugin lives in one git repo, so granularity drives repo structure. **Corey Dulimba, 14:56: *"do we have a decision and go forward plan? If not, when will we?"* — still unanswered.**
> - **🔴🔑 GILLES HANDED PEDRO THE PEN IN PUBLIC AND PEDRO HEDGED.** Gilles, 16:48: *"@Pedro Ferreira can you own the decision from a PM point of view? 😉"* → Pedro, 17:01: *"I guess i am the closest to the subject :P **if it causes no technical issues or limitations**, agreed to move to one marketplace."* **Three concessions in one line: justifies his standing instead of using it, endorses Felix's proposal instead of producing one, and hands the veto back to engineering — the exact opposite of what Carsten had routed to PM.** ⚠️ **Second clean WRITTEN instance in 5 days** after 07-17 *"might work - checking"* (Namita took the idea 12 min later). **Same surface, so this one DOES strengthen the parked candidate** *"stating a thing as a plan beats stating it first — the hedge transfers authorship"* → **n=2 clean, hand to `promotion-judge` at 08-01.** ⚠️ Do NOT cross-count the 07-16 Manas spoken instance. ([[feedback_first_reply_ownership_sentence]])
> - **🟢🔑 PEDRO'S OWN CALL, AND IT HELD: he refused to claim authority over a technical decision** (*"je ne veux pas prendre l'autorité sur une décision qui est technique"*). **Correct, and Felix + Ian proved it within the hour by closing the repo half themselves.** The move is to decline the engineering half out loud and take only the customer-facing one ([[Govern a Consistency Layer Over Primitives You Don't Own]]).
> - **🔴🔑🔑 PEDRO CAUGHT A REAL ERROR IN OUR OWN AUDIT FRAMING — excat is NOT a gap in Felix's list.** I was about to have him post that Felix "missed the largest AEM catalogue". **Wrong.** Felix's list is scoped *"AEM marketplaces in Coworker"* and **excat is referenced by no manifest, so its absence is correct.** **Composition of excat's 60, read from `data/skills.json` 07-22: 53 = AEM Edge Delivery Services developer tooling · 6 = the team's own repo workflow (`create-pr`, `update-changelog`, `dev-deploy-k8s`, `frontend-review`, `react-spectrum-s2`, `update-banner`) · 1 = `excat-ui-tour`.** **It is AEM but it is EDS migration tooling for developers, not customer-facing Coworker skills.**
> - **🔴🔑 THE NUMBER TO QUOTE FROM NOW ON.** The audit's 105 spans 4 catalogues but **only 45 are in Coworker-registered marketplaces** (aia-extensions 25 + epa 18 + forms 2). **On those 45: `when-to-use` = 5 (~11%), `domain` = 2 (both Forms).** → **The banked 34.3% is carried by excat and is the flattering number; ~11% is the true customer-facing figure and the stronger argument.** **And the audit covers 3 of Felix's 8, not 4 of 8.** Extending it to all 8 is a config edit in `scripts/fetch_skills.py` plus a pipeline run. ⏳ **Pedro committing to post the extended report Friday 07-24 (he is out from 07-27).**
> - **⚠️ THE INPUT NOBODY IN THAT THREAD HAS: Manas, 07-16** — *"rather than loading all the skills… how do we start moving more towards the **skill search mechanism**?… **everything doesn't have to be modeled as a skill; a lot of it can be modeled as product documentation**."* **If part of the corpus demotes to documentation, the plugin boundary is being drawn around a denominator that is about to change.** Ian Boston was in that room and can corroborate. ⚠️ Direction, not a decision ([[feedback_proposal_vs_decision]]).
> - **🔑🔑 THE AUDIT IS THE ANSWER TO A QUESTION FELIX ASKED IAN 07-06 AND NEVER GOT.** In `#p42-architecture`, Felix 07-06: *"@Ian Boston Is there any process to assess overlap between skills and agent on Coworker? Is there any guidance on how best create our marketplace and manifests for Coworker?"* — **no reply, 18 days.** And Felix reposted top-level 07-22 15:25: *"If we are going to merge all skills under aem-aia-extensions as suggested by Carsten. What testing/validation can we put in place so we can easily merge PRs? **Should we run Coworker evals?**"* → **The debate already moved from whether-to-consolidate to how-to-test. Pedro's overlap+disambiguation audit + the `ao`-benchmarks right-skill-rate is the eval gate they are asking for. Frame it as the answer to a standing ask, not a new offer.**
> - **🔑 BERTRAND ASKED THE GRANULARITY QUESTION CONCRETELY HERE 07-16, ALSO UNANSWERED.** On the discovery SKILL.md "Resolving the AEM author repository" section: *"shouldn't this be a **cross-AEM** skill as such? I mean it shouldn't be any different when intending to work against an AEM asset, an AEM page, an AEM fragment?"* cc Felix, Tanju, Ian. → **The plugin-granularity decision, posed by Pedro's own manager, in concrete form, sitting 8 days without an answer. The written boundary position Pedro owes should answer Bertrand's example directly.**
> - **⚠️ UNREAD, DO NOT CHARACTERIZE: Felix Meschberger's "AEM Agentic Architecture" wiki `3955827624`** (07-13, born of a Coworker-DACI discussion) — *"how we should be looking at skills (not agents any longer) and user experiences"*, with vision/reference/guides sub-docs. **If it already draws skill/plugin boundaries, Pedro's Friday position must cite it, not write over it. Open it (VPN) before posting.** ([[feedback_confirm_ask_before_producing]])
> - **🔎 KNOWLEDGE (P6):** applied — [[Govern a Consistency Layer Over Primitives You Don't Own]] (decline the primitives, govern what the customer sees across them), [[A Single-Harness Marketplace Is Not a Cross-Harness Standard — Publish vs Find]] (the consolidation is a find/consolidate move), [[feedback_first_reply_ownership_sentence]] (the 17:01 hedge), [[feedback_audit_outward_artifacts]] (the excat mislabel + the Coca-Cola/Wells-Fargo near-miss, both caught before posting), [[feedback_proposal_vs_decision]] (Felix's "one marketplace" and Manas's direction are proposals). **No new knowledge entry — corroboration.**
>
> ### 🔴🔑 2026-07-22 — TBYB DORMANT ACTIVATION: THE STATE PEDRO HAS BEEN ARGUING FOR IS ALREADY RUNNING IN PROD AT 152 ORGS, AND THE "NO BANNER" MECHANISM IS TWO FLAGS, NOT ONE. (Read from `#aia_coworker_convergence` `C0BDRAMULQ0`, 07-22.)
> - **🟢🔑 174 orgs were provisioned on the BACKEND in one go** (Namita, `ao#7229`, *"doing the full cohort on the backend in one go since it takes time with the git process. The final ff is on the UI side, so we can control the appropriate batches on the day"*). **07-21 only ~22 got the UI flag flipped** (Namita: *"We have rolled out Coworker (new UI) to the 22 orgs scheduled for today"*). **The next ~152 all at once, targeted Thursday 07-23** (Paul Midura: *"That is the decision… target Thursday, 7/23"*). → **⚠️ CORRECT THE v7 STATUS NOTE: "cohort 1 live ~174" is wrong — 174 provisioned, 22 UI-live, rest 07-23. And 152 orgs are RIGHT NOW in exactly the backend-active/UI-off state Pedro's silent-activation ask describes. He no longer has to argue it is possible; it is the current state of 152 customers.**
> - **🔴🔑 THE "NO BANNER" ANSWER IS EXC-48837, AND IT IS TWO SEPARATE FLAGS.** Namita's 07-21 UI-kill-switch thread (`1784677176.311149`): the direct AIA link still worked on a killed org. **Tim Lynn: the kill switch *"only gates the entry points (rail, left nav from EC home), but not the route itself"*.** **Mikaela Symanovich: *"the try now banner etc shows when coworker is enabled AND kill switch is true. But the immersive route is only gated by the enablement flag"* → filed EXC-48837, taking it 07-22.** → **Two flags: `enablement` + `kill switch`, entry points governed separately from routes. Owners = Mark Doten (built the kill switch, flag docs `wiki.corp.adobe.com/x/_y7e7`), Tim Lynn, Mikaela, Stephen Gould coordinating. This is the mechanism for Pedro's 07-14 Q1 ("backend without a shell entry point"). Pedro is the only one in that channel with a business reason for "enabled-but-invisible" to be a durable STATE, not a bug to fix — that is the ownership rep.** ([[feedback_first_reply_ownership_sentence]], [[The Game Itself — Position Over Merit]])
> - **🔑 KEN HALF-ANSWERED THE SCALE QUESTION 07-18** (provisioning thread `1784331887.503479`): *"the SKU won't be available in AEP Provisioning until after the 1st week of August. We have work in place (some minor tweaks required) to honor it."* Mark → EXC-48499; Daniel-Cristian Miu → `aep-ai#5101`, *"indeed, it's a config change."* → **The scale ask (2.6k AEM TBYB via the same git-by-cohort process) goes to Ken in HIS 07-18 thread, one question: does the post-first-week-August automated provisioning take a patch that size in one go, or is there a ceiling.**
> - **🟢 Namita is already instrumenting the AOv1-vs-Coworker comparison** (*"let's also keep an eye on if we see usage on AOv1 from any of these 22 customers"*) — adjacent to what the bridge was meant to produce. Worth knowing before re-opening the bridge with her.
> - ⚠️ **The channel was flipped public then back to PRIVATE 07-20 (Peter Walker / Lianne Ramos)** — read via MCP, do not assume everyone can see it.
> - **🔎 KNOWLEDGE (P6):** [[An Undefined Gate Is a Date Nobody Can Give]] (the no-banner mechanism was undefined; EXC-48837 defines it), [[feedback_proposal_vs_decision]] ("no banner" was intent + "sounds good", now it has a ticket). No new entry.
>
> ### 🟢🔑 2026-07-21 — COHORT 1 IS LIVE, DISCOVERY IS THE FIRST AEM SKILL LIVE, AND THE LEADERSHIP STATUS NOTE SHIPPED THROUGH A BERTRAND REVIEW (v7).
> - **🟢 Cohort 1 went live 07-21 (~174 AEP orgs).** AEM cloud service still excluded (cohort 3, no date). **Experience Discovery is the first AEM skill LIVE in Coworker** — 5 internal orgs since 07-01 (Assets-only). EPA 18 + EDA 14 testing stage/prod; Governance 6 in prod but its enablement PR `ao#5773` has no AEP owner.
> - **🟢 "CX Coworker One Adobe Demo" manifest now in prod (07-20)** — consolidates all skills incl. all AEM, for enablement/validation/demos, not customer-facing. **Bertrand is pushing an AEM skill-naming scheme (`aem-[app]-[feature]-[action]`) before customer exposure** — a teams action, and Pedro's naming lane. **Bug bash:** EPA done last week, EDA + Governance targeted; panel bug bash (Jul 22) postponed until use cases gathered.
> - **📤 THE LEADERSHIP STATUS NOTE (`AEM Agents on Coworker — Status`, vault) went to v7 and Pedro SENT it.** Reordered per his own intro (Surfaces/Provisioning/AOv1-decommission definitions + Dimension A/B), per-agent table synced from the GA Readiness canvas (`F0BD4RALNHF`), then Bertrand's review applied: Dim A trimmed to a bug-bash column (Manifest + ETA dropped), cohort-1 detail removed, provisioning rewritten in plain terms. **This is the weekly running status for agent teams + leadership incl. Saar.** New feedback banked: [[feedback_bertrand_status_comms]].
> - **📊 CHECK-IN PREP (Bertrand) — mapping of Pedro's work Apr→Jul vs G1/G2/G3:** G2 (Coworker migration) dominates (~70 deliverables), G1 (reporting) solid (~48), **G3/adoption stalled (~14, front-loaded to April)** — O2 personalization KRs KR6 (06-15) + KR3 (07-15) overdue, little movement since spring. **VP-direct visibility thin since the May-11 Loni+JM deck** (~3 Loni / 2 JM touches all quarter); the 07-10 DX-PM-Sync where someone else presented Pedro's value-to-credit mapping is the cost. Two "do-better" moves for the check-in: rallumer G3; put the migration story + BVR in front of Loni/JM directly (via Tina Ngo for pricing). ⚠️ Vault OKR boards frozen at 2026-04-20 — statuses there don't reflect reality. See the check-in dashboard produced this session.
> - **🔎 KNOWLEDGE (P6):** corroboration only — [[The Game Itself — Position Over Merit]] (the visibility gap + owning the status note), [[An Undefined Gate Is a Date Nobody Can Give]] (client-id trust track), [[feedback_bertrand_concrete_first]] + new [[feedback_bertrand_status_comms]]. No new knowledge entry.
>
> ### 🟢🔑 2026-07-20 — WEEKEND SWEEP CLOSE-OUT + RENDERING OWNERSHIP REPS (18-channel sweep, window 07-17→07-20). **THE ROLLOUT IS ON FOR 07-21, THE CLIENT-ID BLOCKER IS DE-RISKED (NOT CLOSED), AND PEDRO POSTED TWO RENDERING-SURFACE REPLIES ON HIS OWN LANE.**
> Detail + dated follow-ups in `watches.md` (loads at session start). This block = the net.
>
> - **🟢 THE ROLLOUT IS REAL AND ON FOR 07-21.** Cohort-1 = **~174 orgs** (Ulta added — its comms is a "coming soon" email 07-20, live ~07-23; Superloop opted out). Namita provisioning all 174 backend in one go (`ao#7229`); the UI feature-flag controls the batches on the day. **The client-id/trust blocker did NOT slip it** — it is a parallel security track. AEM stays cohort 3, still no date.
> - **🟢🔑 CLIENT-ID / TRUST BLOCKER — DE-RISKED, NOT CLOSED.** The revert holds (works today). **Alex Trifan (Coworker/gateway) agreed to request-signing with a service token + whitelist that clientid, instead of re-pushing the new client_id** — so the CSO risk (broken Coworker→AEM connectivity) is contained. Ian + Tanju aligned on the CoWorkerRouting diagram (07-17); **Marius Petria engaged 07-20 with two live open questions** — ServiceProxy tenant-isolation, and who verifies the calling user has access to the targeted AEM env (Coworker vs One AEM MCP). The commentable text proposal is not written yet. Tuicu↔Tanju One-AEM-MCP meeting ~07-21; the Alex sync is unconfirmed. **GRANITE-70593 is deliberately NOT actioned as an allowlist — the proxy is the chosen path.** ⚠️ **VW = the forcing case for per-person/per-agent gating; Ian answered per-AGENT (a co-innovation customer points its manifest at just `.../experience-governance`), per-PERSON granularity inside the org still unanswered.** ⏳ watches.
> - **🟢🔑 TOKYO MANIFEST SHIPPED — PEDRO'S DELIVERABLE, DONE.** PR **`ao#7148`** merged + deployed 07-17 (Felix raised, Daniel-Cristian Miu approved). **Pedro named it `cx-coworker-demos` (wide, not Tokyo-specific — his call, aligned with Bertrand + Wouter); excat excluded, no pushback; his CODEOWNER sentence got Ken named as approver** ([[The Game Itself — Position Over Merit]], [[feedback_first_reply_ownership_sentence]]). **⚠️ Wouter's weekend test: AEP/CJA/AJO work in the manifest; the AEM part is blocked 07-20 by author-UI env startup failures (15/50 → ~2/3), Felix confirmed low-level, NOT the client-id path.** Live fire before the 07-21 lab; Bertrand escalating to cloud-foundation. **The AEM-skills-through-the-Coworker-harness question is still not answered end-to-end.**
> - **🟢🔑 RENDERING OWNERSHIP REPS — PEDRO REPLIED TO BOTH ASKS 07-20 12:18-12:20** (#aep-agent-orchestrator-collaboration `C08U50NRA01`, cc Sorin + Eugene; both had sat unanswered since 07-17). **Manish Bansal (A2UI card + backend call) answered his guardrail question: auth = user-context** (*"button click is user specific request API call, it is ought to be user context based authorization"*) → **ball back to Pedro to turn user-context into the concrete guardrail + offer to write it up as the "skills that render actionable UI" pattern** ([[Govern a Consistency Layer Over Primitives You Don't Own]]). **Pankaj Sangra (inline-URL render) awaiting his end-goal** (Pedro answered: no supported inline-full-webpage capability today, asked preview vs interact vs act-on-page). ⚠️ **#2300 (`Adobe-dxue/coworker-ui-experience`, PageUrl-context-INTO-agent) is Eugene's question, NOT Pankaj's inline-render — three distinct capabilities, do not collapse** ([[feedback_dont_conflate_pattern_with_object]], self-corrected mid-session). #2300 OPEN, assignee Mikaela Symanovich, no movement since 07-17. ⚠️ **Pedro enforced "pas d'inférence" on the Manish reply** — do not post invented guardrails as if they were existing Adobe policy; state honestly that no written best-practice exists and offer to define it ([[feedback_audit_outward_artifacts]]).
> - **🔑 SKILL-PROVISIONING PRESETS MOVED.** Yunyao Li 07-18 posted **Aggressive 19/17/0 (recommended) vs Conservative 15/12/9** — **supersedes the 15/19/8 buckets**. XLG pushed back on default-on write-skills → backend limited write access to a subset of their users (07-20). **Namita now "drives skills from the PM side" (Rachel, 07-20) — adjacent to Pedro's turf; Kapil Rohra = governance for Coworker.** → get the audit in front of Yunyao ([[Three-Layer AI Skill Governance Architecture (Customer-Side)]]).
> - **Other, banked:** Manas handed convergence closure to **Yelena Doliner** (not driving org→manifest himself this week; no movement on IAM+RBAC Ian→Jonas or the AEM bi-weekly). EDA agent bug bash **07-21** (Marius Duta); Coworker SideRail bug bash **07-22** (Felix doubts readiness); 1st customer AOv1→AOv2 **07-24** provisioning not visibly cleared. **Philippe Kapfer on PTO** (zero moves; invited to Pedro's rendering channel by Sorin's batch, not self-inserted — low threat this week; Pedro capturing his governance knowledge before he left = good). **AEMAGT-2319 still no public status** — chase in JIRA. Gilles questioning why the convergence channel is private.
> - **✅ CORRECTED THIS SESSION:** the Bertrand client-id heads-up **WAS sent** (Pedro DM'd him re GRANITE-70593, found via search) — the "not confirmed sent" watch is closed. **Felix replied** to the 4-point check 07-17 18:13 (pointed to the RCA runbook `2026-0715-Governance-OBO-ClientID.md`).
> - **🔎 KNOWLEDGE (P6):** all corroboration, **no new entry** — [[An Undefined Gate Is a Date Nobody Can Give]] (the client-id trust decision), [[Govern a Consistency Layer Over Primitives You Don't Own]] + [[The Game Itself — Position Over Merit]] (rendering reps + the CODEOWNER sentence), [[Three-Layer AI Skill Governance Architecture (Customer-Side)]] (Yunyao presets), [[feedback_dont_conflate_pattern_with_object]] + [[feedback_audit_outward_artifacts]] (the #2300 self-correction + the "pas d'inférence" enforcement). Instance-only.
>
> ### 🔴🔑 2026-07-17 — 18-CHANNEL SLACK SWEEP (window 07-13→07-17, 5 parallel readers). **THE ROLLOUT IS REAL AND IMMINENT, THE CONVERGENCE HARDENED INTO A PROD GATE, AND A TRUST BLOCKER JUST PUT THE WHOLE ROLLOUT ON HOLD.**
> Not the meetings (those are banked separately). This is what moved in the channels around them. Permalinks in the sweep; grep the channel + date to re-find.
>
> - **🔴 COHORT 1 IS FINAL AND SHIPS 07-21 ~08:00. THE COUNT SETTLED AT ~174, NOT 185.** Klaasjan Tukker confirmed the list final (relayed by Lianne Ramos, 07-15, *"we can deploy the comms"*); **Paul Midura trimmed 185 → 177** (removed 8 B2B-only IMS orgs), then **APAC pulled 3 more — Energy Australia (in RFP), News Corp AU (price-sensitive), SBS (holding for FIFA coverage)** → **~174.** Cutover flag-flip proposed ~08:00–08:30 so the India email team's admin notices can follow. **Advance comms (banner, Gainsight, internal email 07-15, external 07-16, trial page, ExL use-cases page 07-17) all shipped.** ⚠️ **This is the 185-number finally resolving — 185 was never AEM, and it is now 174 and not AEM either.** AEM stays cohort 3, still no date (Ken: *"the two product teams need to align on the date"*).
> - **🔑🔑 "RAIL" IS NOW "PANEL" — TERMINOLOGY LOCK.** Rodson Clavel renamed the channel 07-16 (`cxue-coworker-rail-hybrid-collaborators` → `...-panel-...`) and the surface with it: **"Coworker Rail" → "Coworker Panel".** The **07-31 cutover of the ai-assistant rail → Coworker Panel** is confirmed on that channel (distinct from the 07-21 chat cutover). **Fix outbound language: say Panel.** ⚠️ Add to [[reference_transcript_glossary]].
> - **🟢🔑 AEM WAS PULLED INTO PANEL TESTING, BY BERTRAND.** Cole Connelly added AEM + Workfront to the panel-testing invite 07-15 (panel loads on `experiencemanager`/`assets` stage routes with the flags on); **Bertrand looped Corey Dulimba + Apoorva Gupta + Shankari Panchapakesan** into the thread 07-16. **1–2 AEM reps this round, broader AEM testing next week.** ⚠️ Cole flagged a **two-rail risk for Workfront** (their own rail + Coworker if AIA not disabled).
> - **🟢🔑 SECURITY GATE IS GREEN — PEDRO OWNS THE STATEMENT.** Pedro, 07-14, #owners-alignement: *"Security Gate for AEM on Coworker: **not blocking for migration switch**. Kickoff meeting held today with AEM Security. Thread models will be updated… **NOT BLOCKING for migration switch. Canvas gate updated.**"* **Matches what he told Rachel + Manas ("security/ops/legal not blocking"). Consistent, sourced.**
> - **🟢🔑 RECONCILE — THE RENDERERS ARE NOT THE BOTTLENECK PEDRO TOLD MANAS THEY WERE.** **Corey Dulimba to Pedro + Yanira, 07-15: *"for phase 1 not needed… we aren't using any of them today in AIA so no need to have them in co-worker right now."*** (The 3 renderers — Plan, Template, Assets — came from Silvia's EPA UI audit.) → **Pedro told Manas 07-16 *"the big red item is around the UI… the renderers we need to port… the biggest bottleneck."* Corey says the renderers specifically are deferred.** ⚠️ **The real UI work is the panel↔main-screen interaction, NOT the renderers. Re-state the bottleneck precisely — it is narrower than what Manas heard.** Pedro is already organizing the panel-use-case calls (Governance 07-17, EPA + Eugene Mon 07-21) to define exactly that.
> - **🔴🔑🔑 A TRUST BLOCKER JUST PUT THE AEP ROLLOUT ON HOLD — IAN BOSTON -1, AND IT IS AEM'S OWN ARCHITECT BLOCKING.** Ian Boston, 07-16, #p42: *"I am **-1 on allowlisting all CoWorker client ids in all AEM Environments** as they are used by GPT clients directly. **We have evidence that Claude.ai makes calls to APIs that it's not been given permission by the user on the UI**… We need to establish trust between CoWorker and AEM."* → **Jose Antonio Insua (AEP/Coworker): *"No problem. We'll hold the rollout until there is a final decision."*** Fix on the table: route all Coworker traffic through a **single service proxy with signed headers** (ticket **GRANITE-70593**, CoWorkerRouting diagram 07-17). ⚠️ **This gates the very enablement Pedro is pushing for TBYB. Watch it — it can slip 07-21.**
> - **🔴🔑 THE CONVERGENCE HARDENED INTO A PROD GATE.** Tanju Erinmez, 07-14, #p42: **EGA and EPA were *prohibited from merging their MCP PRs to prod unless they move their MCP server behind the CX Enterprise MCP Server.*** → **One AEM MCP is becoming the single AEM MCP behind the CX gateway, enforcing `explorers.yaml`.** And it now **ingests Coworker Marketplace manifests directly** (Tanju demoed EGA/Brand-Guidelines through it: *"there's no reason to copy and paste files around. We can consume the manifest directly"*). ⚠️ **But it is name-only sync today — no skill-body ingestion, no upstream-divergence detection (*"we have no process to keep notified that Skills somewhere else got updated"*). Aspirational, not shipped. Do not quote the convergence as done.**
> - **🟢🔑🔑 AND IT ANSWERS ASTRAZENECA: THE AEM MCP WILL SUPPORT AMS (MANAGED SERVICES).** Tanju, 07-15: *"AEM MCP relies on CM and IMS functionality. The good news is that **AMS will be supported as well**, with the effective feature set currently being built out."* → **This is the missing half of the 07-14 AstraZeneca "Sites on MS" answer** ([[watches]]) — the agents-on-6.5 story is being built, routed via `#aem-agents-ams`. **Still "being built out", not shipped — do not promise a date.**
> - **🔑 EPA IS BEING RENAMED EGA (Experience Generation Agent).** Satya Deep Maheshwari + Felix Delval, 07-15. **`experience-generation.yaml` = the AOv1→AOv2 BRIDGE manifest, NOT the canonical direct-EPA-in-Coworker manifest**; Forms stays separate (`aem-forms-experience-builder.yaml`). `ao#6312` merged 07-17 (append EGA skills to the AEM-AIA manifest, proceed to prod; orgs entitled to the *skill* but maybe not the *API* — API failure handled inside the skill). ⚠️ **Update the taxonomy: EPA = EGA now. Do not treat "EGA" as the old Governance-adjacent acronym.**
> - **🔴🔑 THE SKILL-PROVISIONING MODEL FOR COHORT 1 IS TAKING SHAPE, AND IT IS MANAS'S "PER-CAPABILITY POV" MADE REAL.** Yunyao Li (with Manas) built the first cut with Claude Code, 07-16: **15 skills default / 19 opt-in / 8 admin-controlled** — three buckets by read/write + data sensitivity + reliability (2+ production customers), sourced from **Rubin usage data** (Angela Han's team). Trigger was **Manas: *"we need a more detailed PoV in terms of what APIs/MCPs, skills, features need to be enabled for what. Are we going to enable delete audience for everyone? Absolutely, no."*** **Preeti Singh + Yelena Doliner** own the capability inventory in the Anjul deck. → **This is exactly the [[Three-Layer AI Skill Governance Architecture (Customer-Side)]] made operational by the platform, and it is the governance layer Pedro's audit feeds. Get the audit in front of Yunyao Li.**
> - **🔴 THE BRIDGE IS MEETING RESISTANCE ON-CHANNEL FROM KEN AND NAMITA, UNRESOLVED.** Ken, 07-15: *"The UI contract changes between AO 1.0 and 2.0. **I'm not convinced it will work.**"* Namita, 07-14: *"the general direction is to **deprecate the AI Assistant brand**. Having an 'AI Assistant' branded surface in AEM but under the hood calling the Coworker API does not make sense… maybe you should at least call this **Coworker in-app**?"* + she disputes Pedro's number (*"I am not sure about this 2.6k number either… we are excluding all AEM CS customers"*). **This is the fourth org against the bridge (Ken, Namita, Bertrand, + the war-room silence). Pedro's own manager already told him to stop defending it.**
> - **🟡 PEDRO'S POD QUESTIONS TO RACHEL (07-14) GOT ZERO REPLIES ON-CHANNEL.** Three unanswered: are AMEX/Coke/AstraZeneca formal PODs; his claim of the **Named Generalization Owner** role for anything landing in AEM; and *"a POD is co-innovation, not a migration… enabled on Coworker with the AI Kill Switch left off."* **Still open — worth a nudge, but Rachel is out until ~07-29, so it waits or goes to Namita.**
> - **🔴 FORMS REPORTING IS INVISIBLE, AND PEDRO MADE AN EXTERNAL 6–8-WEEK PROMISE TO CLOSE IT.** The AEM agent reports use the AEP copilot as source of truth; **Forms has non-AEP flows that don't show up** (Hemanta Gupta, 07-15). Pedro deferred the fix to the Rubin migration rather than build CSV ingestion: ***"the current plan is to migrate those reports to Rubin… over the next 6-8 weeks for the full port"*** (~mid-September 2026). **Forms owns its own side-loading investigation.** ⚠️ **This is now a dated external commitment to a peer team — watch mid-Sept.** Ties H-009 (the Rubin port is Pedro's counter-play deliverable) — [[H-009]].
> - **🆕 FOUR NEW CO-INNOVATION / CUSTOMER SIGNALS.** **Volkswagen** (07-17, Tuicu) — wants *only the Governance agent* for *specific people* during co-innovation → the concrete case against "all AEM MCPs behind One AEM MCP", forces per-person/per-agent gating. **Cox Communications** (07-13) — EDA troubleshooting (Web Tier + Replication), manually enabled by Sergiu, TAM Anubha Bhandari. **LG U+** (Korea top-3 telco, ~2,500 users) — wants Governance, **blocked on Korean language** (Governance eval returns English-only), needed **first week of August**. **Pfizer** — Governance ABAC breaks at **>1000 user groups** (they have 1542) → ruled a bug, `ASSETS-73270`, this sprint.
> - **🟡 PHILIPPE KAPFER JOINED PEDRO'S #aem-aep-coworker-rendering CHANNEL (07-17)** with Caroline Pierpoint, Ramon Bisswanger, Alejandro Ramirez Cheves. No discussion yet. **Competitor frame — his home lane is Governance; the rendering surface is Pedro's. Watch what he does there.** ([[project_aem_agents_intelligence]] Philippe section.)
> - **🟡 TWO RENDERING-SURFACE ASKS ARE SITTING UNANSWERED IN PEDRO'S TERRITORY.** Manish Bansal (07-17, interactive-canvas Skills via A2UI custom cards — *"a Compute Diff button that calls an internal service and updates the canvas"*) and Pankaj Sangra (inline-URL rendering in chat). **Both are Pedro's Coworker-rendering/guidance lane and both are unanswered — cheap ownership reps.**
> - **📋 EDA→Coworker migration canvas dates (F0BFGUCHUEL, "On Track"):** bridge in prod **07-17** · skills+bridge bug bash prod **07-22** · MCP Gateway + observability **07-24** · **1st customer on AOv1→AOv2 07-24 (BLOCKED by AEP customer provisioning)** · evals **07-31** (solution still being selected). **AEP provisioning is the recurring blocker across every lane.**
> - **🔎 KNOWLEDGE (P6):** applied — [[Three-Layer AI Skill Governance Architecture (Customer-Side)]] (Yunyao's 15/19/8 buckets = the governance layer, live), [[A Single-Harness Marketplace Is Not a Cross-Harness Standard — Publish vs Find]] (One AEM MCP behind CX gateway + direct manifest ingestion = the find/consolidate layer hardening), [[H-009]] (Forms→Rubin 6-8wk = the port deliverable, now externally promised), [[An Undefined Gate Is a Date Nobody Can Give]] (the client-id trust decision is the new undefined gate holding the rollout). **No new knowledge entry — all corroboration of existing lanes.**
>
> ### 🟢🔑🔑 2026-07-17 (07:18→09:15, live group DM `C0BHWQA3PJ5`) — **TOKYO ENABLEMENT: BERTRAND INVENTED A STANDING FIELD DEMO SURFACE AND ASSIGNED PEDRO TO BUILD IT. THE WIN IS REAL AND SO IS THE MISS.**
> Room: Rachel Hanessian + Bertrand + **Wouter Van Geluwe** (field enablement, new) + Pedro; Namita joined 07-16 23:44; **Ken Russell + Daniel-Cristian Miu** joined 08:10; Sergiu 08:36; Felix added by Pedro 08:36. ✅ High-fidelity source (Slack, verbatim).
>
> - **THE ASK.** Rachel, 07-16 18:29: field enablement in **Tokyo next week, 60 internal people** doing Coworker labs — *"wanted to see if there were any AEM pieces we could have them try out"*. Wouter: labs run on **CitiSignal**, each learner gets their own AEM CS program. **Bertrand bit immediately** with a real product argument: *"The AEM skills are progressing quickly, **some things are demonstrable already**."*
> - **🔴🔑🔑 THE MISS, AND IT IS THE CLEANEST INSTANCE YET OF THE HEDGE COSTING HIM THE IDEA.** Wouter, 07:37: *"ideally users shouldn't have to switch manifests manually, everything should be in one… is that possible?"* **Pedro, 07:40: *"Compose a single enablement manifest for Tokyo at authoring time, pulling the plugins we need across AEM and EPA marketplaces **might work - checking**"*.* **Namita, 07:52, twelve minutes later, same idea stated as a plan:** *"Yes we can ask someone to raise a PR to 1. create a new manifest that extends this default one + adds all the required AEM mktplaces… 2. target the lab org id… **this would essentially simulate our desired future state of having everything in a single manifest**."* → **He had it first and hedged it; she posted it as a plan and it became hers.** Not a knowledge miss — an **authority** miss. ⚠️ Second instance in 48h of his own work landing under someone else's name (07-16: the DX AI PM Sync pricing deck). **Different mechanism, do not cross-count.**
> - **🟢🔑🔑 AND THEN HE WON THE THING THAT ACTUALLY MATTERED, IN THREE MINUTES.** Bertrand, 07:57: *"I'm sure they can, but **Coworker PRs are approved/merged by the Coworker team**"* — true and empty without a name. **Pedro, 08:07: *"need a name on your side who approves and merges today. Felix's last manifest PR sat without a reviewer, there is no CODEOWNER on that path."*** → **Namita, 08:09: *"I can ask Ken and give him context."* Ken Russell + Daniel-Cristian Miu in the room at 08:10. Full brief posted 08:12.** **The one thing that could kill the date, closed in 180 seconds, by naming a mechanical failure mode instead of asking for help.** ([[The Game Itself — Position Over Merit]])
> - **🔑🔑 BERTRAND SCOPED IT UP AND CREATED AN UNOWNED OBJECT. 08:00:37: *"let's not make this Tokyo specific — **a lot of SCs would make use of this right now** — something like **Coworker Demos** would make sense as a manifest name."*** → **A disposable lab manifest became a standing demo surface for the whole field.** **Wouter reached the same place independently at 08:29: *"please use a generic name as I'm doing this enablement in **other locations throughout the year**"* + *"**cx-coworker-one-adobe** would even be better"* (🔥 reaction).** → **Whoever composes it decides what every SC shows every customer. Nobody has claimed it. Pedro writes the PR, so he names the file — the name IS the claim.** Same figure as the parity list and the Named Generalization Owner. ⚠️ **Namita's 08:12 brief to Ken reverted to *"a Coworker lab for internal folks in Tokyo"* + *"Wouter's lab org"* — the scope-up is Bertrand's and Wouter's, and it is already leaking back to Tokyo-specific. Build it wide; both of them said it in public.**
> - **🟢 BERTRAND BLOCKED THE RIGHT THING WITHOUT PEDRO ASKING.** 07:54: *"**it's too early to merge all the AEM skills and plugins in the default one** (that's the main PROD configuration)"* → enablement-only manifest, prod default untouched. **Pedro's product-exposure concern was handled by his manager, in public, for free.**
> - **🔴 THE DEBUG-MODE ROUTE IS DEAD, KILLED BY BERTRAND ON SECURITY.** Learners are on **`@adobeeventlab.com`**, and manifest-switching (debug mode) is gated on `@adobe.com` → Bertrand: *"ah, that's the problem"*. Wouter offered to open debug mode to the eventlab domain; **Bertrand, 08:05: *"I suspect that won't pass the security guardrails — not sure how 'secure' this domain is."*** → **Backend-defaulting the org is the only path, which is also what Wouter wanted at 07:37.** ⚠️ **Wouter's own fallback recreated the problem he opened with and nobody said so.**
> - **✅ THE ORG IS ONE ORG AND IT DISSOLVES THE DOMAIN QUESTION. Wouter 08:28: IMS Org `907075E95BF479EC0A495C73@AdobeOrg`.** Then 08:58→08:59, answering Daniel: *"we use demo accounts that use the @adobeeventlab.com domain"* … *"for **on-demand access to the same org and the same content**, people use their @adobe.com email, **so it should work for both domains**"* → **one IMS org holding BOTH domains. Target the org, grant nothing to a domain, Bertrand's security objection never applies.**
> - **🔑 CITISIGNAL CLOSED BY WOUTER, WITH A GAP NOBODY CAUGHT.** 07:46: *"We have been using EPA in the past **through AIA** with the CitiSignal programs, so that should be fine."* ⚠️ **Through AIA, not through the Coworker harness.** That is [[reference_aia_vs_coworker_axes]] exactly — front vs backend, do not collapse. **"It worked in AIA" says nothing about Coworker, especially with the renderers gone.** Unremarked in-thread.
> - **🔴 AND THE ASK GREW.** Wouter, 07:46: *"The manifest for the enablement should include **all Adobe skills across all products, we use everything**."* + Namita: *"simulate our desired future state of having everything in a single manifest"* → **the fat-manifest question, live, in front of 60 field people.** Satya's context-cost point; Ian Boston's ~50% right-skill-selection on AOv1. **Pedro's overlap audit is the only instrument pointed at this, and it only covers the AEM side (105 skills / 4 marketplaces — not CJA, Target, AJO).** Offering to extend it across the Coworker team's marketplaces is the land-grab ([[Govern a Consistency Layer Over Primitives You Don't Own]]).
> - **📤 PEDRO'S COMPOSITION CALL, POSTED 08:36 and tagged to Bertrand:** the marketplaces that already run in a manifest today — `aem-aia-extensions`, `governance-agent-marketplace`, `epa`, `forms`, `onboarding` — **NOT excat**: *"Its skills have never been in a manifest and a field lab is the wrong place for their first run."* **60 of the 105 AEM skills are excat's and excat is referenced by no manifest. He is the only person who knows that.** = the one thing in the whole thread nobody else could produce.
> - **⏳ FELIX DM'd 09:15: *"Tu as besoin que je fasse quelque chose avec Wouter"*** — the answer is no, Wouter already gave the org ID; what is needed is the PR.
> - **🔎 KNOWLEDGE (P6):** applied — [[The Game Itself — Position Over Merit]] (name the mechanism, claim the object), [[An Undefined Gate Is a Date Nobody Can Give]] (the approver was the undefined gate; naming it closed it in 3 min), [[reference_aia_vs_coworker_axes]] (the CitiSignal-through-AIA gap), [[feedback_proposal_vs_decision]] (Bertrand's "Coworker Demos" is a name he floated, not a decision), [[Govern a Consistency Layer Over Primitives You Don't Own]] (the audit offer). **Should have applied and did not: [[feedback_first_reply_ownership_sentence]] — "might work - checking" at 07:40 is the anti-ownership sentence, and it cost him the idea.** **Candidate-shaped, NOT parked (park is 23 and over cap):** *stating a thing as a plan beats stating it first — the hedge transfers authorship.* n=1 clean. **Hand to `promotion-judge` at 08-01.**
>
> ### ✅ CLOSED 2026-07-17 — THE MANAS CALL WAS **2026-07-16**. ONE CALL, CONFIRMED BY PEDRO. INGESTED.
> This block previously read *"2026-07-17 — MANAS CALL PREP (call held ~08:00; outcome NOT captured)"*. **Wrong date, and there was no second call — Pedro confirmed 2026-07-17: *"le call avec Manas était le 16 (hier), pas d'autre call."*** The transcript (`Meeting Notes/AEM to coworker transition/20260716 - AEP Manas Sync .md`) is dated 07-16 and Pedro says in it *"we had **yesterday** a bug bash already for production agent"* — that bug bash was **07-15**. **Nothing is missing.** Full ingest below.
> Agenda as recorded: skills migration status · **org→manifest visibility** (the artifact Bertrand has asked for 3×) · the **DOMAIN / WHEN-TO-USE / WHEN-NOT-TO-USE audit** and what exists in Coworker today · migration acceleration. He cut the "multiple marketplaces" line and left POD/TBYB out of writing. **⚠️ The marketplace cut is now the finding — see below.**

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

