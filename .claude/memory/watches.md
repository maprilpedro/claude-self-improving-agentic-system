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

### 🆕🔴 2026-09-02/03 — THE SLACK AUDIT LEFTOVERS (full read: [[project_aem_agents_intelligence]] 2026-09-02/03 block)

- 🔴 **Lianne Ramos: deploy the AEM Gainsight "You will soon have access to Coworker!" for the 09-08 cohort (AEM tab of Paul's Cohort 3 file) and reply in her thread.** Asked for 09-02. https://adobe.enterprise.slack.com/archives/C0ABFLYLZK7/p1788303738883819?thread_ts=1788299118.059049&cid=C0ABFLYLZK7
- 🔴 **Confirm `#12863` to Yelena + Corey** (23 orgs stay on their manifests, 28 added to `cx-coworker`) and say whether UPS and the other `aem-aia` orgs move to default. Corey: "please confirm tomorrow" = 09-03. https://adobe.enterprise.slack.com/archives/C0ABFLYLZK7/p1788287042298669?thread_ts=1788287042.298669&cid=C0ABFLYLZK7
- 🔴 **Siddharth: ABAC Content Hub live in prod (09-01), works without the panel (Philippe 09-02) → move his 34 orgs to early cohorts.** ⚠️ Conflicts with what you told Paul 09-02 09:11 ("any cohort with SKU = not before Panel"); settle it once in the file. https://adobe.enterprise.slack.com/archives/C0BDAF2H2AG/p1788283915326929?thread_ts=1787563649.301049&cid=C0BDAF2H2AG
- 🔴 **Answer the field on AMS customers in Cohort 2** — Stephanie (Commonwealth Bank) and David Zepeda (Honeywell). Sophia Gray's "opt them out" is unconfirmed. 📅 09-03 https://adobe.enterprise.slack.com/archives/C070SDG809J/p1788310504113279?thread_ts=1787554074.319519&cid=C070SDG809J
- 🟡 Rodson Clavel, one line on `?shell_aiChatEnabled=true`. https://adobe.enterprise.slack.com/archives/C0BCKG35NFP/p1788281672808259?thread_ts=1788249231.451749&cid=C0BCKG35NFP
- 📅 **09-10 — Tatyana Kozachek's September release review: list every AEM agent and Coworker integration on the release wiki.** https://adobe.enterprise.slack.com/archives/C06NCR238DS/p1788273000655649
- 📅 **09-08 — David Gonzalez back from OOO; his demo org activated with AEM in Coworker** ("let me follow-through", 09-02).
- ⏳ Rachel / Raj / Eric: the <2-min demo video + script promised for 09-01 — verify Babu's 08-31 demo links are that deliverable. https://adobe.enterprise.slack.com/archives/C0BT9J90SRZ/p1787937174748749
- ⏳ Guliz: the brand-governance / enterprise-context thread with Bertrand + Philippe promised 08-28 "next week". Not opened.
- ⏳ Emil Serban: Rubin walkthrough once his access works (login `access_denied` 09-02).
- 🔵 **Bertrand's 08-31 `#p42-architecture` question, an "active" AEM instance in Coworker like the EH rail — unanswered; it is the instance picker Cole owes.** https://adobe.enterprise.slack.com/archives/C09KKLW1N86/p1788164868708439
- 🔵 Ethos CORS blocker `EON-73057` (no wildcard CORS on `author-pNNN` domains) now has a channel, `#aem-wildcard-cors-enablement` `C0BTZS3APGF`; Felix joins the Ethos office hour 09-03 17:00 CEST. Next-phase gate, not GA.

### 🆕🔴 2026-09-01 — AEM HAS NO PROMPT SURFACE ON ITS OWN GA MANIFEST

> Full read: [[reference_coworker_system_prompt_blocks]] + the 2026-09-01 blocks in [[project_aem_agents_intelligence]] and [[reference_aov2_marketplace_manifest]].

- 🔴 **Pedro writes the ask to Shubham Lohiya** — can a plugin/marketplace contribute a `block_dir`, or get a plugin-scoped PreTurn hook? Authority sits in their own design decision #4. Namespace `aem_*` (suppression is global by `block_id`). 📅 09-03
- 🔴 **One question to Carsten** — when does the temporary `aem-cx-coworker` bug-bash manifest leave prod. ✅ The pin/un-pin is explained: 09-02 the prod manifest switched to the `prod` branch of `aem-aia-extensions`, `main` no longer affects production. 📅 09-03
- ⚠️ **Never call `aem-aia` "AEM's manifest" outward.** It is the AI Assistant lane; the GA home is the shared `cx-coworker.yaml`.
- 🟢 **Compare the 19 Showcase CSV names to the 19 bug-bash plugin refs** — probably closes the 08-27 scope question. 📅 09-05
- 🟢 **Ask Danny Miller for the guardrails Excel** (Zan Chu asked 08-27, never got it). No AEM guardrail list exists. 📅 09-05
- 🔧 Panel/rail flag: `?shell_aiChatEnabled=true`, after `/ui`, not in the hash. [[reference_coworker_rail_access]]
- 📌 Deferred, Pedro's call: spec a `/deck` skill via `/skill-creator` — 3 PPTX memory files + 10 `patterns/` presentation entries exist, nothing wires them.

### 🔴🔴 2026-08-26 → TUE 09-01 — THE COHORT DECISION IS THE LIVE ONE (compressed 2026-08-31)

> Full read: the 2026-08-25/26 block in [[project_aem_agents_intelligence]]. Pre-compression verbatim in `watches_ARCHIVE_2026-08.md`, grep `Verbatim snapshot appended 2026-08-31`.

- 🔴 **09-01 — do the five ABAC orgs come out of the batch?** Qantas · NWL Brands · Corporate & Investment Bank · Warner Bros Marketing Cloud · Okta. ⚠️ 09-01 Siddharth: ABAC Content Hub is live in prod, the hold reason is gone — see the 09-02/03 section.
- 🔴 **LG Uplus Corp (`472883976A0E01D20A495CE8`) opted out late (08-28); Paul removed it from `Cohort_AEM_2.1_TBYB` 09-01 — move it to an Opt Out cohort in your file.** The only 5 of the 34 `ABAC Customer = YES` that sit on Paul's list, all dated 09-01, landing the day before the parity plan is due.
- 🔴 **`Cohort_AEM_WF_SKU` holds 15 named ABAC customers and has no rollout list on any of Paul's three tabs.** Costco · Pfizer · Delta · PNC · Sams Club · Edwards · Steelcase · PwC GLSC · Microsoft Project Supreme · BAT · Havas · OXXO · Koch · Hottinger · Freddy.Connect. Pedro created the bucket 08-18. Open a line for it or ask Paul to fold it into `Workfront+Target`.
- 🔴 **Before 2026-09-02, reconcile the SKU population.** Bertrand 08-24 says 90 licensed / 24 paid / 66 at $0; Pedro's file says 335; he told AMS ~3K. Ask Bertrand for the DaaS query, not the result. [[reference_tbyb_sku_entitlement]]
- 🔴 **Send the Loni email — four fact divergences still open.** `Monday 21th` → 31st, and `announced publicly` contradicts his own GA definition · `no release blocker` contradicted by `NXUI-1904` · Major count 10 → 11 against JIRA's 4 · `with clear review dates` false for DA and Governance.
- 🔴 **The Governance MCP ARB review is Pedro's and is still `TBD`.** `DXARB-1064`, filed by Marc Pfaff; Christian named Pedro 08-19 to chase Philippe or Marc's stand-in. The only one of the three with no date.
- 🟢 **Send Bertrand the skill-vs-MCP duplications.** He asked 08-24/25. **Five families in the full catalogue** (Brand Governance · Permissions Governance · Content Supply Chain · Document Authoring · Asset Sourcing); **three pairs in the Showcase file** (Governance · Experience Generation · DA). ⚠️ The list differs by file — say which one you are quoting.
- ⚠️ **18 of the 34 opt-out requests are absent from Pedro's own `Cohorts` tab**, many `Org Not Found`, all seven Samsung orgs among them. ✅ No opt-out org appears on Paul's list.
- 🔑 **Paul's `Cohort` column is an `XLOOKUP` into Pedro's own workbook** — his list is derived, so a gap is a stale-link symptom first and a disagreement second.
- ⚠️ **The internal GA announcement went out 08-25 12:42** (`C0BSBN56403`), both false claims removed. Residual: it quotes `62 AEM skills`, which is the marketplace and not what a customer sees. Jaclyn's ask for success criteria between cohorts is still unanswered.
- 🔧 **`AEM Agents on Coworker - GA Bug Bash - Authors` is an Admin Console USER GROUP** → `adminconsole.adobe.com/38931D6666E3ECDA0A495E80@AdobeOrg/users/groups` (AEM Showcase). As created 08-15 it carried only the CM Developer role, no author roles.

### 🆕🔑 2026-08-27 — TWO INVENTORY FILES, DIFFERENT SCOPES, AND THE 08-27 COUNTS WERE WRONG

> Full read: the 2026-08-27 block in [[project_aem_agents_intelligence]].

- 🔴 **CORRECTED COUNTS for `table (3)`/`table (4)`. 93 data rows, 85 skills, 8 MCP — not 92 / 84.** 50 `Skill` · 23 `Skill (Sub)` · **8** `Skill (API Ref)` · 2 Orchestrator · 1 Router · 1 Internal. **User-reachable = 60**, not ~59 (85 minus 25 rows at Access Point `Internal`). The 8th API Ref, never named before, is `aem-cloudmanager-releases-access`.
- 🟢 **LIKELY ANSWERED 2026-09-01, verify in one name comparison.** The prod `aem-cx-coworker.yaml` ("AEM Bug Bash Coworker") installs **19** `aem-aia-extensions` plugins; the Showcase CSV lists **19** skills. And the marketplace `exclude` policy on the GA manifest names **three of the five "missing" families** (`aem-edge-dispatcher`, `aem-workflow-ops`/`-api`, `experience-replication`/`aem-replication`). → **The CSV is probably an extract of what the bug-bash manifest installs, not a rival inventory.** Content Supply Chain + Asset Sourcing are absent for a different reason — not in `aem-aia-extensions` at all. **Compare the 19 names before quoting either count.** [[reference_aov2_marketplace_manifest]] 2026-09-01 block.
- ⚠️ **`table (4).csv` is byte-identical to `table (3).csv`.** A re-download, not a new extract. Run `cmp` before treating a new file as an update.
- 🔴 **Five families are in the catalogue and absent from the Showcase file:** AEM Dispatcher (8 skills) · Content Supply Chain (2 + its MCP) · AEM Workflow (2) · Asset Sourcing (1 + its 76-tool MCP) · AEM Replication (1). Two skills exist only in the Showcase file — `aem-sites-figma-read`, `aem-sites-visualcontentfragments-create`.
- 🟢 **CHEAPEST RATIONALISATION, and Pedro can decide it alone: demote the API-reference layer.** The Showcase file's 7 `Skill (API ref)` rows describe **4 backends**, and only 3 are declared as `API Service` (`bps-il-admin-console` is not; `update-profile-api` names no service). Doing it takes the Showcase skill count **19 → 12** with no capability removed. Manas's 07-16 tiered-documentation point arriving as data.
- 🟢 **Two more cheap ones.** AEM MCP and OneAEM MCP are 14 tools each with near-identical use cases, the only stated difference being `code-mode org` ⚠️ but Carsten froze MCP consolidation 08-19, so post-GA. And `aem-sites-figma-read` is a step of `aem-sites-visualcontentfragments-create` with no other consumer.
- 🔴 **Usage is measured nowhere.** On all 27 Showcase rows `Usage Metrics = No` and `Alerting = No`. The five MCP `Partial` values are a **connection health check** — liveness, not usage. The only usage-shaped object in either file is `Progress log (aem-onboarding-progress)` on `aem-onboarding-workflow`, built by one team for itself. **That is the pattern to generalise and it is Pedro's lane.**
- ⚠️ **Naming: one conversation, not five renames.** `adaptive-forms-authoring`, `experience-generation`, `experience-governance`, `update-profile-api`, `bps-il-admin-console` break `aem-<app>-<feature>-<action>`, and `aem-cloud-manager-ops` spells `cloud-manager` where `aem-cloudmanager-api` spells `cloudmanager`.

### 🆕🔴 WED 2026-08-19 — ASK NAMITA: THE DATA-USAGE OPT-OUT IS NOT THE ROLLOUT OPT-OUT

- 🔴 **How does Coworker treat orgs that have opted out of their data being used for product enhancement?** Nobody has written it down, and it is a different object from the rollout opt-out Namita already runs (the admin email that lets an admin refuse the flip). **Two opt-outs wearing one word** — do not let them be answered as one.
- 🔴🔑 **THE FILE ALREADY ANSWERS IT AND THE ANSWER IS BAD (read 2026-08-19).** Column **N `GenAI Status`** in `20260814-AEM_COHORTS.xlsx` carries the rider status on all 3,104 rows. **Only 533 orgs (17%) are cleared for `Providing the Service and Product Improvement/Dev`.** **905 are `Providing the Service Only (Oct 25 Rider)`** (891 external), 45 `No GenAI`, 5 `No Data Access or Data Usage`, 325 `Unvalidated`, and **1,291 are `#N/A` — a broken lookup, 42% of the file with no status at all.**
- 🔴 **AND THE RESTRICTED ONES ARE ALREADY LIVE. 100 of the 905 `Service Only` orgs are already provisioned, plus 209 of the 1,291 `#N/A`** — **309 orgs on Coworker today that are either contractually restricted or unknown.** Named example, **United Health Group** `8E391C8B533058250A490D4D@AdobeOrg`, Cohort_AEM_3.1, `Providing the Service Only (Oct 25 Rider)`, already provisioned `Ad Hoc`. **Do not present this as an accusation — ask what the rider forbids at which layer, and who enforces it.**
- 🔑 **The three adjacent markers, still to disambiguate.** `No GenAI` 45 · `Unknown GenAI Rider Status - Sensitive Industry` 113 in column G · 104 rows marked `Opt out`. **Ask whether they are the same restriction, overlapping, or unrelated.**
- 🔴 **And it lands on Pedro's own lane, which is the part to say out loud.** Prompt and response events flow into the observation pipeline and into Rubin ([[reference_ai_observation_architecture]], [[project_aem_agents_intelligence]] Rubin block) — *"regardless of their origin, if they touch AEP AO we should have it in Rubin"*. **So a customer who refused product-enhancement usage may still be feeding the reporting layer Pedro owns.** Ask who enforces the exclusion and at which layer. ⚠️ Adjacent to Ian Boston's residency red line, do not merge them.
- ⏳ **Where:** the rollout weekly / group DM `C0BQ4L7BVL2`. Namita runs the rollout while Rachel is out ([[reference_namita_scope]]).

### 📕 PRE-GA AUGUST SECTIONS, COMPRESSED AT THE 2026-09-03 REVIEW (six sections; verbatim in `watches_ARCHIVE_2026-08.md`, grep `appended 2026-09-03 review`)

- 🔴 **`dma_aem_ams` is declared on four Cloud Manager skills, so "GA on Cloud Service only" is not what the skills say.** Pedro told Tina, Haresh and Vaishnav the opposite 08-12. Ask Raul whether AMS counts; every entitlement number since 08-13 may measure the wrong predicate for one team. Correct it before it reaches sales.
- 🔴 **Namita's *"Pedro what do you think about above?"* on rollout speed (50 then batches of 500 vs her 50-100 over 4-5 weeks) never got a textual reply.** Overtaken in practice by the 09-08 cohort, still unanswered in writing.
- ⏳ **Two asks inside Pedro's own Progressive-activation doc:** the HIPAA customer check, and adding AEM Forms PM `99A27D6C5F569E170A495E8E@AdobeOrg` to the internal org list.
- ⏳ **Re-own the three EPA fast-follows** Yanira attached as the price of skipping Legal/AI Ethics on the Content Fragments skills (security threat model · ORR runbook in `#skyline-oncall` · CCF onboarding); they vanished when the conclusion changed. Group DM `C0BPS8BS39C`.
- ⏳ **Answer Corey's 08-10 bar question precisely** — warnings vs failures, hidden vs customer-facing skills (the 0-vs-4 and the 87-vs-98).
- 🆕 **Conrad Woltge has the Coworker "lead" per Jean-Michel** (Bertrand DM 08-13). Watch what "lead" means and whether Pedro's GA authorship survives it. [[feedback_position_over_merit]]
- ⚠️ `aem-aia-extensions` merge gate (16 open PRs / no named approver on 08-17) — superseded 09-02 by the `prod` branch switch; only the *"Coworker pulls the latest plugin, version not read"* spec contradiction (Ian Reasor 08-15) is unreconciled.

### 🔴 STILL OPEN FROM THE 08-12 SEND DAY

- 🔴 **VERIFY THE NON-BLOCK EXISTS, ask Yanira.** The 08-12 EPA decision rests on an informal AI Ethics non-blocking; **what is on file is Legal/ORR/Security only, no named person for AI Ethics.** `decisions/2026-08-12-announce-epa-on-informal-ai-ethics-non-block.md` ⚠️ **Sharper now: on 08-12 evening a second EPA skill set (Content Fragments) was also cleared of AI Ethics, this time by the four people in the thread. Two clearances in two days, no named reviewer on either.**
- 🔴 **CONFIRM THE GA SCOPE IS CLOUD-SERVICE-ONLY, same ask to Yanira.** Pedro told **three PMM** (Tina + Haresh + Vaishnav) *"we aim for GA on CS only"* on 08-12, sourced to a 2026-04-13 statement that itself says Managed Services agents *"may land H2"*. **PMM turns this into field messaging.** [[reference_tbyb_sku_entitlement]] ⚠️ Raul's `dma_aem_ams` flag cuts across this — if EDA entitles AMS, the CS-only line is already not what the skills say.
- ⏳ **ROLLING GA IS NOW A TWO-TEAM PATTERN.** Brian 08-10 (dev skills on the 31st, *"we would pull things from the main manifest"*, never answered Pedro's push-back) and **Corey 08-12 (*"if we miss the 24th we'll just add them in the following week"*)**. Nobody has said no to either. **A third instance turns the single date into a start date.**

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

### 🔴 2026-08-07 → 08-24 — BERTRAND'S PTO RUN-UP (compressed 2026-09-03 — verbatim in `watches_ARCHIVE_2026-08.md`, grep `appended 2026-09-03`)

- 🔴 **The 08-14 weekly to Bertrand is written and still unsent** (`20260816 - Report to Bertrand`); owed on top: exec summary, the fifth blocker, the prod line, the dead OBO link, the 38-of-71 denominator. [[feedback_bertrand_status_comms]]
- ⏳ Still watch the joint PM/PMM GTM plan with Tina Ngo — whether it reaches Loni and whose name is on it ([[feedback_position_over_merit]]).

### 🔴🔑 WED 2026-08-12 — THE MANIFEST DECISION (happened; compressed 2026-09-03 — verbatim in `watches_ARCHIVE_2026-08.md`, grep `appended 2026-09-03`; full read shard `project_aem_agents_intelligence_ARCHIVE_2026-W33.md`, grep `THE OWNERS CALL`)

- Residual only: `cx-coworker` is the GA default, decided 08-12; teams that never PR'd their manifest are in the 08-27 inventory gaps.

### 🔴 THE AUDIT HAS NEVER MEASURED THE DESTINATION (opened 2026-08-10)

- `aem-audits.yaml` lists **10 marketplaces, all AEM**. `cx-coworker` registers **13**; only `governance-agent-marketplace` overlaps → **12 invisible**. **Every disambiguation number is AEM-against-AEM.**
- **Two changes to commission, by PR** ([[feedback_audit_repo_works_by_pr]]): add the 12 as `role: peer`; emit `required_entitlements`. ⚠️ **Say up front that it moves every denominator.** Christian Meyer asked for exactly this on 08-10 and wants a plan after 08-24.

### 🆕🔴 ON-CALL IS A GA GATE NOBODY HAD (2026-08-10, group DM `C0BPMVDECSU`)

- Agents were never onboarded to `#skyline-oncall`; runbooks are written for **a2a**, not the skills model. **Carsten: *"the incident will first land with coworker and then it might be unclear which teams is responsible for a skill."*** Yanira drives, starting with the EPA runbook; Carsten covers for Ian (PTO); **Toby Such, who framed it as the pending ORR work, is out all month.**
- 🔑 **Pedro's move: the audit can emit the skill→team column from CODEOWNERS.** Offer it before seven teams build it by hand. This is the consumer the parked "repoint the ownership axis onto CODEOWNERS" item never had. ⚠️ **Different column from the agent map** (plugin→AOv1 agent); do not merge them.

### 🔴🔑 WEEK OF 2026-08-10 — RUBIN ([[project_aem_agents_intelligence]] 2026-08-06 RUBIN SYNC block)

- **✅ AXIS SETTLED 2026-08-07 — publish on the skill NAME with the error rate footnoted.** PR15's plugin rooting stays the record of record; the name is what ships. **The footnote is not optional, it is what makes it defensible.** Measured on the 08-07 run, **98 rows / 85 distinct skills**, the name gives a clean application segment on **51 of 98**; 18 loose tokens, 14 from declared `domain:`, 4 from plugin, **11 unresolved**. Live artifact = canvas **`F0BN06V01GF`**. ⏳ Still worth asking Rubin to log `plugin` — it retires the footnote.
- **⏳ Canvas `F0BN06V01GF` fix-list** (Pedro filled it 08-07): the **`Confirmed` column has no owner named on any row** — putting a name per row is what could close five of the seven agent-map decisions in one meeting; the **error-rate note is not on the canvas**; the Rationale states the future as present (*"all skills shall have a dedicated application token"*, today 51 of 98); `aem-cloudmanager` = EDA is now unhedged though two of its fifteen read as Modernization, which has no reporting id; two typos in the opening two lines.
- **⏳ Early access to the Report Builder was promised for this week.** Chase it. 🔴 Pedro's own words: *"if we miss that milestone, then I will have nothing for the GA."*
- **⏳ The skill-grouping map is Pedro's to send**; Rubin is waiting on it. ⚠️ Same object as the seven agent-map decisions — cannot go complete before 08-10.
- **🔴 Ask the two questions that were missed** while Angela Han and Karthik sat in the room 22 minutes: (1) Ramkesh's GA-skills-only claim, **needed for 08-10**; (2) Hemanta Gupta's no-ingress finding. ⚠️ Angela's side-load answer is adjacent and cuts mildly against Hemanta — she objected to the **cadence** (*"are you going to side load them every week?"*), not the capability. **Not an answer, do not bank it as one.**
- **🔴 SKU vs TBYB still cannot be split**, and it blocks Namita's cohort ordering. Yanira named the older blocker (**Andre, DAS team: no quick indicator**) and is surfacing it on Slack. Angela's bar: a **root provisioning API**, not a weekly spreadsheet. Interim: two digests, one filtered to each org list.
- **🔑 Free distribution win:** Report Builder reports carry a subscriber list and others can clone them. **Three Workday reviewers asked for more broadcast** (Felix Delval, Yanira, Razvan). Cheapest promotion-case move available.

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

### 🔵 BEFORE QUOTING ANY MCP NUMBER

- 🔴🔑 **PROVEN STALE 2026-08-16, NOT SUSPECTED — `Total tool calls (30d)` READS 95,898, BYTE-IDENTICAL TO THE 07-24 VALIDATED SET.** A rolling 30-day window cannot return the same digits three weeks apart. Tool-call data comes from the **manual AWS lookup**; request/org data comes from Splunk directly, which is why the Splunk-side panels moved and this one did not. **Every value-realization number in the board is the 07-24 vintage.** No refresh message from Jabran since 07-24, when he said he had not done one *"in last few weeks"*. **Ping him before pulling any number for the KR video, the Tina deck or the Bertrand weekly.**
- 🔴 **AND THE AUTOMATION THAT WOULD FIX IT IS DEAD WHILE READING `Done`.** `LOGREQ-16791` (onboard AEM MCP CloudWatch logs to Splunk) is **Status Done / Resolution Done, updated 08-06** — but its only comment is the LPT bot **auto-closing it as a process rejection**, *"This ticket has been closed — no automated provisioning will occur from it"*, because it was not filed through the DevHome portal. **Nobody re-submitted.** Re-file at https://devhome.corp.adobe.com/toolbox/discover/324036 or ask on `#splunk-users`. ⚠️ Its own description dates the last snapshot to **30 days to 2026-07-07**.
- ✅ **`correct:` 2026-08-16 — the Eli Lilly deep-dive gap WAS answered.** Jabran to Brian, in-thread: *"I can see it in the list ... could be a splunk loading delay ... can you please recheck?"* **Not a data gap, the blue-circle load delay.** ⚠️ Eli Lilly is in the OKR-review speaking notes, so let the panel finish loading before concluding anything about it.
- **Jabran, 07-24: 30-day window only** — *"a bug in some panels not respecting the time filter"*, fix promised *"next week"*. **Still no fix confirmation as of 08-16.**
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

### 🟡 JULY CARRY-OVERS (compressed 2026-08-31 — verbatim in `watches_ARCHIVE_2026-08.md`, grep `Second pass, same 2026-08-31`)

- 🔑 **Rendering surface, ball with Pedro.** Manish Bansal answered with the auth model (user-context). **Offer to write up the repeatable "skills that render actionable UI" guardrail** — the call carries the user's token not an over-privileging service token, the target service is allowlisted, audit. **The write-up is the land-grab, not the answer.** Pankaj Sangra still owes his end goal (preview vs interact vs act-on-page). `#aep-agent-orchestrator-collaboration` `C08U50NRA01`, cc Sorin + Eugene.
- ⚠️ **Three distinct capabilities, do not collapse them.** `#2300` in `Adobe-dxue/coworker-ui-experience` (PageUrl context NOT forwarded to Coworker; Mikaela Symanovich, no movement since 07-17) is Eugene's context-INTO-the-agent question, not Pankaj's inline render.
- ⏳ **Client-id / OBO — no direction concluded.** Carsten 08-13: *"none got to a final conclusion."* The gap is **one named check** (allow the caller only when it is Coworker, on the `act` claim), scoped to the AEM MCP servers, which Tanju calls straightforward. Options wiki `4003355459`; `GRANITE-70593` owns the fleet-level call. ⚠️ **There is no AEP-imposed "Wednesday deadline" — do not escalate on one.** Watch: does Ian's commentable proposal land, and does Coworker hold the re-push until the proxy is in place. Runbook → `Adobe-Experience-Platform/aep-ai/…/2026-0715-Governance-OBO-ClientID.md`.
- ⏳ **VW is the shaping test case** — co-innovation wants only Governance for specific people. Ian answered the per-AGENT half; **the per-PERSON half is unanswered.** And Wouter's Tokyo test never covered AEM end to end (env startup failures, not the client-id path).
- ⏳ **Pedro's own 07-24 list, unticked ≠ missed.** The UI-vulnerabilities POC thread (Eugene, Andres, Valentin, Ramon — names unresolved to handles) · push TBYB with Yanira · messages for Release Management (Razvan, surname unknown) · one co-innovation thread in `#aem-agent-owners-alignement` (subject TBD, ask Pedro). Draft only ([[feedback_never_send_slack]]).
- 🔵 **2026-11-01 — re-check the `aem-experience-catalyst` (excat) exclusion.** `recheck_after` in `aem-audits.yaml`, then re-run `scripts/publish.py`. It carries **61 skills** and is excluded from every audit because no manifest reaches it; **the day one does, every roster, naming count and collision number moves at once with nothing to announce it.** Flip `role: excluded` → `peer`.
- ⚠️ **Info, no action.** Cohort 1B criteria explicitly exclude AEM and the 7/30 final list is now unverifiable from where Pedro sits · Forms→Rubin port ~mid-Sept 2026, Forms usage invisible in reports until then · 2026-07-31 was code-complete for the panel, not availability, and **the EH-side plan built on "the rail ships 07-31" still needs re-dating.**

### 🔴 CAREER — MID-YEAR REVIEW (undated, the next real checkpoint)

- **⏳ Bertrand's mid-year review is pending.** Pedro has already told him he is aware of the AI-phrasing feedback. ⚠️ **Do not re-open that conversation backward** ([[feedback_dont_litigate_prior_replies]]). **What counts is evidence between now and the review.**
- **🔴 The AI-phrasing item is the symptom; the "good scribe" read is the damage.** Felix Meschberger doubts Pedro understands the topics he works on. **Plainer prose does not move that — one visible judgment per outward artifact does.** Watch for a Meschberger-facing moment where he takes a position and holds it.
- **🔴 Scope risk: Ramon proposed in writing that a Bucharest PM take over the release track.** Not hostile, but it sits in a record Bertrand reads. **Decide before the review whether to defend it or trade it deliberately — don't let silence decide.**
- **⏳ Depth was named by two of seven reviewers** (Meschberger; Valentin *"fewer initiatives, more depth"*). Coordination praise is universal; **depth is where the doubt clusters, and depth is the Senior Director marker.**
- **🟢 Bank these, they are manager-authored scope evidence in a permanent record.** Bertrand, unprompted, in Workday: the Coworker migration is *"a dependency for a lot of other teams, not just his own"*, and *"the reporting layer Pedro is building is becoming the thing the rest of us lean on to make good calls."*
- **🔴 Bertrand also wrote G1's work *"needs to be… redone for a large part given the move to Coworker."*** → the Rubin/definition port is the H2 G1 story, not insurance. **G3 got four words ("well noted") and no outcome comment. That asymmetry is where H2 gets allocated.**
- **⏳ One paragraph to reframe if it comes up** — *"I did not try to debate - what I did was to share as much informations as I collected"* **reads as the scribe posture in the first person.** The true version is a judgment: he declined the engine-topology fork and owned the customer-facing boundary, validated by Felix and Ian within the hour on 07-22.

### 🟡 STALENESS + SIZE FLAGS (refreshed 2026-09-03 at the System Review, Pedro's call on all of them)

- ✅ **System Review ran 2026-09-03** (H-008 killed, parked table back under cap at 6, two decisions scored). Next due **2026-10-01**.
- 🟢 **AAI Status & Todo archived 2026-09-03 on Pedro's go: 123K → 63.5K bytes, live note starts at Focus 08-13.** Still his: the Top 3 (flagged dead in place), the `Current Status` refresh (two stale claims named in the flag), two May-dated tasks under Scheduled (Next). 53 🔴 against 2 🟡 unchanged.
- ⚠️ **EH Status & Todo `Current Status`, fifth consecutive review, 14 weeks.** Six banners above it now say the same thing. A refresh, not an archive. Pedro's.
- ⚠️ **O1 / O2 KR notes untouched since 07-14** while the AAI Status carries Bertrand's Q2 line and the 28.5% Q3 figure; the roll-up is ahead of the detail.
- ⚠️ **Three predicted dates passed with no outcome captured:** the 08-26 all-hands AEM+Coworker segment, the 09-01 Developers Live session, the 08-14 weekly to Bertrand (unsent at 20 days).
- 🟢 `watches.md` compressed at this review (six pre-GA sections → one); repo memory healthy (AAI ~17K, EH ~18K, state ~10K).

### 📕 RESIDUALS OF THE CLOSED AUGUST SECTIONS (consolidated 2026-08-31 — six 📕 sections moved out; verbatim in `watches_ARCHIVE_2026-08.md`, grep `Verbatim snapshot appended 2026-08-31`)

- 📅 **2026-09-02 — the feature-parity plan for paying/SKU customers**, Pedro's own date in the Loni mail. ⚠️ UHG is named in it as on-hold and is already provisioned.
- 🔴 **`NXUI-1904` is the one GA blocker and AEM raised it** — mailto links prepended with the Unified Shell base URL. Reporter Yanira, screenshots Eugene, assignee Tim Lynn, PM Cole Connelly. `New`, zero comments, zero PRs. Ask for an owner and a date.
- 🔑 **`AEMAGT-2581` is the only cross-agent bug-bash finding and it is `Normal` and unassigned** — delete/cleanup unreliable across 3 of 4 surfaces. ⚠️ Both inventories confirm it by absence: no skill covers delete, cleanup or rollback.
- ⏳ **Tina Ngo still owes the Coworker-side documentation link**, structured by use case not by skill — Corey named documentation an unlisted GA gate. (Residual of the Developers Live watch, closed 09-02: the 08-24→09-01 webinar window has passed, incl. Corey + Brian's 09-01 session.)
- ⏳ **Keep Trent Davies's written agreement** on the MCP-gateway/ARB exception. The GA rests on it and it is not visible in Slack.
- ⏳ **Two prod-manifest residuals.** `prod/cx-coworker.yaml` still has no `api_configs`; the Showcase-scoped prod manifest was never built.
- ⏳ **Confirm the roadmap slide was actually edited** in `FY26 Q4 AEM Roadmap.pptx` (~slide 57). Closed verbally 08-15; the 08-17 document deadline passed unconfirmed. Links in [[project_experience_hub]].
- ⏳ **Suggested prompts in Coworker still unreconciled** — decision #3 of the 07-03 chat-entry note. Route Fu Chi (pipeline) + Zeus Courtois (AO2). EH-side.
- ⏳ **Still owed to Pedro:** Cole Connelly's AEM instance-selection outline · Ilya Grafutko's front-matter document link · Florin Florescu on whether the Dev Agent needs a Developer role · Marius Duta on which instance the EDA bash used.
- ⚠️ **Unsourced claims to fix before the deck travels again:** *"gapping 9 months of AI technologies"*, *"state of the art"*, `memory` as a named Coworker capability, `Create a new site` with no matching skill. And `Progressive rollout to all AEM customers` must read `all AEM Cloud Service customers`.
- ⚠️ **Two unverified public claims from 08-12 still open** — *"each agent team has run its own bug bash"* and *"we are running co-innovation projects and PODs with customers"*, against Ian Boston's 07-31 *"CoWorker is not enabled for AEM customers yet"*. Close them quietly rather than be corrected.
- ⏳ **The official name is `CX Enterprise Coworker`** — not "Adobe Coworker", not "CX-Coworker". Pedro mixes all three inside single drafts.
- ⏳ **Three from the 08-10 pre-call state:** the seven agent-map decisions only Pedro can take (51 of 88 skills with no agent, so no agent-cut number is publishable) · AI Ethics on EPA (*"team will evaluate end of Aug"*, after both 08-14 and 08-24) · `skill_inclusion_policy` rewards silence — zero manifests use it, absent defaults to `stable`, and every AEM skill declares `experimental`.
- ⏳ **`required_entitlements` — confirm Carsten's monorepo PR check landed**, and chase the teams that never answered.
- ⏳ **`aep-ai#10061`'s `deferred` on One AEM MCP** — does it travel to `cx-coworker`? Corey filed it GA-blocking. And 15 of 16 ported plugins are still unexercised.
- 🔵 **09-01 review input — the instrumentation candidate has two hits and one miss.** 08-15 he reproduced four AO-ops questions in a browser; 08-16 he answered Raul's entitlement question from his own audit output; 08-19 he asked Raul for a Gainsight contact while Huong Vu's written ask had sat 13 days in his own Slack. **Deliberately not parked** — cap full, all one programme.

## History (closed)

<!-- ✅-closed watches move here with close date; prune below ~10 lines -->
- 2026-08-24 — **Bertrand landed and picked the work straight up** (*"ca depile, ca depile"*). The 08-14 weekly never went; the 08-21 pre-read was the last thing he read.
- **2026-08-07** — file reshaped to the one-line rule (30.7K → ~10K tokens). Full prior content verbatim in `watches_ARCHIVE_2026-08.md`.
- 2026-08-06 — **Clint's 72-hour clock CLOSED.** Pedro answered 08-05 17:29 object-backed (62/63 manifest census, twelve CODEOWNERS lines); **Carsten answered the lifecycle question in 29 minutes after a week of silence.** Positive control for [[Say the Sentence That Obliges — the Hedge Transfers the Ask]]. Residuals kept above.
- 2026-08-06 — **KR 1e outcome resolved:** the video was never played, the meeting was derailed. Residuals kept above.
- 2026-08-03 — monthly System Review ran. H-007 resolved, parked cap enforced 15→2, decisions scored. **Next due 2026-09-01.**
- 2026-08-03 — the check-in was 2026-07-21; iA Writer track dead, Pedro's call. Authoritative goals = the submitted Workday version.
- 2026-08-03 — sections ≤ 2026-07-17 moved to `watches_ARCHIVE_2026-07.md`.
- 2026-08-03 — `.claude/memory-backups/20260702-pre-P1/` deleted, recoverability verified against git first.
