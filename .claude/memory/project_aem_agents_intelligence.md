---
name: aem-agents-intelligence-aai-project-context
description: "Full context on Coworker Lead (renamed 2026-10-28 from AEM Agents Intelligence, AAI) — AEM on Coworker, agent reporting, AO 2.0 liaison, three-tier reporting, agent ownership, stakeholders. One of four projects; sisters project_experience_hub.md, project_release_management.md, project_security_health.md."
metadata: 
  node_type: memory
  type: project
  originSessionId: 5f12dcf1-db3b-44ce-bf6c-50e0a17cb9e9
---

> **🗂️ Four projects since 2026-10-28 (Pedro's call).** This project is now **Coworker Lead** (was AEM Agents Intelligence; this filename is kept so the archive links hold). Vault folder renamed `2026/AEM Agents Intelligence/AAI - Project Folder/` → `2026/Coworker Lead/Coworker Lead - Project Folder/`, Status → `Coworker Lead - Status and Todo.md`. Sisters: [[project_experience_hub]], [[project_release_management]] (release tasks moved there from this file's Status, 10-13 block), [[project_security_health]].
>
> **Two-project split — Phase 2 structurally complete (2026-05-13).** AAI vault folder was then at `2026/AEM Agents Intelligence/AAI - Project Folder/`. Companion `project_experience_hub.md` covers EH. Meeting Notes moved to neutral `2026/Meeting Notes/` (2026-05-13). AI-Assistant legacy folder retired. No legacy folders remain.

> **📦 Archive discipline (weekly shards; last restructure 2026-07-01).** Old context lives in per-ISO-week shards `project_aem_agents_intelligence_ARCHIVE_<year>-W<wk>.md` (+ long-form reference in `..._ARCHIVE_reference.md`), mapped by `..._ARCHIVE_INDEX.md`. **To find old context: read the INDEX first (dates + topics per shard), then `rtk proxy grep` the shard — never full-Read a shard.** This active file = hot state (currently **the 2026-09-01 session**; 07-15 → 07-27 archived to W29/W30 on 08-03, the 08-03 sweep + Agent Owners Alignment to **W32a** on 08-04, the two 08-04 blocks to **W32b** on 08-06, the **08-04 CLINT + 08-05 ROLLOUT SYNC blocks to W32 on 08-07**, the **08-05 AUDIT REPO + 08-06/07 AUDITS-WENT-PUBLIC blocks to W32 on 08-10**, and the **08-25/26 COHORT block to W35 on 09-02**) + the compact durable reference below. ⚠️ **The archiver moves dated blocks but does NOT move RESUME pointers — check the pointer still resolves after every run.** **Cap rule, enforced by `scripts/archive_memory.py` (run in `/consolidate` Step 5): keep this file < ~20K tokens / one-shot-readable; event blocks older than ~2 weeks auto-archive to their weekly shard + the index rebuilds.**
>
> ⚠️ **"moving 0 block(s)" HAS TWO CAUSES — DIAGNOSE BEFORE ACTING (2026-08-07).** (1) **The layout invariant below is broken** → the archiver cannot see the blocks. That is a bug, fix it. (2) **Every dated block is newer than `RETENTION_DAYS = 7`** → there is genuinely nothing it may move yet, which is correct behaviour on a dense week. **Check which one you are in before "fixing" anything.** On 2026-08-07 the file sat at **23.5K against a 24K read cap with every block under 7 days old**, so the only lever was **writing the blocks shorter** — the largest was a single 3.4K-token event block, trimmed to 2.2K. 🔑 **On a dense week the cap is a writing constraint, not an archiving one.** ✅ A **SessionStart hook now warns** when any session-start file approaches the cap (`scripts/archive_memory.py --check-startup`, wired in `.claude/settings.json`) — added because both prior truncation incidents were discovered by accident, never by a warning.
>
> 🔴 **LAYOUT INVARIANT, learned the hard way 2026-08-04 — DATED EVENT BLOCKS MUST SIT ABOVE THE LIVING-REFERENCE SECTIONS.** `split_active()` in the archiver treats the first non-blockquoted `## ` heading as the start of the living reference and everything after it as unmovable. This file had drifted so that four dated `> ###` blocks sat *below* `## 2026 Yearly Goal — G1`, so the archiver saw **one** block (the protected RESUME) and reported *"moving 0 block(s)"* while the file sat at **29K tokens, 5K past the read cap** — i.e. **the cap guard reported success while the file was silently truncating at session start, which is the exact 2026-06 awareness-loss failure it was built to prevent.** Fixed by reordering (content-preserving, verified line-multiset-identical), after which the same script moved 29K → 19K on the first try. **When appending a new dated block, put it directly after the RESUME, never at the end of the file.**

