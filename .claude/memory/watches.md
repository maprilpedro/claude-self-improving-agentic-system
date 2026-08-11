---
name: watches
description: Single dated registry of open follow-ups ("surface at session start on X"). Read at every session start and by /reply. The ONE home for dated checks — never buried in event blocks.
metadata:
  type: project
---

# Watches — dated follow-ups (single registry)

> **Rules, and they are load-bearing.** One line per watch: **due date · what to check · where · why it matters**. **No narrative** — context lives in the project memory blocks and in `watches_ARCHIVE_2026-08.md`. `recall` and `/reply` read this file; `/consolidate` maintains it. The archive script never touches it.
>
> **⚠️ Reshaped 2026-08-07 because it had stopped working.** It reached **30.7K tokens against a 25K read cap**, so it was **truncating at session start** — dated follow-ups were silently vanishing, the exact failure it exists to prevent. Measured: it was **not an age problem**. Closed sections were 10% of the weight; the five largest were 38%; the 08-10 GA checklist alone was 4.5K. The cause was drift from the one-line rule above. Full prior content, verbatim and byte-identical, is in **`watches_ARCHIVE_2026-08.md`** — grep it, never full-Read it.
>
> **Keep it this way.** A new watch is a line plus a pointer. If it needs a paragraph, the paragraph belongs in the project memory block that is being written anyway.

## Open

### 🆕🔴 2026-08-11 — MCP IS AN UNDECLARED GA DEPENDENCY, AND "THE OBO DISCUSSION" IS NOT ABOUT OBO

