---
name: digest
description: Apply a reusable PM extraction template to a source (vault note, transcript, deck, pasted text) and produce a structured note — executive summary, decisions+owners, risks, action items, or a Senior-Director "so-what". Default engine = Claude (reads the source fresh + applies Pedro's project knowledge). Switch to a fully-local Qwen/Ollama engine for sensitive content with --qwen or words like "local"/"privé"/"sensible". Use whenever Pedro says "digest this", "summarize this", "pull the decisions/risks/actions out of this", "what's the so-what", or runs /digest. Prefer this over ad-hoc summarizing — the templates bake in Pedro's own rules (decisions ≠ proposals, forward-looking actions only, position-over-merit lens) so output is consistent and his.
disable-model-invocation: true
---

# Digest

Turn one source into a structured PM note by applying a fixed template. This is the "Transformations" idea from Open Notebook: define the extraction once, reuse it across sources, get consistent output. The value over a free-form summary is that the templates encode Pedro's standing rules, so he never has to re-explain them.

## Templates (`templates.json`)

| Template | Output |
|---|---|
| `exec` (default) | Executive summary, 5 lines, pyramid order |
| `decisions` | Decisions + owner + date + firm/proposal (does NOT promote proposals to decisions) |
| `risks` | Risks + impact + owner + mitigation, flags unowned ones |
| `actions` | Forward-looking action items only (owner + due), checkbox format |
| `sowhat` | Director→Senior-Director lens: 3 moves + 1 narrative to own + 1 positioning risk |

Templates are Pedro's to edit/extend — add one, the skill logic doesn't change.

## Defaults (Pedro)
- **Language: English by default**, choosable per run with `--lang fr` (or any code). Pedro picks.
- **Output:** the vault, `020 Professional/Adobe/Projects/2026/Digests/` (write via `obsidian-cli`, or filesystem for a new folder). Filename: `<YYYYMMDD> - <title> - <template>.md`.

## Engine (claude ⇄ qwen) — transparent switch

Same command, same template, same output file + structure either way. Pick the engine:
- **claude** (default) — best quality, uses Pedro's project knowledge.
- **qwen** — when Pedro adds `--qwen` / `--engine qwen`, or says "local" / "privé" / "sensible".

| Engine | Brings | Cost |
|---|---|---|
| **claude** (default) | Project memory + reasoning on top of a fresh read of the source | Content goes to Anthropic |
| **qwen** | Fresh read of the source only, 100% local | No Claude context, lower quality |

Every output header states the engine (`engine: claude` / `engine: qwen`) so the difference is never hidden.

### claude engine (default) — read fresh, apply, write
1. **Read the source live** (vault note via `obsidian-cli`, file path, or pasted text) — don't work from memory.
2. Apply the chosen template's rules, using Pedro's project knowledge where it sharpens the result (e.g. `decisions` → use what you know about owners and decision-signals; `sowhat` → the full promotion context from memory). Where memory and the fresh source disagree, the source wins for facts; mark any inference vs sourced claim.
3. Write the structured note yourself, header `> engine: claude · Template: <name> · Source: <name>`, save to `2026/Digests/`.

### qwen engine (`--qwen`) — local, private, metadata only
Launch the generator and relay ONLY its metadata — do NOT `cat` the result:
```bash
python3 <skill-dir>/digest_local.py --source "<absolute path>" --template decisions --lang fr \
  --out "/Users/pedrofer/Library/CloudStorage/GoogleDrive-maprilpedro@gmail.com/My Drive/ObsidianVault/020 Professional/Adobe/Projects/2026/Digests"
```
The script reads the source, applies the template against local Qwen, writes the note, prints a one-line JSON blob (path, template, words). Content never enters Claude's context. Requires `ollama` running.

## Workflow
1. Pick engine (default claude; `--qwen` or "local/privé/sensible" → qwen) and template (default `exec`, ask only if ambiguous).
2. claude → read fresh + apply + save + 3-line summary. qwen → run the script, relay metadata only.

## What this is NOT
- Not chat/RAG/search over a corpus (Claude + deep-research already do that).
- Not the Open Notebook app. Just the transformation step, native + optionally local.
