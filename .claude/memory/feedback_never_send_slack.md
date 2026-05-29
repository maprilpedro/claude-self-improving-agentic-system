---
name: feedback-never-send-slack
description: Hard rule — never send Slack messages on Pedro's behalf. Draft only; he pastes himself. Reading/searching Slack is fine.
metadata:
  type: feedback
---

**HARD RULE: never send Slack messages.** Do not call `slack_send_message`, `slack_send_message_draft`, `slack_schedule_message`, reply, or post anything to Slack on Pedro's behalf — ever. Draft the text, hand it to Pedro, he pastes it himself. Reading and searching Slack (read_channel, read_thread, search) is fine and encouraged.

**Why:** The Slack send tool auto-appends "Sent using @Claude" to the message, which breaches [[feedback-keep-claude-private]] in public, in front of leadership (it leaked on Pedro's first reply in the #aem-agents AOv2 thread, 2026-05-29, visible to Bertrand/Apoorva/Ian). Posting to Slack is also outward-facing and irreversible. Pedro made this a hard rule after that leak.

**How to apply:** When Pedro approves a Slack reply, output the final text in a code/quote block for copy-paste. Never offer to send it. If he says "send"/"envoie", treat it as "give me the final text" — confirm he pastes it, do not call a send tool.
