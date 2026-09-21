---
name: aem-agents-intelligence-aai-project-context
description: "Full context on the AEM Agents Intelligence project — agent reporting platform, AO 2.0 liaison, Loni+JM May 11 deck, three-tier reporting, agent ownership, AAI stakeholders. Sister file to project_experience_hub.md."
metadata: 
  node_type: memory
  type: project
  originSessionId: 5f12dcf1-db3b-44ce-bf6c-50e0a17cb9e9
---

> **Two-project split — Phase 2 structurally complete (2026-05-13).** AAI vault folder at `2026/AEM Agents Intelligence/AAI - Project Folder/`. Companion `project_experience_hub.md` covers EH. Meeting Notes moved to neutral `2026/Meeting Notes/` (2026-05-13). AI-Assistant legacy folder retired. No legacy folders remain.

> **📦 Archive discipline (weekly shards; last restructure 2026-07-01).** Old context lives in per-ISO-week shards `project_aem_agents_intelligence_ARCHIVE_<year>-W<wk>.md` (+ long-form reference in `..._ARCHIVE_reference.md`), mapped by `..._ARCHIVE_INDEX.md`. **To find old context: read the INDEX first (dates + topics per shard), then `rtk proxy grep` the shard — never full-Read a shard.** This active file = hot state (currently **the 2026-09-01 session**; 07-15 → 07-27 archived to W29/W30 on 08-03, the 08-03 sweep + Agent Owners Alignment to **W32a** on 08-04, the two 08-04 blocks to **W32b** on 08-06, the **08-04 CLINT + 08-05 ROLLOUT SYNC blocks to W32 on 08-07**, the **08-05 AUDIT REPO + 08-06/07 AUDITS-WENT-PUBLIC blocks to W32 on 08-10**, and the **08-25/26 COHORT block to W35 on 09-02**) + the compact durable reference below. ⚠️ **The archiver moves dated blocks but does NOT move RESUME pointers — check the pointer still resolves after every run.** **Cap rule, enforced by `scripts/archive_memory.py` (run in `/consolidate` Step 5): keep this file < ~20K tokens / one-shot-readable; event blocks older than ~2 weeks auto-archive to their weekly shard + the index rebuilds.**
>
> ⚠️ **"moving 0 block(s)" HAS TWO CAUSES — DIAGNOSE BEFORE ACTING (2026-08-07).** (1) **The layout invariant below is broken** → the archiver cannot see the blocks. That is a bug, fix it. (2) **Every dated block is newer than `RETENTION_DAYS = 7`** → there is genuinely nothing it may move yet, which is correct behaviour on a dense week. **Check which one you are in before "fixing" anything.** On 2026-08-07 the file sat at **23.5K against a 24K read cap with every block under 7 days old**, so the only lever was **writing the blocks shorter** — the largest was a single 3.4K-token event block, trimmed to 2.2K. 🔑 **On a dense week the cap is a writing constraint, not an archiving one.** ✅ A **SessionStart hook now warns** when any session-start file approaches the cap (`scripts/archive_memory.py --check-startup`, wired in `.claude/settings.json`) — added because both prior truncation incidents were discovered by accident, never by a warning.
>
> 🔴 **LAYOUT INVARIANT, learned the hard way 2026-08-04 — DATED EVENT BLOCKS MUST SIT ABOVE THE LIVING-REFERENCE SECTIONS.** `split_active()` in the archiver treats the first non-blockquoted `## ` heading as the start of the living reference and everything after it as unmovable. This file had drifted so that four dated `> ###` blocks sat *below* `## 2026 Yearly Goal — G1`, so the archiver saw **one** block (the protected RESUME) and reported *"moving 0 block(s)"* while the file sat at **29K tokens, 5K past the read cap** — i.e. **the cap guard reported success while the file was silently truncating at session start, which is the exact 2026-06 awareness-loss failure it was built to prevent.** Fixed by reordering (content-preserving, verified line-multiset-identical), after which the same script moved 29K → 19K on the first try. **When appending a new dated block, put it directly after the RESUME, never at the end of the file.**

