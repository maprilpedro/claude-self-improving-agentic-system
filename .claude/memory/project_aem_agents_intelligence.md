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

> ## ▶️ RESUME HERE — **2026-10-27 pm:** Bertrand 1-1 ingested (low-fidelity Otter, block directly below): rate card → Tina, customer comms → Gina Casagrande + Guillaume Carlino, Bertrand asked whether Coworker gets a foundation roadmap line, one passage unresolved (ask Pedro). Persistent instructions: Raul answered Herbie only (no joint ask), Trent draft given to Pedro, vault note `AO 2.0/Coworker Persistent Instructions Status.md` ([[reference_coworker_system_prompt_blocks]] 10-27). **2026-10-27 am:** Pedro asked to track Bertrand's Summit 2027 labs canvas (block below). **2026-10-27 (consolidate of 10-23):** the AEM MCP Server security FAQ is approved by Pedro and with Product Legal (10-23 block directly below). EH side: Unified Shell (Mark Doten) says it will block the left-nav Coworker icon at RCP, Pedro keeps the item, his reply to Guliz is drafted and not posted ([[project_experience_hub]] 10-23 block). Due before this consolidation and not checked here: Namita beta answer (10-26), H1'27 canvas items (10-26), Bertrand's review today 10-27. _Earlier:_ **2026-10-23 (consolidate of 10-21 → 10-22):** 10-22 block below. Namita's Coworker skills beta MVP gives AEM the user list; Pedro took the AEM side on Shankari's reply-all (review due **10-26**), Shankari answered claiming the escalation for Assets. 🔴 Owed: a call with Shankari on who does what, Bertrand told first. Also: Pedro's own SJ recap framing (SJ block), Rubin feedback wiki pointer, Agentic SKU name, Atlassian MCP 401. EH side: H1'27 canvas items due before Bertrand's **10-27** review, Eugene fading out of EH, da.live write access still down ([[project_experience_hub]] 10-21/10-22 blocks). _Earlier:_ left off **2026-10-21 am (Pedro in SJ, forum day 2):** the 10-20 session transcript is in the vault (`Meeting Notes/AEM Champion Forum 2026/`), summary + 21 improvement asks with counts in the vault note `2026 AEM Champion Forum Feedback` (AAI folder, per-session sections; the SJ page keeps follow-ups and links), 4 watches added under 2026-10-20 in [[watches]]; **ingested 10-21** (Status Focus 2026-10-20 (SJ) block, memory block directly below, H-010a candidate #2 logged not counted, one candidate parked, Removing Friction refined). 🔴 Owed from the session: tell Tina the readout needs a named owner per category (~11-03); share the per-user Rubin dashboard with the champions; the end-of-November access date was said to customers. _Earlier:_ left off **2026-10-19 morning, day before SJ**: KR1e slide numbers refreshed (MCP W38-W40, Modernization W42, block directly below), Tina's SJ session doc captured verbatim in the SJ vault page + a 5-question challenge Pedro has NOT answered yet, M1 migration plan read (10-14 PDF), Loni deck ask = **B** (Pedro 10-16), UPS stays on slide 4 as a Pod customer. 🔴 Owed: Mike Tilburg on the 37K → 72K live pages jump; Pedro's yes/no on the SJ challenge (Q1 the "every skill is available today" opening). _Earlier:_ left off **2026-10-14 evening**: adoption plan for Bertrand (x4.5 permissions message SENT, full plan ~10-23, Loni deck skeleton in vault, slide-6 ask OPEN), System Review done (H-009 killed, H-010 split, Two Milestones promoted, next review 11-02), and the 🔴 **AEM-Coworker denominator is unreconciled (37 / 57 / 811 / 1,000+)**, blocks directly below. Pedro's open pings: Shubham (Newell), Corey (UPS naming), Pritom (access date), Shankar/Soumya (org count), Yelena (CXCO-230). _Earlier 10-14:_ left off **2026-10-14** (Slack check, block below the adoption ones: CXCO-230 contradiction, Havas ask, Pritom owns the access-control routing, two 09-22 watches closed. Then the 10-13 blocks.) _Previous:_ left off **2026-10-13** (back from PTO 09-28 → 10-12; block directly below: the PTO Slack audit, the SJ Champion Forum page, the Rubin legal hold, the follow-ups waiting on him. Then the 09-27 MCP read of the champions and the 09-25 champions block). 🔴 **SJ Champion Forum 10-20/21: session "Agentic Workflows" with Martin + Tina; vault page `AAI - Project Folder/AEM Champion Forum 2026 - San Jose.md` is the single home for links.** 🔴 **Rubin Chat Analysis is on legal hold since 09-25; Pedro has no access until the AEP Datalake onboarding is approved person by person.** Older resume line kept below for the 09-27 state.
>
> _Previous resume (09-27):_ left off **2026-09-27** (Coworker + MCP read of the champions, block directly below: Workday opted out over user-rights control, Ford waits for the panel, the "zero Coworker" champions are heavy on AEM MCP direct. Then the 09-25 champions block: 8 licensed champions incl. Ford, Workday, ServiceNow still on AOv1 with zero Coworker. ⚠️ Nothing captured from Slack after 09-22, the 09-24 prod release outcome is unknown; run an audit first. Then the 09-22 Slack audit block; then the 09-17/18 and 09-16 blocks). 🔴 **THE PANEL ACTIVATION HAS FOUR DATES. Pedro's own 09-16 post: prod 09-24, go/no-go 10-01, TBYB 10-05, SKU 10-12. Marius 09-22: 09-30 for go/no-go and TBYB. Mark Doten: 28th or 30th, unanswered. Paul Midura to the field: AEM held until 10-12. Loni holds 09-21 and her GA email is queued.** ✅ GA live for more than 1,000 orgs since 09-15, still without the panel. 🔴 **Unanswered and tagged to him: NWL Brands (three pings, escalated), nine Gainsight removals, three Yanira asks, Bertrand's Rubin split, Lénárd's prod regression** — [[watches]] 2026-09-22 section. The 09-02/03 audit block moved to shard W36 on 09-22 (consolidation); the 09-01 and 08-27 blocks went to W36 / W35b on 09-16 (read `..._ARCHIVE_INDEX.md`). Still his from 09-03: the Top 3 re-triage and the `Current Status` refresh in the AAI Status & Todo. Previous pointer text kept: 🔴 **AEM HAS NO PROMPT SURFACE ON THE MANIFEST THAT CARRIES ITS GA SKILLS.** 🔑 **Coworker's persistent-instruction layer is `.ao/prompts/system/` block directories, scoped per MANIFEST — and AEM's 18 GA plugins live in `cx-coworker.yaml`, which AEM does not own. So every AEM skill runs under `app/aep`, told it is an Adobe Experience Platform coworker.** The ask is written and the target is named (Shubham Lohiya). Full mechanism → [[reference_coworker_system_prompt_blocks]]. See the 2026-09-01 block directly under this; the 08-27 inventory work is in shard W35 (archived 2026-09-03).
>
> ### 🟡 2026-10-27 — BERTRAND 1-1 (LOW FIDELITY): CUSTOMER COMMS GOES THROUGH GINA, THE RATE CARD THROUGH TINA, AND COWORKER HAS NO ROADMAP LINE
> - **Source.** Vault `Meeting Notes/Bertrand 1 1/20261027 - Bertrand Pedro 1 1_otter_ai_transcript.md` (~29 min, ~14:15 CET, an hour before Bertrand's H1'27 review). ⚠️ Otter mixed languages, more than half the turns are noise: sense only, no quotes, no numbers. Status: AAI Focus 2026-10-27 (Bertrand 1-1), EH Focus 2026-10-27.
> - **Pedro reported the forum.** Cross-product queries valued; governance the main brake (limit which users of an org get Coworker, token visibility); a step beyond AOv1; compared to Claude and ChatGPT, some thought it was Adobe's own model (Bertrand: the model matters); CMS workflow refinements, URL structure, the hidden approval, thumbs with comments. Consistent with his 10-22 recap. Persistent instructions: four layers, Trent next. Bertrand agreed on four levels, tied it to Experience Context and business context as extra context the agent gets on every question.
> - **Bertrand's asks.** (1) Coworker as a roadmap line at foundation level beside Sites, Assets, Forms. Pedro: central JIRA, no central resources, Yanira and him, roadmaps sit with each team; besides Coworker his top-level items are Release Management (Razvan) and EH. (2) The Coworker rate card and roles (cost per action plus a global cost). Pedro knew only what Bertrand told him, Tina is his contact; Bertrand had a Slack from Tina on the pricing model → Pedro asks Tina.
> - **Customer comms.** Docs AOv1 → Coworker ahead of plan, the AOv1 part can stop (who updates it: garbled "Larna"). Pedro's idea: short use-case capsules from the champions (permission audits), LinkedIn-length videos, a blog page. Bertrand: Gina Casagrande (Director, Experience Cloud Evangelism, [[project_adobe_org]]) owns that space; he built demos (video, script, clickable; existing customers vs new on Experience Workspace). Pedro: check with Guillaume Carlino (docs, the 07-30 Security Health release notes) and Gina.
> - **Projects and user management.** Pedro asked the Projects PM for an intro; Bertrand interested in multi-user project conversations. Pedro in contact with the user-management PM; no integration work on AEM's side, but AEM is frontline on rollout order and customer comms.
> - **Unresolved (~18:30 to 20:55).** Feature enablement, someone who covered for Pedro doing it in his place to free operational time, Razvan, the Bucharest hierarchy; Bertrand agreed to something. Ask Pedro, do not reconstruct.
> - **Read.** Bertrand asked, an hour before his H1'27 review, whether Coworker deserves a roadmap line; Pedro described the resource gap and did not claim the line (as far as the transcript shows). Candidate instance of [[Your Biggest Lane Can Have No Slot in the System That Scores You]] and [[H2 Planning Visibility — Own the Narrative Before It Gets Written Without You]]; not added to the entries, the source is too degraded. Watch → [[watches]].
>
> ### 🟡 2026-10-27 — SUMMIT 2027 LABS: BERTRAND'S TEAM CANVAS HAS FOUR PROPOSALS, NONE FROM PEDRO
> - **Source.** Canvas `Summit 2027 Sessions and Labs` (https://adobe.enterprise.slack.com/docs/T02CAQ0B2/F0CAF0U4V43). Bertrand `#aem-cloud-foundation-pm` 10-19 09:01: "in our next team meeting, let's review our collective proposals for Summit (sessions and labs)"; 10-20 12:14: "please post your ideas" (https://adobe.enterprise.slack.com/archives/GTYKF4UAC/p1792393260820929). Pedro asked 10-27 to track it.
> - **On the canvas (owners not named in the body).** (1) AI discovery experience with LLM Apps; (2) agent-ready website with WebMCP; (3) DaaS x CDN: Content Request usage with the CDN Insights Agent in Coworker; (4) AEM CS developer productivity with IDE Agent Skills and Coworker (CM, CDN, Dispatcher, AEM, SRE): code assessment skill in VS Code + Copilot, "why is my site slow right now" ending in a patch Coworker merges and deploys to an RDE, traffic spike RCA, security posture patch.
> - **Comments 10-26 (positions, not acceptance).** Bertrand to Laurentiu Odoleanu 13:37: "maybe consolidate Lab 1 and Lab 2 as a single one? (same as a year ago with Content AI + LLM Apps?)". Bertrand to Brian Chaikelson + Shweta Dua 13:37: "looks good to me, can you please submit via Ron's form?"; Shweta 13:39: "Thanks ! Sure, will do". The section that comment anchors to is not readable; Shweta is DaaS, so likely lab 3.
> - **Process.** Labs go through Ron Nagy's form, deadline Mon 10-26 (Tracy Seibel `#aem-foundation-leadership` 10-21, "to be used vs. separate canvas", https://adobe.enterprise.slack.com/archives/C08KDFWL5GW/p1792610752427789). Speaker sessions have no open call (Mike Stiles `#summit-questions` 10-22: content strategy still being finalized with the exec team, https://adobe.enterprise.slack.com/archives/CDKFSPL0P/p1792682857310699).
> - **Read (inference).** Labs 3 and 4 put Coworker skills on the Summit stage; their GA status is not checked here (the Cloud Manager pipeline-troubleshooting skills were pulled from GA 09-16, EH memory 09-22 block). No lab on the canvas is Pedro's; the sessions call is the slot still open. Knowledge: [[The Vision-Reality Gap in AI Products]] · [[H2 Planning Visibility — Own the Narrative Before It Gets Written Without You]]. Watch → [[watches]].
>
> ### 🟢 2026-10-23 — THE AEM MCP SERVER SECURITY FAQ PASSED PRODUCT MARKETING AND WENT TO PRODUCT LEGAL
> - **What.** Group DM `C0BUE8GE754` (Emily Cohen, Sr Marketing Security Manager, Security at Adobe; Ian Boston; Tanju Erinmez; Yanira; Tina Ngo; Richa Kaul; Bertrand). The asset is `AEM-MCPServer-MVP-1026.docx` (https://adobe.sharepoint.com/:w:/r/sites/SecurityAtAdobe/Shared%20Documents/Security%20Marketing%20%26%20Culture/Field%20Enablement/Security%20Overviews%20and%20Fact%20Sheets/CX%20GenAI/AEM%20Agentic%20MVP/AEM-MCPServer-MVP-1026.docx?d=w93a9bbb87b2f4a7abda093980c37eca9&csf=1&web=1&e=erOmbi), a Field Readiness security overview that Emily's team uses to answer customer security questionnaires. Emily 09-29: the MCP server gets more customer security questions than Coworker, and "these assets are used for security reviews and are in the line of revenue". Workfront issue: https://experience.adobe.com/#/@wfadoberm/so:adoberm-Production/workfront/issue/6abd17dd0006f71b9743f0c58f16984c
> - **The tension.** Ian (09-30, 10-14) kept the sandbox detail out. In his view the gVisor sandbox "does not isolate the kernel" and is not safe for code generated by a third-party LLM; AEM Security signed it off anyway and an exception is still open for AEM-CS; detailing it "will not answer the question without raising more". Emily wanted the full data flow, the sandbox and the user authorization step. Tanju 10-13: "we are turning in circles"; he approved 10-22 without settling her last comment. The 10-16 text still says the request runs in "an isolated environment" with seccomp. 10-23 Emily accepted Tanju's edits on the admin restriction ("On my production instances, MCP is read-only").
> - **Pedro.** Approved in Workfront 10-23 (Product Marketing step, his screenshot 14:11 PDT). Emily 14:42 PDT: "Pedro. You're it and we go to product legal"; 23:47 CEST: "Ok you're good. It's off to Product Legal", "Ellis says he can look at it later next week" (likely Ellis Dobkin, Legal for AEM agents in the Stakeholder Map; not confirmed). Joe Stewart (Sr PMM) showed as a pending approver; Yanira: "not even on this chat. From PMM side it is Tina". Tina reviewed with no edits 10-24; Emily 10-26: "I think we're good for now" (both her directs are on maternity leave). Closes the 10-15 watch on Yanira's approval ask.
> - **Carry.** The sandbox is the question a knowledgeable customer will ask, and it will route to Pedro or Bertrand. Watch → [[watches]]. Knowledge: none apply.
>
> ### 🟡 2026-10-22 — THE COWORKER SKILLS BETA FOR AEM HAS A MECHANISM, AND PEDRO TOOK THE AEM SIDE IN WRITING
>
> - **Source.** Shankari's email 10-22 07:06 "FW: AEM / Coworker Coordination" (to Pedro, Yanira, Bertrand, Namita, Felix Delval; cc Clint, Ian Reasor, Ian Boston, Grant Russell, Apoorva, Ankur, Ankush), forwarding Namita: "Met with the team today… MVP mechanism", proposal doc `AEM Skills Beta Program.docx` (Horia's OneDrive, https://adobe-my.sharepoint.com/:w:/r/personal/horiag_adobe_com/Documents/work/ML%20and%20Experimentation/Generative%20AI/AEM%20Skills%20Beta%20Program.docx?d=wfeefff3cc18c4704a191907091662569&csf=1&web=1&e=4VGeDe). "We are removing any need for customer-admin-facing access control for this MVP… your team can control exactly which users get access to your beta plugins/skills." Mihai (with Ken Russell) sets up manifest + segments, "a couple of days". Below it, Shankari's 10-08 notes of the "AEM / Coworker Coordination" meeting (**Manas's invite**, 9:05 to 9:30, during Pedro's PTO): no cohort-zero pathway exists in Coworker, Horia and Pritom to define one.
> - **What it closes.** The gap Pedro named 09-11 ([[reference_coworker_pods]] 09-16 block): early enablement with custom manifests did not fit because these customers want specific users only, outside the Coworker runbook. Namita's MVP gives AEM the user list.
> - **The tension.** Pedro 10-22: Shankari keeps meeting key Coworker people (Horia, Pritom, Manas, Ken) without him, they are not in sync, he wanted to tell her to stop. Advice given: no "stop" in the reply-all (Shankari is a Group PM peer, office next to Loni's; the 10-08 meeting was Manas's and fell in his PTO, so a public complaint loses on facts), settle roles in a call, Bertrand informed first, use the reply-all to pick up the action. ⚠️ Correction the same day: Shankari is **not** his manager, the paper arrangement lasted about a month in spring ([[project_adobe_org]]).
> - **Sent.** Pedro sent his reply 10-22 ~10:45 PDT, built from the draft (pick up the review, AEM side by Monday 10-26, possibly "I'll be the AEM contact… one channel on each side"). Exact sent text not pasted. Bertrand DM and the Shankari call not confirmed. Watch → [[watches]]. Knowledge [[The Game Itself — Position Over Merit]] · [[Pick Up the Open Action Item]] · [[Don't Let Program Managers Carry Your Liaison Relationship]].
> - **Shankari's answer, 10-22 ~10:49 (to Pedro; reply-all or direct not known):** "TY! Just so you know, I escalated this, which is why they responded to me, to be fair. Assets has been hurting significantly with multiple customers waiting for over 8 weeks." Read: she claims the escalation and speaks for Assets customers (UPS asset sourcing portal lost 09-14, restore PRs still open 10-15). Advice: do not argue credit in writing; give her the escalation in the call and agree the forward split (she brings Assets customer priority, Pedro runs the AEM side of the beta mechanism across AEM skills and the Coworker channel). Also applied: [[How to Commit Political Suicide — Warning Patterns]] (being right in the wrong way, in public).
> - **Also 10-22, pointers.** Yanira's Rubin / ao-quality gap list lives on wiki 4072898074 (https://wiki.corp.adobe.com/pages/viewpage.action?pageId=4072898074, sent by DM 10-13; seeded from Lénárd's 10-06 list posted by Felix: no questionnaire answers, first 1,000 calls of a chat only, no AO or AEM Splunk search, no ask-an-agent-why; plus chat id + region lookup, an internal/external org filter, the "Adobe Experience Manager" label, both Bertrand 10-02). Not read, Confluence 401. Agentic SKU name → [[reference_tbyb_sku_entitlement]]. 🔴 Atlassian MCP token expired 10-22 (JIRA and Confluence both 401): reconnect before any JIRA or wiki read.
>
> ### 🔴 2026-10-20 (ingest 10-21) — SJ "AGENTIC WORKFLOWS": THE ROOM SAID NO ON VALUE, PRAISED PLANNING TASKS, PANNED PAGE CREATION, AND SPENT TWENTY MINUTES ON ACCESS CONTROL
>
> - **Source.** Vault `Meeting Notes/AEM Champion Forum 2026/20261020 - AEM Champions Forum Day 2 Session AEM Coworker.md` (Teams, ~60 min, Tue 10-20 pm, after Bertrand's remote demo and the morning Coworker session). Room mic `CR SJ FT08/Tidewater VC Managed (64)` = everyone in the room (Tina Ngo led, Corey, Pedro, Martin, every champion), attribution by content only; named remote voices Dianne Eveler, Varadi Kedarnath (Kedar), Jineet Vora. Full summary, feedback tables and the 21 improvement asks with people/occurrence counts: vault note `AAI - Project Folder/2026 AEM Champion Forum Feedback.md` (one section per session; moved off the SJ page 10-21 on Pedro's ask, the SJ page keeps the follow-ups). Status: Focus 2026-10-20 (SJ).
> - **What happened.** Few hands for the pre-work; "did you find value?" → "No?". Planning and verification tasks won (Greg, Bank of New York: ABAC plan for Content Hub, "99% of where I want to get", "saved me at least a day or two", watched which skills ran; a champion had permission groups tested, Excel back). Production lost on polish against the expert baseline (Brent/Brett, partner: relative URLs, "an error that no author would ever make", "it wasn't a better process", not recommending it to his customers; Dianne: "I might as well go into Claude"). Pages always "boxy brochure". Second half = org level, as Martin predicted 10-01: Kedar will not open to authors without profiles, Dianne's regulated FS org has it disabled, Jineet on credits, one voice against guardrails. No champion has built a custom skill; the room wants Coworker to propose turning a repeated task into a skill. No vote on the one blocker (Q5), the organizer closed; Tina owes the readout ~11-03.
> - **Said to customers by the Adobe side, keep consistent.** Per-user access via Admin Console profiles **by end of November** (M1 plan calls it tentative); same model in demo and customer orgs; a per-user credit dashboard exists (Rubin, "we should probably share it with you"), no efficiency view (privacy); the all-or-nothing GTM is deliberate; foundational skills 75% / custom 25%; skills matched by **name and description** at session start; memory and org-level customization "rolling out" / "on the roadmap".
> - **Pedro's lanes.** (1) The end-Nov date is now a customer commitment → [[watches]]. (2) Name+description selection is the argument in the Shubham name-only-descriptions thread. (3) The Rubin per-org dashboard is the Esri artifact; share it with the champions, owner unassigned. (4) Kedar = candidate conditioned decision #2 for H-010a (logged in `active.md`, not counted); Dianne = decision without condition. (5) Pedro's SJ value pick (custom skills) got zero takers; the stories that landed were advisory (ABAC, permission tests). Brian's 10-05 gap confirmed by the room itself.
> - **🔎 KNOWLEDGE (P6).** Instances: [[Removing Friction Is Not Enough — Agent Adoption Can Still Fail]] (+10-20 refinement written: org trust and the expert baseline as invisible frictions); [[Two Milestones Wearing One Word]] ("end of November" is one word for new-customer auto-provisioning, the Wave B migration and the flag removal); [[Say the Sentence That Obliges — the Hedge Transfers the Ask]] ("we take on", "we should probably share it with you", no owner named either time); [[The Vision-Reality Gap in AI Products]] (Brent asked whether demos run a lighter model, "same model" closes the architecture excuse and leaves skill quality); [[Govern a Consistency Layer Over Primitives You Don't Own]] (the skill description budget). **Parked, 1 instance, gates met:** *Agentic Value Lands First on Advisory and Verification Tasks; Production Tasks Lose Against the Expert's Baseline*, 2nd instance expected in Rubin Chat Analysis by intent class, auto-drop 11-02; the 10-20 event is booked there (one-event-one-home). No new entry.
> - **Pedro's own recap of the session, 10-22 (three lines for an outward summary, his framing, recipient not named).** Team pleasantly surprised by the feedback; the step forward from AOv1 noted (one voice in the transcript, the British sandbox user); Coworker now a tool champions can use; value seen and foundations liked; but junior on content creation, and governance (access for specific users, credits per user) blocks wider use; Coworker UI gaps (input prompt hidden behind the spinner, silent tool-call failure, thumbs down without a reason). Critique narrowed "they see the value" to "champions who used it" because the room answered "no" at the start; whether the sent version kept that is not known. **Check later statements to the same readers against this framing.** Instance of [[Lead the Slide With the Honest Read of Your Own Metric, Not the Flattering Number]] (4th instance line added to the entry).
>
> ### 🟢 2026-10-20 — LEGAL APPROVED #1 + #2 FOR EVERYONE ON THE WIKI, ONE DAY AFTER PEDRO'S SCOPED ASK
>
> - **What happened.** Pedro answered Tonia Hashimoto with Loni's actual ask and a narrow request (Yanira's suggested scope): #1 usage reporting + #2 troubleshooting for all wiki users plus new users. Legal (Tonia + Carla) agreed the same day; Loni's Legal meeting cancelled; a streamlined approval workflow is coming. Loni's end-October deadline met ~10 days early.
> - **Still open.** "Quality / chat analysis" uses unapproved. Yanira → PR to Ilya Grafutko. Pedro → tell Corey, one line to Loni + Bertrand. The "~70 opt-outs" vs 59 Excel lines.
> - **Also 10-20.** Licensed AEM customer list located (DashDiscovery `AEMLicensedCustomers`, Pedro has access): [[reference_aem_licensed_customers]].
> - **🔎 KNOWLEDGE (P6):** instance of [[Say the Sentence That Obliges — the Hedge Transfers the Ask]] (a precise, bounded ask got a yes in a day where the 10-19 "asap" got a question back). One observation, no new entry.
>
> ### 🔴 2026-10-19 (ingest 10-20) — LONI'S KR REVIEW: RUBIN UNBLOCKED BY END OF OCTOBER, AEM DATA HANDLING HANDED TO BRIAN + IAN
>
> - **Source.** Vault `AAI - Project Folder/KR Reviews/20261019 - KR Meeting Review - Transcript.md` (Teams, Tatyana hosts). Pedro and Loni shared the `CR SJ ET13/Innsbruck` mic; line-by-line attribution in the file header.
> - **Rubin access.** Pedro told the room access was blocked ~2 weeks ago after misuse (customer chats in PowerPoint). Loni: valid concern, handle it rather than say no; **"I'd like to talk to legal… it needs to be unblocked by end of October… if I need to be dragged into something, let me know."** This is what Loni wants from Tonia Hashimoto (Director, AGC), who asked 10-19 20:13. Internal certification floated (speaker unclear, maybe Pedro).
> - **Ownership vacuum, filled in the room by someone else.** Loni: who thinks about customer data handling for AEM (MCP, Experience Context, learning ledger)? Bertrand: "Nobody at the moment… TBD"; named Ian Boston, PM counterpart "Brian and myself"; Loni: "Brian and Ian… let's give them this problem." Pedro did not claim it. Coworker-wide side stays with the Coworker core team (Horia).
> - **Permissions.** Bertrand's mechanism: the UI disables or hides the button, Coworker says nothing until you try. Loni: treat the failed publish as a wish, help them do it (route a request to the owner), beta candidate. Loni: the Coworker text box is "the purest" signal.
> - **Pedro's numbers in the room** (keep consistent): 12 paying customers migrated last week, ~10 this week, a couple of hundred internal orgs left, ~70 opt-outs mostly governance (the 10-13 Excel had 59 lines), adoption on par with AOv1, failure figures garbled.
> - **Loni's three review-wide themes:** CS attrition teardowns (Contentful, Contentstack), 20% growth vs down-sells mismatch (Shweta), labs/early-access model instead of "friends and family" co-innovation (Tracy, Tatyana collect 5 to 10 features).
> - **🔎 KNOWLEDGE (P6):** [[Say the Sentence That Obliges — the Hedge Transfers the Ask]] (an unowned problem was assigned in front of the VP, to a peer); [[Removing Friction Is Not Enough — Agent Adoption Can Still Fail]] (permissions). No new entry.
>
> ### 🔴 2026-10-15 → 10-19 — M1 PLAN READ, DECK ASK = B, KR1e NUMBERS REFRESHED, SJ DOC CHALLENGED
>
> - **M1 Rollout Migration Plan (PDF 2026-10-14, `~/Downloads/2026-10-14 Coworker Governance M1 Rollout Migration Plan.pdf`), "Tentative / Not Confirmed".** 3,979 orgs on Harness / 3,996 on Shell (all products, customers + internal), 147 segments, 360 named users. Wave A internal/NFR 194 orgs 21-28 Oct; Wave B non-pod chat 2-23 Nov (3,753 simple orgs 2-12 Nov); Wave C pod/Projects 30-57 orgs, no dates (Projects owns); flag removed by 30 Nov. Auto-provisioning for new customers from 2 Nov, unconfirmed, so the "10-15 release" was code complete only (instance of [[Two Milestones Wearing One Word]]). Four gates: org eligibility, user permission (Access Control), UI visibility (Unified Shell, Mark), Projects. Not covered: whole-org opt-out, customer comms (Kapil pending), audit UI (M2), token visibility. 🔴 The November migration sits inside Pedro's +20% measurement window.
> - **Slack 10-15/16 (not yet answered by Pedro unless noted):** Felix tagged Pedro on the UPS manifest PRs (#14609 Clint/Shankari, #19835 Krishnadas; Grant Russell suggests `aem-aia-extensions/experimental`). Yanira asked Pedro to approve the Security doc in Workfront (10-15). Mihai: 10-15 release = new customers only, most TBYB customers go through migration. AOv0: of Pedro's 6 orgs, 4 opted out; Canon Medical and Country Financial active in 3B but still on AOv0; Stephen: opting out of Coworker ≠ out of AIA. Adrian: left-nav Coworker ~100 clicks/week; panel announcement code in prod, no orgs targeted. Yanira "governance team or Cole?" on hiding nav for users without access → the M1 plan answers it (Unified Shell, gate 3). Caitlin Cody wants the VCP demo recording. Ellis (10-16) proposes a narrower Rubin access route. Bertrand silent on x4.5.
> - **Loni deck (vault `Coworker AEM Adoption - Loni Deck Structure (2026-10-14).md`).** Slide-6 ask = **B, Pedro 10-16**: Loni validates the measure (+20% external WAU by end Nov, baseline week of 10-06); her yes fixes the definition so no other number replaces it. Open: which Rubin view counts (dashboard 280 vs Pedro's subscription 576), Pedro "je ne sais pas", ask Soumya. **Correction (Pedro 10-16):** UPS stays on slide 4, Pod customer, ~8-9 enabled users (Stephen Gould 10-14), opted out of the org-wide rollout only; Claude had wrongly said to replace it.
> - **KR1e slide numbers, 10-19 (screenshots `screenshots/20261019-kr1e-slide/`).** MCP, Tanju explorer W38-W40 (to 10-04), Success+Failure cut: 171,991 ops, 625 orgs, 17,481 sessions, 91.1% success; weekly 42,297 / 59,677 / 70,017 (W38 matches the 09-28 slide exactly = same cut, so the rise is real); clients `exc_app` 55,622 (32%, AI Assistant + Coworker mixed) > Cursor 50,212 (29%) > Claude 24,945 (15%); top orgs after removing Sites Internal (19,072) and Adobe orgs: Microsoft Hotel 9,772, Bayer 9,260, medi 8,895, Swedbank 8,873. W41-W42 not yet published. Modernization, growth-lab W42: provisioned 6,032, active 3,154 (+14% vs W38, flat since W41), successful 1,226, Build & Publish 121 (90), Go Live 20 (13), live pages 72,086 (13,197 in W38; Timothee said 36,995 on 10-08, unverified jump, importer reworked 10-15), deployed 115,383, partners 72/82. Pedro asked Claude to write the slide text; Claude stated the rule once and wrote it ([[feedback_pedro_writes_claude_critiques]] override path). Links for both reports → [[reference_splunk_mcp]].
> - **SJ (10-20/21).** Tina's doc re-pasted 10-19, same as 10-13, none of the 10-13 fact checks fixed; full text in the SJ vault page. Pedro: audience = VPs and engineering managers from ~40 customers, hybrid. Claude's challenge (grilling format, unanswered): fix the "every skill is available today" opening; move the inventory to a form; a dedicated remote moderator; name the readout owner and soften "we take on"; a vote to pick the one blocker.
> - **🔎 KNOWLEDGE (P6):** [[Two Milestones Wearing One Word]] (10-15 release vs 2 Nov auto-provisioning); [[Lead the Slide With the Honest Read of Your Own Metric, Not the Flattering Number]] (live pages x5.5 held back until Mike confirms). No new entry.
>
> ### 🔴 2026-10-14 — SLACK CHECK: PEDRO'S "NOT BLOCKERS" LINE CONTRADICTED OVERNIGHT, HAVAS WANTS SJ DAY
> - **CXCO-230.** Pedro 10-13 16:52 `#cx-coworker-trial-rollout-core`: "the two PRs are not merged but they are not blockers for todays and next weeks activations" (confirmed with Yanira). Yelena 10-14 00:02: AEM rollout happened, next 10-20, PR not merged, "subset of customers using AEM Skills in Coworker will be blocked." Ian 10-06: CXCO-230 is the AEM Service Proxy PR that lets customers control traffic per environment (CDN rules with IP allow lists); needs a no-change-period exception. Unanswered at 09:46. https://adobe.enterprise.slack.com/archives/C0ABFLYLZK7/p1791928930767479
> - **Access control routing.** Kapil silent; Pritom Baruah answered 10-13 22:46 (Kapil and Mihai own it, outcomes + dates to come); Yanira: route such asks through Pritom. Pedro 10-14 09:25 stated the ask as admin controls access, "10+ large customers" blocked.
> - **Havas POP (Kevin Gerard-Moreau, Elise Lawley pointed to Pedro):** 30 min on Coworker for AEM Assets, with Workfront use cases, Tue 15:00 to 15:45 UK, ideally 10-20 (SJ). Unanswered.
> - **Yanira 10-13:** internal orgs sitting in AEM_SKU cohorts to go through the internal-org activation process (Paul, Yelena); Ashok Kumar parity tracking, Loni's ask, "EOM to restart". Pedro shared the opt-out grouping and the 7-day engagement (AEM Coworker WAU 304, AOv1 external 455 end August) in the Yanira+Tina group DM.
> - **Closed from 09-22:** NWL Brands (Siddharth's email route, Mohit Arora call, `ASSETS-78931`); Lénárd's webMCP regression (Mikaela's Unified Shell PR-12563, Corey tested OK). Still open: AEM per-plugin token budget pushes skill descriptions to name-only (Shubham). Gainsight step 6 still Pedro's in Sky, Merck, and Paul's ping.
> - **🔎 KNOWLEDGE:** CXCO-230 is an instance of [[Parallel Artifact Streams Diverge — Always Check the Latest Version]] at the level of status lines: the same fact reached the same channel twice with opposite values within eight hours, and per [[feedback_critique_check_facts_not_prose]] that is his exposure. Next time, lead with [[Surface the Risk Before Leadership Has to Ask]]. No new entry.

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