> ## ▶️ RESUME HERE — 2026-11-02 (full consolidation of the 10-29 session, no session 10-30 → 11-01; today's state only, rewritten each pass; older blocks via [[project_aem_agents_intelligence_ARCHIVE_INDEX]], the pre-10-29 pointer chain in [[project_aem_agents_intelligence_ARCHIVE_reference]])
> - **Moved 10-29.** Per-user access M1 has been in stage since 10-28 without the Admin Console sync the champions heard for end of November; Pedro took it to Kapil 10-29 21:30. AMEX (CXCW-787) is Pedro's, in Doing. Manik (Workday ILX "access denied") answered and emailed. Retiring the XL "AIA + Agents" section waits on Gabriel Walt's EMA call.
> - **Waits.** Kapil's answer (call outcome not captured). Horia on Babu's 11-02 forum (looks cancelled). Yanira on the Projects contacts and docs, then Pedro's reply to Corey (Projects GA before 11-10, Forrester). Namita on the beta setup. Aditi on the usage stories (first batch 11-11). Gina/Mark slot, Jing, Akin. Karthik's Rubin org-status filter (Databricks IP ACL, Sunidhi).
> - **Due today 11-02.** Namita follow-up; Gabriel nudge if silent; forum recap only if the forum ran. Late: Trent DM (~10-31); tell Bertrand he is named on rate card v2 (Tina wrote twice more).
> - **Risk.** "Access control by end of November" names two things, M1 (Coworker-local groups) and Admin Console profiles. If M1 is called done, the champions' ask stays open; Walmart's ASP beta is on hold for it.
>
> ### 🔴 2026-10-29 — SLACK SWEEP 10-28 EVENING → 10-29: M1 ACCESS CONTROL IS NOT WHAT THE CHAMPIONS HEARD, AMEX IS PEDRO'S, WORKDAY ILX GETS "ACCESS DENIED" (read 10-29 ~13:00-15:00 CET; Pedro's answers in session)
> - **Access control M1, in stage since 10-28.** Yanira's notes 10-28 21:54 CET (https://adobe.enterprise.slack.com/archives/C0BARAMM89Z/p1793220844576109): admin menu visible to a System Admin only, groups local to Coworker with no Admin Console sync, Coworker roles only. The champions heard "Admin Console profiles, end of November" on 10-20. **10-29 13:02:** turning M1 on cut Coworker on the stage org aem-sites-engineering; Paul Pop took the org out of access control and Coworker came back (https://adobe.enterprise.slack.com/archives/C0BQXNMHJJ0/p1793275367326779). Plan: wiki 4078318264 "Coworker Governance M1 Rollout Plan"; Yanira says a meeting with the PM is planned for the rollout. Rachel assigned **CXCW-628** "[Allianz] Access control and rollout governance" to Kapil 10-28 19:01: Allianz asks what Walmart asks. **Pedro 10-29: "Le controle d'acces sans Admin console est un bloquer pour moi et AEM"**, raised with Kapil 10-29 21:30; aim, a name and a date for the Admin Console sync. Outcome not captured.
> - **AMEX.** Rachel assigned **CXCW-787** "AMEX, Coworker <> AEM Integration" to Pedro 10-28 19:01 (Scoping); CXCW-785 "AMEX, Skills and playbook/template versioning" to Namita, same batch (https://adobe.enterprise.slack.com/archives/C0BL4DXTU30/p1793210467250629). JIRA 401, description unread. [[reference_coworker_pods]] said in August nobody was named AEM-side; this names Pedro. Pedro 10-29: "amex c'est pas fait - je dois faire / doing" (Claude had marked it done after giving the links; corrected, card in Doing).
> - **Workday ILX.** Manik Bhalla DM 10-28 18:30 (https://adobe.enterprise.slack.com/archives/D0C2GQMCSTU/p1793208654395959): org `D6FD298C63BC94730A495FC1` workday-ilx-aem is marked activated 09-22 in Pedro's Excel, the customer gets "access denied"; second org `0AB2768154D414A20A4C98A5`. The Excel is very likely `20260820-AEM_COHORTS.xlsx` (OneAEM SharePoint, internal, not customer facing), sent 09-17 the same morning to Daniel Mrose and Dan Balescu. Unverified lead: Workday opted out 09-15 over user-rights control ([[reference_customer_workday]]). Pedro answered and emailed 10-29.
> - **Projects GA.** Corey wants Projects GA in their demo org before 11-10 for the Forrester Wave, and asks the GA date and whether GA means on by default or provisioned (https://adobe.enterprise.slack.com/archives/C0BARAMM89Z/p1793210460483969 · `#forrester` https://adobe.enterprise.slack.com/archives/C0C90524YQJ/p1793226247503419; Mark Szulc there: "Where is CW Projects enabled? Is it GA?"). The only date seen is Yanira's "tentative Nov 2"; she says Projects runs on stage orgs (AEM Sites Team). Pedro asked Yanira 10-29 for the Projects contacts and docs, replies to Corey after.
> - **Smaller.** Babu's 11-02 forum looks cancelled (Aditi got cancellations for Monday's AEP meetings); Pedro asked Horia 10-29 13:57 (https://adobe.enterprise.slack.com/archives/C0CB0MC4KTQ/p1793278668100089); one correction line in the alignment channel if confirmed. Tina twice more unanswered ("Bertrand was already consulted", "not much has changed since it was shared with him"), Akin silent; pricing is Bertrand's. Soumya booked a slot 10-28 18:02. Cole brings back the tenant selector, hidden under "+" (the answer to Bertrand's 08-31 instance question). Namita asks whether Coworker can read DA (Jen Ciraldo's case, https://adobe.enterprise.slack.com/archives/C070SDG809J/p1793214825785049).
> - **Knowledge.** Two instances of [[Two Milestones Wearing One Word]]: "access control by end of November" (M1 local groups vs Admin Console profiles) and Corey's "GA = on by default or provisioned?"; dated instances added to the entry. H-010a: Allianz is an ask, no count change. The Kapil aim follows [[Say the Sentence That Obliges — the Hedge Transfers the Ask]] (ask for a name and a date). Watches → [[watches]].
>
> ### 🟡 2026-10-29 — XL DOCS: RETIRING THE "AIA + AGENTS" SECTION WAITS ON GABRIEL WALT'S CALL ON EMA (email thread pasted by Pedro 10-29, no link)
> - **Thread.** "AEM to Coworker Panel Updates Sync", later "… - Modernization Agent". **Alison Heimoz 10-20** (to Yanira, Pedro, Khushwant Singh, Alexandru Sarchiz, Anuj Kapoor, Rick Brough): Agentic Capabilities docs for Governance and EPA (Content Create, Content Update, Figma2CF) published 10-12; Governance pages and the three EPA detail pages redirected; EPA overview pages wait for the remaining Forms pages. Forms + Assets → Anuj, Khushwant; Development → Alexandru. "There does not seem to have been any information about the Moderization Agent"; Chris Bohnert (documented it, was OOO) had none either. "Please advise."
> - **Yanira 10-20:** EMA is Gabriel Walt's, Chris to follow up with him; "since EMA is not on Coworker. Most content should remain the same only perhaps match to 'Agentic capabilities' as discussed before instead of Agents". A position, not a decision ("let's see what Gabriel wants to change if anything"). **Alison 10-21:** asked Gabriel to "sync with Yanira, Pedro, and Chris as necessary", other writers to BCC.
> - **Yanira's follow-up (undated in the paste, after 10-21)** to Gabriel + Chris: "Can you share the latest status of EMA evaluation to move under Agentic Capabilities? We're pending this outcome to finalize retiring the AIA + Agents section in XL." No answer from Gabriel in the paste.
> - **Why it matters.** The last open piece of the AOv1 → Coworker docs move Bertrand called ahead of plan (10-27 block below). EMA runs its own chat, not Coworker. Pedro is named in Alison's ask; she wrote in public 09-02 that she had asked Pedro several times about OneAEM MCP docs without a reply (Stakeholder Map), so a second silent docs ask would repeat it. Pedro 10-29: "follow-up". Knowledge: [[Pick Up the Open Action Item]]. Watch → [[watches]].
>
> ### 🟡 2026-10-28 pm — PINGS OUT, THE SKILLS BETA ANSWERED, A WEEKLY COWORKER FORUM (detail in the blocks below and on the Kanban; release side in [[project_release_management]])
> - **Rate card v2.** Pedro to Tina 14:38 "do you know who decides for Q1 ?"; 16:59 Tina: Akin Ajayi + the BMS team drive it. Tina DM'd 17:00 (wrong channel, "pricing has always been a PMM area with collab w/ PM"). Pedro's first reply draft relayed Bertrand's 1-1 in stronger words than Bertrand used; caught before sending. Sent 17:19: the AEM concern is alignment with the Sites pricing redo, "Bertrand for AEM and Apoorva for Assets". **Pricing is Bertrand's, hard rule** ([[feedback_dont_trace_bertrand_owned]]).
> - **Skills beta.** Shankari pointed to Shelly Chiang's ASP co-innovation wiki (12 customers) within a minute; the reply-all to Namita went 15:51 (10-22 block below).
> - **Outreach.** Gina (Demo Hub call with Mark Szulc, Canberra; two slots proposed 16:08, Mark tagged but not a member of that DM). Soumya + Aditi 15:56. Jing + Aditi 16:00; the "working with Karthik" line was verified true afterwards (his Rubin org-status thread since 10-07, Sunidhi's DaaS tables in [[reference_aem_licensed_customers]]).
> - **Horia 15:54.** Babu Ramaraj's weekly "What's New & What's Next" Coworker forum from Mon 11-02, the answer to AEM's San Jose feedback. Pedro announced it in `#aem-agentic-owners-alignement` 16:42 and committed to a recap after each forum.
> - **Knowledge.** Instances of [[Say the Sentence That Obliges — the Hedge Transfers the Ask]] (asking for the owner's name got one in 2h20, then in one minute; two more @-mentions of non-members, Mark and Karthik) and [[How to Commit Political Suicide — Warning Patterns]] (near-miss, a manager's 1-1 relayed to a peer under pushback). Dated instances added to both entries.
>
> ### 🟢 2026-10-28 — PEDRO'S COWORKER PRIORITIES MAP (his iPad sketch, agreed in session; image `screenshots/20261028-coworker-priorities-map.png`)
> - **Five branches, in this order.** (1) **Adoption**: per-user access control first, named as the blocker (end of November promised to the champions vs Pedro's "plutôt janvier"), cohorts (Cohort 4_others), Tina's champions readout, Rubin + the usage stories with Aditi. (2) **Commercials**: Tina, per-operation ("API-based") pricing. (3) **AEM on Coworker roadmap**: persistent instructions (Trent), skills beta (Namita). (4) **Marketing**: Gina demos (Demo Hub), short videos ("TikTok", Guillaume, Aditi stories as material). (5) **Coworker roadmap**, to follow not to deliver: Projects, others.
> - **Why "Adoption" and not "clients et accès".** It can be measured, so it can become Pedro's H1'27 goal with a number: the slot his biggest lane lacks, without a central roadmap line ([[Your Biggest Lane Can Have No Slot in the System That Scores You]]). Release management and EH need their own maps. **Use this order at recall and in the Tuesday update.** The tasks themselves live on the Kanban board `Coworker Lead - Project Folder/Coworker Kanban.md` (Todo, Doing max 3, Done; card text `<branch> · <action>`), Pedro's option B, 10-28. **The tree is a Mermaid `flowchart LR` at the top of the Coworker Lead Status & Todo** (section "Coworker Priorities Tree", added 10-28 ~13:10 on Pedro's ask "est-ce que tu as re-créé mon arbre"). **Five branches only since 10-28 ~14:30** (task leaves removed on Pedro's go during the /consolidate review): the board is the single home of the tasks, the tree changes only when the branches do. 10-28 ~14:25, two Adoption cards added: ping **Soumya Sharma** (she leads Coworker adoption, DM 10-16) and reach out to **Jing You** (Coworker data scientist, 10-20 retention view naming AEM) for help on AEM adoption reporting; detail in the Stakeholder Map. **Coworker roadmap branch, 10-28 15:54:** Horia (group DM with Babu Ramaraj, Corey, Pedro; https://adobe.enterprise.slack.com/archives/C0CCYGSUQ9X/p1793199285484519), "on the topic we discussed last week" (Pedro and Corey told him at SJ that AEM finds Coworker hard to follow): a new weekly forum by Babu, "CX Enterprise Coworker (Core Product Release) | What's New & What's Next", demos across Projects, Governance, Context Intelligence, Memory, Skills & Tools, Gen UI/UX, plus shipping and roadmap; first Mon 11-02 8:35-9:30 PT (17:35 Basel), 45 accepted incl. Gina, Yelena, Huong. Neither Pedro nor Corey had the invite; both asked to forward. A concrete outcome of AEM's feedback, and the "follow" mechanism for branch 5.
>
> ### 🟢 2026-10-28 — BERTRAND WANTS AEM TO REPORT ITS OWN COWORKER USAGE STORIES FIRST, PEDRO PROPOSED THE FORMAT IN WRITING
> - **Source.** Rachel Hanessian's newsletter "The Adoption Pulse" issue 11 (10-26, central Coworker): customer spotlight Slalom ("We're just becoming reviewers and polishers and Coworker can do the 80, 90% of it", pages from Word, custom blog/newsroom skills, 200+ content fragments from one Excel). AEM usage, AEM not named. CX-wide numbers, not AEM: 2,925 orgs enabled, 1,455 used once, 3,332 WAU, 36.8% WoW retention; Workfront panel 188 → 1,460 orgs on 10-22. Tactic 1 says orgs opted out for lack of user-based access control (H-010a, central team's own words).
> - **Bertrand 10-28 07:54** to Rachel (cc Horia, Pedro, Aditi): update the prompt so the product piloted is attributed; if manual, what triggered the Slalom contact; "I would really like Pedro and Aditi to be able to report on these usage patterns first". Then to Aditi: would her analysis have surfaced Slalom.
> - **Context.** Bertrand assigned Aditi 07-28 to research how customers use the agents "in coordination with Yanira and Pedro" (Stakeholder Map). Her `AEM_Coworker_Customer Use case Analysis.pptx` (09-23) reads Rubin chats. Slalom quote origin not found in Slack or the vault; slalom.com gets weekly spacecat reports (likely on AEM, inference); Slalom also has a partner sandbox org `slalompartnersandboxamericas` (Ekta Kotadia `#asset-selector-integration` 09-10).
> - **Sent 10-28 ~10:45 CET, email to Aditi, Bertrand cc** (drafted by Claude at Pedro's explicit request, exact sent text not pasted): every 2 weeks 2-3 AEM customer stories; Aditi picks conversations in Rubin, Pedro checks the org is a real AEM customer (license, cohort, not partner or internal) and adds usage numbers; the best ones get a CSM call for the customer's words; same stories to Rachel's newsletter; Slalom org to check before counting it; first one Wed 11-11. Aditi is in San Jose (8 h behind until US DST ends 11-01).
> - **Sent text, pasted by Pedro 10-28 13:14** (10:47, To Bertrand + Aditi, not cc): "every 2 weeks, we send Bertrand 2-3 AEM coworker stories / You pick up the outstanding conversations from Rubin, / I check the org is a real AEM Customer (licence, cohort, not a partner or internal org) and add the usage numbers / We ask the CSME for contact with customer and get their own words / We then share the same stories with Rachel for her newsletter - AEM is named. / For Slalom, they have a partner sandbox org - checking which org they use and overall usage. / We aim for say November 11th ? … Bertrand - please chime in if you see it differently".
> - **Bertrand's reply (pasted 13:14):** "Slalom is also a real customer with real traffic - https://aemcs-workspace.adobe.com/customer/program/90156#domainNames (on top of having a sandbox as well) - so good to know if the report below related to prod or non prod". Nothing on the format or the date. **Answer found 13:18 (Pedro's other session):** the live usage is the customer org **SLALOM LLC** (`5EF652E2…7F000101`, Cohort_AEM_WF_TBYB, cohort 2, #2 of 64 orgs in the 10-27 Rubin sub-192 report; ⚠️ corrected 14:05: that report is sent daily but covers **the last 7 days, aem* skills only**, so "22-30 a day" was wrong, it is 22-30 per rolling week); the sandbox `slalompartnersandboxamericas` (`01A7B808561E59F17F000101@AdobeOrg`, p11802) had 4 Cloud Manager interactions 09-11 → 09-15 and none since; a third org, Slalom APAC Partner Sandbox, is in 0_Activated. ✅ Verified 13:24 (fluffyjaws.adobe.com): program 90156 = SLALOM, LLC, `5EF652E25570B5E77F000101@AdobeOrg`, the same org as the Rubin usage. **Answer to Bertrand = prod. Pedro sent the reply 10-28 ~14:00**, text pasted 14:13: prod, program 90156 / org ID; sandbox 4 interactions mid-September, zero since; 90 days 325 interactions, 6 users, 37% AEM skills, 32% Workfront (103/325, matches); blog/newsroom from Word, bulk CF edits in October, custom event skill; "200+ CFs from one Excel" not visible, Pedro checks with the customer team; "we now check the org, not the company"; asks Bertrand + Aditi ok for 11-11. ⚠️ It dates the Word-built pages "(10/11)"; the data says 09-10/11 (September). Write "September 10-11" in the 11-11 batch. Detail in the vault findings note. Rule fixed in the findings note: test the org (prod of a licensed program vs sandbox/internal/demo), not the company type. Pedro 13:14: Bertrand "répond sur ce qui me semble un détail, pas sur le process - c'est régulier et irritant". Read given: the detail is the hole in his "not a partner" rule, and no objection after "chime in" = consent ([[feedback_bertrand_concrete_first]]).
> - **The Slalom story checked on Rubin, Coworker only (`interactions_ao2`, ~13:33, counts no chat text).** Holds on data: blog/newsroom pages from Word (09-10/11: build-blog-from-doc 13, aem-sites-pages-create 12), bulk content-fragment work + custom skill `slalom-events-cf` (week of 10-05), Excel 3 interactions. Needs the customer: "200+ CFs from one Excel", "four people", the "80, 90%" quote. Workfront queries every week (85) = a separate story. First recall-ready AEM story for the 11-11 batch. Detail in the findings note. Lesson: Rubin's chat answers "AI Assistant" by default; name Coworker + the IMS org, ask the source table. **~13:41 overall:** 90 days, 325 Coworker interactions, 6 users, AEM 36.6%, zero AI Assistant v1, rank #38 of 518 orgs (518 likely includes internal/demo orgs: one more figure for the unreconciled denominator, not a reconciliation). 8 chats located (6 completed): blog/newsroom from Word ✅, bulk CF ✅, custom skills ✅, **"200+ CFs from one Excel" ❌ not confirmed** (the one Excel chat inspected/de-duplicated). ⚠️ Prompt 1 counted skill uses (09-07 week 139), prompt 2 interactions (81): quote interactions only.
> - **Read.** Aditi keeps her assignment; Pedro owns what counts as an AEM customer. Instance of [[Convergence Framing — Collapse Multiple Stakeholder Asks Into One Artifact]] (Bertrand's two asks + Pedro's 10-27 capsules idea → one biweekly artifact). ⚠️ "usage numbers" assumes Pedro can see Rubin per-org numbers; his own access was on legal hold. Watch → [[watches]].
>
> ### 🟡 2026-10-27 — BERTRAND 1-1: PEDRO DEFENDED THE DISTRIBUTED COWORKER ROADMAP, THE RATE CARD MOVES WITHOUT AEM, GINA RUNS DEMO HUB, MANAS IS LEAVING (transcript redone by Pedro 10-28, readable)
> - **Source.** Vault `Meeting Notes/Bertrand 1 1/20261027 - Bertrand Pedro 1 1_otter_ai_transcript.md`, replaced 10-28 by Pedro's second Otter run ("Point sur Coworker et Roadmap", ~28 min, ~14:15 CET, before Bertrand's H1'27 review; the first run was unreadable, backup in the session scratchpad). Status: AAI + EH Focus 2026-10-27.
> - **SJ readout.** Pedro met Yelena, Horia, Namita, Huong; Corey was there. Horia: "c'est le chaos chez nous", too many people and features, the Friday meeting became everyone's sync point. Forum feedback as in the 10-22 recap. Bertrand's video segment was well received.
> - **Manas is leaving (Bertrand, verbal, not confirmed).** In the recording Bertrand raises "le départ de Manas" (03:24) and says "je sais pas pourquoi"; "his decision" is not in the recording. Only Slack trace: Pedro to Yanira 10-28 11:24, "Betrand told me yesterday Manas is leaving (and that is his decision)" (https://adobe.enterprise.slack.com/archives/D018PT00155/p1793183075537689). No public announcement found 10-28. Pedro "didn't know 100%". Pedro works with Trent meanwhile.
> - **Persistent instructions.** Four layers: system prompt blocks (Adobe), business context (customer admin), project context (customer project team), memory (per user). Pedro places AEM instructions in the system prompt blocks, then per profile, to confirm with Trent. Bertrand tied it to Experience Context and business context. He missed the last Friday Coworker roadmap call; he noted schedulable agents.
> - **Projects and access control.** Pedro asked the Projects PM for one or two intro calls and enablement on a few AEM orgs; Bertrand interested in multi-user project conversations. User-level access: nothing to integrate on AEM's side, but AEM is frontline (who gets access, which customers first, the RCP, comms). Pedro: **"j'ai plutôt l'impression que ça va être janvier l'année prochaine."** ⚠️ The champions heard end of November ([[watches]] 10-20).
> - **Coworker as a roadmap line.** Bertrand's plan that day: Agentic Foundation with a Coworker dependency, Experience Context, no Coworker item as such; does foundation level (business context, permissions, coordination) need an item and people, or does it come for free? Pedro: central JIRA, no resources besides Brian for his team and Philippe for governance, Yanira and him, roadmaps at team level, "on était parti là-dessus le semestre passé, si tu veux changer je peux changer, mais je pense que ça fait sens". **He argued for the distributed model and offered to change; he did not claim the line.** His other top-level items: Razvan's (release management) and EH.
> - **Rate card.** Bertrand: a cost per operation instead of a flat 25 credits per prompt; he saw a Tina message that it advances and is worried it moves without AEM while Sites pricing is redone on the same principle. Pedro: ask Tina, get AEM into the discussion. Tina 10-28 05:33 `#aem-agentic` (to Apoorva): official pricing per level on Field Readiness, updated pricing not before Q1 (said Q4, may slip). Apoorva asked whether AEM gets a say on per-skill pricing.
> - **Release activation handed over** (last Thursday of the month, 17:00 CET; the passage the first transcript could not read). **Victor Mirica** (`vmirica`, Rolling Stones, covered Pedro's PTO) now runs it in Pedro's place to free operational time; Pedro stays in the loop. Bertrand agreed; chain roughly Nicu (manager), Razvan. Pedro's choice, not a scope transfer.
> - **Customer comms.** AOv1 → Coworker docs ahead of plan, AOv1 part can stop soon. Pedro: blog-style capsules from champion use cases, on the model of Bertrand's 5-min LinkedIn video. Bertrand: **Gina Casagrande runs Demo Hub**, published his video there and added it to the global Coworker docs. The Demo Hub matrix says AEM has a demo video, script and clickable demo; it does not. Bertrand met **Mark Szulc** ("Mark zuc"; ✅ 10-28 `mszulc`, Mgr Product Marketing, AEM agents demo owner) on demo scenarios: two needed, existing customers and new customers on Experience Workspace (Bertrand pushed Martin: Coworker is hidden "en mode headless" there). Pedro: docs with Guillaume Carlino; demos with Gina, including "ce qu'on dit qu'on a mais qu'on n'a pas". Bertrand: "c'est vraiment la bonne", also for other products.
> - **Read.** On the record, Pedro defended the distributed roadmap. **Pedro 10-28: keeps that position, "mais je comprends le problème"** (the lane has no slot in what scores him). The fix belongs in his own H1'27 goals, not in the product roadmap. [[Your Biggest Lane Can Have No Slot in the System That Scores You]] · [[H2 Planning Visibility — Own the Narrative Before It Gets Written Without You]]. Bertrand closed with "Demain je suis à ton bureau" (10-28); he was sick on 10-28 and did not come. Watch → [[watches]].
>
> ### 🟡 2026-10-27 — SUMMIT 2027 LABS: BERTRAND'S TEAM CANVAS HAS FOUR PROPOSALS, NONE FROM PEDRO
> - **Source.** Canvas `Summit 2027 Sessions and Labs` (https://adobe.enterprise.slack.com/docs/T02CAQ0B2/F0CAF0U4V43). Bertrand `#aem-cloud-foundation-pm` 10-19 09:01: "in our next team meeting, let's review our collective proposals for Summit (sessions and labs)"; 10-20 12:14: "please post your ideas" (https://adobe.enterprise.slack.com/archives/GTYKF4UAC/p1792393260820929). Pedro asked 10-27 to track it.
> - **On the canvas (owners not named in the body).** (1) AI discovery experience with LLM Apps; (2) agent-ready website with WebMCP; (3) DaaS x CDN: Content Request usage with the CDN Insights Agent in Coworker; (4) AEM CS developer productivity with IDE Agent Skills and Coworker (CM, CDN, Dispatcher, AEM, SRE): code assessment skill in VS Code + Copilot, "why is my site slow right now" ending in a patch Coworker merges and deploys to an RDE, traffic spike RCA, security posture patch.
> - **Comments 10-26 (positions, not acceptance).** Bertrand to Laurentiu Odoleanu 13:37: "maybe consolidate Lab 1 and Lab 2 as a single one? (same as a year ago with Content AI + LLM Apps?)". Bertrand to Brian Chaikelson + Shweta Dua 13:37: "looks good to me, can you please submit via Ron's form?"; Shweta 13:39: "Thanks ! Sure, will do". The section that comment anchors to is not readable; Shweta is DaaS, so likely lab 3.
> - **Process.** Labs go through Ron Nagy's form, deadline Mon 10-26 (Tracy Seibel `#aem-foundation-leadership` 10-21, "to be used vs. separate canvas", https://adobe.enterprise.slack.com/archives/C08KDFWL5GW/p1792610752427789). Speaker sessions have no open call (Mike Stiles `#summit-questions` 10-22: content strategy still being finalized with the exec team, https://adobe.enterprise.slack.com/archives/CDKFSPL0P/p1792682857310699).
> - **Read (inference).** Labs 3 and 4 put Coworker skills on the Summit stage; their GA status is not checked here (the Cloud Manager pipeline-troubleshooting skills were pulled from GA 09-16, EH memory 09-22 block). No lab on the canvas is Pedro's; the sessions call is the slot still open. Knowledge: [[The Vision-Reality Gap in AI Products]] · [[H2 Planning Visibility — Own the Narrative Before It Gets Written Without You]]. Watch → [[watches]].
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

Site Advisory Agent (AEMAGT-2, Laurentiu Odoleanu PM, Remus Stratulat ENG) is customer-facing, integrated with Brand Concierge, runs on Content AI — NOT in Pedro's 6. Reference page at `2026/Coworker Lead/Coworker Lead - Project Folder/Site Advisory Agent (AEMAGT-2).md` (move target Phase 2).

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

Draft saved April 24 at `Coworker Lead - Project Folder/Agent Reports/20260424 - Priority Consolidation View.md` (Phase 2 move target). Answers Loni's April 13 unanswered question (*"what % of top requests are making it into the agent"*).

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

**AAI canonical (post Phase 1 — 2026-05-03):** `2026/Coworker Lead/Coworker Lead - Project Folder/Status and Roadmap/Coworker Lead - Status and Todo.md`

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
