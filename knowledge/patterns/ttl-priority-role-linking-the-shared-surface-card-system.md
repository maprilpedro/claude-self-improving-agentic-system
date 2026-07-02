# TTL + Priority + Role-Linking — The Shared Surface Card System

_Section: Anti-Patterns — part of `patterns/`; router = README.md._
- **Date identified**: 2026-03-31
- **Observations**: (1) EH announcement widget managed manually — teams asked EH engineers to create/update cards. (2) Experience Hub voice note (Pedro, March 30): proposed automated card creation with TTL, priority ranking, and role-linked display. (3) Shankari's 4-week rule enforced manually — TTL automates the enforcement.
- **Pattern**: In any shared surface where multiple teams want to publish content (announcements, cards, prompts, widgets), a four-mechanic system prevents the surface from becoming noise: (1) Self-service creation — teams submit, PM approves; (2) Priority ranking — set by platform PM, not contributing team; (3) Time To Live — every item expires automatically unless renewed with performance data; (4) Role-linking — items display only to the profiles they're relevant for.
- **Why this works**: It turns a human governance process (Shankari manually enforcing the 4-week rule) into an automated one. The PM's role shifts from "enforcer of expiry dates" to "setter of the system rules." Teams know the rules upfront and self-select accordingly.
- **Connection to contribution model**: This is the contribution model applied to content publishing. The same principles (teams own, platform gates) apply to both widgets and cards.
