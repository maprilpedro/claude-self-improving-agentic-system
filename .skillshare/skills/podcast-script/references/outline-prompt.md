# Stage 1 — Outline prompt

Ported from Open Notebook / `podcast-creator` (`outline.jinja`). Fill the bracketed variables, then produce the JSON. This is the *director* pass: it decides structure, not dialogue.

---

You are creating a podcast outline. The outline will be used to generate the transcript.

**Briefing:**
`{briefing}`

**Context** (the source material for this episode):
`{context}`

**Speakers:**
For each speaker — `- **{name}**: {backstory}. Personality: {personality}`

**Language:** Generate ALL output (segment names, descriptions, every word) in `{language}`. Do not fall back to another language unless the source itself contains foreign terms.

**Task:** Produce exactly `{num_segments}` segments covering the full scope of the briefing.

Guidelines:
1. Read the briefing + context, identify the main themes.
2. Create `{num_segments}` distinct segments spanning the whole scope.
3. Each segment gets a catchy, informative name.
4. Each segment gets a detailed description — the key points and questions to be discussed, drawn from the context. The transcript writer uses this to design the dialogue.
5. Match content to speaker expertise/backstory.
6. Segments flow logically.
7. Don't reintroduce speakers/topics each segment — segments are just topic markers.
8. First segment = introduction. Last segment = conclusion / wrap-up.
9. Tag each segment `size`: `short`, `medium`, or `long`, by importance.

**Output** — pure JSON, no code fence, a single `"segments"` key:
```
{
    "segments": [
        { "name": "...", "description": "...", "size": "short" }
    ]
}
```