> ## ▶️ RESUME HERE — left off **2026-09-18** (consolidated 2026-09-21, hygiene-plus: the 09-17 enablement recap-slide critique and the EH-MAU lookup, one short block directly below; the substantive 09-16 audit block follows it). 🔴 **The AEM panel is 09-24 now — Pedro's own 09-11 re-date (announce 09-24, TBYB activation the week after, SKU with panel 10-05) — and it wobbled again on 09-15 between release, enablement and the last Unified Shell slot. Settle it with Yanira.** ✅ **GA is live for more than 1,000 orgs since 09-15 (Cohort 3B, 980 in one day), still without the panel.** 🔴 **Unanswered and tagged to him: six opt-out Gainsight removals, Corey on Humana, Soumya's bug review, Tatyana's release list, Hemanta's Rubin question, Yanira's 09-15 DM** — [[watches]] 2026-09-16 section. The 2026-09-16 audit block is directly below, then the 09-02/03 block; the 09-01 and 08-27 blocks moved to shards W36 / W35b on 09-16 (read `..._ARCHIVE_INDEX.md`). Still his from 09-03: the Top 3 re-triage and the `Current Status` refresh in the AAI Status & Todo. Previous pointer text kept: 🔴 **AEM HAS NO PROMPT SURFACE ON THE MANIFEST THAT CARRIES ITS GA SKILLS.** 🔑 **Coworker's persistent-instruction layer is `.ao/prompts/system/` block directories, scoped per MANIFEST — and AEM's 18 GA plugins live in `cx-coworker.yaml`, which AEM does not own. So every AEM skill runs under `app/aep`, told it is an Adobe Experience Platform coworker.** The ask is written and the target is named (Shubham Lohiya). Full mechanism → [[reference_coworker_system_prompt_blocks]]. See the 2026-09-01 block directly under this; the 08-27 inventory work is in shard W35 (archived 2026-09-03).
>
> ### 🟡 2026-09-17/18 — THE ENABLEMENT RECAP SLIDE, AND THE EH MAU THAT DOES NOT EXIST
>
> **09-17, the tech enablement live session (Gina Miller MC, 17:00 CEST).** Pedro's closing slide, "AEM Agentic Capabilities - Recap", four lines: (1) the six use cases (Discovery, Content Optimization, Governance, Experience Production, Experience Modernization, Development); (2) "Access Via MCP (Direct AEM MCP, Coworker MCP), Adobe Surfaces"; (3) "One journey across AEM, AEP and AJO with CX Coworker – and more to come"; (4) "Learn more on AEM Agentic Capabilities and reach out to AEM teams". Critique given before the session, facts first ([[feedback_critique_check_facts_not_prose]]): "Coworker MCP" is not a thing (AEM MCP reached through Coworker); Experience Workspace absent although Tina relayed Loni's steer 09-10 to show all surfaces; "CX Coworker" is neither the internal nor the official name; line 4 names no doc, channel or demo org, which is exactly where the field stopped the week before (Vijay 09-09: SCs have only AEM Showcase JAPC, Coworker not enabled there; Ashok 09-08: is there a demo script). Four Development skills are out of GA since 09-08. ⚠️ **What actually went out is uncaptured** — debrief. The "One journey" line was his; the only edits were the span (Coworker out of the product list, no dash) per [[feedback_edit_the_span_not_the_artifact]] and [[feedback_pedro_writes_claude_critiques]].
>
> **09-18, "combien de MAU sur EH".** None on file. The only EH figure is 14,000 weekly users / 79% return, 2026-06-05, Guliz Sicotte's number; nothing newer in vault or memory after fifteen weeks; Grafana access still unconfirmed; the daily Rubin digest covers `aem*` skills on Coworker, not EH. Same finding as the 07-22 block in [[project_experience_hub]] — the measurement chain is still unplugged.
>
> ### 🔴🔑 2026-09-16 — THE SLACK AUDIT 09-03 → 09-16: THE PANEL MOVED TO 09-24, A THOUSAND ORGS WENT LIVE, AND SIX OPT-OUT TAGS SAT UNACKNOWLEDGED
>
> **📍 METHOD.** Four parallel readers on 18 channels plus Pedro's own pass on `<@me>` mentions (8 pages), `to:me` and 14 group DMs, window 09-03 → 09-16. The readers' reports lived in this session only; the durable facts are below. ⚠️ Two method notes banked in [[reference_slack_audit_channels]]: the epoch bound handed to the readers was a day off (compute it with `date -j`, never hand-convert), and the decisions again sat in DMs and group DMs, not channels.
>
> **🔑 THE PANEL DATE IS 09-24 NOW, AND PEDRO MOVED IT HIMSELF.** 09-11 15:12, group DM with Bertrand, Ian, Carsten, Jaclyn, Yanira: Ethos fix (`EON-73057`) on stage 09-24/25, prod mid/end October; Coworker UI workaround (Mikaela Symanovich — render the panel from the shell domain instead of the AEM domain) by 09-17; **AEM Panel GA announcement 09-21 → 09-24**, TBYB panel activation "the following Monday" (he wrote "Monday September 24th"; the Nick Whittenburg thread says ETA 09-28), **SKU customers with panel 10-05**. Rodson 09-11: only two Unified Shell releases left, 09-17 and 09-24, then RCP freeze for the rest of the year (Coworker-specific changes exempt, the shell is not). Bug bash panel 09-22/23 (Yanira). CF Editor ETA 09-23; Page Editor slipped to the ~10-13 Sites release. ⚠️ **09-15 22:12 → 22:57 the date wobbled again:** Mikaela proposed the prod release on 09-24, not the 09-22 bash; Yanira "from customer pov we would be fine with enablement Sep 28"; Mark Doten "doesn't match up with any releases; our last release is 9/24"; Yanira "we might need to pivot for Bug Bash… will sync with Pedro tomorrow". Release, activation and announcement are three events wearing one date — instance (2) of the parked [[Two Milestones Wearing One Word]].
>
> **📦 GA IS LIVE, AND THE NUMBERS.** Internal orgs 09-04 (Cohort AEM_1.1_INT, three in the first batch, Stephen Gould). **42 most-active TBYB orgs 09-08/09** (Cohort 2.1; Telefonica Germany ran the first skill). Pedro to Tina 09-09: "2 skills, 6 runs" after 20 hours, "feedback from internal is good but low too"; to Jaclyn: "no drama so far, low usage too". Coworker proposed "a couple hundred" for the next batch and Pedro agreed ("500 is a bit YOLO, but hey - low usage, TBYB - we need to widen the scope"); Paul's 3B list went 962 → 1,379 → 1,385 inside 24 hours, Yelena provisioned 1,326 then Namita said "include all". **09-14/15 Cohort 3B: Pedro's own post 09-15 17:22, "980 Orgs (AEM + TBYB) have been activated yesterday. Total now > 1,000 orgs enabled."** Yelena "the roll out completed" 20:31; sys-admin emails 09-16 02:57 except expired Promo SKU; Gainsight 3B segments live. Akin 09-14 on a shareable customer count: "100s at the moment and it will grow to thousands over the next month", not for external use. Pricing lines: 25 credits per prompt in trial (Corey), $20k unmetered six-month offer for new deals and no rate card before Q4 (Tina 09-03), Ken's three GTM tracks (TBYB 10k credits / trial license $20k / actual license), programmatic enablement via FI/SKU "by end of the month" (Ken 09-09).
>
> **🔴 WHAT WAS TAGGED TO PEDRO AND NOT ACKNOWLEDGED.** Six AEM-Gainsight removals on opt-outs (LG Electronics, BT Consumer, Lloyds, Nissan JPN, Securian, GM Financial) plus the 09-04 and 09-10 comms checklists and Lianne's 09-02 deployment ask — Huong Vu closed the AEP side every time, no AEM line in any thread; the only reply on record is 09-10 "checked, all good!" on the cohort-list review. Corey 09-10: Humana asked for cohort 1, not enabled, zero replies from anyone. Soumya Sharma 09-12 asked Pedro to review the AEM rows of the Sep-9 go-live report; unanswered, Yanira took it (new channel `#aem-coworker-activation-signals` `C0BRJRDG56J`, JIRA label `aem-cw-reported-bugs`, filter 737071; Pedro's 09-15 post lists 18 new bugs and 9 recurring). Tatyana's 09-10 release-review ask: zero replies ever. Namita's 09-03 VW/governance-coinnovation POC question: closed by Namita herself. Philippe's 09-03 "how are the others doing to test the side panel?" in Pedro's own thread: dead. Hemanta Gupta 09-07: Rubin has no bulk-export API, how do the reports migrate — unanswered. Instance of [[H2 Planning Visibility — Own the Narrative Before It Gets Written Without You]] and of the peer-window rule in [[feedback_response_window_for_exec_questions]].
>
> **🟢 WHAT HE DID ANSWER, same day, mostly in the owners channel and DMs:** Apoorva on Altria's rail view (Adrian Ciulea closed it: the old AIA panel plus the "Try Coworker" popup that shows on every non-Coworker instance); Vaibhav on Mission Square security docs (Ilya + Horia; Corey added the Field-readiness fact sheet); Apoorva on OneAEM MCP reach through Coworker (yes); Greg Klebus on Generali / `Cohort_AEM_2.2.2` ("next cohort, early/mid next week"); Felix on paying-customer GA math ("ETHOS or COWORKER FIX ETA+1w min"); Guliz on the misleading approval label; Cedric on notifying internal org owners; Carsten on AstraZeneca AMS enablement; Prashant Jain on the 950 orgs (announced; status column = Definitions > Actual Provision Date > Cohort > Orgs); Ashok on `Cohort_AEM_OPTOUT_Panel`; Shraddha on UPS. And the 09-11 recap in `#tmp-enable-ao-for-aem-customers` was the sentence that obliges: co-innovation in AEM ≠ PODs; HIPAA-ready is required for HIPAA-signed customers because AEMCS handles customer-generated data and is audited for it.
>
> **🔴 CO-INNOVATION ENABLEMENT IS A FIGHT IN THE OPEN.** `#tmp-enable-ao-for-aem-customers` `C0BSHAA3NEQ`, created 09-11 by Clint Goudie-Nice from a DM with Tim Lynn, Namita, Ken Russell, Horia, Stephen Gould, Shankari, Pedro and Grant Russell. Clint's 09-09 end-to-end write-up (route the org to the `aem-onboarding` manifest → per-customer user segment PR with CODEOWNERS approval → separate provisioning issue with business approval → manual UI flag via Tim Lynn) and his 09-11 line, "I'm feeling like the Coworker team does not want us to engage in putting AEM skills in coworker". Namita 09-11: Best Buy and Walmart under BAA, no enablement until Coworker is HIPAA-ready; Under Armour `No GenAI`; "We cannot have AEM randomly enabling customers without going through the official trial or pod." UPS asked to pause by email 09-04 (Corey), removed from 3B 09-14. Mechanism → [[reference_coworker_pods]] 2026-09-16 section. Instance of [[Govern a Consistency Layer Over Primitives You Don't Own]].
>
> **📦 FACTS BANKED.** Four skills pulled from GA over customer-git access from the sandbox — onboarding, troubleshooting, dispatcher, codeveloper (Sergiu Coman 09-08; DACI open). Internal AEM orgs moved from `aem-aia` onto the prod manifest (Carsten 09-14). From 09-23 a plugin update propagates only on a version bump (Mihai-razvan Dana 09-14); Carsten: bump on every change; Lénárd's `/release-prod` skill automates it. **OneAEM MCP is "AEM MCP" everywhere** (Tanju 09-11) → [[reference_mcp_terminology]]. Dedicated `aem-ams` manifest shipped for the AstraZeneca demo 09-09 (Akash Jain; Carsten: "honestly, I doubt that this will scale — but its the only mechanism that exists today"). Co-innovation process merged, EY first customer, `experimental` folder on the `cx-coworker` known-marketplace disabled by default (Felix 09-09). Gateway Stateless: AEM signed off 09-15, prod 09-21. **Tanju 09-15: the AEM MCP eval is capped near 50% by design** — discovery-first server, the eval scores only the first tool a turn picks, so always `lookup-api-spec`; Georgiana Copil asked for an issue on `q/cx-coworker-gateway`, no fix committed. Vitaly Tsaplin's multi-trial evals: root cause is two Coworker tool-calling modes with different naming (`mcp__AEM__read-api` vs `aem__read_api`, Tomas Ondrejka 09-11), Coworker fixed it, rerun pending 09-16 (`AEMAGT-2763`). Coworker chat context = min(400K platform cap, model window) − 18K, so Sonnet ≈182K and Opus ≈382K (Bertrand's bot 09-15). Peter Klassen answered Bertrand's 08-31 active-instance question on 09-07: consolidate into One AEM MCP, NLS makes choosing content sources obsolete — Pedro not in the thread. Tech enablement session 09-17 (Gina Miller MCs; dry run 09-10; Tina 09-15 "great feedback from the session today"). AEM Agentic Internal org `920B81666AA009DC0A495E1C@AdobeOrg` created 09-08/09, Coworker + panel activated, user groups "AEM Agentic Admins" and "AEM Agentic Authors - Bug Bash". Yanira: the owners channel's canvases are maxed, remove skill canvases 4+5+8 (now in wiki 4036529200); bug-bash wiki 4049438703. Workday engineer meeting 09-15 23:00 CEST with Tina → [[reference_customer_workday]].
>
> **📚 THE 09-04 → 09-11 WEEK, from the W37 journal (vault `2026/Journal/2026-W37-Journal.md`).** 09-09 OKR review KR1e speaking notes: GA stated as fact; active orgs 626 (−5.9%), users 1,634 (−2.6%), "orgs come back, users still don't"; **the MCP instrument switched to server-log operations (147,427 operations over four weeks to 09-06, 618 orgs, direct agent clients 58%) and was declared final to LT — the plant from [[migrate-leadership-from-a-volume-metric-to-a-value-metric-without-a-cliff]] is at cycle 1 for the third time**; interactions per user 3.4 (−23%) on the slide vs 3.7 on 08-17, unreconciled. Whether the slot was delivered is recorded nowhere. Rubin weekly to 09-08: 84 actives (+68%), 46 orgs, 453 interactions.
>
> **🔎 KNOWLEDGE (P6):** applied — [[H2 Planning Visibility — Own the Narrative Before It Gets Written Without You]] (the six opt-out tags) · [[Govern a Consistency Layer Over Primitives You Don't Own]] (co-innovation enablement inside Coworker's runbook) · [[Lead the Slide With the Honest Read of Your Own Metric, Not the Flattering Number]] and [[Raw Call Volume Is Mostly the Agent Talking to Itself — Classify Before You Headline]] (an eval that scores only the first tool pick) · [[An Undefined Gate Is a Date Nobody Can Give]] (panel 21 → 24 → 28) · [[Say the Sentence That Obliges — the Hedge Transfers the Ask]] (the 09-11 HIPAA recap, a positive case) · [[feedback_dont_audit_pedros_execution]]. **No new entry. Two parked candidates gained an instance** — `knowledge/hypotheses/parked.md`, judge at 10-01.
>
> ### 🔴 2026-09-02/03 — THE SLACK AUDIT: THIRTEEN UNANSWERED ASKS, FIVE CLOSED IN-SESSION, AND THREE TIMES SOMEONE ELSE SPOKE FOR AEM
>
> **📍 METHOD.** `to:me` + `<@me>` mentions + the group DMs, window 08-23 → 09-02. The high-value asks were again in DMs and group DMs, not channels. **Closed the same morning:** Alison Heimoz / Anuj Kapoor on OneAEM MCP docs → routed to Tanju Erinmez (after Alison wrote in public, `#aem-pm-techdoc-ops-all` 09-02 05:53, *"we have asked Pedro several times, but we have not had a response yet"*) · Felix Delval on AMS orgs marked out of scope → Pierre Tager asked for the AMS org list, Ashok Kumar on the shared org and unified shell vs `.io` · Mike Tilburg on per-user credit visibility (VW, Centene) → *"not possible today"* · Yanira's canvases → merge 4+5+7+8 into one wiki, *AEM Skill Selection Playbook* · Gerald Prendi's Enterprise Context UI PRs (#12300/#12301, Intuit SVP co-innovation) → Ken Russell took it, land on the incubator line, manifest targeting per user because Intuit has two pods.
>
> **🔴 STILL OPEN, WITH CLOCKS → all in [[watches]] 2026-09-02/03 section.** Lianne Ramos's Gainsight alert for the 09-08 cohort (asked for 09-02) · Yelena/Corey's `#12863` confirm and whether UPS moves off `aem-aia` (Corey: *"please confirm tomorrow"*) · Siddharth Sahni: **ABAC for Content Hub is live in prod (09-01)** and Philippe confirmed 09-02 *"ABAC work without the right panel"* → he wants his 34 orgs in early cohorts, ⚠️ while Pedro told Paul Midura 09-02 09:11 *"the SKU customers (any cohort with SKU) = shall not be before Panel is ready = late September at best"* · the field's AMS question (Stephanie, Commonwealth Bank AMS+Target/WF in Cohort 2; David Zepeda, Honeywell), Sophia Gray answered *"opt them out"* unconfirmed · Rodson's `?shell_aiChatEnabled=true` one-liner.
>
> **🔑 THREE TIMES THIS WEEK, A LATE REPLY WAS ANSWERED OVER.** Babu asked Pedro for a value-prop slide (08-31 15:29) → Bertrand answered at 20:00 with the Q4 roadmap deck and *"customer count is 0 because we have not started rolling out"*. Babu asked for a newsletter blurb on AEM skills (09-01 14:58, *"you there Pedro..."*) → **Tina Ngo wrote it at 00:37**, the paragraph that now describes AEM as *"the content system for brand and product truth"*. The AMS question → Sophia Gray. Each gap was hours. Instance logged into [[H2 Planning Visibility — Own the Narrative Before It Gets Written Without You]]; the response-window rule ([[feedback_response_window_for_exec_questions]]) applies to peers too.
>
> **📦 FACTS BANKED.** Carsten 09-02 09:35 → 11:46: **the Coworker prod manifest now points at the `prod` branch of `aem-aia-extensions`; `main` no longer affects production** — this is what the 08-31 pin / 09-01 un-pin was for. Felix 09-02 09:26: **Ethos Cluster Gateway does not support CORS on `author-pNNN-eNNN` domains, `EON-73057`**, blocks Coworker UI → backend calls from the panel in UE, next phase (paying customers), no Ethos commitment, `#ethos-cluster-gateway` unmonitored; Corey created `#aem-wildcard-cors-enablement` (`C0BTZS3APGF`, Sebastian-Filip Virtopeanu bridging, Mihai Matache: Contour ≥1.23 supports regex); Yanira points at the AEM–Ethos biweekly Friday call. Namita 08-31 asked AEM+WF to audit customer orgs on AEM-only manifests → Pedro: keep the co-innovation manifests, Namita agreed 09-02 04:43. Paul 09-01 21:18: **LG Uplus (`472883976A0E01D20A495CE8`) opted out late, removed from `Cohort_AEM_2.1_TBYB`**, to move to an Opt Out cohort in Pedro's file. Pedro posted Rubin access to the owners channel 09-02 11:03 (*filter by `aem*`*). Anjul, per Pedro's 08-28 DM to Bertrand: **wants 50 customers talking about AEM on Coworker at Summit 2027**. Tatyana 09-01: **09-10 September release review, list every AEM agent and Coworker integration on the release wiki**. Rachel/Raj/Eric's <2-min demo video + script was due 09-01, not visibly delivered (Babu got the `20260831 - AEM Coworker 01 - Experience Hub` demo links 08-31). Guliz's promised brand-governance/enterprise-context thread (08-28, *"next week"*) not opened. Emil Serban (role TBD, *"our skills"*) wants Rubin traces; login `access_denied`, then subscribed to the group and could not find the skill. The *"Andrea renamed the panel"* message does not exist in Slack: rail→panel was **Rodson 07-16**, *"everything needs to be called coworker"* was **Josh 07-08**.
>
> **📚 BERTRAND'S POSTS 08-24 → 08-31, the three still owed a reply.** 08-31 `#p42-architecture`: an *"active"* AEM instance under the Coworker prompt with a context switch like the EH left rail, Eugene tagged — **unanswered, and it is the instance picker Cole owes**. 08-28 `#aem-agentic-discovery`: a skill to push Coworker artefacts (Firefly MCP images) into Assets, only the bot answered. 08-31 `#coworker-pms-and-friends`: *"Sandbox"* in Coworker settings is misleading for AEM → Namita filed `coworker-ui-experience#4027` to remove it, Anirudh Verma on it. Also: 08-27 `#p42-architecture`, approval-state vs published as a first-class parameter on discover/retrieve/research, *"AEM the trusted context layer vs just another retrieval API"*; 08-31 five channels renamed `agent` → `agentic`, validated with Tina and Vaishnav Gorur.
>
> **🔎 KNOWLEDGE (P6):** **new entry** [[Three-Storey Test — Conversation / Intelligence / Governance, Rent the Brain but Own the Learning]] (commit `e59ac96`, from the *IA et Stratégie* video on Claude Force; applied: AEM owns governance, the learning loop sits in the harness, the exit signal is *where AEM customers arrive from*, which needs a surface-of-origin dimension in Rubin → Angela Han) · [[Govern a Consistency Layer Over Primitives You Don't Own]] (the `app/aem` prompt blocks on the shared GA manifest must be additions, never overrides — [[reference_coworker_system_prompt_blocks]] 09-02 section) · [[Definition Ownership Is the Moat on Shared Data Infrastructure]] · [[An Undefined Gate Is a Date Nobody Can Give]] (Lianne's Gainsight has a date; the placement question never got an answer, so the calendar answered it) · [[H2 Planning Visibility — Own the Narrative Before It Gets Written Without You]] (refined, three instances). Prompt audit for Fable 5.1 applied to skills/agents/CLAUDE.md, commit `e712731`.
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
