> ## Long-form reference sections moved out of project_aem_agents_intelligence.md (load on demand)

## Index (what's here)
- **Early June 2026 (06-01 → 06-12)** — Bucharest keynote delivery + slide work + early Coworker discovery (added to archive 2026-06-24; see section at the bottom). Includes the 06-01 #aem-agents fragmentation threads, the 06-03/04/05 consistency-layer + Felix single-harness work, the 06-06→10 Bucharest deck, the 06-10/12 Rubin + AIA-timeline risks, Cole 1-1 (06-11).
- May banner tail + 2026-05-19 consolidation checkpoint
- Varun Kalra Discovery sync (Apr 22)
- Loni + Jean-Michel May 11 meeting; H2 Planning (Apr 28); P42 Status (Apr 21); Yanira consolidation (Apr 30); BVR Governance Agent (Apr 23)
- H-005 RESOLVED; EGT workshop (May 28); Ian AOv2 decision (May 12); Eugene/Silvia A2UI mechanism (May 28); Apoorva entry-point thread (May 28-29)
- May 6 x4 (MCP MOC, Namita, Yanira, Felix); May 5 x2 (Bertrand, Felix)
- May 12-27 cluster: Mithril/Tim, Corey 1-1s, eng bridge, close-out, Ian NorthStar publish+thread, Bucharest framing, Skill Registry, P42 sync, Felix/Lara, Bertrand 1-1, Mithril sync, AOA May 18

---

## Felix reports + report pipeline

**LIVE for EPA.** Shared with Bertrand April 9. Bertrand named Pedro and the dashboard in Loni's H2 planning meeting April 13 — public sponsorship at VP level. Conrad validated in Agent Owner alignment same day. Jim Stoklosa feedback incorporated April 13.

**Report-to-JIRA pipeline.** Tested with Governance Agent. Validated by Varun (April 22): useful IF end-to-end inside same UI; not useful as separate skill. Need JIRA column with ticket + end date per action item. MCP idea (Gilles Knobloch) — parking lot.

**Report hosting.** Certificate approved by Shankari April 9. Felix + Quentin configuring CDN + Okta path. Unblocked.

**Jim Stoklosa role:** prepares EPA reports for Corey Dulimba. Validation role = data accuracy + feature behavior. Corey = PM owner sign-off (lighter ask, but required for Loni path).

**Audit Sprint April 30:** 9 of 16 audit items closed in single day. 10 PRs. Wave 1 Tier 1 (5 trust-hygiene), Wave 2 Tier 2 (4 visible-commitment), 2 of Tier 3 early. Plus 2 Important Indicators (#4 No-Results Triage, #5 Owner column on Capability Gap Map). Plus monthly retention shipped (PR #55) revealing **45% weekly orgs vs 71.2% monthly orgs stickiness gap** on Discovery W17.

### 🟡 2026-05-05 — Reports → DaaS / evaluator migration call (Pedro + André + convener + Mark/Lara track) [backfilled 2026-06-05]

Source: `AEM Agents Intelligence/AEM Experience Agent Reports/20260505 - Agent reports move to Daas.md` (Otter). Call to align Pedro's weekly agentic report with the **in-region evaluator framework**.

- **André** = the evaluator builder. Framework: each agent pushes traces → **regional Delta table**; per-region/per-agent evaluators read raw prompts, run **LLM-as-judge** against PM-defined criteria **in region**, push a **score** → centralized **Databricks** table (cross-region/cluster/agent). Has a config app where teams define criteria + region (the fancy UI replacing git markdown). Uses in-region OpenAI. Wants Pedro's git + wikis to understand + recreate an existing metric as a test.
- **Convener (Speaker 1, governance/observability + supports Mark Pfaff)** = the push: **replace Pedro's manual stack with a NEW app**, everyone defines criteria once there, data in Databricks, then layer agents/MCP so senior mgmt can ask high-level questions. Governance agent = **customer zero**, then sell adoption to other teams. **JC/JCSR** want Pedro + governance aligned → present a **business story** so teams come to adopt. **Mark Pfaff + Lara** = evaluator metric definition on harder KPIs.
- **The legitimate migration driver = compliance.** Pedro on record: *"compliance is not a topic here, it should be"* — current pipeline = **Bedrock cross-region + cross-region aggregation ("which is bad, which I know")**. Evaluator = in-region, PII-compliant → closes Ian's data-residency risk + Michael's pushback. This is the clean reason to migrate off the manual SQLite/Bedrock pipeline.
- **Pedro's persona model (his framing, leadership-facing):** 3 personas — technical teams (Langfuse traces, stays), agent-owners/PMs (per-capability stats), senior mgmt (aggregated). Two report layers: **Python-calculable KPIs** + **Business Value Realization** (LLM-as-judge, one definition file per BVR block in git, refined with each PM). **Not done yet:** aggregate BVR into one number per agent + one overall number.
- **⚠️ Strategic guard (same move as the harness session):** don't own the engine (André's evaluator infra + Databricks = theirs), **own the definition** — the persona model, the BVR criteria files, the aggregation logic, the business story JC wants. Pedro *wants* to hand off the manual pipeline ("set me free") — fine, but the weekly report is his **visible leadership artifact**; if it's absorbed into an app owned by the convener + André, keep the definition/narrative layer as Pedro's so visibility doesn't migrate with the infra.
- **Ties:** Rubin needs AEP/AOv2 data (Bertrand 6/4) → this in-region Databricks = the source; Mark Pfaff (evaluator) = the MCP-report person Pedro wanted to sit with (+ Tanju). **Pedro action (taken):** share git/wikis/repos with André + test recreating one existing metric in his app. (Pedro was traveling the following week = Bucharest.)

