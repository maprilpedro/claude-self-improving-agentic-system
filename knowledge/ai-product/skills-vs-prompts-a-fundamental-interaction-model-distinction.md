# Skills vs Prompts — A Fundamental Interaction Model Distinction

_Section: AI Product Risks — part of `ai-product/`; router = README.md._
- **Date identified**: 2026-03-31
- **Source**: Pedro's voice notes (March 30); Bertrand brief drafted March 31; Agent Owner Alignment March 20.
- **Insight**: Prompts and skills are not the same thing, and surfacing them interchangeably in an AI product surface is a structural mistake.
  - **A prompt** is an open-ended intent expression. It invites the user to try something. It says nothing about whether the agent can reliably execute it.
  - **A skill** is a scoped, tested, packaged workflow. It communicates what the agent can do, what it cannot, and what a successful outcome looks like.
- **Why this matters for surface design**: A surface that shows prompt suggestions against agents with a 40-50% failure rate trains users to expect things the product can't reliably deliver. Every hallucinated or out-of-scope response after clicking a suggested prompt is a trust hit. Skills change the contract — users interact with defined capabilities, not an open box.
- **The evolution**: Prompt suggestions → skills discovery → skills + MCP connection awareness. Each step narrows the gap between what's surfaced and what's reliably executable.
- **Design implication**: The right interaction surface for a maturing AI product shows: (1) what skills are active for this user's license and environment; (2) what MCP connections are live (what tools/data the agent can reach); (3) what it cannot do. Not a generic grid of prompts.
- **Application**: When designing or evaluating any AI assistant surface, ask: are these suggestions grounded in what this system can actually reliably do for this user? If not, you are surfacing promises you can't keep.
