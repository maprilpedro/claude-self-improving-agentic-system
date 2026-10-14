---
name: feedback-recall-without-prompts
description: Session-start recall must not trigger approval prompts. Use the Read tool and single simple commands, never compound cd/pipe Bash.
metadata:
  type: feedback
---

On 2026-10-14 a plain "recall" cost Pedro 5 to 6 approval prompts.

**Why:** the reads were done with compound Bash (`cd ...; cat | head -c`, `sed -n "$(grep ...)"`, `echo` chains). Compound commands and `cd` don't match any `Bash(x:*)` allow rule, so auto mode asks every time. The Read tool on files inside the repo or the vault needs no approval.

**How to apply:** for session start ([[feedback_session_start]]), read `project_aem_agents_intelligence.md`, `project_experience_hub.md`, `watches.md`, `.claude/state.md` with the Read tool (use `offset`/`limit` for the top blocks). Use Grep tool, not shell grep. If Bash is needed, one command, no `cd`, no pipes.
