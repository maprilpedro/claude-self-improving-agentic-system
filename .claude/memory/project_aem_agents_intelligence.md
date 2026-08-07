---
name: aem-agents-intelligence-aai-project-context
description: "Full context on the AEM Agents Intelligence project — agent reporting platform, AO 2.0 liaison, Loni+JM May 11 deck, three-tier reporting, agent ownership, AAI stakeholders. Sister file to project_experience_hub.md."
metadata: 
  node_type: memory
  type: project
  originSessionId: 5f12dcf1-db3b-44ce-bf6c-50e0a17cb9e9
---

> **Two-project split — Phase 2 structurally complete (2026-05-13).** AAI vault folder at `2026/AEM Agents Intelligence/AAI - Project Folder/`. Companion `project_experience_hub.md` covers EH. Meeting Notes moved to neutral `2026/Meeting Notes/` (2026-05-13). AI-Assistant legacy folder retired. No legacy folders remain.

> **📦 Archive discipline (weekly shards; last restructure 2026-07-01).** Old context lives in per-ISO-week shards `project_aem_agents_intelligence_ARCHIVE_<year>-W<wk>.md` (+ long-form reference in `..._ARCHIVE_reference.md`), mapped by `..._ARCHIVE_INDEX.md`. **To find old context: read the INDEX first (dates + topics per shard), then `rtk proxy grep` the shard — never full-Read a shard.** This active file = hot state (currently **the 2026-08-06/07 session**; 07-15 → 07-27 archived to W29/W30 on 08-03, the 08-03 sweep + Agent Owners Alignment to **W32a** on 08-04, the two 08-04 blocks to **W32b** on 08-06, and the **08-04 CLINT + 08-05 ROLLOUT SYNC blocks to W32 on 08-07**) + the compact durable reference below. ⚠️ **The archiver moves dated blocks but does NOT move RESUME pointers — check the pointer still resolves after every run.** **Cap rule, enforced by `scripts/archive_memory.py` (run in `/consolidate` Step 5): keep this file < ~20K tokens / one-shot-readable; event blocks older than ~2 weeks auto-archive to their weekly shard + the index rebuilds.**
>
> ⚠️ **"moving 0 block(s)" HAS TWO CAUSES — DIAGNOSE BEFORE ACTING (2026-08-07).** (1) **The layout invariant below is broken** → the archiver cannot see the blocks. That is a bug, fix it. (2) **Every dated block is newer than `RETENTION_DAYS = 7`** → there is genuinely nothing it may move yet, which is correct behaviour on a dense week. **Check which one you are in before "fixing" anything.** On 2026-08-07 the file sat at **23.5K against a 24K read cap with every block under 7 days old**, so the only lever was **writing the blocks shorter** — the largest was a single 3.4K-token event block, trimmed to 2.2K. 🔑 **On a dense week the cap is a writing constraint, not an archiving one.** ✅ A **SessionStart hook now warns** when any session-start file approaches the cap (`scripts/archive_memory.py --check-startup`, wired in `.claude/settings.json`) — added because both prior truncation incidents were discovered by accident, never by a warning.
>
> 🔴 **LAYOUT INVARIANT, learned the hard way 2026-08-04 — DATED EVENT BLOCKS MUST SIT ABOVE THE LIVING-REFERENCE SECTIONS.** `split_active()` in the archiver treats the first non-blockquoted `## ` heading as the start of the living reference and everything after it as unmovable. This file had drifted so that four dated `> ###` blocks sat *below* `## 2026 Yearly Goal — G1`, so the archiver saw **one** block (the protected RESUME) and reported *"moving 0 block(s)"* while the file sat at **29K tokens, 5K past the read cap** — i.e. **the cap guard reported success while the file was silently truncating at session start, which is the exact 2026-06 awareness-loss failure it was built to prevent.** Fixed by reordering (content-preserving, verified line-multiset-identical), after which the same script moved 29K → 19K on the first try. **When appending a new dated block, put it directly after the RESUME, never at the end of the file.**

