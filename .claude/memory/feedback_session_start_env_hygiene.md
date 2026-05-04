---
name: Session-start env-var hygiene for dual-project memory loads
description: For this project (EH+AAI dual-load), avoid CLAUDE_CODE_DISABLE_1M_CONTEXT=1 and early CLAUDE_AUTOCOMPACT_PCT_OVERRIDE in .claude/settings.local.json. Cold load is chunky, autocompact triggers near-immediately.
type: feedback
originSessionId: 6a27bd23-6c26-4487-9d24-4161e45e13a5
---
For this project specifically (EH + AAI dual-project memory load: 2× project memory files + 2× Status & Todo + knowledge `INDEX.md` routing), keep 1M context **on** and let autocompact fire at the default threshold rather than at 80%.

**Why:** May 4, 2026 session start surfaced that two env vars in `.claude/settings.local.json` had been degrading cold loads — `CLAUDE_CODE_DISABLE_1M_CONTEXT: '1'` plus `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE: '80'`. The combination meant sessions began near the compact threshold and triggered an early autocompact before substantive work could land. Pedro asked for explanation, then for project-only removal. Removed today.

**How to apply:**
- If a future session feels like context is tight from the very first turn, check `.claude/settings.local.json` for an `env` block. If 1M context is off or autocompact threshold is below default, that's likely the cause.
- Don't add either env var back without an explicit reason. This project's session-start ritual (read EH + AAI memory + INDEX.md + Status & Todo) is intentionally chunky.
- Generalizable: any Claude project with multi-project memory architecture (this repo's pattern) will have the same sensitivity. If a similar setup is created for another domain, mirror the absence of these env vars.
