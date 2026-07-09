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
| Catalina Preda (AEP, Coworker quality/evals) | "Katharina", "Catalina/Katharina" mix within one transcript (07-06) |
| Georgiana Copil (AEP, gateway governance/quality doc) | — |
| Rebecca Yonezcu (Sr Product Designer — Discovery + Content Optimization agent renderers; NEW 07-08) | "Yonezcu see"/"Yonescu" — spelling unverified, confirm before quoting |
| Dan (lead, the "AI Assistant Team" = the Gem Stack implementation) | "done"/"Dan in doctors" (Otter garble, 07-08 Sorin 1-1) |
| Zeus Courtois (lead eng, Mithril/Fruitbar/Prompt Library Platform under Joshua Hailpern; owns the AO2 suggested-prompt/recommendation system — surfaced in this role 07-08) | "Zeus" — NOT a new person, already EH-side; do not create a duplicate |
| Ryan Cobourn (design/transition owner, convergence room; NEW 07-08) | "Cobourn"/"Coburn" — ⚠️ do NOT merge with **Cole** Connelly; both are real, distinct people in the Coworker sessions |
| Horia Galatanu (Coworker panel release timing, w/ Cole + Babu; NEW 07-08) | "Horia" — spelling unverified |
| Ashish (Basel presenter, Coworker sessions; NEW 07-08) / Adrian (Bucharest, new team member, separate left-nav impl) / Michal (WebMCP tools, w/ Rodson) | all Otter-unverified spellings — confirm before quoting/indexing |
| Ellis Dobkin (Legal — AEM agents, Agent Orchestrator legal work, the P42 PLA; NEW 07-09) / Meredith Elder (Legal, Ellis's team, product council, supports Commerce; NEW 07-09) | — |
| ⚠️ **Jacqueline** (Legal-side GTM, co-wrote the legal-intake checklist with Yanira; 07-09) | **do NOT merge with Jaclyn Eckersley** (FinOps, AEM Eng VP-side) — different people, near-identical names |
| Kristal (GTM driver for Agent Orchestrator; hand-off target once the credit model firms; 07-09) | surname unknown |
| ⚠️ unresolved person garbles | "Encore" (Assets team member), "Jean-Claude" (Tanju searching a name live), "will/wool" (07-08 Sorin 1-1, an eng who'd know AI-Assistant activation/Gem-Stack config), "Iulia"/"Ilie" (07-08 Rachel rollout call — a security/legal reviewer on Horia Galatanu's AEP team; ⚠️ NOT Ilya Grafutko; Horia to Slack the real name) — PEOPLE not teams; do not carry as agents/teams |

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
| Claude (the client/surface) | "Claudia", "clod surface" (07-06 gating transcript) |
| conformance eval (gateway gate 3) | "conformer Seibel" (07-06) |
| agent(ic) gateway | "identity gateway" (Victor 07-06, low-conf — verify which he meant before quoting) |
| Sliccy (external OSS) | "Slicc", "sleek", "Slick" |
| skills.yml / marketplace.json | various spellings — verify against repo before quoting |
| Gem Stack (original product-knowledge-only AI Assistant, pre-agents; Dan's team; some customers still on it via flags, reason = Managed Services) | "gem stack"/"team dan" — canonical concept surfaced 07-08 |
| LLM Optimizer (the risk-based no-extra-paperwork precedent Legal cites, 07-09) | "LM Optimizer" |
| PLA (the legal agreement done once for Project 42 + all agents underneath) | — |
| AI rider (provisioned at SKU level, Coworker-wide, not per-agent) | "AI waiver" (Yanira, 07-09) |

## Structural traps (not garbles)

- **"CR <ROOM>" labels** = conference-room mics, not people; map per-meeting by content (`feedback_transcript_attribution`). **In the 07-08 Rachel rollout transcript, `CR` (CR BASL 05) = PEDRO himself** — his own positions/commitments are under the room-mic label; do not misattribute them as a third party.
- **Otter without timestamps** — no time anchors; date statements by content only.
- **AIA (front/UI) ≠ Coworker/AOv2 (backend)** — transcripts blur them; keep the axes distinct (`reference_aia_vs_coworker_axes`).
- **"Tool Calls"** is the locked measurement term — transcripts saying "interactions/invocations/requests" get analyzed as what they actually counted (`reference_mcp_terminology`).
