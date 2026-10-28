---
name: AEM Experience Hub project context
description: EH-only after Phase 2 vault split (2026-05-03). Surface, contribution model, Sorin team, O2 personalization KRs. AAI work in sister file.
type: project
originSessionId: 298c09b0-7372-4e27-9660-87019bb7d26c
---

> **Phase 2 vault split landed 2026-05-03.** AAI content (agent reporting, AO 2.0 liaison, Loni+JM May 11 deck, three-tier reporting, Felix/Rubin/Varun threads, Apoorva punch-list, KR3/4/5/6) lives in `project_aem_agents_intelligence.md`. This file is EH surface, contribution model, Sorin team, O2 personalization KRs only.

> ## ▶️ 🔴 2026-10-28 — RBI ESCALATION: THREE WEEKS OF PM SILENCE ON A RENEWAL-AT-RISK THREAD, PEDRO ANSWERED WITH THE UPDATE-FREE EXTENSION (release lane, kept EH-side)
> - **Source.** Email thread "RBI <> Adobe - Follow up meeting", pasted by Pedro 10-28. RBI = Raiffeisen Bank International (customer contact Pablo Cejas Romanelli). Account team: Patrick Hauzel (Account Manager FSI), Martin Floess, Markus Rogger (Sr Manager Enterprise Sales FSI). Giovanni Sarbia (Senior Cloud SME), Vlad Bailescu (EM Sites), Bertrand, Razvan (added by Bertrand 10-23).
> - **The ask.** RBI wants AEM updates at their own pace, monthly (discussed with Pedro 09-08), for regulatory reasons. Flagged ~6 months ago, escalated early September. Sales chased PM six times 10-07 → 10-20. Patrick 10-20: renewal and the AEM Cloud extension next year at risk. Giovanni 10-22: a possible slower-cadence SKU ("only Product Management can comment on or commit"); another RBI entity weighs on-prem → AEMaaCS next year; RBI is off RO again for a separate issue; his data says manual updates do not reduce regression risk. Vlad: Core Components version cannot be pinned. Next customer call **Tue 11-03**.
> - **Pedro's reply, sent 10-28 ~10:10 CET** (built from his 09:58 draft; which suggested edits he kept is not known): platform health and vulnerability fixes first; Update-Free extension for selected customers, 3 × 1 week → 10+ × 1 week per year; guardrail max 2-3 releases behind; interim monthly manual updates. Current limits (Experience League, checked 10-28): 3 Update-Free periods of 7 days per rolling 12 months, Quiet Hours max 8 h.
> - **Same limit, four customers in two weeks.** Norfolk asked 10 h Quiet Hours (Dharani 10-23; Pedro to Nicu 10-22: "Increase Quiet hours to 10h for one customer"). Microsoft (Doug Hicken 10-27 `#internal-aem-microsoft`: "Quiet hours and update free periods simple do not do what we need them to do"). UPS RO pause 11-01 → 01-11. RBI. A policy question, not a per-account reply.
> - **Read.** Release management is the lane Ramon proposed a Bucharest PM take over ([[watches]] CAREER section). A three-week PM silence on a Sales escalation with Bertrand cc'd is evidence for that proposal. Knowledge: [[Say the Sentence That Obliges — the Hedge Transfers the Ask]]. Watch → [[watches]].
> - **Also 10-27.** Pedro told Merit Vossmann (TAM; B. Braun account, inferred from "Congrats for BBraun takeover") that Visual Regressions will be decommissioned "over next months", announcement on the way, "date in around 6 months", and that she may say so to the customer. Her follow-up "what do we recommend using instead ? one of our agents?" was unanswered at 10-28 09:45. Not known whether this is the same tool as Fred-as-a-Service (09-22, "target of 6 months" to Amit Gupta). https://adobe.enterprise.slack.com/archives/D0CBFJ858TD/p1793110852430919
>
> ## ▶️ 🟡 2026-10-27 — BERTRAND 1-1, EH SIDE (low fidelity; full read: [[project_aem_agents_intelligence]] 2026-10-27 Bertrand block)
> - **Experience Workspace from EH.** Martin (Buergi, inference) relayed a customer wish to reach Experience Workspace from EH. Bertrand's idea: an EH widget listing the Experience Workspace environments per Cloud Manager program or project, with a link. Not settled, no owner.
> - Pedro told Bertrand his top-level roadmap items besides Coworker are Release Management (Razvan) and EH, an hour before the H1'27 review. Whether his canvas lines (due 10-26) were filled is still unchecked.
> - Eugene raised ("j'ai perdu Eugene"), Silvia named after; who covers EH design is not clear in the transcript. The 10-30 task stays. Knowledge: none apply beyond the AAI block.
>
> ## ▶️ 🟡 2026-10-23 — THE LEFT-NAV COWORKER ICON: UNIFIED SHELL SAYS IT WILL BLOCK IT AT RCP, AND GULIZ'S CONSISTENCY ASK POINTS THE OTHER WAY
> - **The block.** `#unifiedshell` thread, Adrian Ciulea 09-30, EXC-49877 (https://adobe.enterprise.slack.com/archives/CHU6PSRNY/p1790773859305559). Adrian's change gives the left-nav Coworker item the AIMark icon, the same one as the header Coworker button; the item already opens the right rail since 10-01. Mark Doten 10-02: "The left menu should only be for app navigation", "this is not normal and an anti pattern". Stephen Gould 10-02: apps that had the AIA header button keep that button for Coworker users. Bertrand 10-02: "ok - Adrian sorry for the extra work" (he accepted removal). Adrian reopened 10-15 after talking to Pedro and reading the analytics. Mark 10-15: "i still don't think you should keep it", "there's also an RCP, i don't expect an anti pattern to be approved for release", "why would we release something during RCP to support a feature that shouldn't exist?", "the button exists in the header already". Pedro 10-15: "We have 100+ users clicks on that button per week - I dont' want to remove now while we are in adoption period". The number is clicks from Adrian's analytics (about 100 a week), not users. RCP releases go through the AEP APPS Change Approval Board (https://wiki.corp.adobe.com/pages/viewpage.action?pageId=3816182757) and Mark submits the shell changes.
> - **Guliz 10-23**, alignment channel (https://adobe.enterprise.slack.com/archives/C0BARAMM89Z/p1792779005879539): the Cloud Manager Coworker rail implementation has the wrong icon, treatment and words; it should be "troubleshoot with Coworker", the wand head sparkle icon, the right button style. She asked Yanira to include design in Q&A for Coworker implementations. Brian Chaikelson opened `#tmp-aemcs-cm-coworker-design` (`C0CBQRKB6US`) with Laurentiu Odoleanu, Florin Florescu, Sergiu Coman, Silvia and Guliz; Yanira tagged Pedro. Same day in Martin's `#experience-workspace` WIP thread, Guliz: "As long as it's updated before customers see it".
> - **Pedro's position 10-23:** keep the left-nav item ("Le bouton a 100 clicks par semaine, je ne veux pas l'enlever maintenant"). A reply to Guliz was drafted at his request: EH and the left-nav item are his team's, the item stays during adoption and goes once most traffic moves to the header button, Silvia to confirm the icon so it can ship. His first-draft reaction ("bof") was to a version that asked design "which pattern to use", which read as conceding removal. **Not posted as of 10-27 10:30 CET** (thread read). Before posting: a one-line heads-up to Bertrand (he accepted removal 10-02); say clicks, not users; "wand head sparkle" = the header icon is unverified; CAB approval still goes through Mark.
> - **Read.** Guliz's consistency complaint is the argument for shipping the icon: an item that stays with the old icon is the inconsistency she objects to. A design yes on the icon weakens "a feature that shouldn't exist". Supersedes the open fallback question in the 10-14 block below. Watch → [[watches]].
> - Knowledge: instance of [[Govern a Consistency Layer Over Primitives You Don't Own]] (the seam blocking a deliverable; dated instance added to the entry, outcome pending) and [[Selection and Cross-Surface Consistency Are a PM Mandate]]; the exit condition follows [[Announce a Forced Surface Migration With an Opt-Out]].
>
> ## ▶️ 🔴 2026-10-22 — H1'27 PLANNING CLOSES BEFORE BERTRAND'S 10-27 REVIEW, AND EUGENE IS FADING OUT OF EH
> - **H1'27.** The canvas is `H1'27 Foundation Planning` (https://adobe.enterprise.slack.com/docs/T025FJ55H/F0C5A1D4GAJ); Tracy Seibel `#aem-foundation-leadership` 10-21: final In/Out reviews, Cloud Services & Security (Bertrand) **Tue 10-27 7-8 am PST** after Assets (Apoorva, Shankari); deck slides 2-22 built from the canvas; customer-facing roadmap due 11-20. Canvas rules: link each H2'26 line to an H1'27 DX initiative or close it, at least 5 HC per roadmap, one Invest label. Pedro on 10-14: "damn - missed the H127 planning".
> - **Pedro's lines.** SKYOPS-136515 Release Management Scalability (5 HC) and SKYOPS-136517 AI transformations of Rotary release tools (8 HC) still TBD under DX-1263; HOME-832 EH Product Adoption (4 HC in H2) still TBD. His three RS-EX H2 items sit inside shared CF roadmaps (H2 canvas F0AL123SP8D, matched on title and RS HC, not confirmed in JIRA): CSO → SKYOPS-137585 (RS 2), vulnerabilities → GRANITE-66668 (RS 1), EDA breaking changes → AEMAGT-1282 (RS 2); H1'27 successors SKYOPS-161584, GRANITE-75092 (no RS line yet), AEMAGT-2920 ("RS: ?"). The H2 canvas investment table names Pedro PM of CFRO (Release Mgmt, Content AI, LLMO DRS, LLM Apps, Repo Service) with two other PMs, under Razvan, 58 HC.
> - **EH HC.** Sorin DM 10-14: "I assume the HC are the same; right ? in experience hub and investment"; Pedro "Yes" (he had first typed "Dont we have 1 more ?" and struck it). So 4 HC, under the 5-HC minimum; the H1'27 Workforce table tags only 3 of Sorin's team to DX-1222. Open: is there a fifth, or does HOME-832 fold into DX-1281.
> - **🔴 Eugene.** Pedro to Sorin, DM 10-21 07:07: "Silvia informed me Eugene is fading out of EH - not sure you where aware". No date, no replacement named. EH loses its only designer while the nav-slot asks (Content AI, Unified Shell left-nav) are open. Watch → [[watches]].
> - Knowledge: [[H2 Planning Visibility — Own the Narrative Before It Gets Written Without You]] applies to the H1'27 canvas; [[Your Biggest Lane Can Have No Slot in the System That Scores You]] fits the CFRO PM listing (named in a table, three PMs, no roadmap line of his own beyond RS).
>
> ## ▶️ 🟡 2026-10-21 — WRITE ACCESS TO THE ANNOUNCEMENTS OWNERS SHEET IS GONE, AND PEDRO IS NOT THE ONLY ONE OFF THE ROW
> - Pedro 10-21: he can read but not write `https://da.live/sheet#/oneadobe/aem-experience-hub-announcements/announcements-owners`, signed in through Foundation Internal (IMS org `907136ED5D35CBF50A495CD4`). In the org config `https://da.live/config#/oneadobe/` the most specific path row decides, and the owners sheet sits at the site root, so **row 10** (`/aem-experience-hub-announcements/+**`, write) governs it.
> - Row 10 now names bohnert, pauli, ahosgood, pklassen, daurer, raga, buergi. **The group `907136ED5D35CBF50A495CD4/eh-announcements-da` is gone**, and so are slavic, chuesler, kozma, mhaack, cpeyer from the January config (Alexandre Capt, https://adobe.enterprise.slack.com/archives/C05QU7MMRNF/p1767869755149569). Reading, not confirmed: the row was rewritten and the group dropped, so everyone who wrote through the group lost write. Who rewrote it is not known.
> - Pedro's move: check the CONFIG write row (rows 1 to 9) for who can edit the config, then ask Mircea Salan (he set it up, https://adobe.enterprise.slack.com/archives/C08FV485MBQ/p1761554719459839), Sorin in copy, to restore the group in row 10 and add pedrofer@adobe.com. Sorin (slavic) is off the row too, so he may not be able to fix it himself. Pedro writes the message. Watch → [[watches]]. Knowledge: none apply.
> - Same day, a Cloud Manager announcement in the widget format, "Create an Edge Delivery site with AEM authoring, faster": title 55 characters, body 381 over three paragraphs, one em dash in paragraph 2. Author not confirmed in the session.
>
> ## ▶️ 🟡 2026-10-14 — UNIFIED SHELL CALLS THE LEFT-NAV COWORKER ITEM AN ANTI-PATTERN
> - Adrian Ciulea DM 10-13 15:09: while aligning the left-nav Coworker icon with the top-right button, the Unified Shell discussion concluded the left-menu Coworker item should go, top button only. Open: fallback when the panel is not available (keep the left item opening full-page Coworker?). Sync with Adrian 10-14 am, Pedro pinging the Coworker PM. Sits next to the Content AI ask (10-13): both are about what owns the slot above the fold. Instance of [[Selection and Cross-Surface Consistency Are a PM Mandate]] and [[Govern a Consistency Layer Over Primitives You Don't Own]]. https://adobe.enterprise.slack.com/archives/D0BHLEE6UCX
>
> ## ▶️ 🟡 2026-10-13 — CONTENT AI WANTS THE SPOT ABOVE COWORKER IN THE EH NAV
> - Mircea Salan 10-12 (group DM `C0BPMFYLTJL`, Pedro + Eugene tagged): a request to move the Content AI nav item under Home, before Coworker. Pedro 10-13 10:29: "i would keep Coworker 'first'", and asked Mihai Copae who the requester is. Requester not named yet; Peter Klassen asked 09-10 to position Content AI in the navigation pane. Instance of [[Selection and Cross-Surface Consistency Are a PM Mandate]]: the nav order is the EH front door, and Pedro held it this time.
>
> ## ▶️ 🟡 2026-09-22 — SLACK AUDIT 09-16 → 09-22, EH SIDE (full read: [[project_aem_agents_intelligence]] 2026-09-22 block)
> - **🟢 The nav asks are moving without a go from Pedro.** Adrian Ciulea 09-22: "I will be taking care of adding the LLM Apps menu item"; Sorin opened `HOME-926`, Laurentiu wrote the spec, asked Pedro for feedback (DM 09-22: "Looks very good!… Sorin has more experience"). Eugene 09-16: the Product Announcements widget already supports targeted, flagged announcements, use it for LLM Apps; wants a call with Pedro + Sorin + Laurentiu (Laurentiu "will set something up", 09-21). Pedro to Laurentiu 09-22: "one EDS page per announcement… image + text… click more for info", modelled on Brand Concierge.
> - **🟢 Announcements.** Pedro 09-22 11:11 `#experience-hub`: wants a Coworker Panel announcement, asked for the BC page with "the great design". Mihai Copae had already posted 09-18 in `#aem-bc-trial`: BC trial activate page updated to Peter Klassen's design, preview on stage (AEM FCCS2 Stage org, "Show me" button). Pedro 09-16 `#aem-cloud-foundation-pm`: kudos to Peter, "we'll pivot to request a similar design for next announcements".
> - **🔴 Guliz 09-16 DM: "I need you to add Silvia or me to every Coworker panel meeting… I really need to be there for anything CW related. I'll tell you why later."** Pedro agreed. Pritom Baruah dropped into the Coworker rollout sync proposing "alignment post GA on Coworker UI collaboration"; Pedro read it as wanting to drive; Guliz: "strange things are happening". Guliz also shared the Projects MVP roadmap; Pedro to sync with Horia. The "why later" is not on record.
> - **🟢 Pipeline troubleshooting button.** Temp channel `#tmp-cw-pipeline-activation-ui` 09-16 (Pedro): skills pulled for GA, button still live. Sorin 09-16: keep it, best effort. Sergiu: no, avoid disappointment. **Brian 09-17: remove the button until the AOv1-style implementation returns, Coworker version "a few weeks".** Pedro's plan 09-22 (to Tina/Yanira, then Brian): re-wire AOv1 into Coworker skills, keep the new-gen work with Manas/Trent, full switch "some weeks still".
> - **🟢 Ramon.** Support view shipped in Unified Shell 09-17 at `experience.adobe.com/#/aem/heimdall-security` (read-only for `AEMSecAlpha` and `Skyline SRE`, fetches what EH shows: Security Health, pen tests, CMK). Developers Live recording done with Ron. **He still needs the EH-priorities meeting with Pedro.**
> - **📦** Rotary calendar updated by Nicu 09-16 (Vlad's ask done); Assets code freeze 09-29, URR authoritative. Fred-as-a-Service: Pedro told Amit Gupta 09-22 "progressively de-commission… target of 6 months". `#experience-workspace-cm` (09-21): Felix Meschberger's brand-bucket model vs Bertrand's CM-program control plane; Ian: fix the EDS FQDN first, automate via CM APIs. Prodesp channel silent since 09-04.
> - **📝 12:38 — the Coworker Panel announcement, his to write.** He asked for text on the BC announcement pattern (chapeau · two-line title · one concrete subline · CTA). Rule said once, then three title options given (author-outcome first: "Your AEM assistant now lives in the page."; the product-name one last), two sublines, two CTAs. Three checks before it ships: the name ("CX Enterprise Coworker" is the session title and the popup text, Tina/Akin hold the official one); flag-target only the activated orgs (Eugene 09-16: the widget supports it), because the date is disputed and "Show me" must not open nothing; drop "fix" if it points at the four Development skills out of GA since 09-08. [[feedback_pedro_writes_claude_critiques]] · [[feedback_audit_outward_artifacts]].
> - ⚠️ **Tenth consecutive flag on the EH Status & Todo `Current Status`**, seventeen weeks. Pedro's to refresh.
>
> ## ▶️ 🔴 2026-09-16 — THE PANEL ACTIVATION NEEDS EH IN RODSON'S CHANNEL, AND THREE TEAMS WANT EH REAL ESTATE
> - **🔴 Panel activation is EH's front-door work now.** The AEM panel is announce 09-24 / TBYB activation the week after / SKU 10-05 (AAI 2026-09-16 block). Pedro asked 09-16 where to connect Rodson Clavel with the EH team → `#cxue-coworker-panel-hybrid-collaborators` `C0BCKG35NFP` (Rodson's; pinned activation recipe; Tim Lynn, Mark Doten, Mikaela Symanovich and Josh answer there; Bertrand is in, the EH team is not). Sorin, Eugene, Mihai and Adrian to be added; Pedro's own 09-01 activation thread there is dead after Philippe's 09-03 question. CORS and custom-domain rendering live in `#aem-wildcard-cors-enablement` `C0BTZS3APGF` — Mikaela's shell-domain render is becoming the real solution, not a temp fix; customer author domains land "in January" (Mark Doten 09-11).
> - **🔵 The instance-switcher question got an answer without AEM.** Peter Klassen, 09-07, in Bertrand's 08-31 `#p42-architecture` thread: "the plan is to consolidate with One AEM MCP - with NLS i believe choosing content sources would become obsolete." Pedro was not in the thread; whether that is EH's answer is his to say. Cole's instance-picker outline still owed.
> - **🔴 Three asks for EH real estate in one week.** Laurentiu Odoleanu 09-09 `#experience-hub`: Adobe LLM Apps in the left nav between UE and CM, GA November, feature flag for internal tenants first (Sorin) — asks Pedro's go. Peter Klassen DM 09-10: "ok to position Content AI there in the Navigation Pane?" Prodesp (Alexandre Boldrin, 09-04 then a nudge 09-11, `#tmp-prodesp-no-eh`): restrict EH per profile for politically isolated municipalities; EH deep links reach author features that were disabled, Cloud Manager visible without a product profile (`CMGR-72725`); Sorin apologised 09-14, "we will review and figure out an answer". Instances of [[Selection and Cross-Surface Consistency Are a PM Mandate]].
> - **🟢 Announcements and the release lane.** Mihai Copae 09-11 design proposals (Pedro: "I think i like it ! Specially the first one"), 09-14 improvements on stage (bigger title and image, centred, scrollable long content) awaiting feedback; wiki "How to create an announcement" 3696785260. Sorin 09-09: the LLM Optimizer announcement tenant list is being updated with Andrei Chiriac, flag re-enabled later that week. Ramon 09-16: Developers Live recording done with Ron (Security Scanning → Experience Hub → Claude + AEM MCP), support-view changes on Unified Shell 09-17, and he needs an EH-priorities meeting with Pedro. Vlad Bailescu 09-16: update the `uber-release-registry` dashboard with the new Rotary schedule.
> - ⚠️ **Ninth consecutive flag on the EH Status & Todo `Current Status`**, sixteen weeks. Pedro's to refresh.
>
> ## ▶️ 🔴 2026-09-02/03 — THE PLACEMENT QUESTION GOT ANSWERED BY A DATE, AND BERTRAND ASKED THE INSTANCE-SWITCHER QUESTION IN PUBLIC
> - **🔴 Lianne Ramos, 09-02 01:02, `#cx-coworker-trial-rollout-core`:** the AEM tab of Paul Midura's *Cohort 3* file is the list of AEM customers gaining Coworker on **09-08**; she asked for the AEM Gainsight *"You will soon have access to Coworker!"* alert to be deployed ~a week ahead (i.e. 09-02) and a reply in her thread once done. **This is the 07-15 Rachel / 08-05 Huong placement ask, now with a customer date on it.** No written EH placement decision exists; the alert is going out through the central channel regardless. Watch → [[watches]].
> - **🔵 Bertrand, 08-31 `#p42-architecture`:** saw a Coworker demo showing the *"active"* Workfront instance under the prompt; asks whether AEM wants the same, an active CS or AMS instance with a switch between AEM contexts *"as we do in the Experience Hub from the left hand side rail"*, Eugene tagged. **Unanswered. It is the front-door selection problem stated by Bertrand himself, and it is the instance-picker outline Cole Connelly owes.** Instance of [[Selection and Cross-Surface Consistency Are a PM Mandate]].
> - ⚠️ **Eighth consecutive flag on the EH Status & Todo `Current Status`**, now ~14½ weeks behind. Not banner-stacked; Pedro's to refresh.
>
## About Experience Hub

AEM Experience Hub is the unified home screen / landing page for AEM Cloud Service at experience.adobe.com. Launched August 2024. Previously named AEM Home and AEM Launchpad. Not a replacement for existing AEM UIs. An action-oriented entry point that surfaces the right tools per persona.

**Current PM:** User (took over from Shankari March 2026.)

**Org:** User → Bertrand (Senior Director PM) → Loni (VP PM for AEM)

**Obsidian vault root:** `/Users/pedrofer/ObsidianAdobeVault/020 Professional/Adobe/Projects/2026/Experience Hub/`

---

## 2026 Yearly Review Goals (drafted with Bertrand, April 2026)

**G1 — Agent Intelligence & Reporting (now AAI scope):** see `project_aem_agents_intelligence.md`. Listed here for completeness — built and owned via the AAI surface.

**G2 — EH Platform Integration:** Own Experience Hub's integration with AEP and Adobe DX, including AO 2.0 migration and the new agent prompting surface. Ensure EH remains a reliable and current entry point as the underlying platform evolves.

**G3 — Experience Hub Adoption & Growth:** Establish Experience Hub as the measurable driver of AEM practitioner adoption growth, with data and narrative that leadership can point to at any level. Document and attribute EH's contribution to AEM monthly active user growth. Deliver the contribution model and user profiling that make EH contextual and extensible, and enable other teams to surface their work through EH as a shared platform.

File: `AEM EH - Key Files/Experience Hub - 2026 Yearly Review Goals.md`

---

## Team and Capacity (confirmed April 1, 2026 Sorin 1:1)

Pedro is PM of record. Team: Sorin Slavic (lead engineer), Eugene Bannykh (UX, US timezone), Mircea Salan (engineer, internship project lead), Anna Maria (intern).

Effectively 1 engineer. Sorin split across multiple projects. Anna Maria cannot contribute meaningfully near-term. Mikhail and Anastasia departed around the same time she arrived. Hiring pipeline open: best case May 1 first hire, June 1 second. Worst case: summer or positions closed. Roadmap declares 3 (1 + 2 in progress) for planning. Headcount minimum for roadmap: 5. EH bundled under Growth and Adoption.

Sorin's framing: "We are not a big house, but we are a proud house."

**Eugene Bannykh's manager:** Silvia Mulet Ferre (Sr Product Design Manager, Adobe Design, Austin) → Guliz Sicotte → Archana Thiagarajan → Eric Snowden (SVP Adobe Design) → David Wadhwani. Adobe Design is a separate VP chain, NOT AEP — relevant for cross-org coordination on EH UX.

---

## 3 Product Priorities for 2H2026

**Priority 1 — Skills + MCP surface**
Replace generic prompt grid with skills-aware, MCP-connection-aware chat surface. AO 2.0 lands May–July — right moment to redesign. Bertrand brief drafted (`EH as the Skills and MCP Surface - Bertrand brief.md`). Hold until Eugene's design view reviewed and MCP current state confirmed with Sorin.

**Priority 2 — Contribution Model / UX AI Framework**
Full alignment Pedro + Eugene + Sorin (April 1). Sorin independently drafting — main focus for 2 open reqs (UX + AI). Pilot mechanism: +Add Extension (App Builder, React SPA, IMS identity). Mircea Salan demoed March 27 — not production-ready. Known gaps: feature flag not activated, App Registry instability, stage-to-prod manual command, iframe context injection limited to user profile only, wizard needs simplification.

**Priority 3 — Customer Profiling**
5 profiles (General, Content Author, Asset Librarian, Developer, Admin). Bertrand deprioritized. Pedro's reframe: profiling is the mechanism that makes Priority 1 contextual, not a standalone ask. Don't raise until Skills+MCP is validated.

---

## 2H Roadmap

HOME-832 in JIRA (created April 1, 2026) — four H2 initiative descriptions: AI Assistant Integration Improvements, Collaboration Model Implementation, User Profiling Research, Supporting Teams and Promotional Surface. Working draft: `Home 2H2026 Roadmap - Experience Hub EH.md`. Canva roadmap planning doc still to be located and shared with Sorin.

---

## EH as MAU Driver — Claim to Own

Bertrand quote in April 13 Loni meeting: *"I would like to think that what we did with Experience Hub has been a key driver in expanding the number of monthly active users for AEM."* >60% customer base. Pedro's product. Surface this claim explicitly — own it, back it with data, make it a narrative Pedro controls. Stable metrics deck (KR5) is one vehicle. Grafana access obtained April 8 — cross-check vs Felix reports outstanding.

---

## EH Surface Integrations

### Brand Concierge Light-up — Summit Deadline (April 19-22, 2026)

Three options discussed in April 1 refinement sync. Sorin confirmed full production implementation is too late. Eugene designed wizard ~1 month ago. Bertrand contributed to shaping. Content AI indexing takes hours — can't be faked on customer side. Cloud Manager micro frontend PR (Peter's team) still open. Decision sent to Bertrand + Peter. Effective answer deadline April 2.

### Experimentation Page Integration (Jim Stoklosa's team)

Experimentation page is a full-screen landing page + sub-pages, not a widget. True to Eugene's mockups. Not all customers get it — contextual experimentation is an extension, not a default entitlement. Available across all AEM flavors.

EH responsibility: feature flag + navigation button visibility logic. Business logic (which tenants see it) defined by experiments team via API condition — EH maintains it but cannot define it alone. Micro frontend implementation: experiments team's responsibility (same model as security team). Sub-pages: experiments team must declare them so EH can manage pathing. Recent widget: experiments team should onboard their noun to unified shell recent service.

Jim's team: Dereje Dilnesaw (required), Julien Ramboz (required), Sanjeev Verma (optional). Slack sent April 1; Dereje responded April 8.

### Prompt Search (April 2 EH Demo)

Unified search for assets via AI assistant prompt (click +) is almost done. Returns results from first production repository user has access to — same as semantic search in AEM Assets. Bug confirmed: pulls from first prod repo only (context bug). Working with CJ analytics team on tracking gap between displayed and recorded prompts. Search still only covers assets — pages, content fragments, experiments, launches not included. Context bug (multi-environment users default to first prod env) still open.

### Adoption Data (April 2 EH Demo)

- Growth stable but stuck — Sorin: "stuck at 85%"
- Return users stable at ~62%
- New user count is dropping
- Prompt suggestions: steady views. "Content or knowledge" prompts most used.
- Analytics tracking bug: gap between what's shown and what's recorded — working with CJ analytics team

---

## Fu Chi (AEP Personalization) — EH-side personalization owner

Fu Chi (AEP team) built the personalized prompt recommendation pipeline. Weekly 1:1 with Pedro. Shankari was invited to first sessions.

**Architecture she owns:**
- Pipeline: user prompts → clean → embeddings → K-means clustering → topic reports
- Signal blending: user history (primary) → org signals (fallback) → global signals
- Output: CSV/table of user IDs + ranked prompt recommendations
- EH owns prompt bar + buttons. AEP owns right rail.
- Prompt library is centralized — agent owners can enrich it

**Already exists in her data:** behavioral cluster analysis (content authoring, asset focus, cloud manager usage) — raw material for Priority 3 (Customer Profiling). Real, not hypothetical.

**Workflow-aware recommendations** (suggest next action based on prior steps) on her roadmap, not yet prioritized.

**Open actions with Fu Chi:**
- Fu Chi to share prompt recommendation file
- Fu Chi to share Analytics DB wiki page for widget recommendation analysis
- Fu Chi to send draft email + spreadsheet for agent owner prompt review (March 25 ask — status unclear)
- Fu Chi to share Workfront persona use case (March 25 ask)
- Pedro to review prompt file with Sorin + schedule follow-up

---

## Cross-VP — Prompt Library Platform (O2 KR `EH consumes prompt library not wiki`)

Added April 28, 2026:

- PM: Cole Connelly (Principal PM, NY)
- EM: Joshua Hailpern. Lead engineers: Somya Biswari, Zeus Courtois.
- Org chain: Cole → Stephen Gould (GPM, SF) → Tim Lott (Director, Lehi) → Daniel Sheinberg (Sr Director) → **Sunil Menon (VP, Experience Cloud Portfolio, SJ)** → Amit Ahuja → Anil Chakravarthy.
- **Sunil Menon = peer of Loni Stark at VP level** under Amit Ahuja. Prompt Library Platform sits in his tree, NOT in AEM/Loni's.
- Right ladder: tactical Pedro→Cole, strategic Pedro→Stephen Gould (also Pedro's existing DX/Unified Shell contact), portfolio decisions Loni→Sunil at VP layer.
- Org-chart screenshots: `screenshots/20260428-org-*.png`.
- **2026-05-19 bridge:** Joshua Hailpern (EM here) also leads AIA UI / Mithril / Fruitbar; Somya Biswari + Zeus Courtois are lead engineers on both. Prompt Library Platform and Mithril/Fruitbar = same engineering galaxy under Sunil Menon's tree. Full note in `project_aem_agents_intelligence.md` "May 19 — Engineering bridge".

---

## Interpersonal Watch (cross-cutting, kept EH-side)

| Person | Dynamic | Notes |
|---|---|---|
| Philippe Kapfer | Senior PM under Bertrand. Scope: Governance Agent + Security. Arrived 2 years after Pedro. Took security perimeter from Pedro. Potential promotion competitor — actively building Loni visibility. | Tactic: agree 1:1, create dissent in front of the boss (April 2). Pattern to break: hold position under public pressure, don't retract. Recovery path: reintroduce concerns as technical requirements, not debates. Use Corey Dulimba as first testeur for unpolished work, NOT Philippe. Treat as competitor, not ally. He doesn't attack — he makes you applaud him. |

---

## Sorin Workstream — Active Threads

### Data Compliance — Risk accepted (Bertrand, April 1, 2026)

Ian Boston (April 1) confirmed two legal risks with the agent reporting pipeline (data residency cross-region pull, governance/deposition risk). **Bertrand's decision (April 1):** "Ian's comments are important but not critical. We continue with Felix." Decision logged in `/decisions/2026-04-01-data-compliance-continue-felix.md`. Pipeline ownership lives AAI-side now; EH carries the surface implication only — the EH integration does not introduce additional compliance scope.

### Open Outreach (April 2, 2026 baseline)

| Person | Topic | Status |
|---|---|---|
| Ilya Grafutko | QI program synergy | Met April 14 |
| Ian Boston | Regional data aggregation | Confirmed two legal risks April 1 |
| Bertrand | Data compliance | Risk accepted April 1 — closed |
| Peter Klassen | Brand Concierge light-up option | Responded April 2 (full proposal) |
| Jim Stoklosa + team | Experimentation page onboarding call | Dereje responded April 8 |

---

## EH Status & Todo (Obsidian) + Key Files

All paths relative to: `/Users/pedrofer/ObsidianAdobeVault/020 Professional/Adobe/Projects/2026/Experience Hub/AEM Experience Hub - Project Folder/`

- Status & Todo: `AEM EH Status and Roadmap/Experience Hub - Status and Todo.md` (renamed from `EH - Status and Todo.md` 2026-05-03)
- Bertrand 1-1 questions: `AEM EH - Key Files/Experience Hub - Questions for Next 1-1 with Bertrand.md` (cross-cutting, kept EH-side)
- Sorin 1-1 questions: `AEM EH - Key Files/Experience Hub - Questions for Next 1-1 with Sorin.md`
- State of Project: `AEM EH - Key Files/Experience Hub - State of the Project.md`
- Stakeholder Map: `AEM EH - Key Files/Experience Hub - Stakeholder Map.md`
- 2H Roadmap draft: `Roadmap/Home 2H2026 Roadmap - Experience Hub EH.md`
- EH Evolutions proposal: `202603 - EH Evolutions proposal.md`
- Bertrand brief: `EH as the Skills and MCP Surface - Bertrand brief.md`
- MOC: `🎯 AEM Experience Hub MOC.md`
- Meeting notes folder: **moved out of EH folder 2026-05-13** → `/2026/Meeting Notes/` (neutral, shared with AAI and other projects). Previously `Adobe Projects 2026 Meeting Notes/` under EH project folder. Rename + move applied because folder content (Bertrand, Felix, Namita, Ian, Yanira 1-1s) was cross-cutting, not EH-specific.

---

## Slack Channels (EH-relevant)

`#experience-hub`, `#experience-hub-ai-assistant`, `#aem-home-platform-team`, `#aem-home-core-team`, `#temp-experiencehub-dxue`, AEM experience hub extension builder.

---

## Reporting chain

⚠️ Corrected 2026-10-22: Shankari is no longer in the chain (paper manager for ~1 month in spring 2026 only). Pedro → Bertrand (Sr Director PM, Basel) → Loni Stark (VP AEM & Commerce, SJ) → Amit Ahuja → Anil Chakravarthy → Shantanu Narayen. Arrangement temporary — Shankari moving to report directly under Loni on a 6-month trial. Pedro's check-ins go directly to Bertrand. Loni's actual title: **VP, AEM & Commerce** (PM + Product Marketing).

---

## May 5 Bertrand 1-1 — EH-side drop-ins

Source: `Meeting Notes/Bertrand 1 1/20260505 - Bertrand Pedro 1 1_otter_ai_transcript.txt`. AAI signals in sister memory file.

**Mithril / Coworker (Joshua Hailpern team).** AI Assistant V2 with "mode rail" (observer + suggestion). Launching ~late May (T-25 days). **AEM Sites NOT included** — repeat exclusion pattern (also Modernization Agent + Experience Workspace). Bertrand asked Sorin + Eugene to do Mithril review. Pedro saw UI via night Slack May 4. Bertrand: *"Ça va être un point important pour la migration AOv2 si on y va."* Bertrand actioned: chase Guliz on XD/Adobe-Design loop visibility.

**Marcus Räck (Experience Workspace creator).** Declined Pedro's unified-chat ask: *"je pense qu'il faut chaque solution ait son propre tchat."* 4 chats now (Experience Workspace, Modernization, Slick, Rosetta=Manager Services). ⚠️ **"Slick" + "Rosetta" = low-confidence names** — from a garbled May 5 Otter auto-transcript (*"sleek… le chat dans Rosetta qui est la version manette services"*, Unknown Speaker; "manette services" = mis-heard "Manager Services"). Pedro didn't recall the names 2026-05-28, will verify later. Don't assert as canonical until confirmed. Pedro pushing common substrate (history, context). Bertrand views chat unification as AOv2-migration-relevant.

**Cédric Huesler — repair contact.** Pedro got him annoyed via Slack push on AOv2 + contribution model May 5 morning. Tactical contact for Experience Workspace + AOv2-on-Sites discussions.

**Sylvia Mulet Ferre auto-fix-prompt initiative for EH.** Sylvia (Eugene's manager, Adobe Design / Guliz tree) launching: hypothesis = users come once and stop because request too complicated from start. Bertrand skeptical: *"je sais pas trop où elles vont venir avec ça."* Track scope + intersection w/ Eugene.

**Customer migration pattern.** 1-year migration deadline approach. Decouple "platform update" vs "platform move." Nico's content-repo migration initiative waking customers up — many need re-migration with hard deadlines.

**EH headcount note.** *"On va avoir 2 personnes qui sont remplacées pour Experience Hub. On va être de trop"* (Bertrand).

---

## May 12 — Bertrand 1-1 EH-side drop-ins

Source: `Meeting Notes/Bertrand 1 1/20260512 - Bertrand Pedro 1 1.md`. AAI-side content in sister memory.

**1. 🆕 Quiet Hours Update via Agents — beta launching.** Activated on ID. Customers run **Quiet Hours-Update via the chatbot/agent** (free). Beta cohort: (customers who previously used Quiet Hours Update) ∩ (customers w/ AI) = **81 customers** to activate. Expect dozens of feedback. **Ties O4 (Ship Quiet Hours).** Concrete proof point for May 11 deck "customer trust increase" slide. Companion to Bertrand customer-trust slide (Pedro to add quote-worth slots).

**2. 🆕 Breaking changes manager — name rename needed.** Raspberry team finds "breaking changes" too negative. Concept stays: central repo declaring breaking changes w/ dates, impacted customers, procedures, docs. For ~120 customers internal use + customer-facing awareness. Pedro action: source new name.

**3. 🆕 Two new EH hires start beginning of June.** ✅ CONFIRMED started 2026-06-01 (Pedro, 2026-07-03) — the System Review "did they start?" flag is closed; onboarding plan still open. Resolves Bertrand May 5 *"2 personnes remplacées pour EH"* note. Profiles:
- One ex-AEP.
- One full-stack AI engineer (*"qui fait pas mal d'AI"*).
- Bertrand: *"ça peut vous aider à coder plein de trucs."* Capacity inflection for EH eng (Sorin = 1 effective today).

**4. Customer update push state — O6 lever.** ~120 customers behind on Content Fragments / content freshness. ~100 still behind. **Aldi (7-8 programs) + Volkswagen + Americans** = key targets. Plan: propose manual update first → automatic update later. **1-year window option:** customer commits to test impl + monthly platform updates while staying off auto-update. CSM one-by-one outreach. Mostly positive responses to progressive migration. Ties to O6 Aging Customers (slipped end-March KR).

**5. AOv2 + skills + context framing.** EH-relevant fragments: cross-surface AI-Assistant continuity Bertrand wants (chat history retrievable across surfaces); Michael compliance pushback (data residency primary-region constraint). Open product question for EH surface = where does the AI Assistant icon route post-Mithril (per-surface context vs global Assistant). Full AOv2 framing in AAI memory.

**6. Sylvia auto-fix-prompt initiative status.** Bertrand May 5 flagged. May 12 update: Sylvia "very actively" in contact with Tim Lynn (Mithril). Pedro coached her to synchronize w/ Guliz but hedge on AOv2. Bertrand: Gilles + Michael had AOv2-counterpart meeting with Manas + Ken — relayed *"v1 was very complicated."*

**Pedro action items from EH side:**
- Slot Quiet-Hours-via-Agents 81-customer beta into May 11 deck customer-trust slide.
- Find rename for "Breaking changes manager."
- Verify Grafana JSON-size issue post-Raul-list-fix before next exec demo (cross-cutting, also AAI).
- Confirm AI Assistant SKU/pricing model w/ Bertrand (cross-link Mithril Silvia pricing question).
- Onboard plan for 2 June hires.

---

## May 12 — Mithril Silvia Eugene Pedro sync (EH-side anchor)

Source: `Meeting Notes/Eugene/20260512 - Mythril Silvia Eugene Pedro Sync.md`. Full notes in AAI memory. EH-side anchor:

- Silvia use case = **context-reading, not UI-interaction.** *"We don't want AI to interact with UI. We want AI to read UI."* Mithril MVP misses this.
- Eugene framing: post-Mithril, AI Assistant icon becomes contextual per surface (pipeline, etc.). Pre-Mithril = dummy shortcut everywhere.
- 🆕 **Matthew** = Mithril co-owner alongside Tim Lynn. Surname TBD. Tomorrow May 13 Silvia + Eugene + Tim + Matthew sync. Pedro not invited — Silvia reports back.
- 🆕 Migration window UX problem: multi-month window with mixed v1/v2/migrating agents. User confusion on which has skills/Mithril. Mitigation = in-app notifications (Silvia). Eugene: low risk currently.
- 🆕 Pricing question: AI Assistant free or paid? Affects failure tolerance. Pedro action: confirm w/ Bertrand.
- Pedro→Silvia: relayed Loni reframe (*"maybe v2 not the correct question, list requirements"*) — same Loni reframe Bertrand reported at P42 hours later. Converging signal.

**EH action:** send Silvia engineering-manager-per-AEM-agent list (Guliz-assigned design POV on AOv2).

---

## May 12 — Cross-cutting Loni reframe (full content AAI-side)

Loni reframe verbatim — *"No, that's not the question. Question is context, and how do we equip our agents with proper context."* Strategic anchor at VP level. Connects EH (Mithril context-reading primitive ask) ↔ AAI (Ian's North Star architecture for AEM agents AOv2). Same axis, two surfaces. Full context in AAI memory; EH-side relevance = context-reading on Mithril is the **visible UI expression** of the strategic context-architecture pivot.

---

## May 22 — EH's role in the distributed-harness model (Ian NorthStar exchange)

Ian Boston's Agentic NorthStar + the May 19-22 thread reshape how EH should be positioned. Full AAI-side record in `project_aem_agents_intelligence.md` "May 22 — Ian NorthStar thread".

In the distributed-harness model **the UI decides which harness/agent to call** (Ian: explicit/prompted selection, not auto intent-detection), and **cross-surface consistency is vital + PM-led** (Ian: *"an Adobe user feels like it is the same surface regardless of implementation details or UI engineering ownership"*).

**This makes EH (and the agent surfaces) the selection + consistency layer for AEM agents — not just a launchpad.** EH's job grows into: (a) the surface where practitioners select / are prompted toward the right agent (the selection UX Pedro now PM-leads, Ian on record), and (b) the consistency layer that makes distributed, independently-owned agent UIs feel like one Adobe surface (the answer to the 4-chats fragmentation: Experience Workspace / Modernization / Slick / Mithril).

Ties to: EH Priority 1 (Skills+MCP surface), the contribution model, Eugene's per-surface contextual AI Assistant icon, Mithril context-reading (Silvia — context-reading powers good prompted selection), and Pedro's convergence push (now architect-backed). Strategic upgrade to EH's narrative: **EH = the practitioner-facing selection + consistency layer in Adobe's distributed agent architecture.**

---

## Sister project

`project_aem_agents_intelligence.md` — agent reporting platform, AO 2.0 liaison, three-tier reporting, Loni+JM May 11 deck, H-005 resolved, Felix/Rubin/Varun threads, Apoorva punch-list, KR3/4/5/6, AEMEO-9508 Data Advisory Agent overlap watch, Vaishnav PMM signal, broadcast-rep muscle. **+ May 12 Loni reframe + Ian = North Star architect + Ian one-pager deliverable + May 13 Felix/Lara 3-way (External Agent naming, $2K/mo cost data, Mark Pfaff).**
