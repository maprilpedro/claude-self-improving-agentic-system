---
name: aem-agents-intelligence-aai-project-context
description: "Full context on the AEM Agents Intelligence project — agent reporting platform, AO 2.0 liaison, Loni+JM May 11 deck, three-tier reporting, agent ownership, AAI stakeholders. Sister file to project_experience_hub.md."
metadata: 
  node_type: memory
  type: project
  originSessionId: 5f12dcf1-db3b-44ce-bf6c-50e0a17cb9e9
---

> **Two-project split — Phase 2 structurally complete (2026-05-13).** AAI vault folder at `2026/AEM Agents Intelligence/AAI - Project Folder/`. Companion `project_experience_hub.md` covers EH. Meeting Notes moved to neutral `2026/Meeting Notes/` (2026-05-13). AI-Assistant legacy folder retired. No legacy folders remain.

> **📦 Archive discipline (weekly shards; last restructure 2026-07-01).** Old context lives in per-ISO-week shards `project_aem_agents_intelligence_ARCHIVE_<year>-W<wk>.md` (+ long-form reference in `..._ARCHIVE_reference.md`), mapped by `..._ARCHIVE_INDEX.md`. **To find old context: read the INDEX first (dates + topics per shard), then `rtk proxy grep` the shard — never full-Read a shard.** This active file = hot state (currently **the 2026-08-07/10 session**; 07-15 → 07-27 archived to W29/W30 on 08-03, the 08-03 sweep + Agent Owners Alignment to **W32a** on 08-04, the two 08-04 blocks to **W32b** on 08-06, the **08-04 CLINT + 08-05 ROLLOUT SYNC blocks to W32 on 08-07**, and the **08-05 AUDIT REPO + 08-06/07 AUDITS-WENT-PUBLIC blocks to W32 on 08-10**) + the compact durable reference below. ⚠️ **The archiver moves dated blocks but does NOT move RESUME pointers — check the pointer still resolves after every run.** **Cap rule, enforced by `scripts/archive_memory.py` (run in `/consolidate` Step 5): keep this file < ~20K tokens / one-shot-readable; event blocks older than ~2 weeks auto-archive to their weekly shard + the index rebuilds.**
>
> ⚠️ **"moving 0 block(s)" HAS TWO CAUSES — DIAGNOSE BEFORE ACTING (2026-08-07).** (1) **The layout invariant below is broken** → the archiver cannot see the blocks. That is a bug, fix it. (2) **Every dated block is newer than `RETENTION_DAYS = 7`** → there is genuinely nothing it may move yet, which is correct behaviour on a dense week. **Check which one you are in before "fixing" anything.** On 2026-08-07 the file sat at **23.5K against a 24K read cap with every block under 7 days old**, so the only lever was **writing the blocks shorter** — the largest was a single 3.4K-token event block, trimmed to 2.2K. 🔑 **On a dense week the cap is a writing constraint, not an archiving one.** ✅ A **SessionStart hook now warns** when any session-start file approaches the cap (`scripts/archive_memory.py --check-startup`, wired in `.claude/settings.json`) — added because both prior truncation incidents were discovered by accident, never by a warning.
>
> 🔴 **LAYOUT INVARIANT, learned the hard way 2026-08-04 — DATED EVENT BLOCKS MUST SIT ABOVE THE LIVING-REFERENCE SECTIONS.** `split_active()` in the archiver treats the first non-blockquoted `## ` heading as the start of the living reference and everything after it as unmovable. This file had drifted so that four dated `> ###` blocks sat *below* `## 2026 Yearly Goal — G1`, so the archiver saw **one** block (the protected RESUME) and reported *"moving 0 block(s)"* while the file sat at **29K tokens, 5K past the read cap** — i.e. **the cap guard reported success while the file was silently truncating at session start, which is the exact 2026-06 awareness-loss failure it was built to prevent.** Fixed by reordering (content-preserving, verified line-multiset-identical), after which the same script moved 29K → 19K on the first try. **When appending a new dated block, put it directly after the RESUME, never at the end of the file.**