> ## ▶️ RESUME HERE — left off **2026-08-07** (the audits went public to the agent owners, two decisions landed, and the announcement bar currently evaluates to **zero**)
>
> **🔴 THE ONE NUMBER FOR MONDAY 08-10: the announcement bar produces 0 skills today, 4 if warnings are tolerated, on the 87 user-visible.** But **13 skills fail only disambiguation**, which is minutes of writing each → **17 announceable with no migration at all.** Full funnel in the **2026-08-06/07 block** directly below. **Two decisions also landed: agent = plugin (PR15), and the checklist is the announcement bar, not a release gate.**
>
> **🟢 THE GA PLAN IS NO LONGER INTERNAL. Pedro presented it to the Coworker team on 2026-08-05 and got no push-back on the dates.** GA **08-24**, bug bash **08-17→08-21**, formal commitment from all AEM teams **Monday 08-10**. Cole Connelly: *"wow, that's sooner than I expected, so that's awesome."* **What came back is a list of things AEM owes, and two of them were not on any AEM plan.** See the **2026-08-05 ROLLOUT SYNC block, archived to shard `..._ARCHIVE_2026-W32.md` on 08-07** (grep `ROLLOUT SYNC` there).
>
> **🔴 THE PANEL-OFF ASSUMPTION IS CONTESTED.** The Road-to-GA canvas assumes AEM ships GA with the Coworker panel switched off. Cole named the hole: a customer holding **both AEP and AEM** would get the panel in AEP and not in AEM. *"It might be possible… but I just don't know if that's a bad product experience."* **It is now an explicit release decision, not an AEM assumption.**
>
> **🔴 TWO COLE ASKS ARE OWED BEFORE GO-LIVE, AND NEITHER IS IN ANY AEM PLAN** — the **AEM instance picker** in the Coworker UI (Workfront hit this and it produced semi-escalations), and **what the suggested prompts become in Coworker**. Pedro answered neither in the room.
>
> **🟢 There are now numbers where there were opinions.** The audit repo `OneAdobe/aem-coworker-audits` ran on 2026-08-05: **27 of 88 AEM skills are in the consolidation target**, **112 of 215 manifests** reach an AEM marketplace, naming is **14 conform / 34 warn / 29 fail** on the user-visible cut, and **13 of the 24 skills carrying a `when-to-use` restate their own description.** ⚠️ **These are the 08-05 figures and the catalogue has since grown to 98 (87 user-visible) — always name the run date and the cut; see the 2026-08-06/07 block.** See the **2026-08-05 AUDIT REPO block**, and [[reference_aem_coworker_audits]] for how to re-run it. 🔑 **Its first external pull arrived the next hour** — Yelena Doliner wants a skills repository reference on her cross-product wiki, and Yanira answered *"Pedro's putting a list of the Git repo."*
>
> **✅ THE GA MODEL IS DECIDED — 2026-08-06, by Pedro: separate the two milestones.** Release is per-plugin and belongs to the teams; the 08-24 announcement is portfolio-level and belongs to him. **Monday's deliverable is two artifacts, not one.** Record: `decisions/2026-08-06-ga-model-separate-release-from-announcement.md`, reasoning in the box below. **What is still open is the vocabulary** — if "GA" keeps naming both states the decision reverts silently, and that is the same `lifecycle` field Clint asked about on 07-29.
>
> **How it got here.** At the **2026-08-03 Agent Owners Alignment** (block archived to shard `..._ARCHIVE_2026-W32a.md` — grep `AGENT OWNERS ALIGNMENT` there) Corey Dulimba, Brian Chaikelson, Guliz Sicotte and Ankur Arora aligned on **"whoever is in the manifest is GA", per agent, now** — against Pedro's composite gate (skills, naming, manifest, UI, provisioning, security, ORR, legal, quality, reporting). Pedro acknowledged and did not decide. He committed to bring a **per-agent GA checklist to Monday 2026-08-10**. That checklist is the **Dimension A table** the V4 status doc has planned since 07-13. **Forcing date: Developers Live, weekly from ~08-24, Corey + Brian's session 09-01, both demoing Coworker only.**
>
> > **✅ DECIDED BY PEDRO, 2026-08-06 — "prends le troisième chemin. Sépare les deux choses qu'on confond."** Full record, alternatives, trade-offs and the scoreable predictions: `decisions/2026-08-06-ga-model-separate-release-from-announcement.md`.
> > **THE DECISION: GA is two milestones, not one.** **Release** is a per-plugin act, a team moving its plugin from the `experimental` marketplace file to the `ga` one — **it belongs to the teams**, it matches the mechanism Carsten and Satya built on 08-04, and Pedro is out of that loop deliberately. **The announcement** is the portfolio event on **08-24** — legal, security, ORR, AI Ethics, docs, PMM — **and it belongs to Pedro.** The composite list was never wrong about content, only about scope: it is the bar for what Adobe says publicly, not a gate on a manifest write.
> > **→ Monday's deliverable is therefore two things, not one:** a **per-agent release state** (teams fill it, Pedro holds the format) and an **announcement bar** (Pedro holds it, portfolio-level, not per agent). 🔴 **Pedro writes both — Claude does not draft them** ([[feedback_pedro_writes_claude_critiques]]).
> > **🔴 THE TRADE-OFF HE ACCEPTED, AND IT IS REAL:** he gives up the per-agent gate, which was the leverage the composite model gave him. **And the whole thing reverts silently if "GA" keeps being used for both states — so naming the two is now load-bearing, and it is the same `lifecycle` field Clint asked about on 07-29 that nobody has answered.** ⚠️ **AI Ethics on EPA does not move** (*"team will evaluate end of Aug"*, after both 08-14 and 08-24); the decision does not solve it, it isolates it to the announcement.
> > **Watch on 08-10:** if the split is right, Corey and Ankur take the release half without argument and the room moves to the announcement bar's contents. **If the room argues about the split itself, the framing is wrong.**
> >
> > **The reasoning that produced it (kept, it is the reusable part).** **The two models demand different artifacts, and that is the real cost of not choosing.** Under the composite gate the checklist is a **gate** — rows are conditions, the output is a date per agent. Under "in the manifest = GA" the checklist is not a gate at all, because each team can already decide; what Pedro would be writing is a **scope disclosure** — what a customer gets and does not get per agent, plus post-GA fast-follows. **Bring the gate-shaped artifact to a room that has moved to the other model and it answers a question they stopped asking.**
> > **The proposed split: the two models are arguing because two different milestones are wearing one word.** *"In the manifest"* is a **release mechanism**, per plugin, owned by the teams — and Carsten and Satya have now built exactly that (one branch, `experimental` and `ga` marketplace json, a plugin in one or the other), so the mechanism exists in code whether or not anyone writes a checklist. The composite list is not a gate on release; it is the bar for the **announcement** — the portfolio-level 08-24 moment with legal, security, docs and PMM attached. **Let teams ship into the `ga` manifest as they are ready; hold the composite list for what Adobe says publicly.**
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
> ### 🔴🔑 2026-08-06/07 — THE AUDITS WENT PUBLIC, TWO DECISIONS LANDED, AND THE ANNOUNCEMENT BAR PRODUCES **ZERO** TODAY
>
> **📤 THREE AUDIT POSTS TO `#aem-agent-owners-alignement`, 2026-08-06** (09:43 the intro naming the three audits + the Playbook and Naming canvases; 11:31 naming; 11:35 target marketplace; 12:34 disambiguation with an explicit **ACTION** line). First time the audit output was published to the owners rather than DM'd. **Ian Reasor picked it up the same evening in `#aem-agent-onboarding`** (*"For skill disambiguation, we're ahead of the pack"*) and **Christian Meyer routed it into EPA's channel** (*"it would make sense to keep an eye on the different reports… we didn't mention this topic in our sync this morning"*).
>
> **✅ DECISION 1, Pedro, 2026-08-06 — the agent axis is rooted on the PLUGIN, not on the skill name's application token.** Shipped as PR15 (`e3d14cc`). The evidence that decided it: the name token covers 67 of 88 and is *inferred*, and it **disagrees with the declared `domain:` on 14 of the 18 skills where both exist** (all 14 declared `domain: assets`, names said edge / cloudmanager / forms / nothing); the plugin covers **88 of 88, declared**, and **no plugin has ever belonged to two agents**. ⚠️ **Keyed on the plugin NAME ALONE** — 61 of 88 skills still have to move marketplace, so keying on `marketplace/plugin` would drop the agent at the moment of the move, which is the same drift that disqualified names. Many plugins to one agent is fine (Onboarding 2, Cloud Manager 5, Content Fragments 13); the arrow never forks the other way. ⏳ **37 of 88 seeded, 51 still unassigned across 7 open decisions** — including **two governance ids** (`experience_governance_agent` vs `governance_agent`, 11 skills pinned to the first) and **Onboarding, which is a real agent with no reporting id**.
>
> **✅ DECISION 2, Pedro, 2026-08-07 — the skills checklist is the ANNOUNCEMENT BAR, not a release gate.** Directly extends `decisions/2026-08-06-ga-model-separate-release-from-announcement.md`. **A red row does not block a team writing into the `ga` manifest**; it bounds what Adobe can say publicly. 🔑 **This is what keeps the 08-06 split intact** — a checklist used as a release precondition would take back with one hand what he gave with the other, and it is the thing the room could fight on 08-10.
>
> **🔴🔑 AND THE BAR PRODUCES ZERO. This is the number for 08-10.** On the **87 user-visible** skills of the 2026-08-06 run:
>
> | Bar | Announceable |
> |---|---|
> | conform on all three (naming · in target · disambiguation) | **0** |
> | conform-or-warn on all three | **4** |
>
> **The funnel, conform-or-warn:** 4 at 3-of-3 · **30 at 2-of-3** · 29 at 1-of-3 · 24 at 0-of-3. **And the 30 split usefully:** 16 pass naming + disambiguation and are **not in the target marketplace** (an engineering move), **13 pass naming + marketplace and fail only disambiguation** (minutes of writing each), 1 needs only a rename. → **🔑 17 skills are announceable for writing effort alone, with no migration.** The bottleneck is disambiguation, 6 conform of 87. ⚠️ The four that pass are **warn everywhere, conform nowhere** — the column says "fails nothing", not "good". And **marketplace has no warn level**, it is in or out.
>
> **⚠️ THE PUBLISHED NUMBERS ALREADY MOVED, SAME DAY.** The 08-06 run was republished after the three Slack posts and the catalogue went **88 → 98 skills**. Naming fails **28 → 37**. Anyone opening his linked report now reads different numbers than his message. 🔑 **Second instance in one day of the trend-integrity trap** (the first: the 37→28 fail drop on 08-06 was entirely `de0819b` "an underscore is a warn", nine Cloud Manager skills, **zero team renames**). **Rule the repo now needs stated out loud: a published delta must be re-derived by re-running today's rules over both dates, and the denominator must be named every time.**
>
> **🔴🔑 COREY ON DISAMBIGUATION — *"yes, this is a new one I haven't heard before"* (2026-08-06 17:46), 48 seconds before *"i'll create a ticket for shift left"*.** ⚠️ **The record says otherwise, and the record is thin in an instructive way.** Pedro asked him **directly on 2026-06-24 16:19** in a group DM with Felix Delval, with the `Skill Overlap Audit (POC)` PDF attached and EPA's own pair cited (`parse-docx-brief` vs `parse-pdf-brief`, 0.44): *"Adopt two fields on your skills: domain (single home) and when-to-use…"*. **Corey never replied. Zero messages in that thread.** Two fair caveats: it is **six weeks, not months**, and the **June ask was two fields, not three** — `when-NOT-to-use` appears later (07-06 `#p42-architecture`, 07-07 Forms). The 07-09 post naming all three *was* in Corey's own channel but sat as a thread reply to Bertrand.
> 🔑 **The mechanism, and it is the second instance in two days.** Same content, three deliveries: a **DM with a PDF** → no reply for six weeks · a **thread reply in his channel** → unseen · a **published report with a number and an ACTION line** → a JIRA in 48 seconds. Pairs exactly with the Clint case (62/63 → Carsten answered in 29 minutes after a week of silence). **The variable is not the sentence alone, it is the sentence plus a countable object plus a venue with an audience.** Logged into [[Say the Sentence That Obliges — the Hedge Transfers the Ask]] as a venue corollary. ⚠️ **Do not litigate this with Corey** ([[feedback_dont_litigate_prior_replies]]) — he has taken the action; the value is the mechanism, not the receipt.
>
> **🟢🔑 AND THE `lifecycle` FIELD JUST BECAME LOAD-BEARING FOR PEDRO'S OWN REPORTING LANE, not only for vocabulary.** **Ramkesh Meena, 2026-08-06 in `#aem-agent-owners-alignement`**, after exploring Rubin for Coworker: chat-level analysis already works for any conversation (`rubin.adobe.io/dashboard/chat-analysis`, skills invoked, responses, flow) and per-IMS-org lookup works too — **but the *CX Enterprise Coworker* tab, the one with customer/IMS-org analytics, interaction counts and WoW growth, *"appears to be available only for GA skills. I wasn't aware of this earlier."*** His conclusion: the only thing missing is an **overall dashboard aggregating across all IMS orgs**. Pedro replied 08-06 09:34 that he has **restarted the dashboard discussion with the Rubin team** and will loop Ramkesh and Ian Reasor in.
> 🔑 **So a skill that is not GA is invisible in the org-level Coworker analytics.** That turns `lifecycle` from a naming argument into a **reporting dependency**: whatever Monday decides about GA vocabulary decides what Pedro can measure and report per customer. **Say that on 08-10 — it is the strongest reason the field has to mean something.** ⚠️ Single source, one person's read of a dashboard, **unverified** — check it against Angela Han / Karthik before quoting. Ties [[H-009]] but is **not** one of its three registered decision signals, so it is recorded here and deliberately not logged as hypothesis evidence (08-03 review restricted that arm).
>
> **🔎 KNOWLEDGE (P6):** [[Say the Sentence That Obliges — the Hedge Transfers the Ask]] (**+1 instance and a new venue corollary**), [[An Undefined Gate Is a Date Nobody Can Give]] (the announcement bar is the gate, and it currently evaluates to zero — writing it is what makes 08-24 answerable), [[A Packaging Unit Is a Customer Taxonomy — Ownership Needs Its Own Record]] (the plugin-vs-name root decision is point 3 resolved with measurement), [[Success Definitions Must Be Agreed Before Metrics Are Scaled]] (88→98 mid-day, denominators must be named). **No new entry — all four are instances.**

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

