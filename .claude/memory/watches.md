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

### 🔴🔴 MON 2026-08-17 — THE BUG BASH CANNOT RUN AS PLANNED UNTIL ONE OF THESE IS DECIDED

> Found 2026-08-15. Full read: the 2026-08-14/15 block in [[project_aem_agents_intelligence]]. Mechanics: [[reference_aov2_marketplace_manifest]] 08-15 addendum.

- 🔴 **THE TARGET IS A PROD ORG AND THE PLUGINS ARE ON DEV+STAGE ONLY.** AEM Showcase `38931D6666E3ECDA0A495E80@AdobeOrg` sits in **prod segments only, zero of 30 stage segment files** — so the stage shell is not an option, it is an identity gate not a config one. **Bug bash starts Tue 08-18.**
- 🔴 **AND THE PROD PORT IS BIGGER THAN ANYONE HAS SAID: `prod/cx-coworker.yaml` HAS NO `api_configs` AT ALL.** Pushing only the plugin list ships AEM skills that cannot call AEM. **Nobody has costed porting the block.** Ask Lenard Palko + Ian Reasor + Grant Russell, and reframe from "endpoints" to **"who ports `api_configs` and is it doable by Monday COB"**.
- 🟢 **The pattern to copy rather than invent:** prod already carries per-server `env_overrides` with a `stage:` branch for *"stage IMS users"* — CJA, AJO, GenStudio, Marketo, Workfront all declare one. AEM has none.
- ✅ **YANIRA'S BLOCKER IS CLEARED (she wrote 08-15 03:32 → https://adobe.enterprise.slack.com/archives/D018PT00155/p1786757531908129, Pedro answered that evening).** She had assigned **no author roles** because program, environment and AEM role were all unknown. Her prep stands: user group `AEM Agents on Coworker - GA Bug Bash - Authors` + the **CM Developer Role** required for EDA skills. ⏳ **Her thread to Florin Florescu is still unanswered** → https://adobe.enterprise.slack.com/archives/C0BARAMM89Z/p1786714657830989?thread_ts=1786714378.824629&cid=C0BARAMM89Z
- ✅ **THE STAGE ROUTE IS DEAD, PROVEN NOT ARGUED (08-15 evening).** `401 invalid OAuth token`, different IMS org. The fallback org `AEM Sites Engineering` returns `403025` + `User is not provisioned` and has no Admin Console in its launcher. → **The bash runs on the prod shell.**
- ✅ **THE MERGED PLUGIN SET WORKS** — `/aem-cloudmanager-program-management` made a live API call and returned 13 programs on stage. **First real exercise of it, by Pedro.**
- 🔴 **EVERY WALL WAS AN ENTITLEMENT, FIVE FOR FIVE.** Admin rights are not access. **The dominant failure mode on Tuesday will be product profiles, and the bash would report provisioning as agent quality.**
- ✅ **YANIRA ANSWERED 2026-08-15 evening, Pedro** — `149891` · `1546481` (prod-author; stage-author is `1546482`) · `AEM Users` + `AEM Sites Content Managers`. 🔑 **Note for Monday: the AEM environment does NOT depend on Carsten.** Options 1 and 2 both point at Showcase, so program `149891` holds either way; only the stage-org option would move it and it is ranked last. **So the product-profile attachment can proceed before his answer, and it is the difference between finding the entitlement wall on Sunday or on Tuesday morning with 30 people watching.**
- 🟢 **BEST OPTION: a Showcase-scoped prod manifest**, precedent `cx-coworker-lloyds.yaml` / `cx-coworker-prada.yaml`. Dissolves Ian Reasor's regression objection. ⏳ Ask Lenard or Gerald how an org is bound to a manifest.
- 📤 **Posted 08-15 21:23**, Carsten group DM → https://adobe.enterprise.slack.com/archives/C0BPSMZBRPB/p1786821819886959. No replies at 21:30. **Missing from it: the 401 itself, the lloyds/prada precedent, and a date.**
- ⏳ **Ask Marius Duta which shell the EDA bug bash used** on Showcase. 🔑 **Sharper now — ask which *instance*: `eda-dev-author`, or one of the `CxCowork-2` set.** The existence of that program is evidence he already answered it in practice.
- ⏳ **Yanira's readiness call, Mon 13:30 CET** with agent owners. Her two open questions: what role exactly, and which of Showcase's many programs. She asked **Florin Florescu** whether the Dev Agent needs a Developer role — unanswered since 08-13.

