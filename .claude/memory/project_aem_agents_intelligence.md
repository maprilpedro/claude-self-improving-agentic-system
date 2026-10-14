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

> ## ▶️ RESUME HERE — left off **2026-10-14** (Slack check, block directly below: CXCO-230 contradiction, Havas ask, Pritom owns the access-control routing, two 09-22 watches closed. Then the 10-13 blocks.) _Previous:_ left off **2026-10-13** (back from PTO 09-28 → 10-12; block directly below: the PTO Slack audit, the SJ Champion Forum page, the Rubin legal hold, the follow-ups waiting on him. Then the 09-27 MCP read of the champions and the 09-25 champions block). 🔴 **SJ Champion Forum 10-20/21: session "Agentic Workflows" with Martin + Tina; vault page `AAI - Project Folder/AEM Champion Forum 2026 - San Jose.md` is the single home for links.** 🔴 **Rubin Chat Analysis is on legal hold since 09-25; Pedro has no access until the AEP Datalake onboarding is approved person by person.** Older resume line kept below for the 09-27 state.
>
> _Previous resume (09-27):_ left off **2026-09-27** (Coworker + MCP read of the champions, block directly below: Workday opted out over user-rights control, Ford waits for the panel, the "zero Coworker" champions are heavy on AEM MCP direct. Then the 09-25 champions block: 8 licensed champions incl. Ford, Workday, ServiceNow still on AOv1 with zero Coworker. ⚠️ Nothing captured from Slack after 09-22, the 09-24 prod release outcome is unknown; run an audit first. Then the 09-22 Slack audit block; then the 09-17/18 and 09-16 blocks). 🔴 **THE PANEL ACTIVATION HAS FOUR DATES. Pedro's own 09-16 post: prod 09-24, go/no-go 10-01, TBYB 10-05, SKU 10-12. Marius 09-22: 09-30 for go/no-go and TBYB. Mark Doten: 28th or 30th, unanswered. Paul Midura to the field: AEM held until 10-12. Loni holds 09-21 and her GA email is queued.** ✅ GA live for more than 1,000 orgs since 09-15, still without the panel. 🔴 **Unanswered and tagged to him: NWL Brands (three pings, escalated), nine Gainsight removals, three Yanira asks, Bertrand's Rubin split, Lénárd's prod regression** — [[watches]] 2026-09-22 section. The 09-02/03 audit block moved to shard W36 on 09-22 (consolidation); the 09-01 and 08-27 blocks went to W36 / W35b on 09-16 (read `..._ARCHIVE_INDEX.md`). Still his from 09-03: the Top 3 re-triage and the `Current Status` refresh in the AAI Status & Todo. Previous pointer text kept: 🔴 **AEM HAS NO PROMPT SURFACE ON THE MANIFEST THAT CARRIES ITS GA SKILLS.** 🔑 **Coworker's persistent-instruction layer is `.ao/prompts/system/` block directories, scoped per MANIFEST — and AEM's 18 GA plugins live in `cx-coworker.yaml`, which AEM does not own. So every AEM skill runs under `app/aep`, told it is an Adobe Experience Platform coworker.** The ask is written and the target is named (Shubham Lohiya). Full mechanism → [[reference_coworker_system_prompt_blocks]]. See the 2026-09-01 block directly under this; the 08-27 inventory work is in shard W35 (archived 2026-09-03).
>
> ### 🔴 2026-10-14 (capture) — NOBODY KNOWS HOW MANY AEM CUSTOMERS HAVE COWORKER: 37, 57, 811 OR 1,000+
> - Thread `C0AB9GHQRD2`, Ian Boston 2026-10-01 10:28: leadership wants AEM credits sold, credits used, and "% of customers with no usage that can use CoWorker (we have customers who cant due to their own Governance controls on their AEM Environments)". Bertrand: aep-insights dashboard, contact Shankar Muthan; Soumya Sharma "owns the Rubin dashboards". Yanira tagged Pedro "fyi"; **Pedro has not replied**.
> - **Four denominators:** aep-insights says **37** AEM customers have AI credits (Ian thought all ~1,800 did); Ian: "IIUC only **57** have access currently"; Shankar's view showed **811** using Coworker, Ian: "The data is wrong. We 100% do not have 811"; memory says GA for **1,000+** orgs since 09-15. ⚠️ **This is the base of the adoption plan's +20% and of the Loni slide 1. Do not put "1,000+ orgs" on a slide until one of these is reconciled.**
> - Why the data is wrong (Shankar): his tool sees AEP entitlements and `acp_ao`-provisioned orgs only, not credits added in the backend; rows with credits used > purchased (Jet2, Intuit). Shankar + Mukesh Jha moving the org/product data into the provisioning DB. Ian pushes DPaaS ("Adobe Governance approved"), offered to test with a sample; position, not a decision.
> - Ties: H-010b (attribution) as an internal ask, not a customer decision, so **not evidence**; not one of H-009's three signals (killed today, verdict stands). [[Raw Call Volume Is Mostly the Agent Talking to Itself — Classify Before You Headline]] (scope/window/basis: four counts, four bases). Pedro is still out of `#aep-coworker-core` (confirmed 10-14). https://cq-dev.slack.com/archives/C0AB9GHQRD2/p1790843332421809

