---
name: Detect and offer to refresh stale Current Status / Focus sections
description: Status files drift when one is actively maintained and adjacent ones aren't — actively scan for staleness before adding new tasks, offer to refresh
type: feedback
---

Rule: Before adding tasks to a Status & Todo file, scan the Current Status and Focus sections for date lag vs. current reality. If they are >2 weeks behind, flag it and offer to refresh — don't add new tasks on top of a stale frame.

**Why:** Confirmed April 23 2026. The AI-Assistant Status & Todo file Current Status section was frozen at April 2 (Felix integration pending, hosting not started, JIRA pipeline not finalized). Actual state on April 22: Felix pipeline live and VP-sponsored, hosting cert approved, JIRA pipeline trialed on Governance Agent, W1 upgrades in progress, new Varun workstream, new Rubin workstream. Pedro accepted the refresh offer instantly ("refresh please") — the stale frame was a known problem he hadn't gotten to. The EH file was current because it's the active surface; the AI-Assistant file drifted because nobody updates it directly.

**How to apply:** When editing a Status & Todo file, read the Current Status section first. Compare its dates to recent commits, recent memory entries, and recent meeting notes. If there's a >2-week lag: tell Pedro "the Current Status section is dated X — reality has moved (summarize one line). Refresh first?" Don't silently add new tasks to the old frame — that compounds the drift. Also check "Focus — Do in This Order" tables for items already shipped or shifted.
