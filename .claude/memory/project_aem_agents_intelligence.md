---
name: aem-agents-intelligence-aai-project-context
description: "Full context on the AEM Agents Intelligence project — agent reporting platform, AO 2.0 liaison, Loni+JM May 11 deck, three-tier reporting, agent ownership, AAI stakeholders. Sister file to project_experience_hub.md."
metadata: 
  node_type: memory
  type: project
  originSessionId: 5f12dcf1-db3b-44ce-bf6c-50e0a17cb9e9
---

> **Two-project split — Phase 2 structurally complete (2026-05-13).** AAI vault folder at `2026/AEM Agents Intelligence/AAI - Project Folder/`. Companion `project_experience_hub.md` covers EH. Meeting Notes moved to neutral `2026/Meeting Notes/` (2026-05-13). AI-Assistant legacy folder retired. No legacy folders remain.

> **📦 Archive discipline (weekly shards; last restructure 2026-07-01).** Old context lives in per-ISO-week shards `project_aem_agents_intelligence_ARCHIVE_<year>-W<wk>.md` (+ long-form reference in `..._ARCHIVE_reference.md`), mapped by `..._ARCHIVE_INDEX.md`. **To find old context: read the INDEX first (dates + topics per shard), then `rtk proxy grep` the shard — never full-Read a shard.** This active file = hot state (currently **the 2026-08-04 session**; 07-15 → 07-27 archived to W29/W30 on 08-03, the 08-03 full Slack sweep to **W32** on 08-04) + the compact durable reference below. ⚠️ **The archiver moves dated blocks but does NOT move RESUME pointers — check the pointer still resolves after every run.** **Cap rule, enforced by `scripts/archive_memory.py` (run in `/consolidate` Step 5): keep this file < ~20K tokens / one-shot-readable; event blocks older than ~2 weeks auto-archive to their weekly shard + the index rebuilds.**
>
> 🔴 **LAYOUT INVARIANT, learned the hard way 2026-08-04 — DATED EVENT BLOCKS MUST SIT ABOVE THE LIVING-REFERENCE SECTIONS.** `split_active()` in the archiver treats the first non-blockquoted `## ` heading as the start of the living reference and everything after it as unmovable. This file had drifted so that four dated `> ###` blocks sat *below* `## 2026 Yearly Goal — G1`, so the archiver saw **one** block (the protected RESUME) and reported *"moving 0 block(s)"* while the file sat at **29K tokens, 5K past the read cap** — i.e. **the cap guard reported success while the file was silently truncating at session start, which is the exact 2026-06 awareness-loss failure it was built to prevent.** Fixed by reordering (content-preserving, verified line-multiset-identical), after which the same script moved 29K → 19K on the first try. **When appending a new dated block, put it directly after the RESUME, never at the end of the file.**

