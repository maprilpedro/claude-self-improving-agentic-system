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

### Failure Taxonomy Needs an Explicit Quality vs Gap Split
- **Date identified**: 2026-03-30
- **Source**: Bertrand de Coatpont's response to W13 agent reports, March 30.
- **Insight**: When presenting agent failure data to senior stakeholders, mixing quality failures (agent tried, something broke) with capability gaps (agent structurally cannot do this) in a single table forces the reader to do the classification work themselves. Bertrand's first refinement request was to split these explicitly. The distinction matters because the response is different: quality failures go to engineering, capability gaps go to the roadmap.
- **Two failure types to surface explicitly:**
  - Quality = `failed-update`, `routing-issue`, `not-enabled`, `not-configured` tags. Agent tried. Fixable.
  - Gap = `unsupported` tag + explicit refusals. Agent cannot. Requires product decision.
- **Application**: Any top failed requests table should have a Type column. One word — Quality or Gap — that removes the inference burden from the reader.

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

### Monetization Is Unresolved When Agents Replace Seats
- **Date identified**: 2026-03-26
- **Source**: Loni's Session IV (Surfaces, March 26). Haresh Kumar raised; Loni and Bertrand acknowledged.
- **Insight**: Traditional seat-based SaaS pricing breaks when agents replace human users. If one agent does the work of ten humans, and you charge per seat, your revenue collapses as adoption succeeds. MCP/skills metering (charge per capability invocation) is the emerging model but is not yet defined or tested. This is a company-level strategic gap.
- **PM implication**: Do not position agent capabilities in customer conversations using a pricing frame until internal strategy is landed. The cost conversation can kill the capability conversation before it starts (see Haresh's $500K customer story).
