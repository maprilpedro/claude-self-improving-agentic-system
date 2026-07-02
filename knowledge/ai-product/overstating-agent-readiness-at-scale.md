# Overstating Agent Readiness at Scale

_Section: AI Product Risks — part of `ai-product/`; router = README.md._
- **Date identified**: 2026-03-26
- **Source**: Haresh Kumar's customer story in Session IV (March 26). Modernization agent story failed in the field.
- **Insight**: An agent that works in a contained demo environment may fail at enterprise scale. Large codebases, complex configurations, and unusual edge cases expose limitations that controlled environments don't. Telling a customer that an agent can solve their problem before you have real-world evidence at their scale is a trust-destroying mistake.
- **Signal to watch for**: "It works well in contained environments" = not yet validated at enterprise scale. Treat as pre-GA until proven otherwise.
- **Application**: Before recommending an agent to a customer, ask: what is the largest real-world deployment we have evidence from? If the answer is a pilot or a demo, say so.
