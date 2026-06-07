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

### Measure at the Unit of User Intent, Not the Unit of System Event
- **Date identified**: 2026-04-22
- **Source**: Varun Kalra (Discovery Agent technical validator, Apoorva's team) in sync with Pedro, April 22, 2026. Discussing how Apoorva's three value-realization metrics (Query Unsuccessful Rate, First Useful Result Rate, Remaining Prompts Rate) should be computed.
- **Insight**: Value-realization metrics for an agent have to sum to something meaningful (typically 100%) to be interpretable as a distribution. They only sum cleanly when the denominator matches the unit of user goal — the intent — not the unit of system event — the interaction. Pedro's initial implementation measured at chat or interaction level. Varun's correction: one intent can span multiple interactions. If the user fires four queries refining the same intent and two return results, splitting the four into different buckets at the interaction level produces three categories that will never add to 100%. Measure at the intent level: the intent is the carrier of "did the user get what they wanted."
- **Concrete rule**:
  - **Intent 1, returned nothing** → Query Unsuccessful bucket.
  - **Intent 2, returned results, no follow-up query for the same intent within 2 minutes** → First Useful Result bucket.
  - **Intent 3, required follow-up refinements before success** → Remaining Prompts bucket.
- **Why this matters beyond metrics**: Intent-level measurement forces the product team to define "what is an intent" — which in turn forces clarity on what the agent is supposed to resolve vs. what's a refinement vs. what's a new task. This is a product-definition exercise disguised as a measurement exercise.
- **Application**: For any agent-UX metric that involves success / failure classification across a conversation, audit the unit. If it's at the interaction or chat level, you probably need intent-level aggregation. The 2-minute window is a reasonable default for intent continuity; the exact threshold needs validation with the product owner.
- **Anti-pattern**: Reporting three mutually-exclusive categories that don't sum to 100%. The gap IS the signal that your unit of measurement is wrong.
- **Related**: Technical Success Rate vs Value Realization Rate (different metrics, same intent-unit principle); VRR Is a Tiered Metric.

### "No Results Found" Is a Product Gap in Agentic UX — Not a Legitimate Answer
- **Date identified**: 2026-04-22
- **Source**: Varun Kalra and Apoorva Gupta's team, Discovery Agent validation review (April 16 audit + April 22 Varun sync).
- **Insight**: In classical search UX, "no results found" is a legitimate response — the system searched, nothing matched, the user knows to refine. In agentic UX, it's a failure to engage. Varun: "Telling the customer that we can't do anything and saying 'no results found' means we can't do anything. We need to nudge the customer — ask clarifying questions or give suggestions." An agent that returns empty-handed in response to a prompt has abdicated its role as an agent. The correct minimal response is "I understood this much, can you clarify X?" or "here are three directions you might explore."
- **The differentiation problem**: When "unsupported query" and "no content matched" collapse into the same "no results found" response, the product team can't triage. Is this a content gap (real user need, no data)? A scope gap (user asking for something the agent was never built to do)? A search-quality gap (data exists, agent couldn't find it)? The single response destroys diagnostic clarity.
- **The Governance Agent model as contrast**: Governance Agent explicitly returns "I cannot help with this" for unsupported queries. That's distinguishable from "nothing matched." You can see what the agent can't do and build a roadmap from it. Varun's framing: "If we are not doing this, we cannot differentiate between a scenario where the customer query legitimately led to no results vs. the query was not supported."
- **Application**: In any agentic surface, banish the empty reply. Every failure mode should be named and distinguishable. Minimum failure taxonomy: (1) I understood but I'm not built for this, (2) I couldn't understand — please clarify, (3) I understood and the data doesn't exist, (4) I understood and there's a system error. Each is actionable differently.
- **Anti-pattern**: Returning silent-fail responses that a classical search product would accept. The bar for agentic UX is engagement, not query fidelity.
- **Related**: The Open Chat Box as Discovery Mechanism; Agents Need to Surface Problems, Not Just Solve Them.

