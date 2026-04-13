---
name: Session setup commands
description: Always run /color orange and /rename ADBE-PM-ASSISTANT at the start of every session
type: feedback
originSessionId: 2dba12ec-aa30-4d93-b3b6-91e423b1fff5
---
At the start of every conversation, remind the user to run these two commands if they haven't already:

1. `/color orange`
2. `/rename ADBE-PM-ASSISTANT`

**Why:** These are Claude Code UI slash commands — only the user can invoke them. They cannot be automated via hooks or run by Claude directly. Updated April 10, 2026.

**How to apply:** At session start, prompt the user: "Don't forget: /color orange and /rename ADBE-PM-ASSISTANT"
