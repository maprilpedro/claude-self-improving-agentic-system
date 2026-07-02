# Two-Column Prompt Design — Display Label + Execution Prompt

_Section: Personalization Architecture for AI Surfaces — part of `ai-product/`; router = README.md._
- **Date identified**: 2026-04-20
- **Source**: Eugene Bannykh, April 20 Fu-Chi sync. Prompt card UX problem.
- **Insight**: Suggested prompts have a fundamental UX conflict: prompts that work well with an AI tend to be long and verbose (context, constraints, output format). Prompts that display well on a card need to be short (a title a human can scan). Most prompt libraries pick one side of this — either verbose-and-unreadable or short-and-underperforming. The fix is a two-column schema: **display label** (human-readable, short, scannable) + **execution prompt** (verbose, contextual, what actually goes to the model). User clicks the label, system sends the execution prompt.
- **Generation path**: The execution prompt is the authored artifact. The display label can be LLM-generated as a summarization step — cheap, consistent, reproducible. No PM writes two versions; they author the execution prompt and the system summarizes.
- **Why this matters**: Without it, every AI surface that shows suggested prompts either trains users to expect short prompts (bad results) or confronts them with a wall of text (low engagement). Two columns resolves the conflict structurally.
- **Application**: Any prompt library schema should include display label as a first-class field alongside the execution prompt. Both stored, both retrievable. Retrofit is cheap if the library is centralized. Expensive if prompts are hardcoded across multiple surfaces — which is itself an anti-pattern (see Prompt Library as Contribution Surface below).
