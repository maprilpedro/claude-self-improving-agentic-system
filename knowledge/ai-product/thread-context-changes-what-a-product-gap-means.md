# Thread Context Changes What a Product Gap Means

_Section: Agent Measurement Infrastructure — part of `ai-product/`; router = README.md._
- **Date identified**: 2026-04-09
- **Source**: Jim Stoklosa call + PR #24 (product-gaps-thread-context branch), April 9, 2026.
- **Insight**: A product gap row in an agent report has different meaning depending on what came before it. A user hitting "I can't do that" after one cold prompt is different from hitting it after 5 attempts at rephrasing. Thread context (up to 5 prior prompts) transforms the gap list from isolated signals into conversational evidence. It tells you whether users are exploring, frustrated, or blocked structurally.
- **Companion feature**: "Show agent answer" — displays what the agent actually said. Without this, the Quality/Gap split relies on tags alone. With it, you can read the agent's response and verify the classification. A clean "I cannot do that" is a gap. A weird hallucinated answer is a quality failure even if tagged as a gap.
- **UX consideration**: Default collapsed per row. A "show thread" toggle keeps the table readable while making detail available on demand. Always-expanded kills scannability.
- **Application**: Any agent report with a product gaps section should have thread context and agent answer as available detail. They are the difference between a report that shows what happened and one that shows why.
