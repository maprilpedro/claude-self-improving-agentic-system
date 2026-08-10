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

> ## ▶️ RESUME HERE — left off **2026-08-10 evening**, after the owners call. **The manifest turned out to be the real gate, and the audit had never measured the destination.**
>
> **✅ THE 08-10 OWNERS CALL HAPPENED AND IS CAPTURED — see the 2026-08-10 block below.** The live clock out of it: **the bug-bash manifest decision is owed WED 2026-08-12**, default `cx-coworker`.
>
> **🔴 THE BAR STILL PRODUCES 0: 0 skills conform on all three audits, 4 if warnings are tolerated, on the 87 user-visible.** **13 fail only disambiguation** (minutes of writing each) → **17 announceable with no migration.** Full funnel in the **2026-08-06/07 block, shard `..._ARCHIVE_2026-W32.md`** (grep `AUDITS WENT PUBLIC`). ⚠️ **Corey asked on 08-10 whether the bar counts warnings and whether hidden skills are in the cut. Answer it precisely — that IS the 0-vs-4 and the 87-vs-98.** ⚠️ And **EPA reconsolidated skills on 08-10 evening, so the catalogue is already stale on that agent.**
>
> 🔴🔑 **GA IS DEFINED, BY PEDRO, 2026-08-10, IN HIS OWN WORDS — "GA = Adobe dit publiquement que les agents AEM sont disponibles, avec legal, security, docs, PMM derrière."** GA is the **public announcement moment** and it is his. ⚠️ **And customer announcements are owed BEFORE it** (his words, 08-10) — see the pre-GA announcement note below.
>
> **The two milestones are PANEL-LESS vs PANEL** — GA without the Coworker panel **08-24**, GA with the panel **~09-21** (canvas column "Coworker UI with Panel GA"; the panel also sits in Post GA Fast Follows). **This is what he told Bertrand on 08-10 and it is the operative split.**
>
> 🔴 **DO NOT SAY "release belongs to the teams, per-plugin, via `lifecycle`". Pedro: "complètement faux" (2026-08-10).** That phrasing was Claude's, welded from the 08-06 decision file, and the `lifecycle` field has now been banked as the release mechanism **twice and corrected twice**. It is not the mechanism. What survives from 08-06 is only the definition above, which he confirms is the same thing as the announcement half.
>
> **The other two decisions stand.** 08-07 — the checklist is the announcement bar, not a release gate. 08-07 — agent-cut numbers publish on the **skill name** with the measured error rate footnoted, because Rubin cannot log the plugin axis PR15 chose. **PR15's plugin rooting stays the record of record; the name is what gets published.**
>
> **✅ THE HEADS-UP TO BERTRAND WAS SENT 2026-08-10 13:37 CEST** (DM `DQ6H0AV7H`, ts `1786361855.054289`). Pedro's draft, Claude critiqued the sign-off line against the canvas. What he actually sent, and it differs from the critique in two good ways: he **linked the 08-10 audit catalogue run** instead of headlining "0 of 87 pass" (the reader verifies it himself, and Pedro is not commenting his own number), and he wrote *"on a capturé les use cases manquants"* rather than naming the four PMs' panel reserve. ⏳ **Two things he put on Bertrand instead of deciding:** *"dis moi si tu veux que je loop Loni directement"* (Bertrand is on PTO, so silence defaults to Jaclyn — **Pedro should decide it himself in the 08-14 update**) and the Eng/PgM blanks *"dans les prochaines heures"*. **He promised weekly updates in that DM.**
>
> **🔴 Bertrand is on PTO 08-07 → 08-24, back ON GA day** (✅ corrected 08-10 from his Slack status; the earlier "returns after 08-24 / misses the GA" was wrong). He misses 08-10, the 08-14 sign-offs and the bug bash, then lands the day of the GA with zero runway. Heads-up drafted, two slots still blank (AI Ethics fallback, cover for 08-10→08-21). See the 08-07/10 block.
>
> **🟢 THE GA PLAN IS NO LONGER INTERNAL. Pedro presented it to the Coworker team on 2026-08-05 and got no push-back on the dates.** GA **08-24**, bug bash **08-17→08-21**, formal commitment from all AEM teams **Monday 08-10**. Cole Connelly: *"wow, that's sooner than I expected, so that's awesome."* **What came back is a list of things AEM owes, and two of them were not on any AEM plan.** See the **2026-08-05 ROLLOUT SYNC block, archived to shard `..._ARCHIVE_2026-W32.md` on 08-07** (grep `ROLLOUT SYNC` there).
>
> **🔴 THE PANEL-OFF ASSUMPTION IS CONTESTED.** The Road-to-GA canvas assumes AEM ships GA with the Coworker panel switched off. Cole named the hole: a customer holding **both AEP and AEM** would get the panel in AEP and not in AEM. *"It might be possible… but I just don't know if that's a bad product experience."* **It is now an explicit release decision, not an AEM assumption.**
>
> **🔴 TWO COLE ASKS ARE OWED BEFORE GO-LIVE, AND NEITHER IS IN ANY AEM PLAN** — the **AEM instance picker** in the Coworker UI (Workfront hit this and it produced semi-escalations), and **what the suggested prompts become in Coworker**. Pedro answered neither in the room.
>
> **🟢 There are now numbers where there were opinions.** The audit repo `OneAdobe/aem-coworker-audits` ran on 2026-08-05: **27 of 88 AEM skills are in the consolidation target**, **112 of 215 manifests** reach an AEM marketplace, naming is **14 conform / 34 warn / 29 fail** on the user-visible cut, and **13 of the 24 skills carrying a `when-to-use` restate their own description.** ⚠️ **These are the 08-05 figures and the catalogue has since grown to 98 (87 user-visible) — always name the run date and the cut.** Both the **2026-08-05 AUDIT REPO block** and the **2026-08-06/07 block** are in shard `..._ARCHIVE_2026-W32.md` (archived 08-10 — grep `AUDIT REPO EXISTS` and `AUDITS WENT PUBLIC`); [[reference_aem_coworker_audits]] has how to re-run it. 🔑 **Its first external pull arrived the next hour** — Yelena Doliner wants a skills repository reference on her cross-product wiki, and Yanira answered *"Pedro's putting a list of the Git repo."*
>
> **✅ THE GA MODEL IS DECIDED — 2026-08-06, by Pedro: separate the two milestones.** Release is per-plugin and belongs to the teams; the 08-24 announcement is portfolio-level and belongs to him. **Monday's deliverable is two artifacts, not one.** Record: `decisions/2026-08-06-ga-model-separate-release-from-announcement.md`, reasoning in the box below. **What is still open is the vocabulary** — if "GA" keeps naming both states the decision reverts silently, and that is the same `lifecycle` field Clint asked about on 07-29.
>
> **How it got here.** At the **2026-08-03 Agent Owners Alignment** (block archived to shard `..._ARCHIVE_2026-W32a.md` — grep `AGENT OWNERS ALIGNMENT` there) Corey Dulimba, Brian Chaikelson, Guliz Sicotte and Ankur Arora aligned on **"whoever is in the manifest is GA", per agent, now** — against Pedro's composite gate (skills, naming, manifest, UI, provisioning, security, ORR, legal, quality, reporting). Pedro acknowledged and did not decide. He committed to bring a **per-agent GA checklist to Monday 2026-08-10**. That checklist is the **Dimension A table** the V4 status doc has planned since 07-13. **Forcing date: Developers Live, weekly from ~08-24, Corey + Brian's session 09-01, both demoing Coworker only.**
>
> > **✅ DECIDED BY PEDRO, 2026-08-06 — "prends le troisième chemin. Sépare les deux choses qu'on confond."** Full record, alternatives, trade-offs and the scoreable predictions: `decisions/2026-08-06-ga-model-separate-release-from-announcement.md`.
> > 🔴🔴 **READ THIS FIRST — HALF OF THE BOX BELOW IS WRONG, PEDRO 2026-08-10.** Only the **definition** survives: **GA = the public announcement, with legal, security, docs and PMM behind it, and it is Pedro's.** He confirms the "announcement" half and the GA are **the same thing**. ❌ **The "release belongs to the teams, per-plugin" half is "complètement faux"** — do not repeat it, in any of its three phrasings (marketplace-file move, `lifecycle` field, team-sets-its-own-GA). ❌ **"Two milestones" does NOT mean release vs announcement.** It means **GA without the Coworker panel (08-24) vs GA with the panel (~09-21)**. The reusable reasoning further down (two events wearing one word, gate-shaped vs disclosure-shaped artifact, what Corey actually asked for) is still good; the mechanism claims are not.
> >
> > **THE DECISION AS ORIGINALLY WRITTEN (superseded in part, kept for the record): GA is two milestones, not one.** **Release belongs to the teams** and Pedro is out of that loop deliberately. 🔴 **CORRECTED 2026-08-07 by reading the thread — the release MECHANISM is the skill's `lifecycle` field, NOT a plugin move between marketplace files.** Carsten Ziegeler, 08-05 17:58 in Clint's thread, verbatim: *"For now, we can start with using the lifecycle metadata on a skill - we are currently in eng discussing on how to best manage the plugins/marketplace in our monorepo - **but that is not blocking GA**."* So the plugin/marketplace split is **an eng discussion in flight and explicitly post-GA**. The earlier line here — *"it matches the mechanism Carsten and Satya built on 08-04"* — was wrong twice over: on 08-04 11:04 Carsten wrote *"I **started a discussion** around this in C09KKLW1N86 on how we can support this from our end"*, and even the co-innovation-vs-GA manifest split is his *"I think… or there will be something similar"*. ⚠️ **A discussion was banked as a shipped mechanism and a proposal as a decision** ([[feedback_proposal_vs_decision]]) — and the false version contradicted **Pedro's own public position in the same thread** (08-05 17:29, *"I would like to use it [lifecycle] to differenciate skills that are GA and ones not"*). 🔑 **This puts `lifecycle` on the critical path of release, not only of vocabulary** — so the `skill_inclusion_policy` finding below (built, zero of 217 manifests use it, absent defaults to `stable`, which would delete AEM's honest 62-of-63 `experimental`) is now a release argument for 08-10, not a naming one. **The announcement** is the portfolio event on **08-24** — legal, security, ORR, AI Ethics, docs, PMM — **and it belongs to Pedro.** The composite list was never wrong about content, only about scope: it is the bar for what Adobe says publicly, not a gate on a manifest write.
> > **→ Monday's deliverable is therefore two things, not one:** a **per-agent release state** (teams fill it, Pedro holds the format) and an **announcement bar** (Pedro holds it, portfolio-level, not per agent). 🔴 **Pedro writes both — Claude does not draft them** ([[feedback_pedro_writes_claude_critiques]]).
> > **🔴 THE TRADE-OFF HE ACCEPTED, AND IT IS REAL:** he gives up the per-agent gate, which was the leverage the composite model gave him. **And the whole thing reverts silently if "GA" keeps being used for both states — so naming the two is now load-bearing, and it is the same `lifecycle` field Clint asked about on 07-29 that nobody has answered.** ⚠️ **AI Ethics on EPA does not move** (*"team will evaluate end of Aug"*, after both 08-14 and 08-24); the decision does not solve it, it isolates it to the announcement.
> > **Watch on 08-10:** if the split is right, Corey and Ankur take the release half without argument and the room moves to the announcement bar's contents. **If the room argues about the split itself, the framing is wrong.**
> >
> > **The reasoning that produced it (kept, it is the reusable part).** **The two models demand different artifacts, and that is the real cost of not choosing.** Under the composite gate the checklist is a **gate** — rows are conditions, the output is a date per agent. Under "in the manifest = GA" the checklist is not a gate at all, because each team can already decide; what Pedro would be writing is a **scope disclosure** — what a customer gets and does not get per agent, plus post-GA fast-follows. **Bring the gate-shaped artifact to a room that has moved to the other model and it answers a question they stopped asking.**
> > **The proposed split: the two models are arguing because two different milestones are wearing one word.** *"In the manifest"* is a **release mechanism** owned by the teams. ⚠️ **The claim that Carsten and Satya had already built it (one branch, `experimental` and `ga` marketplace json) is CORRECTED 2026-08-07 — see the box above.** Carsten's own words on 08-04/08-05 are *"I started a discussion"* and *"we are currently in eng discussing"*, and he put the plugin/marketplace work **explicitly post-GA**. The release mechanism available for 08-24 is the **`lifecycle` field on each skill**, which the team sets. The composite list is not a gate on release; it is the bar for the **announcement** — the portfolio-level 08-24 moment with legal, security, docs and PMM attached. **Let teams ship into the `ga` manifest as they are ready; hold the composite list for what Adobe says publicly.**
> > **Why it fits what Corey actually asked for:** *"for our skills to be considered GA in the standalone coworker application so that as the rest of the field is talking to customers about coworker, AEM is included in those discussions"* — that is a request about **the field conversation**, i.e. the announcement, not about a manifest write. It also keeps the one item that cannot be declared away: **AI Ethics on EPA still reads *"team will evaluate end of Aug"***, after both the 08-14 sign-off date and the 08-24 GA date.
> > **The question in one sentence:** does an agent's GA status get set by its own team moving a plugin, or by Pedro signing a row? **Answered 08-06: the team sets it, and Pedro sets what "GA" entitles a customer to expect.**
>
> **The live artifact is Pedro's Slack canvas `F0BNF9LDKMW` "AEM Skills Naming Convention — WIP"** — convention, meta fields, one marketplace, plugin naming. Its state and the remaining fix-list are in the **2026-08-04 SKILLS GROOMING block, archived to shard `..._ARCHIVE_2026-W32b.md` on 08-06** (grep `SKILLS GROOMING` there). ⚠️ **CORRECTED 2026-08-04 by reading Slack: it WAS posted** (08-03 13:42 in the Bertrand thread + 13:50 announced in `#aem-agent-owners-alignement`). The "written and never posted" line was wrong. **A second canvas now exists — `F0BMUV76DHU` "AEM Agents Road to GA", Yanira + Pedro, updated 08-04 15:11 — and it is the Monday deliverable.** Its full contents and the fix-list for it are in the **2026-08-04 SLACK VERIFICATION block, same shard `..._ARCHIVE_2026-W32b.md`** (grep `SLACK VERIFICATION` there).
>
> **✅ CLINT'S THREAD IS ANSWERED — Pedro posted 2026-08-05 17:29, released the merge, and got the `lifecycle` question answered by Carsten in 29 minutes.** The 72-hour clock is moot. **Two things came out of it: the vocabulary is now a committed 08-10 agenda item in public, and a 64-character skill-name limit landed that is not in the naming canvas.** See the **2026-08-06 CLINT REPLY block** directly below; the pre-reply state is the **2026-08-04 CLINT block, archived to shard `..._ARCHIVE_2026-W32.md` on 08-07** (grep `CLINT` there).
>
> **Pedro was on PTO from the evening of Fri 2026-07-24 to the morning of 08-02/03.** The return-queue state of play is the **2026-08-03 FULL SLACK SWEEP block, archived to shard `..._ARCHIVE_2026-W32a.md`** (grep `FULL SLACK SWEEP` there) — read it with the PTO caveat at its head, which is the reason nothing in the 07-24→08-03 window is a responsiveness signal. Dated follow-ups are in `watches.md`, which is the single registry.
>
> ⚠️ **"The four things waiting on him" was audited against Slack on 2026-08-04 and three of the four were already wrong.** Only **Clint** is genuinely unanswered. **Tina and Alejandro were answered on 08-03**, **Ramon delivered rather than waited**, and **Hemanta has no DM with Pedro at all**. Corrected state, with what is actually owed, is the **2026-08-04 SLACK VERIFICATION block in shard `..._ARCHIVE_2026-W32b.md`**. **Lesson, second time in two days: a "waiting on you" list decays within days — verify it in Slack before acting on it** ([[feedback_confirm_ask_before_producing]], and the 08-03 sibling where a Slack deliverable was banked ✅ without reading the thread back).
>
> 🔴🔑 **THE REPORTING LANE HIT A WALL ON 08-06 AND IT IS SELF-INFLICTED: RUBIN CANNOT GROUP BY PLUGIN, WHICH IS THE AXIS PR15 CHOSE THAT MORNING.** The only fallback offered is grouping on the skill name — the axis the same decision disqualified. **Early access to an unreleased Rubin Report Builder lands the week of 08-10**, and Pedro said out loud *"if we miss that milestone, then I will have nothing for the GA."* **SKU vs TBYB still cannot be split** and Yanira named the older blocker (Andre, DAS team: no quick indicator). See the **2026-08-06 RUBIN SYNC block** below. ⚠️ **Two open questions routed to Angela Han and Karthik were not asked while both sat in the room for 22 minutes.**
>
> ⏳ **Open with Gilles Knobloch:** Pedro asked him 08-03 whether the KR 1e video played in full or as the broken 1-second version. Awaiting reply.
>
> **Prior sessions:** 07-27 OKR-review prep → shard **W30**; 07-20/21/22 rollout, marketplace + TBYB blocks → shard **W30**; 07-16/17 Manas → **W29**. Read `..._ARCHIVE_INDEX.md`, then grep the shard.
>
> ### 🔴🔑 2026-08-10 — THE OWNERS CALL. THE MANIFEST WAS THE REAL GATE ALL ALONG, AND THE AUDIT HAD NEVER MEASURED THE DESTINATION
>
> **✅ THE CALL HAPPENED AND PEDRO SET A CLOCK.** 20:12 in `#aem-agent-owners-alignement`: two options for the bug-bash manifest, `cx-coworker` named as the default, **decision owed WED 2026-08-12** so teams can still PR their manifest updates. 🔑 **He named a default plus a date instead of asking an open question, and he listed the cost against himself** — *"Higher risk of exposing unfinished skills to customers"*, *"Governance Agent is the sole team on cx-coworker today"*. → [[Say the Sentence That Obliges — the Hedge Transfers the Ask]], clean positive instance. 20:23 he also posted the **TBYB progressive-activation canvas `F0BPBFCST5F`**, which is Namita's cohort-ordering ask finally moving.
>
> **🔴🔑 THE MANIFEST QUESTION, AND THREE PEOPLE GAVE THREE ANSWERS IN ONE HOUR.** Corey Dulimba spotted it **08-07 18:51** in the canvas thread (`C0BMUV76DHU`, parent `1786121430.931869`): *"what Manifest is this referring too? in the roadmap it says All AEM Plugins are set in CX Manifest **but here teams are checking it off for being in the AEM AIA manifest**."* **The Manifest-GA sign-offs were answering a different question than the column asked.** Resolved 08-10: Carsten 14:48 *"we havent full confirmation on that one yet - for now… everyone is in the AEM AIA manifest"* and again 15:35 *"lets focus on… the AEM AIA manifest"*; Corey 15:07 *"if we are only in AEM AIA then all customer would need to be manually provisioned and other DX skills are not there, don't think that is enough to say we are GA"* + *"AEM AIA was for co-innovation and CX coworker is where we need to be for GA"*; Pedro said `aem-aia` at 14:57 then `cx-coworker` at 15:30, and landed on `cx-coworker` in the 20:12 post. ⚠️ **Carsten also revealed the decision had been assigned to Pedro without him knowing** — *"someone mentioned last week that you are talking to coworker folks which manifest it will be"*, Pedro: *"Missed it was on me"*. **Carsten skipped the call** (he has just inherited the OBO/client-id topic, *"discussions were never concluded"*).
>
> **📏 THE OBJECT THAT SETTLES IT, read from the repo (sparse clone at `f648493`, 2026-08-06 — RE-VERIFY ON `main` BEFORE QUOTING).** `cx-coworker.yaml` carries **exactly one AEM plugin of the eighteen in `aem-aia`**, `experience-governance`. Workfront and loyalty are in; AEM is not. And `aem-aia.yaml` **explicitly lists `disabled_plugins`: cja, dx-api, experimentation, predictive-ai** — it deliberately cuts the AEP plugins, which is Corey's argument in the file. 🔑 **So "GA on `aem-aia`" means the customer gets an AEM-only assistant, not Coworker.** Two more mechanisms in that file: `plugin_deduplication_strategy: overwrite` with *"the earliest-listed marketplace wins"* and AEM's marketplace sitting **10th of 13**, so an AEM plugin can lose a name collision silently; and `required_entitlements`, which Gerald Prendi called **mandatory** for any plugin in the default manifest (07-29, `aep-ai#7241`/`#7225`) and which only Governance has been through.
>
> **🔴 THE AUDIT HAS NEVER MEASURED THE DESTINATION.** `aem-audits.yaml` lists **10 marketplaces and all ten are AEM**. `cx-coworker` registers **13**, of which only `governance-agent-marketplace` overlaps → **12 invisible**. `cx-coworker` *is* in `home_manifests`, so plugin placement is visible; the **collision surface is not**. 🔑 **Every disambiguation number Pedro quotes is AEM-against-AEM. Moving to `cx-coworker` changes the denominator and nobody has measured it.** Christian Meyer asked for exactly this (*"gestion des conflits, possiblement des requirements plus stricts"*, 15:32) and both his guesses already have objects. **Not commissioned:** add the 12 as `role: peer`, emit `required_entitlements`. ⚠️ Say out loud that it moves every denominator ([[Success Definitions Must Be Agreed Before Metrics Are Scaled]]).
>
> **🆕🔴 A GA GATE NOBODY HAD — ON-CALL.** Group DM `C0BPMVDECSU` (Yanira, Carsten, Hariprasad Kuppuswamy, Pedro). *"agents were never onboarded to `#skyline-oncall`"*; existing runbooks are written for **a2a**, not the skills model; **Carsten 16:32: *"the incident will first land with coworker and then it might be unclear which teams is responsible for a skill"*, 16:33: *"with a2a we had clear services with ownership in place."*** Yanira drives (collect runbooks → SRE review → Carsten reviews skill responsibility → start with EPA); Carsten covers because Ian is on PTO. Antecedent 08-07: **Toby Such** framed it as the pending ORR work, and **he is on PTO the whole month** (parent thread `C0BN3HU53GU`, Pedro is in it). ⚠️ **NOT the same object as the agent map** — the map is plugin→AOv1 agent for reporting, this is skill→responsible team for paging. **They share an input, not a column.** 🔑 **But the audit can produce the skill→team column, which revives the open "repoint the ownership axis onto CODEOWNERS" item — it now has a consumer.**
>
> **🔴 TWO PEOPLE ASKED THE SAME UNANSWERED COHORT QUESTION.** Brian Chaikelson 19:02 (*"Is this just the pods? When would the next group be?"*) and Silvia Mulet Ferre 20:19 (*"on the 24th, are we going to move all the AEM customers to co-worker integration, or will be just selected customers?"*). **Brian records his Developers Live segment WEDNESDAY, before his PTO**, and **EDA may slip a week** — Pedro proposed either announcing all agents with no special mention, or telling the few onboarded customers *"EDA not present yet"*.
>
> **🔴 TINA NGO INTERCEPTED THE LONI PATH, 18:27** — *"before you let loni know, can you tell me first? think we should communicate a joint plan PM/PMM"*. Pedro agreed at 18:32. ⚠️ **Not hostile and the ask is reasonable, but state the fact: on the afternoon he was weighing going to Loni direct, that route now passes through PMM first. He stays co-author, he is no longer the sender.** Watch whether the joint plan actually reaches Loni with his name on it ([[feedback_position_over_merit]]).
>
> **Also today.** Governance PgM sign-off closed after Pedro chased Daniel Mrose (Robert Guthrie, 16:46). **EPA is reconsolidating skills right now** (Corey 19:21 — model discovery removed, three Content Fragments skills merged into one), **so the 08-10 catalogue run is already stale EPA-side**. Mihai Copae delivered a first EH iteration on a PR link, Coworker-gated with fallback; Eugene is back and briefed. Corey asked the bar question at 16:52 — *"are we worried about warnings or only failure for GA? is your report picking up hidden skills or only the customer facing ones?"* — **the 0-vs-4 and 87-vs-98 question, answer it precisely.**
>
> **🔎 KNOWLEDGE (P6):** [[Say the Sentence That Obliges — the Hedge Transfers the Ask]] (positive instance, default + deadline + self-stated cost), [[Success Definitions Must Be Agreed Before Metrics Are Scaled]] (**refined** — the denominator is set by the destination, not by your own estate), [[An Undefined Gate Is a Date Nobody Can Give]] (Corey found the undefined gate himself this time, in the sign-off column), [[feedback_position_over_merit]] (the Tina interception), [[feedback_dont_conflate_pattern_with_object]] (Claude conflated the on-call ownership gap with the agent map; corrected in place).
>
> ### 🔴🔑 2026-08-07/10 — THE REPORTING AXIS IS RESOLVED BY PUBLISHING ON THE **WRONG** AXIS ON PURPOSE, AND A CARSTEN CORRECTION PUTS `lifecycle` ON THE RELEASE PATH
>
> **✅ DECISION 3, Pedro, 2026-08-07 — publish agent-cut numbers on the SKILL NAME, with the measured error rate in a footnote.** Closes the collision opened 08-06 (PR15 rooted the axis on the plugin; Rubin cannot log plugins). Of the two exits named that day, he took the second rather than wait on a logging field. 🔑 **It is defensible only because the error is measurable today** — publishing on a rejected axis without the number attached would be the thing the audit exists to prevent.
>
> **📏 THE ERROR RATE, from the published 2026-08-07 run — 98 catalogue rows, 85 distinct skills.** The name resolves the application from a **clean name segment on 51 of 98 rows**. Of the rest, **18** are inferred from loose tokens, **14** come from the declared `domain:` field and not from the name, **4** from the plugin, and **11 do not resolve at all**. ⚠️ **Say 98 rows and 85 skills every time** — the gap is duplication, not growth.
> 🔑 **`evaluate-page` is the whole argument in one skill.** It sits in the `experience-governance` plugin, so it is a Governance skill; its name files it under `sites`, while its three siblings `evaluate-image`, `evaluate-text` and `brand-discovery` go to `governance`. One name token separates the right row from the wrong one.
> 🔴 **The `assets` token is the real hole** — 17 skills carrying **at least four different agent answers** (Discovery 1, Content Optimization 1, no AOv1 agent 3, Onboarding 2, undecided 10). The canvas had assigned it Content Optimization, correct for 1 of 17.
>
> **📍 Canvas `F0BN06V01GF` "Agents to Skills Mapping" is the live artifact for this axis** (distinct from the naming canvas `F0BNF9LDKMW` and from the Road-to-GA canvas `F0BMUV76DHU` — **three canvases, say at the top of each what it is for**). Pedro filled it 08-07 off the audit table and made three changes worth keeping: **`Skill name "Application" = Agent`** (kills the ambiguity with the declared `domain:` field), a **`Confirmed` column**, and two decisions taken in place — **`aem-cloudmanager` = Experience Development Agent**, and `aem-cloudservice` = EDA on a token **zero skills carry today**. ⏳ **Open on it:** the Confirmed column is `:tbc:` on every row with **no owner named** (naming the owner per row is what could close five of the seven agent-map decisions in one meeting); the error-rate note is **not on the canvas**; the Rationale still states the future as present (*"all skills shall have a dedicated application token"* — today it is 51 of 98); two typos in the opening two lines (*"the spit previously available"*, and the goal sentence loops on "skills").
>
> **🔴 Bertrand is on PTO 08-07 → 08-24 and returns ON GA day** (✅ **corrected 2026-08-10 from his Slack status** — the prior "returns AFTER 08-24 / misses the GA itself" was wrong and had propagated into three files). He misses the 08-10 owners call, the 08-14 sign-offs and the 08-17→21 bug bash, **then lands the day of the GA and the announcement with zero runway.** Pedro drafted a heads-up (his own draft, Claude critiqued); its sign-off line was rewritten 08-10 against the canvas. Two slots deliberately left blank because only he can fill them — **what he does if the AI Ethics sign-off on EPA is not there by 08-21**, and **who covers escalation 08-10 → 08-21**. 🔑 **Narrower than first framed but sharper: the run-up is uncovered and he arrives cold on announcement day, so the ask is a named cover plus a pre-read before the 24th.** ⚠️ **Ian Boston is away too** (08-06, *"if you want to revert that while I am away, please feel free to take the approval over"*).
>
> **🔒 NEW HARD RULE, Pedro 2026-08-07 — Claude does not write code, ever.** See [[feedback_claude_does_not_code]]. Sibling of [[feedback_pedro_writes_claude_critiques]].
>
> **🔎 KNOWLEDGE (P6):** [[A Packaging Unit Is a Customer Taxonomy — Ownership Needs Its Own Record]] (**refined** — its 08-06 telemetry corollary now has a resolution: when the substrate cannot carry the axis you chose, publish on the axis it can carry *with the disagreement rate attached*, and keep the chosen axis as the record of record), [[Lead the Slide With the Honest Read of Your Own Metric, Not the Flattering Number]] (**3rd instance** — the footnote is the honest read of a number he owns, volunteered before anyone asked), [[Success Definitions Must Be Agreed Before Metrics Are Scaled]] (the 98-rows / 85-skills denominator), [[feedback_proposal_vs_decision]] (⚠️ **failed in capture, not in reading** — see the correction box above). **Parked candidate opened: "Report the Judgment, Not the Plan It Produced."**

