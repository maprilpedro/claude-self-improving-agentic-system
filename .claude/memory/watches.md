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

## Open — cross-cutting

- 🔁 **EVERY TUESDAY · weekly update to Bertrand (Pedro's routine, set 2026-10-13).** At Tuesday session start, surface it and pull the week's facts (dates and numbers checked) from memory. Five lines: one concrete win, one choice he made, one risk or ask with an owner, what moves next week. Goes out even incomplete. Pedro writes, Claude checks facts, never sends. Why and format: vault `Career/Gallup Call to Action.md`, [[user_cliftonstrengths]], [[feedback_bertrand_status_comms]].
- 🟡 **Calibration #9, Pedro: pending.** What he changed in the RBI reply and the Aditi email before sending (10-28). **Asked once 10-28 ~12:48 (recall); do not ask again.** If he pastes the sent versions, log the diffs in [[feedback_draft_in_pedros_voice]]. Aditi half: sent text pasted 13:14 (in [[project_aem_agents_intelligence]] 10-28 block), but the Claude draft was not kept, so no diff is possible. RBI half still pending.

> 🗂️ **Grouped by project since 2026-10-28** (Pedro's four projects: Coworker Lead, Experience Hub, Release Management, Security Health). Inside each project, dated sections stay newest first; lines moved out of a mixed section keep their text and sit under a "From <date>" sub-heading. Cross-cutting items (career, staleness) sit at the end. A new watch goes under the project that owns it.

## 🚀 Coworker Lead

### 🆕 2026-10-28 — USAGE STORIES + ROADMAP LINE (full read: [[project_aem_agents_intelligence]] 2026-10-28 blocks; the RBI lines of this section moved to Release Management)

- ✅ **CLOSED 10-28 · Coworker foundation roadmap line: Pedro keeps the distributed model** ("je garde ma position, mais je comprends le problème"). No note to Bertrand. The visibility problem stays open: Coworker coordination needs a slot in his own H1'27 goals, not in the product roadmap.
- 📅 **10-29 · Aditi's answer to Pedro's biweekly AEM usage-stories proposal** (email 10-28, Bertrand cc). Then **Wed 11-11 · first 2-3 stories to Bertrand**; confirm Pedro can see Rubin per-org numbers before then. **Before every batch, read the vault note `Coworker Lead - Project Folder/AEM Coworker Usage Stories Findings.md`** (template, checks, candidates, run log; created 10-28). ⚠️ Confirm with Yanira that quoting chat content fits Legal's approved uses (#1/#2), not the pending "chat analysis" bucket. → [[project_aem_agents_intelligence]] 2026-10-28 block.
- 🟡 **Rachel's answer to Bertrand: where the Slalom quote came from, and product attribution in her newsletter prompt.** Same email thread.
- 🔴 **Bertrand 10-28 (reply to Pedro's proposal): is the Slalom usage prod or non prod?** Prod = program 90156 (https://aemcs-workspace.adobe.com/customer/program/90156#domainNames), sandbox = `slalompartnersandboxamericas`. Answer found 10-28 13:18: the live usage is the customer org SLALOM LLC (22-30 interactions a day), the sandbox stopped after 09-15. Pedro owes the reply (he wrote "checking which org they use"). ✅ Verified 13:24: program 90156 = SLALOM LLC (`5EF652E25570B5E77F000101@AdobeOrg`), so the answer is prod. Next check: the reply went out.

### 🆕 2026-10-27 — BERTRAND 1-1 (full read: [[project_aem_agents_intelligence]] 2026-10-27 Bertrand block)

- 📅 **~10-30 · Tina on the Coworker rate card, and AEM in the discussion.** Cost per operation instead of 25 credits per prompt; Bertrand worried it moves without AEM while Sites pricing is redone. Tina 10-28 `#aem-agentic` to Apoorva: official per-level pricing on Field Readiness, updated pricing not before Q1.
- 📅 **~11-03 · Demo Hub with Gina Casagrande** (she runs it): the AEM row claims a demo video, script and clickable demo that do not exist. Two scenarios needed (existing customers, new customers on Experience Workspace), Bertrand with Mark Szulc (probable). Docs side: Guillaume Carlino, "on en reparle semaine prochaine" (10-27).
- 🟡 **Manas is leaving** (Bertrand, verbal, 10-27; no public announcement found 10-28, do not repeat it as fact). Watch for the announcement, then who inherits his Coworker scope and the CXCO reviews (Yanira 10-21: merged before 11-01). Pedro works with Trent meanwhile.

### 🆕 2026-10-27 — COWORKER PERSISTENT INSTRUCTIONS, RAUL FIRST (full read: [[reference_coworker_system_prompt_blocks]] 2026-10-27 block)

- ✅ **CLOSED 10-27 13:10 · Raul answered three minutes later: Herbie only.** "Ask was Herbie specific - and the changes mentioned by Sebastian are for Herbie - the problem there is that the initial prompts were targeted to solve only AIF issues (Herbie being an agent for internal use-cases only)". No joint ask. The Trent ask is AEM-only, with Herbie's per-team instruction file as the precedent. DM: https://adobe.enterprise.slack.com/archives/D02DQLX6TAL/p1793102822364299. Vault note `AO 2.0/Coworker Persistent Instructions Status.md`.
- 📅 **~10-31 · Trent Davies DM, then the architects heads-up.** Not in Slack as of 10-28 09:30 CET. At next session start, search Slack for it (do not ask Pedro). Once sent: Trent's answer ~3 days later, then Pedro's reply in his 09-02 thread with "Also send to channel" (https://adobe.enterprise.slack.com/archives/C09KKLW1N86/p1788350207699419).
- 🟡 **Felix Delval → Lénárd Palkó, unanswered since 10-14:** "do we have tools to choose a different manifest for a particular UI?" (https://adobe.enterprise.slack.com/archives/C09KKLW1N86/p1791986083941449). The answer decides both Felix's skills ask and Pedro's instructions ask.

### 🆕 2026-10-27 — SUMMIT 2027 LABS CANVAS (full read: [[project_aem_agents_intelligence]] 2026-10-27 block)

- 📅 **~11-03 · Summit 2027 labs, Bertrand's canvas** (https://adobe.enterprise.slack.com/docs/T02CAQ0B2/F0CAF0U4V43). Which of the four went into Ron Nagy's form (deadline 10-26), did Lab 1 + Lab 2 merge, what Bertrand's team meeting kept. Labs 3 and 4 demo Coworker skills: check they are on track for GA before Summit.
- 🟡 **Summit 2027 speaker sessions call not open** (Mike Stiles `#summit-questions` 10-22). When it opens, Pedro decides whether to propose a session. Nothing of his on the canvas today.

### 🆕 2026-10-23 — MCP SECURITY FAQ (full read: [[project_aem_agents_intelligence]] 2026-10-23 block; the left-nav line moved to Experience Hub)

- 📅 **~10-30 · AEM MCP Server security FAQ with Product Legal** (Ellis, "later next week", Emily 10-23). Then check it is published on Field Readiness. Group DM `C0BUE8GE754`.

### 🆕 2026-10-22 — COWORKER SKILLS BETA FOR AEM (full read: [[project_aem_agents_intelligence]] 2026-10-22 block; the H1'27 canvas and Eugene lines moved to Experience Hub)

- 📅 **~10-26 · Pedro's AEM-side answer on Namita's `AEM Skills Beta Program` proposal** (which beta skills first, which customers and users, who keeps the user list), committed in his 10-22 reply-all if the sent text kept the date. Also check Mihai and Ken's manifest + segments setup landed ("a couple of days").
- 🟡 **Coworker coordination roles with Shankari.** Settle who does what in a call, Bertrand told first. Next time she convenes Coworker people, check Pedro is on the invite.

### 🆕 2026-10-20 — SJ SESSION "AGENTIC WORKFLOWS" (transcript in vault `Meeting Notes/AEM Champion Forum 2026/`; summary + 21 improvement asks with counts in the vault note `2026 AEM Champion Forum Feedback`, follow-ups on the SJ page; ingested 10-21)

- 📅 **~11-03 · Tina's categorized readout to the champions** (promised "two weeks" in the room). The improvement table in the vault note `2026 AEM Champion Forum Feedback` is the input (moved off the SJ page 10-21). Check it went out and that the non-bug items have a named owner.
- 🔴 **End of November · per-user Coworker access via Admin Console profiles was promised to the room.** The M1 plan (10-14) calls the same window "Tentative / Not Confirmed" (Wave B 2-23 Nov). **Pedro to Bertrand 10-27: "j'ai plutôt l'impression que ça va être janvier l'année prochaine."** If it moves, Kedar's and Dianne Eveler's orgs heard the date; tell the champions before they find out.
- 🟡 **Share the per-user Rubin usage dashboard with the champions** (Tina in the room, answering Jineet Vora: "we should probably share it with you"). Same artifact Bertrand handed Pierre Tager for Esri. Owner unassigned.
- 🟡 **H-010a candidates, not logged:** Dianne Eveler's org has Coworker disabled (regulated financial services, guardrails), Kedar will not open it to authors without profile-level control. Grade at the ingest, not here.

### 🆕🔴 2026-10-19 — DAY BEFORE SJ (full read: [[project_aem_agents_intelligence]] 2026-10-15 → 10-19 block)

- 🔴 **Before the KR1e slide ships · Mike Tilburg: where does the live-pages jump come from** (36,995 on 10-08 per Timothee → 72,086 in growth-lab W42, one extra Go Live customer, importer reworked 10-15). Until confirmed, say "20 customers live, up from 13", not "x5.5".
- 📅 **~10-19/20 · Tanju's W41 + W42 MCP Adoption Report** in `#aem-mcp` (biweekly, Sunday evening). Refresh the KR1e MCP block; check Workday / Ford / HPE are still in the org list. Link → [[reference_splunk_mcp]].
- ~~🔴 **Before 10-20 · SJ challenge, Pedro's yes/no on Q1-Q5**~~ ✅ Session held 10-20. Q5 (a vote on the one blocker) did not happen, the organizer closed the session; readout owner is Tina. See the 2026-10-20 section above.
- 🟡 **Open since 10-15/16, unanswered by Pedro as far as seen:** Felix on UPS manifest PRs #14609 / #19835; ~~Yanira's Workfront approval of the Security doc~~ ✅ 10-23 Pedro approved the AEM MCP Server security FAQ in Workfront (screenshot 14:11, group DM `C0BUE8GE754`); Emily Cohen 14:42 "Pedro. You're it and we go to product legal", Joe Stewart's pending slot was a mix-up (Yanira 10-24: "From PMM side it is Tina"); Caitlin Cody (VCP demo recording); Gina's Tech Insiders page to forward; Ellis's narrower Rubin access proposal; Horia ping on access control (Corey "push HARD").
- 🔴 **Tonia Hashimoto (Director, Associate General Counsel, NOT VP) 10-19 20:13, "Coworker Chat Access for AEM" email, Bertrand cc'd: asks what Loni's request is.** Legal approved 10-16 (Ellen Wong) use #1 usage/adoption reporting + #2 troubleshooting of customer-identified issues; Nick = product-improvement tagged data only; "quality / chat analysis" uses pending, need more info. Ellen updated wiki 10-19, Yanira moving approved users to PR (Ilya). Pedro's 10-19 16:48 "legal hold 3 weeks+ … asap" reads against that. Pedro to reply with Loni's actual ask + the pending gap. ✅ Loni's ask found in the 10-19 KR review transcript: "I'd like to talk to legal… unblocked by end of October".
- ✅ **2026-10-20 ~16:00 · Legal approved Pedro's ask** (after Tonia + Carla): #1 and #2 for everyone on the wiki + new users for #1/#2 only; Loni meeting cancelled; a streamlined approval workflow to follow. Loni's end-October deadline met early. Still open: quality / chat analysis uses (adoption plan action 1 may sit there), Loni's broader customer-content topic. Next: Yanira submits the PR to Ilya; tell Corey. (Loni + Bertrand were in CC of the Legal thread, no extra line needed, Pedro 10-28.)
- ~~🔴 **End of October · Rubin access unblocked (Loni's deadline, KR review 10-19).**~~ 🟡 Brian + Ian own AEM-side customer data handling (Loni's assignment); watch whether Pedro has a role in it. Reading the 16 blocked chats (adoption plan action 1) is likely in the PENDING bucket, not #2.
- 🟡 **Loni deck · which Rubin view is the measure (280 dashboard vs 576 subscription): ask Soumya;** confirm when Rubin access is back (~10-20). Slide 6 = B (Pedro 10-16).

### 🆕🔴 2026-10-13 — BACK FROM PTO (full read: [[project_aem_agents_intelligence]] 2026-10-13 block; SJ links live in the vault page `AEM Champion Forum 2026 - San Jose.md`; the UPS, Tatyana, Content AI and left-nav lines moved to their projects)

- 🟡 **Rubin access: Pedro requested it via the AEP Datalake onboarding wiki 10-13 (4070164622).** ➡️ 10-20 Legal approved #1/#2 for everyone on the wiki, so Pedro's own access should follow the PR to Ilya (assumes he is listed; check the wiki). Approval is per person by Legal; Yanira escalated 10-08. ⏳ Events dataset request (aep-ao.pages.adobeitc.com) not confirmed. Check approval by 10-16, or no Chat Analysis for SJ; if silent, ping Angela Han / Yanira.
- 🟡 **10-15 · Clint (10-05): access management answer, Pedro's call 10-13: waits for Kapil's reply, then answers** (10-15 release = new customers; existing = migration, no date; interim = Ken's Jira path, a handful of accounts). https://adobe.enterprise.slack.com/archives/C0BSHAA3NEQ/p1791214990969299 · Walmart thread (capture 10-13): https://adobe.enterprise.slack.com/archives/C0BSHAA3NEQ/p1790271325127159 · ⏳ Walmart Jira filed? Mihai Fecioru migration-plan ETA (Corey asked 10-09, no answer).
- 🟡 **10-15 · Coworker release: does user-level access reach existing customers?** If not, BofA and Merck (opted out on control, 10-13 list) stay blocked. ✅ Opt-out list source (Pedro 10-14): the Coworker team's Excel of customer responses. → AAI memory 10-13 opt-out block.
- 🟡 **Kapil: no reply, but Pritom Baruah answered 10-13 22:46** (Kapil and Mihai own the stream, "we will share the outcomes… when to expect what"; Yanira: such asks route through Pritom). Pedro 10-14 09:25: his ask = admin controls access, "10+ large customers" blocked. ⏳ Pritom's outcome + date. https://adobe.enterprise.slack.com/archives/C0C8M97T0F7
- 📅 **10-15 · Clifton Strengths results to Angela/Valentin** (asked for 10-07). ✅ Closed 10-13: results in hand; Pedro says Angela/Valentin already have access (admin), nothing to send. · **10-15 · Coworker user-level access release** (H-010 arm (a) test). · **10-15 · push the 8 zero-Coworker champions.**
- 📅 **Before 10-20 · SJ session: settle 45 vs 60 min against the official agenda; answer Corey's 90-min ask; cover Brian's Coworker content-production gap; check champion Coworker access (SKU cohorts 10-13 / 10-20); avoid overlap with Huong/Risha's Tue Coworker session.** Attendee list, budget approval and rehearsal date still unknown.
- 📅 **10-19 · re-run the champions workbook after SKU activation.** · **10-21 · Gateway deadline for MCP servers bypassing it.**
- 🔴 **CXCO-230 contradiction.** Pedro 10-13 16:52 in `#cx-coworker-trial-rollout-core`: the two PRs are "not blockers". Yelena 10-14 00:02: AEM rollout done, next 10-20, PR not merged, "subset of customers using AEM Skills in Coworker will be blocked". Ian 10-06: needs a no-change-period exception. No reply in her thread. https://adobe.enterprise.slack.com/archives/C0ABFLYLZK7/p1791928930767479
- 🔴 **Havas POP (Kevin Gerard-Moreau 10-13): 30 min Coworker for AEM Assets, Tue 15:00 UK, ideally 10-20 = SJ day.** Unanswered. https://adobe.enterprise.slack.com/archives/C0C8R2FDD2R/p1791904909473219
- 🟡 **Internal orgs in AEM_SKU cohorts (Yanira 10-13 18:30):** Paul/Yelena want them through the internal-org activation process; to discuss. Also Ashok Kumar parity tracking (Loni's ask), "EOM to restart". · Florin 10-13: Rubin "563 orgs used Cloud Manager skills"; Pedro 10-14 flagged orgs > interactions as suspicious, to recheck once Rubin access lands. · Nicu: Norfolk meeting today 10-14.
- 📅 **Adoption plan (10-14):** ✅ x4.5 message SENT to Bertrand 10-14 ~11:12 (VA7, 112 chats, 14% vs 3%, 16 blocked chats to read, full plan ~10-23) → watch his reply; full plan ~10-23; Pedro's pings to Shubham (Newell), Corey (UPS naming), Pritom (access date); action 1 = read the 16 blocked AEM chats once Rubin is back (~10-20), then fix with Corey + Apoorva (11-14 date withdrawn). Same Rubin pass: read the Macy's 49-turn chat (bulk-action value test). → AAI memory 10-14 adoption block + vault note.
- 🔴 **Before 10-23 (full plan) · the AEM-Coworker denominator: 37 (aep-insights credits) / 57 (Ian) / 811 (Shankar, "wrong") / 1,000+ (GA).** Reconcile with Shankar Muthan or Soumya Sharma before any slide carries an org count. Yanira's 10-01 "fyi" tag to Pedro unanswered. https://cq-dev.slack.com/archives/C0AB9GHQRD2/p1790843332421809
- ✅ **System Review done 2026-10-14** (next 11-02). ~~System Review overdue since 10-01~~ — Pedro's call; recommended after SJ.

### 🆕🔴 2026-09-22 — AFTER THE 09-16 → 09-22 SLACK AUDIT (full read: [[project_aem_agents_intelligence]] 2026-09-22 block; supersedes the 09-16 section, closed items in the 📕 list below; the EH and Fred lines moved to their projects)

- 🔴 **FOUR DATES FOR ONE PANEL ACTIVATION. Reconcile before Loni's GA email goes out** (Yanira asked Tina 09-22 02:42 when it ships). Pedro 09-16 owners post: prod 09-24 · go/no-go THU 10-01 · TBYB 10-05 · SKU 10-12. Marius 09-22: go/no-go + INT/TBYB **09-30** · SKU 10-12. Mark Doten 09-16: "can't release in october w/o an exception… can we target the 28th or 30th?" (Yanira ↑ to Pedro, no reply) then "2 more shell releases, 9/24 and 9/30". Paul Midura 09-21 to the field: AEM held until **10-12**, script says "targeting Oct 2026 for the right-rail". Loni still holds 09-21. https://adobe.enterprise.slack.com/archives/C0BTZS3APGF/p1789574823757829?thread_ts=1789484984.583589 · Marius: `#aem-agentic-development-management` 09-22 10:10
- ✅ **NWL Brands — closed for Pedro (checked 10-14).** Siddharth rerouted to `cx-coworker-questions@`, activation request submitted, customer call with Mohit Arora, tracked in `ASSETS-78931`. Nothing owed. https://adobe.enterprise.slack.com/archives/C06K2E373SA/p1789658825330199?thread_ts=1789390963.162599
- 🔴 **Nine AEM-Gainsight removal tags, still zero AEM lines (rechecked 10-14).** Sky, Merck, and the Paul Midura ping: every other step is struck through, Pedro's step 6 is the only one left open besides WF. One line saying Huong's removal covers AEM closes all nine. https://adobe.enterprise.slack.com/archives/C0ABFLYLZK7/p1789754766828449 · p1789757343079309 · p1789574705290839
- 🔴 **Yanira, three asks this week without a reply:** 09-21 signals "who owns investigating *No AEM skill invoked*" (Carsten answered, Pedro didn't) https://adobe.enterprise.slack.com/archives/C0BRJRDG56J/p1789988284861769 · 09-22 03:12 owners report + two feedback questions (Marius answered) https://adobe.enterprise.slack.com/archives/C0BARAMM89Z/p1790039529797229 · 09-22 03:53 DM: review co-innovation slides 7-9 and send her the 4-pillars timeline slide; add panel doc updates to `CQDOC-24021`.
- 🔴 **Bertrand 09-22 11:23 DM: Soumya's go-live report separates real customers from internal, so the Rubin report can too.** His implicit ask is the internal/external split Pedro said 09-16 was "pas encore possible". https://adobe.enterprise.slack.com/archives/DQ6H0AV7H/p1790068992635049
- ✅ **Lénárd webMCP regression — fixed (checked 10-14).** Mikaela removed DOM webMCP tools from immersive Coworker (Unified Shell PR-12563), shipped to prod, Corey tested "all good its working". Open side item: AEM blows its per-plugin token budget, so skill descriptions drop to name-only (Shubham). https://adobe.enterprise.slack.com/archives/C0AMKB79AJX/p1790065419467739
- 🟡 Gina 09-21: folder preference before her recap email; recording + ALM link in the planning channel. 🟡 Namita 09-18 tagged Pedro+Tina for AEM Coworker demo assets (Anagha Gala), none surfaced. 🟡 Brian 09-18 "can we add new skills for the current GA rollout" — no reply. 🟡 Marius/Emil: onboard AEM Agentic Internal's two programs to RO? Pedro's own 09-21 counter-question is unanswered. 🟡 Fabian Lotz (Infineon) credit-consumption precision — with Tina now.
- 📅 **09-22/23 — stage bug bash, teams on their own IMS orgs** (Mark Doten flagged them 09-21). 📅 **09-23 — plugin updates need a version bump.** 📅 **09-24 — Coworker prod release; Mark Doten: any AEM user with Coworker enabled gets the rail on prod enablement.** 📅 **09-28/29 — all-hands bug bash on prod.** 📅 **09-29 — Rotary code freeze (URR is right, the screenshot was wrong).** 📅 **09-30 / 10-01 — go/no-go, date disputed above.** 📅 **10-05 vs 10-12 — TBYB activation, disputed above.** 📅 **10-12 — SKU customers with panel.**
- 📅 **10-01 — System Review, H-009 re-assess, promotion-judge on the two parked candidates** (`Two Milestones Wearing One Word` now has instance 3, `Your Own Artifacts Disagreeing`).
- 🔴 **10-20/22 SJ champions — 8 licensed champions still on AOv1 with zero Coworker** (Ford, ServiceNow, Workday, Pitney Bowes, Wipro, Prudential, HPE, City National Bank). **09-27: Ford = after the panel (sequenced); Workday = opted out over user-rights control (09-15 call); Workday, Sunstar, Ford, HPE are heavy on AEM MCP direct (Cursor/ChatGPT/Copilot), so zero Coworker ≠ zero AI. ServiceNow, HPE, Prudential, CNB still to check in the Cohort 3 file.** Push them before SJ; re-run the workbook after the 10-12 SKU activation. BNY + Fanatics active on Coworker but not on the licensed list, check why. [[project_aem_agents_intelligence]] 2026-09-25 block.
- ⏳ Hemanta Gupta 09-07 Rubin bulk-export — still zero replies from anyone. https://adobe.enterprise.slack.com/archives/C0AS8RV5997/p1788770340374949 ⏳ Huz Abdullah 09-18: AEMaaCS author IP allowlist 403s Coworker, escalated to Yanira; Ian's `allowedServices: [AemMcp, Coworker]` model is on wiki 4049263594, comms plan (2-week notice) undecided. ⏳ Vitaly eval rerun `AEMAGT-2763`. ⏳ Shubham prompt-block ask — no trace. ⏳ Workday 09-15 outcome. ⏳ 09-09 OKR review outcome.
- 🔴 **Esri credit governance — Bertrand took it to Horia 09-20 and handed Pierre Tager the per-org Rubin dashboard to show the customer.** Four customers, same ask, three weeks (VW/Centene, Esri, UHG/Capital Group, Infineon). Pedro (09-22 13:42): will raise it with Bertrand, tied to the 09-22 11:23 internal/commercial split ask on the Rubin report. One classification problem, two levels (org type · user/action); AEM's canonical org classification is Raul's list [[reference_skyline_p42_orglist]], not AEP's "Commercial". [[reference_customer_esri]]
- 📅 **10-20/22 — SJ trip for the AEM champions** (~30 people from large customers, three days, a dedicated Coworker session). Bertrand DM 09-22 09:19, pre-clearing before a budget ask that "n'existe pas forcément". Reply yes today and claim the Coworker session; ask who from leadership is on site; check it against his PTO (Yanira 09-18 "post your PTO", dates not on file). Instance of the visibility gap in [[reference_promotion_strategy]].
- ⏳ **Coworker Panel product announcement** — Pedro writes it on Peter Klassen's BC design; three text options given 09-22 (naming "CX Enterprise Coworker" to confirm with Tina/Akin; flag-target the activated orgs only; drop "fix" if it points at the four Development skills out of GA). Eugene's call with Sorin and Laurentiu is the design forum.
- 🔬 **H-010 opened 09-22** (credit attribution / access control gates Coworker expansion): four customers, resolution 2026-12-15. `knowledge/hypotheses/active.md`.

### 📦 2026-10-14 — 13 sections dated ≤ 09-03 moved verbatim to `watches_ARCHIVE_2026-10.md` (System Review, Pedro's go). Grep there; still-live items surface in the project memory blocks.

### 🔵 BEFORE QUOTING ANY MCP NUMBER

- 🔴🔑 **PROVEN STALE 2026-08-16, NOT SUSPECTED — `Total tool calls (30d)` READS 95,898, BYTE-IDENTICAL TO THE 07-24 VALIDATED SET.** A rolling 30-day window cannot return the same digits three weeks apart. Tool-call data comes from the **manual AWS lookup**; request/org data comes from Splunk directly, which is why the Splunk-side panels moved and this one did not. **Every value-realization number in the board is the 07-24 vintage.** No refresh message from Jabran since 07-24, when he said he had not done one *"in last few weeks"*. **Ping him before pulling any number for the KR video, the Tina deck or the Bertrand weekly.**
- 🔴 **AND THE AUTOMATION THAT WOULD FIX IT IS DEAD WHILE READING `Done`.** `LOGREQ-16791` (onboard AEM MCP CloudWatch logs to Splunk) is **Status Done / Resolution Done, updated 08-06** — but its only comment is the LPT bot **auto-closing it as a process rejection**, *"This ticket has been closed — no automated provisioning will occur from it"*, because it was not filed through the DevHome portal. **Nobody re-submitted.** Re-file at https://devhome.corp.adobe.com/toolbox/discover/324036 or ask on `#splunk-users`. ⚠️ Its own description dates the last snapshot to **30 days to 2026-07-07**.
- ✅ **`correct:` 2026-08-16 — the Eli Lilly deep-dive gap WAS answered.** Jabran to Brian, in-thread: *"I can see it in the list ... could be a splunk loading delay ... can you please recheck?"* **Not a data gap, the blue-circle load delay.** ⚠️ Eli Lilly is in the OKR-review speaking notes, so let the panel finish loading before concluding anything about it.
- **Jabran, 07-24: 30-day window only** — *"a bug in some panels not respecting the time filter"*, fix promised *"next week"*. **Still no fix confirmation as of 08-16.**
- **🔴 The "Tool Calls" lock is slipping.** Tanju's report now says **"operation"**; Christian Meyer challenged it 07-28, undecided. **Pedro owns this term** ([[reference_mcp_terminology]]).
- Unresolvable IMS orgs (`127B272369BC84400A495C0A@AdobeOrg`, 19,922 requests) — Jabran suspects AEM trial envs.

## 🏠 Experience Hub

### From 2026-10-23 — left-nav Coworker icon (full read: [[project_experience_hub]] 2026-10-23 block)

- 🟡 **Pedro's reply to Guliz on the left-nav Coworker item** (drafted 10-23, not posted as of 10-27 10:30 CET): https://adobe.enterprise.slack.com/archives/C0BARAMM89Z/p1792779005879539. One line to Bertrand first (he accepted removal 10-02). Then check Silvia's answer on the icon and whether Mark Doten takes EXC-49877 to the change board during RCP.

### From 2026-10-22 — H1'27 canvas, Eugene (full read: [[project_experience_hub]] 2026-10-22 block)

- 📅 **~10-26 · Pedro's H1'27 items in the canvas `H1'27 Foundation Planning`** (https://adobe.enterprise.slack.com/docs/T025FJ55H/F0C5A1D4GAJ) before Bertrand presents Cloud Services & Security on **Tue 10-27, 7-8 am PST** (Tracy Seibel, `#aem-foundation-leadership` 10-21). His TBD H2'26 lines there: SKYOPS-136515 Release Management Scalability, SKYOPS-136517 AI transformations of Rotary release tools, HOME-832 EH Product Adoption. His three RS-EX H2 items were folded into shared CF roadmaps (H2 canvas F0AL123SP8D, matched on title and RS HC): CSO → SKYOPS-137585 (RS 2), vulnerabilities → GRANITE-66668 (RS 1), EDA breaking changes → AEMAGT-1282 (RS 2). In H1'27 they become SKYOPS-161584, GRANITE-75092 (no RS line yet) and AEMAGT-2920 ("RS: ?"). HOME-832 = 4 HC in H2'26, Sorin 10-14 "I assume the HC are the same", Pedro "Yes"; under the canvas 5-HC minimum, and the Workforce table tags only 3 of Sorin's team to DX-1222. Canvas rules: link each to an H1'27 DX initiative or close it, at least 5 HC per roadmap (no .5), one Invest label, remove TBD when committed. Customer-facing roadmap due 11-20. *(Kept whole here because it spans three projects; the vault tasks are split: HOME-832 in EH, SKYOPS + AEMAGT in Release Management, SKYOPS-161584 + GRANITE in Security Health.)*
- 🔴 **~10-30 · Eugene fading out of EH** (Silvia to Pedro, relayed to Sorin 10-21). Get the date and who covers EH design, before the nav-slot decisions land. → [[project_experience_hub]] 2026-10-22 block.

### 🆕 2026-10-21 — DA.LIVE WRITE ACCESS (full read: [[project_experience_hub]] 2026-10-21 block)

- 🟡 **~10-23 · write access back on the announcements owners sheet** (`https://da.live/sheet#/oneadobe/aem-experience-hub-announcements/announcements-owners`). Row 10 of `https://da.live/config#/oneadobe/` lost the `eh-announcements-da` group. Pedro asks Mircea Salan, Sorin in copy, to restore the group and add him. Check an edit saves; if not, the CONFIG write row (rows 1 to 9) names who can fix it.

### From 2026-10-13 — back from PTO

- 🟡 **Content AI nav item (EH): answered 10-13 10:29, "keep Coworker first", asked Mihai Copae for the requester.** ⚠️ Mircea asked, the reply went to Mihai. Requester unknown; Peter Klassen asked 09-10 to place Content AI in the nav. https://adobe.enterprise.slack.com/archives/C0BPMFYLTJL
- 🟡 **EH Coworker left-nav item (Adrian 10-13):** Unified Shell says left-menu Coworker is an anti-pattern, keep only the top button; open question = fallback when the panel is off. Sync booked 10-14 am. https://adobe.enterprise.slack.com/archives/D0BHLEE6UCX

### From 2026-09-22 — Slack audit

- 🟡 EH: Eugene 09-16 wants a call on the LLM Apps announcement (Laurentiu sets it up); Adrian took the nav item, spec `HOME-926`; Pedro's 09-22 BC-page ask is answered by Mihai's 09-18 post in `#aem-bc-trial` (stage preview, Peter's design). Ramon needs an EH-priorities meeting. Guliz 09-16: add her + Silvia to every Coworker panel meeting; Pritom Baruah wants a "post-GA alignment on Coworker UI collaboration" — set the call.

## 🔁 Release Management

### 🆕 2026-10-28 — RBI ESCALATION + RELEASE PAUSES (full read: [[project_release_management]] 2026-10-28 block)

- 📅 **11-03 · RBI customer call (Patrick Hauzel, Martin Floess).** How Pedro's 10-28 reply landed, whether RBI is in the "selected customers", and the date for the Update-Free extension (still not given).
- 🟡 **Release management item in Bertrand's H1'27 plan = SKYOPS-163976** (+ SKYOPS-163977), both "HC: TBD"; Bertrand 10-27: "sans que je sache trop ce que ça veut dire". Pedro explains it to him (in person 10-28 possible) and asks Nicu to set 5 HC. Canvas F0C5A1D4GAJ.
- 🟡 **Merit Vossmann: what replaces Visual Regressions** (asked 10-27 15:20, her customer call 10-28). https://adobe.enterprise.slack.com/archives/D0CBFJ858TD/p1793110852430919

### From 2026-10-13 — back from PTO

- 🟡 **Dustin / UPS RO pause 11-01 → 01-11: answered 10-13 10:20.** Pedro pointed him to the RO wiki ("Pause Updates for a program in RO", https://wiki.corp.adobe.com/spaces/WEM/pages/1971265640) and asked for the ticket in the DM; customer is opening a support ticket (Dustin 10-12). ⏳ Ticket number not yet shared. Razvan's 09-28 UnderArmour / Best Buy ask still open. https://adobe.enterprise.slack.com/archives/C0C6UD4G5V0
- 🟡 **Tatyana release review dates: answered 10-12 18:53** (Nov 2026.11 → 11/19, early for the BF/CM exclusion; Dec 2026.12 → 12/10, early for the year-end exclusion). ⚠️ **January not given**, and her 18:14 bump asked for Jan too. https://adobe.enterprise.slack.com/archives/D06K07DHUTU/p1791821657048099

### From 2026-09-22 — Slack audit

- 📌 Fred-as-a-Service: Pedro told Amit Gupta 09-22 "progressively de-commission, target 6 months". First time on record; check it against anything he tells Nicu or the customer.

## 🛡️ Security Health

### 🆕 2026-10-28 — project created (context: [[project_security_health]]; tasks in the vault `Security Health - Status and Todo.md`)

- 🟡 **Ramon's EH-priorities meeting** (asked 09-16, the EH Status had it due 09-26; no record it happened). Also open: RS lines on SKYOPS-161584 (CSO) and GRANITE-75092 (vulnerabilities) for H1'27.

## Cross-cutting

### 🔴 CAREER — MID-YEAR REVIEW (undated, the next real checkpoint)

- 🟡 **10-28 · ask Bertrand the date of the mid-year review** (he was at Pedro's office that day).
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

## History (closed)
- 📦 **Moved verbatim 2026-10-14 (cap breach, ~24K):** the four 📕 sections (closed by 09-22 / 09-16 audits, pre-GA August, residuals of August) + the two compressed 08-07/08-12 sections → `watches_ARCHIVE_2026-08.md`, grep `appended 2026-10-14`. Open residuals inside them (NXUI-1904, AEMAGT-2581, `dma_aem_ams`, Trent's ARB agreement) are for the System Review to close or revive.

<!-- ✅-closed watches move here with close date; prune below ~10 lines -->
- 2026-08-24 — **Bertrand landed and picked the work straight up** (*"ca depile, ca depile"*). The 08-14 weekly never went; the 08-21 pre-read was the last thing he read.
- **2026-08-07** — file reshaped to the one-line rule (30.7K → ~10K tokens). Full prior content verbatim in `watches_ARCHIVE_2026-08.md`.
- 2026-08-06 — **Clint's 72-hour clock CLOSED.** Pedro answered 08-05 17:29 object-backed (62/63 manifest census, twelve CODEOWNERS lines); **Carsten answered the lifecycle question in 29 minutes after a week of silence.** Positive control for [[Say the Sentence That Obliges — the Hedge Transfers the Ask]]. Residuals kept above.
- 2026-08-06 — **KR 1e outcome resolved:** the video was never played, the meeting was derailed. Residuals kept above.
- 2026-08-03 — monthly System Review ran. H-007 resolved, parked cap enforced 15→2, decisions scored. **Next due 2026-09-01.**
- 2026-08-03 — the check-in was 2026-07-21; iA Writer track dead, Pedro's call. Authoritative goals = the submitted Workday version.
- 2026-08-03 — sections ≤ 2026-07-17 moved to `watches_ARCHIVE_2026-07.md`.
- 2026-08-03 — `.claude/memory-backups/20260702-pre-P1/` deleted, recoverability verified against git first.
