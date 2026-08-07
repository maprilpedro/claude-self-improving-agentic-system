---
name: The audit repo works by PR, never commit to main
description: aem-coworker-audits is Pedro's repo and it runs on feature branches + PRs. Claude committed straight to local main on 2026-08-06 and he stopped it. Check the workflow before writing to any repo of his.
metadata:
  type: feedback
---

**The rule.** `~/GitHub/aem-coworker-audits` (remote `OneAdobe/aem-coworker-audits`) is developed **branch → PR → merge**. On 2026-08-06 it had PRs #9 through #13 in a single day. **Never commit to `main`, never push, never open a PR without asking.**

**What happened.** Pedro asked for an agent axis to be wired in. Claude did the work, ran the tests, and committed straight to local `main`. He replied *"tu as fait un PR sur les audits ??"* — alarm, not curiosity. Nothing had been pushed, but the commit sat one ahead of `origin/main` while **PR #13 was open**, which would have handed him a divergence to untangle. He then said *"ne touche a rien - j'ai fait faire une PR15 et je la review"* and reverted the working tree himself.

**Why it matters beyond tidiness.** The repo is **private, redacted, and outward-facing** — its reports get linked into Slack channels ([[reference_aem_coworker_audits]]). A commit that lands without review can put a number in front of thirty people. The PR *is* the review step, and Pedro is the reviewer.

**How to apply.**
1. **Look before writing.** `gh pr list --repo <slug> --state all --limit 5` and `git log --oneline -5`. If recent work arrived through PRs, that is the workflow.
2. Do the work on a **feature branch**, run the tests, and **stop**. Report what is on the branch and let him open the PR.
3. If a commit has already landed somewhere it should not, **say so immediately and factually** — what is local, what is pushed, what is on a remote — and offer the reset. Do not quietly fix it.
4. This generalises: **the repo's own conventions are a fact to check, not to infer from the task.** Same class of error as banking a Slack deliverable from the plan instead of reading the thread ([[feedback_confirm_ask_before_producing]]).

**Related:** [[reference_aem_coworker_audits]] · [[feedback_pedro_writes_claude_critiques]] (he owns the outward artifact; a merged commit in a shared repo is one) · [[feedback_no_internal_to_personal_repos]]
