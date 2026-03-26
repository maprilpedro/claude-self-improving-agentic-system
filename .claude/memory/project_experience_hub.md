---
name: AEM Experience Hub project context
description: Full context on the Experience Hub project - what it is, who owns it, team, org, state, risks, and SD angle
type: project
---

AEM Experience Hub is the unified home screen / landing page for AEM Cloud Service at experience.adobe.com. Launched August 2024. Previously named AEM Home and AEM Launchpad. Not a replacement for existing AEM UIs. An action-oriented entry point that surfaces the right tools per persona.

**Current PM:** User (took over from Shankari in March 2026)

**Why:** Shankari is on the user's team (peer PM, not a direct report) and is moving off the project. User is taking over a high-visibility project directly watched by Bertrand (Senior Director PM, user's boss) and Loni (VP Product Management for AEM).

**Team:**
- Shankari: peer PM on the team, currently still driving Summit deliverables before handing off fully
- Sorin: lead engineer (key person, strong technical judgment)
- Open headcount: backfill for Mihai who left (hiring in progress)
- Eugene: UX Designer, US timezone, reports to Silvia Mulet
- Silvia Mulet: UX Manager, leads UX team on Experience Hub. Booking time with Pedro and Eugene to review current UX projects and next steps.
- Was 3 engineers, now 2

**Org:**
- User → Bertrand (Senior Director PM) → Loni (VP PM for AEM)

**Top priority for 2026:** Integrating AEM agents into Experience Hub. Agent prompts surfaced inside Experience Hub via the Prompt Library Platform. Seven agents in total as of March 2026: Experience Production (CR), Governance (Bertrand/CR), Discovery (Apoorva), Onboarding (Nick), Modernization (Gabriel/Mike), Development/EDA (Brian Chaikelson, reports to Bertrand — pipeline troubleshooting is a skillset within it), Content Optimization (Apoorva).

**Agent Owner Alignment meeting (2026-03-23):**
- Summit readiness round robin: EPA has blockers (file upload, context awareness, bugs). Interoperability demo between EPA and Discovery uncertain — may be dropped from Summit.
- Scoring debate: current agent value/functionality scoring is subjective. Bertrand, Apoorva, Shankari, Brian agreed to formalize metrics. Key distinction needed: functionality vs actual customer value (repeat usage, stickiness).
- LangFuse: Brian proposed prompt clustering via Jupyter notebooks to understand unsupported/incorrectly answered questions.
- AMS risk: managed services customers will ask about agent availability at Summit. PMs need roadmaps ready.
- Tracing work stream must close by end of week.

**Loni's AEM PM Virtual Working Session I — Agents (2026-03-23):**
- Loni convened a first-principles session on agent strategy. Small senior group: Pedro, Bertrand, Conrad, Cedric, Corey, Michael, Ian.
- A2A is dead. Confirmed by Conrad and not contested. MCP + API won as integration model.
- No agent loop in current architecture. Agents route, they don't reason. AO 2.0 adds reasoning loops — May at earliest, June-July realistic (Cedric). This is the structural root cause of the 40-50% failure rate.
- Seven agent categories are "made up" per Loni. They reflect PM intuition, not customer reality. Will evolve based on analysis of 1200 real customer questions (Corey holds this data).
- No documented personas or jobs-to-be-done for any agent (Michael raised this, Conrad confirmed from log analysis).
- Conrad: security patterns too hot to advance — LLM access needs to be separated from certain data first.
- Durable themes replace brittle 6-month roadmaps. Loni's frame: AEM moving from content management to context management.
- Pedro contributed at 58:25: persona-based interaction model — technical users via MCP/API, UI-based users (e.g. security) via guided product surfaces. Conrad validated this in front of Loni.
- Next steps Loni named at close: (1) Corey analyzes 1200 questions, (2) Conrad documents agent patterns, (3) first-principles architecture review separate from AO limitations.
- Note: "CR SJ ET15/Kettering VC" in the transcript is a conference room mic. All those lines are Loni speaking.

