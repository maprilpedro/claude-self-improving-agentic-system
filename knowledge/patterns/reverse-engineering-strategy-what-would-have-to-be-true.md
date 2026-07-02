# Reverse-Engineering Strategy — "What Would Have to Be True?"

_Section: Artifact Architecture — part of `patterns/`; router = README.md._

- **Date**: 2026-05-04
- **Source**: Lafley & Martin, *Playing to Win*, Ch 8 ("Shorten Your Odds")
- **Pattern**: When a strategy team can't agree between competing options (or one person's option dominates the room), do not debate which is right. Reframe each option as a hypothesis and ask the seven-step question for each: *what would have to be true for this option to be the right one?* Then go test the conditions, not the conclusion. The team converges on the option whose conditions hold up, instead of the option held by the loudest voice.
- **The seven steps** (compressed):
  1. Frame the strategic choice — make options concrete and mutually exclusive.
  2. Generate strategic possibilities — at least three, including one that breaks current assumptions.
  3. Specify conditions for each — what would have to be true (industry, customer, position, competition, capability) for each to be the winning choice.
  4. Identify barriers to choice — which conditions look least likely or hardest to verify.
  5. Design tests for the barriers — proportional to the leader's confidence (lower confidence = bigger test).
  6. Conduct the tests — run them honestly, even if results are unwelcome.
  7. Make the choice — the option whose conditions hold becomes the strategy; document the discarded options + why.
- **Why it works**: It depersonalizes the choice. Every executive in the room owns the *test*, not the *option*. Disagreement gets routed to "we disagree about which condition matters" — which is testable — instead of "we disagree about who is right" — which is not.
- **PM application**: Use this in Director-level strategy debates where two roadmap directions compete and political weight is uneven. Frame both as hypotheses, ask the seven-step question, surface the conditions, propose the cheapest test for the most-disputed condition. The act of running the seven steps is itself a Senior Director move — it converts a position fight into a learning exercise.
- **When it applies**: Strategy debates with multiple credible options. Roadmap forks. Competing capability investments. Build vs buy vs partner. Cross-org arguments where positional power is uneven.
- **When it fails**: When time is too short to test (operational decisions). When the conditions are unfalsifiable in any practical timeframe (very long-term bets). When the choice is a values question rather than a strategy question.
