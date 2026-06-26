---
name: reference_aov2_marketplace_manifest
description: AOv2 skill packaging — marketplace ≠ manifest. Convergence/overlap/selection happens at the MANIFEST, not the marketplace. Multiple marketplaces is by design. Only 2 of 4 AEM repos are real marketplaces.
metadata:
  type: reference
---

# AOv2 skill packaging — marketplace ≠ manifest (live-verified 2026-06-26)

Whenever the question is "unify the AEM skills" / "put them in the same marketplace" / "is the multi-marketplace split a problem" — this is the corrective frame. The convergence unit is the **manifest**, not the marketplace.

## The model (sourced: `Adobe-Experience-Platform/ao` → `docs/reference/domains/plugins-and-skills/`, author ssree, under review 2026-03)

```
N marketplaces (GitHub repos, catalog sources)
   → plugins/skills INSTALLED into a MANIFEST (scope: application > tenant > user, most-specific-wins)
   → the manifest = the runtime co-present set
   → the LLM selection function runs over the manifest
```

- A **marketplace** = a GitHub repo carrying `.claude-plugin/marketplace.json` (format compatible with Claude Code plugin docs). Registered → shallow-cloned for catalog browsing.
- A **manifest** binds plugins via `plugin_ref = plugin@marketplace`, so **one manifest pulls plugins from many marketplaces**. Bindings keyed `(plugin_ref, manifest_id)`.
- **Multiple marketplaces is BY DESIGN**, not a defect. AEP's own diagram shows "Marketplace Repos (GitHub)" plural. Teams keep their own repos; convergence is at the manifest.
- This is the same fact as [[reference_skyline_p42_orglist]]-adjacent "selection is manifest-scoped" — selection/overlap is bounded to whatever is co-present in a manifest, testable via a constructed manifest.

## The "4 AEM marketplaces" claim is imprecise (live-verified 2026-06-26 via `pedrofer_adobe` gh)

4 distinct GitHub repos across 3 orgs — but only **2 are real AOv2 marketplaces**:

| Repo | marketplace.json? | What it is |
|---|---|---|
| `Adobe-AEM-Foundation/aem-aia-extensions` | ✅ | real marketplace (shared AI-Assistant catalogue, multi-team) |
| `Adobe-AEM-Sites/epa-experience-generation-extensions` | ✅ | real marketplace (EPA / Experience Generation) |
| `Adobe-AEM-Foundation/aem-experience-catalyst` (excat) | ❌ | full standalone app (docker, deploy, operator) — not a marketplace |
| `adobe-aem-forms/forms-skills` | ❌ | custom packaging (`publish.sh`, `.mcp.json`) — not a marketplace |

→ Forms + excat must be repackaged to `marketplace.json` (or standalone-skill upload) to enter AOv2 at all. Today only AIA + EPA are registrable.

## Implication for the empirical eval owed to Ian (see [[project_aem_agents_intelligence]] 06-26)

Do NOT consolidate marketplaces. Construct an **AEM manifest** that makes the candidate skills co-present, run the AEP selection eval over it. The manifest IS the test-harness scope. Ties [[reference_coworker]] + the skill-overlap audit (`GitHub/adbe-skill-audit`).
