---
name: reference-transcript-glossary
description: Canonical names + terms and their known Otter/Teams transcript garbles. Loaded by /ingest-transcript and transcript-extractor BEFORE reading any transcript — systematic de-garble instead of re-deriving per ingest. Grows one line per new garble.
metadata:
  type: reference
---

# Transcript glossary — canonical names, terms, and known garbles

> **Use:** load before reading any transcript. Map garbles → canonical on extraction; quote verbatim stays original but the *analysis* uses canonical. When a NEW garble is resolved during an ingest, add it here (that is the whole maintenance model).
> **Born from real damage:** "Encore" + "Jean-Claude" (Otter garbles of person names) were carried as TEAMS and went out in a broadcast to agent owners before the 07-01 correction.

## People (canonical → known garbles / traps)

| Canonical | Garbles / traps |
|---|---|
| Ian Boston (`boston@`, AEM archi/compliance) | "in Boston" — do NOT merge with Ian Reasor |
| Ian Reasor (`ireasor@`, AEP/Coworker eng) | "Risa", "Ian Risa" — the OTHER Ian |
| Manas | "Manus" (EPA canvas typo) |
| Loni Stark | "Lonnie" |
| Felix Meschberger (`@fmeschbe`) | do NOT merge with Felix Delval (`@fdelval`, EPA/AEM eng) |
| Tanju Erinmez | — |
| Ilya Grafutko | "Ilie" (corrected 06-30) |
| Rachel Hanessian (`@hanessia`) | "Hanessia Anessian" |
| Namita Kavadi | "Namita Kalra" |
| Matt Colón (`@coln`) / Tim Lynn (`@tlynn`) | handle confusion (fixed 06-15) |
| ⚠️ unresolved person garbles | "Encore" (Assets team member), "Jean-Claude" (Tanju searching a name live) — PEOPLE not teams; do not carry as agents/teams |

## Terms / products (canonical → garbles)

| Canonical | Garbles |
|---|---|
| One AEM MCP (server) | "1am MCP", "1AM/AMCP", "1AMM CP", "one MCP" |
| Coworker | "who worker", "co worker" |
| Anthropic | "Entropic" |
| Claude | "claw", "cloth" |
| Governance Agent / MCP | "EGA/BGA/AGA", "golden agent" |
| recipes | "receipts" |
| cross-agent | "X agent" |
| garage-week | "Gayatri", "garage" |
| Manager Services | "manette services" |
| Langfuse (in "integrate reporting with Langfuse") | "fuse chain" |
| Sliccy (external OSS) | "Slicc", "sleek", "Slick" |
| skills.yml / marketplace.json | various spellings — verify against repo before quoting |

## Structural traps (not garbles)

- **"CR <ROOM>" labels** = conference-room mics, not people; map per-meeting by content (`feedback_transcript_attribution`).
- **Otter without timestamps** — no time anchors; date statements by content only.
- **AIA (front/UI) ≠ Coworker/AOv2 (backend)** — transcripts blur them; keep the axes distinct (`reference_aia_vs_coworker_axes`).
- **"Tool Calls"** is the locked measurement term — transcripts saying "interactions/invocations/requests" get analyzed as what they actually counted (`reference_mcp_terminology`).
