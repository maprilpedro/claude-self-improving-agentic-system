# Auth-Walled Hosting Blocks PM Validation Workflows, Not Just Agent Consumption

_Section: AI Product Risks — part of `ai-product/`; router = README.md._
- **Date identified**: 2026-04-08
- **Source**: Greg Klebus 401 error on Content Optimization report (April 8, 2026). Chrome Sidekick plugin required.
- **Extension of**: "Auth-Walled Hosting Is Incompatible with Agent-Consumable Reports" (2026-03-31)
- **New signal**: The auth-wall problem is not limited to agent consumption. It blocks human PM validation workflows too. When agent owners can't access the report to validate their data, the PM review cycle stalls. In this case, Sidekick is required to authenticate — a plugin most PMs don't have installed. Every agent owner Pedro tried to loop in for validation hit this wall.
- **Application**: Report hosting requirements must be validated with the intended audience before distribution starts. "Can a script fetch this URL?" is the agent test. "Can any PM with a browser access this without a special plugin or account?" is the human test. Both must pass before a report goes broad.

---
