# Auth-Walled Hosting Is Incompatible with Agent-Consumable Reports

_Section: Agent Measurement Infrastructure — part of `ai-product/`; router = README.md._
- **Date identified**: 2026-03-31
- **Source**: Pedro/Claude analysis of Bertrand's "agents will consume this data" ask, March 31.
- **Insight**: When a senior stakeholder says "agents should be able to consume this data," they are describing a technical constraint on hosting. Auth-walled systems (SharePoint, internal document stores, anything requiring SSO login) break agent consumption because an automated agent hitting the URL gets an auth wall, not data. This kills the machine-readable use case entirely, even if the URL is stable.
- **The right default**: Static hosting with no auth (GitHub Pages, public CDN, or internal open static host). If the data is sensitive, token-based access is acceptable — but not full OAuth/SSO flows that require browser interactions.
- **Application**: When evaluating hosting options for any report or data artifact that agents need to read, filter out any option that requires a browser-based login. Ask: "Can a script fetch this URL without human authentication?" If no, it doesn't qualify.
