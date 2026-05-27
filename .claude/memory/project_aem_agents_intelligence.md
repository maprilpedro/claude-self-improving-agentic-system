---
name: aem-agents-intelligence-aai-project-context
description: "Full context on the AEM Agents Intelligence project — agent reporting platform, AO 2.0 liaison, Loni+JM May 11 deck, three-tier reporting, agent ownership, AAI stakeholders. Sister file to project_experience_hub.md."
metadata: 
  node_type: memory
  type: project
  originSessionId: 5f12dcf1-db3b-44ce-bf6c-50e0a17cb9e9
---

> **Two-project split — Phase 2 structurally complete (2026-05-13).** AAI vault folder at `2026/AEM Agents Intelligence/AAI - Project Folder/`. Companion `project_experience_hub.md` covers EH. Meeting Notes moved to neutral `2026/Meeting Notes/` (2026-05-13). AI-Assistant legacy folder retired. No legacy folders remain.

> ## ⏱ Consolidation checkpoint — 2026-05-19 (staleness flags, NOT new facts)
>
> Session summary: [[20260519 - Session Summary]] (May 18 Agent Owners Alignment ingested, Pedro hosted). Date-driven items now past — confirm outcomes, don't assume:
> - 🔴 **Loni + JM deck (week of May 11)** — meeting window passed. Outcome NOT captured. Debrief ask: did it happen, what landed, what's the follow-up. This is the single biggest open.
> - 🔴 **SD-1 / SD-2 / SD-3** (due May 6/8) + **KR4 Priority Consolidation** (due May 8) — all past due, status uncaptured. Reconcile.
> - 🟡 **Felix/Lara Langfuse Governance pipeline** — PR merge Fri May 15 → data due Mon May 18 (yesterday). Confirm landed + integration started.
> - 🔴 **Workshop Foundation facilitator** — captured as HIGH PRIORITY Bertrand 1-1 item (block in `Experience Hub - Questions for Next 1-1 with Bertrand.md`). Lead the next 1-1 with it. No longer "decide" — the decision is accept; the action is say-yes-to-Bertrand-with-the-May-18-link.
> - 🟢 **Ian North Star 1-pager — LANDED 2026-05-19** (was NOT started as of May 18). Ian published [Agentic NorthStar](https://wiki.corp.adobe.com/spaces/~boston/blog/2026/05/19/3894002388/Agentic+NorthStar) as a blog the day after the call Pedro hosted (where Pedro publicly named Ian owner). Gating artifact RESOLVED — escalation/forcing-function no longer needed. Pedro lane flips to respond + distribute. Full entry: "May 19 — Ian publishes Agentic NorthStar" below.
> - 🟡 **CCF / ISO 42001 — scope NARROWED (May 18).** No longer all AEM agents → **Discovery + Governance only** this year. Loni+Bertrand finalizing exact list. July 17 deadline holds. Bertrand: *"important but not urgent, not top of stack."* Downgrade from 🔴.
> - 🔴 **Roadmap deck restructure** — Bertrand cut date **Fri May 22** (snapshot → design agency), **final Fri May 29** (broad distribution). Per-agent overview + timeline + skill-detail slides. Pedro's 6 agents need coverage.
> - 🔴 **Greg Klebus customer escalation** — Rosh + Genentech, multi-IMS-org agent scope (AOv1 = 1 org limit). Ian pulled into customer arch conversations. Feed into requirements + North Star.
> - 🟢 **Corey call** — Tue May 19 (today). On track.
> - **Apoorva punch-list** April deadlines all past — confirm closed vs slipped.
>
> Apply: when Pedro references any of the above, ASK for current state before reusing the memory value. Memory is point-in-time; these are expired.

AEM Agents Intelligence (AAI) is the agent-portfolio reporting and strategy work Pedro owns inside the AEM PM org. It is distinct from Experience Hub (EH, the AEM home-screen product). AAI maps to G1 (Agent Intelligence & Reporting). EH maps to G2 + G3.

**Pedro's role:** PM of record for AEM agent intelligence reporting. Named PM liaison AEM ↔ AO (Bertrand, April 14, 2026). Drives Felix reports, Priority Consolidation view, Portfolio Monthly Briefing, AEM-AO SLA. Owner of AAI surface for the May 11 Loni + Jean-Michel deck.

**Counterparts:** Yanira Castaneda (PgM AO-tracked agents — Pedro's PgM counterpart). Apoorva Gupta (Discovery Agent PM, validation gate). Felix Delval (data engineer, report pipeline). Lara (taxonomy + Governance reporting). Varun Kalra (Discovery validator). Karthik Penikalapati (Rubin technical lead). Conrad Woltge (Sr Principal Architect, AO liaison). Trent Davies + Ken Russell (AO eng). Sergey Generalov (AO PM). Jaclyn Eckersley (FinOps, AEM Eng VP-side).

**Org chain:** Pedro → Shankari → Bertrand (Sr Director PM) → Loni Stark (VP AEM & Commerce). Bertrand also reports laterally with Jean-Michel Pittet (VP Eng AEM, Basel) on agent strategy.

**Obsidian vault:** `/Users/pedrofer/Library/CloudStorage/GoogleDrive-maprilpedro@gmail.com/My Drive/ObsidianVault/020 Professional/Adobe/Projects/2026/AEM Agents Intelligence/AAI - Project Folder/`

**OKR home:** `/120 Projects/Work/OKRs/O1 - AI Agent Intelligence/` (KRs already AAI-correct: Apoorva punch-list, Loni+JM presentation, Priority Consolidation, agent owner sign-offs, monthly metrics deck, AEM-AO SLA, BVR Discovery methodology).

---

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

---

## Felix reports + report pipeline

**LIVE for EPA.** Shared with Bertrand April 9. Bertrand named Pedro and the dashboard in Loni's H2 planning meeting April 13 — public sponsorship at VP level. Conrad validated in Agent Owner alignment same day. Jim Stoklosa feedback incorporated April 13.

**Report-to-JIRA pipeline.** Tested with Governance Agent. Validated by Varun (April 22): useful IF end-to-end inside same UI; not useful as separate skill. Need JIRA column with ticket + end date per action item. MCP idea (Gilles Knobloch) — parking lot.

**Report hosting.** Certificate approved by Shankari April 9. Felix + Quentin configuring CDN + Okta path. Unblocked.

**Jim Stoklosa role:** prepares EPA reports for Corey Dulimba. Validation role = data accuracy + feature behavior. Corey = PM owner sign-off (lighter ask, but required for Loni path).

**Audit Sprint April 30:** 9 of 16 audit items closed in single day. 10 PRs. Wave 1 Tier 1 (5 trust-hygiene), Wave 2 Tier 2 (4 visible-commitment), 2 of Tier 3 early. Plus 2 Important Indicators (#4 No-Results Triage, #5 Owner column on Capability Gap Map). Plus monthly retention shipped (PR #55) revealing **45% weekly orgs vs 71.2% monthly orgs stickiness gap** on Discovery W17.

---

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

## Varun Kalra Discovery sync (April 22, 2026) — strategic signal

**Platform legitimacy signal:** Varun voluntarily offered to retire his own wiki and consolidate into Pedro's platform. Quote: *"I want to get away from it because you're already doing a lot of work on this. I want to streamline and finalize on how we can ensure that there's only one way we are creating the final reports."* First peer agent-owner team to choose Pedro's platform as canonical. Senior Director-level scope signal.

**Measurement reframe — intent-level, not interaction-level.** Varun's correction on Apoorva's 3 VR metrics: First Useful Result Rate, Query Unsuccessful Rate, Remaining Prompts Rate sum to 100% **only at intent level**, not interaction/chat level. One intent can span multiple interactions. Rules:
- Intent returned nothing → Query Unsuccessful
- Intent returned results, no follow-up within ~2 minutes → First Useful Result
- Intent required follow-up refinements → Remaining Prompts

2-minute window is Apoorva-hypothesis, needs confirmation.

**"No results found" is a product gap, not a legitimate answer.** Varun's framing: in agentic UX, "no results" = failure to engage. Correct minimum response = clarifying question or suggestion. Discovery uses single response for unsupported queries / content doesn't exist / search-quality failures — collapses triage. Governance Agent's "I cannot help with this" is the better model.

**Varun's deep skill — to absorb into Pedro's platform.** Multi-source analysis for zero-result Discovery queries. Combines prompt + code + Splunk logs + live AEM instance. Categorizes zero-results: standard/semantic search, page searches, forms, content fragments, custom metadata, unsupported. Per-agent custom block in Pedro's platform. Pfizer "Cephalon" typo case = exemplar.

**Report UI feedback:** weekly trends to top, externals count at top (externals > internals surprised Varun), graphs interactive (good), repeat-users 1-week window OK for now.

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

**Pedro named PM AEM-AO liaison April 14, 2026.** When Jaclyn asked "who's responsible for AO, the connection with AO?", Bertrand: **"It's Pedro."** Sergey on AO side. Public, in front of Conrad, Jaclyn, Yanira. Significant visibility.

**AO 2.0 = different product, not backward-compatible** (per Conrad April 14):
- AO 1: central orchestration, central code base, central team incorporating all changes.
- AO 2.0: harness. Different surfaces. Different build model. Plugin / marketplace architecture. Anthropic open protocols. Small subsets, run in Adobe environment or customer cloud. Teams contribute skills + take responsibility.
- V1 stays operational in parallel — no forced migration.

**AOv2 architecture:** AO codebase = `github.com/Adobe-Experience-Platform/ao`. AOv2 = plugin/marketplace. Pattern: install AO local → create marketplace git repo (template `OneAdobe/ao-plugin-extensions-template`) → develop plugins/skills → install marketplace into AO. Internal docs: `aep-ao.pages.adobeitc.com/getting-started/` and `/plugin-development/`. Manas Garg leads dev experience push. Core AO team: Trent Davies, Ken Russell, Sergey Generalov, Akash Maharaj, Alexander Falca. CJA team engaging via Josh Butikofer.

**Conrad on AO 1 adoption:** *"Widely not flying based on usage data. Nobody's using really heavily except maybe EPA. And EPA has JIRA surface and not even orchestrator."*

**Loni's frame (via Jaclyn, KR review + April 21):** *"We cannot just be at the mercy of somebody else. We need to have our own strategy of what we want to do."* AEM owns its agent strategy, not following AEP by default. Durable frame for May 11 deck.

**April 29 strategy session outcome.** 2-hour block, Bertrand + Conrad + Yanira + Jaclyn + Ian + Carsten + Trent + Ken. Notes at `Meeting Notes/Agent Owner Alignement/20260429 - Alignment_ AEM Agents & AOv2.md`.

**Status (corrected 2026-05-04 by Bertrand post-meeting):** AOv2 as AEM's forward agent path was **discussed, not decided.** Do NOT present as locked decision. Bertrand explicitly flagged this when Pedro began drafting Yanira's introduction.

**What was actually agreed (directional, not commitment):**
- AEM A2A servers decommissioned — removes parallel infra (agreed in principle, timeline not set).
- Internal-open-source engagement model with AO team (PRs, forks) — preferred working mode.
- Scope split direction: AEM owns use cases + practitioner experience + customer co-innovation + agent definitions. AO 2.0 owns harness + runtime + orchestrator. Treat as direction, not contract.
- Bertrand framing line (his words, usable as quote): *"I would prefer us, AEM, to focus on the AEM use cases rather than building technology if there's a dedicated team for the infrastructure around it."*

**Open / unresolved (do NOT close in Yanira intro):**
- Forward-path commitment to AOv2 — open.
- AO 1 → AO 2.0 backward compatibility — open since April 14.
- AEM-AO SLA scope (KR6) — Pedro liaison, scoping in progress.
- A2A decommission timeline — open.

**April 29 deep transcript pass (added 2026-05-05).** 4160-line Otter transcript at `Agent Owner Alignement/20260429 - Alignment_ AEM Agents & AOv2.md` re-read in full. New signals beyond post-meeting summary:

*Architecture pivot (V1 → V2):*
- **Thin-orchestrator + fat-agents** (V1) **→ fat-central-agent + thin-agents** (V2). Fundamental rewrite. Implications for AEM agent harness ownership not yet drawn.
- Trent 1:23:07: AOv2 origin = reactive post-Opus-4.5 pivot. *"Suddenly behind, like our direction is completely wrong. And so we just completely pivoted. Migration plan has been secondary."* AOv2 NOT a stable platform yet — read carefully before betting AEM roadmap on it.
- Skills > MCP. Trent (head of AO) at 43:xx: *"in my personal use of agents, I find that I don't use mcp hardly at all."* Ken: *"mcp is a special tool"* (40:03) — demoted from layer to tool. Bertrand defended MCP-first 44:21 — *"I'm just a bit worried in the back of my mind that mcp becomes like the Swiss knife."* AEM has invested heavily in MCP-on-top-of-agents — re-evaluate posture given AO leadership skepticism.
- Marketplace = **per-team repos**, not central monorepo. Wells Fargo precedent: per-customer marketplace. AEM may be expected to ship its own.
- AOv2 lives at `ao.adobe.io` **side-by-side** with V1, not unified-shell-first (Trent 1:43:32). Counter to assumed unified-shell integration.
- Conrad 1:42:51 translation rule: *"weeks is translated into years in AM market landscape. So when you say 4 weeks, then people hear it's like 4 years."*

*Decisions landed (verbatim-anchored):*
- **V2 = direction.** Conrad 1:48:42: *"V2 is something we want to pursue and will replace what we have in V1."* But: 1:55:39 Bertrand BASL close: *"A meeting where we end with more questions than answers is a very good meeting."* — Pedro's "discussion not decision" framing holds.
- **A2A decommission for AEM specifically.** Conrad → Carsten 1:39:16: *"decision is yours, decommission and done."* Note nuance: AOv2 still supports A2A federation (Trent 1:20:39) — AEM's own A2A layer is what gets retired.
- **MCP confirmed primary AEM-into-AOv2 channel** by Carsten 1:12:53. EPA = canonical use case ("experience production main use case around mcp").
- **Reuse existing AEP-AO collab Slack channel** — Pedro suggested 1:12:12, Conrad agreed 1:12:18. No new channel.
- **AEM contribution path = PRs into AOv2 repo.** Trent 1:46:39: *"fork it, push, push PRs, file issues, complaints, feature requests."* Conrad commits 1:46:51: *"we know the code base, we can send you PRs."* Internal-open-source contribution model formalized.
- **Conrad's directive lands "next week"** to all agent owners (1:54:30). Forcing function. Trent disclaimed authority 1:22:37 (*"I won't presume to say that I can tell you what it should be"*) — Conrad is the actual decision-maker.

*Pedro's contributions (chunk 3 = his hour, full verbatim record):*
- 1:15:28 — surfaced **AEM Context project**. Trent labeled it *"the North Star question"* (1:16:11). Strong positioning win — flagged at AO leadership level. Lever for May 11 deck.
- 1:21:27 — pushed AOv2 vs A2A vs native-skills decision pressure. Critiqued Discovery Agent native-skills approach (Raul's experiment): *"felt very developer-centric… exposing way too much of the underlying implementation for what I think a practitioner would expect from an agent."* Flag — careful using this in front of Apoorva/Raul.
- 1:26:10 — convergence ask: **Experience Workspace** (3-panel UI for AEM Sites — AI coworker / admin UI / preview) should be AOv2, not yet-another-assistant.
- 1:27:32 — full convergence framing: *"Slicky… Experience Workspace… Experience Modernization Agent (cloud code on Ethos)… all aim at solving one thing, running a harness somewhere properly. I'd love to see them converge, and if AO 2.0 is the thing, I'd love that to be possible."*
- 1:28:17 — **the framing line, in Pedro's voice**: *"I would prefer us, AM, to focus on the AM use cases rather than building technology if there's a dedicated team for the infrastructure around it."* Use this as walk-out line — sourced to Pedro, not retrofitted to Bertrand.
- 1:29:11 — *"I don't think anyone has decided anything… we all learning about it."* This is Pedro's discussion-not-decision frame in real time. Holds.
- 1:29:42 / 1:30:51 — pressed Trent on **manifest customer-exposure configurability**: can AEM hide parts of marketplace UI from customers? Unresolved.
- Action item Pedro accepted: provide **Experience Workspace demo** to Conrad — Gilles or Michel (Knobloch) candidate demoer; Pedro to share recording.

*Bertrand's framing (full):*
- MCP-as-Swiss-knife concern (44:xx) — defended AEM's MCP-first investment vs Trent's MCP-skeptic posture. Tension still open.
- Multi-role / product-profile model for AOv2 admin (1:32:39, 1:33:01) — sys admin vs practitioner profile in admin console.
- **Pricing / SKU bombshell** 1:49:46–1:52:57: per-agent credit model + dedicated AI SKU may not survive AOv2 (skills collapse the per-agent unit). 1:52:32: *"didn't realise the consequences go to market-wise and pricing-wise before this meeting."* **Bertrand self-assigned to answer.** Adds AEM AI SKU risk to the May 11 conversation.
- BASL close 1:55:39: *"A meeting where we end with more questions than answers is a very good meeting. I have no problem with that. I think we achieve something."* Conrad concurs 1:55:49: *"We have much better questions now."*

*Felix:* did NOT speak in April 29 transcript. Felix's critique — that low-level agent owners had not been involved — surfaces in the **May 4** meeting, not here.

*Other speakers — Trent's signature concession on evals:*
- **Skill-level evals = UNSOLVED** in AOv2. Trent 1:37:56: *"I don't think we have that fully fleshed out the way you're describing Ian yet… it's a hard problem to solve, given how skills work, because the agent may or may not load any number of skills."* **Pedro's three-tier reporting platform has no AOv2 skill-granularity counterpart.** Position as gap AEM helps close — leverage for May 11 deck.

*New open items (add to AAI tracking):*
- Manifest customer-exposure configurability (Pedro's open ask 1:29:42 / 1:30:51) — follow up with Trent / Manas.
- AEM Context project ↔ AOv2 skills-and-tools layers — Trent labeled North Star, no joint workstream defined. Define one.
- Convergence ask: Slicky / Experience Workspace / Modernization-agent / AOv2 — no owner, no decision. Pedro is the convergence advocate; needs Bertrand alignment.
- Slick + AOv2 coexistence — Trent action item ("I'll have to think about Slack"), watch for resolution.
- Pricing / SKU under skills model — Bertrand self-assigned. AEM AI SKU + credit-tracking system may not survive.
- AEM AOv2 contribution path opened — pick first PR target (small one, low cost, high signal).
- Skill-level evals gap — frame as opportunity, not blocker.
- AOv2 mandatory or optional for AEM — Trent declined to legislate; Conrad directive next week is the forcing function.

*Quote bank (May 11 deck-ready):*
- Pedro framing line: *"I would prefer us, AEM, to focus on the AEM use cases rather than building technology if there's a dedicated team for the infrastructure around it."*
- Trent on AEM Context: *"the North Star question."*
- Conrad on V2: *"V2 is something we want to pursue and will replace what we have in V1."*
- Conrad on agentic monetization: *"you cannot sell any product in a short future if it is not AI enabled. So the skill harness might be a mandatory thing to sell AEM at all"* (1:53:19) — Bertrand's pricing question in the room.
- Bertrand BASL close: *"A meeting where we end with more questions than answers is a very good meeting."*
- Conrad summary: *"We have much better questions now."*
- Loni durable frame (April 21, still relevant): *"We cannot just be at the mercy of somebody else."*

**May 4 Agent Owners Alignement update (Pedro delivered).** Notes: `Agent Owner Alignement/20260504 - Agent Owners Alignement.md`. Pedro delivered the cautious framing in front of agent owners (Bertrand + Conrad off): *"There was no decision taken during the meeting... future discussions and synchronizations between Bertrand, Conrad, and the various teams, although early feedback from Conrad was pretty positive on V2."* Held the line — no pre-emption of Conrad's directive.

**New signals from May 4 meeting:**
- **Corey Dulimba (EPA) urgency:** *"This is becoming relatively urgent because we all have H2 roadmaps."* Asked for timeframes. Pedro deferred — Bertrand + Conrad off, won't commit dates on their behalf. **H2 roadmap risk if directive slips past mid-May.**
- **Felix Delval critique:** *"discussion that involved the low level, like all of the agent owner. And from my perspective, very little has been done at this level."* Wants per-agent migration validation to start **NOW**, not post-directive. *"the moment we decide it's a go live, we will have like weeks before we should all migrate."*
- **Raul Hudea status:** team has started on easier agents — auth gaps surfacing as first migration friction. Validates Felix's framing.
- **Yanira action:** *"I'll start a thread in AEM agents and then you guys can jump and see who might, how we can get started."* AEM agents Slack thread for AOv2 owner-level migration scoping. Watch for thread, contribute Pedro angle.

**ISO 42001 / Tech GRC compliance audit (NEW, May 4 — Robert Guthrie raised).** Brand-new compliance controls for AI services based on **ISO 42001**. ~12-13 tickets, similar to Nov-Dec CCF compliance work. **Audit starts June. Evidence due July 17.** Robert: *"I never saw this work on any of the roadmap discussions"* — trying to reach Loni, JM, Bertrand. **May force H2 roadmap changes across all agents.** Source: Amit. Track in Status & Todo as 🔴 — surface to Bertrand before May 11 deck (this is exactly the kind of "I want to make sure that Lonnie and everybody above is understanding" Robert flagged).

**CSO process split — Pedro action item (May 4).** Felix flagged need to separate business agent CSO vs technical agent CSO. Brian: each CSO must map to actual oncall team (don't wake wrong team). Pedro accepted action: *"Yeah, I'll take the point."* Status & Todo task created.

**Reporting demo (May 4) — landed:** Pedro showed Governance monthly retention (4-week return, increasing) + Philippe's brand-checks BVR metric implemented in reporting. Next: ping Brian + Corey for their BVR metrics. Pattern of contribution model working in practice — Philippe's team contributed metric directly.

**Corey + Gilles post-summit lab (May 4 opener).** EPA workbook with pluggable AEM playground instance — fills variables automatically. Highlights Discovery + Governance too. Open invitation for other agents to add labs. Possible asset for Loni+JM May 11 (customer-getting-started narrative).

**AI Assistant vs AOP — Pedro's mental model** (canonical: `AAI - Project Folder/AO 2.0/AI Assistant vs AOP.md`):
- **AI Assistant** = conversational/generative AI layer. The "brain." LLM-powered. Fuzzy / open-ended.
- **AOP** = Adobe Orchestration Platform. The "hands." Backend orchestration, deterministic execution.
- AI Assistant interprets request → AOP orchestrates execution.

**AEP AO / AI Assistant role split** (per Ilya Grafutko Slack 2026-04-27):
- AO Platform PM: `@sgeneralov` (core, integrations) + `@igrafutko` (quality / safety / compliance)
- AI Assistant PM: **Rachel Hanessian** (`@hanessia`) (Adoption) + `@namitak` Namita (Dashboards, AI Integration, AI quality)
- AO v2 (coworker): `@sgeneralov` + `@igrafutko`
- AO v2 — AIA extensions: `@namitak` + **Rachel Hanessian** (`@hanessia`)

For AEP Grafana dashboard issues (Agents traffic): ping Namita (`@namitak`).

**AEM-AO SLA scope (KR6).** Pedro PM liaison since April 14. Jaclyn ask triggered by recent AO CSO (response too slow). Open question: defined SLAs AEM-AO as internal vendor? Conrad + Trent + Sergey are AO-side counterparts. AO 2.0 backward compatibility unresolved (April 14 — Bertrand + Yanira + Jaclyn + Conrad in room, none could confirm). SLA-level commitment to push: "AO 2.0 will not break AEM agents A, B, C without N weeks notice."

---

## Loni + Jean-Michel meeting (week of May 11, 2026)

**Was week of May 4, rescheduled May 1 to week of May 11.**

**JM = Jean-Michel Pittet, VP Engineering AEM (Basel)** — confirmed April 16. Engineering-side VP peer to Loni (VP AEM & Commerce PM). Top AEM leadership pair — Pedro's highest-visibility moment to date.

**JM org (separate from Loni's):** Shantanu → Anil Chakravarthy → Sridhar Gantimahapatruni → Jean-Michel.
**Loni's org:** Shantanu → Anil Chakravarthy → Amit Ahuja → Loni.

**JM's team:** Alexander Saar (VP Eng AEM Remote Germany — Ian Boston, Jaclyn Eckersley, Carsten Ziegeler under him). Michael Marth (VP AEM Eng Basel — Gilles Knobloch, Felix, Mihai Corlan under him). Conrad Woltge (Sr Principal Architect direct report). Gitesh Malik. Mitch Nelson. Philipp Koch.

**Framing decided April 14:** Show report as-is. Be transparent — not compliant, to be handed off to DaaS team once formalized. Don't hide compliance gap. Right position for VP audience.

**Bertrand review of Portfolio Briefing:** Monday May 4 AM, before agent sync 4pm. Pending Bertrand confirmation. Pedro Slacked Bertrand the Briefing link + 71% retention finding May 1 night (in French, friendly tone).

**Senior Director moves status (as of May 1, unchanged May 3):**
- **SD-1** Haresh Slack drafted, not sent. Goal: confirm Vaishnav Gorur PMM + intro request. Plan: Mon May 4. Confirmation due Wed May 6.
- **SD-2** JM warm-up Claude project — in progress, not shipped. Due May 8. Loads: Felix report, Priority Consolidation view, HC rollup, Apoorva punch-list status, AO 2.0 lite context, 7-agent portfolio list. Seeded queries (10 pre-computed). Slack to JM with link Monday May 12 (CC Jaclyn).
- **SD-3** $500K P42 cost trace — not started. Due May 8.
- **KR4** Priority Consolidation view — April 24 draft. Due May 8.
- **Yanira QBR ownership ask** — task for Mon May 4.

**Vault gap (still open):** No canonical pre-meeting strategic brief next to KR3 note. Should draft week of May 5. Sections: strategic frame, what we present, what we don't, expected questions + pre-staged answers, exit definition.

---

## H2 Planning + HC Rollup (April 28)

Canvas at `Roadmaps/H2 2026 Planning - Initiatives and Roadmaps.md` (EH folder, cross-link from AAI). Full extraction + analysis at `Roadmaps/H2 2026 HC Rollup for AI agents.md` (move to AAI Phase 2).

**Three-table HC Rollup:**
1. **Direct Agentic Web Items (DX-1220)** — 9 items + Pedro-promoted (HOME-832 + AEMAGT-538 placed for narrative even though canonical parent is DX-1222). ~98+ HC.
2. **AI related but not in AEM Agents P42** — 3 items (WRKSP-1223 Fluffy Jaws V2, AEMEO-9508 Data Advisory Agent, AEMSRE-3429 P42 ORR). All under DX-1220 in JIRA but NOT in 6-agent reporting taxonomy. 14 HC.
3. **Agent-related Items in OTHER Initiatives** — DX-1222, DX-1223, DX-LLMO. 17 HC after AEMAGT-538 promotion.

**Slack Parent vs JIRA Parent dual columns** added per Pedro. Reveals LLMO-4141: Slack Parent = LLMO-4023 (current source doc) vs JIRA Parent = DX-1134 "Adobe LLM Optimizer / Project Elmo" which is **Closed**. Real-world data quality issue.

**Slide 40 draft mapping (gaps to flag Bertrand):**

| Pedro's reporting agent | H2 funded match | Status |
|---|---|---|
| Experience Production (EPA — Corey) | NOT directly named | ⚠ gap |
| Discovery (Apoorva) | NOT directly named | ⚠ gap |
| Governance (Philippe) | AEMAGT-856 — 11 HC | ✅ matched |
| Content Optimization (Greg) | possibly Content AI Support GRANITE-66359 (15 HC) | ⚠ confirm |
| Development / EDA (Brian) | AEMAGT-1282 — 16 HC | ✅ matched |
| Onboarding (Nick) | NOT directly named (Site Advisory ≠ Onboarding) | ⚠ gap |
| Modernization (Mike Tilburg / Gabriel Walt) | AEMAGT-538 — 33+ HC | ✅ matched |

Half of 6-agent taxonomy not visibly funded.

**Most consequential overlap:** **AEMEO-9508 Data Advisory Agent** (Shweta Dua, IceBox/Unassigned). 5-way overlap with Pedro: both P42, "Value Realization" explicit Phase 1 skill of Shweta's, persona includes "Product Managers" (Pedro's audience), framing positions vs "static dashboards" (Pedro's reports), MCP Layer overlap with Skills+MCP brief. IceBox = window to influence scope. Need Slack Shweta + Yanira this week.

---

## P42 Status — April 21 (Jaclyn + Yanira + Pedro)

**New dedicated leadership Slack channel (April 21):** Pedro + Yanira + Jaclyn + Conrad + Ian + Bertrand. Purpose = keep decisions tight, avoid broader forums.

**Jaclyn's asks:**
1. **Headcount rollup per agent** for slide 40. Foundation pattern: ~20% heads onto agents.
2. **Profitability framing** — revenue vs cost per agent. Not urgent, on radar. Yanira's PMM guess for EPA: Melissa Tao or Tina Nicu.
3. **$500K P42 pre-prod dev/workflows/cloud infrastructure cost** flagged on finance slide. Origin unclear ("the other Shweta," not Shweta Dua, asked for cost centers). Jaclyn suspicious: *"we have nobody using these agents, how could it be a half a million cost?"* JM has seen the number. Questions will come.
4. **Summit survey — agent-perspective analysis via Claude.** Jaclyn called the AEM survey version "mind blowing." Pedro committed to try.
5. **Claude project for Loni/JM exec self-query.** Jaclyn's tip — she gives other VPs Claude projects so they can self-query.

**Yanira Monday Agent Alignment agenda:** open forum for Summit readouts. Unstructured dump. Not the meeting to push new material.

**Compliance question Jaclyn raised (unresolved):** *"Just close them and then we're compliant or what does that mean? Does AEM need to be compliant? Does AO need to be compliant?"* Compliance ownership AEM-AO not clearly scoped. Future agenda.

---

## Yanira Slack consolidation (April 30)

Yanira Slack ("AEM Agents Usage at high level"), CC Jaclyn — feedback that current report's WoW data is "too transactional." Pedro confirmed co-innovation classification already in pipeline (just not surfaced). **Yanira ask + Bertrand KR5 Stable Monthly Metrics Deck + May meeting high-level summary all converged into the same artifact: AEM Agent Portfolio Monthly Briefing.** "Portfolio" naming locked April 30 (matches Jaclyn's frame from April 21 P42).

---

## BVR — Governance Agent (April 23)

**2 candidate BVR (Business Value Realization) metrics from Philippe review:**
1. **Number of brand checks performed per month**
2. **Number of permission audit requests performed via agent per month**

Ownership split:
- Validation with Philippe (PM Governance)
- Implementation with Lara (parallel reporting track)

Source: [AEM Agentic Success Definition Compliance Framework](https://wiki.corp.adobe.com/spaces/WEM/pages/3774169978/AEM+Agentic+Success+Definition+Compliance+Framework) (WEM Confluence space).

**Capability-level monthly usage** = first concrete application as headline value metric (distinct from TSR / VR / VRR). Headline material for Loni + JM.

---

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

## H-005 RESOLVED (May 3, 2026)

**First ever resolved hypothesis.** *"Owning Cross-Agent Measurement Standardization Creates Structural Cross-Org Influence for the Experience Hub PM."* Proposed March 26.

**Confirmed with 7 evidence lines (Apr 13 → May 1):**
1. AEM-AO liaison naming (Apr 14 — Bertrand named Pedro publicly).
2. Felix reports named at VP level (Apr 13 — Bertrand to Loni).
3. Loni prompt-to-roadmap question Pedro answers (Apr 13).
4. Varun voluntary consolidation of Discovery wiki into Pedro's platform (Apr 22).
5. Karthik / Rubin definition acceptance (Apr 16 — 7-agent list locked in tools).
6. Three-tier reporting architecture locked, Pedro owns middle tier (May 1).
7. Portfolio Monthly Briefing v0 shipped (Apr 30).

**Lesson:** original test design ("count agent teams that adopt a TSR/VRR standard") was Director's test. Actual confirmation came at Senior Director's test (*"are you in the room when the architecture is being decided?"*). Both true now. **Cross-org influence accrues to owner of data substrate before any literal "standard" ships — don't gate role claim on standard's maturity.**

---

## Stakeholder shortlist (AAI lane)

**AEM Agent PMs:** Apoorva Gupta (Discovery), Corey Dulimba (EPA), Philippe Kapfer (Governance), Greg Klebus (Content Optimization), Brian Chaikelson (EDA), Nick Whittenburg (Onboarding), Gabriel Walt / Mike Tilburg (Modernization).

**Agent PgMs:** Yanira Castaneda (AAI counterpart), Pritie Sharda, Robert Guthrie, Marius Duta, Amit Arora, Prashant, Georgeta Vladescu-Viezure, Juliana Campbell.

**AO / AEP:** Conrad Woltge (Sr Principal Architect), Trent Davies (eng, AO), Ken Russell (eng, AO), Sergey Generalov (PM, AO), Ian Boston (compliance), Manas Garg (AOv2 dev experience).

**Data / Reporting:** Felix Delval (data eng, EPA pipeline), Lara (taxonomy + Governance), Varun Kalra (Discovery validator, Apoorva's team), Karthik Penikalapati (Rubin tech lead), Angela Han (Rubin owner).

**Design (Adobe Design lane):** Silvia Mulet Ferre (Eugene's manager), Uma Subbu.

**Leadership:** Loni Stark (VP AEM & Commerce), Jean-Michel Pittet (VP Eng AEM), Jaclyn Eckersley (FinOps, AEM Eng VP-side), Bertrand de Coatpont (Sr Director PM, manager), Shankari Panchapakesan (Group PM, transitional).

**PMM:** Tina Nicu, Akin (PMM for AEM survey), Vaishnav Gorur (new PMM AEM agents — pending confirm Wed May 6), Haresh Kumar (chain to Vaishnav).

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

## May 6 — MCP MOC report shipped to Bertrand (acked)

Pedro shipped first MCP report MOC 2026-05-06. Slack to Bertrand: *"starting to work on MCP reporting with @fdelval. Aiming for a report what would look like this. Still refining on my side, but gives you the direction. Once I'm fine, will review with stakeholders/agent owners. NB — those are numbers Claude invented for the report template based on the splunk data. Not connected, not validated."*

**Bertrand acked.** Direction validated.

**What it confirms:**
- Pedro's report-design lane (Felix May 6 split: Pedro = design, Felix = Splunk extraction)
- "Tool Calls" terminology landed via MOC layout
- Iterative MOC-first posture (same pattern as Briefing v0 April 30)
- Stakeholder/agent-owner review GATED on Pedro refinement + Felix real-data connection

**Next:** Felix + Tanju Splunk extraction → replace Claude placeholders → review with Yanira / agent PMs / Conrad TBD.

---

## May 6 Namita 1-1 — Mapping owners + Langfuse path + master-list signal

Source: `Meeting Notes/Namita 1 1/20260506 - Namita Pedro 1 1 .md`. ~14 min EN. 5 of 5 walk-outs hit.

**Material signals:**

1. **AEM Grafana mapping = Jabin (creator) + Raul (editor), manual SQL.** Closes NYL data-freshness diagnosis. Pedro lane: refresh + automation.

2. **Internal-user exclusion = "technical accounts, copilot engine"** — Namita pasted in chat. Add to Felix Postgres filter.

3. **V2 reporting path = Langfuse + Claude skill bridge.** Ilya's team building skill to join V1 (Rubin / analytics DB) ↔ V2 (Langfuse). V2 data substrate ≠ V1. Access via Ilya or Alex (TBD — Saar or AEP eng).

4. **🚨 Customer master-list gap = org-wide.** Namita verbatim: *"Nobody seems to have that golden source of truth. Lists for AEP somewhere, lists for AEM. That consolidated list — something we need to nail sometime."* Same diagnosis as NYL thread. **Senior-Director-grade lane** if Pedro proposes consolidated source — cascades to NYL + Felix mapping + Rubin + Namita TBYB list.

5. **Rubin (Namita) = passive posture.** Data Science team builds. Open to AEM custom on request.

6. **Connection warm.** Slack DM open, *"happy to be in the loop"* on V2 reporting.

**Implications:**
- NYL Bertrand 9 AM Slack May 8 sharpens with Jabin+Raul + master-list framing.
- Ilya focused 1-1 needed (Langfuse access + V1↔V2 bridge + Rubin V2 future).
- Felix loop on Langfuse layer (missing piece for V2 internal traces).
- Master-list 1-pager = candidate Senior-Director-grade artifact for pre-May-11 Bertrand pitch.

---

## May 6 Yanira Slack thread — AEM Agents AOv2 Migration Workshop

Source: Slack thread launched by Yanira Castaneda 2026-05-06 18:03. Channel TBD (likely AEM agents broad). Pedro CC'd. Tag groups: @agent-owners-engineering, @agent-architects, @agent-owners-pgm, @agent-owners-product.

**Material content:**

1. **Workshop = Phase 2 (Evaluate) operationalized.** Reinforces 5-phase plan validity. Fills AC42 alt-forum void (Felix Delval exited AC42 May 5).

2. **Felix Meschberger (NEW high-signal voice):** *"agents should migrate to Skills+API and leave the build-out and operation of the agent harness to someone else — in AEM or AOv2 TBD."* 100% aligned with Pedro's Slide 2 ownership boundary. **Quote anchor candidate for Slide 2.** Asked Yanira for workshop content/success criteria. Distinct from Felix Delval. TBD title/org — confirm with Bertrand.

3. **Carsten Ziegeler shifted** from MCP-first (Bertrand 1-1 May 5) to skills+API alignment (Yanira thread May 6: *"Right, fully agree"*). MCP-vs-skills tension resolving toward skills-direct-API.

4. **A2A decommission direction reinforced.** Conrad (April 29) + Felix Meschberger (May 6) converging: A2A integration is "fragile path." Slide 3 fork moves from "open" to "directional."

5. **Felix Delval workshop framing:** register current agents AS-IS on AOv2, observe. **No evals in AOv2 ATM** → AEM eval-surface lever reinforced.

6. **Timing:** early PST proposed (Ankur Arora India + Jason Weaver DRM both asked). Early next week.

**Implications for May 11 deck:**
- Drop "Felix vs Carsten" tension narrative — consensus emerging.
- Replace with: skills+API consensus + workshop next week = visible momentum.
- Slide 2 quote anchor consideration: Felix Meschberger as alternative to Bertrand line.
- Slide 1 Phase 2: reframe from "EPA staging test (Felix-led)" → "AEM Agents AOv2 Migration Workshop (Yanira-led, all agent teams)" — broader, all-agent.

**Continuation (Ian Boston + Felix Delval, 2:02 PM onwards):**

- **Ian Boston conditional pro-MCP:** if AOv2 = one of many harnesses, MCP has OAuth-onboarding adoption advantage vs API bearer-token friction. Re-opens MCP-vs-skills tension on different axis: skills = build path consensus, MCP = exposure surface for external harnesses. Both can hold.
- **2-5% conversion data point (NEW)** — Ian: *"At the current levels of adoption we are seeing 2-5% conversions of most agents input funnels resulting in use."* Headline-grade for May 11 deck. Adoption-first reframe: *"unless AOv2 can change that, we should be looking at eliminating friction blocking inputs to the funnels."* Aligns with Loni's "we cannot be at the mercy of somebody else."
- **Yanira routes architect decision to Monday Architects call (Conrad-led).** Distinct venue from migration workshop. Ian misses (Basel SR workshop). Carsten + Conrad attending.
- **Felix Delval AOv1-unworkable brief:** staging hard to test, local deployment unmanageable, agent paraphrases user prompts, no local E2E for UI components. Plus product push to move forward. Plus *"AO2 also takes care of Orchestration, I don't think we have looked into AO2 with the prism of orchestrating the current functionality."* New evaluation lens: AO2-as-orchestration. Add to Phase 2 workshop scope.

**Refined deck implications:**
- 2-5% conversion = potential headline number (confirm w/ Ian + Yanira pre-deck)
- MCP friction-elimination angle holds alongside skills consensus
- AOv1 unworkability = Phase 4 Go-vote ammunition
- AO2-as-orchestration = new Phase 2 dimension

**Continuation — Carsten proposal (2:41 PM, NOT decision):**
- *"AOv1 has most likely not the future, no customer showed interest in A2A, nearly no relevant AI product supports A2A out of the box. Continuing with A2A does not make sense. It complicates our setup and does provide zero value. Focusing on MCP/API to provide the required basics and then adding - if required - skills on top seems to be the way forward."*
- **Proposes A2A retire + AOv1 sunset + MCP/API base + Skills-on-top layered model.** Decision pending — gated on Conrad directive + Phase 4 collegial.
- AOv2 + Claude + other AI products support MCP/API per Carsten → ecosystem-fit argument.
- **Direction emerging across architects** (Felix Meschberger + Carsten + Ian + Felix Delval positions converging in workshop thread). NOT alignment achieved. Capture as "direction emerging, pending decision venues."

---

## May 6 Felix 1-1 (~25-min FR sync)

Source: `Meeting Notes/Felix Pedro 1 1/20260506 - Felix Pedro 1 1.md`. Felix + Pedro.

**Material signals:**

1. **MCP scope CLARIFIED.** Customer use of MCP on **non-Adobe surfaces (ChatGPT / Claude)** = reaction to AEM agents. NOT internal AEM agents calling MCP. Felix forced clarification: *"MCP je suis allergique à ce mot là."*

2. **Pedro ↔ Felix MCP work split.** Pedro = report design (manual first on EDS, validate, automate later). Felix = Splunk extraction layer via Splunk MCP server → side Postgres DB.

3. **Apples-vs-oranges rule for Loni/JM (terminology locked Pedro 2026-05-06):**
   - Use **"Tool Calls"** — NOT "interaction" or "invocation" — for MCP. Pedro chose this from Felix's hit/tool-call options.
   - Cannot compare agent interactions vs MCP Tool Calls on same chart
   - Cannot do per-agent MCP breakdown — tools tagged, not agents
   - Felix: *"Pour moi le seul truc qui doit être clair quand tu le montres à Loni c'est que tu compares des oranges et des pommes."*

4. **Splunk 90-day window** = constraint. Felix dumps to side DB to maintain history beyond ~2026-02-06.

5. **Multi-turn flow breakage = NEW EPA product gap** 🔴. Surfaced via Amine (Felix eng) auto-categorizing weekly CSVs with Claude. Many at Summit hit it.

6. **Amine pattern = reusable per-agent value indicator pipeline.** CSV → Claude auto-categorization → ticket creation. Extends Lara/Governance pattern. Candidate for Tier-2 reuse (Brian / Greg / Apoorva).

7. **DB redesign:** SQLite → **Postgres + LLM-as-Judge layer**. Engineers connect to central DB this week.

8. **VPC / Ethos IP-range blocker** — Felix's range marked in-use months. Ethos cleanup ticket created. Pedro to share Ethos contacts if any.

9. **AOv2 — Felix at 8/10–9/10 going.** *"Ce n'est pas le problème, c'est la gravité."* AEM has no own-orchestration eng team, management won't fund one → AOv2 evident. Question = when (2 weeks vs 2 years), not if.

10. **Reporting strategy:** Felix recommended manual report first → automate later. Reverse-engineer from desired report.

**Risk flags:**
- R1 🔴 Apples-vs-oranges. Deck must enforce hit-not-interaction rule.
- R2 🟡 Splunk 90-day window time-sensitive — backfill needs to start now.
- R3 🟡 Per-agent MCP breakdown impossibility. Bertrand asked for client + agent split. Manage expectation. Confirm w/ Namita tonight.
- R4 🟢 Felix takes MCP extraction layer.
- R5 🟡 Multi-turn breakage = real EPA pain.
- R6 🟢 AOv2 8/10–9/10 reinforces 5-phase frame.

---

## May 5 Bertrand 1-1 (~20-min FR sync)

Source: `Meeting Notes/Bertrand 1 1/20260505 - Bertrand Pedro 1 1_otter_ai_transcript.txt`. Two named speakers (Pedro + Bertrand), rest Unknown — attribution by content.

**Material signals:**

1. **AOv2 5-phase plan VALIDATED 🟢** (Bertrand 8:27 verbatim): *"AoV2 a l'air prometteur. Plutôt pour faire une évaluation. On demande aux équipes de faire des évaluations de migration et de workload. On collecte. Puis après on décide collégialement."* Matches Pedro's 5-phase exactly. Slide 1 + Slide 2 boundary content validated.

2. **Slide 2 (Ownership) — Bertrand additions to AOv2-owns column:** Telemetry + UI. Slide framing preference: *"plus une guidance que d'une finition pure et dur."* PPTX + KR3 deck note updated.

3. **MCP workstream → Bertrand owner.** *"Je vais m'occuper des MCP."* Closed from Pedro's plate. Pedro tracks but doesn't own.

4. **MCP-in-reports — new ask cluster.** OKR review yesterday: JM + Loni "particulièrement en forme." Contrast surfaced publicly: agents low usage vs MCP high usage. 170K April calls flagged. Bertrand wants client-level breakdown — internal vs external, customer names. Same depth as agent-level reports. **Tomorrow Namita 1-1 = direct lever** (she owns AI Assistant Dashboards / AI Integration / AI quality + AOv2 AIA extensions). Briefing v0 sections 5-6 candidate.

5. **Customer-level use-case reverse-documentation — new analytics direction.** Bertrand: *"Microsoft utilise des outils A et B → use case probablement X. Est-ce qu'on peut rétro-documenter?"* Push beyond macro consolidation. Identify top-3 engaged customers ("3 clients qui ont vraiment mordu à l'hameçon"). Method TBD with Felix.

6. **Mithril / Coworker — NEW SURFACE launching ~late May (T-25 days).** Joshua Hailpern's team. "Mode rail" = AI Assistant V2 (observes screen, suggests). Pedro saw via night Slack May 4. **AEM Sites NOT in Mithril** — repeat exclusion (also Modernization, Experience Workspace). Bertrand: *"Ça va être un point important pour la migration AOv2 si on y va."* Bertrand surprised no XD / Guliz in loop — actioned: chase with Guliz. Marcus Räck (Experience Workspace creator) declined Pedro's unified-chat ask. 4 chats now (Experience Workspace, Modernization, Slick, Rosetta). Pedro got Cédric Huesler annoyed via Slack push.

7. **MCP vs skills-direct-API tension.** AOv2 platform agents rewritten WITHOUT MCP. Felix pro-skills-direct-API. Carsten pro-MCP. Conrad "modérément…" Pedro: *"Si entre Carsten, Félix et Ian ils pouvaient au moins être d'accord."* Bertrand handles. Critical for May 11 deck.

8. **Felix EXITED Architecture Committee 42** 🔴 — *"P42 ça se passe je vais même plus parce qu'on n'avance pas."* Cross-agent leadership void Pedro flagged today now operationalized as forum disengagement.

9. **June Bucharest workshop (Alex Saar host)** — Bertrand 1h opener, prep pending, agenda on wiki. Adjacent venue for Pedro coordination role since AC42 stuck.

10. **Loni+JM May 11 agenda** — Bertrand still working out structure ("il faut refaire l'ancien weekly"). Pedro can propose section ordering.

11. **EH-side drop-ins:** Bertrand asked Sorin + Eugene to do **Mithril review**. **Sylvia Mulet Ferre launching auto-fix-prompt initiative for EH** — Bertrand skeptical: *"je sais pas trop où elles vont venir avec ça."* Customer migration: 1-year migration pattern, decouple "platform update" vs "platform move." Nico's content-repo migration waking customers up.

**Risk flags:**
- R1 🔴 Felix exited AC42 — cross-agent leadership void worse than Pedro knew this morning.
- R2 🔴 Mithril launches T-25 days WITHOUT AEM Sites. Repeat AEM-exclusion pattern.
- R3 🟡 MCP vs skills-direct-API: Felix + Carsten + Ian + Conrad don't agree. AEM platform agents written WITHOUT MCP contradicts AEM's MCP-first investment.
- R4 🟡 Bertrand customer-level reverse-doc ask = scope-expanding. Felix already stretched.
- R5 🟢 Pedro gained ground: 5-phase plan validated, MCP off plate, boundary slide validated with 2 additions.

---

## May 5 Felix 1-1 (33-min FR sync)

Source: `Agent Owner Alignement/20260505 - Felix Pedro 1 1.md`. All "Unknown Speaker" — attribution by content. Felix in self-described "cahier de doléances" mode.

**Material signals:**

1. **BVR critique — must add banner before May 11 deck.** *"BVR à 100% veut rien dire, BVR à 0% veut dire quelque chose."* Treat like temperature/pH (relative, not %), NOT comparable across agents OR across BVR categories. Calibration baseline: week-before-Summit (near-100% internal `am-sitestrial` tests) vs Summit week (real users). Self-aware: *"si ça monte je demande promo, si ça monte pas je montre autre métrique."* Felix adds banner to Value Realization section. Per-agent custom indicator pattern (Lara/Governance brand-checks/month) extends to EPA + Discovery.

2. **AOv2 — pro-V2 via staging test, anti-V2 via blind trust.** *"Tous les agents owners il n'y a personne qui se fie de l'équipe d'AEP. Gilles se fit pas, moi je me fie pas, Corey se fie pas."* Conrad/Trent/Carsten "hors sol." Conrad "enthousiaste" to V2. Ken Russell team NOT prod-ready, IS staging-ready. Felix recommendation: launch staging migration test AS OF TODAY on real AEM agent. *"Tant qu'on n'a pas fait ça en staging, on n'a pas fait grand chose."* Risk of moving = maigre. Risk of NOT moving = bigger.

3. **Gradial competitor on EPA — NEW signal.** *"Beaucoup de gens vont nous voir: vous implémentez pas ça rapidement, on passe sur Gradial."* First explicit competitor name in AAI lane. Speed argument for V2. **Confirm with Corey + Yanira before May 11 deck commits to it.**

4. **Cross-agent technical leadership void — Felix's main grievance.** Conrad/Trent/Carsten "hors sol." Different repos / archis / observability (Splunk vs Longfuse). "Agents owners vont pas dans meetings d'autres agents." *"AOA est mort parce que l'orchestration est nul à chier."* Felix ask: non-mandatory best-practice guidelines by architects seeing multiple projects. Repeats 22:10: *"il manque du leadership technique sur les agents."* Felix invites Pedro to co-sponsor with Bertrand. **Senior Director-grade move if Pedro picks up. Frame as PM coordination layer, NOT architecture.**

5. **Infrastructure moves this week.** OneAdobe repo migration — Felix grants Pedro access tonight US-time. Domain move next week. VPC for DB next (bureaucratic, slow). PR merging this morning — AEM-agents-report extraction tool, separate weekly DB, env-var configurable.

6. **Loni/JM endorsement.** Felix: *"Je crois qu'il faut qu'on fasse un rapport pour Loni Jean-Michel pour la semaine prochaine avec plein de chiffres."* Offered to recheck numbers.

7. **Namita validation.** Felix on Namita: *"elle parle l'humain comparé à certaines personnes."* Validates Wed May 6 1-1 bet.

**Risk flags:**
- R1 BVR % in Briefing v0 = interpretability risk. Banner before May 11 deck.
- R2 Pedro-as-AO-liaison exposure. Don't argue AEP framing in front of agent owners — route through Bertrand.
- R3 Gradial unverified — confirm Corey/Yanira pre-deck.
- R4 Cross-agent leadership void = real opportunity. Don't overstep Conrad/Bertrand turf.

---

## Open vault gaps (still tracked)

- Stakeholder Map Vaishnav entry (held until Wed May 6 confirmation)
- Pre-meeting strategic brief for May 11 Loni + JM (draft week of May 5)
- Briefing v0 sections 5-6 (pending Indicator #8 on May 17)

---

## May 12 — Mithril Silvia ↔ Tim Lynn exchange + Pedro outbound DM

**Event.** Silvia Mulet Ferre (Eugene's manager, Adobe Design / Guliz tree) opened a public thread with Tim Lynn (Mithril project owner) on Mithril clarifications. Three confirmations + one open ask Pedro can answer.

**Confirmations from Tim Lynn:**
- **Mithril = AO2 only.** Not AO1. *"we're aiming to have things wired up e2e by end of may. parts of the api have been committed to our new UI repo and AO, but the shell side is still WIP."*
- **Context-reading not default.** Use-case Silvia described (assistant reads open page + full context without manual user input) requires per-page/app tooling that registers itself with Mithril in the DOM-tools pattern. Reference demos = "edit schema" + "pueblo".
- **Skills authorship unclear.** Tim didn't know whether end-users or internal Adobe teams create skills — likely AO team question.

**Silvia's open ask (Pedro = answer):** *"with who can we connect (PM, eng) to make sure context-reading is part of AO2 & Mithril?"* for AEM.

**Pedro outbound DM 2026-05-12 (EN, Slack).** Identified self as AEM-AO PM liaison (Bertrand-named April 14). Confirmed alignment between Silvia's context-reading ask and EH foundational primitive. Proposed division: Silvia drives Adobe Design side (Tim + Guliz), Pedro drives AEM PM side (Sergey Generalov + Conrad Woltge). Joint ask = **context-reading as a Mithril primitive, not per-app re-implementation.** Asked for 15 min this week. Looping Eugene.

**Why this matters:**
- Bertrand May 5 action — *"chase Guliz on XD/Adobe-Design loop visibility"* — materializing. Silvia (Guliz tree) operating directly with Mithril. Loop visibility is happening; Pedro inserts as the AEM-PM pole.
- Pedro's AEM-AO liaison mandate now operational at PM-to-PM-counterpart level (Adobe Design Sr Manager → AEM PM) on a high-leverage primitive, not just at AO PM↔PM (Sergey).
- Context-reading = same primitive Pedro pushes on EH Priority 1 (Skills+MCP surface) with Eugene. Adobe Design + Pedro aligned ask = stronger together than either alone.
- End-of-May Mithril e2e wiring = T-19 days. Window to influence Mithril primitive list is now, not after launch.

**Posture (hedge — confirmed Pedro 2026-05-13):** AEM has **not yet committed to AOv2.** ~90% probable, **progressive**, internal resistance still active. Conrad directive imminent but not landed. Pedro's ask to Silvia is **purely architectural** (primitive vs per-app), **decoupled from AEM AOv2 commit timeline.** Architecture ask remains valid for any Mithril consumer regardless of when AEM moves. Knowledge entry promoted: leadership/ "Decouple the Architecture Ask from the Platform-Commit Timeline" 2026-05-13.

**Bertrand FYI Slack v2 (FR, drafted 2026-05-13, NOT YET SENT).** Adds hedge paragraph: *"je n'ai rien committé sur le timeline AEM. L'ask est purement architectural (primitive vs re-impl par-app), décorrélé de notre évaluation AOv2 en cours (workshop Yanira semaine prochaine, directive Conrad imminente)."* Send-or-wait gated on user confirm.

**Bertrand FYI Slack drafted (FR, not yet sent).** Quick informational note referencing his May 5 action, confirmations from Tim Lynn, Pedro's outbound move, division of labor. No ask. To send when user confirms.

**Open:**
- Awaiting Silvia reply on 15-min slot.
- Tim Lynn = new stakeholder (Mithril project owner, doc author). Org chain TBD — confirm.
- Skills authorship question (end-user vs internal-Adobe) still unresolved — route to Sergey when contact lands.

---

## May 14 — Corey 1-1 (call HELD; was scheduled May 19)

**Reconcile.** Earlier memory said "call lands Tue 2026-05-19." It actually landed **Thu 2026-05-14** (Corey rescheduled earlier; on Pedro's day off, ~23 min, EN). Source: `Meeting Notes/Corey 1 1/20260514 - Corey Pedro 1 1 .md`.

**What landed:**
1. **Decision — new from-scratch simple EPA report, not a retrofit of the multi-persona report.** Corey: define the 4 (up to 10) key metrics he wants, build clean, drop the old report if the simple one suffices. Pedro confirmed persona-scoped (Corey = key persona), Claude Code generates it (low effort). **Corey committed to send metrics in plain English same day (May 14).**
2. **Cosmetic principle:** drop tables that duplicate a chart's visual; hard-collapse.
3. **VR-per-agent loop set:** single DB (Copilot + external) across agents; Felix most advanced on Sites VR; other agents' use cases too spread for one number → split per agent, maybe umbrella later. **Corey workflow:** his team collects EPA VR defs → wiki → sync Pedro → integrate. Pedro accepts one plain-English high-level def to start.
4. **MCP double-count flag:** Corey said EPA uses the content MCP → Gilles' ~1.2M Splunk call number (shown Loni+JM) likely double-counts. Pedro continuing DAS/Databricks tool-call filtering (off noisy Splunk pings/responses). Not urgent for Corey but EPA scaling MCP focus going forward; usage low today; tool calls skew to lists not actions (governance).

**Prep targets NOT covered (still owed):** Gradial confirm/deny, multi-turn flow gap trajectory, EPA H2 roadmap timeline read, EPA lab as customer-getting-started asset. Carry to next Corey touchpoint (VR-wiki sync).

**Why it matters.**
- **First-testeur pattern** (post April-2 Philippe-as-mirror) now produced a concrete artifact, not just feedback — Corey moved from reviewer to **co-author** of a scoped EPA report. Operational, not theoretical.
- Aligns with H-005 (substrate-before-standard): Corey is the cross-agent customer of the data substrate Pedro owns.
- Two-step substrate move holds — ship simple report to Corey first, iterate, then harden for Philippe + Yanira + Conrad. Compounds with monthly Portfolio Briefing cadence.

**Doc.** Outcome section in AAI Status & Todo: **`## Corey call notes — May 14`** (replaced the prep section). Forward tasks tracked in the "From May 12 — Corey report feedback + call HELD May 14" To Do block.

---

## May 19 — Corey proof-of-utility + portfolio growth-vs-retention split + Agent Owners light version + Tanju External Agent Report

Source: Pedro chat update 2026-05-19 + External Agent Report screenshot (Returning Orgs/Users per Agent, trailing-4-week, latest week May 10).

**1. 🟢🚨 Proof of utility — Corey reused parts of Pedro's report to serve a Cédric request.** Not theoretical value: an EPA PM pulled from Pedro's substrate to answer a Cédric Huesler ask. Hard external-consumption evidence. Promotion-grade — direct H-005 (substrate-before-standard) confirmation, and the strategic counterweight to the bad growth numbers. Pair these two in any exec framing; never present the decline naked (FB-030, `feedback_first_reply_ownership_sentence`).

**2. New workstream — light report version for Agent Owners.** Pedro building a lighter External Agent Report variant scoped for the Agent Owners audience. Companion to the Corey "from-scratch simple EPA report" pattern (May 14) — same move: audience-scoped cut, not a retrofit of the multi-persona report.

**3. Tanju — augment External Agent Report (ex-MCP), started on Governance Agent.** Pedro + Tanju expanding the External Agent Report (locked name; "Agent Integration" was informal — do NOT relock). Governance Agent first. Ties Splunk MCP loop Pedro↔Felix↔Tanju + Lara Langfuse Governance pipeline.

**4. Portfolio growth numbers DOWN.** Latest portfolio report: **-10% external orgs, -30% external users** (growth/total). Concretizes the May 12 Bertrand "numbers descending" risk. Caveat holds: internal/external categorization (Raul list) still weighs on the number — treat as not-yet-hard signal, not raw truth.

**5. Retention (External Agent Report — Returning, trailing-4-week, latest week) — opposite story where it counts.** Returning **orgs** (count / % of agent's external orgs): Discovery 107 / 69%, Experience Production 94 / 68%, Experience Development 30 / 46%, Governance 19 / 47%, Content Optimization 7 / 30%. Returning **users**: Discovery 39 / 15%, Experience Production 38 / 21%, Experience Development 15 / 21%, Governance 10 / 22%, Content Optimization 2 / 8%. Trend curves: **Discovery + Experience Production rising strongly**; Development / Governance / Content Optimization flat-low. So the decline is **concentrated on the 3 low agents, not global** — the two flagships retain and grow. (Corrects the earlier verbal "flat for Discovery" — Discovery retains hardest.)

**6. 🆕 Sharp PM insight — org-level retention high, user-level retention low.** Orgs return (30–69%) but few individual users within them are repeat (8–22%). Org stickiness, shallow user-level engagement. The next question is user-level engagement, not acquisition. Connects to knowledge: repeating-users = primary value signal; measure at unit of user intent.

**Why it matters.** Two metrics must stay distinct in exec framing: growth (down, data-caveated) vs retention (up on the two flagships). The honest non-defensive story = "decline is concentrated + categorization-noisy; retention strong where it counts; substrate proven consumed (Corey/Cédric); here's the plan (Agent-Owners light version, Tanju Governance augmentation)." This is the May 11 Loni+JM deck spine and the Bertrand 1-1 point.

**Doc.** AAI Status & Todo: new tasks (Agent-Owners light version, Tanju External Agent Report Governance) + Current Status note on growth-vs-retention split. Bertrand 1-1: point 5.

---

## May 19 — Engineering bridge: Mithril/Fruitbar ↔ Prompt Library Platform (Hailpern / Somya / Zeus, Sunil tree)

Connective insight surfaced 2026-05-19 cross-referencing the two Hailpern announcements (Mithril Hybrid 2.0 + Fruitbar) against the EH-side "Cross-VP — Prompt Library Platform" memory.

- **Joshua Hailpern** is EM of the **Prompt Library Platform** (Cole Connelly's PM area, O2 KR "EH consumes prompt library not wiki") AND leads the **AIA UI / Mithril / Fruitbar** stack. Same person, both sides.
- **Somya Biswari** + **Zeus Courtois** appear on both: lead engineers on Prompt Library Platform (April 28 memory) and named in the Mithril announcement (Somya = Quarry Component integration lead; Zeus = "You Shall Not Pass" AI-generated-code-quality automation).
- Implication: **Prompt Library Platform and Mithril/Fruitbar/AIA-UI are the same engineering galaxy** — Hailpern + Somya + Zeus — and it sits under **Sunil Menon's VP tree (Experience Cloud Portfolio), NOT Loni/AEM's**. (Cole → Stephen Gould → Tim Lott → Daniel Sheinberg → Sunil Menon → Amit Ahuja.)
- Why it matters: when Pedro engages Mithril/Fruitbar (validation with Josh/Adam) or the prompt-library KR, it's the same org pole. Cross-org influence runs through Stephen Gould (strategic, also Pedro's DX/Unified Shell contact) / Cole (tactical), at VP layer Loni↔Sunil. Don't treat Mithril and Prompt Library as separate org problems — one tree, one set of people.
- See vault note `AAI - Project Folder/AO 2.0/Mithril & Fruitbar - Crash Course (non-frontend).md` + EH memory "Cross-VP — Prompt Library Platform".

---

## May 20 — close-out: Loni+JM reconcile, Aditi/Pierre Tager, Bertrand 1-1 prepped

**1. 🔄 Loni+JM deck reconcile — NOT yet held (pending), NOT a missed outcome.** Earlier framing across memory + AAI Status ("outcome NOT captured, single biggest open") was WRONG — Pedro confirmed 2026-05-20 the deck has not happened. KR3 is an upcoming *delivery*, not a debrief gap. The staleness-auditor's "single highest-leverage refresh" (debrief Loni+JM) was built on the wrong premise. Corrected in AAI Status (staleness flag + Focus item A). Next: confirm date/format with Bertrand (1-1 point 4), then finalize the deck. **Lesson for the system: a "missing outcome" flag can be a not-yet-happened event mislabeled — verify happened-vs-pending before calling something the biggest open.**

**2. Aditi (PM, reports to Pierre Tager in Bertrand's org) — meeting invite via Shankari's reference.** She wants AI-Assistant current state + what's next + what the liaison R&R looks like. **Pedro's read (2026-05-20): NOT a risk.** Aditi is new, doesn't know the Agents space; Pedro will help her onboard. The Shankari referral = recognition that Pedro is the AI-Assistant source/authority — a visibility signal, not displacement. Pedro IS the liaison (Bertrand-named April 14, not revoked); you don't send someone to learn a role from the person being replaced. Real (lighter) sub-point: the liaison R&R is *recognized but not written* — opportunity to formalize it (promotion-useful), not defend it. **Pierre Tager = new, scope unknown — confirm.** Captured in Bertrand 1-1 file Role-Clarification point 3 (FYI-light) + Stakeholder Map.

**3. Bertrand 1-1 (2026-05-20) — prepped, outcome = debrief-ask.** Agenda written into `Experience Hub - Questions for Next 1-1 with Bertrand.md` (FR, 5 points): (1) accept Workshop Foundation facilitator, (2) ✅ Mithril/Fruitbar UI correction ALREADY done with Bertrand before the 1-1, (3) escalate + offer to seed Ian North Star 1-pager, (4) confirm Loni+JM date, (5) growth-vs-retention non-defensive framing. **Outcome not yet captured — debrief next session: what landed on workshop role, Ian 1-pager, Loni+JM date, and the Aditi/liaison-R&R question.**

**Doc.** AAI Status: staleness flag + Focus item A reconciled; Aditi task added (From May 19 block). Stakeholder Map: Aditi + Pierre Tager to add.

---

## May 19 — Ian Boston publishes Agentic NorthStar (🟢 gating artifact RESOLVED)

Source: [Agentic NorthStar](https://wiki.corp.adobe.com/spaces/~boston/blog/2026/05/19/3894002388/Agentic+NorthStar) — Ian Boston, 2026-05-19. **Supersedes every "Ian 1-pager NOT started" flag** (consolidation checkpoint, May 12 P42 §, May 18 Agent Owners §5, May 20 close-out). It exists now.

**Format = deliberate blog, not a wiki page.** Ian: *"a view today that may be obsolete within a week... if this post proves to have a future, then it will evolve into a page."* Ends on a question — ***"Should this be our Agentic NorthStar?"*** → discussion artifact, not a locked spec. Matches Pedro's discussion-not-decision frame; safe to cite with Conrad in room as "the architect's North Star, in review." Anchored to the 2018 Skyline NorthStar.

**NorthStar statement (verbatim):** *"Focus on Skills backed by high value, unique APIs and MCPs driven by the data and content that our customers have entrusted to us, supporting our customers individual and institutional memory to ensure leaving Adobe will be a heartbreaking experience."* Three pillars: Skills (reasoning now commodity via Claude / Codex / Pi-OpenClaw SDKs) + unique APIs/MCPs (where value lives) + **memory as the moat** (institutional memory = lock-in).

**Architecture — distributed > single harness.** Ian rejects "one harness to rule all" (edge cases to the harness-owner = the essence to the skill-owner; a single instance can't specialise UI + context; high skill-cardinality kills reasoning — *"50% delivering 5% is not success"*). Lands on a **distributed harness**: each team owns its own UI + Skills + Session, specialised to its context — *"Each team that owns the context needs to be able to own the UI and specialise it. The skills for the context needs to be their skills."* **Memory is the exception: a shared service across harnesses**, explored by Adobe Research as **memory-as-MCP** (referenceable through a skill). Maps 1:1 to AEM's Slide 2 ownership boundary AND to Bertrand's May 18 "Adobe Harness" (memory + layered context provided by the foundational layer so AEM doesn't build it).

**Hard numbers (sourced to the architect):** AOv1 for AEM agents = **50% "ok", only 5% "exceptional"; explicit feedback 50% unworkable, 5% worse.** P42 adoption rapid, results disappointing. Requirements-first evidence — the bar AOv2 must clear. Pairs with Ian's 2-5% conversion (May 6).

**Two diagrams** on the blog (single vs decentralised) — recreated as Mermaid + slide-impact mapping in the KR3 deck note §"Ian Boston Agentic NorthStar (2026-05-19) — deck integration". Decentralised: UI-A→Harness-A and UI-B→Harness-B each with own Skills + Session, both wired to one central **Memory MCP**. Source PNGs = Confluence attachments 3894001962 (single) + 3894001966 (distributed).

**Strategic read.**
- Gating item flipped 🔴→🟢. Forcing-function escalation no longer needed.
- **Public-naming → delivery:** Pedro named Ian owner on the May 18 call he hosted; Ian shipped May 19. Bank the win — naming an owner publicly in a forum Pedro chairs produced the artifact.
- Pedro's lane = distributor / operationaliser (corrected role, NOT architect). Doc landing triggers: respond as first substantive voice (architecture-altitude visibility, reinforces resolved [[H-005]] substrate-before-standard), carry into agent teams as the requirements anchor, compile requirements back to AOv2.
- Deck fuel for Loni+JM: Slide 2 add Memory-as-shared-MCP; distributed-harness validation of the AEM/AOv2 boundary; 50/5 baseline (requirements-first, never naked); memory-as-moat spine line tying to Loni *"not at the mercy of somebody else."*
- Credit Ian as author on any slide. Don't weaponise the distributed model against Conrad/AO in room — frame as "architecture converging on distributed + shared-memory; AEM contributing requirements."

---

## May 22 — Ian NorthStar thread: outcomes (routing, memory→Saar, UX = PM-lead, consistency mandate)

Pedro engaged Ian's NorthStar as first substantive responder (Slack + wiki footer comment, May 19-22). High-value exchange — Ian answered every question and escalated. Source: wiki comments page 3894002388 + Slack. Also referenced: Ian's [Claude Token costs](https://wiki.corp.adobe.com/spaces/~boston/blog/2026/05/20/3894008282/Claude+Token+costs) blog.

**1. Routing answered — "the UI deciding which harness to call."** Ian (wiki reply, hedged "I think we are going to see"): harnesses loaded with the skills they need + the UI decides which harness to call, via **explicit or prompted selection, NOT automatic intent detection**. AOv1's orchestrated-intent-above-agents made reasoning weaker. AOv2 + FluffyJaws show explicit/prompted > auto. Also: a skill can be shared across harnesses, and harness-to-harness A2A calls are fine (FJ calls DAA over A2A) — distinct from AOv1 directed agent-to-agent (dead) and customer-facing A2A (retiring). **Implication: selection is a surface/product problem before an orchestration one → Pedro's lane.** ("UI decides" = Ian's forward prediction, not a locked spec.)

**2. UX/selection — "must be PM lead" (Ian, on record).** Pedro claimed the practitioner-UX read; Ian: *"UX, yes, absolutely, must be PM lead."* Architect-endorsed lane.

**3. 🆕 Consistency mandate.** Ian: *"Consistency will be vital so an Adobe user feels like it is the same surface regardless of the implementation details or UI engineering ownership."* In tension with distributed-UI-ownership → reconciling it = Pedro's job: own the **cross-surface consistency layer** across distributed agent surfaces. Architect-backed answer to the 4-chats fragmentation (Experience Workspace / Modernization / Slick / Mithril; Marcus refused unification). Backs Pedro's convergence push. Senior-Director-grade lane.

**4. Memory ownership → escalated to @asaar (VP).** Ian: who owns memory = tbd; partly user-bound, partly team/org, both with residency requirements; users span CXO + DMe → leadership question. Proposed identity-like model (central personal+org via IMS/AUP + common API/schema; product-specific memory with solution teams). **Ian escalated to Alexander Saar (VP Eng) for cross-Adobe alignment at his level.** → AEM needs requirements ready for that conversation. Doc drafted: vault `AO 2.0/What AEM Needs from a Central Memory Service.md`. Route via Bertrand (don't insert into the VP alignment directly). NOTE: Pedro asked Ian to write the official requirements ("would you put together…"); Ian routed it up to Saar. Pedro's doc = AEM's private *input*, not the official artifact. **Standing weekly checkpoint tracker** (5 checkpoints: doc exec-ready → hand to Bertrand → on Saar agenda → conversation held → outcomes fed back; next check 2026-06-01, then weekly) lives in AAI Status Focus — surface + update it weekly at session start.

**5. Moat — Ian loved + sharpened it.** Pedro's "open, portable, but heartbreaking to leave" → Ian: *"a great way of putting it"*, tied it to an early-March conversation with **@lkao + @gmiller**, said Adobe Research is working in the space. Refinement: **portable WITH EFFORT** + value-on-top = the moat (his Gmail-takeout analogy). Confirms moat = the data, not the mechanism; interface stays open (memory drawn as MCP). **Visibility: Pedro's phrasing now attached to a senior architecture conversation.** Confirm who @lkao + @gmiller are.

**6. Token economics** (Ian's Claude Token costs post + a ClaudeCode deep-dive screenshot). MCP server manifest = **~2K-15K tokens/turn even when unused** (5 MCPs ≈ 50-75K history budget lost permanently); Skill ~200-500; hook 0. Context window ~200K, conversation history = largest segment (40-60%), compaction trades quality for budget. → Argument for **skills-over-MCP** (reinforces Trent/Carsten/Felix-Meschberger consensus; mild tension with AEM's MCP investment + MCP-first posture). Sharpened memory-requirements doc req 6: a Memory MCP must keep its manifest lean + return ranked context only. Latent sharp question (unused): Ian's token-costs post argues against MCPs while his NorthStar draws memory AS an MCP — is memory the high-value exception, or skill/hook-backed?

**7. 🟢 Influence pattern (bank for Senior Director narrative).** Pedro's sharp questions at the right altitude triggered owner action twice: public-naming → Ian shipped the NorthStar (May 18→19); memory question → Ian escalated to Saar VP (May 22). Operating at architecture-conversation altitude, named-in-the-room, triggering motion above him. Reinforces resolved [[H-005]] (influence/substrate before standard). Promotion-frame = "operating at architecture-conversation altitude," NOT "I am the architect" (Ian = architect; Pedro = PM distributor + UX/consistency lead + requirements compiler).

**Process note:** Claude misread "would you put together…" as a self-delegation and pre-drafted the requirements doc; Pedro corrected (it was addressed to Ian). Claude also paraphrased the token-costs post before reading it. See [[feedback_confirm_ask_before_producing]].

---

## May 26-27 — Bucharest workshop framing + "everything is a skill" reframe

Pedro animates ~1h at the June Bucharest workshop (Saar-hosted; Bertrand opens 1h). Sync with Stefan (5/22) revealed the real constraint: **audience = 56 people, global, mixed (devs, mostly managers + senior managers, sales, PMs)** → NOT a brainstorm. Format = **keynote / teach-and-align**; the actual skills-vs-agents decision stays a small-group call. Very likely the **Workshop Foundation skill-proliferation facilitator role** Bertrand asked Pedro to take (May 12, re-aired May 18). Prep note: vault `AAI - Project Folder/Bucharest June Workshop — Skill Proliferation + Modernization.md`.

**Framework (Pedro owns the structure):** two gates — Gate 1 *Should it exist?* (competitive / persona / seamlessness = the modernization filter = Bertrand's "what's worth investing in" governance); Gate 2 *Which harness?* (see reframe). Plus a persona × context 2×2. Merge insight: proliferation (supply) + modernization (criteria) = one question — *where does agentic investment go, and how do we decide?*

**🆕 Conceptual reframe (Pedro caught it):** the org's "skills under existing agents vs new agents" framing is **partly outdated** under Ian's NorthStar. Reasoning is commodity → **everything is a skill**; the "agent" dissolves as a build unit into skills-in-a-harness (Ian: DAA = "a collection of Skills in a harness"). So Gate 2 isn't "skill vs agent" but **"everything's a skill — which harness?"** (existing by default; new harness only on a new persona+context boundary). Hold for the mixed room: agent dies as a *build* unit, survives as a *GTM/customer* unit (sales still sells "agents"). Knowledge captured: `ai-product/` "Everything Is a Skill". This upgrades Pedro's session from running the stale binary → teaching why the question changed = operationalizing Ian's NorthStar (his distributor role).

**Open / confirm:** outcome (decision rule + shortlist vs the binary); Stefan / Day-2 fit; pre-align the two gates with Bertrand before the room.

**Process note (vault):** prep note created via filesystem Write at the canonical deep path; clicking its `[[wikilink]]` before Obsidian indexed it spawned an empty stub at a root `AAI - Project Folder/` — deleted, canonical intact. Use obsidian-cli for new vault notes + wikilinks to avoid the index-lag stub. See [[feedback_confirm_ask_before_producing]].

---

## May 27 — Cross-Harness Skill Registry idea + "There Waiting" blog + Ian refinement

Bucharest-prep session pivoted into a new Pedro proposal, banked in two vault notes (English, filesystem Write): [[Cross-Harness Skill Registry — Gap Proposal]] (internal, dated, objection-handling) + [[From North Star to There Waiting]] (public blog draft, Ian-style, ends on a question).

**The idea (Pedro, 2026-05-27).** In the distributed-harness model (any harness: AOv2, Claude SDK, Codex, custom), nobody owns a curated, cross-harness, customer-facing way to find/reach the right skill. AOv2's marketplace = per-repo `marketplace.json` + `SKILL.md` (Anthropic format), dev-facing, install-time, no review gate, not aggregated. Gap is systemic (AOv2 included). Confluence grounding: "Beginner's guide to add a plugin/skills to AEP AO 2.0" (3851715892, V. Barshikar); AIA Platform Architecture shows `marketplace · catalog · installer` already forming.

**Scope.** Jobs = (a) discovery + (b) routing/selection (NOT (c) entitlement = AO+commerce, later). Curation gate at entry. **Schema = the moat** (what each harness declares to appear: id/owner/persona/context/lifecycle/harness/deployment) = definition-ownership = [[H-005]]. **Harness-agnostic — "which harness" is a metadata field, NOT the axis.** Pedro's own correction: don't make "in AOv2 / not in AOv2" the organizing axis (re-centers on an undecided platform, couples fate to it, leaks implementation into the customer view, breaks Ian's consistency mandate). The "in/not-in-AOv2" view is legit only as a separate internal migration tracker.

**Positioning.** Anchor "publish vs find" (dev publishes into a harness / customer finds across all). Avoid "plumbing" (denigrates AO/Ian) + "App Store" (implies entitlement). Lead positive; AOv2-contrast yes-and only if challenged.

**🆕 Ian refinement (Slack, 2026-05-27) — pre-align worked.** Pedro DM'd Ian the angle before publishing; Ian engaged (not blindsided). Ian: *"The customer should not have to find the right skill, it should be there waiting"* — a UI surface connects to a harness with all applicable skills present, "precise and complete"; skills defined once, used in many harnesses. **Not a rejection, a relocation:** "there waiting, precise and complete" REQUIRES Pedro's machinery (a registry that knows all skills across harnesses + curation that keeps each surface precise+complete as skills proliferate). **The move (banked): concede the front-end (browse = friction, Ian right), claim the back-end (registry + schema + curation = nobody owns it = the moat).** Don't litigate; forward-frame. Pedro sent the reply.

**Blog reshaped:** title "From North Star to **There Waiting**" (Ian's words = credit + co-shaped). Spine: browse is the wrong answer (GPT Store cautionary tale) → there-waiting (Ian) → backstage shared-declaration + curation → the one browse case = admin/buyer (storefront survives there) → close on the schema question ("what must each harness declare").

**Credit mechanics (SD visibility gap).** Write-to-own (Ian's model). Authorship banked dated. **Publish the blog (public/indexed/citable), NOT email** — email = megaphone to point seniors at the post, blog = venue. Pre-align gate: Ian ✅ → Bertrand + Conrad heads-up → publish as open question. Turf = the real risk (AIA Hailpern building catalog/installer; AO), NOT "PM not architect" (Ian: selection+consistency "must be PM lead"). Don't call it "officially mine" pre-landing.

Pending: requirement block signed Pedro for the Saar-bound input; rename blog file to match title.

---

## May 12 P42 Status Sync — Loni reframe + Ian = North Star architect

Source: `Meeting Notes/Yanira/20260512 - P42 Status Sync.md`. Bertrand + Ian Boston + Jaclyn (+ Pedro arriving). 112-line transcript cuts at 6:30 mid-handoff to Pedro.

**1. 🚨 Loni reframe verbatim (May 11, reported by Bertrand May 12).** Loni: *"No, that's not the question. Question is context, and how do we equip our agents with proper context."* Explicit rejection of AOv2 yes/no framing. Pivot = **context architecture** as the strategic axis. Bertrand: *"more than memory. Connecting content sources from different places and deciding which bits should be passed as actual content."* → Strategic anchor for May 11 deck. **Open the deck with this.**

**2. 🚨 Ian Boston = North Star architect for AEM agents AOv2 strategy.** Bertrand 6:30 verbatim: *"this looks like a new North Star architecture for Pedro."* — interpretation: Ian's architecture serves as **North Star *for* Pedro's work**, NOT Pedro is the architect. Ian = author. Pedro = consumer / operationalizer / PM distribution layer. **Ian self-assigned: one-pager for teams.** Watch for Ian deliverable.

**3. Ian's AOv2 requirements list (5 items — Ian-authored):**
   - Skill portability: skill must work everywhere (Claude SDK, codex, Claude AI, AOv2) without per-harness config.
   - URL auto-recognition: AOv2 recognizes registered Adobe APIs without lockdown config.
   - Properly open source — no private dependencies. Anyone in Adobe can fork + run own server.
   - Standards compliant — skill from any location works.
   - A2A retire confirmed (no customer interest).

**4. Forcing-function lever Ian named.** *"Any skills not using registered APIs that we recognize just won't work in AOv2... so make sure your APIs are good."* AEM-wide API quality = forcing function for cross-agent technical standards. Pedro's PM lane: drive this across agent teams.

**5. Skills/MCP/API hierarchy direction.** API first. MCP retained — wrap existing MCPs in skills. First skill iteration reuses MCPs. A2A out. Aligns with Carsten May 6 proposal.

**6. Governance Agent = prior art on global-context API.** Bertrand: *"that's exactly what AEM governance is working as well, on this global context."* Philippe's Governance has built context-API substrate. Reuse signal. **Tension:** Pedro needs Philippe's prior art for portfolio narrative — handle transactionally given competitor frame. Don't hand Philippe the framing of the cross-agent context story; cite Governance as a reference implementation while keeping the portfolio narrative under Pedro.

**7. "Burned from AOv1" — Jaclyn confirm (5:05).** *"They're so burned from ao of one."* AOv2 must clear a high bar. Reinforces Felix May 5 ("hors sol" critique) + Conrad April 14 ("widely not flying").

**Pedro's actual role here (corrected):**
- Not the architect — Ian owns that.
- Pedro = PM liaison + distributor + portfolio operator. Carries Ian's one-pager into agent teams. Compiles requirements + commitments + SLAs back to AOv2.
- Compounds with H-005 (substrate-before-standard) — Pedro owns the data substrate; Ian owns the architecture spec. Different lanes, mutually reinforcing.
- Still material for Senior Director path: being **named in the room** when VP architecture conversation lands. Promotion-frame is "operating at architecture-conversation altitude," NOT "I am the architect."

**May 11 deck implications (corrected):**
- Open with Loni context-reframe (verbatim).
- Requirements slide = Ian-authored, Pedro distributes. Credit Ian explicitly.
- Pedro's slide = PM operator / liaison / portfolio reporter — own substrate + distribution, not architecture.
- Mithril Silvia context-reading ask = visible expression of Loni reframe; same-day Pedro→Silvia hedge ("don't promise v2") consistent with Loni "context is the question."
- Governance Agent global-context callout (reference implementation reuse).

**Cross-links:**
- Mithril ↔ Silvia loop (May 12 EH-side memory) — context-reading primitive ask now has explicit VP-level (Loni) backing.
- Trent April 29 "AEM Context = North Star question" + Bertrand May 12 "North Star architecture" = compounding label around context-architecture as cross-Adobe primitive.

**Open / TBD:**
- Transcript cut at 6:30 (Bertrand: *"Two questions... Do you want to..."*) — Pedro's portion not in this file. Find Pedro segment if recorded separately or follow up with Bertrand on what was assigned.
- 🟢 **Ian one-pager LANDED 2026-05-19** (was NOT produced as of 2026-05-18). Self-assigned May 12, published as a blog May 19 — the day after the Agent Owners call where Pedro publicly named Ian owner. North Star requirements doc was the gating artifact for per-team AOv2 evaluation; now Pedro CAN reference + distribute it. See "May 19 — Ian publishes Agentic NorthStar" entry.
- Governance global-context API technical detail — schedule Philippe sync (carefully framed).

---

## May 13 — Felix + Lara + Pedro 3-way (External Agent naming lock, Langfuse pipeline, cost data)

Source: `Meeting Notes/Felix Pedro 1 1/20260513 - Felix Lara Pedro 1 1.md`. ~30 min EN.

**1. 🆕 "MCP report" → "External Agent Report" naming locked.** Felix: *"MCP je suis allergique à ce mot là."* MCP ambiguous (Tanju millions of internal tool calls true; ChatGPT-Copilot consumption near-zero also true). New architecture:
   - **AI Assistant Report** (internal AEM assistant usage)
   - **External Agent Report** (Adobe agents consumed via ChatGPT / Copilot / Claude — MCP integration layer)
   - **Umbrella high-level comparison report**
   - Companion to existing "Tool Calls" counter-unit lock (May 6). Both naming rules live for May 11 deck.

**2. Lara Langfuse pipeline for Governance.** PR in flight to send correct trace tags on Langfuse. Friday May 15 merge → prod → weekend backfill → Monday May 19 data → integrate into report. POC = manual CSV download from Langfuse → DB. Felix preferred long-term mechanism: push from agents → central DB via IMS user token.

**3. User metadata enrichment (Felix ↔ Bertrand from Playground team).** User table now has full_name / user_type (4 types) / email via API. Felix full sync script done — remote API-based, no longer local. Bridge between systems operational.

**4. Internal/external classification — Raul list = current gospel.** Raul updated list yesterday May 12 → Pedro processed → reports show org/user increase (explains anomaly in numbers). ~18-20 Raul-flagged-external orgs look internal (lab/sandbox). Felix heuristic catches 30-40 obvious-Adobe (Adobe Corp, Adobe Consulting marked external in Raul list). Pedro decision: stick with Raul until classification aligned, avoid display↔data divergence. Still pursuing API/MCP source vs github README.

**5. 🆕 Mark Pfaff = new contact.** ECP usage + tool calls cross-check on Databricks. Numbers align both platforms. Pedro started Governance External Agent report based on Mark's work — tool calls, users, repeated users. Add to Stakeholder Map.

**6. Portfolio report landing-page link shipped.** AEM report EDS landing page now has direct portfolio link. Layout = Gilles slide / Felix May 12 slide reproduced. Includes MAU retention (under hood for G&R sync, senior-management abstract).

**7. Rubin posture confirmed 🟢.** Pedro tested Rubin. Won't replace AAI substrate medium-term. Felix: **LLM-as-Judge = the moat.** Rubin has returning users/orgs, not the judge layer. Confirms H-005 substrate-before-standard.

**8. 🆕 Cost data — $2K/mo report generation.** ~30% LLM-as-Judge (heavy, accepted). Rest = per-block Opus call on every text block × many blocks × many pages. Lara push: most blocks should be static code, only key findings need LLM. Felix agreed, will streamline. $100-150 per report at full price. Governance agent prod cost: ~$100/mo. EPA/their agent: <$10/mo.

**9. MCP UI for engineers (Felix).** Lara + Pedro added. Slow (summary executed per request — Felix removing). Once API+MCP done, weekly EPA download for engineer problem-detection. aitools-flex slow PR cycle = blocker.

**10. Cadence.** Pedro off Thu+Fri. Lara works Fri. Next 3-way Monday May 18.

---

## May 12 — Bertrand 1-1 (FR, ~20 min)

Source: `Meeting Notes/Bertrand 1 1/20260512 - Bertrand Pedro 1 1.md`. Chronologically: this 1-1 → P42 Status Sync (same day) → Mithril Silvia (same day). Pedro got Loni reframe from Bertrand here, relayed to Silvia hours later, Bertrand re-stated at P42 to Ian.

**1. 🚨 May 11 deck framing locked.** Bertrand: *"Un point de vue AEM sur ao deux zéro. Qu'est ce qu'on va faire? C'est surtout pas la question. Faut pas dire deux zéro si les gens vont se braquer du fait de l'expérience pas terrible."* **Don't say "v2." Frame = requirements-first.** People defensive due to v1 experience. Action: document what AOv2 brings.

**2. Loni reframe — second layer (verbatim via Bertrand).** *"elle a remis une couche notamment sur la dimension contexte, est ce que dans la solution qu'on voudra utiliser pour nos agents, il faut pouvoir plugger proprement ce qu'on va construire pour gérer le contexte."* Context-management plug-in capability = requirement. AOv2 fits or not — TBD. Plus skills hierarchy structure open. **Loni reframe is layered + reinforced, not one-shot.**

**3. Friday softening signal.** Gilles + Felix + Michael talked Friday. Position softened to *"peut être quelque chose qu'on regarde"* — less categorical than Thursday. Direction-emerging frame holds.

**4. ⚠ R Cross-surface AI Assistant continuity vs Michael compliance.** Bertrand: *"il nous faut que toutes les surfaces, les interfaces AEM... qu'on puisse avoir des échanges assistants ui, ui assistance."* Bilateral UI↔Assistant + conversation continuity across surfaces. **Michael disagreed** — compliance: conversations must stay in same primary region as Cloud Service. Tension echoes Ian Apr 1 data-residency risk. Open.

**5. Skills vs context distinction (Bertrand mental model).** Skills = technical context (LLM request adds skills). Context (Bertrand sense) = closer to Governance Agent prior art — content + instructions. Skills possibly customer-contributed. Pedro: *"j'ai pas encore complètement digéré ce que c'est supposé faire."*

**6. Open architecture question (Pedro, unresolved).** One AI Assistant per agent / per domain? Or one global Assistant? If global: how differentiate skills + context per domain? Bertrand answer: **context-awareness routing** — *"Je suis dans page Editor donc les skills qui vont bien c'est ça."* Assumes Mithril team thought about this. Open.

**7. 🔴 Migration timeline — September unrealistic.** Pedro to Bertrand: *"il ne faut pas imaginer que la mise V c'est septembre et que tout le monde sera prêt en septembre."* Multi-month mixed-state window confirmed. Same point Pedro raised w/ Silvia same day.

**8. Silvia reported to Bertrand.** Pedro: Silvia "very actively" pushing for content-awareness via Tim. Coached: synchronize w/ Guliz BUT careful *"on n'a pas choisi avoué deux."* Bertrand confirms Gilles + Michael had AOv2-counterpart meeting with Manas + Ken — relayed "v1 was very complicated."

**9. 🆕 🟢 Workshop Foundation — Bertrand asked Pedro to facilitate skill-proliferation session.** Peter Parker dropped, had 2 agenda items. One item = *"comment on va gérer la prolifération ou la gestion des skills à l'échelle d'aem."* Bertrand: *"Je cherche un animateur pour cette session, tu n'en as pas parlé?"* — Pedro hasn't responded. **Opportunity. Same lane as Ian's API-quality forcing function.** Pedro action: accept facilitator role.

**10. 🔴 Usage numbers DESCENDING — Jaclyn asked for JM + Loni numbers.** Pedro pulled. Internal/external categorization still problematic → impacts numbers. **Numbers show usage going down.** Post-Summit partially explains. *"j'espère que les chiffres sont pas trop faux."* Working w/ Yanira + André Bedas + Raoul on single source of truth.

**11. 🟢 Grafana Bertrand presented Friday = "off completely" — Raul fix closes drift.** Pedro at 1-1: *"pas mal off"* because Bertrand pulled all orgs unfiltered + end-March → May Raul-list scorecard drift. **Raul has since fixed the list** — Namita banner no longer needed. JSON-config-too-large constraint may still need separate attention (Grafana stopped supporting), confirm before next exec demo. Pedro reports stayed approximately right throughout.

**12. JM/Loni first meeting structure.** 45 min - 1h. Pedro proposed deck order: status → inhibitors (slides updated) → credit usage UP → retention → MCP add-on if interested. Splunk MCP: lots of noise, little signal, few tool calls yet. Governance MCP report done, others in progress.

**13. Corey review confirmed in 1-1.** *"Pas mal de cosmétiques et d'utilisabilité."* Call held May 14 (see "May 14 — Corey 1-1" entry).

**Pedro action items from this 1-1:**
- Accept Workshop Foundation facilitator role for skill-proliferation session.
- Land JM/Loni deck order: status → inhibitors → credit-up → retention → (optional) MCP.
- Verify Grafana JSON-config-size issue separate from Raul-list drift; confirm Grafana refresh post-Raul-fix before next exec demo.
- Build credit-usage-up + customer-trust slides w/ Quiet-Hours-via-Agents 81-customer beta as concrete proof point (EH cross).

---

## May 12 — Mithril Silvia Eugene Pedro sync (EH/AAI cross-cutting)

Source: `Meeting Notes/Eugene/20260512 - Mythril Silvia Eugene Pedro Sync.md`. ~22 min EN.

**1. Pedro hedge confirmed in room.** Told Silvia: AEM teams not committed to AOv2. Sites pushing back hard. Don't promise v2 in upstream conversations. Use cautious language. Aligns w/ Decouple-Architecture-Ask knowledge entry.

**2. Loni reframe surfaced same day (pre-P42).** Pedro relayed to Silvia: *"Loney comes with: maybe v2 is not the correct question. Maybe we should ourselves list the requirements and then see how v2 would fit in."* Same Loni reframe Bertrand reported at P42 hours later → converging signal at VP level.

**3. AEM evaluation criteria (Pedro stated in room):** Skills > orchestrator. Portable skills (work w/ Claude / ChatGPT / AOv2). Open-source platform model (fork + PR). Output = requirements + commitments + SLAs to AOv2.

**4. 🆕 Silvia use case explicit:** *"We don't want AI to interact with UI. We want AI to read UI."* Mithril demo missed this — context-reading not in MVP. Will raise w/ Tim Lynn + Matthew tomorrow May 13.

**5. Silvia parallel work — Guliz-assigned.** Design POV on AOv2 for AEM. Analysis this week. Pedro action: send Silvia engineering-manager list per AEM agent team. She'll connect for UI/context portion.

**6. Eugene Mithril framing.** Current AI Assistant icon = dummy, opens same chat everywhere, no UI context. Post-Mithril = contextual per-surface (pipeline, etc.). Strategic surface rollout, not blanket.

**7. 🆕 Migration window UX problem (Pedro raised).** Multi-month window where some agents on v1, some on v2, some migrating. User won't know which has skills/Mithril vs which doesn't. Open product question. Silvia mitigation: in-app notification (*"version of LLM not supporting this data, stay tuned"*). Eugene: low risk, customers not workflow-dependent yet.

**8. 🆕 AI Assistant pricing question (Silvia raised).** Free or paid? Affects failure-tolerance UX. Pedro recalls: SKU exists post-Summit, token package, run out → purchase. **Action: confirm w/ Bertrand.** Ties to Bertrand April 29 pricing/SKU bombshell.

**9. Data instability flagged (Pedro→Silvia).** Org counts fluctuating morning vs evening due to Raul-list manual update. Beware numbers.

**10. 🆕 Matthew = new Mithril co-owner stakeholder.** Surname TBD. Tomorrow's Silvia + Eugene sync includes him + Tim Lynn. Pedro NOT invited.

**Pedro actions tracked:**
- Send Silvia engineering-manager-per-agent list.
- Check w/ Bertrand on AI Assistant SKU/pricing.
- Stay tuned for Silvia/Tim/Matthew sync outcome (May 13).

---

## May 18 — Agent Owners Alignment (Pedro HOSTED)

Source: `Meeting Notes` → `Agent Owner Alignement/20260518 - Agents Owners Alignement - .md`. ~32 min, EN. **Transcript now COMPLETE (gap 14:21→29:05 filled 2026-05-19) — items 4/5/8 revised + new signals 9-12 added.**

**1. 🆕 Pedro hosted the cross-agent forum (Yanira on PTO).** First time Pedro chairs the Agent Owners Alignment. Ran agenda, gave the AOv2 status himself, handed mic to Bertrand for roadmap process. Visibility / altitude data point — Pedro operating the standing cross-agent venue, not just contributing. Bank for Senior Director narrative; offer to be Yanira's standing backup host.

**2. 🆕 CCF / ISO 42001 scope NARROWED (Robert Guthrie).** Initial scope = all AEM agents. Now = **Discovery Agent + Governance Agent only** this year. Loni + Bertrand still finalizing exact list. Deadline **July 17** to be compliant (auditors collect evidence Aug-Oct, possibly into Oct). 10-12 CCF controls mapping to ISO 42001 international standard. Other teams may opt in if ready. **Bertrand (verbatim):** *"important, but not really urgent... not going to block any deal that we know of in the next two quarters... not top of stack at the moment."* Tech GRC may begin reaching out to Discovery + Governance teams. **Supersedes May 4 entry** (was ~12-13 tickets, all agents). Downgrade tracking 🔴 → 🟡.

**3. 🆕 Roadmap deck restructure (Bertrand, NEW format).** Timeline view of internal + GA dates → per-agent overview slide (production, modernization, development — Brian started development overview) → per-skill/job detail slide for any non-self-explanatory bullet. **Snapshot cut THIS Friday May 22** → handed to a design agency for refinement. **Final Friday May 29** → distributed broadly: roadmap webinars, field, customers, support. First time roadmap restructured this way. Bertrand: *"every word, every bit, every minute we spend on the deck is not wasting time, this is used a lot in the field."* Agent owners PM + eng asked to invest time this week. **Pedro lane:** as host + portfolio operator, ensure his 6 agents have timeline + overview coverage before May 22.

**4. AOv2 — Pedro framed publicly as host (the "introduce the request" already partly executed).** Pedro stated: confirming from Bertrand ("the architect") **green light for the EVALUATION of migrating current platform onto AOv2, NOT the decision**. *"There are still questions at senior management if [AO]V2 is the platform that we should move into."* Directions Pedro named to Ian: open-source model (fork + PR), moving into skills. Requirements-first framing landed verbally with agent owners. The drafted broadcast message becomes the written follow-up with criteria + AS-IS staging ask.

**5. 🟢 Ian North Star 1-pager — LANDED 2026-05-19** (verbatim May 18: *"I'm about to start... I haven't actually started it"* → published the very next day). Pedro publicly named Ian owner on this call; Ian shipped [Agentic NorthStar](https://wiki.corp.adobe.com/spaces/~boston/blog/2026/05/19/3894002388/Agentic+NorthStar) May 19. **Public-naming → delivery: a forcing-function win without the forcing-function Slack.** Gating artifact resolved. See "May 19 — Ian publishes Agentic NorthStar" entry.

**5b. 🆕 Ian "prove-it-first" posture (14:42-15:35).** AOv1 failure modes Ian named: hard/slow agent onboarding into AOv1, delays in license-usage reporting. North Star requirement = don't repeat these. Ian verbatim: *"AOv2 has got [to] prove itself, prove that it can deliver those things to us before we agree to commit to it. Now others may have different views."* This IS the requirements frame — AOv2 must prove delivery against AOv1 pain before AEM commits. Strong evaluation-not-decision anchor, sourced to the architect.

**5c. 🆕🚨 Bertrand "Adobe Harness" rename + multi-layer context/memory = the North Star content seed (17:09-19:05).** Bertrand sensing AO → **"Adobe Harness"** rename ("AO 2.0 will have a new name soon"), more than an agent orchestrator. The harness must provide, so AEM doesn't build it itself: **memory management** (Claude-Code-style compaction, project/state storage, short + long term), **context management** at org / app / user layers. Bertrand: *"content is context for AEM. Skills would be context as well. User preferences, what the user has been doing... different layers of context."* Skills alone = one piece of context only. **Bertrand's explicit ask: AEM must document what it needs from the foundational Adobe layer.** This is the actual scope seed for Ian's 1-pager — context mgmt + memory mgmt + multi-layer context, beyond skill files. Ties directly to Loni's context reframe.

**6. 🆕 Ian deploy-to-stage skill.** Ian: *"I have a skill to deploy these sort of things to a single pod in stage, which Claude will do for you."* Claude-driven single-pod stage deploy. Bertrand referenced developer console + I/O runtime as logical fit. **Enabling asset for the per-team AOv2 AS-IS staging evaluation** — reference it in the broadcast so teams have a deploy path.

**7. 🔴 Greg Klebus — customer escalation.** Rosh + Genentech want to go big on agents, deployed across **multiple IMS orgs**. AOv1 today **limits agent scope to 1 IMS org**. Greg asked Ian to join customer architect / implementation-partner conversations as eng/arch rep — future-proof deployment across **AEM + AJO + AEP**. Greg will summarize outcome. Expected to recur with larger customers. **Concrete customer-driven requirement** — feed into Ian's North Star input + Pedro's portfolio requirements lane. Track Genentech + Rosh as named drivers.

**8. Philippe demo (agent automation) — substance captured.** Governance Agent learning: customers don't just want better tooling, they want to **change the whole flow**. Demo: asset update → governance check → pass = one action, fail = create Jira bug with reasoning/suggestion/annotation on the asset. Triggers: asset change, Jira ticket events. Deterministic flow + can call MCP / start flow from an MCP code event. Built for an upcoming **Samsung demo**. Philippe's framing: shift from tooling to customer self-service, *"we are not scalable now,"* integrate at the CR start or push info back at the end. Pedro offered to share docs/pointers with the group; Philippe terse (*"Yeah, well, I'm sure you do."*) — competitor-frame caution holds.

**8b. 🆕 Bertrand reaction to Philippe demo — positioning unclear + proliferation-governance concern (25:40-27:35).** Bertrand: impressive ("power of web coding") BUT *"I'm not sure where it fits... this is a developer-centric tool... a UI like this could be in the Adobe Developer Console."* Target persona unclear. **Open PM concern (verbatim-anchored):** *"if all of us start coming up with things like that every other week, that's going to be very challenging to manage in product management... what should get attention, priority... lots of ideas can be implemented quickly and how do we sort that out? Where is our business going? What is it worth investing in business-wise beyond the technology?"* — Bertrand naming the **initiative/skill-proliferation governance gap in the open**. Direct tie to the Workshop Foundation skill-proliferation session Bertrand asked Pedro to facilitate (May 12 memory). Reinforces that ask publicly.

**9. 🆕🚨 Gilles Knobloch — skills-portable-NOW, decoupled from AOv2 (15:38-16:55).** Gilles asked his team: can we move into skills development WITHOUT waiting for AOv2? **Experience Production Agent team already did it** — defined skill files, plugged into **AO V1 with zero AOv2 dependency**, skill files portable later (move to AOv2, integrate in Experience Workspace). Motivation = team "stuck in velocity." Demo recording forwarded. *"A nice compromise — get benefits of the future architecture without having to wait for it."* Pedro committed: *"I'll take your demo, Gilles, and just see where we can spread it."* **Material: this operationalizes Decouple-Architecture-Ask-from-Platform-Commit-Timeline — skills work proceeds regardless of AOv2 commit. Distribute the demo across agent teams.**

**10. 🆕 Gilles NL-flow vision + localhost deploy gap (27:49-28:58).** Wants natural-language flow description (not box-connecting); checked Philippe repo, not obvious. Vision: customer meeting → transcript → auto-generate flow → next-day confirm with customer → functional demo. Deploy gap: Philippe tool runs localhost (*"do we deploy it to? I see localhost."*) → leads into Ian deploy-to-stage skill + Bertrand dev-console / I/O-runtime fit.

**Pedro proactive actions (revised post full transcript):**
- **Get Gilles' EPA portable-skills demo recording; distribute across agent teams.** Pedro committed in-room. This decouples skills work from AOv2 commit — high-leverage, unblocks velocity, aligns with the Decouple knowledge entry.
- **Seed Ian's North Star with now-rich content:** Bertrand's Adobe-Harness layered context + memory mgmt requirements + Ian's "avoid AOv1 onboarding/license-reporting failure modes" + Greg multi-IMS-org + EH context-reading. The seed is no longer thin — scaffold the doc and hand Ian a populated draft.
- Convert verbal AOv2 framing into written broadcast (evaluation not decision, AS-IS staging, Ian deploy-skill pointer, Gilles skills-portable-now path).
- Escalate Ian 1-pager via Bertrand forcing-function Slack.
- Drive roadmap-deck coverage for the 6 agents before Fri May 22 cut.
- Capture Greg multi-IMS-org + Genentech/Rosh as portfolio requirement; get Greg's summary.
- **Accept Workshop Foundation skill-proliferation facilitator role** — Bertrand's in-meeting proliferation-governance lament is the public reinforcement; the forum is the answer to his own concern.
- CCF reconcile: Discovery + Governance only, July 17, deprioritized.
- Bank host role; offer standing backup-host for Yanira.
