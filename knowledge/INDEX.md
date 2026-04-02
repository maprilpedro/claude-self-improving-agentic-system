# Knowledge Index

> Router for the PM knowledge system. Read this first to find what you need.

## Folder Inventory

| Folder | Purpose | Status | Entries |
|--------|---------|--------|---------|
| `domain/` | Core PM knowledge: discovery, strategy, personas, market signals | Active | 19 |
| `patterns/` | Recurring PM frameworks, decision patterns, templates | Active | 28 |
| `hypotheses/active.md` | Hypotheses currently being tested | Active | 5 |
| `hypotheses/resolved.md` | Confirmed or killed hypotheses with evidence | Empty | 0 |
| `false-beliefs/` | PM conventional wisdom proven wrong | Active | 14 |
| `tools/` | Decision matrix: when to use which PM method/tool | Active | 6 |
| `experiments/` | Experiment tracking and results | Active | 1 |
| `leadership/` | Senior Director operating patterns: cross-org influence, strategic narrative, stakeholder gravity | Active | 28 |
| `interpersonal/` | One-on-one relationship dynamics: reading people, political types, managing up/lateral/down, trust, conflict, adversaries | Active | 0 |
| `ai-product/` | PM knowledge for AI-native products: measurement, surface strategy, failure modes, agent dynamics | Active | 23 |

## Sources Ingested

| Source | Date | Type | Key Contributions |
|--------|------|------|-------------------|
| Greene, *The Art of Seduction* | 2026-04-02 | Book | Attention redirection, mirroring, strategic withdrawal, charisma components, soft sell, anti-seducer audit, myth over logic, purpose creates followership, reading people vs stated preferences |
| Greene, *The 33 Strategies of War* | 2026-04-02 | Book | Strategic positioning, polarity strategy, grand strategy, coalition-building, alliance strategy, negotiation while advancing, counterattack strategy, presence of mind, exit strategy, false beliefs about consensus/retreat/first-mover |
| Gallo, *Presentation Secrets of Steve Jobs* | 2026-03-19 | Book | Communication frameworks, presentation patterns, false beliefs about presenting, stakeholder management techniques |
| AEM Experience Hub — Loni Working Sessions I & IV | 2026-03-23 / 2026-03-26 | Live strategy sessions | Hero surfaces concept, agent measurement gaps, TSR vs VRR, architecture ceiling insight, cross-org influence patterns, durable themes |
| Shankari 1:1 handoff | 2026-03-27 | PM handoff conversation | Adoption cadence as PLG instrument, PLG checkbox antipattern, governance posture as leadership signal, personalization experiment approach, EH North Star vision |
| Bertrand W13 report exchange + gap re-analysis | 2026-03-30 / 2026-03-31 | Email exchange with Sr Director + artifact audit | Failure taxonomy quality vs gap split, JIRA tracking column pattern, stable hosting before broad distribution, trends in consolidated view, auth-walled hosting incompatible with agent consumption, parallel artifact stream divergence |
| Bertrand 1:1 + Agent Owner Alignment March 20 + Pedro voice notes | 2026-03-31 | 1:1 notes, meeting transcript, voice memos | VRR is a tiered metric not a scalar, skills vs prompts interaction model distinction, cross-region data aggregation compliance risk, contribution model with quality gate pattern, TTL+priority+role-linking card system |
| Eugene Bannykh Slack + personalization tension with Bertrand | 2026-03-31 | Slack conversation + stakeholder alignment | Pilot via existing feature not new build, identify scaling constraint before committing to model, reframe deprioritized item as mechanism for agreed priority |
| Yanira 1:1 + Sorin 1:1 (March 19) | 2026-03-30 | Meeting notes | Two-track reporting infra pattern, success definitions before scaling metrics, DAS team context, custom widget framework, personalization OKR history |
| Felix Delval 1:1 + aem-agent-reports repo analysis | 2026-03-25 | Technical deep dive | Mandatory + custom dashboard pattern, agent onboarding as data problem, measurement infrastructure design |
| EPA vs EGA cross-analysis | 2026-03-24 | Internal report analysis | Success metric definition divergence, why cross-agent comparison fails without shared definition |

## Routing Table

