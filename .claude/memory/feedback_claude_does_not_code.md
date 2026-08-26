---
name: feedback-claude-does-not-code
description: "🔒 HARD RULE, 2026-08-07 — Claude does not write code. Ever. Not scripts, not audit collectors, not one-off analysis programs. Produce the answer, the table, the reasoning."
metadata:
  node_type: memory
  type: feedback
---

# 🔒 HARD RULE — Claude does not code. Ever.

**Pedro, 2026-08-07, verbatim:** *"mais attention, je ne veux pas que tu codes (plus jamais)."*

Said mid-task, while Claude was reading `aem-coworker-audits` source and shaping a measurement script for the name-vs-plugin error rate. **The instruction is unconditional and has no scope carve-out** — not "not this time", not "not without asking".

## What this covers

No writing or editing of code in any form. Scripts, audit collectors, one-off analysis programs, notebooks, config-as-code, "just a quick python to count this". **Including throwaway analysis in the scratchpad.** If the answer needs a computation, say what the computation is and what it would show, or read the already-published output and reason over it.

## What is still fine

Reading code and reporting what it does. Reading published JSON/markdown run output. Quoting counts that a report already produced. Reviewing and critiquing code someone else wrote — that is the same shape as [[feedback_pedro_writes_claude_critiques]], which is the sibling rule for prose.

**Why:** it is his repo, his craft, and his name on the commits. The same logic as the writing rule — an artifact Claude authored is one Pedro cannot defend line by line, and the audit repo is now public to the agent owners, so its code is an outward artifact ([[feedback_audit_outward_artifacts]]).

## ⚖️ EXCEPTION GRANTED 2026-08-26 — the cohort-file comparison, and it was Pedro's call

The rule above says it has **no override clause**, unlike its sibling [[feedback_pedro_writes_claude_critiques]]. So when Pedro asked twice for a 4,457-row vs 1,065-row cohort comparison across two `.xlsx` files, Claude **stopped and put the choice to him** rather than deciding. He chose *"lève la règle pour ce cas"*: read the two files, produce the discrepancy table, **keep nothing and commit nothing**.

**What this establishes, and what it does not.** It establishes that the rule is his to suspend, and that the honest move on a locked rule is to surface the conflict in one question rather than infer permission. It does **not** create a standing carve-out for spreadsheet work — he was offered the option to soften the rule to "no delivered code, throwaway analysis allowed" and **did not take it**. **The default remains: hand back the specification.** Ask again next time.

⚠️ **The handback still has to be worth having.** The spec given before the exception (inputs, operation, expected output, plus three data traps) was the right shape, and one of those traps — Paul writes org IDs **without** the `@AdobeOrg` suffix, Pedro's file **with** — was exactly what would have made a naive `VLOOKUP` return zero matches silently.

⚠️ **Same session, a second scope step:** he then asked for the 13 rows to be written into Paul's workbook and highlighted. That was treated as inside the same exception. **Writing values over Paul's `XLOOKUP` formulas was flagged to him, not done silently.**

**How to apply:** when a task seems to need code, stop and hand back the specification. Name the input, the operation and the shape of the answer, then let Pedro write it. Do not offer to code it "just to check". Do not narrate the script you would have written.

Sibling rules: [[feedback_pedro_writes_claude_critiques]] · [[feedback_audit_outward_artifacts]] · [[feedback_one_artifact_per_ask]]
