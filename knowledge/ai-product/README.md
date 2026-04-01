# AI Product Management

> PM knowledge specific to building products with or around AI agents, LLMs, and AI-native surfaces. This domain is evolving fast. Every entry should include a date — shelf life is short.

---

## Measuring AI Features

### Technical Success Rate vs Value Realization Rate — They Are Not the Same
- **Date identified**: 2026-03-24
- **Source**: EPA vs EGA report cross-analysis; Felix Delval's measurement infrastructure; Bertrand 1:1 March 24; Conrad/Gilles Slack March 24.
- **Insight**: Two agents in the same org can report 9% and 75% success rates and both be telling the truth — because they're measuring different things. EPA measures whether a user accepted a proposed content change (behavioral, hard bar). EGA measures whether the agent returned non-empty content (content signal, lower bar). These numbers are not comparable without context. Cross-agent comparison without a shared definition of success creates a false picture.
- **TSR (Technical Success Rate)**: Did the agent complete the requested action without an error? Binary. Easy to compute. Low bar. Tells you the system worked. Doesn't tell you if it was useful.
- **VRR (Value Realization Rate)**: Did the user actually get value? Higher bar. Requires behavioral signal (user accepted, acted on, returned to use again). Harder to define and measure. The metric that matters to customers and leadership.
- **Application**: Any cross-agent measurement standard must agree on TSR and VRR definitions before publishing numbers. Without this, comparing agents misleads everyone, including the agents' own teams.

