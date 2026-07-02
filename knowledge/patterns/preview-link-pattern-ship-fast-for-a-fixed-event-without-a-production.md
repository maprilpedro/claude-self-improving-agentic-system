# Preview Link Pattern — Ship Fast for a Fixed Event Without a Production Commitment

_Section: Anti-Patterns — part of `patterns/`; router = README.md._
- **Date identified**: 2026-04-01
- **Source**: Sorin Slavic in April 1 EH refinement sync — Brand Concierge Summit options discussion.
- **Observations**: (1) Summit deadline (April 19-22) made full production implementation impossible in 2 weeks. Sorin proposed using a preview link — automatically generated for in-progress changes, gives full integration and real behavior, but is not merged to production. (2) Security team previously used a similar approach for early demos. (3) The pattern separates "does it work?" validation from "is it production-ready?" quality assurance.
- **Pattern**: When a fixed event (summit, exec demo, customer pilot) creates a hard deadline that production quality cannot meet, use the preview link approach: write the code, bypass production guardrails, generate a preview link for the specific demo context. After the event, decide whether to invest in making it production-ready or remove it.
- **Conditions**: (1) The audience is known and controlled — you know exactly who will click it and in what sequence. (2) The event is time-bounded — it's not a permanent commitment. (3) There's an explicit plan for what happens after — either productionize or remove.
- **Risk**: If the preview version leaks or gets treated as a commitment, you've created expectations you haven't shipped to. Be explicit upfront: "This is a Summit-only preview, not a product commitment."
- **Application**: Before saying "we can't do this in time for the event," ask whether a preview link version is viable. It often is, and it lets the event happen without blocking a production decision.