**Loni's AEM PM Virtual Working Session IV — Surfaces (2026-03-26):**
- Small senior group: Loni, Pedro, Bertrand, Corey Dulimba, Haresh Kumar, Arun Taneja.
- Project 42: launched July 2025 as a strategic map (not a project). Core assertion: content management becomes context, for agents and humans. Explicitly said different experiences are needed for agents vs. humans. Agents were originally described at functional/business levels; industry has since broken them into skills. Pedro should reference Project 42 by name in all strategic documents.
- Hero Surfaces / "Times Square" concept: Loni's directive to identify canonical human UIs to drive people toward, run PLG on, and ensure are callable from other contexts. Experience Hub is the natural candidate. Action item left open — Pedro should own this definition.
- "Talk to the CMS": Corey surfaced that users want an administrative agent for bulk actions (find pages, delete launches, etc.) via conversation instead of Groovy scripts. Open chat box is doing real discovery but also generating frustration via hallucinations. Recommendation: scope-limit, be explicit about what the agent cannot do.
- A2A nuance: in Session I (March 23), A2A was "dead." In Session IV, Loni noted Google released A2A v1.0. Two narrow real use cases: (1) security/trust gradients — trusted write agent called by untrusted flexible agent; (2) specialized agent chaining. For AEM customers, Skills/MCP remains the primary path. Do not say "A2A is dead" flatly in any communication.
- AEM velocity constraint: Bertrand confirmed monthly release cycle is physics. Any MCP/API capability addition must go through release validation. DA (Document Authoring / Edge Delivery) is the confirmed future stack, proven with early customers. Long adoption curve, no migration button.
- Modernization agent field risk: Haresh Kumar shared that a major customer (carpet company in Atlanta) rejected ~$500K in additional licensing to access new capabilities. Modernization agent story is fragile — enterprise-scale evidence missing.
- Monetization gap: seat-based pricing doesn't work when agents replace seats. MCP/skills metering model undefined. Haresh + another stakeholder working through non-seat-based model. Do not raise externally until internal strategy is landed.
- Pedro's visibility: Pedro's point about avoiding scattered UIs was echoed by Loni in the session synthesis. Repeated cross-session credibility signal.
- CAPS action item: Arun Taneja structuring surfaces/LLM apps for CAB/CAPS customer discussion. Needs slides/POV first. Opportunity for Pedro to contribute and gain cross-org visibility.

**Felix Delval's EPA measurement infrastructure (confirmed 2026-03-25 1:1):**
Felix built a full Python reporting platform — not a skill. Repo: `/Users/pedrofer/GitHub/aem-agent-reports`.

**Architecture:** CSVs → loader.py (normalize) → metrics/funnels/journeys/trends modules → LLM insights (Claude Haiku via Bedrock, YAML fallback) → Jinja2 HTML with Chart.js. Generates reports/week_YYYYMMDD/[agent].html + index.html.

**Already in the system:**
- Technical Success Rate AND Value Realization Rate — both first-class metrics
- Funnel per capability (Interactions → Customers → Users, SR%, VR%, WoW)
- Customer journeys: top 10 orgs, pattern mining, sample prompts
- 6-8 week trends, retention rate, new/repeated users, adoption blockers
- LLM insights (signals/watch/action needed) with YAML fallback — report always generates

**6 agents already configured in agents.yaml:** Discovery, EPA, EDA, Content Optimization, Governance, Experimentation. Adding an agent = 2 lines YAML + CSV data. It's a data problem, not an engineering problem.

**Mandatory + custom dashboard concept already in design:** standard HTML template (mandatory) + per-agent YAML insights (custom).

**Gap vs Bertrand's ask:** Distribution channel breakdown (playground/try-before-you-buy/SKU/co-innovation) is not yet in the system. Everything else is.

**For EGA extension:** Governance Agent is already configured. Missing = EGA interaction CSVs in the right format. Question for Philippe: can EGA data be exported to match loader.py schema?

**Data team role (Shweta/Jean-Claude):** Feed clean data into the pipeline from the data platform. Felix has done the design work — they don't need to rebuild it.

Pedro and Felix have a daily working session (as of 2026-03-26). Felix is the primary technical collaborator on agent reporting standardization.

**Prompt Library Platform:** Backend infrastructure for curating and serving AI prompts. Admin UI + end-user UI embedded in AI Assistant. Supports role filtering, similarity detection, B2B/B2C detection. PM: Cole Connelly. EM: Joshua Hailpern.

**Key risks as of March 2026:**
1. TJ's Adobe Analytics dashboard at risk of deletion (TJ left the company, account deactivation pending). Urgent.
2. Vision-reality gap: employee meeting demo showed vision mock, not actual product. Multiple stakeholders have false expectations.
3. Capacity: 2 engineers vs 15+ stakeholder teams with competing asks.
4. No contribution model: teams ask for features but don't build them.
5. Agent quality: ~40-50% bad responses, no standardized quality measurement across Adobe. Confirmed in Agent Owner Alignment meeting 2026-03-17 (file: "Agent Owner Alignement 20260316.md" in Obsidian vault). Root causes: no defined success criteria per agent, LangFuse piloted by some teams only (not centralized), Grafana covers usage not quality, Prompt Library has no review/approval process before prompts reach customers, conversations derail and users don't return. User flagged this to Horia (CXO Skills Catalog owner) with a quality caveat for AEM Content skills 27-35 and a wiki note. This is a known risk that could undermine Summit credibility if "A = Available" is interpreted as production-ready.
6. Unified Shell alignment: boundary between Experience Hub and Unified Shell still unclear.

