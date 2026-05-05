---
name: Big-file parallel chunk extract methodology
description: When asked to absorb a transcript or document larger than ~100K / 2000 lines, do not stream-read into the main context. Spawn 3-5 parallel background agents, each reading a contiguous chunk, returning a structured signal extract. Main thread synthesizes from extracts only.
type: feedback
---

When a transcript or doc is too large to read fully into main context (>100K bytes or >2000 lines), use parallel chunk extraction instead of trying to read it sequentially.

**Why:** April 29 AEP-AEM AOv2 Alignment Otter transcript was 4160 lines / ~172K. A direct Read would have either failed or saturated the context window before any synthesis could happen. Pedro framed the ask explicitly: "the file is huge. get a strategy to still be able to absorb it." The chunk-extract method shipped memory + State of Project + Status&Todo + MOC updates in one session without context exhaustion.

**How to apply:**

1. **Trigger.** File >100K or >2000 lines, or any time a single Read would consume >40% of remaining context budget. Especially relevant for Otter transcripts, long Slack threads, multi-hour meeting recordings, large codebases of legal/spec docs.
2. **Chunk plan.** Divide into 3-5 contiguous line ranges (avoid over-splitting — synthesis cost scales with chunk count). Otter transcripts: split on time boundaries if visible (hour marks); else equal line counts.
3. **Spawn parallel background agents** (`Agent` with `run_in_background: true`, single message, multiple tool blocks). Each gets:
   - File path + exact line range (`offset` / `limit` to Read)
   - Output schema — what to extract: decisions landed, open questions, named asks, quote bank with timestamps, speaker attributions, action items
   - Caller context — what project this feeds, why it matters, what NOT to bother with
   - "Return structured extract under N words" — keep returns small enough that main thread can hold all of them
4. **Synthesize in main thread.** When all agents return, fold extracts into target artifacts (memory file → State of Project → Status&Todo → MOC, in that order). Main thread never reads the source file directly.
5. **Quote bank discipline.** Each agent should return verbatim quotes with timestamps + speaker, not paraphrases. Deck-ready material lives in those raw quotes.
6. **Speaker attribution check.** Before quoting in deliverables, verify room-mic labels per `feedback_transcript_attribution.md` — same room ≠ same person across meetings.

**Cost note:** 4 parallel agents on ~40K each is cheaper context-wise than one sequential 172K read, even though total tokens read across agents is similar — main thread only sees the compressed extracts.