> ### 🔴🔑 2026-08-06 — THE `lifecycle` GATE IS ALREADY BUILT IN AO, NOBODY HAS SWITCHED IT ON, AND ITS DEFAULT PUNISHES THE TEAMS WHO DECLARED HONESTLY
>
> **Source: direct read of `Adobe-Experience-Platform/aep-ai` at `main`, 2026-08-06.** ⚠️ **Method note worth keeping: a first pass using `gh api` with `xargs -P 10` produced SILENT FALSE NEGATIVES** — it reported zero hits on a file that demonstrably contains the string when fetched alone (secondary rate limiting, no error surfaced). **Redone with a sparse `git clone` plus a positive control** (217 of 217 manifests match a key known to be present). **Rule: any negative result from a parallel API sweep needs a control that must come back positive, or it is not evidence.**
>
> **1. THE MECHANISM EXISTS AND IS WIRED END TO END.** A manifest declares a top-level **`skill_inclusion_policy`**, a list of allowed `metadata.lifecycle` values. A skill whose lifecycle is not in the list is **not surfaced at all**. Field + validator at `services/aep-ai-runtime/src/aep_ai_runtime/agents/config/base.py:122` and `:424`, propagated onto `skills.inclusion_policy` at `:430`, enforced at `services/aep-ai-runtime/src/aep_ai_runtime/skills/discovery.py:141`. A bare string is accepted as shorthand for a one-element list. **Empty list, the default, surfaces everything.**
>
> **2. 🔴 ZERO OF 217 MANIFESTS USE IT** — not `aem-aia`, not `cx-coworker`, across prod/stage/dev. **The switch is built and nobody has flipped it.**
>
> **3. 🔴🔑 THE DEFAULT INVERTS THE INCENTIVE, AND THIS IS THE SENTENCE FOR 08-10.** A skill that declares no lifecycle **defaults to `stable`** (`services/aep-ai-runtime/src/aep_ai_runtime/skills/models.py:69`, *"Skills that omit it default to 'stable' so pre-existing skills are never filtered"*). AEM's **62 of 63 declare `experimental`**, i.e. they told the truth about not being finished. **Switch the gate to `['stable']` and the AEM skills vanish while every team that filled in nothing survives.** The field rewards silence and punishes declaration. **That is the concrete, checkable reason the field cannot be adopted as-is, and it is an object, not an opinion.**
>
> **4. VOCABULARY.** Documented common values are **`stable`, `experimental`, `deprecated`** (`models.py:69`); the config docstring's own examples are `['stable']` and `['stable', 'beta']`. **`ga` is not among them.** Values are free-form so `ga` would function, but reusing `stable` invents no token. ⚠️ `discovery.py` logs a loud warning when a policy excludes *every* skill, precisely because a typo like `stabel` would silently blank a manifest.
>
> **5. ⚠️ AUDIT MISMATCH TO FIX BEFORE QUOTING ANYTHING.** `aemaudit/skills.py:189` defaults an absent `lifecycle` to **`""`**; AO defaults it to **`stable`**. Unreconciled, the audit will report "absent" where the platform behaves "mature", so its numbers will not predict what the gate does.
>
> **6. STATE OF THE AUDIT ITSELF.** `lifecycle` **is already parsed** (`aemaudit/skills.py:63` + `:189`, `metadata.lifecycle` then top-level). **No collector work needed.** But **none of the five audits emit it** — verified against the three catalogue JSONs of the 2026-08-06 run. It is a new report over existing data. ⚠️ **Denominator discipline: the 62/63 is the prod `aem-aia` manifest; the audit's native unit is the 88-skill catalogue across nine marketplaces.** Two populations. Say which one every time, the way the naming audit already does with its 77-of-88 user-visible cut.

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
