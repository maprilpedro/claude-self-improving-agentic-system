# Platform Contribution Model with Quality Gate

_Section: Anti-Patterns — part of `patterns/`; router = README.md._
- **Date identified**: 2026-03-31
- **Observations**: (1) Experience Hub had 15+ teams requesting features from 2 engineers — unsustainable service desk dynamic. (2) Security was the only team that contributed back — proved self-service is possible. (3) EH Evolution proposal explicitly separates what EH gates (design, metric, lifecycle, testing) from what contributing teams own (build, data, monitoring).
- **Pattern**: Small platform teams cannot scale by building everything for consuming teams. The right model: define a contribution framework where consuming teams own their own features, and the platform team owns the quality bar. Platform team provides standards, component library, and approval gate. Consuming teams provide the build and the maintenance.
- **Three conditions for it to work**: (1) A published standard — teams need to know what "good" looks like before they build. (2) A gate with teeth — platform PM must be willing to reject contributions that don't meet the standard. (3) At least one proof point — one team that successfully contributed validates the model for others. Security in EH is that proof point.
- **What the gate covers**: Design standards, conversion metric, time-to-live (TTL) commitment, test evidence.
- **When it fails**: When the platform PM says yes to everything to avoid friction. The surface becomes noise, users stop trusting it, and the original problem (too many asks, too few engineers) is worse than before.