> ## ▶️ RESUME HERE — left off **2026-08-27 morning**. 📊 **A FULL SKILL + MCP INVENTORY WAS READ (92 items) AND IT SAYS TWO THINGS PEDRO CAN ACT ON: EVERY ONE OF THE 84 SKILLS HAS ZERO MONITORING, AND FIVE CAPABILITIES SHIP TWICE, ONCE AS SKILLS AND ONCE AS MCP TOOLS.** 🔑 **The second one is the exact question Bertrand asked out loud on 08-24/25 and nobody has put the evidence in front of him.** An English rationalisation report was written. See the 2026-08-26/27 block directly below; the 08-25/26 cohort work is the block under it.
>
> ### 📊🔑 2026-08-26/27 — THE SKILL + MCP INVENTORY, AND THE OBSERVABILITY COLUMN IS EMPTY
>
> **📍 THE SOURCE.** `~/Downloads/table (3).csv`, 92 rows, columns `Item Name · Type · Owner Team · Access Point · Use Case · Env · Auth Method · Monitoring · Mon. Source · Usage Metrics · Alerting`. ⚠️ **A point-in-time extract, not a live artifact — the estate moves weekly, so re-pull before quoting any of these counts.** Read 2026-08-27.
>
> **THE SHAPE: 84 skills + 8 MCP servers across 14+ owner teams.** Type split: **50 `Skill` · 23 `Skill (Sub)` · 8 `Skill (API Ref)` · 2 `Skill (Orchestrator)` · 1 `Skill (Router)` · 1 `Skill (Internal)`.** 🔑 **Only ~59 are reachable by a user** — the 23 subs carry Access Point `Internal` and are invoked by orchestrators, never selected directly. **That is the honest denominator when someone asks what a customer can reach**, against the `62 AEM skills` in the GA announcement and the 11 visible in prod. Owner concentration: AEM Sites 13 · Cloud Manager 11 · AEM Assets 11 · AEM Dispatcher 8 · Sites/CF 6.
>
> **🔴 FINDING 1 — NOTHING IS MEASURED. All 84 skills carry `Monitoring: no`, `Mon. Source: -`, `Usage Metrics: no`, `Alerting: no`.** Not most. All. The 8 MCP servers carry `partial`, sourced from platform telemetry. **No skill is observable, therefore no skill is reportable** — which is the structural reason skill-level reporting keeps failing, now visible as one uniform column rather than an argument. Directly Pedro's lane.
>
> **🔑 FINDING 2 — FIVE CAPABILITIES SHIP TWICE, AND THIS IS BERTRAND'S OPEN QUESTION.** Brand Governance (5 skills + `governance__bga_*`) · Permissions Governance (2 skills + `governance__pga_*`) · Content Supply Chain (2 skills + `csca__*`) · Document Authoring (2 skills + 11 CRUD tools) · Asset Sourcing (1 skill + 76 tools). **Bertrand, `#aem-agent-owners-alignement` 2026-08-25 12:48, verbatim:** *"if we keep the oneAEM MCP server to barebone tools, without duplicating the skills, then we make the coworker MCP much more interesting and 'valuable' - generating value to customers and to Adobe (revenue)… the question is whether, by artificially augmenting the role of tools, we are not shooting ourselves in the foot (business wise, not technically)."* And 08-24 19:32: *"if our coworker skills are pointing at MCP tools, then they should work 'as is'… But if they are pointing at APIs, then they will only work in Coworker (eg. the assets-discovery skill)."* → **The duplication is a pricing and portability decision, not a hygiene bug. Pedro holds the five named families; Bertrand holds the question. That is the move.**
>
> **⚠️ FINDING 3 — `AEM MCP` AND `OneAEM MCP` OVERLAP HEAD-ON.** 17 tools each, both covering environments and read/write/delete, under **different owner teams** (AEM Platform vs AEM Sites/CF). Post-GA, not GA — Carsten's 08-19 freeze decision explicitly held off moving other MCPs under One AEM MCP.
>
> **🟢 FINDING 4 — SEVEN "SKILLS" ARE DOCUMENTATION.** `aem-cloudmanager-api` (112 endpoints) · `aem-open-api` · `aem-r-api` · `aem-sling-api` · `aem-repository-discovery-api` · `aem-content-workflow-access` · `bps-il-admin-console`. All typed `Skill (API Ref)`. **This is Manas's 07-16 point arriving as data** — *"everything doesn't have to be modeled as a skill; a lot of it can be tiered documentation"* — and reclassifying them is the cheapest cleanup available while also fixing the denominator.
>
> **🟢 FINDING 5 — TWO TEAMS BUILT THE SAME PATTERN SEPARATELY.** Dispatcher = 1 orchestrator + 7 subs; Cloud Manager pipeline troubleshooting = 1 orchestrator + 6 subs. Identical shape, an orchestrator routing to a per-step failure investigator. One shared pattern would serve both.
>
> **Smaller, all actionable.** (a) **Six skills read a brief out of a document** (`docx-parse`, `docx-read-text`, `docx-export`, `docx-extract-annotations`, `brief-docx-highlight`, `pdf-parse`) — and the estate already has the right answer next door in `aem-sites-content-update`, a Router that classifies and dispatches. (b) **18 names break `aem-<application>-<feature>-<action>` and they cluster by team, not at random** — Brand Governance, Enterprise Context and Content Supply Chain all use verb-first (`discover-brands`, `evaluate-page-against-brand`, `view-brand-checks`, `manage-enterprise-context-rules`). **One alignment conversation, not eighteen renames.** Two names also mix `_` and `-` inside (`aem-assets-metadata_form-onboarding`, `aem-assets-search_filter-onboarding`). (c) 🔴 **Three skills carry `IMS + PAT` and they are the only three that write to a customer's git repo** — `aem-cloudmanager-pipeline-troubleshooting`, `aem-cloudmanager-pipeline-fix-applier`, `aem-edge-dispatcher-fixing`; two mention "revoke PAT" in their own use case. **They are also unmonitored. That is the audit line.**
>
> **🕳️ THE GAP VISIBLE BY ABSENCE.** No skill covers **delete, cleanup or rollback**, and workflow support is read-only (`aem-content-workflow-inspect`, no execute path). **Matches `AEMAGT-2581`**, the only cross-agent finding of the bug bash, still filed `Normal` and unassigned.
>
> **📤 An English rationalisation report was produced in-chat** (inventory shape, the five findings ranked, the smaller items, and a six-step suggested order). Not sent anywhere.
>
> **🔧 ADMIN CONSOLE, small but it cost time.** `AEM Agents on Coworker - GA Bug Bash - Authors` is an **Admin Console User Group**, not a product profile and not an AEM-side group — which is why it is invisible if you look under Product Profiles. **Path: adminconsole.adobe.com → check the org switcher is on AEM Showcase → Users → User groups.** Direct: `https://adminconsole.adobe.com/38931D6666E3ECDA0A495E80@AdobeOrg/users/groups`. **Created by Yanira 2026-08-15**, and her own caveat still stands unless someone changed it: *"I did not add any author roles b/c I don't know what program we will be using, what environment, what AEM Role"* — **she added only the CM Developer role.** Latest add: Yanira to Gerald Prendi, 2026-08-26 14:31, group DM `C0BSY04G1LL`.
>
> **🔎 KNOWLEDGE (P6):** applied — [[Everything Is a Skill — the "Agent" Dissolves as a Build Unit]] (the API-ref demotion and the skill-vs-MCP duplication are both the build-unit question resurfacing) · [[A Packaging Unit Is a Customer Taxonomy — Ownership Needs Its Own Record]] (18 naming exceptions clustering by owner team, not at random) · [[Selection and Cross-Surface Consistency Are a PM Mandate]] · [[Lead the Slide With the Honest Read of Your Own Metric, Not the Flattering Number]] (~59 user-reachable is the honest denominator against 62 and 84). **No new entry — see the consolidation note.**
>
> ### 🔑🔴 2026-08-25/26 — THE COHORT FILES COMPARED, AND THE ABAC QUESTION IS ANSWERED
>
> **📊 THE COMPARISON, and it is now a repeatable method.** `20260820-AEM_COHORTS (1).xlsx` tab `Cohorts` (**4,457 orgs**, header row 1) against Paul Midura's `Copy of DRAFT - AEM, Target and Workfront Coworker Cohort Rollout Lists.xlsx` tab `AEM+Target` (**1,065 orgs, header row 19, data from row 20**, file `Last Updated: 8/26/26`). Overlap **1,064**. 🔑 **THE JOIN FAILS WITHOUT NORMALISING — Paul writes org IDs WITHOUT the `@AdobeOrg` suffix, Pedro's file keeps it.** Strip the suffix and upper-case both sides or you get zero matches. His other two tabs: `Workfront+Target` 1,106 orgs, `Target Only` 426.
>
> **✅ ON THE FOUR SHARED COLUMNS THE TWO FILES AGREE PERFECTLY — 0 differences on 1,064 orgs** for `GenAI Status`, `Industry`, `ECCID`, `Opted Out`. `Cat 5 Legal` flagged on neither side. **Only the `Cohort` column disagrees, on 13 orgs.**
>
> **🔑 AND THE REASON IS MECHANICAL, NOT A DISAGREEMENT.** Paul's `Cohort` column is not typed, it is `XLOOKUP($B<n>, [1]Cohorts!$B:$B, [1]Cohorts!$A:$A)` — **a live external link into a workbook named `Cohorts`, which is Pedro's own file.** His `IMSORG NAME` column is a `VLOOKUP` into the same book. **So Paul's cohorts are DERIVED from Pedro's, and the 13 mismatches are a stale link pointing at an older copy, not two teams disagreeing.** ⚠️ **Before treating any list-vs-list gap as a disagreement, check whether one is computed from the other.**
>
> **🔴 THE 13, AND THEY POINT ONE WAY.** Eleven of thirteen are `Pedro = Cohort_AEM_3.2_SKU` against a Paul TBYB cohort; the last two agree it is SKU and differ only on the wave. **Five carry `Targeted Activation Date 2026-09-01`** — Qantas Airways `11B20CF953F3626B0A490D44` · NWL Brands AEM `6A0F02095FAB0D640A495FE8` · Corporate & Investment Bank `6AAB041762B261FF0A495E40` · Warner Bros Marketing Cloud `7FF852E2556756057F000101` · Okta Inc `ADD71D3E633F65A90A495CE5`. **Eight more with no date**, all flagged `Confirmed Paying Customer = YES`: InvoCare Australia · Stagwell GenStudio ×4 org IDs · SAP SE · Kaiser Foundation Hospitals · Revlon. ⚠️ **Pedro's own file contradicts itself on the five urgent ones — cohort says `3.2_SKU`, `Confirmed Paying Customer` is blank.** ✅ **Lists 1 and 2 were handed to Paul 2026-08-26**, and Pedro had the 13 rows written to `Cohort_AEM_3.2_SKU` and highlighted yellow in a copy of Paul's file (rows 32, 45, 46, 51, 60, 445, 992, 1007-1010, 1075, 1081). ⚠️ **Writing the value replaced the XLOOKUP with static text on those 13 rows — they will not refresh.**
>
> **🔴🔑 THE ABAC ANSWER, AND IT CLOSES THE 08-24 WATCH.** Column `ABAC Customer` in the cohorts file: **34 orgs marked `YES`.** **Exactly 5 of them are on Paul's rollout list, and they are the same 5 dated 2026-09-01.** 100% overlap, not a coincidence. → **The published `Known limitations` note tells them ABAC is *"not yet available"*, but on migration they LOSE it**, with no replacement and no date ([[reference_coworker_enablement]] correction). **The other 29 are on NONE of Paul's three tabs**: 15 `Cohort_AEM_WF_SKU`, 6 `Cohort_AEM_0_Activated` (all internal/demo/partner — AEM Showcase, US XSC AEM Showcase, Adobe Demo System, Portfolio CSC Team, acs-apac-internal, **Publicis Sapient Global**), 2 `1.1_INT`, 2 `3.2_SKU` (both internal labs), 2 `4_OTHERS`, 1 `SHALL_NOT_MIGRATE` (**Under Armour**), 1 out of scope.
>
> **🔴 THE REAL GAP: 15 NAMED ABAC CUSTOMERS SIT IN `Cohort_AEM_WF_SKU` AND THAT COHORT HAS NO ROLLOUT LIST ANYWHERE.** Costco · Pfizer · Delta · PNC Bank · Sams Club · Edwards Lifesciences · Steelcase · PwC GLSC · Microsoft Project Supreme · BAT Shared Services · Havas · OXXO · Koch Companies Public Sector · Hottinger Brüel & Kjær · Freddy.Connect. 🔑 **Pedro created that bucket himself on 08-18** (*"I will shuffle the common AEM+Workfront orgs to the end. With 2 groups - one internal, one SKU"*). It exists, it holds fifteen ABAC customers, and nobody has written what happens to them. [[An Undefined Gate Is a Date Nobody Can Give]]
>
> **📋 THE OPT-OUT REGISTER IS LIVE AND ACCELERATING.** Tab `Opt-Out Requests`, **34 requests** between 08-18 and 08-26, from field sellers (Ryan Hickling, Danny Mason, Craig Stangis, Brian Ravert, Jim Bunn, Brett Knoll, Athena Han, Mark England, Clara Chu, Rayan Pulis, Matt Wooten, Harshil Gambhir, Jonathan Welsh). ✅ **ZERO of them appear on Paul's rollout list — that filter works.** ⚠️ **18 of the 34 are absent from Pedro's own `Cohorts` tab**, many carrying status `Org Not Found` (all seven Samsung orgs among them). 🔑 **The recurring reason is the one ABAC would answer — *"customer not comfortable with lack of permission based controls"* appears three times** (Endeavour Group, Aware Super, AMP). Others: AstraZeneca ×2 and eight more *"active opportunity"*, Wellmark *"CX Coworker not HIPPA ready"*, National Australia Bank *"not approved by Security"*, Services Australia *"AI addendum not yet signed"*, Bank of Queensland *"not signed Gen AI Terms"*.
>
> **💰 BERTRAND PUT A NUMBER ON SKU CUSTOMERS AND IT IS NOT PEDRO'S NUMBER.** `#aem-agent-owners-alignement` 2026-08-24 18:34: **Paid 8 (Q1) + 16 (Q2) = 24 unique · $0 46 + 23 = 66 · Total licensed 54 + 39 = 90.** *"so 24 'real' customers and a lot of $0 SKU customers"*. ⚠️ **Against Pedro's own 335 (Skyline P42 classification, 08-12) and his ~3K quoted to the AMS team the same day.** 🔑 **Probably different denominators, not a contradiction** — Bertrand counts contracts resolvable in DaaS over 2026-Q1+Q2 only; Raul's list counts orgs classified SKU regardless of quarter. **Unreconciled.** Bertrand named the source on 06-08: **DaaS, via Jean-Claude Jung and Andre Cascais.** Pedro asked them for a named list on 08-20 and got no reply.
>
> **📣 THE INTERNAL GA ANNOUNCEMENT WENT OUT 2026-08-25 12:42** in group DM `C0BSBN56403` (Carsten, Bertrand, Yanira, Jaclyn). **Both false claims were removed before sending** — no *"all AEM Agents"*, no *"feature parity"*. It kept the June-10 anchor, Bertrand's routing point (*"AI Assistant is limited to simple tasks, often routes to the wrong agent"*), and links the published doc. ⚠️ **It says `62 AEM skills` in the marketplace** — true of the marketplace, not of what a customer sees (prod carries 11 visible in 1 plugin). Carsten's only edit: *"One AEM Marketplace"* → *"A single AEM Marketplace"*, to avoid collision with OneAEM. Jaclyn asked for success criteria between cohorts — **unanswered**.
>
> **🗓️ THE AEM ALL-HANDS IS WEDNESDAY 2026-08-26 AND BERTRAND RESTRUCTURED IT.** He wrote in `#aem-cloud-foundation-pm` 08-25 12:10: *"I would like us to 'hijack' tomorrow's AEM all hands"* — 30 minutes, **5 sections of 6 minutes**, Overview (Bertrand) · **AEM and Coworker (Pedro)** · oneAEM MCP Server (Brian Chaikelson) · Enterprise Context (Philippe Kapfer) · Content AI (Peter Klassen). *"Your 6 minute contribution should be very visual, micro demos, 1 slide max."* Marli Satyadi owns the deck.
>
> **🔎 KNOWLEDGE (P6):** applied — [[An Undefined Gate Is a Date Nobody Can Give]] (`Cohort_AEM_WF_SKU` exists with fifteen named customers and no date, the cleanest instance yet) · [[Lead the Slide With the Honest Read of Your Own Metric, Not the Flattering Number]] (335 vs 90 vs 24 — the honest read is that the denominators differ and nobody has said so) · [[feedback_critique_check_facts_not_prose]] · [[feedback_dont_conflate_pattern_with_object]] (derived-vs-independent list, see the XLOOKUP finding).
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