### Capability-Level Monthly Usage Is the Value Narrative Metric (BVR)
- **Date identified**: 2026-04-23
- **Source**: Pedro + Philippe Kapfer Governance Agent report review, April 22–23, 2026. Context: identifying what metrics to expose for Governance Agent value realization ahead of Loni + Jean-Michel meeting (week of May 4). Wiki reference: [AEM Agentic Success Definition Compliance Framework](https://wiki.corp.adobe.com/spaces/WEM/pages/3774169978/AEM+Agentic+Success+Definition+Compliance+Framework).
- **Insight**: TSR, VR (intent-level), and VRR (tier-based) all answer the same question at different resolutions: *was this interaction valuable?* They operate at the interaction or intent level. Leadership doesn't consume interaction-level data — they consume **rate of value-producing events per month**. That requires a different metric unit: **capability-level monthly count**. "Brand checks performed per month" and "permission audit requests via agent per month" are not derivatives of VR or TSR — they are the count of times the agent did its job. This is the metric that maps to the adoption narrative ("the agent delivered value X times this month") and to the Senior Director level story Pedro is building for Loni.
- **Two Governance Agent candidates (April 22)**:
  - Number of brand checks performed per month
  - Number of permission audit requests performed via agent per month
- **Why this unit matters**: Rate metrics (TSR, VR) normalize for volume — a 60% VR at 100 interactions and at 100,000 interactions read the same. The capability-level count restores the volume signal that VPs need: "this agent is being used 50× more than last quarter." Without it, a successful adoption arc is invisible in your dashboard.
- **When to use each unit**:
  - TSR → *does the system work?* (engineering / platform health)
  - VR intent-level → *does the user get what they came for?* (product experience quality)
  - VRR tiered → *what shape of value distribution are we seeing?* (strategic framing)
  - **BVR capability-count → *how much value did this agent produce this month?*** (adoption narrative, VP-facing)
- **Application**: For every AEM agent, identify 1–2 capability-level monthly counts that map to its reason for existing. These become the headline numbers in the adoption story. Validate definitions with the agent's PM owner; implement with the parallel reporting track owner.
- **Anti-pattern**: Reporting only rate metrics to leadership. The absence of a volume number makes every success story unfalsifiable — nobody can tell if the agent is growing or shrinking.
- **Related**: Metric Definition Ownership — PM Validates, Reporting Track Owner Implements; Two-Validator Pattern for Report Rollout; VRR Is a Tiered Metric.

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

### Agents Need to Surface Problems, Not Just Solve Them — The "Sensor + Hero" Model
- **Date identified**: 2026-04-10
- **Source**: Loni Stark, H2 Prelim In/Out Priorities Part 3 (April 2026). Dynamic Media Templates / Content Optimization Agent discussion.
- **Insight**: Agents fail to drive adoption not because they're hard to use, but because users don't know they have a problem worth solving. The leaky pipe analogy: there may be a broken pipe in your home right now — it's urgent, but you're calm because you don't know about it. Agents that only execute on demand miss the upstream problem: no one thought to ask.
- **The two-part model Loni described**:
  1. **Sensor**: The agent (or surface) proactively surfaces a signal — "your 10 banner ads are underperforming and it's costing you $1M in revenue." Without this, the human never triggers the workflow.
  2. **Hero**: When the problem is surfaced, fixing it needs to be trivially easy and make the human look good. Not just "easy to use" — easy *and* career-positive. Marketers who find a problem but know fixing it means more work won't raise it.
- **The exec dashboard corollary**: The sensor signal needs to surface to leadership, not just the practitioner. A marketer who knows their banner is underperforming won't raise it if it creates work. Surface it directly to an exec dashboard so the pressure to act comes from above, not from the user discovering it themselves.
- **Application**: When evaluating why an AI feature has low adoption, ask first: does the user know they have a problem this feature solves? If the trigger is purely user-initiated, you haven't solved the awareness problem. The feature needs a proactive signal — an alert, a notification, an inline indicator — that surfaces the need before the user thinks to ask. This applies to EH: showing agent capabilities isn't enough. EH needs to surface that the capability is relevant *right now* for *this user*.

### Removing Friction Is Not Enough — Agent Adoption Can Still Fail
- **Date identified**: 2026-04-10
- **Source**: Apoorva Gupta, H2 Prelim In/Out Priorities Part 3 (April 2026). Content Optimization Agent + DM Templates adoption analysis.
- **Insight**: Apoorva's Content Optimization Agent simplified rendition creation (no need to know smart crop presets). Adoption is still negligible. DM Templates launched 18 months ago, 14 months of near-zero adoption. In both cases: feature exists, friction was removed, adoption still didn't come. Apoorva's own words: "even if you remove the friction, the adoption is not happening to the level we want."
- **Why this happens**: The friction that's visible to PMs (the UI is hard, the steps are complex) is not always the friction that blocks users. The invisible friction is: they don't know they need this, they don't have a workflow trigger that pulls them to the feature, and the moment of need doesn't happen in the surface where the feature lives.
- **Loni's reframe**: It's not that we targeted the wrong persona. It's that we built a car with controls too hard for the driver to use. The persona was right — the execution didn't serve them. But even with a fixed UI, if there's no trigger pulling that persona to the feature, adoption won't follow.
- **Application**: Before investing in friction reduction for a low-adoption AI feature, validate that the awareness and trigger problems are solved. Friction removal on an unknown feature produces nothing.

### The Cold Start Problem for AI Agents
- **Date identified**: 2026-04-10
- **Source**: Loni Stark, H2 Prelim In/Out Priorities Part 3 (April 2026). Brand-aware metadata + onboarding agent discussion.
- **Insight**: Loni's explicit question: "How does a human get the aha moment without even having to invoke any agent?" A feature that requires user initiation to show value has a cold start problem — the user has to take an action to see why they should take an action. This is circular. The feature has to be useful from the moment the user lands in the surface, before they've done anything.
- **Concrete form**: If a user lands on a screen and sees nothing relevant to them until they click something, you've failed the cold start test. The contextual value has to be visible from state zero — relevant, timely, requiring no configuration or invocation.
- **Connected pattern**: This is why the "Sensor + Hero" model matters — proactive surface of relevant signal solves the cold start problem. The user lands and sees: "Here's what matters for you right now." No click required.
- **Application**: For every new AI feature or agent capability added to EH, ask: what does the user see before they do anything? If the answer is a blank box or a generic grid of prompts, you haven't solved cold start.

### Agent Failure Rate Is Often an Architecture Ceiling, Not a Prompt Quality Problem
- **Date identified**: 2026-03-23
- **Source**: Loni's AEM PM Virtual Working Session I (Agents, March 23). Cedric Huesler confirmed.
- **Insight**: A 40-50% agent failure rate can look like a prompting problem. It often isn't. If agents route to a solution without reasoning through one, there is a structural ceiling on quality that no amount of prompt tuning will raise. In AEM, the current architecture routes — it doesn't reason. AO 2.0 adds agent loop reasoning. Until it lands, the failure rate has a floor.
- **Why it matters for PMs**: If you frame a quality problem as a prompting problem, you will burn cycles on the wrong fix and fail to communicate the real root cause to leadership. Framing it as an architecture ceiling does two things: it stops wasted effort, and it sets a realistic timeline (the fix arrives with AO 2.0, not the next sprint).
- **How to communicate it**: "The current agents route to a solution — they don't reason through one. This is a structural ceiling, not a prompt quality problem. AO 2.0 addresses the root cause. Expected: May at earliest, June-July realistic."

### AO 2.0 Is Plugin-Based, Following Anthropic Open Protocols
- **Date identified**: 2026-04-07
- **Source**: Sergey Generalov email (April 2, 2026) forwarded via Shankari → Bertrand → Pedro. Bertrand 1:1 April 7.
- **Insight**: Agent Orchestrator 2.0 is extensible through plugins using Anthropic's open protocols (same underlying model as MCP). The pattern: install AO locally → create a plugin repo from a marketplace template → add your marketplace to AO settings → iterate on plugins and skills. AO 2.0 is also going open-source with a maintainer/contributor model — teams can send PRs and senior members can become closer contributors.
- **Why it matters for EH**: (1) EH's Skills surface (Priority 1) should evaluate whether to source skills from registered AO plugins rather than a separate mechanism. (2) The plugin/marketplace contribution model may be a cleaner path than the App Builder/iframe approach Mircea demoed March 27. (3) AO 2.0 lands May–July — the timing aligns with the Skills surface redesign window.
- **Key distinction**: Manas Garg = AO engineering lead. Sergey Generalov = PM adjacent to the AO orchestrator (partial ownership). Conrad is the architecture lead. For PM-level AO 2.0 questions, the right contacts are Conrad, Ian Boston, Carsten Ziegeler, and Sergey Generalov — not Sorin (EH engineering).
- **Caution**: AO 2.0 goes deeper than UI. Bertrand's framing: "it's about the underlying reasoning logic." It's not just a frontend upgrade. Form a point of view before presenting to leadership.

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

## Distributed-Harness Architecture (AOv2 / Agentic NorthStar)

### Everything Is a Skill — the "Agent" Dissolves as a Build Unit
- **Date identified**: 2026-05-22
- **Source**: Ian Boston, *Agentic NorthStar* blog (wiki, 2026-05-19) + follow-up thread (May 19-22), Pedro as first substantive responder.
- **Insight**: Once harness reasoning becomes a commodity (Claude / Codex / Pi SDKs), value moves to **skills + unique APIs + memory**, and the "agent" stops being a distinct build unit. What runs is a *harness loaded with skills*. Ian: *"focus on Skills not agents."* His own example: DAA, formerly an agent, is *"now implemented as a collection of Skills in a harness."*
- **Critical nuance — two units, not one**: the agent dies as a **build/technical** unit but survives as a **GTM/customer-facing** unit — customers still buy "Discovery Agent," "Governance Agent." So: *build as skills; package and sell as agents.* Conflating them confuses devs (who hear "no more agents") and sales (who still sell them).
- **Implication for prioritization**: the common org question "build skills under existing agents **vs** new agents" is partly outdated. Reframe: everything is a skill; the only real decision is **which harness it lives in** — existing by default, a new harness only when a genuine new *persona + context* boundary is crossed (a monolithic harness reasons worse and costs more — see token-cost entry).
- **Caveat**: the NorthStar is a direction (the blog ends on a question), not ratified doctrine. Frame as "where the architecture points"; agent owners' work reframes, it doesn't vanish.
- **Cross-link**: [[Moat = the Data, Not the Mechanism]], [[Selection and Cross-Surface Consistency Are a PM Mandate]], [[Agentic Extensions Have a Token-Cost Hierarchy]].

### Moat = the Data, Not the Mechanism
- **Date identified**: 2026-05-22
- **Source**: Pedro's framing in the Ian NorthStar thread, endorsed by Ian (*"a great way of putting it"*; tied to a senior early-March conversation with @lkao + @gmiller; Adobe Research active in the space).
- **Insight**: A capability built on open, portable standards (open API / MCP, fork-and-run) appears to conflict with lock-in (*"heartbreaking to leave"*). It resolves by separating layers: keep the **mechanism open** (interface, protocol) for adoption + portability; the **moat is the data** — the customer's accumulated content, context, and memory, costly to rebuild elsewhere. *Open interface, sticky data.* Ian's analogy: Gmail is portable (takeout) yet heartbreaking to leave because of the accumulated value on top.
- **Implication**: (1) **Positioning** — sell accrued value, not lock-in: *"you stay because leaving means rebuilding years of context,"* credible precisely because the interface is open. (2) **Measurable** — accumulated-memory value shows up as returning orgs/users + retention (the signal Pedro already owns). (3) For AEM, the customer's content *is* a primary memory source.
- **Cross-link**: [[Repeating Users as the Primary Value Signal]] (measurement), [[Everything Is a Skill — the "Agent" Dissolves as a Build Unit]].

### Selection and Cross-Surface Consistency Are a PM Mandate
- **Date identified**: 2026-05-22
- **Source**: Ian NorthStar thread. Verbatim: *"the UI deciding which harness to call"* (explicit or prompted selection, *not* automatic intent detection); *"UX, yes, absolutely, must be PM lead"*; *"Consistency will be vital so an Adobe user feels like it is the same surface regardless of the implementation details or UI engineering ownership."*
- **Insight**: In a distributed-harness model two things become **product (PM) problems, not architecture**: (1) **Selection** — which harness/agent a request routes to. The UI decides; *explicit or prompted* selection beats *auto intent-detection* (the seductive option that burned trust in AOv1, where the orchestrator inferred intent and routed wrong). (2) **Consistency** — making independently-owned, distributed surfaces feel like one coherent Adobe product. Consistency is in direct tension with distributed UI ownership; reconciling it is the PM mandate, and the architecture-backed answer to "too many surfaces / 4-chats" fragmentation.
- **Implication**: selection-as-UX and cross-surface consistency are the differentiator and the PM's lane (architect put it on record). For AEM this elevates the hero surface (Experience Hub) from a launchpad to the **selection + consistency layer** of the distributed agent architecture.
- **Refinement — the concrete mechanism of cross-surface *continuity* (2026-06-05, EH→EW handoff case)**: when two surfaces are two UIs on two separate harnesses (EH home + Experience Workspace), making one experience span them ("start in EH, deep authoring opens EW, conversation + context carry") does **NOT** require merging the harnesses or putting both on the same engine. It requires **three things shared *above* both harnesses**: (1) a **shared memory/session** keyed to IMS identity (one surface writes, the other reads), (2) a **shared skills/prompt inventory** (a skill invoked on one surface is the same one the other continues — declared once, reachable from both), and (3) a **handoff** (surface A deep-links into surface B passing the session reference + prompt). The harnesses stay separate; continuity lives in the substrate above them. **This is why "distributed engineering, unified experience" is mechanically possible, and why cross-surface continuity is engine-independent** (it does not depend on both surfaces running the same harness). Practical sequencing: the shared skills inventory is the nearer-term piece; the shared cross-surface memory/session is the harder, often-missing piece (a real platform dependency — e.g. Ian's memory service). The PM owns the **cross-surface experience requirement + the handoff contract** (what continuity must carry, grounded in a concrete user moment); the platform owns the **memory service** that fulfills it — own the requirement, not the implementation.
- **Refinement — heterogeneous build substrates force the check-path, they don't permit the components-path (2026-06-05, EH vs EW evidence)**: there are two ways to make distributed surfaces consistent — *build it the same* (shared design-owned components, identical by construction) or *check it's the same* (write the definition, let teams build freely, conform each surface to the definition + flag drift). Which is available is **not a free choice when surfaces already run different component systems.** Observed: Experience Hub uses a custom UI framework; Experience Workspace builds on the DA-NX component library. Because they share no component substrate, consistency between them **cannot** come from shared components — only from a definition + a check that spans both. So the more heterogeneous the surface estate (and a distributed-harness world trends that way), the more the check-path is the *only* one that scales across all of it; shared components remain valid **within** a substrate (a surface that already has them uses them), never **across** independently-built ones. Practical: the consistency definition must be **readable by an LLM** (markdown) precisely so the check works against any surface regardless of how it was built. Don't propose shared components as the cross-surface consistency mechanism; propose the definition + check, and let shared components be one surface's internal way of meeting it.
- **Cross-link**: [[Hero Surfaces Strategy]], [[Too Many Surfaces Is a PLG Killer]], [[Everything Is a Skill — the "Agent" Dissolves as a Build Unit]], [[The Distributed Front Fragments in Three Ways — Three PM-Owned Fixes]], [[A Rendering Contract Carries Structure, Not Skin — the Brand Travels Only Where You Own the Renderer]].

### Agentic Extensions Have a Token-Cost Hierarchy
- **Date identified**: 2026-05-22
- **Source**: Ian Boston, *Claude Token costs* blog (wiki, 2026-05-20) + the ClaudeCode deep-dive token-economics breakdown he cites.
- **Insight**: Every active extension costs tokens **every turn, even when its tools are never called** — and the cost varies by an order of magnitude: hooks **0**, skills **~200-500**, plugins **~500-2K**, **MCP server manifest ~2K-15K**. Context window ~200K; conversation history is the largest segment (40-60%); compaction reclaims budget but trades information quality. Five MCP servers can permanently cost 50-75K tokens of history.
- **Implication**: architecture decisions are token-budget decisions. **Prefer skills (and hooks) over MCPs**; an MCP earns its manifest cost only for a high-value, unique capability (e.g. a shared memory service). A memory-as-MCP must keep its manifest lean and return ranked, relevant context, or it becomes the bloat it is meant to serve. Reinforces the skills-over-MCP consensus (Trent / Carsten / Felix Meschberger).
- **Cross-link**: [[Everything Is a Skill — the "Agent" Dissolves as a Build Unit]], [[Moat = the Data, Not the Mechanism]].

### The Distributed Front Fragments in Three Ways — Three PM-Owned Fixes
- **Date identified**: 2026-05-28
- **Source**: Synthesis from the Ian Boston *Agentic NorthStar* thread (2026-05-19 to 28), Pedro as first responder + co-author.
- **Insight**: A distributed-harness model (each team owns its UI + skills + session) buys depth but fragments in three *separate* ways. Conflating them as one "fragmentation" blob hides the fix. (1) **Juggling** — the user hunts across surfaces (the four-chats problem). Fix: **there-waiting**, the relevant capability is present on the surface the user is already on. (2) **Incoherence** — each surface feels like a different vendor. Fix: a **consistency layer**, shared shell + interaction patterns + cross-surface continuity. (3) **Wrong surface** — a surface misses skills, carries junk, or holds stale ones. Fix: a **registry**, one curated source of truth (shared declaration schema + curation) that the surface-owner PM composes each surface from, precise + complete. Three layers: registry = **supply** (is the surface correct), there-waiting = **delivery** (does the user hunt), consistency = **experience** (does it feel like one Adobe). Remove one, fragmentation returns through that hole.
- **Why it matters**: "distributed = fragmented" is the reflexive objection to a distributed-harness architecture. The answer is **distributed engineering, unified experience**, and all three fixes are product/PM problems, not architecture — the architect (Ian) put it on record: selection + consistency "must be PM led," surface placement is "governed." This is the PM lane in the agent architecture, and the elevation of a hero surface (Experience Hub) from launchpad to the selection + consistency layer.
- **Cross-link**: [[Selection and Cross-Surface Consistency Are a PM Mandate]], [[Everything Is a Skill — the "Agent" Dissolves as a Build Unit]], [[There Waiting Has Two Forms — Consistent Chat or (Often) Invisible]].

### There Waiting Has Two Forms — Consistent Chat or (Often) Invisible
- **Date identified**: 2026-05-28
- **Source**: Ian Boston, NorthStar thread round 3 (2026-05-28).
- **Insight**: "There waiting" (the right capability present where the user works) does not mean a chat window on every surface. **The form follows the surface.** Sometimes a chat is right; often embedded/ambient functionality is better, and *"the best assistants are almost invisible"* (Ian) — e.g. keeping content on brand via real-time guidance woven into the authoring surface, no chat at all. Two forms of presence: (a) a **consistent chat** where chat is the right tool, and every chat must obey shared rules (same controls, the "+" offering the same class of actions, user messages on the same side, **learn-once-or-it-is-a-fail**); (b) **invisible/embedded** everywhere else. Which form a surface gets is **governed** by persona + context, not a per-team choice, via a *surface map* (the sibling of the skill registry).
- **Why it matters**: this sharpens "there-waiting" and defuses the fragmentation fear harder — embedded/invisible help is not another window to juggle, so "many surfaces" never means "many chats." It also sets the UX bar: a chat the user must relearn per surface is a failure. Pairs with the three-fixes model: the consistency layer governs the chat-form surfaces; the registry feeds skills into both forms.
- **Cross-link**: [[The Distributed Front Fragments in Three Ways — Three PM-Owned Fixes]], [[Selection and Cross-Surface Consistency Are a PM Mandate]].

### A Single-Harness Marketplace Is Not a Cross-Harness Standard — Publish vs Find
- **Date identified**: 2026-05-28
- **Source**: Pedro's AOv2 confirmation (2026-05-28) against the distributed-harness model; grounded in the 2026-04-29 AOv2 alignment transcript + AOv2 plugin docs (Confluence 3851715892).
- **Insight**: A per-harness plugin marketplace solves *supply within one harness* and nothing above it. AOv2's model is concretely git-native and local-copy: a marketplace git repo (template `OneAdobe/ao-plugin-extensions-template`) installed into a local AO. It does **not** address the cross-harness layer the distributed model needs: one consistent **declaration standard** so skills are described the same way across *different* harnesses (AEM's, CXO's, DMe's), a **shared discovery index**, and a **curation convention**. The reflexive objection "AOv2 already has a marketplace" conflates the two. The anchor that separates them: **publish vs find** — a marketplace is how a developer *publishes* a skill into a harness; the missing layer is how the right skill is *found and made present* across all of them. (Skill-level evals are a neighbouring unsolved gap: a harness can install skills it cannot evaluate at skill granularity — Trent, 2026-04-29.)
- **Why it matters**: the PM-ownable layer in a distributed-harness world is the standard + discovery + curation *above* any single harness's store. That is definition ownership ([[Definition Ownership Is the Moat on Shared Data Infrastructure]] in leadership/), not a competing service — and the stronger political position, because a standard is not a turf-fight while a central registry is (Ian's round-4 deflation). Naming "publish vs find" is what stops a cross-harness proposal from being dismissed as a duplicate of an existing marketplace. Keep this distinction in internal/architecture conversations, not in a public post that names the AOv2 gap by name (additive-not-corrective).
- **Cross-link**: [[The Distributed Front Fragments in Three Ways — Three PM-Owned Fixes]] (this is the "registry = supply" fix, sharpened against AOv2), [[AO 2.0 Is Plugin-Based, Following Anthropic Open Protocols]], [[Everything Is a Skill — the "Agent" Dissolves as a Build Unit]].

