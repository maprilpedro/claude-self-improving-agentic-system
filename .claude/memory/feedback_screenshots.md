---
name: Save screenshots to project folder
description: Always save screenshots shared by the user to /screenshots in the project repo
type: feedback
---

When the user shares a screenshot, always save a description or extracted content to `/Users/pedrofer/GitHub/claude-self-improving-agentic-system/screenshots/` so it persists across sessions.

**Why:** Screenshots shared in conversation are lost when the session is cleared. The user lost Analytics report screenshots this way on April 2, 2026.

**How to apply:**
- When a screenshot is shared, create a markdown file in `screenshots/` with a descriptive name (e.g., `analytics-eh-workspace-20260402.md`)
- Include: what the screenshot shows, key data points visible, any relevant context
- Commit with `learn:` or `ref:` prefix
- The file becomes the persistent record — reference it in future sessions instead of asking the user to reshare