### 🔴 2026-08-17 — THE ONE GATE THAT MAY BE THE ONLY GATE

- 🔴 **`aem-aia-extensions` has 16 open PRs, six older than ten days, and no named approver.** **Alejandro Moratinos asked "who could help us to merge our changes" on 08-14 10:23 and nobody answered.**
- 🔑 **Why it is now load-bearing:** Ian Reasor, 08-15 — *"Coworker just pulls in the latest plugin and the version isn't actually read."* If that describes the runtime, **the marketplace merge is the only thing standing between a team's commit and prod behaviour.**
- ⚠️ **It contradicts the spec and nobody has reconciled it.** `05-update-strategy.md` FR-UPD-005 says `manual` is the default and is notify-only; FR-UPD-002 says a catalog refresh must not alter installed content. **Requirements doc with unchecked acceptance criteria, so it may describe intent.** ⏳ **Carsten has not answered.** There is also a third value, **`auto_patch`**, absent from every AEM discussion.

### 🆕🔴 FRI 2026-08-14 — OWED NOW

- ⚠️ **`correct:` 08-15 — MOSTLY ANSWERED ALREADY, do not re-raise as "five people waiting".** Pedro answered Ken on the AO 1.0 prompts at 08-14 07:58 and posted his `Progressive activation` doc at 09:19 (https://adobe.enterprise.slack.com/docs/T02CAQ0B2/F0BPBFCST5F), **which already carries the lot sizes (50 first, then batches of 500, triaged by org interactions)**. Group DM https://adobe.enterprise.slack.com/archives/C0BQ4L7BVL2 · her question https://adobe.enterprise.slack.com/archives/C0BQ4L7BVL2/p1786660097959949
- 🔴 **WHAT IS ACTUALLY OPEN — reconcile two rollout speeds, in one line to Namita.** His doc says 50 then batches of 500 (Ken's shape); **she said 50-100 over 4-5 weeks**; her literal *"Pedro what do you think about above?"* still has no textual reply. 🔑 **And say the thing nobody has said in that room — his timeline is post-GA on purpose (`08-27` internals, `08-31` top-50 TBYB, against GA 08-24).**
- ⏳ **Two asks land on Pedro inside his own doc** — the **HIPAA customer check**, and adding **AEM Forms Product Management `99A27D6C5F569E170A495E8E@AdobeOrg`** to the internal org list.
- 🔴 **ASK RAUL WHETHER `dma_aem_ams` COUNTS.** He flagged it 08-13 10:18 for EDA; **Pedro's mandate and the audit both know only `dma_aem_cloud`.** If AMS counts, every entitlement number published from 08-13 measures the wrong predicate for at least one team. Before Monday.
- 🔴 **THE WEEKLY UPDATE TO BERTRAND IS LATE — confirmed not sent by Pedro on 2026-08-15 17:52.** It was due Fri 08-14, promised in the 08-10 DM `DQ6H0AV7H`. **He is on PTO and answering, so the window is open, but it closes.** The 08-21 one is the pre-read before he lands on GA day, so a missed 08-14 makes 08-21 the only one he gets. Format per [[feedback_bertrand_status_comms]]. 🔑 **The week has a concrete win to lead with: 23 → 86 manifest surfaces in one merge.**
- 📅 **FRI 2026-08-15 — confirm the suggested-prompts approach.** Pedro's own dated commitment to the Coworker team. Still open; Sorin's Monday EH update touches the same surface.
- ⏳ **RE-OWN THE THREE EPA FAST-FOLLOWS.** Yanira attached them as the price of skipping Legal/AI Ethics on the Content Fragments skills (Security threat model · ORR runbook in `#skyline-oncall` · CCF onboarding), then the conclusion changed and **all three vanished with it.** Group DM `C0BPS8BS39C`.
- 🔵 **QUOTE CARSTEN'S ONCALL LINE IN THE MONDAY REMINDER** — *"each team not in the monorepo on GA date has to take over oncall for one month completely"* (08-13, manifest thread). An architect attaching a personal cost is stronger than another red audit row, and nobody has repeated it.
- 🆕 **CONRAD WOLTGE HAS THE COWORKER "LEAD" PER JEAN-MICHEL** (Bertrand, DM 08-13 09:15, *"ah ah"*; he forwarded the Loni note on). **Watch what "lead" means in practice and whether Pedro's GA authorship survives it.** [[feedback_position_over_merit]]

### 📕 CLOSED 2026-08-13/14 — THE MANIFEST DECISION AND ITS EXECUTION

> Compressed 2026-08-16. Full read: the 2026-08-13/14 block in `project_aem_agents_intelligence_ARCHIVE_2026-W33.md` and the matching Focus blocks in the AAI Status & Todo.

- ✅ **`cx-coworker` decided 08-13, shipped dev+stage 08-14 16:04** (`aep-ai#10608`, Lenard Palko, approved Gerald Prendi). Reach 23 → 86 of 241. Carsten: prod may be populated before 08-24 while entitlements are in place.
- ⏳ **Two residuals still gating.** Does `aep-ai#10061`'s `deferred` setting on One AEM MCP travel to `cx-coworker` (Corey filed it GA-blocking)? And **fifteen of sixteen ported plugins were unexercised** — ✅ **partly closed 08-15, Pedro ran the Cloud Manager skill end to end on stage**; the rest still have no owner.

### 🆕🔴 MON 2026-08-17 COB — THE TWO DEADLINES PEDRO SET HIMSELF

- 🔴 **`required_entitlements` in every skill.** Mandate sent 08-13 09:44; five teams moved inside eight hours (Governance PR #44 · EPA `AEMAGT-2511` · Forms `AEMAGT-2513` · EDA done · Discovery + Content Optimization done). **Carsten adds a monorepo PR check next week**, which makes it structural. Chase the teams that did not answer.
- 🔴 **Bug bash details and use cases on wiki `4002944931`**, target **AEM Showcase `38931D6666E3ECDA0A495E80@AdobeOrg`**. ⚠️ **Testing has already started decentralised** (Corey and Christian pushed back on waiting; EPA and EDA both ran sessions 08-13) — **the 08-20 confidence declaration will rest on a week of uneven coverage, so say what it covers.**
- ✅ **BRIAN'S EH ASK CLOSED 08-15 — Pedro handled it live with him, verbally.** ⏳ **Residual, and it is the only one — confirm the slide itself was edited in `FY26 Q4 AEM Roadmap.pptx` (~slide 57) before the 08-17 deadline.** Done-live closes the conversation, not the document. Links in [[project_experience_hub]].
- ⏳ **Sorin updates Experience Hub 08-17** (Coworker input, navigation item, announcement + top-bar message), validating on AEM Showcase, tracking thread open with an `EH — Checklist GA 24th` doc. **The EH placement answer is arriving as execution rather than as the written decision that was owed.**
- ⏳ **Tanju is back 08-17** — the One-AEM-MCP-as-single-OBO-fix-point question is his. Object now exists: Carsten's wiki `4003355459`.

### 🆕⚠️ 2026-08-13 — BEFORE QUOTING ANY READINESS NUMBER

- **The funnel is 66 → 56 → 30 → 19** (correct marketplace · name not a fail · disambiguation not a fail · entitlement declared), published 08-13 21:41. **19 is not a regression from the 21 of 08-11 — a fourth criterion was added.** Say so, or the movement reads as decay ([[Lead the Slide With the Honest Read of Your Own Metric, Not the Flattering Number]]).
- ⚠️ **And the entitlement predicate itself may be incomplete** — see the `dma_aem_ams` item above.

### 🔴 STILL OPEN FROM THE 08-12 SEND DAY

- 🔴 **VERIFY THE NON-BLOCK EXISTS, ask Yanira.** The 08-12 EPA decision rests on an informal AI Ethics non-blocking; **what is on file is Legal/ORR/Security only, no named person for AI Ethics.** `decisions/2026-08-12-announce-epa-on-informal-ai-ethics-non-block.md` ⚠️ **Sharper now: on 08-12 evening a second EPA skill set (Content Fragments) was also cleared of AI Ethics, this time by the four people in the thread. Two clearances in two days, no named reviewer on either.**
- 🔴 **CONFIRM THE GA SCOPE IS CLOUD-SERVICE-ONLY, same ask to Yanira.** Pedro told **three PMM** (Tina + Haresh + Vaishnav) *"we aim for GA on CS only"* on 08-12, sourced to a 2026-04-13 statement that itself says Managed Services agents *"may land H2"*. **PMM turns this into field messaging.** [[reference_tbyb_sku_entitlement]] ⚠️ Raul's `dma_aem_ams` flag cuts across this — if EDA entitles AMS, the CS-only line is already not what the skills say.
- ⏳ **ROLLING GA IS NOW A TWO-TEAM PATTERN.** Brian 08-10 (dev skills on the 31st, *"we would pull things from the main manifest"*, never answered Pedro's push-back) and **Corey 08-12 (*"if we miss the 24th we'll just add them in the following week"*)**. Nobody has said no to either. **A third instance turns the single date into a start date.**

### 🆕🔴 THE FOUR COWORKER GA BLOCKERS — PEDRO'S DATED COMMITMENTS, SENT 2026-08-12

> Full read and the reusable move: the 2026-08-12 block in [[project_aem_agents_intelligence]]. He answered the whole list with owners and dates so it closes without being refused.

- 📅 **FRI 2026-08-15 — confirm the suggested-prompts approach.** EH-side, and **decision #3 of the 07-03 chat-entry note is still unreconciled**; Eugene wants them hidden before 08-24 and cannot test in time. Route: Fu Chi (pipeline) + Zeus Courtois (AO2).
- 📅 **MON 2026-08-17 — send Cole the AEM instance-selection outline** for the Coworker UI. His 08-05 ask, *"really painful in AI assistant"*, never surfaced in any AEM bug bash.
- ⏳ **Chase Ilya Grafutko's front-matter document link** — Pedro asked for it in-thread and is committed to work against it *"as it stands today"*. **Without the link the commitment has no object.**
- 📅 **TUE+WED 2026-08-18/19 — all-in AEM bug bash across every agent.**
- 📅 **THU 2026-08-20 — AEM declares the confidence level**, on the bug bash output. 🔑 **Deliberately not "EOW"**, which would have put the decision one working day from GA and in someone else's hands.
- ⚠️ **TWO UNVERIFIED CLAIMS ARE NOW PUBLIC AND BOTH WERE FLAGGED BEFORE SENDING.** (1) *"Each agent team has run its own bug bash"* — seven teams, and Brian said 08-10 that the 24th was unrealistic for dev skills. (2) *"We are also running co-innovation projects and PODs with customers for a couple of weeks"* — **Ian Boston, publicly 07-31, *"CoWorker is not enabled for AEM customers yet"*, and Namita runs the rollout.** **Close both quietly this week rather than wait to be corrected.**

### 🆕🔴 2026-08-11 — MCP IS AN UNDECLARED GA DEPENDENCY, AND "THE OBO DISCUSSION" IS THREE LAYERS WEARING ONE NAME

> ⚠️ **Compressed to the one-line rule 2026-08-11. Full detail — the three-layer table, the ARB thread, the gateway-channel findings — is the `#### Companion` under `### Focus — 2026-08-11` in the AAI Status & Todo.** This section carries only what is dated and owed.

- 🔴 **OWED, unanswered, aimed at Pedro:** is the **MCP ARB review** (wiki `3908581554`) a Coworker GA requirement for One AEM MCP? Christian asked, Carsten bounced it to Pedro + Yanira, nobody replied. Thread `1786454864.103779`.
- 🔴 **DECIDE:** is **MCP readiness inside the announcement bar or explicitly outside it**? Pedro named the dependency himself 08-11 and it is in no artifact. 13 days out.
- ⏳ **ASK CARSTEN, one line:** server side is done (`AEMAGT-1361` Closed 08-06) — is what he is untangling the **client-id allowlisting** instead? 🧠 Deduction only, do not assert.
- 🔴 **TWO OBO TICKETS ROTTING, both per-agent-team:** `GRANITE-71254` (Brand Governance client id) New + Unassigned since **07-30**; `AEMAGT-2343` (aem-shift-left vs `gpt_power_client`, Gilles) New + untouched since **07-15**.
- 🔴 **AEM HAS NO ROW ON THE GATEWAY QUALITY DASHBOARD.** Golden eval dataset missing (Georgiana Copil, 08-11), dev config missing (08-07), both owned by Tanju + Christian. **That surface scores whether the model picks the right AEM tool — the outcome the naming audit proxies for.** Channel `C0ASGEU1BT9`, now in [[reference_slack_audit_channels]].
- ⚠️ **BEFORE CLOSING THE 08-12 MANIFEST CALL:** Paul Pop 08-10 — gateway tools reachable from prod `cx-coworker.yaml` **all fail and hijack tool selection** away from working dx-api tools.

### 🔴 RE-OPENED 2026-08-13 — THE GAINSIGHT BANNER ON AEM SHOWCASE

> Full history (the Sites Trial removal receipt, Apoorva's unanswered risk question, the two 08-11 replies) is in `watches_ARCHIVE_2026-08.md` — grep `SITES TRIAL`.

- 🔴 **Pedro confirmed AEM Showcase as the bug bash target on 08-13** (`38931D6666E3ECDA0A495E80@AdobeOrg`), and **the question that got AEM Sites Trial pulled from the Coworker flag on 08-06 was never answered for Showcase.** Enabling an org brings the **Gainsight banner**; Corey's reason for pulling Sites Trial — *"its an internal Org but we also use it for some external work as well"* — applies to Showcase, which is the SC live-demo org.
- ⏳ **Two replies still gate it, both sent 08-11 and both unanswered:** Rodson Clavel (`C0BCKG35NFP` ts `1786405114.307519`) on whether the panel prod flag is the same switch as the Coworker-enabled flag ([[reference_coworker_enablement]]), and Corey on whether the 08-06 removal still stands. 🔴 **Nobody has ever been named for the SC-enablement heads-up.**

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

### 🔴🔑 WED 2026-08-12 — THE MANIFEST DECISION (out of the 08-10 owners call, which HAPPENED — full read: shard `project_aem_agents_intelligence_ARCHIVE_2026-W33.md`, grep `THE OWNERS CALL`)

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

### 📕 CLOSED 2026-08-10 — the pre-call state of the owners call (compressed 2026-08-14; full text in `watches_ARCHIVE_2026-08.md`, grep `pre-call state`)

- **The three residuals that are still live and are tracked above or in the project memory:** the **seven agent-map decisions only Pedro can take** (51 of 88 skills with no agent, so no agent-cut number is publishable) · **AI Ethics on EPA** (*"team will evaluate end of Aug"*, after both 08-14 and 08-24) · **`skill_inclusion_policy` rewards silence** (zero of 217 manifests use it; absent defaults to `stable`, which would delete AEM's honest 62-of-63 `experimental`).
- **The 08-06 funnel it carried (0 of 87 conform / 4 conform-or-warn) is superseded** by the 08-13 run — 66 / 56 / 30 / 19. Do not requote the old one.

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
