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
| ⚠️ **Namita — TWO RECORDS, UNRESOLVED (flagged 2026-07-16)** | **Namita Kavadi** ("Namita Kalra" garble) is what this glossary and [[reference_namita_scope]] carry (*"AEP AOv1 PM, NOT the MCP-reports track"*). **But the 07-15 rollout-sync Teams display name is `Namita Krishnan`** — and **Teams display names are not Otter garbles**, so that spelling is reliable. Memory also carries a **Namita Krishnan** on the 05-27 TBYB-cohort line with Tina Ngo. **Either there are two Namitas or one of our records is wrong.** ⚠️ **Do not merge, do not guess, and do not put either surname in an outbound artifact until checked** (Slack profile is the cheap test). The 07-15 rollout Namita is the one who runs the weekly while Rachel is out and who said *"if a customer has V2, there's no AI assistant anymore."* |
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
| Pedro Ferreira | "Peter" (Satya, 07-09 credit sync). See also the room-mic trap below |
| Mayank Agarwal (AEM Forms — the GCL-property published-form attribution precedent; NEW 07-09) / Natalia Venditto (token-cost ≠ perceived value; clustering proposal; NEW 07-09) | — |
| ⚠️ **Tina** (owns the field-readiness deck w/ customer-facing credit info, 07-09 credit sync) | likely **Tina Ngo** (Principal PMM, agents GTM) — ⚠️ **NOT Tina Nicu**. Two Tinas in PMM. Confirm before quoting |
| **Daniel Mrose** ("get Daniel's team the documents… scope the security review", 07-09 credit sync) | ✅ **CONFIRMED 07-10** via the reporting line (Lars Krapf → Catalin Luta → Daniel Mrose → Saar). ⚠️ Still do not merge with **Dan**, the Gem-Stack / AI-Assistant-Team lead |
| **Lars Krapf** — Sr Security Researcher, Customer Experience Orchestration (reports to Catalin Luta). AEM→Coworker security review, out Mondays | NEW 2026-07-10 |
| **Catalin Luta** — Sr Manager (7 reports) under Daniel Mrose, CXO. **Manager on the AEM Coworker security review**, so his threat-model statement is authoritative | ⚠️ **not Catalina Preda** (AEP evals/golden-set). Earlier notes called him "AEM eng" — wrong, he is CXO management |
| Toby (readiness/infrastructure contact) / Ovidiu (ORR contact — "nothing needed from their side") | NEW 07-09, surnames unknown |
| **Vineet Sharma** — engineering lead for **Coworker Projects**. Horia's routing for AEM getting hands-on with projects (with Raj Patel) | NEW 2026-07-15. Said as both "Vinit Sharma" and "Vineet" in one breath — ⚠️ spelling unverified, confirm before Slacking him. Do NOT merge with **Vineet Barshikar** (AIA federated-renderer architecture) |
| **Zan Chu** — has the **business-context demo** Rachel offered to share | NEW 2026-07-15, spelling unverified |
| **Gilles Knobloch** — in the Basel room 07-15; his ask (internal hands-on access to projects without a customer) was **relayed by another voice on the same mic** | ⚠️ his own words are mostly NOT on the transcript — do not quote him from the room mic |
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
| Langfuse (in "integrate reporting with Langfuse") | "fuse chain", "lung fuse"; **AEP Langfuse** = "AAP long fuse" (07-09) |
| Rubin (reporting substrate) | "around Robin", "Brabin" (07-09, low confidence — verify before quoting) |
| Tanju Erinmez | "Taneja" (07-09) |
| Claude (the client/surface) | "Claudia", "clod surface" (07-06 gating transcript) |
| conformance eval (gateway gate 3) | "conformer Seibel" (07-06) |
| agent(ic) gateway | "identity gateway" (Victor 07-06, low-conf — verify which he meant before quoting) |
| Sliccy (external OSS) | "Slicc", "sleek", "Slick" |
| skills.yml / marketplace.json | various spellings — verify against repo before quoting |
| Gem Stack (original product-knowledge-only AI Assistant, pre-agents; Dan's team; some customers still on it via flags, reason = Managed Services) | "gem stack"/"team dan" — canonical concept surfaced 07-08 |
| LLM Optimizer (the risk-based no-extra-paperwork precedent Legal cites, 07-09) | "LM Optimizer" |
| PLA (the legal agreement done once for Project 42 + all agents underneath) | — |
| AI rider (provisioned at SKU level, Coworker-wide, not per-agent) | "AI waiver" (Yanira, 07-09) |
| **Coworker Projects** (the 2nd Coworker module — team productivity, codified workflows) | — |
| **Project Halo / Coworker Campaigns** (a 3rd module, absent from Anil's Summit slide; Horia parked it 07-15) | — |
| Fruitbar (the generative-UI surface in Projects) | "project footbar" (07-15) |
| CJA | "CGA", "CJ" (07-15) |
| Joshua Hailpern | "Josh Halpern" (Horia, 07-15) |
| ⚠️ "Scopa"/"Fascopa" (the demo brand in Bertrand's 07-15 Coworker demo, AEM Showcase org) | Otter-garbled, **unverified** — do not put it in an artifact before Bertrand confirms the real demo-site name |
| ⚠️ "Fluffy Jaws" (an MCP an Acrobat colleague added to Coworker for CJA analysis — Horia says "you of course know Fluffy Jaws") | almost certainly a garble of a real internal MCP name; unresolved |
| ⚠️ "Taneja"/"Tanning" (07-15 room) | context suggests **Tanju Erinmez** for "Taneja"; "the list of people at Tanning" = likely "in attendance" mis-heard. Low confidence |
| **Gainsight** (the in-app popup tool AEP will use for the Coworker announcement; AEM uses it too — Pedro confirmed in-room 07-15) | "gain site" |
| **Cohort 0** (Rachel's name for early-access customers *"enabled on both"* Coworker and AI Assistant — the coexistence door; **explicitly NOT "pods"**, which she reserves for agentic-workflow/projects co-innovation) | — |
| Langfuse | "log fuse" (07-15) |
| ⚠️ "Sharda" / "Shankari" (07-15 rollout sync — the credit / rate-card contact Namita named) | **Unresolved.** Namita said "work with Shankari… [on] his rate card", then answered **"Sharda"** when asked for the contact name. Possibly **Pritie Sharda** (Agent PgM), possibly an Otter garble of Shankari Panchapakesan. **She said she would post the name — take it from there, do not guess** |

## Structural traps (not garbles)

- **"CR <ROOM>" labels** = conference-room mics, not people; map per-meeting by content (`feedback_transcript_attribution`). **`CR BASL 05` (and `CR BASL 05 / WALENSEE VC (4)`) = PEDRO in BOTH the 07-08 Rachel rollout transcript AND the 07-09 credit-mapping transcript** — two independent confirmations. **In the 07-08 Rachel rollout transcript, `CR` (CR BASL 05) = PEDRO himself** — his own positions/commitments are under the room-mic label; do not misattribute them as a third party.
- 🔴 **THE "CR BASL 05 = Pedro" DEFAULT IS DEAD — CHECK THE ROOM HEADER FIRST (correction 2026-07-16).** In `20260715 - Coworker w AEM Agent Team Demo`, the label is **`CR BASL 05/LAGO MAGGIORE VC (9)`** and the transcript header states the room outright: **"Present in the room: Bertrand de Coatpont, Gilles Knobloch, Pedro Ferreira."** One mic, three people, **no way to separate them from the label alone.** Proof it is not Pedro by default: after the Scopa demo spiel the room mic delivers, **Horia answers "Thank you, Bertrand. You made it really concrete"** → that block is **Bertrand**, filed under the same label as Pedro's questions. **Rule: read the "Present in the room" header before attributing a single `CR` line, attribute by content, and when three people share a mic, say "the Basel room" rather than guess a name.** A wrong name here is a fabricated quote in Pedro's mouth or a peer's.
- **Otter without timestamps** — no time anchors; date statements by content only.
- **AIA (front/UI) ≠ Coworker/AOv2 (backend)** — transcripts blur them; keep the axes distinct (`reference_aia_vs_coworker_axes`).
- **"Tool Calls"** is the locked measurement term — transcripts saying "interactions/invocations/requests" get analyzed as what they actually counted (`reference_mcp_terminology`).
