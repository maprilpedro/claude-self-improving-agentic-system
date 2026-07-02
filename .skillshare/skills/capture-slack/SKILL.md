---
name: capture-slack
description: Capture a Slack thread into the PM knowledge system — fetch via Slack MCP (or from pasted text/screenshot), attribute exactly, route to the owning project's memory + Status, add watches, then commit. Use when Pedro shares a Slack permalink or pasted/screenshotted thread and asks to "capture", "bank this thread", "ingère ce thread", "capture ce slack", "ajoute ça à la mémoire". Do NOT trigger when he asks to REPLY to the thread (that's /reply — though /reply may hand off here to bank the source) or for meeting transcripts (/ingest-transcript).
---

# Capture Slack

The Slack sibling of `/ingest-transcript` — threads used to enter via screenshot + hand-description. This fetches the verbatim, attributes it, and routes it once.

## Step 1 — Get the thread verbatim

- **Permalink** → fetch via Slack MCP (`slack_read_thread`). Works in interactive sessions OAuth'd to cq-dev only (`reference_slack_mcp_workspace`); if the read fails `channel_not_found`, say so and ask for a paste.
- **Pasted text** → use as-is.
- **Screenshot** → read it; bank the file to `screenshots/` with the standard `YYYYMMDD-topic` name (`feedback_screenshots`); if exact wording matters downstream, ask for a paste.

Reading is allowed; **never send or react** (`feedback_never_send_slack`).

## Step 2 — Attribute + normalize

- Exact speaker + timestamp per message; verbatim stays original language (`feedback_language_split`).
- Resolve handles/garbles via `reference_transcript_glossary.md` (the two Ians, the two Felixes); flag unknown handles as new-stakeholder candidates.
- Positions ≠ decisions — label accordingly (`feedback_proposal_vs_decision`).

## Step 3 — Route once (one home per info)

Route by the CLAUDE.md project table (EH vs AAI):

- **Project memory** — dated event block in the owning project's active memory file: what moved, why it matters, bankable verbatim, permalink. Cite applicable knowledge entries `[[...]]` or "none apply" (P6).
- **Status & Todo** — only if the thread creates/closes tasks (forward checkbox + 📅, `feedback_task_vs_progress_log`).
- **Stakeholder Map** — only for a new person or a posture shift (dated note).
- **watches.md** — any dated follow-up the thread creates ("Reasor back Monday" → a watch, not a buried line).
- Do NOT write a State-of-Project block for a thread capture (headline-only rule, P4).

## Step 4 — Summarize + commit

Brief change summary (`feedback_document_updates`): what was captured, where it landed, watches added, new stakeholders. Commit `learn:` per the Commit Rule (never push).