## Apoorva validation punch-list (KR1) — 📕 CLOSED 2026-08-11, Pedro's call

> ✅ **"oublie" — Pedro, 2026-08-11.** Closed deliberately and **not** verified item by item. Opened at the April 16 meeting (Apoorva Gupta + Ankur Arora + Varun Kalra) against the Discovery Agent report; its lane has since been overtaken by the Coworker migration and the Rubin/definition port, and Bertrand's Q2 response already says G1's work *"needs to be… redone for a large part given the move to Coworker."* **Do not re-raise it at the next System Review.**
>
> **Tombstone, so the shape is not lost:** 8 items — (1) 50-60% data gap vs Grafana ✅ closed April 22 by Varun · (2) TSR counting "no result found" as success · (3) tag classification bleeding across agents · (4) First Useful Result Rate missing · (5) content-type breakdown for Discovery · (6) aggregated-metrics transparency · (7) promo SKU + TBYB credit utilization view · (8) calculation-logic documentation per metric. **Full text in git history** (`git log -S "Apoorva validation punch-list" -- .claude/memory/`).
>
> 🔑 **Two things worth carrying forward, because they outlived the list.** The **"no results found" reframe** (a product gap, not a legitimate answer) is banked in `knowledge/` and still true. And the attribution line — say *"Apoorva's team stress-tested and found gaps"*, **never "Apoorva validated"** — still applies to any report she has reviewed.

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

