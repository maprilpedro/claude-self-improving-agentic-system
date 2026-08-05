---
name: reference-aem-coworker-audits
description: "The audit repo OneAdobe/aem-coworker-audits — five audits over the AEM Coworker skill estate, published redacted into git. What each one answers, how to run it, and where the pseudonym salt lives."
metadata:
  node_type: memory
  type: reference
---

# aem-coworker-audits — the audit agent for the AEM skill estate

**Built 2026-08-05.** Local `~/GitHub/aem-coworker-audits`, remote `OneAdobe/aem-coworker-audits`, **private**, Adobe service_id `615301`.

🔑 **What it is FOR, said by Pedro 2026-08-05: showing progress while the teams migrate.** They are renaming skills and filling `domain` / `when-to-use` right now, so the audit is a **measuring instrument for a migration in flight**, not a one-off diagnostic. Consequences: (1) it has to be **re-run on a cadence** — the 08-05 run is the baseline; (2) the interesting number is the **delta**, not the snapshot; (3) the marketplace repos keep their git history and every collector already takes a `ref`, so **earlier snapshots can be backfilled later** and nothing is lost by not starting the series today; (4) a trend must **re-grade the past with current rules** rather than compare stored numbers, or a vocabulary edit reads as thirty teams renaming overnight.

Design ported from **Gerald Prendi's `Adobe-AEM-Foundation/governance-agent-marketplace` PR #29**, credited in `CREDITS.md` + a `provenance:` block in the config. 🔴 **That repo is READ-ONLY — no PR, no branch, no issue, ever.** Pedro's standing instruction, 2026-08-05.

## The five audits

| Audit | Answers |
|---|---|
| `manifest-coverage-matrix` | which of the 215 AO manifests reach which AEM marketplace, per environment, with `D` declared / `i` inherited / `x` removed |
| `skill-routing-audit` | which skills compete for the router on one manifest, and which pairs are near-duplicates |
| `skill-vs-tool-audit` | which MCP tools face those skills, and whether a tool bypasses a skill |
| `skill-naming-audit` | every name against `aem-<application>[-<feature>]-<action>[-<qualifier>]`, with a proposed rename |
| `skill-disambiguation-audit` | whether `domain` / `when-to-use` / `when-NOT-to-use` exist **and say anything** the description does not |

A sixth, `skill-in-target-marketplace` (what is already in the consolidation destination vs what is not, by application), is designed and half-built on branch `feat/skill-in-target-marketplace`.

## The three things that make it different from PR #29

1. **`disabled_plugins` and `known_marketplaces[].policy` are honoured.** Both upstream resolvers compute a pure union up the `extends` chain and ignore them, so they over-report the roster on exactly the AEM manifests that matter.
2. **AEM's MCP tools are declared inline on the manifest**, not in the gateway directory. Reading only `config/cxo-ai-gateway/.../mcp_servers/` misses AEM's whole tool surface.
3. **Nothing hardcodes an org, repo, path or prefix.** `aem-audits.yaml` is the only place any of it appears, enforced by an AST test. Upstream's `AO_REPO` still points at a repo that was renamed (`Adobe-Experience-Platform/ao` → `aep-ai`).

## Running it

```bash
export AEM_AUDIT_SALT="$(security find-generic-password -s AEM_AUDIT_SALT -w)"
scripts/publish.py     # all five, redacted, into docs/runs/<date>/ + docs/STATUS.md
```

`docs/STATUS.md` is generated and carries the salt fingerprint **and** the commit it was produced from. `out/` is gitignored and holds unredacted runs. A `.githooks/pre-commit` refuses any commit carrying a customer manifest name or an internal ethos hostname.

🔴 **The salt lives in exactly one place: Pedro's macOS keychain, service `AEM_AUDIT_SALT`.** There is no team secret store — checked 2026-08-05, nobody knows which one it would be. Lose the laptop and every pseudonym changes with no error. The first salt was already lost this way on 2026-08-05, between two runs the same day, which is why the fingerprint stamp now exists.

## What may leave the repo

A finding names a skill, a plugin and a marketplace. It states counts and environments. **It never names a customer manifest, a customer org, or an internal hostname** — see [[feedback_no_internal_to_personal_repos]] for why that rule is not optional here.

`docs/findings/` is the home for judged output and is deliberately empty. A ranked pair is a candidate; a finding needs someone to write down the failing user request.

Related: [[reference_aov2_marketplace_manifest]] · [[reference_one_aem_mcp_repo]] · [[reference_aem_agent_ownership]]
