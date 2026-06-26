---
name: feedback_no_internal_to_personal_repos
description: Never relocate Adobe-internal content off the corporate boundary (personal GitHub, external services). Tools should fetch internal data at runtime, not store it. Surfaced 2026-06-26 when a push was correctly blocked.
metadata:
  type: feedback
---

Never relocate Adobe-internal content off the corporate boundary — personal GitHub accounts, external services, anywhere outside Adobe's org. A `--private` flag does NOT make it safe; private-on-a-personal-account is still off-boundary.

**Why:** 2026-06-26 — building `GitHub/adbe-skill-audit`, the push to Pedro's **personal** GitHub (`maprilpedro`) was blocked by the harness as data exfiltration. The committed files carried Adobe-internal specifics: `ao` monorepo file paths, the "April AEM Customer Service Outage" reference, engineer rosters (eval reviewers), **customer names** in manifest filenames (`cx-coworker-amex`/`-ibm`/`-servicenow`), internal repo names. The block was correct, not tatillon. Pedro chose **local-only, no remote.**

**How to apply:**
- A tool/audit repo should carry **generic scripts + instructions** and **fetch** internal data at runtime (via `gh` / live APIs), never **store** internal specifics in committed files.
- Before any push to a non-Adobe remote: scrub internal names, customer identifiers, internal paths, the outage references, eng rosters into a gitignored local doc — or keep the repo local-only.
- If Pedro asks to push internal content somewhere off-boundary, surface the boundary concern and let him decide (don't work around the block). Options to offer: scrub-then-push, push to an Adobe org instead, or local-only.

Ties [[feedback_keep_claude_private]], [[feedback_audit_outward_artifacts]].
