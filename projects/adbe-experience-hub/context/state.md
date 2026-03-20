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

Roughly 40 to 50 percent of agent responses are poor or unsupported today. Metrics for agent quality are not standardized across Adobe. Grafana covers usage but not quality. LangFuse is being evaluated for quality measurement. This must be resolved before driving adoption at scale.

## Tech Notes

- Custom widget framework (not Pueblo — chosen because Pueblo lacked needed customization)
- Navigation uses Assets navigation pattern, not Unified Shell
- Adobe Analytics for adoption tracking (active users, navigation actions, AI prompt usage, announcement clicks)
- Prompt Library dependency was on an old version, updated recently, needs redeployment
