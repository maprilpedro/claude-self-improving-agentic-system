# Stage 2 — Transcript prompt (run once per segment)

Ported from Open Notebook / `podcast-creator` (`transcript.jinja`). Run this **once per segment, in order**, passing the running transcript back in each time. This is the *writer* pass: it produces the actual spoken dialogue for ONE segment only.

---

You are writing the transcript for **one segment** of a podcast. Other passes handle the other segments — stay inside this segment.

**Briefing:**
`{briefing}`

**Context** (source material):
`{context}`

**Speakers:**
For each — `- **{name}**: {backstory}. Personality: {personality}`

**Language:** Write ALL dialogue in `{language}`. Do not switch languages except to quote specific foreign terms.

**Outline** (the full director plan, for continuity):
`{outline}`

**Transcript so far** (everything already written — read it so you continue naturally, do NOT repeat it):
`{transcript}`   ← omit on the first segment

**Write dialogue for THIS segment only:**
`{segment}`

`{is_final}` → if true, this is the last segment: wrap up the conversation and land a conclusion.

Format requirements (strict):
- Use the real speaker names: `{speaker_names}`.
- Choose who speaks by personality, backstory, and topic fit.
- Stay inside this segment — don't run ahead.
- At least `{turns}` turns between speakers.
- Each speaker contributes meaningfully to their expertise.
- Balanced exchanges — avoid long monologues. Natural transitions.
- Don't reintroduce speakers/topics; the segment is just a topic marker.
- Conversational, engaging, natural — not a lecture.

**Output** — pure JSON, no code fence, a single `"transcript"` key:
```
{
    "transcript": [
        { "speaker": "<real name>", "dialogue": "..." }
    ]
}
```
