---
name: feedback-edit-the-span-not-the-artifact
description: "When Pedro flags one sentence/phrase, fix THAT span only — don't regenerate the whole artifact."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 75def9b2-7431-4617-a2f8-4050b1882aed
---

When Pedro points at a specific line and says it's wrong ("pas bien", "je n'aime pas la phrase", "retravaille cette partie"), edit **only that span**. Offer 2-4 alternatives **for that line**, keep everything else byte-for-byte. Do **not** rebuild or re-output the whole message/email/document.

**Why:** 2026-06-22, drafting a VP escalation, Pedro flagged a single sentence ("The ask…") and I regenerated the entire email. He had to repeat himself ("je garde le texte précédent mais je n'aime pas la phrase", then "retravaille la partie X et remplace par…"). Re-outputting the whole thing buries the one change, wastes his time, and risks silently altering lines he already approved. It read as not listening.

**How to apply:**
- He flags a span → reply with options for that span, full stop. Don't reprint the surrounding draft unless he asks.
- If the fix genuinely forces changes elsewhere, say so in one line and ask before touching the rest — don't assume.
- A whole-artifact rewrite is warranted only when he asks for one ("refais tout", "réécris le mail"). "This phrase is bad" is not that.
- Default to the smallest diff that satisfies the ask. Ties to [[feedback_one_artifact_per_ask]] and [[feedback_concise_reminder_when_forgotten]].
