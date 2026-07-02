# Knowledge Index

> Router for the PM knowledge system. Read this first to find what you need.

## Folder Inventory

> Entry counts are not tracked here — they drift and earn nothing. For a live count: split folders (`leadership/`, `ai-product/`, `patterns/` — one entry = one file, README = router) → `ls <folder> | wc -l`; single-file folders → grep its headers.
>
> **Split rule (P3, 2026-07-02):** in split folders, read the router README then open only the entry files you need — never bulk-load the folder. A single-file folder gets split the same way when it crosses ~20K tokens.

| Folder | Purpose |
|--------|---------|
| `domain/` | Core PM knowledge: discovery, strategy, personas, market signals |
| `patterns/` | Recurring PM frameworks, decision patterns, templates |
| `hypotheses/active.md` | Hypotheses currently being tested |
| `hypotheses/resolved.md` | Confirmed or killed hypotheses with evidence |
| `false-beliefs/` | PM conventional wisdom proven wrong |
| `tools/` | Decision matrix: when to use which PM method/tool |
| `experiments/` | RETIRED 2026-07-02 — experiment-shaped material routes to `hypotheses/` (log.md kept as tombstone) |
| `leadership/` | Senior Director operating patterns: cross-org influence, strategic narrative, stakeholder gravity |
| `interpersonal/` | One-on-one relationship dynamics: reading people, political types, managing up/lateral/down, trust, conflict, adversaries |
| `ai-product/` | PM knowledge for AI-native products: measurement, surface strategy, failure modes, agent dynamics |

## Sources Ingested

