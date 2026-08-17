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

> ## ▶️ RESUME HERE — left off **2026-08-16 evening**, going into **GA week**. ✅ **THE AEM PLUGIN SUITE IS LIVE ON `cx-coworker` DEV AND STAGE** (PR `aep-ai#10608`, merged 2026-08-14 16:04), **and prod still carries 11 skills in 1 plugin.** 🔴 **THE BUG BASH STARTS TUE 08-18 AND ITS ENVIRONMENT IS STILL UNDECIDED.** 🔴 **AND "GA ON CLOUD SERVICE ONLY" IS ALREADY CONTRADICTED BY FOUR SKILLS THAT DECLARE `dma_aem_ams` — see the 2026-08-16/17 block directly below.**
>
> ⚠️ **`correct:` 2026-08-15 — "NAMITA UNANSWERED, FIVE PEOPLE WAITING" WAS WRONG. Slack read back: Pedro answered most of it on 08-14 morning.** At **07:58** he answered Ken Russell's second question outright (*"yes, the vast majority of prompts in AO 1.0 that customers are asking today are also relevant for Coworker - confirmed"*, `ty` reaction), and at **09:19** he posted his own **`Progressive activation` doc `F0BPBFCST5F`** (https://adobe.enterprise.slack.com/docs/T02CAQ0B2/F0BPBFCST5F) plus the [`20260814-AEM_COHORTS.xlsx`](https://adobe.sharepoint.com/:x:/r/sites/OneAEM/Shared%20Documents/AEM%20%26%20Agentic%20Web/AEM-Coworker%20Migration/20260814-AEM_COHORTS.xlsx?d=w09d49b4f21664b0b9babdfc88a7fca30&csf=1&web=1&e=ruI5AD), in group DM `C0BQ4L7BVL2` → https://adobe.enterprise.slack.com/archives/C0BQ4L7BVL2. **The doc already carries the lot sizes memory said were missing — *"A group of 50 customers is ideal in first step, then progressively in batches of 500"*, triaged by org interactions** (created 08-10 20:13, review requested from Yanira + Tina Ngo + four others).
> 🔴 **What IS still open is narrower and sharper.** (1) **Namita's literal *"Pedro what do you think about above?"* (00:28) never got a textual reply** — he posted the artifact 51 minutes later without addressing her, which is the silence-carries-the-default shape again. (2) **Two rollout speeds are on the table and nobody has reconciled them:** his doc says **50 then batches of 500** (matching Ken's *"20-50 then add 500 every couple of days"*), **Namita said *"we are rolling in waves of 50-100 over 4-5 weeks"***. (3) 🔑 **The doc's timeline is post-GA and that has never been said out loud in the room — `08-27` internal customers, `08-31` first TBYB batch (Top 50)**, against a GA of 08-24. Coherent with Pedro's own GA definition (announcement 08-24, activation after), **but Ken and Namita are arguing rollout speed without that frame in front of them.** (4) **Two asks sit on Pedro inside his own doc, both unactioned — the HIPAA customer check, and adding AEM Forms Product Management `99A27D6C5F569E170A495E8E@AdobeOrg` to the internal org list.**
> ✅ **Bug bash logistics moved without him** — Yanira sent the invites 08-14 19:54/19:58, added Eden Wen's four testers to the wiki, and Matt Colón covers for Tim Lynn. Eden's team declined AEM testing on knowledge grounds and nominated Silvia Mulet Ferre + Eugene Bannykh. **Nothing has been posted in `C0BQ4L7BVL2` since 08-14 19:58.**
>
> 🔴 **JEAN-MICHEL ASKED CONRAD WOLTGE TO TAKE THE "LEAD" ON COWORKER** (Bertrand, DM, 2026-08-13 09:15, *"ah ah"*). He forwarded the Loni note to Conrad. ✅ **Scope confirmed by Pedro 2026-08-14 — Conrad will sit ABOVE Ian Boston and Carsten Ziegeler.** That is the architecture chain Pedro's whole GA runs through: **Carsten is the ally who supplied the entitlement answer, the oncall counterpart and the prod ruling this week, and Ian Boston is the compliance red line on OBO, allowlisting and residency.** → **Pedro's GA lane now has an engineering escalation path that did not exist last week, and he did not put it there.** ⚠️ Nobody has said what "lead" covers; the announcement half is still Pedro's by his own 08-10 definition, but that is now asserted rather than uncontested. [[feedback_position_over_merit]]
>
> **✅ THE BAR NOW PRODUCES A POSITIVE NUMBER — 21 skills Ready for GA on all three criteria**, published 08-11 19:55 as a 4th report (`docs/runs/2026-08-11/ga-ready-skills-catalogue.md`), with the metadata extract for the documentation team. **Supersedes the 08-06 "0 of 87 / 4 with warnings" funnel** (kept in shard `..._ARCHIVE_2026-W32.md`, grep `AUDITS WENT PUBLIC`). ⚠️ **Already behind reality**: four EDA-side plugins renamed 08-11/08-12 and EPA reconsolidated its skills on 08-10 evening. **Re-run before quoting.**
>
> 🔴🔑 **GA IS DEFINED, BY PEDRO, 2026-08-10, IN HIS OWN WORDS — "GA = Adobe dit publiquement que les agents AEM sont disponibles, avec legal, security, docs, PMM derrière."** GA is the **public announcement moment** and it is his. ⚠️ **And customer announcements are owed BEFORE it** (his words, 08-10) — see the pre-GA announcement note below.
>
> **The two milestones are PANEL-LESS vs PANEL** — GA without the Coworker panel **08-24**, GA with the panel **09-21, TBC, "working on making it earlier"**. ⚠️ **He told Bertrand *"ETA milieu-fin novembre"* on 08-10 22:31 and corrected it to 09-21 in Slack and in the Loni note on 08-11. The November figure is WITHDRAWN — do not requote it.**
>
> 🔴 **DO NOT SAY "release belongs to the teams, per-plugin, via `lifecycle`". Pedro: "complètement faux" (2026-08-10).** That phrasing was Claude's, welded from the 08-06 decision file, and the `lifecycle` field has now been banked as the release mechanism **twice and corrected twice**. It is not the mechanism. What survives from 08-06 is only the definition above, which he confirms is the same thing as the announcement half.
>
> **The other two decisions stand.** 08-07 — the checklist is the announcement bar, not a release gate. 08-07 — agent-cut numbers publish on the **skill name** with the measured error rate footnoted, because Rubin cannot log the plugin axis PR15 chose. **PR15's plugin rooting stays the record of record; the name is what gets published.**
>
> **✅ THE HEADS-UP TO BERTRAND WAS SENT 2026-08-10 13:37 CEST** (DM `DQ6H0AV7H`, ts `1786361855.054289`). Pedro's draft, Claude critiqued the sign-off line against the canvas. What he actually sent, and it differs from the critique in two good ways: he **linked the 08-10 audit catalogue run** instead of headlining "0 of 87 pass" (the reader verifies it himself, and Pedro is not commenting his own number), and he wrote *"on a capturé les use cases manquants"* rather than naming the four PMs' panel reserve. ✅ **Bertrand answered the Loni question himself from PTO, 22:15 — *"et donc oui, c'est mieux et important de tenir Loni au courant (cc: me)"*.** ⏳ Eng/PgM blanks on EDA/Forms/Onboarding still open. **He promised weekly updates in that DM.**
>
> **🔴 Bertrand is on PTO 08-07 → 08-24, back ON GA day** (✅ corrected 08-10 from his Slack status; the earlier "returns after 08-24 / misses the GA" was wrong). He misses 08-10, the 08-14 sign-offs and the bug bash, then lands the day of the GA with zero runway. ✅ **The AI Ethics slot is now filled — decision 08-12, announce EPA on the informal non-blocking** (`decisions/2026-08-12-...`). 🔴 **The cover for 08-10 → 08-21 is still blank.** Background: 08-07/10 block, shard `..._ARCHIVE_2026-W32.md` (grep `REPORTING AXIS`).
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
> **✅ CLINT'S THREAD IS ANSWERED — Pedro posted 2026-08-05 17:29, released the merge, and got the `lifecycle` question answered by Carsten in 29 minutes.** The 72-hour clock is moot. **Two things came out of it: the vocabulary is now a committed 08-10 agenda item in public, and a 64-character skill-name limit landed that is not in the naming canvas.** Both the **2026-08-06 CLINT REPLY block** (archived 08-11) and the **2026-08-04 CLINT block** (archived 08-07) are in shard `..._ARCHIVE_2026-W32.md` — grep `CLINT` there.
>
> **Pedro was on PTO from the evening of Fri 2026-07-24 to the morning of 08-02/03.** The return-queue state of play is the **2026-08-03 FULL SLACK SWEEP block, archived to shard `..._ARCHIVE_2026-W32a.md`** (grep `FULL SLACK SWEEP` there) — read it with the PTO caveat at its head, which is the reason nothing in the 07-24→08-03 window is a responsiveness signal. Dated follow-ups are in `watches.md`, which is the single registry.
>
> ⚠️ **"The four things waiting on him" was audited against Slack on 2026-08-04 and three of the four were already wrong.** Only **Clint** is genuinely unanswered. **Tina and Alejandro were answered on 08-03**, **Ramon delivered rather than waited**, and **Hemanta has no DM with Pedro at all**. Corrected state, with what is actually owed, is the **2026-08-04 SLACK VERIFICATION block in shard `..._ARCHIVE_2026-W32b.md`**. **Lesson, second time in two days: a "waiting on you" list decays within days — verify it in Slack before acting on it** ([[feedback_confirm_ask_before_producing]], and the 08-03 sibling where a Slack deliverable was banked ✅ without reading the thread back).
>
> 🔴🔑 **THE REPORTING LANE HIT A WALL ON 08-06 AND IT IS SELF-INFLICTED: RUBIN CANNOT GROUP BY PLUGIN, WHICH IS THE AXIS PR15 CHOSE THAT MORNING.** The only fallback offered is grouping on the skill name — the axis the same decision disqualified. **Early access to an unreleased Rubin Report Builder lands the week of 08-10**, and Pedro said out loud *"if we miss that milestone, then I will have nothing for the GA."* **SKU vs TBYB still cannot be split** and Yanira named the older blocker (Andre, DAS team: no quick indicator). See the **2026-08-06 RUBIN SYNC block, archived to shard `..._ARCHIVE_2026-W32.md` on 08-10** (grep `RUBIN SYNC` there). ⚠️ **Two open questions routed to Angela Han and Karthik were not asked while both sat in the room for 22 minutes.** 📊 **The weekly Rubin digest of 08-10 landed: 84 WAU (−21.5%), 63 orgs (−13.7%), 7-day retention 11.6%, and the Agent Breakdown carries ONE row, "AEM Experience" — the agent axis is already collapsed in the tool, which is what the 08-07 skill-name decision was for.** Working channel is **`#aem-coworker-reporting` `C0BMVMA7DJS`**, where Pedro's three-level spec sits (overall TBYB/SKU · grouped by application token · per skill).
>
> ⏳ **Open with Gilles Knobloch:** Pedro asked him 08-03 whether the KR 1e video played in full or as the broken 1-second version. Awaiting reply.
>
> **Prior sessions:** 07-27 OKR-review prep → shard **W30**; 07-20/21/22 rollout, marketplace + TBYB blocks → shard **W30**; 07-16/17 Manas → **W29**. Read `..._ARCHIVE_INDEX.md`, then grep the shard.
>
> ### 🔴🔑 2026-08-16/17 — THE AUDIT ANSWERED THREE QUESTIONS THAT WERE QUEUED FOR PEOPLE, AND ONE OF THE ANSWERS BREAKS THE CS-ONLY LINE
>
> **A full Sunday on the KR review, the field all-hands deck and the Bertrand report. Every number below is from the audit run of `docs/runs/2026-08-16/`, read not re-run.**
>
> ⏳ **SECOND INSTANCE OF THE 08-15 CANDIDATE, and it is independent.** On 08-15 he answered three AO-ops questions by reproducing them in a browser. On 08-16 the entitlement question queued for **Raul since 08-13** was answered by **reading his own audit output** — different mechanism, same move, two days apart, both closing questions addressed to other people. **Candidate for the 2026-09-01 review, still NOT parked** (cap 7 of 8, closed): *reach for your own instrumentation before the escalation — a question you can reproduce or grep is not somebody else's question.* 🔑 The 09-01 review now has **two** dated instances, not one.
>
> **🔴🔑 `dma_aem_ams` IS ALREADY DECLARED, so "GA on Cloud Service only" is not what the skills say.** Four Cloud Manager skills carry **both** `dma_aem_ams` and `dma_aem_cloud` — `aem-cloudmanager-program-management`, `-environment-management`, `-pipeline-management`, `aem-cloudmanager-pipeline-troubleshooting`. **Raul's 08-13 question is answered by the corpus, not by an opinion**, and these are exactly the skills Pedro ran himself on 08-15. ⚠️ `entitlements.expected` in `aem-audits.yaml` still lists **one** pair, so the audit grades them `declared` without flagging the divergence — **the config is behind what the teams wrote.** 🔴 He told three PMM *"we aim for GA on CS only"* on 08-12. **Correct it before it reaches sales.**
> **🔴 A FIFTH GA BLOCKER NOBODY HAS LISTED — every AEM skill declares `lifecycle: experimental`.** The GA-ready report: *"no skill anywhere declares anything else"*, and **the field has to change before any of them ships.** Absent from Pedro's four-blocker list and from the Bertrand report.
> **📊 The entitlement picture, three layers and only two are in git.** `ENTITLEMENT_FILTERING_ENABLED` = server env, **not observable in any repository**, AO ops only · `permissions.enabled` = **192 of 241 manifests**, already thrown · `required_entitlements` = **82 of 126 skills**. 🔑 *"a gate standing open with our half of the declaration missing"*, and **the first team to add a declaration gets enforcement immediately, with no staged rollout.** ⚠️ **A missing declaration is more exposure, not less** — the skill is offered to every org that reaches the manifest.
> **📉 And prod is nearly empty.** `cx-coworker` prod loads **11 user-visible skills in 1 plugin** (`experience-governance` from `governance-agent-marketplace`); **none of the 16 stage plugins is in prod.** dev and stage each load **64 skills in 16 plugins, 56 user-visible**. GA-ready is **38 of the 71 in `aem-aia-extensions`** (funnel 71 → 70 → 47 → 38). **Do not let dev+stage read as customer-facing.**
>
> **🔴 THE MCP LOOKUP IS PROVEN FROZEN, NOT SUSPECTED.** Opening the board on 08-16 returned `Total tool calls (30d)` = **95,898, byte-identical to the 07-24 validated set** — impossible for a rolling window. Tool-call data comes from the **manual AWS export**; the Splunk-side panels moved and this one did not. **And `LOGREQ-16791`, the ticket to automate it, reads `Status Done / Resolution Done` while its only comment is the LPT bot auto-closing it as a process rejection** (*"no automated provisioning will occur from it"*). **Nobody re-filed it.** 📍 Canonical board pair + the staleness trap now in [[reference_splunk_mcp]].
>
> **✅ THE OBO PICTURE WAS WRONG IN THIS FILE AND IS NOW CORRECTED.** Reading the 08-13 `#p42-architecture` thread: **Jabran Asghar** — *"We already OBO-exchange the incoming token before calling AEM… so AEM effectively never sees `gpt_power_client`. The wiki's 'swap to an allowed client_id' is largely already there. The piece that's not there yet… is the 'only allow `gpt_power_client` when it's Coworker' check."* **Tanju**: extending client-ID validation to the `act` claim is *"straightforward"*. **Carsten Ziegeler**, same thread: *"we had various discussions around this topic since the CSO, none got to a final conclusion"* — his options write-up is wiki **`4003355459`**. → **one named check, not an architecture fight.** 📍 The 07-15 runbook moved repo, `Adobe-Experience-Platform/**aep-ai**/…/2026-0715-Governance-OBO-ClientID.md`; the `/ao/` URL is dead.
>
> **📅 THREE OUTWARD MOMENTS IN 48 HOURS, ALL HIS.** **08-17 KR 1e review** (speaking notes rewritten, vault `20260817 - OKR Review KR1e - Speaking Notes.md`) · **08-17 Loni follow-up with Tina Ngo**, agenda is the narrative for why AEM stays critical in an agentic world · **08-18 AEM & Agentic Web Field Global All-Hands, 10 minutes**, Pedro 5 + **Greg Klebus live demo** 5, audience **AEM customers and sales**.
> 🔴 **The all-hands is Tuesday and the confidence call is Thursday.** Anything said on the 18th precedes the data it would rest on.
> ⚠️ **Two claims in his deck he cannot source** — *"gapping 9 months of AI technologies"* and *"state of the art"*. And **`memory` as a named Coworker capability is unverified** in this record. All three flagged, all three still in the draft.
> 🟢 **The entitlement fix he found himself:** labelling the upper rungs `AEM on Coworker + Adobe Coworker` instead of `AEM on Coworker` — three words, and it stops the ladder promising AJO/GenStudio capability to an AEM-only customer. ⚠️ `Create a new site` has **no matching skill** in the graded catalogue.
>
> **⚠️ CLAUDE ERROR WORTH KEEPING.** A "quality" beat was written into the KR speech ending *"closing that distance is what the bug bash is for"*. **The 38.7% success rate is the AO agents weekly; the 08-18 bug bash is Coworker readiness. Two systems.** Pedro caught it. Beat cut, delivery note added. [[feedback_dont_conflate_pattern_with_object]] — and the same session had already conflated `version` with `update_policy` on 08-15.
>
> ### 🔬🔑 2026-08-15 EVENING — HE REPRODUCED IT INSTEAD OF ASKING, AND NINETY MINUTES CLOSED FOUR QUESTIONS QUEUED FOR AO OPS (compressed 2026-08-17)
>
> **The move worth keeping:** three of the four open bug-bash-environment questions were in `watches.md` addressed to other people with answers due Monday at best. He answered them himself, from a browser, 18:40 → 21:10. [[Say the Sentence That Obliges — the Hedge Transfers the Ask]] — the authority ended up in a reproduction, not in anyone's opinion. ⏳ **Candidate for the 2026-09-01 review, deliberately NOT parked** (cap 7 of 8): *reach for the reproduction before the escalation — an ops question you can reproduce is not an ops question.*
>
> **✅ Stage route dead, proven not argued** — `401 invalid OAuth token`, `author-p149891-*` is a different IMS org from the stage session. Fallback org `AEM Sites Engineering` returns `403025` + `User is not provisioned`, no Admin Console to self-provision. → **the bash runs on the prod shell.**
> **✅ The merged plugin set works** — on stage org `CM Gandalf`, `/aem-cloudmanager-program-management` made a live API call and returned **13 programs**. Manifest → skill load → auth → `cm` api_config → API, end to end, first real exercise of it. 🔑 It also offers a **manual author-URL fallback** = a live workaround for Cole Connelly's instance-picker ask.
> **🔴🔑 EVERY WALL WAS AN ENTITLEMENT, FIVE FOR FIVE, never a skill and never a config.** **Admin rights are not access — you reach an AEM environment only through one of its product profiles.** → the dominant failure mode for ~30 bug bashers is product profiles, and un-fixed the bash measures provisioning and reports it as agent quality.
> **📍 Yanira's three answers** (blocked since 08-15 03:32): program **`149891`** · prod-author **`1546481`** (stage-author `1546482`) · groups **`AEM Users` + `AEM Sites Content Managers`** (+ `AEM Assets Collaborator Users`). `AEM Showcase EDA CxCowork-2` (210760 / 2207539) is a **shell**, zero assets.
> **📤 Posted 21:23**, Carsten group DM `C0BPSMZBRPB` → https://adobe.enterprise.slack.com/archives/C0BPSMZBRPB/p1786821819886959, three ranked options, no replies that evening. ⚠️ Missing from the post: the 401 verbatim, the lloyds/prada precedent, a date.
> **🟢🔑 The best option is his own third — a Showcase-scoped prod manifest** with its own `api_configs`, precedent `cx-coworker-lloyds.yaml` / `cx-coworker-prada.yaml`. **Dissolves Ian Reasor's regression objection** and voids the CODEOWNERS high-blast-radius warning. ⚠️ Unknown to Lenard and Gerald: how an org is bound to a manifest.
>
> ### 🔴🔑 2026-08-14/15 — THE MERGE LANDED, AND THE BUG BASH PLAN TURNED OUT TO HAVE A HOLE (compressed 2026-08-17)
>
> **✅ SHIPPED. `aep-ai#10608`**, opened by Lenard Palko 14:12, approved by Gerald Prendi, merged **2026-08-14 16:04**. 16 AEM plugins on `cx-coworker` **dev and stage**, prod untouched, **both** manifest copies touched, plus `experience-governance` migrated to `aem-aia-extensions` 0.6.0 (which reached the lloyds and prada manifests too). **Nothing was validated before merge** — Gerald: *"Let's merge and test in stage."* ⚠️ **Lenard: *"I'm not sure how to test the rest of the plugins."* Fifteen are still unexercised.**
> 🔑 **The move that made it possible: default-in with an opt-out, not opt-in.** Announced 12:48, merged 3h15 later on a Friday. **The opt-out was real in intent and did not exist in practice** — own it out loud if a team objects; removal is one commit.
> 📊 **23 of 240 manifests → 86 of 241**, 67 of the 86 by inheritance because `cx-coworker` is the base dozens of customer manifests extend. **One PR took AEM from 23 surfaces to 86.**
>
> **🔴 THE HOLE: the bug bash targets a prod org and the plugins are on dev+stage.** AEM Showcase `38931D6666E3ECDA0A495E80@AdobeOrg` sits in **prod segments only, zero of 30 stage segment files** — an identity gate, not a config one. Ian Reasor hesitated on going to prod, *"concerned about potential regressions for the AEP team that is already using the prod manifest in prod"*.
> 🔴🔑 **And `prod/cx-coworker.yaml` carries ZERO `api_configs`** while dev and stage each carry a block of ten. **Pushing the plugin list to prod without porting them ships AEM skills that cannot call AEM.** On prod it is `aem-aia` that carries `aem`, `aem_discovery` and `cm`. **Never costed**, on a manifest whose CODEOWNERS reads *"changes affect all customers. High blast radius."*
> ⚙️ **Three axes were being conflated, now separated:** the **AO deployment env** (chosen by which shell you open) · the **AEM environment** (passed per call, `api_configs.aem` is `kind: dynamic`, so a stage manifest can drive a prod AEM author) · the **IMS org**, which is what actually gates who can log in. **Two are independent; the third decided it.** 🔎 Cloud Manager is stage-bound on two grounds — `base_url_env` follows the AO deployment **and** the client key differs (`agent-orchestrator-stage` vs `aep-agent-orchestrator`). `aem_discovery` is undecidable from the repo; only AO ops can read it.
> 🟢 **The pattern AEM should copy:** the prod manifest already carries per-server `env_overrides` with a `stage:` branch for *"stage IMS users"* — CJA, Experimentation, AJO, GenStudio, Marketo and Workfront all declare one. **AEM has none.**
>
> **🟢 IAN REASOR ANSWERED THE TWO ARCHITECTURE QUESTIONS (08-15 00:51).** The two-copy question is closed and Lenard's PR was right (*"which is why we need to update both"*). ⚠️ But *"Coworker just pulls in the latest plugin and **the version isn't actually read**"* **contradicts `05-update-strategy.md`** (FR-UPD-005 says `manual` is the default and notify-only; FR-UPD-002 says a catalog refresh must not alter installed content). It is a requirements doc with unchecked acceptance criteria, so it may describe intent. **Carsten has not answered.** ⚠️ Claude first inferred that Gerald's `update_policy: manual` freeze does nothing — **wrong, Ian spoke about `version`, a different field. Pedro caught it.** **What matters: if there is no freeze, a team merging into `aem-aia-extensions` on the 23rd changes prod behaviour on the 24th, and the only gate is the marketplace merge.**
> 🔴 **Which makes `aem-aia-extensions` the single point of control, and it is unguarded** — **16 open PRs**, six older than ten days, and **Alejandro Moratinos's *"who could help us to merge our changes"* (08-14) is still unanswered.**
>
> **📉 THE 08-15 AUDIT AND ITS THREE GAPS.** 16 of 17 `aem-aia-extensions` plugins load on dev+stage, **zero on prod**. **`aem-platform-codeveloper` is in no environment at all** and nobody has decided. **Forms, Guides, Onboarding and Codeveloper have not migrated to the target marketplace.** Consolidation stands at **71 of 126 skills (56%)**. ⚠️ *"This says where a skill is, never whether it should move."* **Nobody has written which of the six other AEM marketplaces are in GA scope.**
>
> **⚠️ THE AUDIT REPO OVERWRITES `docs/runs/<date>/` IN PLACE, AND IT HAS BITTEN THREE TIMES.** The 08-13 GA-ready link Pedro sent to every agent team now reads differently from what he sent. **Fix is mechanical: immutable dated folders with a `-b` suffix on rerun, or always cite the commit.** ⚠️ Deliberately **not** counted as the third instance of the parked *Your Own Artifacts Disagreeing* candidate — that row needs an instance from outside the Coworker programme.
>
> **🔎 KNOWLEDGE (P6):** [[Govern a Consistency Layer Over Primitives You Don't Own]] · [[An Undefined Gate Is a Date Nobody Can Give]] · [[Lead the Slide With the Honest Read of Your Own Metric, Not the Flattering Number]] · [[feedback_proposal_vs_decision]] · [[feedback_dont_conflate_pattern_with_object]] · [[feedback_confirm_ask_before_producing]].
> 🔴 **RETRIEVAL MISS, AND IT COST AN HOUR.** [[reference_coworker_enablement]] already records that Coworker access requires **the org to be in a segment in git**. Nobody pulled it before reasoning three levels deep into `api_configs`. **Next time a lower environment is proposed as a de-risking move, check who can log in before checking what the config points at.**

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