> ### 🟢 2026-10-14 — ADOPTION PLAN FOR BERTRAND (brainstorm + grilling)
> - **Correction:** the AEM panel **shipped week of 10-06**; EH promo banner live; migrated SKU orgs get it by default. Local Rubin exports stop 09-25, so "migration had no effect" predates the panel.
> - **Target:** +20% weekly active **external** AEM Coworker users by end Nov, baseline = panel week. Pedro's wish x2, not written.
> - **Finding (Rubin Quality, VA7, hand-computed):** AEM resolved 54% vs Coworker 70%; org-permission blocks ~14% of AEM chats vs ~3% Coworker (**x4.5**); execution failures equal. Pedro's "25-30% end on permissions" = 30.77% of *unresolved*. Limit first: one region, ~112 chats.
> - **Ranked:** (1) permissions: **diagnose the 16 blocked chats first** once Rubin is back, then pick the fix with Corey (Sites) + Apoorva (Assets). Pedro 11:04: a start-of-skill rights check alone only moves the failure earlier; the 11-14 date was withdrawn; (2) value stories at SJ + Havas (UPS built its own skill, unnamed until Corey confirms; Corey's AEM→Workfront skill; Semrush); (3) org list to account teams after Legal + Yanira; (4) admin access = Pritom dependency, not in the +20%. Newell parked until Shubham answers.
> - Material: vault `AAI - Project Folder/Coworker AEM Adoption - Action Plan Material (2026-10-14).md`; Loni deck skeleton (Minto, 6 slides, ask on slide 6 OPEN) in `... - Loni Deck Structure (2026-10-14).md`. Pedro writes the plan, full version ~10-23.
> - ✅ **Sent to Bertrand ~11:12** (Claude edited Pedro's draft on his ask: 122→112, base of the x4.5 stated, limit first, "403" → "refused for lack of rights").
> - **Value, three sources (Pedro):** customers' own skills, third-party tools (Semrush), bulk actions. **His pick for SJ: own skills**, "customiser les workflows par client, par user presque". Bulk action has one candidate example only (Macy's 49 turns, CSV per folder), to read when Rubin is back; VC Brands is NOT one. Open tension Claude raised: per-customer skills vs the consistency layer he defends ([[Govern a Consistency Layer Over Primitives You Don't Own]]). Unanswered: what a champion should be able to do alone after SJ.
> - **🔎 KNOWLEDGE:** the 30.77%-of-unresolved read as "of chats" is the basis trap in [[Raw Call Volume Is Mostly the Agent Talking to Itself — Classify Before You Headline]] (scope/window/basis). +20% instead of x2 and "aims" = [[Lead the Slide With the Honest Read of Your Own Metric, Not the Flattering Number]]. Pedro's catch that a start-of-skill rights check only moves the failure = diagnose before the remedy. New **H-011** (blocked users don't return). Not H-010 evidence: in-chat AEM content rights ≠ admin access control.

> ### 🔴 2026-10-14 — SLACK CHECK: PEDRO'S "NOT BLOCKERS" LINE CONTRADICTED OVERNIGHT, HAVAS WANTS SJ DAY
> - **CXCO-230.** Pedro 10-13 16:52 `#cx-coworker-trial-rollout-core`: "the two PRs are not merged but they are not blockers for todays and next weeks activations" (confirmed with Yanira). Yelena 10-14 00:02: AEM rollout happened, next 10-20, PR not merged, "subset of customers using AEM Skills in Coworker will be blocked." Ian 10-06: CXCO-230 is the AEM Service Proxy PR that lets customers control traffic per environment (CDN rules with IP allow lists); needs a no-change-period exception. Unanswered at 09:46. https://adobe.enterprise.slack.com/archives/C0ABFLYLZK7/p1791928930767479
> - **Access control routing.** Kapil silent; Pritom Baruah answered 10-13 22:46 (Kapil and Mihai own it, outcomes + dates to come); Yanira: route such asks through Pritom. Pedro 10-14 09:25 stated the ask as admin controls access, "10+ large customers" blocked.
> - **Havas POP (Kevin Gerard-Moreau, Elise Lawley pointed to Pedro):** 30 min on Coworker for AEM Assets, with Workfront use cases, Tue 15:00 to 15:45 UK, ideally 10-20 (SJ). Unanswered.
> - **Yanira 10-13:** internal orgs sitting in AEM_SKU cohorts to go through the internal-org activation process (Paul, Yelena); Ashok Kumar parity tracking, Loni's ask, "EOM to restart". Pedro shared the opt-out grouping and the 7-day engagement (AEM Coworker WAU 304, AOv1 external 455 end August) in the Yanira+Tina group DM.
> - **Closed from 09-22:** NWL Brands (Siddharth's email route, Mohit Arora call, `ASSETS-78931`); Lénárd's webMCP regression (Mikaela's Unified Shell PR-12563, Corey tested OK). Still open: AEM per-plugin token budget pushes skill descriptions to name-only (Shubham). Gainsight step 6 still Pedro's in Sky, Merck, and Paul's ping.
> - **🔎 KNOWLEDGE:** CXCO-230 is an instance of [[Parallel Artifact Streams Diverge — Always Check the Latest Version]] at the level of status lines: the same fact reached the same channel twice with opposite values within eight hours, and per [[feedback_critique_check_facts_not_prose]] that is his exposure. Next time, lead with [[Surface the Risk Before Leadership Has to Ask]]. No new entry.

> ### 🔴 2026-10-13 (capture) — WHY CUSTOMERS OPT OUT OF COWORKER: SIX IN TEN ARE "NOT APPROVED INTERNALLY YET", ONE IN EIGHT WANT USER-LEVEL CONTROL
> - **Source.** List of captured opt-out reasons pasted by Pedro 10-13. Origin of the list not stated (likely the rollout opt-out tracker). 59 non-empty lines, two exact duplicates; the same customer may appear more than once.
> - **Breakdown (Claude's grouping, counts per line).**
>   - **Internal AI governance not done: 37.** Governance or AI-council approval 22 (incl. "not an approved AI tool", "AI Council approval", Mynavi "corporate guidelines prohibit GenAI"). Security or infosec review 8 (incl. Lumen, Esri "security clearance"). Legal or GenAI terms 4 (incl. CAG). Regulated or government 3 (GDMS, a government account, US Bank).
>   - **Want control over who or where: 7.** User-level permissions 6 (BofA, Merck "inability to restrict rollout based on user or group", one org asking to disable for non-admin users to protect the trial limit). Lower environment only 1, and BofA also asks for sandbox restriction.
>   - **Cost or commercial: 6.** RFP 2, price/SKU insight 1, Cochlear "authorise and understand our costs", credits/budget 2.
>   - **Contract confusion: 4.** GenAI rider unclear, promo SKU "by accident", auto opted into AO rider, licensed SKU but wants AIA removed.
>   - **Never enabled or wants AIA kept: 3.** Plus **other 2** (none given; lost key stakeholders).
> - **Bankable verbatims.** BofA: "eager to adopt Coworker … blocked by their security and governance requirements until either user-level permissions or sandbox restrictions for Coworker are available." US Bank: "Coworker was enabled in their production environment. It should not have been provisioned to them due to them being a regulated customer." Merck: "inability to restrict rollout based on user or group." Cochlear: "Adobe features that enabled us to authorise and understand our costs."
> - **Reading (inference).** The 37 are a process gap, not a feature gap: Coworker reached orgs before their AI governance saw it (default-on with opt-out, see [[reference_coworker_enablement]]). The 7 control asks map to access layer 2 (user) and to a missing environment layer. The 10-15 release covers layer 2 for new customers only, so BofA and Merck (existing) are not unblocked by it. Cost asks map to credit attribution, the Esri thread. US Bank is a provisioning error: a regulated org got Coworker despite the 3B "rider green only" filter.
> - **Knowledge.** Instance of [[Announce a Forced Surface Migration With an Opt-Out — the Refusals Come Back as Replies Instead of Escalations]] (entry extended 10-14). H-010 access-control arm now 3 named decisions (Workday, BofA, Merck), but control is only 7 of 59; judge at the System Review, not self-promoted. The two Rubin views and the weekly vs monthly AOv1 windows are instances of [[Success Definitions Must Be Agreed Before Metrics Are Scaled]].
> - **Esri discrepancy.** This list says Esri opted out for "security clearance" (per Oznur). Memory had Esri as a credit-attribution case ([[reference_customer_esri]]). Both can be true; do not quote one without the other.

> ### 🟡 2026-10-13 — TWO RUBIN VIEWS OF THE SAME WEEK DISAGREE ON SIZE AND ON DIRECTION
>
> Pedro's Report Builder subscription `sub-192` (aem*, "Commercial") says 576 WAU / 293 orgs / 3,445 interactions, all down WoW. The Rubin CX Enterprise Coworker dashboard (68 skill families) says 280 WAU / 171 orgs / 1.5K interactions, all up. Org-level numbers match exactly where an org uses one skill family (LGCNS 71/1, VC Brands 65, Macy's 49). Main causes: "Commercial" in the subscription keeps Adobe demo/internal/trial orgs, the dashboard customer view drops them; aem* prefix vs a hand-picked 68-family list; several sections of each report ignore the filters or the window; the 09-28/29 all-hands prod bug bash likely inflates the subscription's prior week. Newell Brands is the subscription's top external org and is absent from the dashboard. Neither headline is quotable to Bertrand or at SJ until scope, window and basis are pinned. Full table: `screenshots/20261013-rubin-reports-comparison.md`.
> - **AOv1 external baseline (added 10-13 from Pedro's 09-15 screenshots + portfolio briefing):** ~640 external orgs and ~1,650 users per rolling 4 weeks before the 09-08 migration (599 / 1,409 for ~Aug 17 to Sep 13; 562 / 1,258 for Aug 24 to Sep 20). Weekly external users ran ~450. Monthly ≈ 3x weekly, so compare Coworker only at the same window. Detail in `screenshots/20261013-rubin-reports-comparison.md`.
> - **🔎 KNOWLEDGE (P6):** [[Raw Call Volume Is Mostly the Agent Talking to Itself — Classify Before You Headline]], [[Lead the Slide With the Honest Read of Your Own Metric, Not the Flattering Number]]; org classification → [[reference_skyline_p42_orglist]]. No new entry.
>
> ### 🔴 2026-10-13 (capture) — WALMART: NAMED USERS ON COWORKER ARE MANUAL, A HANDFUL, AND GO THROUGH KEN'S JIRA
>
> Source: `#tmp-enable-ao-for-aem-customers` `C0BSHAA3NEQ`, thread 09-24 → 09-26 (https://adobe.enterprise.slack.com/archives/C0BSHAA3NEQ/p1790271325127159). Pedro not tagged. It is the thread Clint forwarded on 10-05 when he asked Pedro "can we do this or is this a no go".
> - **Jesse Rees 09-24:** Walmart US Marketing & Connect (`718637275BE995F60A495CD0@AdobeOrg`) met Clint and Shankari 08-04 for the Asset Sourcing Portal beta, which needs Coworker; user list sent 08-20; told 09-11 "HIPAA", which he got sales and legal to call inaccurate; no update since. Wants named users only, no announcement. "Otherwise I don't think Walmart can participate."
> - **Lianne Ramos:** "User-level access control isn't available yet (it's on the roadmap for later this year)." Trial = all users plus admin email plus in-product notice. "Coworker does not act as a backdoor", it respects app permissions. Named-user access exists in Customer Pods (Babu Ramaraj).
> - **Ken Russell 09-25 (position, then path):** named users only inside a pod; "Exception can be made for some strategic accounts, but it need to be kept small given the manual work involved", align with Horia. Then: "The provisioning intake form has been updated to include filing a Jira to get the unified shell locked down to n users. There's a path for select customers to have all users on GA functionality and select users on pre-GA functionality. You can follow this path for a handful of customers."
> - **Horia:** manual for now; the feature "is worked on by Kapil Gulshan Rohra. it's a very high priority".
> - **Shankari:** "Our customers are turning blue in the face waiting for access to coinnovation." Her real ask is two layers: Coworker on for the org, pre-GA skills for a few customers only.
> - **Decision (Lianne 09-26):** Walmart NOT on the trial; path = Ken's Jira. Whether it was filed or worked is not on record.
> - **Read for Pedro:** user-level access (the 10-15 release, new customers only, existing ones on a migration with no date per Mihai Fecioru 10-07/09) and per-customer pre-GA skill access are two objects. Ken's Jira covers both for a handful of accounts. `PLAT-290634` (admin-only skill selection) is a third, still unowned. Fifth access-control customer in five weeks (after VW/Centene, Esri, UHG/Capital Group, Infineon; Workday opted out over it).
> - **Pedro moved 10-13 09:57:** DM to Kapil (group DM `C0C8M97T0F7`), asking for doc + roadmap and how AEM can use it. Reply pending.
> - **🔎 KNOWLEDGE (P6):** H-010 (instance, arm (a)); [[Govern a Consistency Layer Over Primitives You Don't Own]]; [[reference_coworker_pods]]. **No new entry.**
>
> ### 🔴🔑 2026-10-13 — BACK FROM PTO: THE SJ FORUM IS LOCKED, RUBIN IS ON LEGAL HOLD, AND FOUR PEOPLE ARE WAITING
>
> Source: Slack audit 09-28 → 10-12 (five parallel readers, ~50 channels and DMs; mentions search was bot-noisy, coverage good not exhaustive) + direct reads of `#aemchampionforum2026` `C0C5CM7UB8F`, the Pedro/Martin/Tina group DM `C0C47KZA3EE`, Tina's session PDF and Martin's discovery docx.
> - **SJ AEM Champion Forum 10-20/21.** Our session renamed "Agentic Workflows" (Tatyana 10-06); agenda locked after Loni/Haresh sign-off, only title and format can move. Length unsettled: Martin read 45 min Wed (09-23), Tina's doc is a 60-min agenda. Martin submitted the session doc on the 09-29 deadline while Pedro was out; Tina rewrote it on Loni's feedback (10-01). Pre-work sent 10-07 (Jenna), Corey added Coworker homework 10-06. Separate Coworker session Tue 10-20 9:45-11:15 PT (Huong Vu, Risha Dewan); Tatyana asks to avoid overlap. Open: Brian's gap (no Coworker Sites content production in three days), Corey's 90-min ask unanswered, champion Coworker access unknown (SKU cohorts 10-13 and 10-20, the second lands on forum day). Not found: attendee list, travel budget approval, rehearsal date. **Vault page with every link: `AEM Champion Forum 2026 - San Jose.md` (AAI folder), linked from Status Focus 09-25 and State headline.**
> - **Martin Buergi, 10-01, privately:** the adoption problem is org-level, not user-level, "we won't be talking to the right people"; proposed "how is your org supporting / blocking you". Tina's final doc makes organizational blockers the most valuable signal. His 09-24 blockers: no trust, no prompt guidance, no skill-writing experience, on top of Pedro's (org-only user management, no per-user access, no token visibility).
> - **Rubin legal hold.** Coworker Legal put Chat Analysis / Investigate on hold 09-25. Angela Han 10-07: Chat Analysis users must request access; AEM side approves per person from wiki 4070164622 (AEP Datalake Onboarding); Yanira 10-08 "Still waiting on Legal, have escalated". Central route: events dataset request at aep-ao.pages.adobeitc.com. Confluence 401 on both wiki pages (VPN), so Pedro's row in the Provisioning table is unverified. Langfuse deprecated for the AI Quality Platform (ao-quality.adobe.io, org "AEP Quality VA7").
> - **Waiting on Pedro (10-12):** Dustin Christensen (UPS peak-season RO pause 11-01 → 01-11, who handles it, ticket or not; group DM `C0C6UD4G5V0`, "let me know asap"; pairs with Razvan's 09-28 UnderArmour/Best Buy ask). Tatyana (Nov/Dec/Jan release review dates; Nicu Melcioiu now owns the calendar). Mircea Salan (EH: Content AI nav item under Home, before Coworker). Clint (`C0BSHAA3NEQ`, 10-05: the 10-15 release gives user-level access management to new customers; existing customers need a migration, no date).
> - **Facts banked.** Coworker panel on prod 10-05. Opt-out wave 10-03/05 (US Bank, Macquarie, Qatar Airways, Humana, TIAA; Lloyds escalated legally). Sites Trial (the champions' org) missed webMCP tools until 10-09. UE webMCP tools still bypass brand control (Amy Zhao PR #482). Gateway deadline 10-21 for MCP servers bypassing it. Champion-ready stories: Air India (Content Create "much easier"), UPS built its own Coworker skill in ~2 min (Corey 10-11), Ford Forms ~500 new forms. Clifton Strengths results due 10-15. Bertrand wants "Crosswalk" out of skill names.
> - **🔎 KNOWLEDGE (P6):** instance of [[Removing Friction Is Not Enough — Agent Adoption Can Still Fail]] (Martin's org-level read) and H-010 (governance asks from Intuit, FSI clients; the 10-15 release is the first test of arm (a)). **No new entry.**
>
> ### 🔴🔑 2026-09-27 — ZERO COWORKER IS NOT ZERO AI: THE CHAMPIONS ARE ON MCP DIRECT, AND WORKDAY SAID NO OVER RIGHTS
>
> Sources: Rubin `aemcs-licensed-orgs-activity-2026-08-18_2026-09-24.csv` (23 licensed champions, internal+external mixed) + `~/Downloads/aem-mcp-all-2026-04-26-to-2026-09-20-explorer.html` (CloudWatch prod, 536K operations). Analysis under a one-case exception → [[feedback_claude_does_not_code]].
> - **Coworker (Rubin):** 7 real customers active, 40 interactions, ~9 users (Lumen 25, Qatar 5, JPMC, AbbVie, HKTB, T. Rowe, Sunstar); 4 partner sandboxes; 8 org-found-zero; 4 not in Rubin. Positive: regulated accounts trying it, ~40% page authoring, multi-product use (BNY, Qatar, JPMC). Depth still 1-2 users per org.
> - **Pedro 09-27: Ford migrates after the panel. Workday opted out: user-rights management** (who uses it, what it reaches, read/write) → [[reference_customer_workday]], first decision-grade instance of H-010.
> - **MCP, champions since W34:** Workday 714 (6,607 since June, Cursor), Sunstar 1,080, Ford 1,030 (Cursor/ChatGPT), HPE 247 (MS Copilot). Six champions silent on every channel.
> - **MCP global:** 17K → 47K ops/week W22 → W38; customer orgs 156 → 255/week. First-party (`exc_app`) customer ops, internal-looking names removed: 1.2K W36 → 3.3K W37 → 5.3K W38, orgs 72 → 87; share of customer ops 9% → 20%. ⚠️ `exc_app` = AIA + Coworker, not separable; `cx-coworker` client is ~nothing (832 total), do not count Coworker with it; Bayer + Dun & Bradstreet = 46% of W37-38; the explorer's "customer" segment includes Sites Internal, CXO Enablement Training LAB, We.Retail-Prod (two thirds of `exc_app` "customer" ops in W34).
> - **Framing Pedro can own:** big AEM customers already use AI on AEM; the question is which door, and for engineering-led customers Coworker has to say what it adds over Cursor + MCP, and let admins govern it. Nothing drafted.
> - **🔎 KNOWLEDGE (P6):** [[Lead the Slide With the Honest Read of Your Own Metric, Not the Flattering Number]], [[Raw Call Volume Is Mostly the Agent Talking to Itself — Classify Before You Headline]]. H-010 updated. No new entry.
>
> ### 🔴 2026-09-25 — THE AEM CHAMPIONS LIST: THE BIGGEST AOv1 USERS HAVE NOT MOVED TO COWORKER
>
> Pedro pasted 40 accounts (the 2026 AEM Champions, the SJ 10-20/22 audience per the file name he chose) and asked who is active. Workbook `~/Downloads/2026 AEM Champions Licence and Usage.xlsx` (5 sheets: summary, AOv1 by org with IMS IDs, Coworker by skill, AEMCS licensed list, caveats). Sources: AOv1 DB 01-01 → 09-21 ([[reference_local_data_repos]]) + his two Rubin CSVs 08-18 → 09-24.
> - **13 champions on both AOv1 and Coworker**, all small on Coworker: Lumen 25, BNY 12, everyone else ≤ 8.
> - **🔴 8 licensed champions still active on AOv1 since 08-18 with zero on Coworker:** Ford (31 since 08-18, 546 YTD, 133 users), ServiceNow 19, Workday 12, Pitney Bowes 10, Wipro 9, Prudential 7, HPE 6, City National Bank 1 (+ Genentech 1, parent Roche active on Coworker). **The heaviest AOv1 users are the ones not migrated.** The push list before SJ.
> - **BNY and Fanatics active on Coworker but absent from the AEMCS licensed list.** 7 accounts show nothing anywhere (DX-ROI, Truist, International Motors, ecx.io, Meticulous Digital, NETBIIS, Cyber64).
> - ⚠️ Unconfirmed matches: Blue Acorn iCi = Infosys sandboxes; ecx.io = IBM iX DACH (not counted); Prudential do Brasil / Distribution / Holdings excluded as Prudential plc. Lumen is `CenturyLink` in AOv1 (same IMS ID). Rubin has no org for Wipro, Pitney Bowes, TechDivision, which AOv1 has.
> - Claude first said "no access" without checking the local repos; Pedro corrected it. Code built under a one-case exception → [[feedback_claude_does_not_code]].
> - **🔎 KNOWLEDGE (P6):** instance of [[Lead the Slide With the Honest Read of Your Own Metric, Not the Flattering Number]] (Coworker WAU growth vs the champions who have not moved) and [[Removing Friction Is Not Enough — Agent Adoption Can Still Fail]]. H-009 not logged (the 08-03 restriction: only the three named signals count). **No new entry.**
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