| You're doing... | Read first | Then check |
|-----------------|-----------|------------|
| User research / interviews | `domain/` | `hypotheses/active.md`, `patterns/` |
| Competitive analysis | `domain/` | `false-beliefs/`, `patterns/` |
| Choosing a method/framework | `tools/decision-matrix.md` | `patterns/` |
| Designing an experiment | `experiments/log.md` | `hypotheses/active.md` |
| Strategy / roadmap work | `patterns/` | `domain/`, `tools/` |
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
| Senior Director visibility | `leadership/` | `hypotheses/active.md` (H-003, H-005) |
| Cross-org influence | `leadership/` (Cross-Org Influence Without Authority) | `interpersonal/`, `patterns/` (Capacity-Ask Mismatch) |
| AI product / agent work | `ai-product/` | `false-beliefs/` (FB-006, FB-007, FB-008) |
| Agent measurement | `ai-product/` (Measurement section) | `hypotheses/active.md` (H-005) |
| Surface strategy | `ai-product/` (Surface Strategy section) | `leadership/` (Pick Up the Open Action Item) |
| Roadmap under uncertainty | `leadership/` (Durable Themes) | `ai-product/` (Architecture Ceiling) |

## Access Log

<!-- Claude updates this after each knowledge access -->
| Date | Folders Accessed | Task |
|------|-----------------|------|
| 2026-03-19 | all | System initialization |
| 2026-03-19 | all | Book ingestion: Presentation Secrets of Steve Jobs |
| 2026-03-26 | leadership/, ai-product/, patterns/, false-beliefs/, hypotheses/ | Session IV analysis, Experience Hub week 1 learnings |
| 2026-03-27 | leadership/, ai-product/ | Shankari 1:1 handoff analysis — PLG governance, adoption cadence, personalization, EH North Star |
| 2026-03-30 | ai-product/, patterns/ | Bertrand W13 report exchange — failure taxonomy, JIRA column, hosting pattern |
| 2026-03-30 | ai-product/ | Yanira 1:1 + Sorin 1:1 — two-track infra, success definitions, DAS team, personalization OKR |
| 2026-03-31 | ai-product/, patterns/ | Memory consolidation + learning reflection — auth-walled hosting incompatible with agent consumption, parallel artifact stream divergence pattern |
| 2026-03-31 | ai-product/, patterns/, hypotheses/ | Session wrap — skills vs prompts, VRR tiered metric, cross-region compliance risk, contribution model pattern, TTL card system, H-005 VRR complication |
| 2026-03-31 | leadership/, patterns/ | Final consolidation — reframe deprioritized as mechanism, pilot via existing feature, identify scaling constraint before committing to model |
| 2026-04-01 | ai-product/, leadership/, patterns/ | Full-day EH session — ownership research before acting, regional failure concentration as signal, surface risk before leadership asks, two-consumer platform root cause pattern, fast track as spec for foundation, nominal vs real capacity, precise question gets precise compliance answer |
| 2026-04-01 | ai-product/, leadership/, patterns/ | EH afternoon — anonymization doesn't fix residency (Ian's stolen data framing), fix it quietly before legal, preview link pattern for summit demos, hard deadlines force scope clarity |
| 2026-04-01 | ai-product/ | Report-to-backlog pipeline trial — auto-generating JIRA stories from HTML report output, epic-per-agent triage structure, agent-owner-epic mapping |
| 2026-04-02 | patterns/ | PM as gating layer in automated pipelines — manual trigger as trust-building step, Slack as lightweight gate, trust ladder model |
| 2026-04-02 | ai-product/, patterns/ | MCP early adoption is developer-tool-led (Cursor 15.6% vs Claude 0.5%); explicit sequence as protection against spread |
| 2026-04-02 | domain/ | Bertrand metric framing — adoption metrics should be ratios vs baseline (MCP edits vs CM UI edits), not absolutes |
| 2026-04-02 | leadership/, patterns/, false-beliefs/, domain/ | 33 Strategies of War ingestion — strategic positioning (polarity, grand strategy, intelligence), coalition patterns, false beliefs about consensus/retreat/first-mover advantage |
| 2026-04-02 | leadership/, patterns/, false-beliefs/, domain/ | Art of Seduction ingestion — attention redirection, mirroring, charisma components, soft sell, anti-seducer audit, purpose creates followership, myth over logic, FB-013 directness, FB-014 charisma |
