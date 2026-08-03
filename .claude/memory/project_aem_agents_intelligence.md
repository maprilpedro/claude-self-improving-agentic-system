---
name: aem-agents-intelligence-aai-project-context
description: "Full context on the AEM Agents Intelligence project — agent reporting platform, AO 2.0 liaison, Loni+JM May 11 deck, three-tier reporting, agent ownership, AAI stakeholders. Sister file to project_experience_hub.md."
metadata: 
  node_type: memory
  type: project
  originSessionId: 5f12dcf1-db3b-44ce-bf6c-50e0a17cb9e9
---

> **Two-project split — Phase 2 structurally complete (2026-05-13).** AAI vault folder at `2026/AEM Agents Intelligence/AAI - Project Folder/`. Companion `project_experience_hub.md` covers EH. Meeting Notes moved to neutral `2026/Meeting Notes/` (2026-05-13). AI-Assistant legacy folder retired. No legacy folders remain.

> **📦 Archive discipline (weekly shards; last restructure 2026-07-01).** Old context lives in per-ISO-week shards `project_aem_agents_intelligence_ARCHIVE_<year>-W<wk>.md` (+ long-form reference in `..._ARCHIVE_reference.md`), mapped by `..._ARCHIVE_INDEX.md`. **To find old context: read the INDEX first (dates + topics per shard), then `rtk proxy grep` the shard — never full-Read a shard.** This active file = hot state (currently **07-21 → 07-27 OKR-review prep**; the 07-15/16 demo, rollout + Manas-sync blocks archived to W29 on 07-20) + the compact durable reference below. **Cap rule, enforced by `scripts/archive_memory.py` (run in `/consolidate` Step 5): keep this file < ~20K tokens / one-shot-readable; event blocks older than ~2 weeks auto-archive to their weekly shard + the index rebuilds.**

> ## ▶️ RESUME HERE — left off 2026-07-27 (OKR review day)
>
> ### 🟢🔑 2026-07-26/27 — OKR REVIEW 7/27 PREP: SPEAKING NOTES SHIPPED TO THE VAULT, AND THREE SOURCING CALLS PEDRO ENFORCED HIMSELF.
> - **📤 Speaking notes (3 min, KR 1e) in the vault:** `AAI - Project Folder/20260727 - OKR Review KR1e - Speaking Notes.md` — speech + delivery notes (7 prepared answers) + source-numbers table. **Pedro rewrote it in his own spoken voice** (added transitions, expanded the plan beat with Production Readiness / Legal / Operational Readiness — his content, not drafted). Exec-summary slide fill-in for row 1.e delivered (Q3 plan / last vs current month / On Watch / wins-path cell).
> - **🔑 THE ONE CLEAN MCP-vs-AGENTS COMPARISON:** MCP 1,202 active external orgs vs agents 665 (~2×, near-identical windows, both external) — in the speech. **NOT comparable, verified and refused:** "returning" (agents = came back across periods; MCP "regular" = ≥3 distinct days same month — different definitions) and Value Realization (agents exec-panel column literally "—"/empty; the 19.5%/28.5% are %-to-plan, not counts). Org overlap between the 1,202 and the 665 is NOT measured — prepared answer says so, no guessed number.
> - **🔑 Fabletics = the write-side customer example** (986 One AEM MCP calls, 89% write — "they use MCP to actually create and change content"), contrast with Eli Lilly (~7k calls, 64% read / 21% discovery). Specific/generic spoken definition added (generic = the agent finding its way around: `list-aem-environments`, `lookup-api-spec`, search; mapping = `mcp_tool_intent_map.csv`, Christian Meyer / Jabran own it).
> - **🔴🔑 PEDRO ENFORCED THE NO-OVERCLAIM LINE THREE TIMES THIS SESSION — his own audit muscle, unprompted:** (1) cut the external/internal milestone because the proving graph isn't on the slide; (2) caught "companies come back, people do not" claiming a 65.5% not shown on the slide → rewritten chart-backed only; (3) **"on a toujours pas de preuve hein, donc aim to pas fixes"** → "the Coworker migration *aims to fix*" + added *"We will see in the retention numbers whether it works"* — which pre-announces his success criterion in front of the LT. ([[feedback_separate_facts_from_proposals]], [[feedback_audit_outward_artifacts]] — instances, no new entry.)
> - ⏳ **Capture the OKR-review outcome** (held 7/27) next session — reactions to the metric-migration plant ("67 thousand is the number I will report") and to the 1,202-vs-665 line.
>
> ## (prior) RESUME — left off 2026-07-22
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
> > This block was first written with the headline *"three decisions moved without him and he is invisible on every decision surface."* **That framing was wrong and it was my error, not a finding.** Pedro's PTO ran from ~2026-07-27 (memory `ad9c398`; Andres Bott 07-29 *"had a quick chat with Pedro before his PTO"*; Ramon Bisswanger 07-29 *"enjoy your PTO"* and 07-30 *"don't look at it during the PTO"*). **Of the ~10 days audited, only 07-24 was a normal working day.** Almost every "unanswered ask" below arrived 07-28→08-03 and is simply an inbox after a holiday.
> >
> > **The evidence was in my own hands** (three separate PTO references in the material I read) **and I fitted a fortnight of holiday into a behavioural narrative I was already carrying** from the Workday feedback and the H-007 resolution. That is the exact failure the 08-03 System Review named — a hypothesis that keeps finding its own confirmation. **Rule: establish the subject's working days BEFORE reading silence as behaviour.**
> >
> > **What survives the PTO explanation (short list):** the 07-24 marketplace audit was never posted *on a day he was working and had named it as his pre-weekend commitment*; the MCP instrument warnings; Security Health shipping; the roster/method corrections. **What does NOT survive:** "seven unanswered asks", "his posts died", "invisible on every decision surface". Those are holiday, not behaviour.
> > ⏳ **Confirm the exact PTO window with Pedro and record it here** — memory says "from 07-27" but he posted lightly on 07-27, 07-29, 07-30 and 07-31.
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
