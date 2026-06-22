---
name: confirm-ask-before-producing
description: "Confirm who an ask is addressed to, and read the source before producing an artifact or characterizing it."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 75def9b2-7431-4617-a2f8-4050b1882aed
---

Two misfires in the 2026-05-22 Ian NorthStar session. (1) Claude read *"Would you put together what AEM needs from a central memory layer?"* as a delegation to itself and pre-drafted the requirements doc — but Pedro had addressed that line to **Ian** in the thread. (2) Claude characterized Ian's "Claude Token costs" blog ("premature compaction → monolith reasons worse") from a one-line gloss without reading it; the post's actual thesis was MCP-vs-Skills token cost (MCP manifest ~2K–15K/turn even when unused vs Skill ~200–500, hook 0).

**Why:** Pedro posts Claude's drafts under his own name and brings them to senior architects (Ian, Bertrand, VP-level). Producing the wrong artifact wastes his time; standing behind an unread source risks him being caught at exactly the altitude where accuracy matters most. Acting on an assumed ask and paraphrasing-without-reading both erode trust where it's most expensive.

**How to apply:** Before producing an artifact, confirm who/what the ask is for — especially when the trigger is a quoted line that could be addressed to a third party. Before attributing or characterizing a source (blog, doc, JIRA, transcript), read it; if only a summary is available, say so explicitly and offer to read the source. When handing Pedro reply text, mark which lines are sourced quotes vs Claude's inferences/positioning moves. Related: [[feedback_jira_mcp_before_opining]], [[feedback_dont_overread_vp_quotes]], [[feedback_edit_the_span_not_the_artifact]].

**Reinforced 2026-06-22 (VP escalation, costly).** Drafting Pedro's AI-Assistant→Coworker escalation (to Bertrand, cc Eugene/Silvia), Claude wrote *"the Coworker rail is not GA, maybe this week, else post-shutdown"* and stated it as fact. It was **false** — three distinct surfaces were conflated: the **rail** (targeted end-July, not "this week"), the **dedicated Coworker app** (cutting to its UI "this week", Josh 25:11), and the **AO-app-replacement page** ("this week else post-shutdown", Tim 36:12). Pedro caught it: *"tu es 100% sûr ? qu'est-ce qui a été capturé ?"* then *"c'est un mail pour un VP, vérifie tout contre le transcript, pas d'invention, pas d'inférence."* **Rules that earn their keep here:** (1) for any high-stakes external artifact (VP/exec audience), build a **source-cited fact ledger first** — every claim mapped to a verbatim quote + speaker + timestamp — *then* draft only from it; don't summarize from working memory. (2) **Never conflate distinct entities/dates/systems** — when several things share a word ("this week", "Coworker", "rail"), pin each to its own source before using it ([[feedback_dont_conflate_pattern_with_object]]). (3) When Pedro pushes *"no inference, give refs"*, that is the bar for the whole artifact, not a single line. A wrong fact in front of a VP is the exact altitude where accuracy is most expensive ([[feedback_voice_drafts_mark_inference]]).
