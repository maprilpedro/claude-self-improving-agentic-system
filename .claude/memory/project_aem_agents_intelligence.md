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

> ## ▶️ RESUME HERE — left off **2026-08-15 evening**. ✅ **THE AEM PLUGIN SUITE IS LIVE ON `cx-coworker` DEV AND STAGE** (PR `aep-ai#10608`, merged 2026-08-14 16:04). 🔴 **AND THE BUG BASH PLAN HAS A HOLE THAT WAS FOUND ON 08-15 AND IS NOT YET FIXED — see the 2026-08-14/15 block directly below.**
>
> ⚠️ **`correct:` 2026-08-15 — "NAMITA UNANSWERED, FIVE PEOPLE WAITING" WAS WRONG. Slack read back: Pedro answered most of it on 08-14 morning.** At **07:58** he answered Ken Russell's second question outright (*"yes, the vast majority of prompts in AO 1.0 that customers are asking today are also relevant for Coworker - confirmed"*, `ty` reaction), and at **09:19** he posted his own **`Progressive activation` doc `F0BPBFCST5F`** plus the `20260814-AEM_COHORTS.xlsx`. **The doc already carries the lot sizes memory said were missing — *"A group of 50 customers is ideal in first step, then progressively in batches of 500"*, triaged by org interactions** (created 08-10 20:13, review requested from Yanira + Tina Ngo + four others).
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
> ### 🔴🔑 2026-08-14/15 — THE MERGE LANDED, AND THEN THE BUG BASH PLAN TURNED OUT TO HAVE A HOLE NOBODY HAD LOOKED FOR
>
> **✅ SHIPPED. `aep-ai#10608`, opened by Lenard Palko 14:12, approved by Gerald Prendi, merged 2026-08-14 16:04.** 16 AEM plugins on `cx-coworker` **dev and stage**, prod untouched. It touched **both** manifest copies (`.ao/` and `config/…/environments/`) and, as a second job in the same PR, **migrated `experience-governance` from `governance-agent-marketplace` to `aem-aia-extensions` 0.6.0**, which reached `cx-coworker-lloyds.yaml` and `cx-coworker-prada.yaml` too. Lenard's local env broke, so **nothing was validated before merge** — Gerald: *"Let's merge and test in stage. No worries at all."* Verified after: EPA skills run on stage (Lenard 16:36), Gerald 16:50 *"Looks good on stage for us too."* ⚠️ **Lenard: *"I'm not sure how to test the rest of the plugins."* Fifteen plugins are unexercised and nobody owns checking them before the bash.**
> 🔑 **The move that made it possible: default-in with an opt-out, not opt-in.** Pedro announced at 12:48 that everything in `aem-aia-extensions` would go to dev+stage that day and asked teams to opt out *"asap"*. It merged 3h15 later on a Friday afternoon. **The opt-out was real in intent and did not exist in practice** — worth owning out loud if a team objects Monday, since removal is one commit (Lenard).
> 📊 **The audit shows it:** `aem-aia-extensions` goes from **23 of 240 manifests to 86 of 241**, 67 of the 86 by inheritance because `cx-coworker` is the base dozens of customer manifests extend. **One PR took AEM from 23 surfaces to 86.**
>
> **🔴 THE HOLE, FOUND 2026-08-15. THE BUG BASH TARGETS A PROD ORG AND THE PLUGINS ARE ONLY ON DEV AND STAGE.** Christian Meyer flagged the timing on 08-14 (*"with the bug bash starting Aug 18, we absolutely have to complete this aspect by Aug 17"*); Ian Reasor said Grant Russell takes the task but *"we had some questions around whether we should be going all the way to prod or just to stage… we're a little concerned about potential regressions for the AEP team that is already using the prod manifest in prod."*
> **Pedro's proposed way out was to run the bug bash on the stage Coworker shell against the prod AEM org. It does not work, and the reason is identity, not config.** `38931D6666E3ECDA0A495E80@AdobeOrg` appears in **prod** segments only (`aem-orgs.yaml`, `aem-onboarding-orgs.yaml`) and in **zero of the 30 stage segment files**. Showcase is a prod IMS org; the stage shell authenticates against stage IMS. **You cannot log into stage Coworker as a Showcase user.**
> 🔴🔑 **AND THE PROD PATH IS BIGGER THAN ANYONE HAS SAID: `prod/cx-coworker.yaml` CARRIES ZERO `api_configs`.** dev and stage each carry one block of ten. **Pushing the plugin list to prod without porting `api_configs` would ship AEM skills that cannot call AEM.** On prod it is `aem-aia` that carries `aem`, `aem_discovery` and `cm`. **This is the real content of Ian's hesitation and it has never been costed**, on a manifest whose CODEOWNERS comment reads *"changes affect all customers. High blast radius."*
> ⚙️ **The three axes that were being conflated, now separated:** the **AO deployment env** (dev/stage/prod, chosen by which shell you open) · the **AEM environment** (passed per call — `api_configs.aem` is `kind: dynamic`, `host_allowlist: adobeaemcloud.com`, so a stage manifest can drive a prod AEM author) · the **IMS org**, which is what actually gates who can log in. **Two of the three are independent; the third is the one that decided it.**
> 🔎 **Cloud Manager is stage-bound on two independent grounds** — `base_url_env: CLOUD_MANAGER_URL` follows the AO deployment, **and** the client key differs (`agent-orchestrator-stage` in dev+stage vs `aep-agent-orchestrator` in prod `aem-aia`). So EDA's lane could never have been covered from stage anyway. **`aem_discovery` is undecidable from the repo** — same key in every env, and `AEM_DISCOVERY_URL` is server-side. Only AO ops can read it. (Analysis largely produced by Pedro's other assistant with repo access; **the three load-bearing facts were re-verified here — the zero `api_configs` on prod, the two client keys, the identical discovery key.** Its skill counts were not verified, do not quote them.)
> 🟢 **The pattern AEM should copy rather than invent:** the prod manifest already carries per-server `env_overrides` with a `stage:` branch commented *"stage IMS users (incl. dev cluster)"* — CJA, Experimentation, AJO, GenStudio, Marketo and Workfront all use it. **AEM has no such entry.**
>
> **🟢 IAN REASOR ANSWERED THE TWO ARCHITECTURE QUESTIONS (08-15 00:51).** (1) *"The first one is for local dev and the others are for their respective environments, **which is why we need to update both**"* — the two-copy question is closed and Lenard's PR was right. (2) ⚠️ *"AFAIK, Coworker just pulls in the latest plugin and **the version isn't actually read**. I'd love if we could actually have control over that, though."*
> 🔴 **THAT CONTRADICTS THE SPEC AND NOBODY HAS RECONCILED IT.** `docs/reference/domains/plugins-and-skills/05-update-strategy.md` **FR-UPD-005** says `manual` is the **default** and is *"Notify only. User must explicitly trigger update."*, with a third value `auto_patch` nobody has mentioned; **FR-UPD-002** says *"catalog refresh MUST NOT alter installed plugin content."* It is a requirements doc with unchecked acceptance criteria, so it may describe intent rather than the runtime. ⚠️ **Claude first inferred from Ian's answer that Gerald's 08-05 `update_policy: manual` freeze does nothing. That was wrong — Ian spoke about `version`, a different field. Pedro caught it.** **What actually matters: if there is no freeze, a team merging into `aem-aia-extensions` on the 23rd changes prod behaviour on the 24th, and the only gate is the marketplace merge.** Carsten has not answered.
> 🔴 **Which makes `aem-aia-extensions` the single point of control, and it is unguarded.** **16 open PRs** on 2026-08-15, six older than ten days, and **Alejandro Moratinos's ask of "who could help us to merge our changes" (08-14 10:23, `#aem-agent-owners-alignement`) is still unanswered.**
>
> **📉 WHAT THE 08-15 AUDIT SAYS, AND THE THREE GAPS.** 16 of 17 `aem-aia-extensions` plugins load on dev+stage, **zero on prod**. **`aem-platform-codeveloper` is in no environment at all** — Lenard flagged it (*"not in aem-aia.yaml at all, so I'm not sure if we should add this"*) and nobody has decided. **Forms, Guides, Onboarding and Codeveloper have not migrated to the target marketplace**; `aem-forms-experience-builder` has no prod manifest at all. And the consolidation itself stands at **71 of 126 skills in `aem-aia-extensions` (56%), 60 of the 115 a customer can reach (52%)** — **half the AEM estate does not come through the door that was just opened.** ⚠️ The report's own caveat: *"This says where a skill is, never whether it should move."* **Nobody has written which of the six other AEM marketplaces are in GA scope.**
>
> **⚠️ THE AUDIT REPO OVERWRITES `docs/runs/<date>/` IN PLACE, AND IT HAS ALREADY BITTEN.** `runs/2026-08-14/` received **six commits** on 08-14, the last at 17:01 (*"Rerun 2026-08-14: cx-coworker loads the target marketplace"*); `runs/2026-08-15/` two, the last at 16:56. **The 08-13 GA-ready link Pedro sent to every agent team now reads 19 of 66 with the line *"17 of the 19 are one plugin, `experience-generation`"* — a qualification his message did not carry.** 🔴 **Third occurrence** (08-06: catalogue 88→98 and naming fails 28→37 under three live Slack posts). **Fix is mechanical: immutable dated folders with a `-b` suffix on rerun, or always cite the commit in the link.** ⚠️ Deliberately **not** counted as the third instance of the parked *Your Own Artifacts Disagreeing* candidate — that row requires an instance from outside the Coworker programme.
>
> **🔎 KNOWLEDGE (P6):** [[Govern a Consistency Layer Over Primitives You Don't Own]] · [[An Undefined Gate Is a Date Nobody Can Give]] · [[Lead the Slide With the Honest Read of Your Own Metric, Not the Flattering Number]] (19 → 38 → the 08-15 recut; say what changed in the bar) · [[feedback_proposal_vs_decision]] (the spec is a requirements doc, not the runtime) · [[feedback_dont_conflate_pattern_with_object]] (`version` and `update_policy` are two fields; AO env, AEM env and IMS org are three axes) · [[feedback_confirm_ask_before_producing]]. **No new knowledge entry and no new parked candidate — parked is at 7 of a cap of 8 and closed until the 2026-09-01 review.**
> 🔴 **RETRIEVAL MISS, AND IT COST AN HOUR.** [[reference_coworker_enablement]] already records that Coworker access requires **the org to be in a segment in git**. Neither Pedro nor Claude pulled it before reasoning three levels deep into `api_configs`. **The identity gate was written down and went unread while the config gate was being analysed. Next time a lower environment is proposed as a de-risking move, check who can log in before checking what the config points at.**
>
> ### 🟢🔑 2026-08-13/14 — THE MANIFEST IS DECIDED, AND ENTITLEMENTS WENT FROM AN UNCOSTED PRECONDITION TO A DATED MANDATE IN ABOUT TWENTY HOURS
>
> **✅ MANIFEST DECIDED 08-13 11:41 — `cx-coworker`, dev/stage/prod.** Pedro closed it in public with the reasoning attached (skills quality feedback good · low customer exposure *given entitlements are set properly* · be as close to the GA setup as possible, including finding the undocumented blockers). ⚠️ **He framed it as *"given the low feedback here, consider it as both options are fine for all teams"*.** That is a defensible read — Carsten's objection had been rendered moot by the entitlement mechanism the day before — **but it re-uses the silence-carries-the-default move that the 08-11 note recorded as dead.** What actually rescued it was a new mechanism, not the silence.
> 🔑 **CARSTEN SUPPLIED THE ENFORCEMENT PEDRO'S BAR NEVER HAD, unprompted, in the same thread:** *"each team not in the monorepo on GA date has to take over oncall for one month completely."* An architect attaching a personal cost to non-compliance is worth more than another red row in an audit. **Nobody has repeated it since. It should be quoted in the Monday reminder.**
> 🔑 **And he closed Christian's real question:** merging to prod means GA, so should it wait for 08-24? Carsten — *"for as long as we have the entitlements in our skills, we dont regard this as a problem if that happens before the factual GA date."* → **prod can be populated before the 24th.** That is written nowhere else and it de-risks the bug bash.
>
> **📤 `required_entitlements` IS NOW MANDATORY, AND THE WHOLE CHAIN IS PEDRO'S.** Namita raised the requirement 08-12 → Pedro asked what the AEM product code actually is → **Namita and Cole both did not know** (*"this might be a question for someone who understands how AEM provisioning works"*) → Carsten confirmed `dma_aem_cloud` / `ims_product_context` and opened a `#p42-architecture` thread → no objection → Pedro sent the mandate to all teams **08-13 09:44** with the copy-pasteable snippet, the AO doc link, the audit link, a **Mon 08-17 COB** deadline, and the audit **updated the same message to enforce it**.
> **📊 Five teams acted inside eight hours** — **Alejandro Moratinos** (Governance, PR `governance-agent-marketplace#44`) ⚠️ **`correct:` 2026-08-14 — first banked as "Alejandro Ramirez Cheves", which is a different person. `amoratinos@adobe.com` / `U03CMAED797`, Senior SDE, is the one doing the Governance skill PRs. Ramirez Cheves (`ramirezc@adobe.com` / `WQXTVCLHM`) also exists and is in the agent-owner table as a Governance dev, so check the handle, never the first name** — Lenard Palko (EPA, `AEMAGT-2511`), Mayank Agarwal (Forms, `AEMAGT-2513`), Sergiu Coman (EDA, done), Ankur Arora (Discovery + Content Optimization, done). **Carsten adds a monorepo PR check next week**, so the requirement becomes structural rather than a reminder.
> 🔴 **ONE GAP, AND IT IS IN PEDRO'S OWN MESSAGE.** Raul Hudea, 08-13 10:18: *"for EDA, `dma_aem_ams` could be added as well."* **The mandate and the audit both know only `dma_aem_cloud`.** If AMS counts, every entitlement count published from 08-13 is measuring the wrong predicate for at least one team. **Ask Raul before Monday.**
>
> **📉 THE BAR GOT HARDER AND THE NUMBER FELL TO 19.** Funnel published 08-13 21:41 — **66** in the correct marketplace (`aem-aia-extensions`) → **56** name not a fail → **30** disambiguation not a fail → **19** declaring the expected entitlement. ⚠️ **This is not a regression from the 21 published 08-11** — he added a fourth criterion. **Say that when quoting it, or the movement reads as decay** ([[Lead the Slide With the Honest Read of Your Own Metric, Not the Flattering Number]]). The post names handles per failing plugin, which is what made the entitlement ask move.
>
> **🐛 BUG BASH — TARGET CONFIRMED, AND IT HAS ALREADY STARTED WITHOUT HIM.** AEM Showcase, org `38931D6666E3ECDA0A495E80@AdobeOrg`, tenant `123654`; wiki `4002944931`; CET-friendly and US-friendly slots both days; details to be added by Mon COB. **Pedro holds 08-18/19 so every team's skills are present, arguing partial coverage gives illegitimate feedback.** Christian Meyer and Corey Dulimba both pushed back the same day — Corey: *"we start testing now… the only benefit of having all skills present is checking routing… we can and should start testing ASAP."* EPA started 08-13, Marius ran an EDA session 08-13 with his own wiki. → **The all-in bash is real but the testing is already decentralised; the 08-20 confidence declaration will rest on a week of uneven coverage.** Amine Hajji is feeding it prompts **extracted from real customer usage via Pedro's own agent report tool**, which is the reporting lane paying into the GA lane.
>
> **🔴 THE ROLLOUT SHAPE IS BEING SET BY SOMEONE ELSE'S RISK MEMORY.** New group DM `C0BQ4L7BVL2` (Namita, Ken Russell, Tim Lynn, Ryan Cobourn, Eden Wen, Victor Vlasceanu, Yanira, Horia). **Ken Russell:** *"Can we roll this out in waves. Where we start small (e.g. 20 - 50) then add 500 every couple of days? I'd like to avoid running into issues like last time where we were dead on arrival or any potential capacity issues."* Namita answers **50-100 over 4-5 weeks**. **Pedro's own plan, posted 08-13 10:44, is an order (internals → TBYB by interactions → SKU → rest of internals) with no lot sizes** — so Ken's numbers fill a blank Pedro left. ⏳ **Namita 00:28: *"Pedro what do you think about above?"* Unanswered.**
> 🔑 **Ken's second question is a free test on Pedro's own data:** are today's AO 1.0 customer prompts still valid for Coworker, so someone can sanity-check which skills get selected? **That is the disambiguation audit's outcome measured directly instead of by proxy.**
> ⚠️ **Eden Wen declined for the Coworker design team** — *"my team does not have the knowledge to test AEM confidently"* — and nominated **Silvia Mulet Ferre + Eugene Bannykh**. Design coverage for the AEM bug bash is therefore AEM's own. Silvia then posted the per-skill UI components in `#aem-agent-owners-alignement` with a **GA-scope vs post-GA split** (Discovery + Onboarding in scope, Experience Production after) and an open offer to review any team's agentic flow.
>
> **⚠️ EPA CONTENT FRAGMENTS — A REVIEW BODY WAS RULED OUT OF SCOPE BY THE FOUR PEOPLE IT WOULD HAVE REVIEWED.** Group DM `C0BPS8BS39C`. Yanira opened 08-12 20:56 — new `aem-sites-contentfragments-*` skills, **no readiness done, biggest concern Legal + AI Ethics**, proposing a fast-track call. **Two hours and seventeen minutes later she closed it herself** — *"Then I think we are covered and won't need Legal / AI Ethics reviews imho"* — on Andreea Miruna Moise's argument that the functionality was already in EPA and CF Discovery is a split of Assets, plus Corey's *"implicitly part of EPA."* Pedro replied *"Great !"* 08-13 10:01. **The reasoning is defensible; the shape is four people deciding that an external reviewer has nothing to look at** ([[feedback_proposal_vs_decision]]). 🔴 **And the three fast-follows Yanira had attached as the price of skipping (Security threat model · ORR runbook in `#skyline-oncall` · CCF onboarding) died with the conclusion — nobody re-owned them.** ⚠️ Corey, same thread: *"if we miss the 24th we'll just add them in the following week"* — **second team in four days to treat GA as rolling** (Brian, dev skills, 08-10). Nobody has said no to either.
>
> **🟢 OBO NOW HAS A DOCUMENT.** Carsten wrote up the state and the paths forward — wiki `4003355459` *"20260813 Supporting Coworker with OBO enabled"*, posted 08-13 11:12 in `#p42-architecture`; Pedro relayed it to the agent owners for anyone with MCP-calling skills. **The three-layer OBO gap logged 08-11 finally has an object.** ⚠️ Two live corrections from Carsten the day before: the global service proxy is **not** a single point of fix (*"we ran into the trap that some of the threads contained wishful thinking"*), then better news that **OBO is used for MCP calls and not API**, so One AEM MCP could be a single fix point again — **needs Tanju, back Mon 08-17.**
>
> **🏗️ EH IS MOVING ON MONDAY, SORIN'S CALL.** He updates Experience Hub 08-17 for the Coworker input + navigation item + announcement and top-bar message, validating on AEM Showcase, and opened a tracking thread with an `EH — Checklist GA 24th` doc. Pedro cc'd. **This is the EH placement answer arriving as execution rather than as the written decision that was owed ~08-17.**
>
> **📅 COVER GAPS STACKING AROUND THE GA.** Ian Reasor is out **08-25 → 09-09**, Grant Russell covering the architect weekly and the agent owner alignment. Toby Such out all month. Andreea Miruna Moise on PTO next week (backup Andreea-Daniela Balan). **Bertrand lands 08-24 with zero runway. The GA week is the thinnest-staffed week of the quarter.**
>
> **📚 Yanira moved documentation to JIRA `CQDOC-23874`** at the doc team's request and named all seven agent PMs to contribute, cc Pedro and Tina.
>
> **🔎 KNOWLEDGE (P6):** [[Govern a Consistency Layer Over Primitives You Don't Own]] (**the entitlement mandate is the cleanest instance on file — he owns none of the skills and set a field every one of them must carry**) · [[Say the Sentence That Obliges — the Hedge Transfers the Ask]] (authority sat in the AO doc + Carsten's confirmation, not in his preference; five teams in eight hours) · [[An Undefined Gate Is a Date Nobody Can Give]] (**positive control — a named field, a snippet, a deadline and an audit that publishes who is missing**) · [[Platform Contribution Model with Quality Gate]] · [[Explicit Sequence as Protection Against Spread]] (the deployment order) · [[Lead the Slide With the Honest Read of Your Own Metric, Not the Flattering Number]] (19 vs 21) · [[feedback_proposal_vs_decision]] · [[feedback_give_url_not_just_id]]. **Parked candidate opened: "A Mandate Moves When It Ships With the Field, the Snippet, the Deadline and the Audit That Names Who Is Missing"** — ⚠️ both instances are inside the Coworker migration; needs one from outside before it can promote.
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