### A Rendering Contract Carries Structure, Not Skin — the Brand Travels Only Where You Own the Renderer
- **Date identified**: 2026-05-29
- **Source**: Researched while pressure-testing a claim in Pedro's consistency-layer draft (Eugene Bannykh proposed `@adobe/a2ui-components` + A2UI as the cross-harness UI contract). Web research on A2UI / MCP Apps / WebMCP; Cedric Huesler's 2025-12-18 #aem-agents framing of A2UI + MCP-UI as the emerging standards.
- **The landscape (three distinct things, often conflated)**:
  - **A2UI** (Google, open, ~Dec 2025): agent emits a declarative JSON description of UI; the **client renders it with its own native components** (React/Flutter/web components). Framework-agnostic, portable, no executable code crosses the boundary.
  - **MCP Apps / MCP-UI** (Anthropic/MCP side): the **app ships its own UI** into the host, rendered in a sandboxed iframe inside the conversation.
  - **WebMCP** (browser standard): a page **exposes its tools** to the browser's agent so the agent can act on the page. This is interaction/control, **not** UI rendering. (Mithril is built on WebMCP.) Orthogonal axis — do not confuse it with the rendering standards.
- **Insight**: An open rendering contract makes the **structure/semantics** of the UI portable (this is an asset card, these fields, these actions). It does **not** automatically carry the **brand skin**. How much of the brand travels depends on *who renders*: full on your own surfaces (you control the renderer + load your component lib); possible in app-hosted hosts where you ship the UI (MCP App iframe in ChatGPT); structure-only in a host that renders A2UI with its *own* components (the look is theirs unless they adopt your library, which a third party will not); none in a text client like Claude Code. So "open standard ⇒ the brand travels everywhere" is **overclaimed** — the correct statement is *the contract keeps the skill usable everywhere; the brand stays consistent only where you own the rendering.*
- **Why it matters**: this is the concrete answer to the fragmentation/"customers bypass our UI and use the skill in Claude" fear — useful but bounded. It also makes the standard-selection decision (A2UI vs MCP Apps) a *product* decision with a real criterion: **where do we want the brand to travel**, not an abstract bake-off. Don't pattern-match the architecture phrasing ("central, consumed everywhere, not re-implemented per harness") onto an object it doesn't cover — compare what actually renders ([[feedback-dont-conflate-pattern-with-object]] in memory).
- **Refinement (2026-06-03, Brian Chaikelson question, now acted on the published post)**: the brand is not one thing — it has **two layers that travel by different vehicles**, and the original entry conflated them. **(1) Visual skin** (colors, components, an asset card) rides the **renderer** → travels only where you own/ship the UI (the bounded claim above). **(2) Structure, voice, workflow, guardrails** ride the **skill (SKILL.md) itself** → travel **everywhere the skill runs, including a plain-text client where there is no rendering contract at all.** So "the brand can't travel to Claude Code" is wrong as stated: the *visual* half can't, but the *behavioral* half does — the skill can still sound like Adobe, follow the workflow, enforce the guardrails, structure the answer. **Consequence for the consistency layer's definition:** it must cover both layers (the look where we control it; the voice/structure/guardrails everywhere), and the behavioral layer is the more portable, more enforceable one.
- **The check splits the same way — LLM-judgeable rules vs human taste (same date)**: how do you *verify* a surface is consistent? Split by layer. The **behavioral brand** (chat grammar, "+" actions, voice, structure, guardrails) is expressible as **checkable rules** → an **LLM-as-judge against a written definition** does well (precedent: the agent reports already use LLM-as-judge for quality conformance). The **visual skin + the "does this feel like one Adobe" craft bar** is **human taste — design's call** (Eugene/Silvia). So the definition's job is to push as much as possible into the checkable layer (so the automated check scales) and be honest that the residual is taste design owns. The cheapest PoC of the whole mechanism = run an LLM against a v0 definition + captured output of 2-3 surfaces and see if the drift report is useful.
- **Cross-link**: [[Selection and Cross-Surface Consistency Are a PM Mandate]], [[There Waiting Has Two Forms — Consistent Chat or (Often) Invisible]], [[The Distributed Front Fragments in Three Ways — Three PM-Owned Fixes]].