**AO / AEP:** Conrad Woltge (Sr Principal Architect), **Trent Davies** (`W4SGEQF46`, `tdavies@adobe.com`, Denver) — ⚠️ `correct:` 2026-08-20, **NOT "eng, AO"**. He is **Sr. Principal Architect, Experience Cloud**, and his role in the GA is specific: he owns the interpretation of *"all MCP servers must be behind the Coworker Gateway and pass the ARB review"* and therefore **grants the exception**. Christian Meyer routed it to him via Carsten on 08-18 13:41. **He is the authority Pedro's "agreement to go GA with reviews open" rests on** — Ken Russell (eng, AO), Sergey Generalov (PM, AO), Ian Boston (compliance), Manas Garg (AOv2 dev experience).

**Data / Reporting:** Felix Delval (data eng, EPA pipeline), Lara (taxonomy + Governance), Varun Kalra (Discovery validator, Apoorva's team), Karthik Penikalapati (Rubin tech lead), Angela Han (Rubin owner).

**🆕 Rollout data + comms (added 2026-08-21, both were missing and both own something Pedro's GA depends on):**
- **Paul Midura** — `pmidura@adobe.com`, `W4RPRDFFV`. **Owner of the cross-solution activation list (AEP + AEM + Workfront)** and therefore of column G `Non-Migration Reason` in the cohorts workbook. Pedro owns column F. DM `D0B2SLATWUX`; working group DM with Tina `C0BR07R1BJ8`. ⚠️ **Not to be confused with Paul Pop** (`pop@adobe.com`, eng, flagged the broken gateway tools on 08-10).
- **Huong Vu** — `huongv@adobe.com`, `U053CPN2XLH`, Senior PMM under Akin Ajayi. **Owns the Gainsight + admin-email machine for the Coworker rollout.** Operators: **Serah Metpalli**, **Young Ah Bang**; **Sonia Espejo Butler** for Workfront. Channel `#cx-coworker-trial-rollout-core` `C0ABFLYLZK7`.
- **Trent Davies** — see AO / AEP above. Sr. Principal Architect, Experience Cloud; grants the Gateway/ARB exception.

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
