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

> ## ▶️ RESUME HERE — left off **2026-08-05** (the weekly Coworker rollout sync HELD — Pedro presented the AEM GA plan to the Coworker team and it landed; earlier the same day, the audit repo was built and published)
>
> **🟢 THE GA PLAN IS NO LONGER INTERNAL. Pedro presented it to the Coworker team on 2026-08-05 and got no push-back on the dates.** GA **08-24**, bug bash **08-17→08-21**, formal commitment from all AEM teams **Monday 08-10**. Cole Connelly: *"wow, that's sooner than I expected, so that's awesome."* **What came back is a list of things AEM owes, and two of them were not on any AEM plan.** See the **2026-08-05 ROLLOUT SYNC block** directly below.
>
> **🔴 THE PANEL-OFF ASSUMPTION IS CONTESTED.** The Road-to-GA canvas assumes AEM ships GA with the Coworker panel switched off. Cole named the hole: a customer holding **both AEP and AEM** would get the panel in AEP and not in AEM. *"It might be possible… but I just don't know if that's a bad product experience."* **It is now an explicit release decision, not an AEM assumption.**
>
> **🔴 TWO COLE ASKS ARE OWED BEFORE GO-LIVE, AND NEITHER IS IN ANY AEM PLAN** — the **AEM instance picker** in the Coworker UI (Workfront hit this and it produced semi-escalations), and **what the suggested prompts become in Coworker**. Pedro answered neither in the room.
>
> **🟢 There are now numbers where there were opinions.** The audit repo `OneAdobe/aem-coworker-audits` ran on 2026-08-05: **27 of 88 AEM skills are in the consolidation target**, **112 of 215 manifests** reach an AEM marketplace, naming is **14 conform / 34 warn / 29 fail** on the user-visible cut, and **13 of the 24 skills carrying a `when-to-use` restate their own description.** See the **2026-08-05 AUDIT REPO block**, and [[reference_aem_coworker_audits]] for how to re-run it. 🔑 **Its first external pull arrived the next hour** — Yelena Doliner wants a skills repository reference on her cross-product wiki, and Yanira answered *"Pedro's putting a list of the Git repo."*
>
> **🔴 THE OPEN DECISION IS THE GA MODEL, AND IT IS PEDRO'S.** At the **2026-08-03 Agent Owners Alignment** (block archived 2026-08-05 to shard `..._ARCHIVE_2026-W32.md` — grep `AGENT OWNERS ALIGNMENT` there) Corey Dulimba, Brian Chaikelson, Guliz Sicotte and Ankur Arora aligned on **"whoever is in the manifest is GA", per agent, now** — against Pedro's composite gate (skills, naming, manifest, UI, provisioning, security, ORR, legal, quality, reporting). Pedro acknowledged and did not decide. He committed to bring a **per-agent GA checklist to Monday 2026-08-10**. That checklist is the **Dimension A table** the V4 status doc has planned since 07-13. **Forcing date: Developers Live, weekly from ~08-24, Corey + Brian's session 09-01, both demoing Coworker only.**
>
> **The live artifact is Pedro's Slack canvas `F0BNF9LDKMW` "AEM Skills Naming Convention — WIP"** — convention, meta fields, one marketplace, plugin naming. Its state and the remaining fix-list are in the **2026-08-04 SKILLS GROOMING block**. ⚠️ **CORRECTED 2026-08-04 by reading Slack: it WAS posted** (08-03 13:42 in the Bertrand thread + 13:50 announced in `#aem-agent-owners-alignement`). The "written and never posted" line was wrong. **A second canvas now exists — `F0BMUV76DHU` "AEM Agents Road to GA", Yanira + Pedro, updated 08-04 15:11 — and it is the Monday deliverable.** See the **2026-08-04 SLACK VERIFICATION block** directly below.
>
> **Clint's thread is no longer silent, and it has a clock.** 2026-08-04 00:42 CEST he posted *"Silence is acceptance? … in accordance with standard Apache voting rules I'll be merging this PR in 72 hours from now"* → **expires 2026-08-07 ~00:42 CEST**. Ian Reasor, Ian Boston and Carsten replied within 20 minutes. See the **2026-08-04 CLINT block** below.
>
> **Pedro was on PTO from the evening of Fri 2026-07-24 to the morning of 08-02/03.** The return-queue state of play is the **2026-08-03 FULL SLACK SWEEP block, archived to shard `..._ARCHIVE_2026-W32.md` on 08-04** (grep `FULL SLACK SWEEP` there) — read it with the PTO caveat at its head, which is the reason nothing in the 07-24→08-03 window is a responsiveness signal. Dated follow-ups are in `watches.md`, which is the single registry.
>
> ⚠️ **"The four things waiting on him" was audited against Slack on 2026-08-04 and three of the four were already wrong.** Only **Clint** is genuinely unanswered. **Tina and Alejandro were answered on 08-03**, **Ramon delivered rather than waited**, and **Hemanta has no DM with Pedro at all**. Corrected state, with what is actually owed, is the **2026-08-04 SLACK VERIFICATION block** directly below. **Lesson, second time in two days: a "waiting on you" list decays within days — verify it in Slack before acting on it** ([[feedback_confirm_ask_before_producing]], and the 08-03 sibling where a Slack deliverable was banked ✅ without reading the thread back).
>
> ⏳ **Open with Gilles Knobloch:** Pedro asked him 08-03 whether the KR 1e video played in full or as the broken 1-second version. Awaiting reply.
>
> **Prior sessions:** 07-27 OKR-review prep → shard **W30**; 07-20/21/22 rollout, marketplace + TBYB blocks → shard **W30**; 07-16/17 Manas → **W29**. Read `..._ARCHIVE_INDEX.md`, then grep the shard.
>
> ### 🔴🔑 2026-08-05 — WEEKLY COWORKER ROLLOUT SYNC (HELD, ~32 min). PEDRO PRESENTED THE AEM GA PLAN TO THE COWORKER TEAM AND IT LANDED. WHAT CAME BACK IS THREE THINGS AEM OWES AND ONE ASSUMPTION THAT DOES NOT HOLD
>
> Room: **Pedro** (`CR BASL 05/LAUENENSEE VC (5)`, Basel), **Yanira Castaneda** (`CR OTT 06/Cavern VC (4)`, Ottawa — she started the transcription), **Namita Krishnan**, **Cole Connelly** (joined ~18 min), **Yelena Doliner**, **🆕 Huong Vu**. **Rachel Hanessian did not join.** Transcript: `AEM Coworker Sync/20260805 - AO to coworker transition and customer rollout .md`. ✅ Good fidelity, two room mics both resolved by content — see [[reference_transcript_glossary]] for how.
>
> **📤 WHAT PEDRO PRESENTED, and it is the canvas `F0BMUV76DHU` said out loud to the platform team for the first time.** Teams have made great progress on skills, *"most of them are ready on the skill side… they are also pushing for having a GA as fast as possible"*. **Formal commitment from all AEM teams across PM and engineering next Monday 08-10** · skills moved to the proper manifest and plugins, with renaming and manifest cleanup · **bug bash across all teams 08-17→08-21**, *"where we will have the UI in Experience Hub and all teams doing their own testing with a full integrated full system as customer would see them"* · docs + GTM + sign-offs in parallel with Yanira and Tina Ngo, *"seems to be no blockers"* · **GA 08-24** · then two cohorts. **The dates match the canvas exactly.** The one carve-out he stated: **the panel use cases will not be presented, because the panel is not ready** — *"for the vast majority of the teams, they can live without."*
>
> **🟢 IT LANDED. Cole Connelly, unprompted: *"Okay, wow, that's sooner than I expected, so that's awesome."*** and at the close *"Awesome to see you guys are so close that we're moving forward."* **Nobody in the room challenged 08-24.** Pedro's own read, twice: *"the team sees so much value with coworker and the skills to the customers that they are okay to develop those cases for now"* and *"teams get excited. They see the true benefits of coworker and they want to push it. So I take that as a positive."* → **The gate got written and the date stopped being a fight.** Cleanest instance yet of [[An Undefined Gate Is a Date Nobody Can Give]], this time on the winning side.
>
> **🔴🔑 1. THE PANEL-OFF ASSUMPTION IS NOT AEM'S TO MAKE.** Pedro, verbatim: *"we were creating the plan based on the assumption that we can turn off the coworker UI panel for our AEM customers until we AEM are ready. So what I understand, it's not possible then."* **Cole's answer is the one to carry:** *"It might be possible. Like we should be able to determine on the app, but I just don't know if it's the right, I don't know if that's a bad product experience for us. So we should just like raise that as like a thing that we're making a decision on for the release too, just so that there's visibility on it."*
> **The concrete failure he named:** a customer holding **both AEP and AEM** gets the panel in AEP, moves to AEM, and it is gone — *"that just creates kind of a disjointed experience a little bit. I know that AEM has its own rail today too, so it's kind of okay."* ⚠️ **That last clause is the whole mitigation, and it expires** — AEM's own rail is exactly what the migration removes. **→ Live instance of [[Two-Frontend Antipattern — Never Run Two Competing UI Surfaces in Parallel]] in its harder form: not two competing surfaces, one surface present in one app and absent in another for the same user.** Pedro's answer in the room was *"let's test it from our side"*. **The decision is now on the release and needs naming, not testing.**
>
> **🔴🔑 2. THE AEM INSTANCE PICKER — COLE ASKED FOR IT BEFORE GO-LIVE AND AEM HAS NO ANSWER.** *"AEM has a bunch of instances… in AI Assistant, there is, I think, an API that was bringing them together and creating a list that would work for AI Assistant. I'm not sure how that operates today in the coworker experience, but we should talk about that because we'll have to surface that on the UI. And we want to make that selection process **ergonomic** because it was really painful in AI assistant."*
> **He has already lived it on Workfront:** *"there's been a big push to make sure that we can find a solution to get their work front instances in… we've had some semi-escalations related to that"*, and the fix there was *"this kind of an unintuitive button in the input box and it'll just get messy if we put like two or three for customers"*. **He asked for AEM's outline *before* go-live so his team can build for it.** Pedro: *"I'll have to make my mind, my head around on that"* and *"this hasn't surfaced [in the AEM bug bashes], but let me let me have another round with the teams."*
> 🔑 **This is the selection layer arriving from the platform side, unclaimed, with a date on it** — [[Selection and Cross-Surface Consistency Are a PM Mandate]]. **The instance picker is EH's front-door problem wearing a Coworker-UI shirt.** Whoever writes the outline sets the pattern for every AEM customer with more than one program.
>
> **🔴 3. SUGGESTED PROMPTS IN COWORKER — the second Cole ask.** *"the prompts that you want to surface when users first come in as suggestions. I think we should talk about what those prompts might look like in the coworker world."* → **This is decision #3 of the 07-03 EH chat-entry note (pause vs keep the Fu Chi prompt feed) arriving from the platform, and it was never reconciled after Josh's side said keep-and-feed-AO2.** Banked EH-side in [[project_experience_hub]].
>
> **🟢🔑 4. THE PANEL TIMELINE, FROM COLE — the first dated statement since Josh went quiet on 07-25 and the 07-31 code-complete passed in silence.** Third round of bug bashes running now with **CJA, AEP, Workfront** (*"I think you guys are on it too"*); *"we're pushing to **stage internally for testing, ideally next week or the end of this week**"*; then another bug-bash round; then push the panel to the **current cohort, which covers RTCDP, AJO and CJA only**. His stated blocker for adding AEM: *"we haven't tested the panel sufficiently within the AEM space… they might have expectations of how it works based on how AI system works today… if we're doing any kind of like custom cards for AEM, we might want to make sure that they show up properly when they're in a more condensed view."*
> ⚠️ **Cole is the route around the Josh silence.** Memory carries him as Prompt Library Platform PM in Sunil Menon's tree; **in this room he is the voice for the panel release and the Coworker UI**, and Josh Hailpern is his EM. **Stop waiting on Josh.** Pedro on his own side: *"I put a end of September there, but eventually we'll get out earlier"* (the canvas says Panel GA 09-21), and *"we just started with Razvan and my team probably will be able to test further tomorrow"* (⚠️ "Razvan" per Otter — plausible, unverified).
>
> **🔴🔑 5. THE GTM MECHANISM, AND IT IS THE 07-15 RACHEL ASK ARRIVING A SECOND TIME WITH A DATE ON IT.** Namita: before flipping a customer, **~one week of heads-up** — Gainsight banners plus emails to admins — *"coworker's coming, it's a bigger, better AI assistant. So just stay tuned for that."* **And the point of it is the exit:** *"we've seen some admins actually responding back to that e-mail saying, oh no, I don't want it. So just giving them a chance to be prepared for this transition and **opt out if needed**."* She framed it as *"based on a learning we had from the previous trial"*.
> **The ask to AEM, verbatim:** *"for AEM customers, what are some surfaces we can use, right? Like admin emails, for sure we should do it, but then **in the surface, in AEM**, like **Shankari used to help us with gainsite**, so how can we do that? How can we do some kind of banners as well?"*
> **🆕 Huong Vu** (GTM comms lead, works with Namita — *"Huong has been leading most of the G[T]M con[versations]"*) split it: **admin emails can go from one central channel** to *"any customer licensing any CXL application"*; **the in-surface banner needs a coordinated AEM effort**, because *"[Gainsight], it seems like we have different mechanism for surfacing in AEP, like CDP, AJO, and then AEM… we'd love the team's help on also surfacing the same copy in AEM as well."*
> → **Second independent ask for AEM's front door in three weeks** (Rachel, 07-15: *"where are all the placements in AEM that we can take over?"*). **EH is the surface with 14K weekly users and this is now on a rollout clock.** Banked EH-side.
>
> **🟢 6. TWO COHORTS, ORDERED BY PAST USAGE — Namita's recommendation and it is a good one.** Batch 1 = **try-before-you-buy** customers, to gather feedback and fix what they report; batch 2 = enable the rest. Her reasoning: *"prioritize customers who have used it a lot, right? Like who've been active users, because then we have higher chances of them using coworker and actually getting us more data, because **when we first did the SKU customers, they didn't even use it and we didn't get a lot of data**."* Pedro agreed and added a second axis: *"we have also a number of, we call them **co-innovation customers**, where they are actively trying coworker, so we'll categorize accordingly"*, and floated splitting TBYB into two or three batches. ⏳ **Ordering the TBYB list by prior AI-Assistant usage is a concrete, unassigned piece of work, and it needs the usage data Pedro's own reporting lane holds.**
>
> **⚠️ 7. THE PROMO $0 SKU IS WRONG IN THE REPORTING, AND THE FIX IS ALREADY RUNNING.** Namita, flagged as *"a really small nuance"* — some customers sat on the **promotional $0 SKU which has since expired but was never returned**, so *"it still shows that they have unlimited credits. And it just for reporting purposes, **it's a little wrong**."* The remediation as customers are rolled in: **the CTT team decommissions the promo SKU** → the customer moves onto the **usage-bound trial with 10,000 credits** → credits reset. Customers may receive a *"my promo SKU has been returned"* notice; **access to Coworker is retained**, nothing about the experience changes.
> 🔑 **Two reasons this is not small.** (a) **It is a data-correctness fact in Pedro's own metrics lane** — any org showing unlimited credits today is mis-stated, and he reports on credit and usage figures ([[Success Definitions Must Be Agreed Before Metrics Are Scaled]]). (b) ⚠️ **It touches [[H-008]]** (razor-and-blades rhetoric as a decline tell): the $0 promo is being wound *down* into a metered 10,000-credit trial, which is movement toward pricing rather than away from it. **Do NOT log it as the second observation** — H-008's discriminant question (is the agent free *because confident paid usage follows*, or *because paid usage is not decoupling*) was still not asked, and an SKU-hygiene cleanup does not answer it. Recorded as adjacent evidence only.
>
> **⏳ 8. YELENA'S WIKI — a filled-in row is owed this week, and Pedro already holds the artifact.** Yelena Doliner maintains a cross-product wiki tracking **Workfront, AEM and Gen Studio assets** onto Coworker — *"one view on one page in case Andrew is asking. Where we are, timelines, and so on."* **Workfront's row is already filled.** Her ask: *"We need to see the list of skills, not like every single skill list, but at least **some kind of a repository that we can refer to**, like your integration testing, like plan what was done and everything."* **Yanira committed for both of them:** *"this is something that we talked about with Pedro, so we'll work on it tomorrow morning. **Pedro's putting a list of the Git repo**"*, then *"sometime this week"*.
> 🔑 **`OneAdobe/aem-coworker-audits`, published the same day, is exactly that repository** — roster, marketplaces, counts, commit-stamped. **First external pull for the audit output, one day after it existed, from outside AEM.** [[Pick Up the Open Action Item]]. ⚠️ **The repo is private and the redaction rules exist for a reason** — decide what leaves it before linking it on a cross-product wiki ([[reference_aem_coworker_audits]], [[feedback_no_internal_to_personal_repos]]).
>
> **RECONCILES.** ✅ **The 07-31 panel code-complete finally has a successor signal** (Cole: stage this week or next) — the 08-04 watch entry said it *"passed with no confirmation and no new date"*, and that is now answered, by Cole and not by Josh. ✅ **The `#aep-coworker-core` blackout is partly bridged** — Namita, Cole, Yelena and Huong were all in this room, so cohort and provisioning state came to Pedro directly; ⏳ **the channel access is still not restored and the fix is unchanged**. ✅ **Cohort 1B's AEM exclusion is superseded** — AEM now has its own two-batch cohort plan off GA 08-24. ⏳ **Rachel still owes the Miro of EH placements** and she was absent again; Namita's banner ask is the same ask from a second person. ⚠️ **Pedro stated GA 08-24 externally while AI Ethics on EPA still reads *"team will evaluate end of Aug"*** — that risk is now outside AEM, not inside it.
>
> **⚠️ UNRESOLVED NAMES from this transcript, do not assert:** *"Paul has a way to get access to all AEM CS customers"* (Namita) — almost certainly **Raul Hudea**, who maintains the P42 org list ([[reference_skyline_p42_orglist]]), but it is an inference; **"Bjoern"** (*"we clarify with Bjoern on the back end manifest"*, Yanira) — unknown; **"Andrew"** (Yelena's escalation audience for the wiki) — unknown; **"Razvan"** in the panel-testing sentence — plausible but unverified.
>
> **🔎 KNOWLEDGE (P6):** 1 new entry — [[Announce a Forced Surface Migration With an Opt-Out — the Refusals Come Back as Replies Instead of Escalations]] (ai-product, 2 obs: Rachel 07-15, Namita 08-05 with the outcome attached). Cited live: [[An Undefined Gate Is a Date Nobody Can Give]] (the written gate is what made 08-24 land unchallenged), [[Two-Frontend Antipattern — Never Run Two Competing UI Surfaces in Parallel]] (the panel present in AEP, absent in AEM), [[Selection and Cross-Surface Consistency Are a PM Mandate]] (the instance picker), [[Success Definitions Must Be Agreed Before Metrics Are Scaled]] (unlimited-credit orgs in the reporting), [[Pick Up the Open Action Item]] (Yelena's wiki row), [[Say the Sentence That Obliges — the Hedge Transfers the Ask]] (⚠️ **watch, do not log yet** — the instance-picker answer is object-backed and available, and *"I'll have to make my head around on that"* is the shape that loses it; the tell will be whether the outline reaches Cole before go-live).

> ### 🔑 2026-08-05 — THE AUDIT REPO EXISTS AND IT PUT NUMBERS ON THE CONSOLIDATION. **27 OF 88 SKILLS ARE IN THE TARGET MARKETPLACE**
>
> **Built `OneAdobe/aem-coworker-audits`** (private, service_id 615301) — five audits over the AEM skill estate, published redacted into git. Design ported from **Gerald Prendi's `governance-agent-marketplace` PR #29**, credited; 🔴 **his repo stays read-only, Pedro's explicit instruction.** Full reference: [[reference_aem_coworker_audits]].
>
> **The numbers, from the 2026-08-05 published run** (commit-stamped, salt fingerprint `dd9d1181`):
>
> | Question | Answer |
> |---|---|
> | Skills in the consolidation target `aem-aia-extensions` | **27 of 88.** The other 61 across 8 marketplaces |
> | Manifests reaching ≥1 AEM marketplace | **112 of 215** |
> | Naming, whole catalogue | 14 conform · 37 warn · 37 fail |
> | Naming, **user-visible cut (the quotable one)** | **14 conform · 34 warn · 29 fail of 77** |
> | `domain` declared | **18 of 88** |
> | `when-to-use` declared | 24 of 88 |
> | `when-NOT-to-use` declared | 18 of 88 |
> | Of the 24 with a `when-to-use`, how many **restate their own description** | **13** (median self-similarity 0.5056, threshold 0.45) |
>
> 🔑 **Coverage is not the number.** More than half the skills that carry a `when-to-use` gain nothing from it. Asking teams for coverage again will not move them — it is a rewrite, not an addition. This is the evidence for the naming-canvas fix-list and for anything said to Clint about cross-skill routing.
>
> 🔴 **"Which application owns this skill" is not answerable from the data.** 21 of 88 names give no application at all, and `domain:` is declared on 18 in **three different formats** (`Assets`, `aem-forms / form authoring (field rules)`, empty). Direct measurement of [[A Packaging Unit Is a Customer Taxonomy — Ownership Needs Its Own Record]] point 3 — the ownership axis stops being derivable and needs its own record. The sixth audit (`skill-in-target-marketplace`, half-built) answers it with a four-tier ladder, and its top rung is a hand-maintained map only Pedro can seed.
>
> **`adaptive-forms-authoring` is duplicated and already diverging** — 0.1.37 in `aem-aia-extensions`, 0.1.41 in `aemforms-aia-extensions`, copied 07-30 and the source never emptied. Two copies, one of them being routed. That is a live bug for whoever calls the skill, not a tidiness problem.
>
> **Method note worth keeping:** a review agent graded the work and was right on a call Claude got wrong — `index` does not belong in the verb vocabulary, because `aem-search-index` reads as *the search index*, a thing, which is the warn the audit exists to raise. Separate-context grading caught what the producing thread could not.
>
> ### 🔴🔑 2026-08-04 — SLACK VERIFICATION OF THE "WAITING ON PEDRO" LIST + THE ROAD-TO-GA CANVAS. THREE OF FOUR WERE STALE, AND THE GA MODEL IS BEING SETTLED IN ARCHITECTURE WHILE PEDRO HOLDS IT
>
> Pedro asked for the Slack state behind the four-people list. Read live 2026-08-04 (threads, DMs, both canvases). **Method note: every item below is from a read, not from memory.**
>
> **✅ CORRECTIONS TO OUR OWN RECORD (4):**
> 1. **The naming canvas `F0BNF9LDKMW` WAS POSTED**, 08-03 13:42 into Bertrand's `#aem-agent-experience-governance` thread (`1785385825.435689`) and announced 08-03 13:50 in `#aem-agent-owners-alignement` (*"All - started to consolidate Skills Naming Convention here. To be reviewed in our Alignment Call this pm."*). Our note said "written and never posted". Wrong.
> 2. **Alejandro was answered 08-03**, 12:40 (the format `aem-[application]-[feature]-[verb/action]` + the link) and 13:42 (the canvas, then *"Please use `aem-brandgovernance` for your skills (seen it proposed by Bertrand)"*).
> 3. **Tina was answered 08-03 15:59–16:24** — a manifest with most AEM skills was shown internally; ETA still blocked on Coworker deliverables, mostly the panel; tracking with Josh; **and *"Coworker UI just announced 2w delay"***. ⚠️ **That is the first dated confirmation of the 07-31 code-complete slip, and it came from Pedro, not from Josh.** She has not replied. **She still has no GA date, which is what she asked for.**
> 4. **Ramon did not wait, he delivered.** 07-30 16:14 he sent a full internal Go-Live announcement draft (target `#one-aem-team-announcements` + manager emails; carries 74% LA remediation vs 28% overall, 914 production programs / 51,101 open third-party vulnerabilities, the Experience League docs link, and a "what's next" list of notifications / proactive monitoring / Log4j-style rapid response). Pedro replied *"Looks goooood"*. **What is owed is Pedro's**, and Ramon asked twice on 07-24 — the **documentation draft** and the **go-to-market / monthly release notes for the Security Health GA** (Pedro: *"That is on my todo P1"*).
> 5. **Hemanta Gupta has no DM with Pedro at all** (channel empty). The Rubin-ingress point is a live question of Pedro's, **not someone waiting on him**. Do not carry it as an unanswered person.
> 6. **Marius delivered the Developers Live thread he owed** — 08-03 17:04 in `#aem-agent-owners-alignement`, with the doc `DevLive_Summer_Series_-_Content_Plan` (`F0BK09AHGQ3`) and a related channel `C0BKA5CD0P6`.
> 7. **Clint is the only one genuinely unanswered.** Thread at 6 replies, **none from Pedro**.
>
> **🔴🔑 THE NAMING ANSWER NOW EXISTS IN TWO PLACES AND THEY DISAGREE.** Public, 08-03 13:42, to Alejandro, in front of Bertrand's thread: **use `aem-brandgovernance`**. Private, 08-04 12:06, DM with Philippe: Philippe argued `aem-brandgovernance` is limiting because permissions and vulnerabilities are coming, proposed **`aem-governance-context / brand / permissions / vulnerabilities`**, and Pedro agreed — *"je crois que c'est Bertrand qui avais propose le aem-brandgovernance, mais comme il n'est pas la et que ta propal me semble bien"*. **The public instruction was never corrected, Alejandro said he would change it, and Bertrand — whose proposal was reversed — was absent from the conversation that reversed it.** Two exposures, a rename executed on the abandoned token, and a manager who learns from the artifact that his own proposal was dropped. **One line in the public thread fixes both.** Instances of [[feedback_proposal_vs_decision]] and [[Say the Sentence That Obliges — the Hedge Transfers the Ask]] (the correction is Pedro's to say, and it is small).
>
> **🔴 COREY PUT HIS ASK IN WRITING AFTER THE MEETING, AND IT IS MORE SPECIFIC THAN THE ROOM WAS** (`#aem-agent-owners-alignement`, 08-03 17:28, ts `1785770924.392919`, **unanswered**). Verbatim asks: what is needed to call a skill GA · is the GA readiness checklist `F0BD4RALNHF` complete · security / ORR / Legal say not blocking, **so is it ok to check that off** · **is langfuse blocking**, and if so are there clear implementation instructions · are there clear instructions for business reporting · **if not, remove them from the GA blockers and give a clear actionable list so we can meet the DevLive goal**. Self-reply 17:31, his own definition: ***"GA in this case means that customers will join the cohort roll out that AEP is doing, so doesn't mean that all customers will have access to co-worker stand alone app."*** → **Monday's deliverable is answering these six, point by point, in his thread.**
>
> **🔴🔑 THE GA MECHANISM WAS SETTLED IN `#p42-architecture` ON 08-04, WITHOUT PM, AND IT IMPLEMENTS THE ROOM'S MODEL RATHER THAN PEDRO'S.** Carsten opened *"Supporting different lifecycles of plugins/skills"* at 08:02 (ts `1785823369.051099`), explicitly *"as briefly touched on in yesterdays call"*, with three options. His recommendation, **two marketplace json from the single monorepo, one GA one experimental** (Coworker lets you point a manifest at a directory), strengthened by his own Coworker PR **`aep-ai#8457`** adding pattern-based plugin inclusion. Satya agreed 13:21; **converged 14:33 — single branch, two manifests (experimental + ga), a plugin is either one or the other**, and a differently-named copy if a plugin ever needs both. → **GA becomes a per-plugin property you change by moving a plugin between two manifests. That IS "in the manifest = GA", per agent.** Same shape as the 07-22 plugin-granularity episode, and this time Pedro is not on PTO. ⚠️ **Do not log as a hedge instance yet — he has had one working day and the thread is still open.**
>
> **📤 THE MONDAY ARTIFACT EXISTS: canvas `F0BMUV76DHU` "AEM Agents Road to GA"**, WIP, **Yanira Castaneda + Pedro**, updated 08-04 15:11, marked *"TO BE REVIEWED with all AEM agent teams"*.
> **Contents.** A `What GA Means` callout — all agents migrated · **one AEM production manifest with all Skills** · **Coworker UI main application only, accessible through Experience Hub, no right panel, no interaction with the left main screen, panel best-effort and potentially after GA** · production-ready quality with per-team bug bash · one end-to-end all-AEM-teams bug bash · **sign-off by all teams across all orgs**. Then a 9-milestone `Road to GA` table with dates: **Skills in Coworker GA 08-10 · Manifest AEM GA 08-10 · end-to-end bug bash 08-17→08-21 · Documentation 08-21 · Sign-Offs (Legal, AI Ethics, ORR, Security, PMM) 08-14 · 🚀 GA + announcements 08-24 · Coworker onboarding TBYB 08-26 · SKU 09-14 (2wk after TBYB) · Coworker UI with Panel GA 09-21.** Then an empty 7-agent × 4-role sign-off matrix (Content Optimization, Discovery, EDA, EPA, Governance, Forms, Onboarding) and an empty `Post GA Fast Follows`.
> **🟢 WHAT IT ACTUALLY FIXES, and Pedro should say it out loud because nobody will notice otherwise:** it **concedes both of Corey's structural objections without naming them** — customer provisioning (TBYB 08-26, SKU 09-14) and the panel (09-21) are now **after** GA (08-24), i.e. no longer gates. And it puts the UI-is-late concession in writing.
> **🔴 WHAT WILL BE ATTACKED MONDAY:** (1) **it is still all-or-nothing** — *"sign-off by all teams across all orgs"* means **the slowest agent sets everyone's date**, so EPA (Corey: ready), Discovery and Content Optimization (Ankur: ready) wait on **Forms and Onboarding**, which are the two weakest rows on the old canvas (Forms = broken CODEOWNER `aem-p42-forms` + version divergence; Onboarding = *"never got past explorers program"*). **Cheapest reconciliation: keep one announcement date, add a per-agent readiness date column, pre-fill EPA + Discovery + Content Optimization from the 08-03 verbal check marks.** (2) **"one production manifest" contradicts Carsten's two-manifest model settled 38 min before the canvas was saved.** (3) **Date ordering breaks** — sign-offs 08-14 precede the bug bash (08-17→21) and the documentation (08-21) they would sign off, and GA 08-24 leaves one working day after the bug bash closes. (4) **The Artefact row is entirely empty and the sign-off matrix is entirely empty** — the exact failure mode that killed Dimension A. (5) **TBYB, SKU and Panel GA carry dates with no Responsible**, and they are the three Pedro cannot see since being removed from `#aep-coworker-core`; last AEM-side statement remains Ian Boston 07-31 *"CoWorker is not enabled for AEM customers yet"*. (6) **Scope grew to 7 agents**, adding Forms and Onboarding, both outside Pedro's reporting 6.
> **🔑 THE SIGN-OFF ANSWER COREY ASKED FOR IS ALREADY ON THE OLD CANVAS, AND ONLY ONE OF THE FIVE IS REALLY OPEN.** `F0BD4RALNHF` records **Legal *"shall not be a blocker"*, Security *"not blocking"*, ORR *"no expected changes to existing ORR/P42 readiness expectations"* (Toby + Ian)** — so three can be checked off with a citation. But **AI Ethics and Accessibility are both "Pending"**, and the AI-Ethics table carries EPA's *"Content Create — work still pending b4 this is ready for a review, team will evaluate end of Aug"*. → **AI Ethics is the one genuine sign-off risk, it lands after the 08-14 sign-off date AND after the 08-24 GA date, and it sits on Corey's own agent.** That is the honest answer to *"is it ok to check that off"*.
> ⚠️ **`F0BD4RALNHF` still reads *"As of 2026-07-03. Target window = end of July"* with a cutover plan dated 07-31** — five weeks stale at the top, on the canvas Corey named by ID. **Three surfaces now answer one question** (`F0BD4RALNHF`, `F0BMUV76DHU`, and Dimension A in the v7 status note) → [[feedback_one_artifact_per_ask]]: say at the top of each what it is now for.
>
> **🔎 KNOWLEDGE (P6):** [[An Undefined Gate Is a Date Nobody Can Give]] (the canvas is the gate finally being written; Corey's six written questions are the same ask a third time), [[Success Definitions Must Be Agreed Before Metrics Are Scaled]] (two live definitions of GA — Pedro's composite vs Corey's "join the AEP cohort rollout"), [[A Packaging Unit Is a Customer Taxonomy — Ownership Needs Its Own Record]] (Carsten's two-manifest lifecycle model makes GA a per-plugin property), [[feedback_proposal_vs_decision]] (the naming reversal is a DM position now contradicting a public instruction), [[feedback_one_artifact_per_ask]], [[feedback_confirm_ask_before_producing]] (the stale waiting-on-you list). **No new entry — the four corrections are hygiene, not a pattern.**

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