- ✅ **OBO on One AEM MCP is DONE.** `AEMAGT-1361` *"MCP Servers need to switch to OBO"* — **Closed**, Tanju Erinmez, comment 2026-08-06: *"Has been rolled to production and activated."* Christian Meyer handed Pedro the link 08-11 17:00. **Pedro's own hedge that day (*"One AEM MCP might have it implemented yet"*) is settled — it is shipped.**
- 🔴 **But Carsten Ziegeler, 08-11 16:54: *"we are currently untangeling the OBO discussion - which frankly is a pain - it seems it is not really about OBO...stay tuned."*** ⚠️ **Two objects are wearing one name** ([[feedback_dont_conflate_pattern_with_object]]). He did not say what the second one is. **Likely the client-id / service-proxy fight he inherited on 08-10** (`gpt_power_client` allowlisting vs Ian Boston's *"all traffic must go via the service proxy"*, `GRANITE-70593`) — **inference, not confirmed. Ask him rather than assume.**
- 🔴🔑 **THE UNANSWERED ONE, AND IT IS AIMED AT PEDRO.** Christian opened `#aem-agent-experience-production` thread `1786454864.103779` asking whether the **MCP ARB review** (wiki `3908581554`) is a Coworker GA requirement for One AEM MCP. **The process has not started.** Carsten bounced it to Pedro and Yanira (*"Do you know? So far, no such requirement was mentioned to me"*) and **nobody has answered.**
- ⚠️ **Carsten's warning is the sentence to carry into the announcement bar:** *"we have to be careful that we are not running into the same situation as with v1 were new requirements popped up one after the other."* → [[An Undefined Gate Is a Date Nobody Can Give]], now pointed at Pedro's own bar.
- 🔴 **Pedro surfaced a new GA dependency himself, 13 days out:** *"some AEM skills are using MCP for tasks - thus have a dependency on MCP. It's not explicit in the GA."* **It is in no artifact. Decide whether MCP readiness is in the announcement bar or explicitly out of it.**
- 🔑 **Same two names keep appearing on gateway prerequisites AEM has not filled** — Tanju Erinmez + Christian Meyer are the owners on record for the missing AEM **golden eval dataset** (Georgiana Copil, 08-11) *and* the missing AEM **dev-environment config** (08-07), both in `#cx-coworker-gateway-collaboration` `C0ASGEU1BT9`. **Two engineers carrying three product-quality gates, and nobody from the product side is in that channel.** Add it to [[reference_slack_audit_channels]].

### 🔴 TUE 2026-08-11 — AEM SITES TRIAL IS BEING PROPOSED BACK IN, AND COREY PULLED IT OUT FIVE DAYS AGO

- Pedro opened panel-in-prod testing 08-11 09:51 in `#aem-agent-owners-alignement` (thread `1786434688.973389`). **Apoorva + Ankur proposed `AEM Showcase` + `AEM Sites Trial`; Apoorva then asked Pedro at 10:55 whether that is risky *"as they used by SC team and customers"* — unanswered.**
- 🔑 **THE RECEIPT: `05791F3F677F1AE80A495CB0@AdobeOrg` (AEM Sites Trial) was REMOVED from the Coworker-enabled feature flag on 2026-08-06 20:36** by Stephen Gould at Corey Dulimba's request. Group DM `C0BNEQALB45` (Corey, Namita, Cole, Stephen, **Pedro is in it**). Reason: enabling an org brings the **Gainsight banner** (Namita confirmed *"ya"*), and Corey: *"its a internal Org but we also use it for some external work as well"*. His exact want, per Stephen 19:18 — *"available if you have the link, but not show up in all the navigation and promotion"*. Wiki `3973983995` Unified Shell x Coworker enablement.
- ⚠️ **Check whether Rodson's panel-in-prod flag is the same switch as the Coworker-enabled flag** ([[reference_coworker_enablement]] — activation ≠ migration, two Unified Shell flags). The reason Corey gave applies either way.
- ⏳ **Marius Duta 11:34, separate thread:** Sites Trial is not relevant for EDA, they bug-bash on Showcase which has the environments and pipelines. → **Sites Trial carries exposure and little test value. Showcase is defensible if someone warns SC enablement, and nobody has been named for that.**
- 🔑 Philippe and Arneh both posted purely internal orgs (Foundation Internal, AEM Sec Alpha, Forms Internal01, Forms PM). **Two teams already did what Apoorva is proposing as the alternative.**
- ✅ **ANSWERED 08-11 11:41** — Pedro posted the Sites Trial precedent in the thread, object-backed (org ID, date, Corey's name, the Gainsight reason), ending *"correct me if that changed since"*. **He deliberately left AEM Showcase alone**, so by omission it is approved.
- ⏳ **TWO REPLIES NOW GATE THE SAME THING, both sent 08-11.** (1) **Rodson Clavel**, in his own thread `C0BCKG35NFP` ts `1786405114.307519` — is the panel prod flag the same switch as the Coworker-enabled flag? **If it is, the Gainsight banner follows onto AEM Showcase, which is the SC live-demo org — the same problem one org over.** (2) **Corey**, on whether the 08-06 removal still stands. **Until one of them lands, Assets and Sites should hold off on posting Showcase.** 🔴 Nobody is still named for the SC-enablement heads-up.

### 🔴 2026-08-07 → 08-24 — BERTRAND IS ON PTO FOR THE RUN-UP, BACK ON GA DAY

- ✅ **CORRECTED 2026-08-10 from his Slack status — he returns 08-24, the GA day itself.** The prior "returns AFTER 08-24 / misses the GA" line was wrong. He misses **08-10, the 08-14 sign-offs and the 08-17→21 bug bash**, then lands the day of the GA and the announcement **with zero runway**.
- ✅ **SENT 2026-08-10 13:37 CEST** (DM `DQ6H0AV7H`, ts `1786361855.054289`), with the 08-10 audit catalogue linked as the readiness receipt.
- **⏳ WEEKLY UPDATES PROMISED IN THAT DM — due 08-14 and 08-21.** 🔑 **The 08-21 one is the pre-read: it is the last thing he sees before landing on GA day.** Format is already dictated by Bertrand's own 07-21 review ([[feedback_bertrand_status_comms]]) — concrete win first, no table detail, plain mechanisms, what is moving not "TBD".
- ✅ **THE PREMISE SOFTENED 2026-08-10/11 — HE IS ANSWERING FROM PTO AND FAST.** Replies at 22:15, 22:43 and 08:43. The "uncovered run-up" framing below still holds for the 08-17→21 bug bash, **but he is reachable right now and that window can close at any moment.** Use it.
- ✅ **CLOSED 2026-08-10 22:15 — THE LONI QUESTION IS ANSWERED BY BERTRAND HIMSELF.** *"et donc oui, c'est mieux et important de tenir Loni au courant (cc: me)"*. He said **cc me**, not route through PMM. ⏳ Note drafted 08-11, **goes out Wed 08-12 morning**; Bertrand asked to review first (*"Oui je veux bien relire avant"*, 22:43). ⚠️ **The draft claims *"Bertrand has reviewed this"* — false until he actually replies. Check before send.** Jaclyn stays the interim reporting line, never the escalation path.
- 🔴 **DATE DRIFT IS THE REAL EXPOSURE NOW.** In 24h Bertrand got **four** answers on GA scope, **three** panel dates (09-11 · 09-21 · *"milieu-fin novembre"*), **two** bug-bash dates (17-21 vs 19) and **two** activation dates (25 vs 26). ✅ Panel settled at **09-21 TBC** (Pedro corrected Slack + the note, 08-11); the November figure is withdrawn. **He is cc'd on the Loni note — every remaining divergence is visible to him.**
- **🔴🔑 AND THE LONI PATH GOT ROUTED THROUGH PMM THE SAME EVENING.** Tina Ngo, 08-10 18:27, group DM `C0B20PQDEG0`: *"before you let loni know, can you tell me first? think we should communicate a joint plan PM/PMM"*. Pedro agreed at 18:32, *"let me draft as joint plan and it to you first"*. **Reasonable ask, and not hostile — but on the day he was weighing going direct, he became co-author instead of sender.** ⏳ **Watch whether the joint plan actually reaches Loni, and whose name is on it** ([[feedback_position_over_merit]]). ✅ **HANDLED 2026-08-11 BY SPLITTING THE ARTIFACT, NOT MERGING IT.** A status to a VP has one author; a GTM plan has two. Pedro sent Tina a **one-sentence PMM placeholder to replace by EOB 08-11**, with the note going Wed morning either way — she is named and credited, he stays the sender, and the message is not hostage to her calendar. 🔑 **The reusable move: give the peer a bounded block with a deadline, not a review right over the whole document.** ⏳ Still watch whether she replaces it in time and whether the joint GTM plan ever lands.
- **Two slots left blank on purpose, only Pedro can fill them:** what he does if the **AI Ethics sign-off on EPA** is not there by 08-21, and **who covers escalation 08-10 → 08-21**.
- 🔑 **The gap is narrower than first framed but sharper — the run-up is uncovered and he lands cold on announcement day.** The ask is a named cover for those two weeks plus a pre-read before the 24th. Nobody is named today. ⚠️ **Ian Boston is away too** (08-06, *"if you want to revert that while I am away, please feel free to take the approval over"*).
- **⏳ Owed on his return** — two lines with what actually happened, the day he is back. The landing note is what makes the heads-up worth having sent.

### 🔴🔑 WED 2026-08-12 — THE MANIFEST DECISION (out of the 08-10 owners call, which HAPPENED — full read: [[project_aem_agents_intelligence]] 08-10 block)

- **Pedro posted the fork 08-10 20:12 in `#aem-agent-owners-alignement` with `cx-coworker` as the named default and a WED 08-12 deadline**, so teams can still PR their manifests. Alternative was a throwaway `aem-bugbash-cx-coworker`.
- **🔑 The object that decides it:** `cx-coworker.yaml` holds **1 AEM plugin of the 18 in `aem-aia`**, and `aem-aia.yaml` explicitly `disabled_plugins` cja / dx-api / experimentation / predictive-ai. **GA on `aem-aia` = an AEM-only assistant, not Coworker.** ⚠️ Read from a clone at `f648493` (08-06) — **re-verify on `main` before quoting**.
- **⏳ Two preconditions nobody has costed:** `required_entitlements` per plugin (Gerald, mandatory, `aep-ai#7241`/`#7225`, only Governance has done it) and `plugin_deduplication_strategy: overwrite` with AEM's marketplace 10th of 13, so a name collision loses silently.
- **🔴 Ask the Coworker team who is CODEOWNER of `cx-coworker.yaml` and on what conditions.** That answer is what makes this three days or three weeks. Not verifiable from Pedro's clone (sparse, no `.github`).
- **⏳ Carsten's PR `aep-ai#8457`** (pattern-based plugin inclusion) would replace 18 entries with one pattern. Check where it stands before enumerating.

### 🔴 THE AUDIT HAS NEVER MEASURED THE DESTINATION (opened 2026-08-10)

- `aem-audits.yaml` lists **10 marketplaces, all AEM**. `cx-coworker` registers **13**; only `governance-agent-marketplace` overlaps → **12 invisible**. **Every disambiguation number is AEM-against-AEM.**
- **Two changes to commission, by PR** ([[feedback_audit_repo_works_by_pr]]): add the 12 as `role: peer`; emit `required_entitlements`. ⚠️ **Say up front that it moves every denominator.** Christian Meyer asked for exactly this on 08-10 and wants a plan after 08-24.

### 🆕🔴 ON-CALL IS A GA GATE NOBODY HAD (2026-08-10, group DM `C0BPMVDECSU`)

- Agents were never onboarded to `#skyline-oncall`; runbooks are written for **a2a**, not the skills model. **Carsten: *"the incident will first land with coworker and then it might be unclear which teams is responsible for a skill."*** Yanira drives, starting with the EPA runbook; Carsten covers for Ian (PTO); **Toby Such, who framed it as the pending ORR work, is out all month.**
- 🔑 **Pedro's move: the audit can emit the skill→team column from CODEOWNERS.** Offer it before seven teams build it by hand. This is the consumer the parked "repoint the ownership axis onto CODEOWNERS" item never had. ⚠️ **Different column from the agent map** (plugin→AOv1 agent); do not merge them.

### 🔴 TUE 2026-08-11 — THE COHORT ANSWER, AND TWO PEOPLE ARE WAITING ON IT

- **Brian Chaikelson** (*"Is this just the pods? When would the next group be?"*) — ⏰ **he records his Developers Live segment WEDNESDAY, before his PTO.** **Silvia Mulet Ferre**, same question in her words on 08-10 20:19. Neither answered.
- **EDA may slip a week.** Pedro's two options on the table with Brian: announce all agents with no special mention, or tell the few onboarded customers *"EDA not present yet"*. Undecided.
- **⏰ Also due Tue AM UK:** the AEM Agents Reporting Status **ahead of Jean-Michel's staff call**, bot reminder cc Jaclyn. Pedro has just told Bertrand he reports via Jaclyn, so this is the surface that carries it.
- **⏳ Answer Corey's 08-10 16:52 bar question precisely** — warnings vs failures, and hidden vs customer-facing skills. **That is the 0-vs-4 and the 87-vs-98.**

### 📕 CLOSED 2026-08-10 — the pre-call state of the owners call (kept for the reasoning, not for action)

- **📍 The artifacts: canvas `F0BMUV76DHU` "AEM Agents Road to GA"** (Yanira + Pedro) is the Monday deliverable — dates skills+manifest GA 08-10 · sign-offs 08-14 · bug bash 08-17→08-21 · docs 08-21 · **GA + announcements 08-24** · TBYB 08-26 · SKU 09-14 · Panel GA 09-21. 🟢 It quietly concedes both of Corey's objections (provisioning and panel now *after* GA) — **say that out loud, nobody will notice otherwise.** 🔴 Fix before posting: still **all-or-nothing** (*"sign-off by all teams across all orgs"* → Forms and Onboarding set EPA's date), **sign-offs precede the bug bash they sign off**, the Artefact row and sign-off matrix are **empty**, and TBYB/SKU/Panel carry dates with **no owner**. ⚠️ The older canvas **`F0BD4RALNHF`** still reads *"As of 2026-07-03. Target window = end of July"* — five weeks stale, and Corey named it by ID. **Three surfaces now answer one question** (`F0BD4RALNHF`, `F0BMUV76DHU`, Dimension A in the v7 status note) → **say at the top of each what it is now for** ([[feedback_one_artifact_per_ask]]).
- **The GA checklist is due, and Pedro committed to it out loud on 08-03** (*"I'll work on that, and we can discuss next week"*). ⚠️ **The table exists and is missing the columns being asked for** — `## Dimension A` in `AAI - Project Folder/AEM Agents on Coworker — Status.md` (v7), seven rows filled, **no readiness date and no gate column** because Bertrand's 07-21 review trimmed it to bug-bash status. **Monday is the missing columns, not a new artifact.** ✅ **Model decided 08-06: two milestones.** Release = a team moves its plugin `experimental` → `ga`, per plugin, teams own it. Announcement = the 08-24 portfolio event, Pedro owns it. → **Monday is TWO artifacts, not one.** Record: `decisions/2026-08-06-ga-model-separate-release-from-announcement.md`. ✅ **Decided 08-07: the checklist is the announcement bar, not a release gate** — a red row does not block a `ga` manifest write. **Say that out loud; it is what keeps the split intact and it is what the room could fight on.**
- **🔴 The number to walk in with: the bar evaluates to ZERO.** On 87 user-visible skills (08-06 run) — conform on all three audits = **0**; conform-or-warn = **4**, warn everywhere. Funnel **4 / 30 / 29 / 24**. 🔑 **13 fail only disambiguation → 17 announceable for writing effort, no migration**; 16 fail only the marketplace move. **Three exits: lower the bar, announce a named subset, or move the date.**
- **🔴 The live risk is vocabulary, not the model.** If "GA" keeps naming both states the decision reverts silently. 🟢 Already on the agenda in public (Pedro in Clint's thread 08-05, cc Ian Boston + Carsten); **Carsten agreed in 29 min** but said *"not blocking GA"* — ⚠️ **that phrase reads two ways and the second is the reversion. Pin that `lifecycle` IS what release means.**
- **🔑 The object-backed sentence for the room** (verified in AO code 08-06): `skill_inclusion_policy` exists and is wired end to end, **zero of 217 manifests use it**, and a skill declaring nothing **defaults to `stable`** — so a `['stable']` gate **deletes AEM's 62-of-63 `experimental` skills while every team that filled in nothing survives.** The field rewards silence and punishes honest declaration. Detail: [[project_aem_agents_intelligence]] 08-06 lifecycle block.
- **🟢 The argument that makes `lifecycle` unarguable** (Ramkesh Meena, 08-06): Rubin's *CX Enterprise Coworker* tab *"appears to be available only for GA skills"* → a non-GA skill is **invisible in per-customer reporting**. ⚠️ **Unverified, one person's dashboard read. Angela Han and Karthik were in the room on 08-06 and it was not asked** — see the Rubin section.
- **🔴 Seven agent-map decisions only Pedro can take. 51 of 88 skills have no agent, so no agent-cut number is publishable.** Two governance ids (`experience_governance_agent` vs `governance_agent`, 11 skills pinned to the first) · Cloud Manager 14 across 5 plugins · Content Fragments 13 · `aem-codeveloper-plugin` 6 (EDA or Modernization, which has no reporting id) · Onboarding 12 (real agent, **no reporting id exists, mint one**) · 5 leftovers · ⚠️ `.claude` is not a plugin (`aem-clean-users` counts wrongly).
- **⚠️ Restate the denominator first.** The three 08-06 Slack posts link reports that were republished the same day: catalogue **88 → 98**, naming fails **28 → 37**. Anyone opening them reads different numbers than the messages say.
- **⚠️ What the decision does NOT solve:** AI Ethics on EPA still reads *"team will evaluate end of Aug"*, after both 08-14 and 08-24, on Corey's own agent. Isolated to the announcement now, not fixed.
- **🔎 The test, so it can be scored:** if the split is right, **Corey and Ankur take the release half without argument** and the room moves to the bar's contents. **If the room argues about the split itself, the framing is wrong.** Two rows already filled verbally and unbanked — Corey/EPA, Ankur/Discovery + Content Optimization.
- ⚠️ **Second time Corey has asked in the same words** (07-09: *"How can we provide a date when we're going to be ready if we don't know what we need to do to be ready?"*). [[An Undefined Gate Is a Date Nobody Can Give]], Pedro owing the gate.

### 🔴🔑 WEEK OF 2026-08-10 — RUBIN ([[project_aem_agents_intelligence]] 2026-08-06 RUBIN SYNC block)

- **✅ AXIS SETTLED 2026-08-07 — publish on the skill NAME with the error rate footnoted.** PR15's plugin rooting stays the record of record; the name is what ships. **The footnote is not optional, it is what makes it defensible.** Measured on the 08-07 run, **98 rows / 85 distinct skills**, the name gives a clean application segment on **51 of 98**; 18 loose tokens, 14 from declared `domain:`, 4 from plugin, **11 unresolved**. Live artifact = canvas **`F0BN06V01GF`**. ⏳ Still worth asking Rubin to log `plugin` — it retires the footnote.
- **⏳ Canvas `F0BN06V01GF` fix-list** (Pedro filled it 08-07): the **`Confirmed` column has no owner named on any row** — putting a name per row is what could close five of the seven agent-map decisions in one meeting; the **error-rate note is not on the canvas**; the Rationale states the future as present (*"all skills shall have a dedicated application token"*, today 51 of 98); `aem-cloudmanager` = EDA is now unhedged though two of its fifteen read as Modernization, which has no reporting id; two typos in the opening two lines.
- **⏳ Early access to the Report Builder was promised for this week.** Chase it. 🔴 Pedro's own words: *"if we miss that milestone, then I will have nothing for the GA."*
- **⏳ The skill-grouping map is Pedro's to send**; Rubin is waiting on it. ⚠️ Same object as the seven agent-map decisions — cannot go complete before 08-10.
- **🔴 Ask the two questions that were missed** while Angela Han and Karthik sat in the room 22 minutes: (1) Ramkesh's GA-skills-only claim, **needed for 08-10**; (2) Hemanta Gupta's no-ingress finding. ⚠️ Angela's side-load answer is adjacent and cuts mildly against Hemanta — she objected to the **cadence** (*"are you going to side load them every week?"*), not the capability. **Not an answer, do not bank it as one.**
- **🔴 SKU vs TBYB still cannot be split**, and it blocks Namita's cohort ordering. Yanira named the older blocker (**Andre, DAS team: no quick indicator**) and is surfacing it on Slack. Angela's bar: a **root provisioning API**, not a weekly spreadsheet. Interim: two digests, one filtered to each org list.
- **🔑 Free distribution win:** Report Builder reports carry a subscriber list and others can clone them. **Three Workday reviewers asked for more broadcast** (Felix Delval, Yanira, Razvan). Cheapest promotion-case move available.

### 🔴 ~2026-08-17 — THE EH PLACEMENT ANSWER NOW HAS A DEADLINE

- GA 08-24 with a **one-week pre-flip customer announcement** means the answer on which EH surfaces carry the banners plus the Gainsight notification is owed around **08-17**. **Cole Connelly delivered the banner Figma on 08-07** (pre-rollout and post-rollout); Pedro routed it to Eugene and Sorin *"when you guys are back"*, and both were away.
- Huong Vu's split still stands: **admin emails go from one central channel**, the **in-product banner needs coordinated AEM work**. Copy exists, with two variants for prior-AIA versus newly-onboarded TBYB.
- ⚠️ **Fourth consecutive staleness flag raised on the EH Status & Todo `Current Status` on 2026-08-11** — 11½ weeks behind, flagged not rewritten. It is Pedro's to refresh.

### 🔵 TUE 2026-08-11 — RE-RUN THE AUDIT (a baseline is not progress)

- Teams are renaming and filling `domain` / `when-to-use` **now**; GA is 08-10 and the bug bash 08-17→08-21, so the delta lands either side of 08-10. A September run captures a finished state with no curve.
- **🔑 Re-derive the delta by running today's rules over both dates**, never by diffing two stored `docs/STATUS.md`. Split movement into *fixed in place* / *arrived conforming* / *removed* / *renamed as proposed* — the denominator moves on its own. (Precedent: the 37→28 "improvement" was entirely a grading change, **zero renames**.)
- ⚠️ **Salt fingerprint must match `dd9d1181`** or pseudonyms cannot be compared with the 08-05 run. Salt lives only in Pedro's macOS keychain.
- Backfill is safe: all nine repos have commits at 2026-07-01, every collector accepts a `ref`.

### 🔴 THIS WEEK — WHAT THE 08-05 ROLLOUT SYNC PUT ON PEDRO

> The GA plan is external now. Pedro stated GA 08-24 / bug bash 08-17→08-21 / commitment 08-10 to the Coworker team and **nobody challenged the dates** (Cole: *"wow, that's sooner than I expected"*). Everything here is what the room handed back. Full read: `..._ARCHIVE_2026-W32.md`, grep `ROLLOUT SYNC`.

- **🔴 Name the panel-off decision instead of testing it.** Cole: *"we should just raise that as a thing that we're making a decision on for the release."* The failure case: a customer holding **both AEP and AEM** gets the panel in AEP, not in AEM. ⚠️ His mitigation (*"AEM has its own rail today too"*) is exactly what the migration removes.
- **🔴 Give Cole the AEM instance-picker outline before go-live** — *"really painful in AI assistant"*, Workfront produced semi-escalations. **It has not surfaced in any AEM bug bash.**
- **🔴 Suggested prompts in Coworker** — Cole's second ask, and it is decision #3 of the 07-03 EH chat-entry note, unreconciled since Josh's side said keep-and-feed-AO2 on 07-08. Route: Fu Chi (pipeline) + Zeus Courtois (AO2 recommendations). EH-side.
- **⏳ Yelena Doliner's cross-product wiki row is owed THIS WEEK** and Yanira committed for both (*"Pedro's putting a list of the Git repo"*). Workfront's row is filled. 🔑 `OneAdobe/aem-coworker-audits` is that repository — ⚠️ **private and redacted; decide what leaves it before linking it** ([[reference_aem_coworker_audits]]).
- **⏳ Order the TBYB cohort by prior usage** (Namita). Unassigned, and it needs the usage data Pedro's reporting lane holds — which is blocked on the SKU/TBYB split above.
- **⚠️ Before quoting any credit or usage figure:** expired promo $0 SKUs were never returned, so those orgs still show unlimited credits (Namita: *"for reporting purposes, it's a little wrong"*). ⚠️ Adjacent to [[H-008]] but **not** its second observation — the discriminant question still has not been asked.
- **🔴 Answer Namita + Huong Vu on AEM surfaces for the pre-flip announcement** (banners + admin emails, ~1 week before each cohort flip). **Second independent ask for AEM's front door in three weeks.** EH-side. 🔑 **PROMOTED 2026-08-10 — this is no longer only an EH item.** Pedro's own definition of GA that day includes *"il faudra des annonces clients avant quand même"*, and this is the machinery those announcements run on. **A GA on 08-24 with a one-week pre-flip notice means the placement answer is owed around 08-17, and nobody has written it.**

### 🔴 2026-08-04 → open — THE CHEAP UNBLOCKS

- **`#aep-coworker-core`: Pedro was removed 07-28 19:41**, the same evening Yelena moved the substantive traffic there from the now-dead `#aia_coworker_convergence`. ⚠️ Fact, not motive. **He owns the AEM migration status and cannot see the channel carrying it. Ask to be re-added, or go direct to Yelena / Namita.**
- **🔑 Cole Connelly is the route around the Josh silence** — Josh Hailpern is his EM, and Cole is the voice for the panel release. Stop waiting on Josh.
- **⏳ Gael Mouello, 07-29**, asked whether AJO's 4 panel invocation points auto-invoke or need integration work. Unanswered, and **it is Eugene's EH question in AJO clothing.**
- **⏳ One public line closes the naming reversal — post it in `#aem-agent-experience-governance`** (Bertrand's thread, still the channel's last message). Pedro told Alejandro publicly to use `aem-brandgovernance` (08-03 13:42), then agreed with Philippe in DM (08-04) to move to `aem-governance-context / brand / permissions / vulnerabilities`. **Alejandro is renaming against the abandoned token, and Bertrand, whose proposal was reversed, was not in the conversation that reversed it.** Cheapest item on the board.
- **🆕 64-character limit on skill names** (Carsten, 08-05). **Not in canvas `F0BNF9LDKMW`.** Add it and validate every proposed rename against it. 🔑 The audit can check it mechanically — it already parses every name.
- **⏳ Canvas `F0BNF9LDKMW` fix-list** (detail: archive, grep `SKILLS-NAMING CANVAS`): the audit figure + report link; the invented examples `form-edit` / `forms-plan-ntb`; "One Marketplace" → **monorepo 1A, decided by Ian Boston 07-28**; `lifecycle` + entitlements; a rename date; owner + date on the Tina note; `"first skills token"` is the **second** segment; both table separator rows sit in position 2. **🔴 It currently ships with no rationale** — the Why block was deleted after its arguments were found inverted. **Someone will supply reasoning if Pedro does not.**
- **⏳ Two audit config changes not yet commissioned:** add `governance-agent-marketplace` (without it the audit is blind to the skills Bertrand flagged) plus onboarding / content-fragments / guides; and decide whether to repoint the ownership axis onto CODEOWNERS.

### 🔴 STILL OWED — THE MARKETPLACE POSITION (corrected 2026-08-03)

> ⚠️ The 07-24 "✅ done and posted" entry was **false** — verified three ways, Pedro posted nothing in `#p42-architecture` after 07-22. **Read with the PTO in front of it: 07-24 was his last working day. n=1, do not stack it into a pattern.** Full forensics: archive, grep `MARKETPLACE AUDIT WAS NEVER POSTED`.

- **Still owed:** the extended audit (5 missing marketplaces into `scripts/fetch_skills.py`) and the **written plugin-boundary position**. Scope: Felix's overlap-process question + his *"should we run Coworker evals"* as the eval gate; Bertrand's 07-16 cross-AEM example; cite Meschberger wiki `3955827624`; decline the repo/admin half.
- **🟢 The re-entry is open and clean.** Satya's wiki `3983883638` explicitly asks for inputs, and **the customer-facing half is still undecided** — Carsten's 07-20 framing (plugins selectable against what the customer purchased) never resolved, and **Corey's *"do we have a decision and go forward plan?"* is unanswered.** Raul proposed renaming the repo `aem-plugins-marketplace` (Carsten: *"eventually yes"*) — Pedro's naming lane. **Enter on the customer-facing boundary, not the repo choice — that one is settled and was never his.**
- ⚠️ Pedro's 07-22 hedge (*"if it causes no technical issues or limitations, agreed"*) stays posted. **Forward-framed only, do NOT walk it back** ([[feedback_dont_litigate_prior_replies]]).

### 🔴 2026-08-03 — MANIFEST CONTENT HAS NO OWNER (Tanju's 07-29 thread, `#aem-mcp-engineering` `C0BAEF9DXT3` ts `1785338723.736529` + `AEMAGT-2435`)

- **The concrete instance of Bertrand's unanswered 07-29 question** (*"Who owns 'fixing' this and making sure we (AEM) are also represented properly in the other official manifests?"*). Tanju: *"There seems to have been a **mishap**… the Brand Governance MCP Server was removed."* An entry vanished, nobody noticed, **a PM found it by testing. Pedro's lane; the incident is the evidence.**
- **`AEMAGT-2435`** — Major, In Progress, Jabran Asghar, **untouched since 07-30**. Real bug = **transitive discovery**: Coworker does not reach Brand Governance via One AEM MCP, **while Claude and ChatGPT do**. ⚠️ Contradicts what Ramon told Bertrand 07-30. Watch for movement.
- **⚠️ The "any delete hits everyone" claim is a relayed distortion — do not repeat it.** Gerald actually wrote: *"a delete or an addition of an **MCP server**, even manual, is **per ORG**… **This would need to be confirmed.**"* Three deltas from Philippe's version: MCP server ≠ plugin, per-ORG ≠ global, and Gerald flagged it unconfirmed.
- **⏳ One question to Philippe first:** Gerald says the governance MCP **was added back** 07-29 and the config **is present** in `cx-coworker`; Philippe says 08-03 it is still broken. **Either the restore did not hold, or he is describing the 07-29 state.** Only he is looking at the screen.

### 🔴 ~2026-08-24 → 2026-09-01 — DEVELOPERS LIVE IS THE FORCING DATE

- Weekly public webinars from ~08-24; **Corey + Brian's session 2026-09-01**. Both will demo **Coworker only, no AI Assistant**.
- Tina Ngo: *"this is the first time when we will be publicly talking about our skills in a public forum… I kind of see this as a GA moment."*
- ⚠️ In-room dates are approximate. **Marius Duta owns the Slack thread** to pin date, milestones, link and agenda (posted 08-03, doc `F0BK09AHGQ3`, channel `C0BKA5CD0P6`) — re-date from it.
- ⏳ **Tina owes the Coworker-side documentation link**, structured **by use case, not by skill**. Corey named documentation as an unlisted GA gate. **She still has no GA date, which is what she asked for.**

### 🔵 BEFORE QUOTING ANY MCP NUMBER

- **Eli Lilly is in the management dashboard but absent from the per-customer deep-dive** (Brian Chaikelson, 07-31, unanswered). ⚠️ **Eli Lilly is in the OKR-review speaking notes.**
- **Jabran, 07-24: 30-day window only** — *"a bug in some panels not respecting the time filter"*. No fix confirmation since.
- **🔴 The "Tool Calls" lock is slipping.** Tanju's report now says **"operation"**; Christian Meyer challenged it 07-28, undecided. **Pedro owns this term** ([[reference_mcp_terminology]]).
- Unresolvable IMS orgs (`127B272369BC84400A495C0A@AdobeOrg`, 19,922 requests) — Jabran suspects AEM trial envs.

### ⏳ CLINT'S THREAD — the residuals after the 08-05 answer closed the clock

- **Clint's question 2, admin-only scope.** Ian Boston routed the source-of-truth question to `#coworker-eng-collaboration` / `#aem-agents-aep-collaboration` and **nobody has asked there.** Entitlements are org-level, so 2A does not reach it.
- **`PLAT-290634` is the real fix and it is dead** — created 2026-06-16, New, Unassigned, zero comments. Extends epic **PLAT-269752**, which already shipped IMS + Workfront providers and caching. **An owner exists on that epic; attaching 290634 to them with a date is the object-backed move.**
- **Cross-skill routing evals** stay unanswerable while Clint's two marketplaces are absent from `scripts/fetch_skills.py`. ⚠️ **Pedro declined that re-run on 08-04 — his call, recorded, not an oversight.**
- **CODEOWNERS still broken** — `aem-p42-forms` unknown owner, EPA and Governance absent. He named the gap; nobody fixed it.

### ⏳ OVERDUE — PEOPLE BACK FROM LEAVE, UNCAPTURED

- **🔴 Rachel Hanessian back ~07-29.** She owes the **Miro of EH placements**, the coexistence/cohort-0 write-down, and the POD answers. **Her 07-15 ask — *"where are all the placements in AEM that we can take over?"* — is still unanswered by AEM after three weeks**, and it is the most direct ask anyone has made on Pedro's own product in this migration. **It does not get answered by waiting.**
- **🔴 Brandon (Coworker UI owner) back ~07-30.** He is the answer to "UI is the biggest bottleneck". **The planned route was via Manas's bi-weekly and that bi-weekly was never set — the route is dead. Go direct or drop it.**
- **🔴 Manas follow-ups, ownerless since ~07-20:** the **org→manifest artifact Bertrand has asked for three times** (Manas handed convergence to Yelena and is **not** producing it, so it stays Pedro's) · the bi-weekly to set · the written agent-context brief · the audit to **Yunyao Li** (⚠️ presets moved to 19/17/0 vs 15/12/9).
- **⏳ Gilles Knobloch** — asked 08-03 whether the KR 1e video played in full. ✅ Answered verbally 08-06: **they never got to it, the meeting was derailed.** Residual below.
- **⏳ Ramon Bisswanger** — Pedro owes the **documentation draft + go-to-market / monthly release notes for the Security Health GA** (asked twice on 07-24, *"that is on my todo P1"*). Ramon delivered his half.
- **⏳ Philippe Kapfer** — DM 08-03 10:47, offers to update the canvas; reports a prod problem in Foundation Internal.
- **⏳ Ken's provisioning window is open** (*"the SKU won't be available in AEP Provisioning until after the 1st week of August"*). **The scale question was never asked: does it take a ~2.6k-org patch in one go, or is there a ceiling?**

### ⏳ REPORTING + KR RESIDUALS

- **🔴 The metric-migration plant did NOT land.** *"67 thousand is the number I will report from now on"* was **cycle 1**, and the KR 1e video was never played. **Treat the next reporting cycle as cycle 1, not cycle 2 — re-plant it live** ([[migrate-leadership-from-a-volume-metric-to-a-value-metric-without-a-cliff]]).
- The 1,202-vs-665 MCP-reach line and Q3 28.5% On Watch **went unchallenged because they went unheard. Do not read the silence as acceptance.**
- **⏳ Ask Gilles or Tatyana Kozachek what displaced KR 1e** and whether it gets a slot next review. A scheduling ask, not a complaint.
- **⚠️ Do not upload another KR video without checking the streamed length.** The uploaded copy played as **1 second**, four times; Tracy's only fix on record is *"download it from the video folder"*.
- **⏳ Exact values for the June external-overtakes-internal crossover.** ~7,600 vs ~6,700 was **read off a curve, not a printed label**, and it is in a submitted Workday document. **Strongest business milestone in G1 — do not leave it approximate.**
- **🔴 Produce one EH number of Pedro's own.** Grafana access logged 2026-04-08 but the Bertrand 1-1 file still asks *"need to join the IDP group… Is access still possible?"* **On a goal titled "measurable driver of adoption growth", he has produced no measurement.** The *14,000 users / 79% retention* in the submitted check-in is **Guliz's June-05 number, not instrumented**.
- **⚠️ Third number needing backing:** *"36 skills have a coherent when-to-use"* is the excat-carried 34.3%; **customer-facing is ~5 of 45**.
- **⏳ Release Management (Razvan)** — capture the 07-30 "Release activation" outcome; the *"Update Free periods"* push-back context is still unknown to memory. **Ask before drafting anything.**
- **⏳ The "super release notes"** — where does the artifact live, and does it get a vault copy ([[feedback_vault_copy_of_published_pages]])? Pedro's open call: name the two Security Health limitations (prod-only, Java-only) or not.

### ⏳ TBYB + PROVISIONING PINGS (set 2026-07-23, still open)

- **Ken**, in his 07-18 provisioning thread: does the automated provisioning landing after the 1st week of August take a **~2.6k-org patch in one go**, or is there a ceiling?
- **The "no banner" state**, in Namita's UI-kill-switch thread, to Tim Lynn / Mikaela / Mark Doten: name the state AEM needs (backend-enabled, zero entry points, **immersive route closed too**) and that **EXC-48837** decides whether it is durable. **Ownership rep, not a question.**
- **Sergiu + Felix** — is the bridge uni- or bidirectional, does Coworker get prior-turn context. **Relay, do not defend the bridge.**
- ⚠️ **Correct the v7 status note:** "cohort 1 live ~174" → **174 provisioned backend, 22 UI-live 07-21, ~152 targeted 07-23**.

### 🟡 RENDERING-SURFACE OWNERSHIP (07-20, balls in court — `#aep-agent-orchestrator-collaboration` `C08U50NRA01`, cc Sorin + Eugene)

- **🔑 Manish Bansal — ball back with Pedro, and this is the ownership move.** He answered with the auth model (user-context). **User-context alone is not the guardrail: pin (1) the call carries the user's token, not an over-privileging service token, (2) the target service is allowlisted/registered, (3) audit — and OFFER TO WRITE IT UP as the repeatable "skills that render actionable UI" pattern. The write-up is the land-grab, not the answer.**
- **Pankaj Sangra** — awaiting his end goal (preview vs interact vs act-on-page). ⚠️ Pedro's draft asserted "no capability today" without positive proof; **confirm with Rodson/AO before doubling down.**
- **#2300 (`Adobe-dxue/coworker-ui-experience`) — PageUrl context NOT forwarded to Coworker.** Open, Mikaela Symanovich, no movement since 07-17. ⚠️ **This is Eugene's "can the panel act on the EH dashboard" question — context INTO the agent — NOT Pankaj's inline-render. Three distinct capabilities; do not collapse.**

### 🟡 CLIENT-ID / TRUST (de-risked 07-20, watch only)

- ⚠️ **THERE IS NO AEP-IMPOSED "WEDNESDAY DEADLINE". Do not escalate on one** — it would be a wrong fact in front of Bertrand. The RCA is retrospective SEV3; the only time signal was a revert-hold window.
- ✅ **The revert is in place and works.** No outage. Blast radius was **Governance MCP only** (other AEM MCPs have no client_id enforcement).
- 🔴 **The architecture fight is the real blocker and is unresolved:** the RCA says allowlist `gpt_power_client` on a team's own MCP server; **Ian Boston blocks allowlisting on the AEM fleet** (*"all traffic must go via the service proxy"*). **`GRANITE-70593` must decide.** 🟢 Alex Trifan agreed to request-signing with a service token instead of re-pushing. ⏳ **Watch: does Ian's commentable proposal land, and does the Coworker team hold the re-push until the proxy is in place.**
- **🔑 VW is the shaping test case** — co-innovation wants **only Governance for specific people**. Ian answered the per-AGENT half; **the per-PERSON half is still unanswered.**
- ⏳ **Wouter's Tokyo test is still partial** — AEP/CJA/AJO work; the AEM part was blocked by env startup failures, **not** the client-id path. The AEM-skills-through-Coworker question is unanswered end to end.

### 🔴 CAREER — MID-YEAR REVIEW (undated, the next real checkpoint)

- **⏳ Bertrand's mid-year review is pending.** Pedro has already told him he is aware of the AI-phrasing feedback. ⚠️ **Do not re-open that conversation backward** ([[feedback_dont_litigate_prior_replies]]). **What counts is evidence between now and the review.**
- **🔴 The AI-phrasing item is the symptom; the "good scribe" read is the damage.** Felix Meschberger doubts Pedro understands the topics he works on. **Plainer prose does not move that — one visible judgment per outward artifact does.** Watch for a Meschberger-facing moment where he takes a position and holds it.
- **🔴 Scope risk: Ramon proposed in writing that a Bucharest PM take over the release track.** Not hostile, but it sits in a record Bertrand reads. **Decide before the review whether to defend it or trade it deliberately — don't let silence decide.**
- **⏳ Depth was named by two of seven reviewers** (Meschberger; Valentin *"fewer initiatives, more depth"*). Coordination praise is universal; **depth is where the doubt clusters, and depth is the Senior Director marker.**
- **🟢 Bank these, they are manager-authored scope evidence in a permanent record.** Bertrand, unprompted, in Workday: the Coworker migration is *"a dependency for a lot of other teams, not just his own"*, and *"the reporting layer Pedro is building is becoming the thing the rest of us lean on to make good calls."*
- **🔴 Bertrand also wrote G1's work *"needs to be… redone for a large part given the move to Coworker."*** → the Rubin/definition port is the H2 G1 story, not insurance. **G3 got four words ("well noted") and no outcome comment. That asymmetry is where H2 gets allocated.**
- **⏳ One paragraph to reframe if it comes up** — *"I did not try to debate - what I did was to share as much informations as I collected"* **reads as the scribe posture in the first person.** The true version is a judgment: he declined the engine-topology fork and owned the customer-facing boundary, validated by Felix and Ian within the hour on 07-22.

### ⏳ 2026-07-24 — PEDRO'S OWN LIST (named on his last working day before PTO; unticked ≠ missed)

- **The UI-vulnerabilities POC thread** — Eugene, Andres, Valentin, Ramon. ⚠️ Names verbatim, unresolved to handles; could be 4 people or "Andres Valentin" = one. Ramon Bisswanger is on `#aem-aep-coworker-rendering`, so this likely sits in the rendering-surface / actionable-UI-security lane. **Inference, not confirmed.**
- **Push TBYB with Yanira** · **messages for Release Management (Razvan** — ⚠️ surname + scope unknown to memory, resolve first**)** · **one co-innovation thread in `#aem-agent-owners-alignement`** (⚠️ exact subject TBD, ask Pedro). **Draft only, never send** ([[feedback_never_send_slack]]).

### 🔵 2026-11-01 — RE-CHECK `aem-experience-catalyst` (excat) EXCLUSION

- Check whether any AO manifest has started referencing excat. **Where:** `recheck_after` in `aem-audits.yaml`, then re-run `scripts/publish.py`. **Why:** excat carries **61 skills**, is excluded from every audit because no manifest reaches it, and **the day one does, every roster, naming count and collision number changes at once with nothing to announce it.** Flip `role: excluded` → `peer`.

### ⚠️ INFO, NO ACTION

- **Cohort 1B criteria explicitly exclude AEM** (*"AEP + Apps stand alone customer (no AEM or Workfront)"*). The 7/30 final list was never confirmed produced, **and is now unverifiable from where Pedro sits** — the channel carrying it went silent 07-28 and he is not in its replacement. Most recent AEM-side statement: **Ian Boston, 07-31, *"CoWorker is not enabled for AEM customers yet."***
- **⏳ ~mid-Sept 2026 — Forms→Rubin port**, an external 6–8-week promise made ~07-17. Forms usage invisible in reports until then. Correctly dated, no action.
- **🔴 2026-07-31 was "code complete" for the panel and it passed.** Availability was always mid-to-late August. **The EH-side plan built on "the rail ships 07-31" still needs re-dating.**

## History (closed)

<!-- ✅-closed watches move here with close date; prune below ~10 lines -->
- **2026-08-07** — file reshaped to the one-line rule (30.7K → ~10K tokens). Full prior content verbatim in `watches_ARCHIVE_2026-08.md`.
- 2026-08-06 — **Clint's 72-hour clock CLOSED.** Pedro answered 08-05 17:29 object-backed (62/63 manifest census, twelve CODEOWNERS lines); **Carsten answered the lifecycle question in 29 minutes after a week of silence.** Positive control for [[Say the Sentence That Obliges — the Hedge Transfers the Ask]]. Residuals kept above.
- 2026-08-06 — **KR 1e outcome resolved:** the video was never played, the meeting was derailed. Residuals kept above.
- 2026-08-03 — monthly System Review ran. H-007 resolved, parked cap enforced 15→2, decisions scored. **Next due 2026-09-01.**
- 2026-08-03 — the check-in was 2026-07-21; iA Writer track dead, Pedro's call. Authoritative goals = the submitted Workday version.
- 2026-08-03 — sections ≤ 2026-07-17 moved to `watches_ARCHIVE_2026-07.md`.
- 2026-08-03 — `.claude/memory-backups/20260702-pre-P1/` deleted, recoverability verified against git first.