> ## ▶️ RESUME HERE — left off **2026-08-04** (Clint thread read live, then the 08-03 Agent Owners Alignment ingested)
>
> **🔴 THE OPEN DECISION IS THE GA MODEL, AND IT IS PEDRO'S.** At the **2026-08-03 Agent Owners Alignment** (block at the end of this file) Corey Dulimba, Brian Chaikelson, Guliz Sicotte and Ankur Arora aligned on **"whoever is in the manifest is GA", per agent, now** — against Pedro's composite gate (skills, naming, manifest, UI, provisioning, security, ORR, legal, quality, reporting). Pedro acknowledged and did not decide. He committed to bring a **per-agent GA checklist to Monday 2026-08-10**. That checklist is the **Dimension A table** the V4 status doc has planned since 07-13. **Forcing date: Developers Live, weekly from ~08-24, Corey + Brian's session 09-01, both demoing Coworker only.**
>
> **The live artifact is Pedro's Slack canvas `F0BNF9LDKMW` "AEM Skills Naming Convention — WIP"** — convention, meta fields, one marketplace, plugin naming. Its state and the remaining fix-list are in the **2026-08-04 SKILLS GROOMING block**. ⚠️ **It was screen-shared to the agent owners on 08-03 but never posted as a link**, so Alejandro, Gerald, Emil and Sergiu still have nothing to read.
>
> **Clint's thread is no longer silent, and it has a clock.** 2026-08-04 00:42 CEST he posted *"Silence is acceptance? … in accordance with standard Apache voting rules I'll be merging this PR in 72 hours from now"* → **expires 2026-08-07 ~00:42 CEST**. Ian Reasor, Ian Boston and Carsten replied within 20 minutes. See the **2026-08-04 CLINT block** below.
>
> **Pedro was on PTO from the evening of Fri 2026-07-24 to the morning of 08-02/03.** The return-queue state of play is the **2026-08-03 FULL SLACK SWEEP block, archived to shard `..._ARCHIVE_2026-W32.md` on 08-04** (grep `FULL SLACK SWEEP` there) — read it with the PTO caveat at its head, which is the reason nothing in the 07-24→08-03 window is a responsiveness signal. Dated follow-ups are in `watches.md`, which is the single registry.
>
> **The four things waiting on him**, in order: **Clint Goudie-Nice** (5 days unanswered in his own `#aem-agent-owners-alignement`, Gartner demo + customer onboarding this week, admin-only-skill gating + co-innovation-only scoping) · **Tina Ngo** (blocked: wants GA timelines for all Coworker skills, says customers can't use Coworker until AEM skills are GA) · **Alejandro Moratinos** (asked 07-30 what the AEM skill-naming convention is, after Bertrand wrote *"there's urgency"*; unanswered, channel silent since) · **Ramon Bisswanger** (waiting to sync the Security Health internal Go-Live; he holds the 74%-vs-28% remediation numbers). Plus **Philippe Kapfer's 08-03 DM** offering to update the canvas and reporting a Foundation-Internal prod problem, and **Hemanta Gupta's Rubin finding** (no ingress for non-AEP teams — threatens the port).
>
> ⏳ **Open with Gilles Knobloch:** Pedro asked him 08-03 whether the KR 1e video played in full or as the broken 1-second version. Awaiting reply.
>
> **Prior sessions:** 07-27 OKR-review prep → shard **W30**; 07-20/21/22 rollout, marketplace + TBYB blocks → shard **W30**; 07-16/17 Manas → **W29**. Read `..._ARCHIVE_INDEX.md`, then grep the shard.
>
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

> ### 🔴🔑 2026-08-04 — CLINT: THE THREAD BROKE ITS OWN SILENCE WITH A 72-HOUR CLOCK, AND THE ENTITLEMENTS ANSWER IS NARROWER THAN WE RECORDED
>
> **⚠️ CORRECTION TO THIS FILE'S 08-03 SWEEP.** It recorded Clint's thread as *"ZERO replies in 5 days"*. True through 08-03. **At 2026-08-04 00:42 CEST Clint posted:** *"Silence is acceptance? Without further input, and in accordance with standard Apache voting rules I'll be merging this PR in 72 hours from now."* → **the clock expires 2026-08-07 ~00:42 CEST.** Three senior replies landed within 20 minutes of it, after five days of nothing. **He manufactured the gate nobody would give him, and it worked** — a clean instance of [[An Undefined Gate Is a Date Nobody Can Give]], this time from the other side of the table.
>
> **What the three replies actually said** (thread `1785359985.004509`, `#aem-agent-owners-alignement`):
> - **Ian Reasor (00:46):** co-innovation features should target *"a manifest other than `aem-aia`"*, unless `aem-aia` becomes the co-innovation manifest with the default Coworker manifest carrying GA. On admin scope: entitlements can switch skills off *"but I don't think that access level is one of the knobs"*, and — the load-bearing bit — ***"nobody has tested with the entitlements flag at all, so there wasn't a ton of confidence in it."***
> - **Clint (00:55):** the entitlements flag would not help anyway, *"There are as many admin product profiles as there are programs right?"*
> - **Ian Boston (10:50):** PR passes checks, **pin the version** so a skill-description change cannot break prod. Then the substantive answer: ***"CoWorker entitlements selecting skills operate at the Org level so you could use entitlements to select orgs but not admins."*** His workaround is runtime, not selection — the skill handles 403 and *"better still report to CoWorkers loop so it deselects the skill while reasoning"*. He also routes the source-of-truth question to `#coworker-eng-collaboration` / `#aem-agents-aep-collaboration`, and asks **where the CODEOWNERS for the `aem-aia` manifest are, because none were pinged on the PR.**
> - **Carsten (11:04):** *"yes, I think the aem-aia manifest will become the co-innovation manifest or there will be something similar based on the default coworker manifest"*, and he has opened that discussion in `#p42-architecture`.
>
> **🔴 SO OUR OWN RECORD OF THE 07-28 DECISION WAS TOO GENEROUS.** This file said Ian Boston's **2A = skill entitlements "mandatory"** was *"half the answer to Clint's admin-scope question"*. It is not. **Entitlements are org-level, so 2A answers question 1 (scope to co-innovation IMS orgs) and does not touch question 2 (admin-only skills) at all.** And a week after being declared mandatory, **nobody has tested the flag.** A decision named a mechanism that has not been exercised.
>
> **🔴 THE TICKET THAT WOULD ACTUALLY FIX IT IS DEAD.** `PLAT-290634` (*"AO: support per-user, integrator-delegated entitlement checks for capability visibility (remote permission provider) with caching"*) — **created 2026-06-16, status New, Unassigned, Normal, zero comments, untouched for seven weeks.** ⚠️ Memory implied Clint filed it with the 07-29 post; he filed it six weeks earlier. **It is not a net-new ask**: it extends the existing epic **PLAT-269752 "Permissions-based AO Agent Filtering"**, which already shipped an IMS permission provider (PLAT-283543), a Workfront one (PLAT-283281) and response caching (PLAT-283985). **So there is an owner on that epic, and the concrete PM move is to get 290634 attached to them with a date.** Clint already gates execution at `tools/list` under passthrough (`toolMode: full | restricted`); the gap is purely *selection before AO opens the session*.
>
> **WHAT IS ACTUALLY PEDRO'S IN THAT THREAD, none of it touched by the three repliers:**
> 1. **The lifecycle label.** Clint asked outright whether `experimental` is right for co-innovation capabilities. **Six replies, nobody answered.** `lifecycle` is already on the canvas fix-list, and **the same field answers Tina's GA question** — one vocabulary, two blocked people.
> 2. **Naming, repository placement and ownership** — he asks for it verbatim. That is the canvas. And Ian Boston's CODEOWNERS question has an answer Pedro already holds and nobody else does: **one broken owner (`aem-p42-forms` = "Unknown owner") on 12 lines, EPA and Governance absent entirely.**
> 3. **Cross-skill routing evals.** Clint's real fear is a selection collision — *"generic prompts about uploading, importing, migrating, or synchronizing assets may overlap other AEM skills"*. **The audit cannot answer it today: his two marketplaces are not in `fetch_skills.py`**, whose list is only `aem-aia-extensions`, `aem-experience-catalyst` (excat), `epa-experience-generation-extensions`, `aemforms-aia-extensions`. ⚠️ **Pedro declined the re-run on 08-04** — recorded as his call, not an oversight.
>
> **READ: do not block the PR.** Ian Boston approved it under one condition and Carsten is making Clint's placement retroactively correct. The value is in the four things above, not in gatekeeping. **The decision that is genuinely Pedro's is whether manifest-audience semantics get settled between Reasor, Boston and Carsten in `#p42-architecture`, or whether he names it as a product decision** — the same clean re-entry the 08-03 System Review identified, with **Corey's *"do we have a decision and go forward plan? If not, when will we?"* still unanswered 12 days on.**
>
> **🔎 KNOWLEDGE (P6):** [[An Undefined Gate Is a Date Nobody Can Give]] (Clint inventing his own gate — the strongest instance yet, and the first from a *counterparty*), [[Say the Sentence That Obliges — the Hedge Transfers the Ask]] (the reply Pedro owes must be object-backed — the audit, the CODEOWNERS gap, the lifecycle field, the epic owner — not "I think we should consider"), [[Success Definitions Must Be Agreed Before Metrics Are Scaled]], [[feedback_proposal_vs_decision]] (2A was a decision naming an untested mechanism). **No new entry.**

> ### 🔴🔑 2026-08-03 — AGENT OWNERS ALIGNMENT (HELD, ~33 min; ingested 08-04). THE ROOM ASKED TO REPLACE PEDRO'S GA GATE WITH "IN THE MANIFEST = GA"
>
> Transcript `Agent Owner Alignement/20260803 - Agents Owners Alignement.md`. **Yanira out; Marius Duta co-facilitated.** Pedro's first working day back. Full notes in the AAI Status & Todo (`## Agent Owners Alignment — Notes (Held 2026-08-03)`).
> **Attendees:** Pedro, Marius Duta, Tracy Seibel, Gilles Knobloch, Philippe Kapfer, Tina Ngo, Corey Dulimba, Brian Chaikelson, Ian Reasor, Ankur Arora, Guliz Sicotte, Carsten Ziegeler.
> ⚠️ **Attribution:** `CR BUCH 04/Basalt VC (5)` = **Marius Duta** (Pedro names him at 1:36; he opens *"Yanira is out today, so I will help Pedro facilitate"*). `CR BASL 05/SEEALPSEE VC (4)` = **Gilles Knobloch** for the 5:57 block only (Pedro: *"just as you mentioned, Gilles"*); **4-person room label, so the 17:22 EPA-bridge block is NOT safely attributed.** Unresolved: *"Vijay"*, *"Ravi"*, *"Nicole"*. Recording gaps ~9:43→12:38, ~24:17→24:44, ~27:38→28:51.
>
> **🔴🔑 THE EVENT: FOUR PEOPLE PUSHED BACK ON THE GATE MODEL, IN ONE ROOM, AND PEDRO DID NOT DECIDE.** Corey opened with *"do we have a clear path to call ourselves a GA?"*, Pedro listed the composite gate (skills · naming and formatting · manifest · UI · customer provisioning · security · ORR · legal · quality · reporting) with one ETA when all pass, and Corey rejected the *shape*: ***"I don't know what customer provisioning means. So that's not checked for my agent… That's not something that we even are in control of, so why is that a gate?"*** → *"I'm giving you the check mark for EPA"* → the counter-model, ***"isn't it just whoever gets added to the manifest would be considered GA?"***
> **His actual want, verbatim:** *"what I would like to see happen as quickly as possible is for our skills to be considered GA in the standalone coworker application so that as the rest of the field is talking to customers about coworker, AEM is included in those discussions."*
> **The alignment behind him was immediate and unanimous.** Brian Chaikelson (*"whatever is net new and ready works in the big coworker standalone UI"*), **Guliz Sicotte** (*"plus one, Corey, we should just go to GA with whatever is added in the manifest"* — note this is **Design**, Eugene's chain, not an agent owner), **Ankur Arora** (*"from our discovery and content optimization agents, we are ready with the skills… along with the EPA, we can bundle those skills and enable it for our first cohort"*, citing a selective Coca-Cola enable already done), **Ian Reasor** removing the risk objection (*"enabling that for customers doesn't turn off AI assistant… no harm, no foul"*).
> **Pedro answered *"I hear a lot of positivity here"* and *"I think I understand the ask here, Corey. Not sure we can solve that right now, but definitely."*** Corey let it go graciously. **The decision is open, it is his, and it is due Monday 2026-08-10** — he committed *"I'll work on that, and we can discuss next week with the status and next steps."*
> **🔁 THE ARTIFACT HE OWES EXISTS AND IS MISSING EXACTLY THE COLUMNS BEING ASKED FOR** (verified 2026-08-04 by reading the note, not from memory). It is `## Dimension A — AEM Agents to Skills and Manifests` in **`AAI - Project Folder/AEM Agents on Coworker — Status.md`** (the v7 leadership note), **seven rows already filled**. ⚠️ **Its columns are Agent · PM · Skills in Coworker · Renderer/UI rework · Bug bash — there is no readiness-date column and no gate column.** The note's own frontmatter records why: **Bertrand's 07-21 review *"trimmed Dimension A to bug-bash status"***. And section 5 of the same note has carried, since mid-July, the row *"The requirements behind each readiness cell (security ORR, traces, reports) — **Pedro** — **Owed to Corey. Teams cannot give a date without it**"*. → **Monday's deliverable is the missing columns on an existing table, not a new artifact.** The 07-13 plan (*"put Dimension A's empty table on screen and make each owner fill their own row"*) did not run on 08-03 — the naming canvas went on screen instead — and then the room asked for the table. **Two rows are already filled verbally and unbanked** (Corey for EPA, Ankur for Discovery + Content Optimization). **Cheapest ownership rep on the board this week.**
> ⚠️ **Read honestly:** this is the second time Corey has asked this question in the same words. On 07-09 he said *"How can we provide a date when we're going to be ready if we don't know what we need to do to be ready?"* **Four weeks later the checklist still does not exist.** Textbook [[An Undefined Gate Is a Date Nobody Can Give]] — and here **Pedro is the one who owes the gate.**
>
> **🔴 THE FORCING DATE ARRIVED FROM MARKETING, NOT FROM THE MIGRATION PLAN. Developers Live** — weekly webinars from ~**2026-08-24**, Corey's and Brian's session moved to **2026-09-01**, both demoing **Coworker only, no AI Assistant**. **Tina Ngo:** *"this is the first time when we will be publicly talking about our skills in a public forum… I kind of see this as a GA moment, meaning people are going to be interested in our skills. They should be readily available in Coworker."* ⚠️ In-room dates are approximate; **Marius owes a Slack thread pinning date, milestones, event link, agenda.**
>
> **🟢 GILLES INDEPENDENTLY CONFIRMED THE AUDIT'S INTERNAL-SKILLS FINDING.** *"there's this idea of business skills… the ones that we would want to expose, while maybe there are some skills that are more like… not something you would call directly. So there is a way to hide skills in the manifest… everything else is more like internal cooking."* → **corroborates `user-invocable: false`** (10 of 46 customer-facing skills are internal; all 7 underscore-named fails are internal). **The live question is not punctuation, it is whether the convention applies to internal skills at all** — and a senior voice has now said in the room that it should not.
>
> **PEDRO'S ON-THE-RECORD CALLS IN THE ROOM.** (1) **One marketplace, `aem-aia-extensions`, "please put them in there"** — and he backed **renaming it** because *"AIA will be decommissioned"*, offering to open the discussion. That is Raul Hudea's `aem-plugins-marketplace` proposal moving, in Pedro's naming lane. (2) The application list read out as **assets · brand governance · cloud manager · cloud service**, ⚠️ **so `cloudservice` is now stated by Pedro to the group while `scripts/audit_naming.py` still rejects it** — the audit vocabulary is formally out of sync ([[Success Definitions Must Be Agreed Before Metrics Are Scaled]]). (3) He flagged a **possible senior-management prefix ahead of `aem-`** (*"maybe the X"*) as still pending — the unresolved Tina prefix. (4) To Tina, the concession that matters: skills are *"almost"* there **but the UI will probably be late for any use case needing the panel interaction** — the 07-31 code-complete slip, stated to the owners for the first time.
> **🔴 ONE ANSWER TO RE-CHECK.** Philippe: *"This one will be installed by default on all manifests, correct?"* → **Pedro: *"That's my understanding, yes."*** **The next morning Reasor and Carsten both said `aem-aia` will probably become the CO-INNOVATION manifest.** Those do not agree, and Philippe is acting on Pedro's answer.
>
> **OTHER SUBSTANCE.** **Carsten settled the packaging question** Brian raised (separate marketplaces for GA vs not-ready?): *"we don't need to do that separation on the marketplace; we can do it based on plugins from a single marketplace"* — **plugins are the separation unit**, which is also the mechanism half of Clint's question. **Corey's two-track model** (phase 1 = GA in Coworker standalone riding the cohorts; phase 2 = AIA decommission, mostly Coworker-team work AEM joins) drew **Tina's objection** *"I actually think they need to happen in like parallel"*, with Brian naming the cost, *"it does complicate documentation… two different worlds"*. **Documentation surfaced as an unlisted GA gate** (Corey: *"one of the GA gates… making sure all of the coworker skills are documented somewhere"*), and **Tina's model is by use case, not by skill** — *"we're going to be adding skills every day. There's just no way that we're going to be tracking thousands of skills by the end of the year"* — she owes the link. **Philippe took the meta-fields action** (`domain` / `when-to-use` / `when-NOT-to-use`, written **wider than AEM**) after Pedro pointed at Forms as the team already using them with a positive effect on selection. **Guliz's shell-collision question** (does Coworker standalone via the shell conflict with AIA via the shell?) got only Corey's informal *"I don't have 100% answer on this"*.
>
> **🔎 KNOWLEDGE (P6):** [[An Undefined Gate Is a Date Nobody Can Give]] — **strongest instance in the file, and this one runs against Pedro**: same question, same asker, four weeks apart, gate still unwritten. [[Success Definitions Must Be Agreed Before Metrics Are Scaled]] (the audit's `APPLICATIONS` vocabulary vs what Pedro read out loud). [[A Packaging Unit Is a Customer Taxonomy — Ownership Needs Its Own Record]] (Carsten: plugins are the separation unit; Tina: group by use case, not by skill). [[Lead the Slide With the Honest Read of Your Own Metric]] (the UI-is-late concession, given unprompted). [[feedback_proposal_vs_decision]] (the room's GA model is a position, not a decision — do not bank it as settled). **No new entry — corroboration across four existing ones.**


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
