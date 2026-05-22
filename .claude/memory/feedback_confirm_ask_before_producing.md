---
name: confirm-ask-before-producing
description: Confirm who an ask is addressed to, and read the source before producing an artifact or characterizing it.
metadata:
  type: feedback
---

Two misfires in the 2026-05-22 Ian NorthStar session. (1) Claude read *"Would you put together what AEM needs from a central memory layer?"* as a delegation to itself and pre-drafted the requirements doc — but Pedro had addressed that line to **Ian** in the thread. (2) Claude characterized Ian's "Claude Token costs" blog ("premature compaction → monolith reasons worse") from a one-line gloss without reading it; the post's actual thesis was MCP-vs-Skills token cost (MCP manifest ~2K–15K/turn even when unused vs Skill ~200–500, hook 0).

**Why:** Pedro posts Claude's drafts under his own name and brings them to senior architects (Ian, Bertrand, VP-level). Producing the wrong artifact wastes his time; standing behind an unread source risks him being caught at exactly the altitude where accuracy matters most. Acting on an assumed ask and paraphrasing-without-reading both erode trust where it's most expensive.

**How to apply:** Before producing an artifact, confirm who/what the ask is for — especially when the trigger is a quoted line that could be addressed to a third party. Before attributing or characterizing a source (blog, doc, JIRA, transcript), read it; if only a summary is available, say so explicitly and offer to read the source. When handing Pedro reply text, mark which lines are sourced quotes vs Claude's inferences/positioning moves. Related: [[feedback_jira_mcp_before_opining]], [[feedback_dont_overread_vp_quotes]].
