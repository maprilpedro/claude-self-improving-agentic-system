# User Feedback as Ranking Signal — ✓/✗ to Densify Sparse Personalization

_Section: Personalization Architecture for AI Surfaces — part of `ai-product/`; router = README.md._
- **Date identified**: 2026-04-20
- **Source**: Eugene Bannykh, Fu-Chi sync. "Our algorithm is only as good as our signals are."
- **Insight**: When the user-level signal is sparse (the cascade's primary problem), an explicit feedback UI can densify it cheaply. A per-recommendation ✓/✗ button turns passive exposure into an active signal — the user tells the system what's relevant to them. This doesn't replace behavioral signals (what prompts they actually use); it complements them by capturing relevance-without-action (user saw it, decided it wasn't for them, said so).
- **Design constraint**: The feedback must require zero friction to be useful. A modal, a confirmation, or a reason-why-field kills the signal. A single click, persisted silently, is the only form that works.
- **Why this matters**: Sparse-data personalization systems often sit on a chicken-and-egg problem — they need behavior to rank well, but users don't engage until ranking is good. Feedback bypasses the loop. Even 5% of users clicking ✗ on irrelevant prompts gives the ranker information it couldn't get any other way.
- **Application**: Any surface with suggested content backed by a ranking system should consider a lightweight feedback UI. Track whether feedback actually changes rankings — if the system ignores it, users will stop clicking and the signal dies. Closing the loop (showing "based on your feedback, here's what we changed") isn't necessary; the ranker just needs to use the signal.
