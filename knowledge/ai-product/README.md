# AI Product Management

> PM knowledge specific to building products with or around AI agents, LLMs, and AI-native surfaces. This domain is evolving fast. Every entry should include a date — shelf life is short.

---

> **Structure (P3 split 2026-07-02):** one entry = one file in this folder; this README is the router. Open the entry file; don't try to load the whole folder. New entries: create the file, add a row here.

## Measuring AI Features

| Entry | Gist |
|---|---|
| [Technical Success Rate vs Value Realization Rate — They Are Not the Same](technical-success-rate-vs-value-realization-rate-they-are-not-the-same.md) | Two agents in the same org can report 9% and 75% success rates and both be telling the truth — because they're measuring different things. … |
| [Measure at the Unit of User Intent, Not the Unit of System Event](measure-at-the-unit-of-user-intent-not-the-unit-of-system-event.md) | Value-realization metrics for an agent have to sum to something meaningful (typically 100%) to be interpretable as a distribution. They onl… |
| ["No Results Found" Is a Product Gap in Agentic UX — Not a Legitimate Answer](no-results-found-is-a-product-gap-in-agentic-ux-not-a-legitimate-answe.md) | In classical search UX, "no results found" is a legitimate response — the system searched, nothing matched, the user knows to refine. In ag… |
| [Capability-Level Monthly Usage Is the Value Narrative Metric (BVR)](capability-level-monthly-usage-is-the-value-narrative-metric-bvr.md) | TSR, VR (intent-level), and VRR (tier-based) all answer the same question at different resolutions: *was this interaction valuable?* They o… |
| [Raw Call Volume Is Mostly the Agent Talking to Itself — Classify Before You Headline](raw-call-volume-is-mostly-the-agent-talking-to-itself-classify-before.md) | In MCP/agent traffic the headline count (requests, or even "tool calls") is a vanity number because most of the volume is the agent operati… |
| [VRR Is a Tiered Metric — Collapsing to One Number Misleads](vrr-is-a-tiered-metric-collapsing-to-one-number-misleads.md) | Value Realization Rate is not a binary. In AEM's measurement context, VRR is structured as a 5-tier classification (tiers not yet fully def… |
| [The Open Chat Box as Discovery Mechanism](the-open-chat-box-as-discovery-mechanism.md) | An open-ended chat interface is one of the most effective ways to discover what users actually want from a system. Users express real inten… |
| [Agents Need to Surface Problems, Not Just Solve Them — The "Sensor + Hero" Model](agents-need-to-surface-problems-not-just-solve-them-the-sensor-hero-mo.md) | Agents fail to drive adoption not because they're hard to use, but because users don't know they have a problem worth solving. The leaky pi… |
| [Removing Friction Is Not Enough — Agent Adoption Can Still Fail](removing-friction-is-not-enough-agent-adoption-can-still-fail.md) | Apoorva's Content Optimization Agent simplified rendition creation (no need to know smart crop presets). Adoption is still negligible. DM T… |
| [The Cold Start Problem for AI Agents](the-cold-start-problem-for-ai-agents.md) | Loni's explicit question: "How does a human get the aha moment without even having to invoke any agent?" A feature that requires user initi… |
| [Agent Failure Rate Is Often an Architecture Ceiling, Not a Prompt Quality Problem](agent-failure-rate-is-often-an-architecture-ceiling-not-a-prompt-quali.md) | A 40-50% agent failure rate can look like a prompting problem. It often isn't. If agents route to a solution without reasoning through one,… |
| [AO 2.0 Is Plugin-Based, Following Anthropic Open Protocols](ao-2-0-is-plugin-based-following-anthropic-open-protocols.md) | Agent Orchestrator 2.0 is extensible through plugins using Anthropic's open protocols (same underlying model as MCP). The pattern: install … |
| [Agent Categories Are Often PM Intuition, Not Customer Reality](agent-categories-are-often-pm-intuition-not-customer-reality.md) | Agent categories (Discovery, Governance, Production, etc.) typically emerge from how PMs think about their domain, not from observed custom… |

## Surface Strategy for AI Products

| Entry | Gist |
|---|---|
| [The Human vs Agent Surface Split](the-human-vs-agent-surface-split.md) | AI products need two fundamentally different interaction surfaces: (1) human practitioners who need a guided, visual, discoverable UI; (2) … |
| [Hero Surfaces Strategy](hero-surfaces-strategy.md) | In a product ecosystem with many surfaces, you cannot run effective PLG, measure discovery, or build compounding feature awareness without … |
| [Too Many Surfaces Is a PLG Killer](too-many-surfaces-is-a-plg-killer.md) | Every time a team builds a new surface, they fragment the audience. Users can't form habits with a product they reach through four differen… |

