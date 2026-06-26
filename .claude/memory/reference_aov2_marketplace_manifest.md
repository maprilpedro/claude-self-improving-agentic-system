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

## Co-presence is a MANIFEST property, not a path/bridge property (2026-06-26, Bertrand thread)

Bertrand's worry: the AOv2 bridge (Plan B) "deports skills from where they'd be tested (Coworker, with all the others)." Technically it does **not** hold:
- The bridge still puts the migrated skills **into an AOv2 manifest** (EPA Plan B slide, verbatim: *"integrate this into an AOv2 manifest consumed by EPA as a technical agent through A2A"*). So the skills are co-present with that manifest's siblings either way.
- **Nothing runs as a lone skill.** "Isolated behind AIA" was a Claude mis-framing (corrected by Pedro). On Coworker, skills already run many-per-manifest today (e.g. `aem-aia` = 7 plugins + inherited AEP).
- The only real variable = **which skills share a manifest** — a manifest-composition choice, identical whether reached via the bridge or native Coworker. The bridge does not change co-presence.
- The only thing never co-present today = skills from **different agents** (each agent = its own manifest: aem-aia, aem-onboarding, dea-aia…). True **with or without the bridge**. Cross-agent co-presence only happens if someone builds a manifest that merges them.

→ Consequence: selection is testable **now** on an existing Coworker manifest, independent of the bridge. The bridge is a delivery-timing question (get skills to AIA customers before Coworker GA), not a test-environment question. Don't conflate "skills delivered via the bridge" with "where selection gets validated." Selection intra-manifest exists today; cross-agent selection is a manifest-design choice, not a migration milestone.