### 🟢 2026-06-05 — Friday arch session HELD (Ian Boston + Felix Meschberger + Pedro): critical-vs-flexible list co-built live, engine NOT decided

Source: `AEM Agents Intelligence/Agent Owner Alignement/20260605 - Ian Felix Pedro.md` (Otter; file was misnamed `0505`, renamed `0605` — this is the **June 5 arch session itself**, not a May event; Speaker 1 = **Felix Meschberger**, relabeled; Speaker 2 = brief, unidentified). **This IS the Friday architecture session the cockpit prepped.** Pedro opened by **naming the elephant** (one harness vs many) — not in the capture, transcript starts mid-flow at 0:00. The room (just Pedro + Ian + Felix, as planned — Reasor was the Slack thread, not this room) **built the critical-vs-flexible list live in a wiki Pedro captures.** Clean execution of the cockpit: elephant named, engine left open, definition owned by Pedro. **The June fork developments (Tanju middle-path, consume-vs-fork, the public RFC) did NOT surface in-room** — they stayed at definition level (Ian: *"we're going too deep… these are conceptual guidelines"*).

**Ian's framing principle (open):** negotiate what's org-wide (identity) vs an abstract pattern that lets solutions innovate. *"If we stifle innovation, we stifle innovation."* All agreed: core UX must be consistent + some core APIs consistent (else duplication).

**Agreed CRITICAL (co-signed Ian + Felix):**
- **Common UX** — chat grammar + core controls + what "+" offers. Starts with **design/brand** ("what does the chat look like"), negotiated across all CX by those who normally do that work. Ian: *"common One Adobe, not One AEM."*
- **In-context, NOT "one touch point to rule them all"** (= the AI Assistant out-of-context mistake). Felix: a common UI dropped in everywhere, but in-context.
- **Core services:** memory (bits across all Adobe), IMS identity (**AIP** should drive — note AIP not AEP), compliance = Adobe policy compliance (CCF, SOC2, HIPAA, FSI). Ian reframes compliance as data-compliance/governance/access/identity properties, not the standards themselves.
- **Skills:** declaration + portability (markdown transportable; **Agent Skills** spec — capital-S = Anthropic skills). EW treats skills as content (markdown, no code).
- **Per-session scoping** of capabilities (skills/MCP/API/tools) **seeded by the surface** — two lines: what's in the surface, what enters the session.
- **Skill selection per surface** — teams have complete control over which skills are available (the AI v1 failure: "analyze my pages" → flips to analytics → "you're not licensed" → "it's my content").
- **Stays current with Anthropic/Claude + standards** = top-level critical. Standards stack: **Agent Skills (top) → Open API → MCP (bottom)**.

**Agreed FLEXIBLE / NOT critical:**
- **Implementation / shared components** (React? MFE?). 💥 **Ian's January experiment = the proof:** team told "make it Spectrum" → agents *found the Spectrum definition and wrote the CSS from scratch, accurate, zero imported code.* Ian: *"that's why I don't think we need the components — components add friction."* Felix conceded: *"critical for UX, not critical from an implementation perspective."* = Pedro's definition-not-components thesis, **proven by Ian, accepted by Felix, in the room.** The shared-component-library question was effectively closed here.
- **How the surface tells the harness which skills** — tag / prompt / semantic search (multiple ways). But Ian: non-deterministic search = uncomfortable → prefer a **curated, referenced, tested list** per surface (quality risk otherwise).

**Architecture nuances captured in-room:**
- **Drive functionality DOWN: tools > APIs > MCPs** (token footprint — Adobe burnt tokens enabling all MCPs). Heavy deterministic ops (roll out 100k pages) → behind an API/MCP, NOT in the harness. Harness executes short code (<20-50 lines, no external deps) in a sandbox.
- **Code execution = the AOv2 gap** Ian named: AOv2 couldn't "calculate pi to 100 figures"; Codex (his recent test) wrote + ran Python in a sandbox and did. (Ian: any harness implementer won't build from scratch — they take Claude/Codex/Pi → the engine question is below the list, left open.)
- **Skills authored dynamically "feel more like memory"** (personal to person/team) — ties Ian's two-layer memory framing (surface-base skills vs individual/team-learnt = memory).

**🟢 What Pedro walked away owning:** Pedro closed with *"I'll capture that in a wiki page so we can extend from there, and open up whenever we feel comfortable."* → **Pedro owns the definition artifact (the wiki).** Ian + Felix both contributed to *Pedro's* captured list = the consistency-layer ownership made concrete, three-way, without Pedro adjudicating the engine. Felix to send Pedro another link with his own additions.

**🟡 Still open / follow-ups:** (a) **engine/harness count = deliberately not decided** (good — matches the plan); the formal "open question with owner + resolving evidence" was discussed at principle level but **not written down as a parked item with an owner** → Pedro to formalize in the wiki. (b) Ian flagged **interpretation risk** (*"this wording will cause interpretation… conceptual guidelines, not directive"*) → the wiki wording needs care so teams don't read it as "model a SkillSelectionPerSurface object." (c) aggregate the captured list into the shareable wiki + decide when to open it up.

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

