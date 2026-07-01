> ## Archive shard — project_aem_agents_intelligence — 2026-W19

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

