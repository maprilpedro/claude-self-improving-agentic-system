# Two-Consumer Pattern Proves Platform-Level Root Cause

_Section: Operating Discipline — part of `leadership/`; router = README.md._
- **Date identified**: 2026-04-01
- **Source**: Felix's cross-region report + Lara Nonino's Governance Agent report — both pulling from the same AEP source with the same compliance exposure.
- **Pattern**: When a problem appears in one consuming system, the root cause could be in that system. When the same problem appears in a second, independent consuming system, the root cause is almost certainly in the shared upstream platform. Pedro correctly reframed the compliance risk from "Felix's pipeline issue" to "AEP platform problem" once Lara's separate pipeline showed the same exposure.
- **Strategic value**: The two-consumer framing changes the conversation from "fix this team's engineering" to "the platform needs to address this." That's a different escalation path, a different owner, and a different solution scope. It also prevents point-fix solutions that leave the root cause intact.
- **Application**: Whenever you're diagnosing a shared infrastructure problem, ask: who else consumes this upstream source? If two independent consumers have the same problem, you have a platform issue. Frame it that way to leadership.
