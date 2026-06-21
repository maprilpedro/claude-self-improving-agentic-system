---
name: podcast-script
description: Generate a ready-to-read podcast SCRIPT (the spoken dialogue) from source material — a vault note, a meeting transcript, a deck, or pasted text. Ports the NotebookLM / Open Notebook content-generation pipeline (outline → per-segment dialogue) natively into Claude. No audio, no TTS, no Docker — just the script Pedro reads (or pastes into any TTS later). Use whenever Pedro says "make a podcast script", "podcast from this", "turn this into a podcast", "script for audio", or runs /podcast-script. Strongly prefer this skill over ad-hoc one-shot generation — the two-stage chain (outline first, then dialogue segment-by-segment carrying the running transcript) is what makes the script sound like a real conversation instead of a wall of text.
disable-model-invocation: true
---

# Podcast Script

Turn one source into a natural-sounding, speaker-labelled podcast script — **the content that gets read**, not the voice. This ports the part of NotebookLM / Open Notebook that Pedro actually values: the script generation. Voice synthesis is deliberately out of scope (read it yourself, or paste into any TTS).

The quality trick — and the reason this is a skill, not a one-shot prompt — is the **two-stage chain**: generate a segment outline first, then write the dialogue **one segment at a time, feeding the already-written transcript back in each time**. One monolithic generation drifts: unbalanced turns, repeated intros, no through-line. Do not shortcut it.

---

## Defaults (Pedro)

- **Language: French by default.** Override per run if the source is for a work/EN audience.
- **Output location:** the vault, in `020 Professional/Adobe/Projects/2026/Podcast Scripts/`. Write via the `obsidian-cli` skill (vault-relative path), so the note lands in the index. Filename: `<YYYYMMDD> - <short-title>.md`.
- **Confidentiality:** runs on Pedro's current Claude — same exposure as any Claude Code session, no new leak. Adobe-internal content is fine here. (A fully-local Ollama path would need the full Open Notebook Docker stack — out of scope for this skill.)

---

## Inputs

1. **Source** (one of):
   - A vault note or notes — read via the `obsidian-cli` skill.
   - A file path — `Read` it.
   - Pasted text in chat — use directly.
   - Nothing given → ask which source.
2. **Episode profile** — pick from `profiles/episodes.json` (default `solo_brief`). The profile sets the format, segment count, and the default briefing.
3. **Language** — French unless Pedro says otherwise.

If the source is a large transcript (>2000 lines / >100K chars), summarise it first (or spawn `transcript-extractor`) and feed the structured summary as context — don't stuff raw transcript into the chain.

---

## Workflow

### 1. Resolve source + profile
Read the source. Pick the episode profile (ask only if ambiguous). Load its `default_briefing`, `num_segments`, and `speaker_config`. Pull the matching speakers from `profiles/speakers.json`.

Let Pedro override the briefing in one line (e.g. "focus on the risks, skip the background"). Merge his steer into the profile's `default_briefing`.

### 2. Stage 1 — Outline
Run `references/outline-prompt.md` with: `briefing`, `context` (the source), `speakers`, `num_segments`, `language`.
Output = JSON `{ "segments": [ { "name", "description", "size" } ] }`. First segment = intro, last = wrap-up. Show the outline to Pedro before writing dialogue if he asked to review; otherwise continue.

### 3. Stage 2 — Transcript, segment by segment
For each segment in order, run `references/transcript-prompt.md` with: `briefing`, `context`, `speakers`, `outline`, the **running `transcript`** (everything written so far), the current `segment`, `is_final` (true on the last), `turns` (from the profile, default 6), `language`.
Append each segment's `{ speaker, dialogue }` turns to the running transcript. **Never regenerate earlier segments.** Keep turns balanced — no long monologues, speakers chosen by who'd naturally carry that topic.

### 4. Assemble + save
Render the full transcript to markdown:
```
# <Title>
> Profile: <episode profile> · Language: <lang> · Source: <source>

## <Segment 1 name>
**<Speaker>:** <dialogue>
**<Speaker>:** <dialogue>
...
```
Save to the vault folder above via `obsidian-cli`. Then give Pedro a 3-line summary: title, segment count, word/read-time estimate (~150 wpm).

---

## Engine (claude ⇄ qwen) — transparent switch

Same command, same profile, same output file + structure either way. Pick the engine:
- **claude** (default) — best quality; steps 1-4 above are run by Claude in-context.
- **qwen** — when Pedro adds `--qwen` / `--engine qwen`, or says "local" / "privé" / "sensible".

| Engine | Brings | Cost |
|---|---|---|
| **claude** (default) | Best prose + Pedro's context, on top of the source | Content goes to Anthropic |
| **qwen** | The two-stage chain run locally on the source only | No Claude context, lower quality |

Every output header states the engine (`engine: claude` / `engine: qwen`) so the difference is never hidden. For the claude engine, add `> engine: claude · …` to the header in step 4.

### qwen engine (`--qwen`) — local, private, metadata only
Do NOT run the chain yourself. Launch the generator and relay ONLY its metadata — do NOT `cat` the result:

```bash
python3 <skill-dir>/generate_local.py --source "<absolute path>" --profile solo_brief --lang fr \
  --out "/Users/pedrofer/Library/CloudStorage/GoogleDrive-maprilpedro@gmail.com/My Drive/ObsidianVault/020 Professional/Adobe/Projects/2026/Podcast Scripts"
```

The script runs outline → per-segment transcript against local Qwen, writes the markdown, prints a one-line JSON blob (path, profile, segments, words, read-time). Content never enters Claude's context. Requires `ollama` running (`curl localhost:11434/api/tags` to check). Default model `qwen3:30b-a3b-instruct-2507-q4_K_M`.

## Editing the profiles

`profiles/episodes.json` and `profiles/speakers.json` are Pedro's to tune — add a format, change a persona, bump segment counts. The skill logic doesn't change when profiles do. Keep `speaker_config` keys in episodes pointing at real keys in speakers.

## What this skill is NOT
- Not audio. No TTS, no voice models, no `.mp3`.
- Not the full Open Notebook app (no SurrealDB, no multi-modal ingestion UI). If Pedro ever wants local-only ingestion of ultra-sensitive content or actual audio output, that's the Docker stack — a separate decision.