### Three-Layer AI Skill Governance Architecture (Customer-Side)
- **Date identified**: 2026-06-05
- **Source**: Silvia Mulet Ferre DM (2026-06-05, correcting an initial misread of her "explicit skills" ask); corroborated independently by Ian Boston's individual/org/solution memory model (Silvia/Ian/Eugene call 2026-06-04). 2 independent sources, different domains (skills governance + memory model), converging on the same layering principle.
- **Insight**: In an enterprise AI product where hundreds of skills could be loaded, *who sees and uses which skills* decomposes into **three nested, non-competing layers**: **(1) Governance** — the company's AI admin / Center of Excellence sets the **allowed set**: what skills exist, which users/roles can access them, approval required before publication. This is enterprise-enablement, honoured at harness runtime. **(2) Surface** — the surface auto-loads the **context-appropriate subset**: skills chosen by the surface PM based on persona, role, and surface context. The user never hunts. **(3) User** — the user curates their **own list within the governance boundary**: personalizes inside what's been unlocked. The layers nest and do not compete — removing any one layer creates a specific failure mode: no Layer 1 → compliance/cost risk (any user can invoke any skill); no Layer 2 → context-budget explosion and user-hunts; no Layer 3 → impersonal, no continuity.
- **Critical distinction from platform governance**: Layer 1 is **customer-facing at runtime** (the enterprise controls their own end-users), not a platform-level policy about how AEM influences its harness vendor (that is a separate governance concern — e.g. harness requirements Row 7 on AEM's influence over the platform roadmap). One is about customers → users; the other is about AEM → platform. Conflating them is a recurring source of confusion in architecture discussions.
- **Implication for harness requirements**: a harness that doesn't support Layer 1 forces the enterprise to manage skill entitlement outside the AI layer, creating enforcement gaps. Row 10 of the harness requirements draft (customer-side skill governance + entitlement) is the Layer 1 requirement specifically. The PM mandate covers all three layers but each to a different owner: governance layer = enterprise enablement PM / AI admin feature; surface layer = surface PM (Pedro for EH/AEM); user layer = design/product for the UX, and the harness for the runtime.
- **Cross-link**: [[Selection and Cross-Surface Consistency Are a PM Mandate]], [[Everything Is a Skill — the "Agent" Dissolves as a Build Unit]], [[Agentic Extensions Have a Token-Cost Hierarchy]] (Layer 2 surface scoping is also a token-budget decision).

### Dynamic Workflows — the Orchestrator Moves Off the Model (Code Coordinates, the Model Judges)

- **Source**: Paweł Huryn, *The Product Compass* — "Claude Dynamic Workflows for PMs: The Ultimate Guide" (2026-06-07). Grounded in Anthropic's dynamic-workflows / harness work (Thariq Shihipar, Sid Bidasaria, claude.com/blog); reproducible experiment repo `github.com/phuryn/dynamic-workflows-experiment`. Trigger inside Claude Code = the `ultracode` keyword (or "use a workflow").
- **Insight**: A *dynamic workflow* is a short JavaScript program Claude writes on the fly to coordinate a fleet of subagents. The model does the **judgment**; the code does the **coordination** (order, routing, stop condition, model tiering). Measured run: 113 agents, 1.95M tokens — the coordinating JS spent **zero model tokens**. The point is not that it is "more advanced" than an agent; it moves the *fragile* part (the plan) out of the model's drifting context into deterministic code.
- **The three failure modes it fixes** (a single long-running agent has all three; this is the rationale behind the consistency-layer "check" slide and any audit/review-at-scale job): **(1) Agentic laziness** — asked to review 50 items, the model reviews ~35, writes a confident summary, declares done. A `for` loop holds all 50 and runs until the array is empty. **(2) Self-preferential bias** — the model grades its own work generously, worst in judge/verify tasks. Make the judge a *separate* agent with separate context, sometimes a different model, majority vote — the bias does not survive being split. **(3) Goal drift** — over a long session the objective loses resolution (every compaction is lossy; "don't touch auth" can evaporate by turn 80). The goal lives in the script, outside the window that compacts.
- **Subagent-vs-workflow test**: use a **subagent** when the job is *one round* of parallel judgment (fan-out + merge — e.g. a competitor teardown, [[feedback_big_file_parallel_chunk_extract]]). Use a **workflow** only when stage N's output *decides* stage N+1 (route / score / filter / loop / retry / build). No chained stages → a workflow is just tokens spent on coordination you didn't need. The six recurring shapes worth naming: classify-and-act, fan-out-and-synthesize, adversarial-verification, generate-and-filter, tournament, loop-until-done.
- **Guardrail = the toolset, not a prompt**: a workflow runs unattended, so no "are you sure?" approval ever fires. "Read-only" ≠ "can't touch the disk" — a read-only agent can still carry a working shell that writes and deletes. Hand each agent an **explicit minimal tool list**, keep any mutating action in one narrow step you review, and check the allowlist instead of trusting the label.
- **Why it matters (PM)**: the PM read is *which weekly jobs become standing workflows* — set the goal once, save the procedure as a **skill**, then **schedule + `/goal` + a token budget** turns it into a recurring job that runs itself (a defined goal, a reusable procedure, a spend cap, a stop condition that is not the model's mood). Worked example (reproducible): 100 customer interviews → extract (one cheap-model agent each) → canonicalize (cluster synonyms) → score (in code) → ideate + ROI-judge → build 3 clickable HTML prototypes, ~12 min, 3/3 verified. Direct ties: the adversarial-verification pattern **is** the consistency-layer check ([[Selection and Cross-Surface Consistency Are a PM Mandate]] — LLM-as-judge against a written definition); "save the procedure as a skill" is [[Everything Is a Skill — the "Agent" Dissolves as a Build Unit]] in practice.

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

### "Do Customers Come Back?" Is the Primary Value Signal for AI Agents
- **Date identified**: 2026-03-23 (Agent Owner Alignment) + 2026-04-10 (H2 Prelim Part 3)
- **Source**: Bertrand + Apoorva + Shankari + Brian debate on agent scoring, March 23. Apoorva's adoption analysis, April 10.
- **Insight**: The most honest single signal for whether an AI agent is delivering value is whether users return. Not whether it completed the task, not whether it returned content, but: does the same user come back? Repeating users indicate realized value — the user found the interaction worth repeating. One-time users could be curious testers. Repeat users are believers.
- **Why this matters**: This was the explicit dividing line in the March 23 scoring debate — functionality (does it work?) vs customer value (do customers come back?). Both matter, but they answer different questions. Functionality is a floor. Return rate is the ceiling.
- **Connected to Apoorva's approach**: Apoorva monitors the Discovery agent daily — tracking which prompts are being used and whether users are returning. She is the only agent PM doing this consistently as of April 2026. Loni praised this explicitly at the close of the April 10 session.
- **Application**: In any AI product review, the first two questions should be: (1) what is the weekly repeat user rate? (2) what are the top 3-5 prompts that repeat users are sending? Those two numbers tell you more than any dashboard.

### Grafana vs LangFuse — Two Different Measurement Jobs
- **Date identified**: 2026-03-16
- **Source**: Agent Owner Alignment March 16, 2026. Felix, Conrad, Bertrand discussion on tool selection for AI measurement.
- **Insight**: These tools answer different questions and should not be conflated.
  - **Grafana** = usage metrics. Interaction volume, active users, returning users, weekly trends. Good for answering "are people using it?" and "is usage growing?" Does not measure quality.
  - **LangFuse** = quality measurement. LLM-as-judge scoring, prompt clustering, failure mode analysis, multi-turn conversation evaluation. Answers "is the agent doing the right thing?" and "what types of prompts are failing?"
- **The gap**: Neither tool alone is sufficient for a PM-facing agent health view. Grafana tells you how much. LangFuse tells you how well. You need both — and each team must define their own success criteria before either tool produces meaningful signal.
- **Brian's addition**: LangFuse can cluster prompts to understand which categories of prompts are going unanswered or incorrectly answered — this is a direct roadmap input. Unsupported prompt clusters = capability gaps to address.
- **Application**: When building AI measurement infrastructure, decide upfront which tool answers which question. Don't ask Grafana to evaluate quality. Don't expect LangFuse to replace usage dashboards.

### Prompt Library Monitoring as Early Adoption Signal
- **Date identified**: 2026-03-16 + 2026-04-10
- **Source**: March 16 Agent Owner Alignment (Shankari + Bertrand prompt library discussion). State of Project (Apoorva's prompt management). H2 Prelim Part 3 April 10 (Loni's closing praise for Apoorva).
- **Insight**: Daily monitoring of which prompts are actually being triggered is one of the earliest adoption signals available. It tells you what users are trying to do, not what you told them they could do. For a PM who owns an agent, the two things to track daily are: (1) which of my prompts are being used and (2) which new prompts are users writing that I didn't anticipate.
- **Apoorva's approach**: She monitors the Discovery agent's prompt usage daily and tracks repeating users. She is one of the only agent PMs doing this as of April 2026. Loni explicitly praised this behavior.
- **Prompt library ownership model**: Prompt library is cross-product (AP team owns the platform). AEM-specific prompts are each agent team's responsibility — test, preview, add, remove. This is not optional. Prompts that go unmanaged drift out of alignment with what the agent can actually do, which directly fuels the trigger failure problem.
- **Application**: Any agent PM should have a daily 5-minute prompt review routine. What got used? What got ignored? What did users ask for that isn't in the library? This is faster signal than any weekly report.

### Two-Frontend Antipattern — Never Run Two Competing UI Surfaces in Parallel
- **Date identified**: 2026-04-10
- **Source**: Loni Stark, H2 Prelim Part 3 (April 2026). Content Hub React vs EDS discussion with Apoorva.
- **Insight**: When a product team maintains two active front-end surfaces for the same capability, every downstream consequence is worse than making either choice. Loni's position: "neither one of those choices is worse than having two of them live."
- **What happens when you run two surfaces**: (1) Engineering is split — both frontends need maintenance, both fall behind. (2) Partners must build extensions for both or pick one and support half the users. (3) Demos become inconsistent — you show React, customer wants EDS behavior or vice versa. (4) Customer escalations multiply — "that feature is GA on one but not the other." (5) You've pushed an architectural decision onto the customer instead of making it yourself.
- **The right move**: Pick one. Commit. Migrate. The transition pain is finite. The two-surface pain compounds indefinitely.
- **Application**: When evaluating any surface consolidation decision, frame the question correctly: "What is the total cost of NOT deciding?" It is always higher than it looks. Loni's framing is decisive: one bad choice beats two permanent ones.

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

### Product Gap vs Quality — The Plain-Language Definition for Stakeholders
- **Date identified**: 2026-04-09
- **Source**: AEM Agent Reports Slack communication to Bertrand, agent owners, Ian, Yanira. April 9, 2026.
- **Insight**: When communicating the PM section of agent reports to a broad stakeholder audience (including non-technical), the Quality/Gap split needs plain language anchors, not tag names.
  - **Product Gap** = the agent structurally cannot handle this. It's a missing capability. Roadmap item.
  - **Quality** = the agent tried but something broke. It's a fixable failure. Engineering item.
- **Why this matters**: Agent owners, program managers, and leadership don't read tags. They read plain English. "Quality issue" and "product gap" are words they can immediately route to the right queue. Using tag-level language (unsupported, routing-issue) in external communication creates an interpretation gap.
- **Application**: In any stakeholder communication about agent report data, use these two labels. Define them once at the top. Everything after that is self-routing.

### Thread Context Changes What a Product Gap Means
- **Date identified**: 2026-04-09
- **Source**: Jim Stoklosa call + PR #24 (product-gaps-thread-context branch), April 9, 2026.
- **Insight**: A product gap row in an agent report has different meaning depending on what came before it. A user hitting "I can't do that" after one cold prompt is different from hitting it after 5 attempts at rephrasing. Thread context (up to 5 prior prompts) transforms the gap list from isolated signals into conversational evidence. It tells you whether users are exploring, frustrated, or blocked structurally.
- **Companion feature**: "Show agent answer" — displays what the agent actually said. Without this, the Quality/Gap split relies on tags alone. With it, you can read the agent's response and verify the classification. A clean "I cannot do that" is a gap. A weird hallucinated answer is a quality failure even if tagged as a gap.
- **UX consideration**: Default collapsed per row. A "show thread" toggle keeps the table readable while making detail available on demand. Always-expanded kills scannability.
- **Application**: Any agent report with a product gaps section should have thread context and agent answer as available detail. They are the difference between a report that shows what happened and one that shows why.

### Metric Definition Ownership — PM Validates, Reporting Track Owner Implements
- **Date identified**: 2026-04-23
- **Source**: Pedro's split of BVR metric work for Governance Agent, April 23, 2026. Context: 2 BVR metrics identified from Philippe review; Pedro naturally routed validation to Philippe (PM) and implementation to Lara (parallel reporting track).
- **Insight**: Defining an agent-specific metric has two distinct ownership questions. (1) **Does the definition match the capability?** — a question the agent's PM owner can answer because they know what the capability is supposed to do. "Permission audit request" must mean the thing the agent actually does, not a tangential event the instrumentation happens to fire. (2) **Can the pipeline produce this number reliably?** — a question the parallel reporting track owner can answer because they own the data flow. Conflating these into one ask to one person either overloads the PM with plumbing or overloads the reporting owner with domain calls they can't make.
- **Pattern**: For each proposed agent metric, route in two directions:
  - **Validation → agent PM owner**: Does this definition match what the capability does? Are there edge cases (retries, cancellations, partial successes) that should be included/excluded? Is the unit meaningful?
  - **Implementation → parallel reporting track owner** (Lara for Governance Agent, Felix for EPA, etc.): Can this be computed from available data? What's the sampling/granularity constraint? Does it reconcile with other metrics?
- **Why this splits cleanly**: The PM owns product definition, the reporting track owner owns measurement infrastructure. Neither wants to do the other's job. Asking the wrong person silently lowers the quality of the answer — PMs will approve anything that sounds reasonable, reporting track owners will implement anything that's technically feasible. Separate asks force each to say no where they should.
- **Application**: When defining any new agent metric, explicitly name both owners in the ask. Track them as distinct swim lanes in the Todo (Philippe Kapfer (validation) / Lara Nonino (implementation)). The same person can play both roles only if they own both the PM and reporting track — rare, and if true worth flagging.
- **Distinction from Two-Validator Pattern for Report Rollout**: Two-Validator is about validating an existing report before distribution (preparer + PM owner). This is about validating a metric *definition* before implementation. Different phase, different owners, same principle: separate conceptual validation from execution.

### Two-Validator Pattern for Report Rollout
- **Date identified**: 2026-04-09
- **Source**: Jim Stoklosa / Corey Dulimba dynamic, AEM Experience Production Agent reports.
- **Insight**: When an agent report is prepared by someone other than the PM owner (e.g. Jim prepares for Corey), two separate validation roles exist: (1) the preparer validates data accuracy and feature behavior — they know the data; (2) the PM owner validates as sign-off — they need to have seen it before it goes to leadership. These are different asks with different depths. Conflating them into one message to one person either over-asks the owner or under-validates the data.
- **Pattern**: Send detailed validation ask to preparer first. Once clean, send a lighter "does this look right to you?" to the PM owner. The owner's sign-off is what makes the visibility path credible — Bertrand won't show Loni a report the PM owner hasn't seen.
- **Application**: Map preparer vs owner for every agent report before sending any validation request.

### External Dependency Framing in H2 Planning
- **Date identified**: 2026-04-09
- **Source**: Jaclyn Eckersley / Bertrand H2 planning Slack thread, April 9, 2026.
- **Insight**: When agents are embedded across team roadmaps (not a standalone team), leadership doesn't create a dedicated agents slide. Instead, Bertrand's framing is: agents are covered within team presentations (Forms, Sites, Assets, Cloud). The only dedicated slides for agent work are for **external dependencies** — things the team depends on but doesn't control.
- **For EH, those are**:
  - AO (Agent Orchestrator 2.0) — EH Skills + MCP surface depends on AO 2.0 landing. If AO slips, EH Priority 1 slips.
  - AI Assistant — EH is the hero surface for the AEM AI Assistant prompt bar. EH is an integrator, not the builder.
- **Why it matters**: In H2 planning, these slides exist so leadership can see cross-team risk. If EH's dependency on AO or AI Assistant isn't named, it's invisible. If something slips, it looks like your roadmap failed, not an upstream miss.
- **Action trigger**: Before H2 planning closes, confirm with Bertrand what EH owns on external dependency framing. Don't build slides without alignment on ownership.

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

### Early MCP Adoption Is Developer-Tool-Led, Not AI-Assistant-Led
- **Date identified**: 2026-04-02
- **Source**: AEM Splunk MCP API Analytics Dashboard — odin/{} server, production, last 24h as of April 2, 2026.
- **Data**: 139,068 invocations in 24h. Client breakdown: Unknown 82% (113,772), Cursor 15.6% (21,617), exc_app 2.2% (2,990), Claude 0.5% (670), ChatGPT 0.01% (19). All through one MCP server (odin/{}). 99% US traffic.
- **Insight**: In the current phase of MCP adoption for AEM, developer tools (Cursor IDE) generate 30x more identified invocations than AI assistants (Claude + ChatGPT combined = 689). The dominant use case is developers integrating AEM capabilities into their coding environment, not end users asking AI assistants to act on AEM. The 82% unknown category is the most important measurement gap — identifying it could completely reshape the picture.
- **Performance flag**: P95 latency of 61 seconds on odin/{} is severe. Average is 5,791ms. One in twenty requests takes over a minute — this will limit developer adoption at scale.
- **401 pattern**: ~2,500 unauthorized errors per hour, stable over 24h. Likely misconfigured clients or token expiry — not a spike, a structural issue.
- **Application**: Don't design MCP measurement assuming AI assistants are the primary consumers. As of April 2026, developers are. Track client breakdown over time — when/if AI assistants overtake developer tools is a leading indicator of MCP reaching mainstream use.
- **Terminology note (2026-05-27 review)**: this entry uses the source dashboard's raw word "invocations." For AEM agent/MCP *reporting*, the locked counter-unit is **"Tool Calls"** (never "invocation"/"interaction") — see memory `reference_mcp_terminology`. Different surfaces: this is an external developer-tool-adoption snapshot, not the customer-facing reporting metric. Also: the 139K/24h figure is a single April-2 snapshot — treat as point-in-time, not a trend.

### Monetization Is Unresolved When Agents Replace Seats
- **Date identified**: 2026-03-26
- **Source**: Loni's Session IV (Surfaces, March 26). Haresh Kumar raised; Loni and Bertrand acknowledged.
- **Insight**: Traditional seat-based SaaS pricing breaks when agents replace human users. If one agent does the work of ten humans, and you charge per seat, your revenue collapses as adoption succeeds. MCP/skills metering (charge per capability invocation) is the emerging model but is not yet defined or tested. This is a company-level strategic gap.
- **PM implication**: Do not position agent capabilities in customer conversations using a pricing frame until internal strategy is landed. The cost conversation can kill the capability conversation before it starts (see Haresh's $500K customer story).

### Personalized Prompt Pipeline Architecture — Signal Blending Model
- **Date identified**: 2026-04-08
- **Source**: Fu Chi (AEP) 1:1s, March 25 and April 7, 2026.
- **Insight**: A real-world personalized prompt recommendation system for an enterprise AI product runs on three layers of signal, dynamically blended. In AEP's implementation for AEM: (1) user history — each user's own past prompts and topics, most weight when history is sufficient; (2) org signals — aggregate behavior of peers in the same org, used as fallback when user history is thin; (3) global signals — product-wide behavior, used when neither user nor org history is available. The blend shifts automatically based on how much signal exists for each user.
- **Pipeline structure**: Prompts collected → cleaned (remove irrelevant/out-of-scope) → converted to embeddings → K-means clustering → topic reports per app. Output: ranked CSV/table of user IDs + top relevant prompts per user.
- **Variety mechanism**: The system penalizes overly similar prompts in the ranking to avoid a narrow recommendation set. Users are exposed to both highly relevant and adjacent topics.
- **Persona limitation**: As of April 2026, the system does not model personas or detailed user profiles — only behavioral clusters (content authoring, asset focus, Cloud Manager usage). Persona modeling is planned but not yet prioritized.
- **Critical distinction — prompts vs widgets**: Prompt recommendations come from this pipeline. Widget recommendations require separate work: query the Analytics DB directly, aggregate agent usage per user, then map to widget suggestions. These are two different data flows with two different outputs.
- **Application**: When designing a personalization layer for an AI product surface, separate the prompt recommendation problem from the widget/navigation recommendation problem early. They have different data sources, different models, and different engineering paths.

### Tag Taxonomy Design for AI Agent Measurement
- **Date identified**: 2026-04-08
- **Source**: Tag review of suggested_tags.csv with Felix Delval, April 8, 2026.
- **Insight**: Tag taxonomies for AI agent measurement fail in predictable ways. The common failure modes, and their fixes:
  1. **Duplicate intent** — multiple tags with identical descriptions (e.g., Check-status, View-status, Progress-tracking all meaning "check translation status"). Produces noise, not signal. Fix: consolidate to one canonical tag per intent.
  2. **Object name vs intent name** — tags named after data objects (Languages, Locale) rather than what the user was trying to do. Misleads analysts and makes filtering unreliable. Fix: name tags by user intent, not by the object the user mentioned.
  3. **Overpromising scope** — tag names that imply a broader meaning than the description provides (e.g., asset-lifecycle implies creation + versioning + archiving, but description only covers expiration). Fix: align name to actual scope, or broaden the scope to match the name.
  4. **Naming convention mismatch** — mixing Title-Case and lowercase-kebab in the same system makes grouping, filtering, and display inconsistent. Fix: normalize to one convention. lowercase-kebab is standard for machine-readable tags.
  5. **Tag names as sentences** — long descriptive names (e.g., search-result-used-in-next-interaction) are unsearchable and unwieldy. Fix: compress to 2-3 word concepts (chained-search, search-result-reused).
  6. **Shadow tags** — a broad catch-all tag that overlaps with multiple specific tags. The catch-all gets applied first and the specific tags get underused. Fix: either remove the catch-all or make it the parent in a hierarchy.
- **Application**: Before publishing a tag taxonomy for cross-agent measurement, run it through these six failure modes. If any apply, fix before rollout — retroactive taxonomy cleanup is expensive.

### Auth-Walled Hosting Blocks PM Validation Workflows, Not Just Agent Consumption
- **Date identified**: 2026-04-08
- **Source**: Greg Klebus 401 error on Content Optimization report (April 8, 2026). Chrome Sidekick plugin required.
- **Extension of**: "Auth-Walled Hosting Is Incompatible with Agent-Consumable Reports" (2026-03-31)
- **New signal**: The auth-wall problem is not limited to agent consumption. It blocks human PM validation workflows too. When agent owners can't access the report to validate their data, the PM review cycle stalls. In this case, Sidekick is required to authenticate — a plugin most PMs don't have installed. Every agent owner Pedro tried to loop in for validation hit this wall.
- **Application**: Report hosting requirements must be validated with the intended audience before distribution starts. "Can a script fetch this URL?" is the agent test. "Can any PM with a browser access this without a special plugin or account?" is the human test. Both must pass before a report goes broad.

---

## Personalization Architecture for AI Surfaces

### Cascading Signal Model — User → Org → Global Fallback Solves Sparse Data
- **Date identified**: 2026-04-20
- **Source**: Fu-Chi Shih's AEM personalized prompt recommendation POC. April 20 joint sync with Pedro + Eugene.
- **Insight**: Personalization systems for AI surfaces fail most often not on the algorithm but on the data. Most users don't have enough individual history to rank anything meaningful — especially new users, low-usage orgs, or users in roles that only touch the product occasionally. The fix is a three-level signal cascade: **user-level signals (primary) → org-level signals (fallback) → global signals (universal fallback)**. Never fail closed. Never return a cold blank.
- **How it works**: For each recommendation target (a prompt, a widget, a skill), the system first checks the user's own history. If the user has enough signal, use it. If not, fall back to their org's behavior — how do other users in this company use the product? If the org is too new or sparse, fall back to global signals — how do all AEM customers behave? Every user gets a ranked list regardless of their history state.
- **Why it matters for PM thinking**: This reframes "personalization requires profiles" — it doesn't. It requires structured fallback. Profiles become useful when the user-level signal is sparse AND the org-level signal is ambiguous: the profile is a deterministic tiebreaker. Profile is *augmentation* to this model, not a prerequisite for it.
- **Application**: For any AI personalization roadmap, do not plan "collect enough signal to personalize by user." Plan "cascade from best-available signal to universal fallback." The system ships on day one with global-only signals and improves over time as user and org data densifies. This also makes it cheap to expand into new surfaces — the cascade works even when a surface has zero per-user data yet.
- **Connected**: EH Priority 3 (Customer Profiling) is the deterministic augmentation layer on top of this cascade. The cascade handles "what to show when we know nothing." Profiling handles "what to show when we know role but not history."

### Two-Column Prompt Design — Display Label + Execution Prompt
- **Date identified**: 2026-04-20
- **Source**: Eugene Bannykh, April 20 Fu-Chi sync. Prompt card UX problem.
- **Insight**: Suggested prompts have a fundamental UX conflict: prompts that work well with an AI tend to be long and verbose (context, constraints, output format). Prompts that display well on a card need to be short (a title a human can scan). Most prompt libraries pick one side of this — either verbose-and-unreadable or short-and-underperforming. The fix is a two-column schema: **display label** (human-readable, short, scannable) + **execution prompt** (verbose, contextual, what actually goes to the model). User clicks the label, system sends the execution prompt.
- **Generation path**: The execution prompt is the authored artifact. The display label can be LLM-generated as a summarization step — cheap, consistent, reproducible. No PM writes two versions; they author the execution prompt and the system summarizes.
- **Why this matters**: Without it, every AI surface that shows suggested prompts either trains users to expect short prompts (bad results) or confronts them with a wall of text (low engagement). Two columns resolves the conflict structurally.
- **Application**: Any prompt library schema should include display label as a first-class field alongside the execution prompt. Both stored, both retrievable. Retrofit is cheap if the library is centralized. Expensive if prompts are hardcoded across multiple surfaces — which is itself an anti-pattern (see Prompt Library as Contribution Surface below).

### Prompt Library as Contribution Surface — Centralized Library, Distributed Ownership
- **Date identified**: 2026-04-20
- **Source**: Fu-Chi + Eugene sync. Eugene: "prompts should not be hardcoded in EH." Fu-Chi: today pulls from wiki, wants prompt library integration.
- **Insight**: In an ecosystem with many AI agents and many surfaces, the prompt library should be treated as a shared contribution surface — one centralized library, distributed ownership (each agent team owns their own prompts, tests them, adds/removes them). Surfaces (EH, AI Assistant right rail, AEP recommendation engine) all consume the same library. PMs self-serve updates; the personalization layer picks them up automatically. No hardcoded prompts in any surface.
- **Why this works**: (1) A single source of truth means an agent team's prompt improvement shows up everywhere immediately. (2) Surfaces don't fight over prompt authorship. (3) The personalization layer is decoupled from prompt authoring — it consumes whatever the library holds, ranks it against user signals. (4) New surfaces can spin up against the same library without requiring prompt duplication.
- **Where it breaks**: If the prompt library owner (cross-product platform team) doesn't expose a clean read API, every surface falls back to wiki/hardcoded lists. That's the EH state today. This is the contribution model pattern applied to prompts — same governance principles (ownership split, consumer teams don't build for others, quality gate on the platform side) apply.
- **Application**: When designing any AI surface that shows prompts, the default should be "source from the shared prompt library." If no such library exists, the product question is not "what prompts should we ship" — it's "who builds the library and what's the access API?" That's a platform-level ask, not a surface-level ask.

### User Feedback as Ranking Signal — ✓/✗ to Densify Sparse Personalization
- **Date identified**: 2026-04-20
- **Source**: Eugene Bannykh, Fu-Chi sync. "Our algorithm is only as good as our signals are."
- **Insight**: When the user-level signal is sparse (the cascade's primary problem), an explicit feedback UI can densify it cheaply. A per-recommendation ✓/✗ button turns passive exposure into an active signal — the user tells the system what's relevant to them. This doesn't replace behavioral signals (what prompts they actually use); it complements them by capturing relevance-without-action (user saw it, decided it wasn't for them, said so).
- **Design constraint**: The feedback must require zero friction to be useful. A modal, a confirmation, or a reason-why-field kills the signal. A single click, persisted silently, is the only form that works.
- **Why this matters**: Sparse-data personalization systems often sit on a chicken-and-egg problem — they need behavior to rank well, but users don't engage until ranking is good. Feedback bypasses the loop. Even 5% of users clicking ✗ on irrelevant prompts gives the ranker information it couldn't get any other way.
- **Application**: Any surface with suggested content backed by a ranking system should consider a lightweight feedback UI. Track whether feedback actually changes rankings — if the system ignores it, users will stop clicking and the signal dies. Closing the loop (showing "based on your feedback, here's what we changed") isn't necessary; the ranker just needs to use the signal.
