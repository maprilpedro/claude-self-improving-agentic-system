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

> ## ▶️ RESUME HERE — left off **2026-08-25 afternoon**. 🚀 **GA DAY WAS 08-24 AND THE PUBLICATION SLIPPED ONE DAY TO 08-25 MORNING.** ✅ **The `Known limitations` note is written and Alison Heimoz put it on the AEM Agentic Capabilities Overview page.** 🔴 **The engineering Go/No-Go from Mitch Nelson + Conrad was still unsigned at 08-24 15:40.** 🔑 **Pedro corrected Claude on the load-bearing fact: a customer who MIGRATES to Coworker loses AI Assistant.** 🔴 **The internal all-Adobe GA announcement is drafted and not sent; its "all AEM Agents are now available" line is contradicted by Pedro's own prod audit.** See the 2026-08-24/25 block directly below.
>
> ### 🚀🔑 2026-08-24/25 — GA DAY, THE DOC NOTE, AND THE CORRECTION THAT CHANGES THE CUSTOMER STORY
>
> **🔑🔴 THE CORRECTION, AND IT IS PEDRO'S, NOT CLAUDE'S.** Claude argued twice on 08-24 that a limitation note must say *"AI Assistant remains available"*, reasoning from **cohort 3** (AEM Cloud Service is excluded from AIA deprecation, and Ken Russell wrote 07-14 that *"cohort 3 probably doesn't have a date"*). **Pedro overturned it in one line: *"un client migre sur Coworker ne peut plus utiliser AIA."*** ⚠️ **The error was conflating two objects again — "the day AEP switches AIA off for everyone" is NOT "what happens to a customer who moves."** A customer can migrate before cohort 3 forces them, and at that moment they lose AIA. **So Pedro was right at 15:29 when he said *"ils ne fonctionneront pas"*, and Claude pushed him the wrong way.** → [[reference_coworker_enablement]] corrected. **Consequence for the published note: for a MIGRATING customer, ABAC is not "not yet available", it is a loss with no replacement and no date.** The open question Pedro can answer from the cohort file: does anyone in the 08-27 internal / 08-31 TBYB batches use ABAC or the panel-dependent use cases today?
>
> **📄 THE `Known limitations` NOTE IS PUBLISHED (Pedro wrote it, Claude critiqued, Pedro cut one paragraph).** Posted 08-24 15:38 in group DM `C0BSBHKHLU9`; **Alison Heimoz added it to the Agentic Capabilities Overview page in the AEM docs at 15:43.** Final text: *"The initial release of AEM agentic capabilities in CX Enterprise Coworker covers the use cases listed on this page. Some capabilities that are available today in AI Assistant are not yet available in Coworker. The in-app side panel is not part of this release. Use cases that depend on it are therefore not yet available, including conversational authoring of attribute-based access control (ABAC) policies and assets review. This page is updated as capabilities become available in Coworker."* 🔑 **Pedro's own decisions that shaped it, all correct:** title announces a **limitation**, not parity (he dropped the word "feature parity" himself); **no date** for the panel; and he cut the "AI Assistant remains available" paragraph because it was false for a migrating customer. ⏳ **Alison's question at 15:43 is still unanswered — *"Is that for the Coworker chat page, or the AEM agentic capabilities overview page, or both?"*** And there is now a **third branch**: Khushwant Singh's new standalone Forms article.
>
> **✅ THE PRODUCT NAME IS SETTLED, FROM THE DOC ITSELF.** Alison, 08-24 15:19, quoting the live overview page: *"New AEM agentic capabilities through **CX Enterprise Coworker**, an evolution of AI Assistant built to help you do more, faster."* → **CX Enterprise Coworker**, not "Adobe Coworker". Closes the 08-21 watch that Claude could not resolve (a WAF blocks the public page).
>
> **🔴 THE GO/NO-GO FROM ENGINEERING WAS NOT SIGNED WHEN THE DAY ENDED.** Yanira, DM 08-24 15:32: *"I sent the email to Mitch and Conrad. As per Jaclyn they should go approving Go No Go from engineering side."* Then **15:34, and this is the line to keep: *"I'm going to start a slack conversation because that email will do nothing."*** Jaclyn Eckersley already had a thread with Conrad + Mitch; update expected *"over the next few hours"*. Sign-offs canvas = `F0BMUV76DHU`. **Greg Klebus signed COA off at 15:51** and warned he might miss the go/no-go call. 🆕 **Mitch Nelson `W4R5W3ZCH` — engineering Go/No-Go approver alongside Conrad, absent from memory until now.**
>
> **📣 THE INTERNAL ALL-ADOBE GA ANNOUNCEMENT IS DRAFTED AND NOT SENT, AND TWO CLAIMS IN IT ARE WRONG.** (1) 🔴 ***"all AEM Agents are now available through Skill in Coworker"* is contradicted by Pedro's own published audit** — prod `cx-coworker` carries **11 user-visible skills in 1 plugin**; the 08-14 merge (`aep-ai#10608`) put 16 plugins on **dev and stage only**; `aem-edge-dispatcher` was deliberately deferred to the release after GA (Abhishek Garg, 08-16); and anything off the GA-ready catalogue at 08-17 COB was **pulled from GA by Pedro himself**. (2) ⚠️ ***"we will reach feature parity on UI late September"*** re-introduces the exact word he had just removed from the external doc, and **the panel does not deliver parity** — ABAC carries two undated blockers beyond it. (3) ⚠️ *"Paying customers migrated once Coworker Panel is ready"* is a different gate from the one in his Loni mail (**feature-parity plan, target 09-02**). (4) ⚠️ *"Deployment starts today"* vs his own progressive-activation doc (**08-27 internal, 08-31 first TBYB batch**).
>
> **🔑 BERTRAND IS BACK (08-24) AND HE REJECTED THE ALL-HANDS SLIDES.** Verbatim, 12:14: *"donc les slides sont bien, mais je suis pas sûr que c'est ce qu'il faut pour un all hands"* / *"ça fait très point projet"*. What he wants instead: **a live demo** — list the AEM skills, an asset search, a page creation, **two conversations prepared in advance** (*"c'est trop lent en live"*), and a talk track on *"les problèmes qu'on a rencontrés avec la génération d'avant, **notamment le routing vers la bonne skill/API, et pourquoi c'est résolu (ou mieux) avec CW**"*. On Greg's demo: *"ça marche bien pour illustrer COA, mais il faut **monter d'un cran** pour le all hands."* ⚠️ **The AEM all-hands is WEDNESDAY 08-26; tonight's 08-24 all-hands was DX.** Pedro asked for 5 minutes 15:00-16:00, Bertrand had **Loni at 15:30** and pushed to 08-25. **The demo is not rehearsed.** 🔑 **The same feedback applies verbatim to the GA announcement** — it reported activity and named no problem solved.
>
> **📊 THE BUG BASH NUMBERS ARE PEDRO'S AND NOBODY ELSE IN THE ROOM HAS THEM** (posted 08-19 21:49): **59 unique AEM skills, 1,838 queries, 540 conversations, 31 unique users, 3.4 turns per conversation.** Split: Assets (Discovery 311, content optimisation 123) · Sites (CF discover 99, visualize 80, inspect 56, bulk edit 34, page updates 28) · Cloud Manager (programs 76, environments 62, pipelines 47) · **Forms (adaptive form creation 53, editing 55)** · Governance (brand guidelines 16). **This is the visibility asset for Wednesday, not the slides.**
>
> **🆕 FOUR NEW NAMES, ALL DOCS-SIDE OR GO/NO-GO.** **Alison Heimoz** `W4RSUJDFW` aheimoz@adobe.com — **owns the AEM docs**, publishes the overview page. ⚠️ **In Basel 08-25 morning, travelling the afternoon, OOO Wednesday 08-26.** **Khushwant Singh** `WAM5KDYBZ` — wrote a new **standalone "Forms Agentic Capabilities Overview" article** 08-24 08:42, still a PR on his personal fork, review requested from Arneh Jain + **Shraddha Singh** `U06NF880220`. **Anuj Kapoor** `WCR7ZUNNB` — asked via Alison 15:45 *"any docs around OneAEM MCP or who owns this?"*
>
> **🔴 ONE AEM MCP WAS ASKED ABOUT TWICE ON GA DAY, BY TWO DIFFERENT PEOPLE, AND NEITHER GOT AN ANSWER.** **Apoorva**, 12:19, group DM `C0BS499NFQD` (with Piyush Singhal, Greg Klebus, Prashant Jain, Yanira): *"is OneAEM MCP also GAing in Coworker along with Coworker skills today?"* **Anuj Kapoor via Alison**, 15:45, on docs and ownership. 🔑 **This is the undeclared GA dependency Pedro flagged himself on 08-11** (*"some AEM skills are using MCP for tasks - thus have a dependency on MCP. It's not explicit in the GA"*) **becoming explicit from two directions on the day.** He has the answer: `adobe-rnd/aem-sites-content-service`, Tanju Erinmez, and `DXARB-1073` came back green 08-19 ([[reference_one_aem_mcp_repo]]).
>
> **🗓️ THE AIA→COWORKER SPEED TIMELINE, BUILT AND VERIFIED THIS SESSION** (Pedro is using it in a slide). **83 working days / 117 calendar days from the 04-29 AOv2 alignment to GA 08-24.** Segments in working days: 04-29→06-10 **30** · 06-10→06-15 **3** · 06-15→07-01 **12** · 07-01→07-13 **8** · 07-13→08-04 **16** · 08-04→08-24 **14**. Cumulative 30·33·45·53·69·83. Raw Mon-Fri, no public holidays. 🔑 **The two numbers that land hardest: Coworker went GA 06-10 and AEM had six skills on it three working days later; and 53 working days separate Coworker GA from AEM GA.** ⚠️ **Do not call 04-29 a decision date** — Bertrand corrected it to "discussed, not decided" on 05-04. ⚠️ **Do not chain the skill counts** (6 → 88 → 102 → 105 → 126 → 66 come from different runs and scopes); the one clean chain is **6 skills on 06-15 in the AIA catalogue → 16 plugins on `cx-coworker` dev+stage on 08-14**. ⏳ **Pedro's `08-04 GA Plan Creation` milestone has no source in memory** — what memory has is the plan presented to the Coworker team 08-05 and the GA model decided by Pedro 08-06.
>
> **🔎 KNOWLEDGE (P6):** applied — [[Lead the Slide With the Honest Read of Your Own Metric, Not the Flattering Number]] (the "all AEM Agents" line and the "feature parity" line are both the flattering number; the honest reads are 11 prod skills and "some use cases are not covered") · [[Say the Sentence That Obliges — the Hedge Transfers the Ask]] (the announcement ended on a cheer and asked nobody for anything) · [[An Undefined Gate Is a Date Nobody Can Give]] (the panel at "late September, TBC", and ABAC with no gate at all) · [[feedback_critique_check_facts_not_prose]] (four divergences caught against what he told the same audience inside 48h) · [[feedback_pedro_writes_claude_critiques]] (he wrote the doc note; he overrode the rule twice and Claude complied after stating it once).
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