| Source | Date | Type | Key Contributions |
|--------|------|------|-------------------|
| Greene, *The 48 Laws of Power* | 2026-04-02 | Book | Reputation as infrastructure, never outshine the master, absence increases value, managing envy as visibility rises, stop at the goal, formlessness as career strategy, self-interest as persuasion key, reform gradually, isolate key blockers, hearts before arguments, false beliefs about transparency/verbosity/availability/timidity |
| McIntyre, *Organizational Politics* | 2026-04-02 | Book | Four political types, recognizing supporters/adversaries, dealing with annoyances vs adversaries, toxic workplace signals, political suicide patterns (emotion hazards, victim framing, bridge burning), position vs personal power, managing up/laterally/down, Four P's of political success, visible results, Power Grid mapping, Political Game Plan |
| Greene, *The Art of Seduction* | 2026-04-02 | Book | Attention redirection, mirroring, strategic withdrawal, charisma components, soft sell, anti-seducer audit, myth over logic, purpose creates followership, reading people vs stated preferences |
| Greene, *The 33 Strategies of War* | 2026-04-02 | Book | Strategic positioning, polarity strategy, grand strategy, coalition-building, alliance strategy, negotiation while advancing, counterattack strategy, presence of mind, exit strategy, false beliefs about consensus/retreat/first-mover |
| Gallo, *Presentation Secrets of Steve Jobs* | 2026-03-19 | Book | Communication frameworks, presentation patterns, false beliefs about presenting, stakeholder management techniques |
| Lafley & Martin, *Playing to Win* | 2026-04-02 / 2026-05-04 | Book (Bookey summary 106pp full) | Strategy Choice Cascade (5 questions), winning aspiration vs participation trap, where to play as exclusion choice, cost leadership vs differentiation, activity systems as capabilities, management systems as strategy reinforcement, playing not to lose as dangerous false belief. **Full ingest 2026-05-04 added:** Strategy Logic Flow four dimensions (Industry / Customers / Relative Position / Competition), Reverse-Engineering "What Would Have to Be True?" 7-step process, Six Strategy Traps (do-it-all, Don Quixote, Waterloo, something-for-everyone, dreams that never come true, program-of-the-month), Six Telltale Signs of Winning Strategy (distinct activity system, loyal customers, profitable competitors, resource superiority, competitors attacking each other, first choice for innovation), Outside Strategy Partner pattern, Marketing Myopia trap (FB-028), narrow competitor set false belief (FB-029), OGSM as cascade operationalization, assertive inquiry vs corporate theater. |
| AEM Experience Hub — Loni Working Sessions I & IV | 2026-03-23 / 2026-03-26 | Live strategy sessions | Hero surfaces concept, agent measurement gaps, TSR vs VRR, architecture ceiling insight, cross-org influence patterns, durable themes |
| Shankari 1:1 handoff | 2026-03-27 | PM handoff conversation | Adoption cadence as PLG instrument, PLG checkbox antipattern, governance posture as leadership signal, personalization experiment approach, EH North Star vision |
| Bertrand W13 report exchange + gap re-analysis | 2026-03-30 / 2026-03-31 | Email exchange with Sr Director + artifact audit | Failure taxonomy quality vs gap split, JIRA tracking column pattern, stable hosting before broad distribution, trends in consolidated view, auth-walled hosting incompatible with agent consumption, parallel artifact stream divergence |
| Bertrand 1:1 + Agent Owner Alignment March 20 + Pedro voice notes | 2026-03-31 | 1:1 notes, meeting transcript, voice memos | VRR is a tiered metric not a scalar, skills vs prompts interaction model distinction, cross-region data aggregation compliance risk, contribution model with quality gate pattern, TTL+priority+role-linking card system |
| Eugene Bannykh Slack + personalization tension with Bertrand | 2026-03-31 | Slack conversation + stakeholder alignment | Pilot via existing feature not new build, identify scaling constraint before committing to model, reframe deprioritized item as mechanism for agreed priority |
| Yanira 1:1 + Sorin 1:1 (March 19) | 2026-03-30 | Meeting notes | Two-track reporting infra pattern, success definitions before scaling metrics, DAS team context, custom widget framework, personalization OKR history |
| Felix Delval 1:1 + aem-agent-reports repo analysis | 2026-03-25 | Technical deep dive | Mandatory + custom dashboard pattern, agent onboarding as data problem, measurement infrastructure design |
| EPA vs EGA cross-analysis | 2026-03-24 | Internal report analysis | Success metric definition divergence, why cross-agent comparison fails without shared definition |
| H2 Prelim In/Out Priorities Part 3 | 2026-04-10 | Live strategy session (Loni + Apoorva + Shankari) | Sensor+hero adoption model, trigger vs friction failure, cold start problem, Content Optimization Agent adoption analysis, DM Templates failure pattern, two-frontend antipattern, Loni first-principles research protocol |
| Agent Owner Alignment March 16 + March 23 + State of Project (cross-synthesis) | 2026-04-10 | Cross-file synthesis | Repeating users = primary value signal; Grafana vs LangFuse; Apoorva daily prompt monitoring; prompt library ownership per agent team |
| Fu-Chi + Eugene personalization sync | 2026-04-20 | 1:1 meeting transcript | Cascading signal model (user→org→global), two-column prompt design (display label + execution prompt), prompt library as contribution surface, ✓/✗ feedback as ranking signal for sparse data |
| P42 Status meeting (Jaclyn + Yanira + Pedro) | 2026-04-21 | Live meeting transcript | Claude projects as queryable exec artifacts (AI-native VP prep), portfolio investment framing for agent HC (20% allocation model), light warm-up before a big-ticket meeting (week-before touchpoint pattern). Confirmed AO 2.0 session + Loni/JM timing, identified $500K P42 cost signal, profitability + HC asks |
| Varun Kalra (Apoorva's team) Discovery Agent report sync | 2026-04-22 | 58min live meeting transcript | Intent-level measurement unit for agent UX metrics, "no results found" as product gap (not legitimate answer), differentiation as diagnostic requirement (single bucket hiding multiple root causes breaks triage), voluntary consolidation signals platform legitimacy (Varun consolidating his wiki into Pedro's platform) |
| Priority recalibration + vault alignment pass | 2026-04-24 | Working session (no external meeting) | Overwhelm as calibration signal (not capacity), do-not-respond-to-overwhelm-by-adding, roll-up vs task tracker (one authoritative home per piece of info), calibration audit (when a priority symbol stops signaling) |
| H2 2026 Planning + HC Rollup analysis | 2026-04-28 | H2 source canvas + JIRA MCP fetches | Dual-Track Source Tracking (Slack Parent vs JIRA Parent), Narrative Claim vs Canonical Truth (Pedro-promoted status pattern), confirmation that AEM Agentic Web initiative spans multiple parent initiatives (DX-1220 Agentic Web, DX-1222 Product Adoption), gap mapping shows half of Pedro's 6-agent reporting taxonomy isn't directly funded in H2 |
| Jiang Xueqin — *The Only Wealth Game That Works* (video) | 2026-06-02 | YouTube essay, routed as career mental model | **Position-over-merit frame** (the foundational career-game frame) — FB-031 (meritocracy-at-work false belief), leadership/ "The Game Itself — Position Over Merit" (5 rules: create a lane / control what counts as value / write the framework / proximity to deciders / position compounds). Keep the diagnosis, drop the wealth fatalism. Pedro's standing "return to it always" instruction → `feedback_position_over_merit` memory. |
| Huryn, *Claude Dynamic Workflows for PMs: The Ultimate Guide* (The Product Compass) | 2026-06-07 | Newsletter (PM-AI technique), routed to ai-product/ | **Dynamic workflows — the orchestrator moves off the model into code** (model judges, code coordinates; 113 agents / 1.95M tokens / zero orchestration tokens). The 3 failure modes a code-harness fixes (agentic laziness / self-preferential bias / goal drift); subagent-vs-workflow test (one round of parallel judgment vs chained stages); six patterns (classify / fan-out-synthesize / adversarial-verify / generate-filter / tournament / loop-until-done); guardrail = the toolset not a prompt (read-only ≠ can't-touch-disk). PM read: which weekly jobs become standing workflows (skill + schedule + /goal + budget). Repo `github.com/phuryn/dynamic-workflows-experiment`. → ai-product/ "Dynamic Workflows — the Orchestrator Moves Off the Model". |
| Dunlop, *Amazon's Secret Weapon: One-Door vs Two-Door Decision Framework* (Cub Think Tank) | 2026-06-18 | Article (Bezos 2015 letter), routed to patterns/ | **One-way vs two-way doors** — irreversible (slow, methodical, consult) vs reversible (fast, high-judgment individual, iterate); classify before sizing the process. Real lever = the error asymmetry (almost no one over-deliberates one-way; the waste is treating two-way as one-way → "death by a thousand cuts") so empower more fast two-way calls. Pedro read: classifying out loud is the visible Director→SD move; inversion ("which open items am I treating as one-way?"); maps to overwhelm/red-tag triage + P42 "only Anil can stop-AIA". Three extensions the frame misses (nearly-irreversible seam / one-way-by-accumulation / political≠technical reversibility). → patterns/ "One-Way vs Two-Way Doors". |
| Coworker thread (PM) + renderer ADR read | 2026-06-19 | Live Slack threads + ADR (consolidation #2) | ai-product/ +3 refinements (no new entries): **meta-harness taxonomy** (harness=SDK loop / meta-harness=Coworker-AMA runs harnesses / manifest defines the harness; locates non-runtime skill-selection at the manifest = PM-ownable); **adoption-earned-not-mandated** (Ian: a forced-Coworker DACI fails; own the portable layer, not the blessed standard); **ADR 001 corroboration** (SVG-via-data-URI = preferred + only path that travels; custom client renderers invisible outside coworker → brand travels via server-SVG = the structure-vs-skin mechanism; ADR rejected per-team packages for shared-repo PRs). H-007 +afternoon reactive engagement (all prep/held, still 0 cold). |
| Coworker session aftermath — Ian/Felix thread + AIP harness disclosure | 2026-06-19 | Live Slack threads (consolidation) | ai-product/ +2 refinements (no new entries): "Publish vs Find" gains the **4-layer skill-selection model** (SDK solves runtime only; surface/governance/discovery stay PM-ownable — Ian "solved by SDKs" + Manas "open at scale"); "The Theses Held" gains the **AIP/AUP all-Adobe harness corroboration** (a 2nd harness provably exists + diverging → substrate is the hedge). H-007 +5th reactive rep (still all prep-iterated, 0 cold). |
| Greene, *How to Make People Fear Disrespecting You* (video) | 2026-06-02 | YouTube, routed as leadership presence | **Respect-with-a-line as a position lever** (aimed at Pedro's over-accommodating gap) — leadership/ "A Touch of Fear and the Use of Leverage" (use leverage when you hold it; a *touch* of fear beats pure likeability, but a reign of fear kills truth-telling); FB-032 ("being agreeable and well-liked is the safe path up"). Honest translation: boundaries + consequences, never intimidation. Anti-pattern = retracting a position under public pressure (Philippe). Overlaps prior Greene ingests (48 Laws / Art of Seduction / 33 Strategies, 2026-04-02) — only the net-new fear/leverage calibration was added. |

## Routing Table

| You're doing... | Read first | Then check |
|-----------------|-----------|------------|
| User research / interviews | `domain/` | `hypotheses/active.md`, `patterns/` |
| Competitive analysis | `domain/` | `false-beliefs/`, `patterns/` |
| Choosing a method/framework | `tools/decision-matrix.md` | `patterns/` |
| Strategy / roadmap work | `patterns/` (Strategy Cascade) | `domain/` (Product Strategy section), `tools/` (Strategy Choice Cascade), `false-beliefs/` (FB-023, FB-024) |
| Communicating strategy upward | `leadership/` (Communicating Strategy Upward) | `tools/` (Strategy Choice Cascade), `domain/` (Product Strategy) |
| Challenging assumptions | `false-beliefs/` | `hypotheses/resolved.md` |
| Learning from new material | Route by content type to relevant folders | |
| Pattern recognition | `patterns/` | `hypotheses/active.md` |
| Preparing a presentation | `tools/` (Headline, Rule of Three, PSE) | `patterns/` (Nine Elements, Holy Shit Moment) |
| Stakeholder communication | `domain/` (Stakeholder Management) | `tools/` (Bucket Method, Elevator Pitch) |
| Reading a specific person | `interpersonal/` | `leadership/` |
| Managing up (Bertrand, Loni) | `interpersonal/` (Managing Up) | `leadership/` |
| Managing laterally (peers, cross-org) | `interpersonal/` (Managing Laterally) | `leadership/` (Cross-Org Influence) |
| Dealing with an adversary or difficult person | `interpersonal/` (Conflict and Adversaries) | `false-beliefs/` |
| Building trust with a new team or stakeholder | `interpersonal/` (Building Trust) | `patterns/` |
| Senior Director visibility | `leadership/` | `hypotheses/active.md` (H-007), `hypotheses/resolved.md` (H-003 promoted) |
| Cross-org influence | `leadership/` (Cross-Org Influence Without Authority) | `interpersonal/`, `patterns/` (Capacity-Ask Mismatch) |
| AI product / agent work | `ai-product/` | `false-beliefs/` (FB-006, FB-007, FB-008) |
| Agent measurement | `ai-product/` (Measurement section) | `hypotheses/resolved.md` (H-005) |
| Surface strategy | `ai-product/` (Surface Strategy section) | `leadership/` (Pick Up the Open Action Item) |
| Roadmap under uncertainty | `leadership/` (Durable Themes) | `ai-product/` (Architecture Ceiling) |

## Access Log — retired 2026-07-02

Access history lives in `git log` over `knowledge/` (commit prefixes show what moved and why).
The old append-only log (2026-03-19 → 2026-07-01) is preserved verbatim in `ACCESS_LOG_ARCHIVE.md` — grep it, never full-Read.