## Distributed-Harness Architecture (AOv2 / Agentic NorthStar)

| Entry | Gist |
|---|---|
| [Everything Is a Skill — the "Agent" Dissolves as a Build Unit](everything-is-a-skill-the-agent-dissolves-as-a-build-unit.md) | Once harness reasoning becomes a commodity (Claude / Codex / Pi SDKs), value moves to skills + unique APIs + memory, and the "agent" stops … |
| [Moat = the Data, Not the Mechanism](moat-the-data-not-the-mechanism.md) | A capability built on open, portable standards (open API / MCP, fork-and-run) appears to conflict with lock-in (*"heartbreaking to leave"*)… |
| [Selection and Cross-Surface Consistency Are a PM Mandate](selection-and-cross-surface-consistency-are-a-pm-mandate.md) | In a distributed-harness model two things become product (PM) problems, not architecture: (1) Selection — which harness/agent a request rou… |
| [Agentic Extensions Have a Token-Cost Hierarchy](agentic-extensions-have-a-token-cost-hierarchy.md) | Every active extension costs tokens every turn, even when its tools are never called — and the cost varies by an order of magnitude: hooks … |
| [The Distributed Front Fragments in Three Ways — Three PM-Owned Fixes](the-distributed-front-fragments-in-three-ways-three-pm-owned-fixes.md) | A distributed-harness model (each team owns its UI + skills + session) buys depth but fragments in three *separate* ways. Conflating them a… |
| [There Waiting Has Two Forms — Consistent Chat or (Often) Invisible](there-waiting-has-two-forms-consistent-chat-or-often-invisible.md) | "There waiting" (the right capability present where the user works) does not mean a chat window on every surface. The form follows the surf… |
| [The Theses Held — Push the Function, Not the Abstraction; Hold the Surface Loose](the-theses-held-push-the-function-not-the-abstraction-hold-the-surface.md) | Both theses are alive and being arrived at independently by others, which is the signal that separates a held position from stubbornness. (… |
| [A Single-Harness Marketplace Is Not a Cross-Harness Standard — Publish vs Find](a-single-harness-marketplace-is-not-a-cross-harness-standard-publish-v.md) | A per-harness plugin marketplace solves *supply within one harness* and nothing above it. AOv2's model is concretely git-native and local-c… |
| [A Rendering Contract Carries Structure, Not Skin — the Brand Travels Only Where You Own the Renderer](a-rendering-contract-carries-structure-not-skin-the-brand-travels-only.md) | An open rendering contract makes the structure/semantics of the UI portable (this is an asset card, these fields, these actions). It does n… |
| [Three-Layer AI Skill Governance Architecture (Customer-Side)](three-layer-ai-skill-governance-architecture-customer-side.md) | In an enterprise AI product where hundreds of skills could be loaded, *who sees and uses which skills* decomposes into three nested, non-co… |
| [Dynamic Workflows — the Orchestrator Moves Off the Model (Code Coordinates, the Model Judges)](dynamic-workflows-the-orchestrator-moves-off-the-model-code-coordinate.md) | A *dynamic workflow* is a short JavaScript program Claude writes on the fly to coordinate a fleet of subagents. The model does the judgment… |

## Agent Measurement Infrastructure

| Entry | Gist |
|---|---|
| [The Mandatory + Custom Dashboard Pattern](the-mandatory-custom-dashboard-pattern.md) | Cross-agent measurement works when there is a shared mandatory baseline (same metrics, same definitions, same format across all agents) plu… |
| [Two-Track Reporting Infrastructure — Fast Iteration vs Stable Foundation](two-track-reporting-infrastructure-fast-iteration-vs-stable-foundation.md) | When building measurement infrastructure for an AI product, two tracks often need to run in parallel: (1) a fast-iteration track (manual, P… |
| ["Do Customers Come Back?" Is the Primary Value Signal for AI Agents](do-customers-come-back-is-the-primary-value-signal-for-ai-agents.md) | The most honest single signal for whether an AI agent is delivering value is whether users return. Not whether it completed the task, not w… |
| [Grafana vs LangFuse — Two Different Measurement Jobs](grafana-vs-langfuse-two-different-measurement-jobs.md) | These tools answer different questions and should not be conflated. |
| [Prompt Library Monitoring as Early Adoption Signal](prompt-library-monitoring-as-early-adoption-signal.md) | Daily monitoring of which prompts are actually being triggered is one of the earliest adoption signals available. It tells you what users a… |
| [Two-Frontend Antipattern — Never Run Two Competing UI Surfaces in Parallel](two-frontend-antipattern-never-run-two-competing-ui-surfaces-in-parall.md) | When a product team maintains two active front-end surfaces for the same capability, every downstream consequence is worse than making eith… |
| [Success Definitions Must Be Agreed Before Metrics Are Scaled](success-definitions-must-be-agreed-before-metrics-are-scaled.md) | Scaling a measurement dashboard before success definitions are aligned across teams creates a false picture. Each agent team may define "te… |
| [Failure Taxonomy Needs an Explicit Quality vs Gap Split](failure-taxonomy-needs-an-explicit-quality-vs-gap-split.md) | When presenting agent failure data to senior stakeholders, mixing quality failures (agent tried, something broke) with capability gaps (age… |
| [Product Gap vs Quality — The Plain-Language Definition for Stakeholders](product-gap-vs-quality-the-plain-language-definition-for-stakeholders.md) | When communicating the PM section of agent reports to a broad stakeholder audience (including non-technical), the Quality/Gap split needs p… |
| [Thread Context Changes What a Product Gap Means](thread-context-changes-what-a-product-gap-means.md) | A product gap row in an agent report has different meaning depending on what came before it. A user hitting "I can't do that" after one col… |
| [Metric Definition Ownership — PM Validates, Reporting Track Owner Implements](metric-definition-ownership-pm-validates-reporting-track-owner-impleme.md) | Defining an agent-specific metric has two distinct ownership questions. (1) Does the definition match the capability? — a question the agen… |
| [Two-Validator Pattern for Report Rollout](two-validator-pattern-for-report-rollout.md) | When an agent report is prepared by someone other than the PM owner (e.g. Jim prepares for Corey), two separate validation roles exist: (1)… |
| [External Dependency Framing in H2 Planning](external-dependency-framing-in-h2-planning.md) | When agents are embedded across team roadmaps (not a standalone team), leadership doesn't create a dedicated agents slide. Instead, Bertran… |
| [Report-to-Backlog Pipeline — Auto-Generating Stories from Structured Report Output](report-to-backlog-pipeline-auto-generating-stories-from-structured-rep.md) | Product gap data in an agent report is only useful if it reaches the teams who can act on it. Manually filing JIRA stories from report obse… |
| [Connecting Failure Data to Engineering Tracking (JIRA Column)](connecting-failure-data-to-engineering-tracking-jira-column.md) | A failure report that doesn't say whether the failure is already tracked is incomplete for an engineering stakeholder. Bertrand's ask: add … |
| [Report Infrastructure Needs a Stable Home Before Broader Distribution](report-infrastructure-needs-a-stable-home-before-broader-distribution.md) | When a senior stakeholder sees useful data for the first time, their first instinct is not to consume it — it's to ask where it lives perma… |
| [Auth-Walled Hosting Is Incompatible with Agent-Consumable Reports](auth-walled-hosting-is-incompatible-with-agent-consumable-reports.md) | When a senior stakeholder says "agents should be able to consume this data," they are describing a technical constraint on hosting. Auth-wa… |
| [Adding a New Agent to a Measurement Pipeline Is a Data Problem, Not an Engineering Problem](adding-a-new-agent-to-a-measurement-pipeline-is-a-data-problem-not-an.md) | Once a measurement platform exists with a defined schema, onboarding a new agent is about getting the right data in the right format — not … |

## AI Product Risks

| Entry | Gist |
|---|---|
| [The Vision-Reality Gap in AI Products](the-vision-reality-gap-in-ai-products.md) | AI products are particularly prone to vision-reality gaps because demo environments are easy to curate and real usage exposes fundamental a… |
| [Overstating Agent Readiness at Scale](overstating-agent-readiness-at-scale.md) | An agent that works in a contained demo environment may fail at enterprise scale. Large codebases, complex configurations, and unusual edge… |
| [Adoption Cadence as a PLG Instrument — The "Netflix Effect"](adoption-cadence-as-a-plg-instrument-the-netflix-effect.md) | A regular adoption review meeting that shows real usage data can become a high-engagement ritual — Shankari's EH adoption reviews had peopl… |
| [PLG Checkbox Antipattern — Announcement Without Ownership](plg-checkbox-antipattern-announcement-without-ownership.md) | In a product with a shared surface (like Experience Hub), teams will request real estate for PLG announcements and then disappear. They add… |
| [Personalization in AI Products — Start Small or Not at All](personalization-in-ai-products-start-small-or-not-at-all.md) | Enterprise personalization infrastructure is almost always more complex than it looks. The DX-level profile at Adobe requires integrating w… |
| [Skills vs Prompts — A Fundamental Interaction Model Distinction](skills-vs-prompts-a-fundamental-interaction-model-distinction.md) | Prompts and skills are not the same thing, and surfacing them interchangeably in an AI product surface is a structural mistake. |
| [Cross-Region Data Aggregation Is a Compliance Risk in AI Measurement](cross-region-data-aggregation-is-a-compliance-risk-in-ai-measurement.md) | AI agent interaction data is collected per region (in AEM: VA, NLD2, AUS5, CAN2, GBRS, IND1). Re-aggregating that data across regions for a… |
| [Confirm Ownership Before Acting — Research First, Assume Nothing](confirm-ownership-before-acting-research-first-assume-nothing.md) | In cross-functional AI programs, PM ownership chains are rarely clean. Adjacent PMs often don't know who owns what. Pedro's situation: he w… |
| [Regional Failure Concentration Is a Diagnostic Signal](regional-failure-concentration-is-a-diagnostic-signal.md) | When failure rate data is available by region, look for concentration before averaging. NLD2 showing a 46% failure rate while overall rates… |
| [Anonymization Does Not Fix Data Residency — Ian Boston's "Stolen Data" Framing](anonymization-does-not-fix-data-residency-ian-boston-s-stolen-data-fra.md) | Anonymization is often suggested as a fix for data compliance in AI measurement pipelines. It is not. As long as a prompt is readable, it r… |
| [Early MCP Adoption Is Developer-Tool-Led, Not AI-Assistant-Led](early-mcp-adoption-is-developer-tool-led-not-ai-assistant-led.md) | In the current phase of MCP adoption for AEM, developer tools (Cursor IDE) generate 30x more identified invocations than AI assistants (Cla… |
| [Monetization Is Unresolved When Agents Replace Seats](monetization-is-unresolved-when-agents-replace-seats.md) | Traditional seat-based SaaS pricing breaks when agents replace human users. If one agent does the work of ten humans, and you charge per se… |
| [Personalized Prompt Pipeline Architecture — Signal Blending Model](personalized-prompt-pipeline-architecture-signal-blending-model.md) | A real-world personalized prompt recommendation system for an enterprise AI product runs on three layers of signal, dynamically blended. In… |
| [Tag Taxonomy Design for AI Agent Measurement](tag-taxonomy-design-for-ai-agent-measurement.md) | Tag taxonomies for AI agent measurement fail in predictable ways. The common failure modes, and their fixes: |
| [Auth-Walled Hosting Blocks PM Validation Workflows, Not Just Agent Consumption](auth-walled-hosting-blocks-pm-validation-workflows-not-just-agent-cons.md) | Date identified: 2026-04-08 |

## Personalization Architecture for AI Surfaces

| Entry | Gist |
|---|---|
| [Cascading Signal Model — User → Org → Global Fallback Solves Sparse Data](cascading-signal-model-user-org-global-fallback-solves-sparse-data.md) | Personalization systems for AI surfaces fail most often not on the algorithm but on the data. Most users don't have enough individual histo… |
| [Two-Column Prompt Design — Display Label + Execution Prompt](two-column-prompt-design-display-label-execution-prompt.md) | Suggested prompts have a fundamental UX conflict: prompts that work well with an AI tend to be long and verbose (context, constraints, outp… |
| [Prompt Library as Contribution Surface — Centralized Library, Distributed Ownership](prompt-library-as-contribution-surface-centralized-library-distributed.md) | In an ecosystem with many AI agents and many surfaces, the prompt library should be treated as a shared contribution surface — one centrali… |
| [User Feedback as Ranking Signal — ✓/✗ to Densify Sparse Personalization](user-feedback-as-ranking-signal-to-densify-sparse-personalization.md) | When the user-level signal is sparse (the cascade's primary problem), an explicit feedback UI can densify it cheaply. A per-recommendation … |