> ### 🔴🔑 2026-08-06 — RUBIN SYNC (held, ~22 min). **THE AXIS HE DECIDED THAT MORNING IS THE ONE AXIS RUBIN CANNOT SEE**
>
> Source: transcript `2026/AEM Agents Intelligence/Rubin/20260806 - AEM Rubin Sync.md`. **Named speakers, no room mics, attribution clean.** Pedro, Yanira, **Angela Han**, **Karthik Penikalapati**, **Venkatesh Kunda**. ⚠️ **Venkatesh is NOT new** — already in [[project_adobe_org]] under Angela. Checked before writing 🆕, per the Huong Vu rule. **Full notes + the verbatims are in the AAI Status & Todo, `## Rubin Sync — Notes (Held 2026-08-06)`.** This is the one-month follow-up to the 07-06 Angela meeting (shard `..._ARCHIVE_2026-W28a.md`); both its threads (SKU split, digest as prototyping surface) were picked up, **neither closed.**
>
> **🔴🔑 THE FINDING — TWO OF HIS OWN 08-06 DECISIONS COLLIDE.** That morning PR15 rooted the agent axis on the **plugin** (declared 88 of 88, never forks; the name token is inferred, 67 of 88, and **disagrees with declared `domain:` on 14 of 18**). That afternoon **Rubin said it does not log plugins** — *"we still did not get that logging data"* — and offered **skill-name grouping, the axis PR15 had just disqualified.** Pedro named that fallback himself in the room without flagging the conflict.
> 🔑 **The ownership decision and the measurement substrate now disagree, and the substrate wins by default** — published agent-cut numbers would silently ride the rejected axis. **Two exits: get `plugin` logged, or publish on the name with the error rate in a footnote.** → Refined into [[A Packaging Unit Is a Customer Taxonomy — Ownership Needs Its Own Record]]: **choosing the axis is not the end, the telemetry has to carry it.**
>
> **🟢 WHAT HE GOT.** A **digest per skill-group** built from a grouping map he supplies, then a dashboard. Plus **early access to an unreleased Report Builder**, week of 08-10 — *"you'll be one of the very first users"*. Reports render HTML, carry a **subscriber list**, and **others can clone and customise them** = the distribution the three Workday reviewers asked for, at no writing cost. ⚠️ **The grouping map is the same object as the seven open agent-map decisions (51 of 88 skills have no agent), so it cannot go complete before 08-10.** 🔴 His own stated risk: *"if we miss that milestone, then I will have nothing for the GA."*
>
> **🔑 Karthik's design point, and it arrives from outside AEM:** the Report Builder exists because ad-hoc querying is non-deterministic — *"it might assume your SQL in a different way when different people ask the same question. This way your report is grounded to the same SQL query."* **A platform team shipped a product against the exact failure Pedro hit twice in two weeks** (07-24 instruments; 08-06/07 the 88→98 republish). → Refined into [[Success Definitions Must Be Agreed Before Metrics Are Scaled]]: definitions drift across **askers and time**, not only across teams.
>
> **🔴 SKU vs TBYB CANNOT BE SPLIT, and the blocker predates this meeting.** Rubin's provisioning data is AEP-side; whether AEM provisions the same way is unconfirmed. **Yanira supplied the harder fact — Andre (DAS team) has already said there is no quick indicator** — and will surface it on Slack. **This is the 07-06 SKU follow-up at one month, and it now blocks Namita's TBYB cohort ordering.**
>
> **🟢 ANGELA REFUSED THE SHORTCUT AND PEDRO TOOK IT WELL.** On side-loading org data: *"are you going to side load them every week?"* He conceded on the spot and reframed to finding the **root provisioning source, an API**. ⚠️ **Note what this is NOT: she objected to the cadence, not the capability.** Adjacent to [[H-009]]'s ingress question and it cuts mildly **against** Hemanta Gupta's walled-garden reading — **but it is not an answer, do not bank it as one.**
>
> **🔴🔑 THE MISS WORTH RECORDING.** Two open questions sat on the Status board **naming Angela Han and Karthik as their verifiers** — Ramkesh's GA-skills-only claim (**needed for 08-10**) and Hemanta's no-ingress finding. **Both people were in the room for 22 minutes. Neither was asked.** A retrieval failure, not a knowledge gap: both were written down, dated, and correctly routed. **Cheap fix: read the open watches for a person before the meeting with that person.**
>
> **⚖️ H-009 — DELIBERATELY NOT LOGGED.** The 08-03 review restricted it to three signals (Meschberger AOv1-decommission DACI · Marth's veto lifted · the IAM+RBAC answer). **None moved here.** Angela's engagement is the same shape already over-counted once — recorded here, kept out of `hypotheses/active.md` on purpose.
>
> **🔎 KNOWLEDGE (P6):** [[A Packaging Unit Is a Customer Taxonomy — Ownership Needs Its Own Record]] (**refined**), [[Success Definitions Must Be Agreed Before Metrics Are Scaled]] (**refined**), [[Metric Definition Ownership — PM Validates, Reporting Track Owner Implements]] (holding cleanly: Pedro defines the grouping, Rubin implements), [[Say the Sentence That Obliges — the Hedge Transfers the Ask]] (⚠️ **candidate, deliberately NOT counted** — the authority sat in a calendar date, not an object he owned, and this hypothesis was caught being padded at the 08-03 review).

> ### 🟢🔑 2026-08-06 — CLINT REPLY (verified by reading the thread, not from the plan). **PEDRO ASKED THE LIFECYCLE QUESTION WITH A NUMBER ATTACHED AND IT GOT ANSWERED IN 29 MINUTES AFTER A WEEK OF SILENCE**
>
> Source: thread `1785359985.004509`, `#aem-agent-owners-alignement` `C0BARAMM89Z`, read in full 2026-08-06. Pedro is reply 8 of 11, posted **2026-08-05 17:29 CEST**.
>
> **📤 WHAT HE POSTED, verbatim.** *"do not hold the merge on my account. **Lifecyle** - I checked the production aem-aia manifest this week and **62 out of 63 skills declare lifecycle:experimental. So the field does not seem to separate anything today. Taking on Agent Allignement call next monday. I would like to use it to differenciate skills that are GA and ones not.** cc Ian Boston Carsten Ziegeler. **Naming and repo** - I posted guidance here : F0BNF9LDKMW for naming convention - let me know. For Ownership - the aem-aia manifest has **twelve CODEOWNERS lines - aem-p42-forms is for unknown owner. Might be why no one pinged on your PR?**"*
>
> **🟢🔑 THE RESULT, AND IT IS A CLEAN POSITIVE CONTROL.** The lifecycle question had sat through **six replies over a week** with nobody touching it. Pedro asked it **with a measurement in front of it** and **Carsten Ziegeler answered 29 minutes later** — *"For now, we can start with using the lifecycle metadata on a skill - we are currently in eng discussing on how to best manage the plugins/marketplace in our monorepo - but **that is not blocking GA**."* → **[[Say the Sentence That Obliges — the Hedge Transfers the Ask]], positive arm.** The authority sat in objects he owned (the 62/63 manifest count, the twelve CODEOWNERS lines, the canvas ID), not in an opinion. Compare the 07-22 `#p42-architecture` hedge, which lost the same lane to two engineers six days later.
>
> **🔴🔑 HE ALSO BOUND THE VOCABULARY TO MONDAY, IN PUBLIC, IN FRONT OF IAN BOSTON AND CARSTEN.** *"Taking on Agent Allignement call next monday. I would like to use it to differentiate skills that are GA and ones not."* → **this is the load-bearing half of the 2026-08-06 GA decision** (release vs announcement reverts silently if "GA" keeps naming both states) and it now has a field, a forum, a date and an engineering yes. ⚠️ **Carsten's *"not blocking GA"* is the phrase to watch** — read one way it means *use the field*, read the other it means *the field is optional*, and the second reading is the reversion. **Pin on 08-10 that `lifecycle` IS what release means.**
>
> **🆕🔴 A HARD CONSTRAINT ARRIVED THAT IS IN NO AEM ARTIFACT — Carsten, 08-05 17:59: *"there is a 64 character limit for the skill name."*** Clint's reply (*"Will make sure to name all my skills exactly 64 characters to clobber that context window"*) got a 💜. **It belongs on the naming canvas `F0BNF9LDKMW` and it is mechanically checkable by the audit, which already parses every name.**
>
> **⏳ WHAT THE REPLY DID NOT TOUCH.** **Clint's question 2 (admin-only scope)** — Ian Boston routed the source-of-truth question to `#coworker-eng-collaboration` / `#aem-agents-aep-collaboration` and nobody has asked there; entitlements are org-level so 2A does not reach it. **`PLAT-290634` is still New/Unassigned/zero comments** since 2026-06-16, and its parent epic **PLAT-269752** has a shipping owner. **Cross-skill routing evals** stay unanswerable while Clint's two marketplaces are absent from `scripts/fetch_skills.py` (⚠️ Pedro declined that re-run on 08-04, his call). **The CODEOWNERS are still broken** — he named the gap, nobody fixed it.
>
> **🔎 KNOWLEDGE (P6):** [[Say the Sentence That Obliges — the Hedge Transfers the Ask]] (**positive instance, log it** — object-backed ask, 29-minute reply, after a week of silence on the same question), [[An Undefined Gate Is a Date Nobody Can Give]] (the 62/63 count is the measurement showing the gate field is empty), [[feedback_proposal_vs_decision]] (Carsten's *"we can start with"* is a position, not a decision — do not bank `lifecycle` as settled until 08-10). **No new entry.**
>
> **🔗 Permalinks** (workspace `adobe.enterprise.slack.com`, channel `C0BARAMM89Z`, thread `1785359985.004509`): [Clint's original 07-29](https://adobe.enterprise.slack.com/archives/C0BARAMM89Z/p1785359985004509) · [Pedro's reply 08-05 17:29](https://adobe.enterprise.slack.com/archives/C0BARAMM89Z/p1785943785311029?thread_ts=1785359985.004509&cid=C0BARAMM89Z) · [Carsten on lifecycle 17:58](https://adobe.enterprise.slack.com/archives/C0BARAMM89Z/p1785945537585269?thread_ts=1785359985.004509&cid=C0BARAMM89Z) · [Carsten on the 64-char limit 17:59](https://adobe.enterprise.slack.com/archives/C0BARAMM89Z/p1785945589411509?thread_ts=1785359985.004509&cid=C0BARAMM89Z)

> ### 🟡 2026-08-06 — THE `skill_inclusion_policy` GATE (⬇️ COMPRESSED 08-10: it is NOT the release mechanism, so it is a finding, not an argument)
>
> Source: sparse clone of `Adobe-Experience-Platform/aep-ai` at `main`, 2026-08-06. **Still true, still useful, just demoted** — Pedro killed "release = `lifecycle`" on 08-10, so this no longer carries a GA argument.
> - **Built and wired end to end.** A manifest declares top-level `skill_inclusion_policy`, a list of allowed `metadata.lifecycle` values; a skill outside the list is not surfaced. `agents/config/base.py:122`/`:424`/`:430`, enforced `skills/discovery.py:141`. Empty list = default = everything surfaces.
> - **🔴 Zero of 217 manifests use it**, across prod/stage/dev.
> - **🔴 The default inverts the incentive.** No declared lifecycle ⇒ defaults to `stable` (`skills/models.py:69`). AEM declares `experimental` on 62 of 63. A `['stable']` gate would delete the honest declarers and spare everyone who left it blank.
> - Documented values are `stable` / `experimental` / `deprecated`. **`ga` is not among them.**
> - ⚠️ **Audit mismatch, unfixed:** `aemaudit/skills.py:189` defaults absent `lifecycle` to `""`, AO defaults it to `stable`. The audit parses the field already but none of the five reports emit it.
> - 🔑 **Two method rules worth more than the finding.** (1) A negative result from a parallel `gh api` sweep needs a positive control or it is not evidence — the first pass produced silent false negatives under rate limiting. (2) Denominator discipline: 62/63 is the prod `aem-aia` manifest, the audit's native unit is the catalogue across nine marketplaces. Never mix them.

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