**Immediate context (March 2026):**
- Summit is ~1 month away. Shankari driving Summit deliverables. User staying in the backseat.
- Post-Summit: user sets direction, builds roadmap with Sorin, resets stakeholder expectations.
- 30-60-90 day plan exists in Obsidian vault.

**Obsidian vault folder:** /Users/pedrofer/Library/CloudStorage/GoogleDrive-maprilpedro@gmail.com/My Drive/ObsidianVault/020 Professional/Adobe/Projects/2026/Experience Hub

**Slack channels:** #experience-hub, #experience-hub-ai-assistant, #aem-home-platform-team, #aem-home-core-team, #temp-experiencehub-dxue, #dx-product-measurement, #tmp_aem_missing_prompt_library

**Product history (Sep 2024 - Nov 2025, from #aem-home-core-team Slack):**
- GA launched August 26, 2025. Named "AEM Launchpad" briefly (Nov 2024), then renamed Experience Hub.
- Roles → Intentions shift decided by Bertrand in December 2024. Navigation labels moved from role names (Content Author, Developer) to intention-based (Authoring content, Building experiences, Writing code, Security). Wiki: Launchpad Intent vs Role Matrix.
- User previously agreed with @adulvac to place Security widget at top for Security & Dev persona. Shankari disagreed. Unresolved.
- Loni signal (Aug 16, 2025): "Great to see Sites Optimizer connected into Experience Hub. Good we are trying to look at in-product nudge for PLG." She watches preset defaults closely.
- Loni asked for specific GA date (not just "summer") in May 2025, and asked "What is our plan to redirect users to Experience Hub?" — no clear answer on file.
- A/B test result (Nov 2025): SIMPLE onboarding variant won decisively (17.9% CTR vs 0.36%). Decision to roll to 100%.

**Known open problems (post-GA, unresolved as of Nov 2025):**
1. Value proposition not clear to users. Shankari's own diagnosis: "The value of Experience Hub is not presented upfront to users."
2. Multiple entry points (Experience Home, Experience Hub, Cloud Manager, bookmarks) causing navigation confusion. No migration/redirect plan confirmed.
3. Environments widget only shows after user logs in once — defeats the wayfinding purpose for new users. Bertrand flagged: "We're going to miss big time on the whole point of the widget."
4. Recents widget inaccurate. Customer (Mark Schulz) flagged directly: "Recents widget needs some love. It's not accurate."
5. Security & Compliance features not discoverable. Even asset librarians can't find them.
6. Left nav structure unresolved post-Summit. Sorin flagged: "There are concerns about lack of structure and categories seeming random."
7. Bounce rate analytics accuracy questioned. "Looks fishy" — under investigation, no resolution on file.
8. Trial environment conflict: enabling Experience Hub breaks Headless Trial experience.

**CXO Agentic Skills Catalog (March 2026):**
- User flagged to Horia that AEM Content skills 27-35 are marked "A" but agent quality is ~40-50% failure rate with no standardized measurement. Risk of overstating readiness to Amit.
- Ian Boston (principal architect) raised a bigger concern: AO 2.0 is a completely new architecture. Teams would need to port existing agent code to ship real skills — significant engineering work, not just writing SKILL.md. 4 weeks to Summit is tight.
- Developer Agent (EDA) has no row in the catalog. User flagged to Brian Chaikelson and Bertrand.
- User asked Shankari for clarity on what specifically she needs reviewed/updated.

**Hero Surfaces one-pager (drafted 2026-03-26, not yet sent):**
Draft saved at: `AEM Experience Hub - Project Folder/Hero Surfaces - Experience Hub as the Times Square for AEM.md`. Waiting for Pedro's review before sending to Bertrand. Goal: get Bertrand's alignment + his name on it, then bring to Loni's next session. Three asks to Bertrand: (1) confirm EH is the right candidate, (2) align on "callable from other contexts" requirement, (3) permission to bring to Loni with his name on it.

**How to apply:** When working on any Experience Hub task, start with this context. The user is new to the project, ramping up, and trying to establish credibility with Bertrand and Loni. Every artifact should help close the vision-reality gap or advance the agent integration priority.
