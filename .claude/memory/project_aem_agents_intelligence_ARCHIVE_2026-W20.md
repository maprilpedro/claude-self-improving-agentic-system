> ## Archive shard — project_aem_agents_intelligence — 2026-W20

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

## May 12 — Ian's AOv2 decision (Conrad delegated) — DECISION-GRADE, closes "discussed not decided"

Source: #aem-agents (`C09J94L2TAR`) Ian Boston post 2026-05-12 08:18 CEST. Aligned with Carsten Ziegeler. cc Jaclyn Eckersley, Yanira Castaneda. *"Conrad has delegated a decision on AOv2 to me."* This is the Conrad forcing-function directive memory had been awaiting since Apr 29 ("V2 = direction, discussion not decision"). **Now decided** (Conrad → delegated to Ian → Ian posted + Carsten-aligned = decision signal per [[feedback-proposal-vs-decision]]).

**The decision (verbatim-anchored):**
1. **Skills-first.** Develop skills first; create MCPs only if required by the skills; create agents only where a skill cannot achieve what's required.
2. **Harness-portable.** Aim to run skills in any harness; do not limit to a single harness.
3. **Adoption-gated harness support.** Support the harnesses customers show usage of for AEM agents; invest effort in a harness only where there's proven AEM-agent usage.
4. **Minimal AOv2 investment until proven BU value.** *"Until there is proven value to AEM BU we should not invest more effort than making the AOv1 agent manifests available as is to AOv2."*
5. **A2A dead.** *"We should not invest further in A2A since no customers have leveraged it."*

**Resolves prior open items:**
- Forward-path commitment to AOv2 — was open → now: skills-first, harness-agnostic, AOv2 support adoption-gated (not a blanket bet).
- A2A decommission — was "direction/timeline open" → now: no further A2A investment, confirmed dead.
- MCP-vs-skills tension — resolved toward **skills primary, MCP subordinate** (Trent's Apr 29 skepticism wins over Bertrand's MCP-first).
- The decision-maker question — Conrad delegated to **Ian** (not Trent, who disclaimed authority Apr 29).

**Strategic read for Pedro:** the decision is the architecture floor his blog sits on. "Skills run in any harness" + "support harnesses where customers show usage" = exactly why the selection + consistency layer (his lane) matters: if skills are portable and harnesses are adoption-driven and plural, someone must make the right skill be there-waiting and keep surfaces consistent. Ian's directive validates the premise; Pedro's blog answers the consequence. Cite it that way to Bertrand.

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

