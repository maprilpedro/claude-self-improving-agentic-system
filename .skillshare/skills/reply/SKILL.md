---
name: reply
description: Draft a reply/message in Pedro's voice with a mandatory pre-flight — entity lookup across memory/vault, open-watch check, knowledge citation, compiled voice rules — then output draft + evidence table. Use whenever Pedro asks to respond to or draft a message for a thread, email, or person — "j'aimerais répondre à", "réponds à", "draft une réponse", "réfléchis à une réponse", "prépare un message pour", "qu'est-ce que je réponds à", "help me reply", "draft a reply/message to". Trigger even when he pastes a thread and just asks what to say back. Do NOT trigger for vault/status updates (that's /ingest-transcript or /jira-sync) or for analysis with no outgoing message.
---

# Reply

Draft an outgoing message (Slack, email, Confluence comment, meeting line) in Pedro's voice — with the checks that history shows get skipped when drafting ad-hoc. Every documented draft failure (NYL data-dump, Coworker/AIA conflation ×3, unmarked inferences, "embedded" over-add) was a skipped check, not missing information. This skill is the checklist compiled.

**Hard rule first: NEVER send.** Output is a draft Pedro pastes himself — the send tool leaks "Sent using @Claude" (`feedback_never_send_slack`). Reading Slack via MCP is fine.

## Step 0 — Confirm the ask + read the actual source

- Restate in one line what Pedro wants to answer and to whom. If ambiguous (which thread? reply-all or DM?), ask — don't act on an assumed delegation (`feedback_confirm_ask_before_producing`).
- Read the real source: pasted text as-is; a permalink → fetch via Slack MCP (interactive sessions only, `reference_slack_mcp_workspace`); a screenshot → read it, but ask for a paste if wording matters. Never characterize a source unread.
- De-garble names/terms via `reference_transcript_glossary.md` if the source is a transcript.

## Step 1 — Entity pre-flight (what do we already know?)

Extract the entities in play (people, agents, threads, products). For each:

1. `ENTITY_INDEX.md` (`.claude/memory/`) → which memory files mention them.
2. The owning project's memory file (active) + targeted `rtk proxy grep` of archive shards via `*_ARCHIVE_INDEX.md` — never full-Read a shard.
3. The owning project's **Stakeholder Map** in the vault (posture, last dated note).
4. The two-Ians / two-Felixes traps and org chains (`project_adobe_org`, glossary).

Output of this step (internal): who this person is to Pedro, last interaction, open items with them.

## Step 2 — Watch check

Read `.claude/memory/watches.md`. Is there an open watch touching this thread/person? A reply into a thread with a pending watch must account for it (e.g. don't ping Reasor before 07-06; don't cite MCP numbers while Christian's traffic-review HOLD stands).

## Step 3 — Knowledge pull (the P6 retrieval rule)

Route via `knowledge/INDEX.md` → folder routers → cite the applicable entries as `[[entry title]]` in your reasoning, or say "none apply". Typical hits for replies: `[[feedback_position_over_merit]]` framing, leadership/ cross-org entries, ai-product/ for technical claims. Knowledge not retrieved at decision time doesn't exist.

## Step 4 — Position check (before wording)

- What does this reply do for the Senior Director lane — claim, concede, convene, or just inform? (`feedback_position_over_merit`)
- Whose artifact/thread is it? Senior's → additive, not corrective (`feedback_additive_not_corrective`); sponsor's (Ian/Bertrand/Loni) → co-author, validate + shared gap + hand back a question, don't answer-over (`feedback_co_author_dont_answer_over`).
- Escalation / VP-visible thread → one literal ownership sentence FIRST (`feedback_first_reply_ownership_sentence`); the deep answer can follow (`feedback_response_window_for_exec_questions`: 30-min window, 5-sentence answer in their literal frame).
- Correcting a misread → forward-framed ("here's what's in motion"), never litigate the prior reply (`feedback_dont_litigate_prior_replies`).

## Step 5 — Draft in Pedro's voice (compiled checklist)

Language: match the thread (Slack interne souvent FR avec Bertrand; cross-org EN). Then:

- **His plain-English level** — no native idioms, no meta-narration of the move, no reciting the other's position back, Slack-clipped not essay, **no em-dashes** (`feedback_draft_in_pedros_voice`).
- **Mark inference vs sourced** — unconfirmed technical claims are HIS exposure; mark them or cut them; keep distinct systems distinct (`feedback_voice_drafts_mark_inference`, `feedback_dont_conflate_pattern_with_object`, AIA-front ≠ Coworker-backend word-lock `reference_aia_vs_coworker_axes`).
- **Proposals ≠ decisions** — no "officially/consolidated/resolved" without a real decision signal (`feedback_proposal_vs_decision`).
- **Audience dosing** — Bertrand: concrete scene + named artifacts first, mechanism last (`feedback_bertrand_concrete_first`). Exec: PKD register very-light to off (`feedback_pkd_chat_tone`); email: at most 1 Dick turn per cluster, approximate > precise, hide receipts, assertive asks, shorter.
- **Terminology locks** — "Tool Calls" (`reference_mcp_terminology`); no Claude/AI-assistant surfacing (`feedback_keep_claude_private`).
- FR register when applicable: clean, no crude slang (`feedback_french_register`).

## Step 6 — Output

1. **The draft** (marked `DRAFT — tu colles toi-même`).
2. **Evidence table** — each claim in the draft → `sourced (ref)` / `inferred (marked in draft)` / `Pedro's position`. This is the audit Pedro's "100% no invention" bar requires (`feedback_audit_outward_artifacts`).
3. **One-line position read** — what this reply buys in the lane.
4. If the reply creates a dated follow-up ("will check X Friday") → offer to add it to `watches.md`.

## Iterating

When Pedro flags one phrase, fix THAT span only — offer 2-3 options for it, don't rebuild the message (`feedback_edit_the_span_not_the_artifact`).
