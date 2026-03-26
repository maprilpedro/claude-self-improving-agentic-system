# State of the Project — March 2026

## What Exists Today

Experience Hub is a working landing page at experience.adobe.com. It has widgets, recents, quick actions, product announcements, and role-based navigation. An AI assistant is integrated with product knowledge Q&A and a support agent. Controlled adoption experiments are running with small user groups. Adobe Analytics tracking is live.

That is the real product. Not more.

## What People Think Exists

The employee meeting demo showed a vision mock from last year, not the actual product. Different teams have formed different expectations based on that demo and individual conversations with Shankari.

Some stakeholders believe personalization is live. Some believe the AI assistant is production-ready. Some believe their feature requests are already on the roadmap.

The gap between perception and reality is the biggest risk on this project.

## History

- 2024: Project started as "AEM Home" (also called "AEM Launchpad")
- August 2024: Launched as Experience Hub
- 2025: Mostly monitoring, controlled experiments, AI agent case support. Selected at G8 in the alphabet program.
- Early 2026: AI agents enter early access. Prompt integration becomes the top priority.
- March 2026: Shankari moves out. Pedro takes over.

## What's Working

- Controlled adoption experiments with real measurement and weekly reviews
- Adobe Analytics tracking is rigorous and drives decisions
- Engineering quality is high. Sorin and the team care about doing it right.

## What's Not Working

- No clear product definition for 2026. No shared document saying what Experience Hub will and will not be this year.
- No stakeholder intake process. Requests arrive via Slack and side conversations.
- Vision-reality gap. Erodes credibility every month it goes unaddressed.
- Abandoned POCs. Multiple efforts started, partially built, never formally killed. They sit in the codebase and in people's expectations.
- No contribution model. Teams ask for features but don't build them. Experience Hub is treated as a service team.
- Unified Shell alignment is broken. Overlapping concerns around navigation and widgets, no clear boundary.

## Agent Quality Issue

Roughly 40 to 50 percent of agent responses are poor or unsupported today. Metrics for agent quality are not standardized across Adobe. Grafana covers usage but not quality. LangFuse is being evaluated for quality measurement — Brian Chaikelson proposed prompt clustering via Jupyter notebooks to understand unsupported queries (Agent Owner Alignment, March 23, 2026). Current value/functionality scoring across agents is subjective. Agreed in March 2026 to formalize metrics distinguishing functionality (does it work?) from customer value (do customers come back?). This must be resolved before driving adoption at scale.

Root cause confirmed in Loni's working session (March 23, 2026): the current agents do not reason — they look for a direct path to a solution and fail if the path breaks. This is an architecture ceiling, not a prompt quality problem. AO 2.0 introduces agent loop reasoning that resolves this, but production availability is May at earliest, June-July more realistic (confirmed by Cedric Huesler). Driving adoption before AO 2.0 lands risks compounding the quality perception problem.

## Architecture Direction (from Loni's Working Session, March 23, 2026)

Loni convened a first-principles working session on agents with a small senior group (Bertrand, Conrad, Cedric, Corey, Pedro, Michael, Ian). Key conclusions:

- **A2A — nuanced (updated Session IV, March 26).** In Session I, Conrad confirmed A2A never materialized for AEM customers — MCP + API won. In Session IV, Loni updated: Google released A2A v1.0 and there are two narrow real use cases: security/trust gradients (a trusted write-capable agent called by a more flexible but untrusted agent) and specialized agent chaining. For AEM customers, Skills/MCP remains the primary path. Do not use "A2A is dead" in communications. Correct framing: A2A has narrow real use cases; Skills and MCP are right for most AEM scenarios.
- **Agent loop reasoning.** Multi-agent coordination via reasoning loops is the working pattern. AO 2.0 is built on this. Cedric confirmed agent loops work significantly better than discrete A2A orchestration.
- **Skills are the right direction.** AO 2.0 is skills-based and composable. SKILL.md files are becoming the standard for portability. Conrad and the architects are reworking agents toward smaller, more API-based skill sets with MCP for experience surfaces.
- **The seven agent categories are not grounded in customer reality.** Loni said this explicitly. They reflect PM intuition about jobs-to-be-done, not observed customer behavior. They will evolve as the 1200 real customer questions (held by Corey) are analyzed.
- **Durable themes replace rigid roadmaps.** Loni reframed roadmap philosophy: no more brittle 6-month plans. Directional themes that hold while features evolve underneath. Example: AEM moving from content management to context management.

Next steps Loni called out at close of session:
1. Corey analyzes the 1200 customer questions — separate what people say they want from what they're observed doing.
2. Conrad documents agentic design patterns in writing.
3. Separate AO limitations from first principles architecture, then design from first principles.

## Seven Agents (as of March 2026)

| Agent | PM Owner | Summit Status |
|---|---|---|
| Experience Production | CR | In progress — blockers: file upload, context awareness, bugs |
| Governance | Bertrand / CR | Functional gaps, customer adoption issues |
| Discovery | Apoorva | On track — interoperability with EPA uncertain |
| Onboarding | Nick | Not yet in production |
| Modernization | Gabriel / Mike | On track — Crosswalk, Figma support |
| Development (EDA) | Brian Chaikelson | Public beta upcoming, pipeline troubleshooting + AI IDE |
| Content Optimization | Apoorva | On track |

## Tech Notes

- Custom widget framework (not Pueblo — chosen because Pueblo lacked needed customization)
- Navigation uses Assets navigation pattern, not Unified Shell
- Adobe Analytics for adoption tracking (active users, navigation actions, AI prompt usage, announcement clicks)
- Prompt Library dependency was on an old version, updated recently, needs redeployment