### VRR Is a Tiered Metric — Collapsing to One Number Misleads
- **Date identified**: 2026-03-31
- **Source**: Bertrand de Coatpont, 1:1 March 31, 2026.
- **Insight**: Value Realization Rate is not a binary. In AEM's measurement context, VRR is structured as a 5-tier classification (tiers not yet fully defined as of March 31 — Yanira's wiki holds the definition). Collapsing a tiered distribution into a single aggregated percentage hides the shape of the data. If 80% of interactions are tier-1 (minimal value) and 5% are tier-5 (high value), the average number could read as "good" while the distribution is actually poor.
- **Consequence**: Every VRR number reported as a single figure before the tier definitions are applied is potentially misleading. Cross-agent VRR comparison with a single number is especially dangerous — the tiers may be defined differently per agent.
- **Fix**: Get the 5-tier definition (from Yanira's success definition wiki). Report VRR as a distribution, not a single percentage. Aggregate only within a tier or across comparable tiers.
- **Application**: Any AI product measuring "user value" should ask: is this a scalar or a distribution? Before presenting a single VRR number to leadership, verify you know what it's averaging over.

### The Open Chat Box as Discovery Mechanism
- **Date identified**: 2026-03-26
- **Source**: Corey Dulimba in Loni's Session IV (Surfaces, March 26).
- **Insight**: An open-ended chat interface is one of the most effective ways to discover what users actually want from a system. Users express real intent in natural language before they know whether the feature exists. The open box discovers needs that no survey or interview would surface — because users don't know to ask for them.
- **The tension**: The same open box generates frustration when the agent can't do what the user just asked. Hallucinated links, out-of-scope responses, and unclear failure modes erode trust quickly.
- **Right response**: Don't close the box. Improve the failure behavior. Be explicit about what the agent cannot do. "I can't help with that yet, but here's what I can do" is far better than a hallucinated answer.
- **Application**: Treat the open chat box as a qualitative research instrument. Log and analyze what users ask for. The things the agent can't answer are your next roadmap inputs.

### Agent Failure Rate Is Often an Architecture Ceiling, Not a Prompt Quality Problem
- **Date identified**: 2026-03-23
- **Source**: Loni's AEM PM Virtual Working Session I (Agents, March 23). Cedric Huesler confirmed.
- **Insight**: A 40-50% agent failure rate can look like a prompting problem. It often isn't. If agents route to a solution without reasoning through one, there is a structural ceiling on quality that no amount of prompt tuning will raise. In AEM, the current architecture routes — it doesn't reason. AO 2.0 adds agent loop reasoning. Until it lands, the failure rate has a floor.
- **Why it matters for PMs**: If you frame a quality problem as a prompting problem, you will burn cycles on the wrong fix and fail to communicate the real root cause to leadership. Framing it as an architecture ceiling does two things: it stops wasted effort, and it sets a realistic timeline (the fix arrives with AO 2.0, not the next sprint).
- **How to communicate it**: "The current agents route to a solution — they don't reason through one. This is a structural ceiling, not a prompt quality problem. AO 2.0 addresses the root cause. Expected: May at earliest, June-July realistic."

### Agent Categories Are Often PM Intuition, Not Customer Reality
- **Date identified**: 2026-03-23
- **Source**: Loni's AEM PM Virtual Working Session I (Agents, March 23). Loni stated this explicitly.
- **Insight**: Agent categories (Discovery, Governance, Production, etc.) typically emerge from how PMs think about their domain, not from observed customer behavior. They reflect internal org structure and PM intuition. Customers don't organize their problems the way product teams organize their agents. The 1200 real customer questions Corey Dulimba holds are the actual design input — and they may not map to the seven categories at all.
- **Application**: Before locking in agent categories as the organizing frame for any roadmap or surface, analyze real usage data. What are users actually asking for? Let observed behavior reshape the categories, not the other way around.

---

## Surface Strategy for AI Products

### The Human vs Agent Surface Split
- **Date identified**: 2026-03-23
- **Source**: Pedro's contribution in Loni's Session I (March 23), validated by Conrad Woltge. Reinforced in Session IV (March 26).
- **Insight**: AI products need two fundamentally different interaction surfaces: (1) human practitioners who need a guided, visual, discoverable UI; (2) agents and technical users who need direct MCP/API access. Conflating these creates products that serve neither well.
- **Design implication**: Build for humans through hero surfaces (Experience Hub, AI Assistant UI). Build for agents through MCP and API. Don't build a UI that tries to be both. The human surface and the agent surface should be designed independently with callability between them — any capability surfaced to humans should also be reachable via MCP.
- **Connected concept**: Hero surfaces strategy (see below).

### Hero Surfaces Strategy
- **Date identified**: 2026-03-26
- **Source**: Loni's AEM PM Virtual Working Session IV (Surfaces, March 26). "Times Square" concept.
- **Insight**: In a product ecosystem with many surfaces, you cannot run effective PLG, measure discovery, or build compounding feature awareness without designating which interfaces are canonical. A "hero surface" is the one you drive users toward, instrument, and build PLG motions on. Without naming it, every surface gets a little investment and none gets enough.
- **Three properties of a hero surface**:
  1. **Instrumented** — you know what users do there and why. PLG experiments run here first.
  2. **PLG-invested** — new capabilities, nudges, and onboarding land here, not across five different surfaces.
  3. **Callable from other contexts** — human-first design, not human-only. Any capability surfaced here must be reachable via agent or MCP. This is what makes it a platform, not just a page.
- **Common failure**: Building a hero surface by name but not by investment. The name means nothing if PLG budget and feature discovery keep getting distributed across all surfaces equally.

### Too Many Surfaces Is a PLG Killer
- **Date identified**: 2026-03-26
- **Source**: Loni's Session IV; Corey Dulimba's observation; Pedro's echoed point.
- **Insight**: Every time a team builds a new surface, they fragment the audience. Users can't form habits with a product they reach through four different entry points. PLG motions can't compound if every nudge lands in a different place. The instinct to build a new surface for every new feature is natural and wrong. The default should be "does this belong inside the existing hero surface?" not "let's build something new."
- **Application**: Evaluate every new UI ask against the hero surface. New surface requires explicit justification. Contributing to the existing surface should be the path of least resistance.

---

## Agent Measurement Infrastructure

### The Mandatory + Custom Dashboard Pattern
- **Date identified**: 2026-03-25
- **Source**: Felix Delval's aem-agent-reports platform analysis; Bertrand 1:1 notes March 24; Conrad/Gilles Slack March 24.
- **Insight**: Cross-agent measurement works when there is a shared mandatory baseline (same metrics, same definitions, same format across all agents) plus a custom section per agent (the unique signals that matter for that specific agent's use case). The mandatory layer enables comparison. The custom layer enables depth.
- **Mandatory baseline should include**: Technical Success Rate, Value Realization Rate, weekly funnel (interactions → customers → users), week-over-week trend, top failure patterns, top customer orgs.
- **Custom layer examples**: For EPA — file upload success rate, content change acceptance by content type. For Governance — rules/access intent breakdown, "cannot help" pattern analysis.
- **Why this matters**: Without the mandatory layer, no one can compare agents or spot cross-agent patterns. Without the custom layer, the report doesn't serve the agent team.

### Two-Track Reporting Infrastructure — Fast Iteration vs Stable Foundation
- **Date identified**: 2026-03-30
- **Source**: Yanira 1:1, AEM agent reporting setup.
- **Insight**: When building measurement infrastructure for an AI product, two tracks often need to run in parallel: (1) a fast-iteration track (manual, PM-driven, quick to change) that produces learning quickly; (2) a stable-foundation track (engineering-backed, data-platform integrated, scalable) that takes months. Confusing the two stalls both. The fast track should not wait for the foundation track to be ready. The foundation track should use the fast track's output as a spec.
- **Pattern**: Get the fast track to ~80% stable first. Use it to learn what the report needs to contain. Then hand that spec to the infrastructure team. This way the infrastructure team builds the right thing, not a guess.
- **Risk**: If the foundation team (DAS in this case) has a different motivation (cost tracking vs product quality), their natural output will not match what PMs need. Explicit alignment on requirements before they build is critical.

### Success Definitions Must Be Agreed Before Metrics Are Scaled
- **Date identified**: 2026-03-30
- **Source**: Yanira 1:1; Yanira's success definition wiki.
- **Insight**: Scaling a measurement dashboard before success definitions are aligned across teams creates a false picture. Each agent team may define "technical success" and "value realization" differently. When those definitions are different but the report shows them side by side, every comparison is misleading.
- **The right asset**: A per-agent success definition document, built jointly by PM and engineering, validated before the dashboard goes broad. In AEM, Yanira holds this as a wiki. Pedro must align Felix's dashboard column definitions to that wiki before presenting to leadership.
- **Application**: Before any cross-agent measurement goes to a senior audience, ask: "Do we have a shared definition of success for each agent in this report?" If no, the numbers are not ready to compare.

### Failure Taxonomy Needs an Explicit Quality vs Gap Split
- **Date identified**: 2026-03-30
- **Source**: Bertrand de Coatpont's response to W13 agent reports, March 30.
- **Insight**: When presenting agent failure data to senior stakeholders, mixing quality failures (agent tried, something broke) with capability gaps (agent structurally cannot do this) in a single table forces the reader to do the classification work themselves. Bertrand's first refinement request was to split these explicitly. The distinction matters because the response is different: quality failures go to engineering, capability gaps go to the roadmap.
- **Two failure types to surface explicitly:**
  - Quality = `failed-update`, `routing-issue`, `not-enabled`, `not-configured` tags. Agent tried. Fixable.
  - Gap = `unsupported` tag + explicit refusals. Agent cannot. Requires product decision.
- **Application**: Any top failed requests table should have a Type column. One word — Quality or Gap — that removes the inference burden from the reader.

### Report-to-Backlog Pipeline — Auto-Generating Stories from Structured Report Output
- **Date identified**: 2026-04-01
- **Source**: Pedro's adbe-agent-report-to-jira project trial, April 1, 2026.
- **Insight**: Product gap data in an agent report is only useful if it reaches the teams who can act on it. Manually filing JIRA stories from report observations doesn't scale. The right pattern: treat the report as a structured data source and auto-generate stories from it directly. Each product gap becomes a story, linked to an agent-specific epic, with the agent owner as default assignee and reporter. PMs triage — they don't create.
- **Structure that works**:
  - One epic per agent — scoped to that agent's gaps only, serves as the triage surface
  - Stories auto-generated by the pipeline — title, description, and acceptance criteria from report data
  - Default assignee + reporter = agent owner — routes accountability without manual intervention
  - Two-path triage — Not Relevant (close Won't Fix + one-line reason) or Relevant (set priority, leave open)
  - 30-day stale rule — stories with no action after 30 days go to backlog grooming
- **Critical supporting file**: Agent-Owner-Epic-Mapping.md — maps each agent to its PM owner, Jira username, and epic key. Pipeline reads this file. Without it, routing breaks.
- **Scale path**: Start with one agent (EGA trial). Get PM feedback on story format. Iterate. Then expand to all agents using the same mapping file.
- **Connection to JIRA Column pattern**: The JIRA column in reports (which existing JIRA tracks this failure?) is the manual precursor. This pipeline is the inversion — report generates JIRA, not the other way around.

### Connecting Failure Data to Engineering Tracking (JIRA Column)
- **Date identified**: 2026-03-30
- **Source**: Bertrand de Coatpont's response to W13 agent reports, March 30.
- **Insight**: A failure report that doesn't say whether the failure is already tracked is incomplete for an engineering stakeholder. Bertrand's ask: add a JIRA column (number if tracked, "not tracked" if not). This closes the loop between product observation and engineering action.
- **Important caveat**: This column cannot be automated from interaction data alone. It requires a human step — agent PMs mapping known failures to existing JIRAs. Build the column structure first, fill it manually, then automate as tracking matures.
- **Application**: Design failure tables with a JIRA column from the start, even if empty. An empty column signals awareness that tracking is expected. A missing column signals it hasn't been thought about.

### Report Infrastructure Needs a Stable Home Before Broader Distribution
- **Date identified**: 2026-03-30
- **Source**: Bertrand de Coatpont's response to W13 agent reports, March 30.
- **Insight**: When a senior stakeholder sees useful data for the first time, their first instinct is not to consume it — it's to ask where it lives permanently. Bertrand's first ask after "a lot of good information" was a stable URL, not a deeper analysis request. A report sent as a file implies it's a one-off. A report at a permanent URL implies it's infrastructure.
- **Secondary signal**: "Agents will consume this data" — Bertrand is already thinking about machine-readable access, not just human dashboards. The hosting question and the data format question are connected.
- **Application**: Before sharing reports broadly, have a hosting answer ready. It changes how people perceive the maturity of the system.

### Auth-Walled Hosting Is Incompatible with Agent-Consumable Reports
- **Date identified**: 2026-03-31
- **Source**: Pedro/Claude analysis of Bertrand's "agents will consume this data" ask, March 31.
- **Insight**: When a senior stakeholder says "agents should be able to consume this data," they are describing a technical constraint on hosting. Auth-walled systems (SharePoint, internal document stores, anything requiring SSO login) break agent consumption because an automated agent hitting the URL gets an auth wall, not data. This kills the machine-readable use case entirely, even if the URL is stable.
- **The right default**: Static hosting with no auth (GitHub Pages, public CDN, or internal open static host). If the data is sensitive, token-based access is acceptable — but not full OAuth/SSO flows that require browser interactions.
- **Application**: When evaluating hosting options for any report or data artifact that agents need to read, filter out any option that requires a browser-based login. Ask: "Can a script fetch this URL without human authentication?" If no, it doesn't qualify.

### Adding a New Agent to a Measurement Pipeline Is a Data Problem, Not an Engineering Problem
- **Date identified**: 2026-03-25
- **Source**: Felix Delval's aem-agent-reports architecture (agents.yaml, loader.py).
- **Insight**: Once a measurement platform exists with a defined schema, onboarding a new agent is about getting the right data in the right format — not building new engineering. Felix's platform adds an agent with 2 lines of YAML + a CSV in the right schema. The bottleneck is always data access, not code.
- **Application**: When advocating for cross-agent measurement standardization, the question to ask each agent team is: "Can you export your interaction data in this format?" That's it. If yes, the report is days away. If no, that's the gap to close.

---

## AI Product Risks

### The Vision-Reality Gap in AI Products
- **Date identified**: 2026-03-23
- **Source**: Experience Hub State of the Project. AEM employee meeting showed a vision mock, not the actual product.
- **Insight**: AI products are particularly prone to vision-reality gaps because demo environments are easy to curate and real usage exposes fundamental architectural limitations. When a leadership demo shows a vision mock instead of the real product, expectations form that the actual product can't meet. Every month the gap stays open, trust erodes.
- **Root causes**: (1) vision mocks are faster to build than real features; (2) it's tempting to show what's possible rather than what exists; (3) stakeholders want to be inspired and don't ask hard questions during demos.
- **Fix**: Name the gap explicitly. "What you saw in the demo was a vision mock. Here is what exists today. Here is what will exist by date X. Here is what requires AO 2.0 and won't be available until May-July." The reset is uncomfortable once. The alternative is permanent erosion of credibility.

### Overstating Agent Readiness at Scale
- **Date identified**: 2026-03-26
- **Source**: Haresh Kumar's customer story in Session IV (March 26). Modernization agent story failed in the field.
- **Insight**: An agent that works in a contained demo environment may fail at enterprise scale. Large codebases, complex configurations, and unusual edge cases expose limitations that controlled environments don't. Telling a customer that an agent can solve their problem before you have real-world evidence at their scale is a trust-destroying mistake.
- **Signal to watch for**: "It works well in contained environments" = not yet validated at enterprise scale. Treat as pre-GA until proven otherwise.
- **Application**: Before recommending an agent to a customer, ask: what is the largest real-world deployment we have evidence from? If the answer is a pilot or a demo, say so.

### Adoption Cadence as a PLG Instrument — The "Netflix Effect"
- **Date identified**: 2026-03-27
- **Source**: Shankari 1:1 handoff, March 27.
- **Insight**: A regular adoption review meeting that shows real usage data can become a high-engagement ritual — Shankari's EH adoption reviews had people showing up "like the next episode of Netflix." This is not accidental. It works when: (1) the data is live and surprising, (2) the PM frames results as "what we learned" not "what we did", (3) the rhythm is consistent enough that missing it feels like missing something important.
- **Application**: Adoption reviews are both a measurement tool and a visibility mechanism. The PM running them gets credit for transparency and rigor. Set the cadence early and hold it.

### PLG Checkbox Antipattern — Announcement Without Ownership
- **Date identified**: 2026-03-27
- **Source**: Shankari 1:1 handoff, March 27.
- **Insight**: In a product with a shared surface (like Experience Hub), teams will request real estate for PLG announcements and then disappear. They add the announcement, check the box, move on. The surface becomes stale and users stop trusting it. Loni and Jean-Michel are pushing company-wide: see usage in production before GA, and watch adoption after GA.
- **Rule that works**: Announcement goes live with a conversion metric and a 4-week review commitment. If the PM doesn't return with results, it gets pulled. No exceptions.
- **Why it matters**: Protecting the signal quality of a shared surface is a PM governance responsibility. If every team gets a slot, the surface becomes noise. Enforcing the rule is the product manager's job, not leadership's.

### Personalization in AI Products — Start Small or Not at All
- **Date identified**: 2026-03-27
- **Source**: Shankari 1:1 handoff, March 27.
- **Insight**: Enterprise personalization infrastructure is almost always more complex than it looks. The DX-level profile at Adobe requires integrating with Target, conforming to a specific framework, and dealing with data platform dependencies. Two years of pushing for this at Experience Hub produced nothing. The right approach for a resource-constrained team: identify two simple proxy data points (e.g. template setting + licenses owned) and run a small experiment. Don't wait for the full infrastructure.
- **Application**: When personalization comes up in roadmap discussions, ask: what is the smallest version of this we can test? Can we run it as a hack on a cohort of 1000 users before committing to a platform integration?

### Skills vs Prompts — A Fundamental Interaction Model Distinction
- **Date identified**: 2026-03-31
- **Source**: Pedro's voice notes (March 30); Bertrand brief drafted March 31; Agent Owner Alignment March 20.
- **Insight**: Prompts and skills are not the same thing, and surfacing them interchangeably in an AI product surface is a structural mistake.
  - **A prompt** is an open-ended intent expression. It invites the user to try something. It says nothing about whether the agent can reliably execute it.
  - **A skill** is a scoped, tested, packaged workflow. It communicates what the agent can do, what it cannot, and what a successful outcome looks like.
- **Why this matters for surface design**: A surface that shows prompt suggestions against agents with a 40-50% failure rate trains users to expect things the product can't reliably deliver. Every hallucinated or out-of-scope response after clicking a suggested prompt is a trust hit. Skills change the contract — users interact with defined capabilities, not an open box.
- **The evolution**: Prompt suggestions → skills discovery → skills + MCP connection awareness. Each step narrows the gap between what's surfaced and what's reliably executable.
- **Design implication**: The right interaction surface for a maturing AI product shows: (1) what skills are active for this user's license and environment; (2) what MCP connections are live (what tools/data the agent can reach); (3) what it cannot do. Not a generic grid of prompts.
- **Application**: When designing or evaluating any AI assistant surface, ask: are these suggestions grounded in what this system can actually reliably do for this user? If not, you are surfacing promises you can't keep.

### Cross-Region Data Aggregation Is a Compliance Risk in AI Measurement
- **Date identified**: 2026-03-31
- **Source**: Ian Boston (via Bertrand 1:1, March 31, 2026).
- **Insight**: AI agent interaction data is collected per region (in AEM: VA, NLD2, AUS5, CAN2, GBRS, IND1). Re-aggregating that data across regions for a unified report may violate data residency laws or contractual data governance agreements — especially in EU regions (GDPR) and regulated industries. The data pipeline may be technically capable of cross-region aggregation while being legally prohibited from doing so.
- **Important distinction**: The AEP Co-Pilot Report itself provides per-region data — the source is clean. The compliance breach happens in the aggregation step performed by the consuming pipeline (Felix, Lara), not at the source. This matters for framing the fix: it's a pipeline behavior problem, not a platform problem. The source doesn't need to change — the aggregation logic does.
- **Why PMs need to own this**: PMs who commission reporting infrastructure are often unaware of data governance constraints. Engineering builds what is technically possible. Legal and data governance teams are not automatically in the loop. The PM asking "do we have the right to aggregate this?" is the right check.
- **Application**: Before scaling any cross-region AI measurement pipeline, explicitly ask: what data residency rules apply to each region? Does the pipeline aggregate after extraction? If yes, that aggregation step may be the compliance breach — even if the source provides clean per-region data.

### Confirm Ownership Before Acting — Research First, Assume Nothing
- **Date identified**: 2026-04-01
- **Source**: AI-Assistant-Findings.md analysis; hanessia and igrafutko ownership chain confirmed.
- **Insight**: In cross-functional AI programs, PM ownership chains are rarely clean. Adjacent PMs often don't know who owns what. Pedro's situation: he was 3 weeks in and unclear whether he was a contributor or PM of record on Agent Assistant. The right move was to read the available documentation before taking a position in a Bertrand 1:1. The findings file confirmed hanessia owns the master PRDs and igrafutko owns QI — Pedro is a contributor on the EH integration surface, not PM of record.
- **Pattern**: Before claiming, disclaiming, or negotiating scope in any cross-team AI program, identify: who has a published PRD? Who runs the QI review? Who do agents on the program report to? Those answers define PM of record. You are a contributor until proven otherwise.
- **Application**: Entering a scope conversation with a stated read ("my read is X — is that yours?") is far stronger than entering with an open question ("so what exactly is my role?"). Research the org before the meeting.

### Regional Failure Concentration Is a Diagnostic Signal
- **Date identified**: 2026-04-01
- **Source**: AI-Assistant-Findings.md — NLD2 46% failure rate across agent interactions.
- **Insight**: When failure rate data is available by region, look for concentration before averaging. NLD2 showing a 46% failure rate while overall rates are lower means the aggregate number understates the problem in that region and overstates it in others. A regionally concentrated failure pattern suggests an infrastructure, latency, or configuration issue specific to that region — not a prompt quality or agent logic problem.
- **Application**: Any cross-region AI product should segment failure data by region before drawing conclusions. If one region is significantly worse, investigate root cause (data residency, latency, regional model deployment) before averaging it away.

### Anonymization Does Not Fix Data Residency — Ian Boston's "Stolen Data" Framing
- **Date identified**: 2026-04-01
- **Source**: Ian Boston's Slack response to Pedro, April 1, 2026.
- **Insight**: Anonymization is often suggested as a fix for data compliance in AI measurement pipelines. It is not. As long as a prompt is readable, it remains customer data — and data residency obligations follow the data, not its identifiability. To anonymize to the point where it is no longer customer data, you must transform it to the point it loses all evaluation value. Ian's framing: if you can no longer identify the customer from the data, you have effectively stolen it — it becomes Adobe data, and you can no longer delete it when the customer terminates (breaking data lifecycle requirements).
- **The one loophole**: Classify prompts as operational data. This permits centralization, but restricts use to maintaining service uptime only. You cannot use operational data to evaluate or improve the service — which makes it useless for agent measurement and reporting.
- **Ian's meta-point**: The PLAs from end of 2025 may not have been fully signed off. His preference is to fix the problem quietly before it surfaces to legal. If legal gets involved and the problem is confirmed: stop immediately, fix, and potentially do more remediation.
- **Application**: When someone proposes anonymization as a compliance fix for cross-region AI data, ask two questions: (1) Is the data still readable as a prompt? If yes, it's still customer data. (2) Does the residency obligation apply to where data is processed, not just stored? If yes, anonymization changes nothing about geography.

### Monetization Is Unresolved When Agents Replace Seats
- **Date identified**: 2026-03-26
- **Source**: Loni's Session IV (Surfaces, March 26). Haresh Kumar raised; Loni and Bertrand acknowledged.
- **Insight**: Traditional seat-based SaaS pricing breaks when agents replace human users. If one agent does the work of ten humans, and you charge per seat, your revenue collapses as adoption succeeds. MCP/skills metering (charge per capability invocation) is the emerging model but is not yet defined or tested. This is a company-level strategic gap.
- **PM implication**: Do not position agent capabilities in customer conversations using a pricing frame until internal strategy is landed. The cost conversation can kill the capability conversation before it starts (see Haresh's $500K customer story).
