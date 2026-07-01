---
name: reference_aov2_marketplace_manifest
description: "AOv2 skill packaging — marketplace ≠ manifest. Convergence/overlap/selection happens at the MANIFEST, not the marketplace. Multiple marketplaces is by design. Only 2 of 4 AEM repos are real marketplaces."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 11c062e2-f578-486b-b95f-3dbff798ebdf
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

## The real AEM marketplace set (from the manifests) — the audit hit partly the wrong repos (2026-06-26)

The "4 AEM marketplaces" the audit (`GitHub/adbe-skill-audit`) used was partly wrong. The **manifest-declared** `known_marketplaces` across the live `aep-aia` manifests are the truth:
- `aem-aia-extensions` (Adobe-AEM-Foundation) — aem-aia "AEM Coworker"
- `AEM-Assets-Adobe/ao-plugin-extensions-aem-onboarding` — Assets Onboarding (Ian Reasor)
- `aem-content-fragments-extensions` (Adobe-AEM-Sites)
- `aemforms-aia-extensions` (adobe-aem-forms) — **NOT `forms-skills`** (what the audit used)
- `aem-guides-extensions` (OneAdobe)
- `dea-extensions` (Adobe-Experience-Platform) — Data Engineering
- **+ ~12 AEP/Analytics marketplaces inherited via `cx-coworker`** (aia, cja, target, ajo, loyalty, …)

→ `excat` (experience-catalyst) is referenced by **no** manifest = confirms it's a standalone app, not an AOv2 marketplace. **Re-point the overlap audit at the manifest-declared marketplaces** before the empirical run for Ian. Inheritance chain: `cx-coworker-base` → `cx-coworker` → `aem-* agent` → `cx-coworker-{customer}`. Full verified flow: vault `AAI - Project Folder/AEM Skills Flow — Front Door to Skill Selection (2026-06-26).md`.

## The one-AEM-manifest proposal + the runtime constraints (thread-confirmed 2026-06-23→26, #p42-architecture)

**Ian Reasor** (`ireasor@`, AEP/Coworker eng — NOT Ian Boston) opened **PR `ao#5388`** proposing `aem-aia.yaml` as a **centralized all-AEM manifest** to share, with the **OneAEM MCP included → baseline functionality without writing skills** (fall back to the MCP when no explicit skill matches). Merged to the queue 06-26. Landing position: *"One manifest that contains all AEM skills"*; per-customer manifests **not a feasible strategy — no self-serve** (but custom ones like Air India's `cx-coworker-air-india.yaml` still exist, hand-authored).

Runtime facts settled in-thread (correct any "layer base + extension live" assumption):
- **Only ONE manifest is active at a given time** (Ankush Malhotra, empirical). Two manifests both extending a base do NOT aggregate their skills in one turn.
- **`manifest_id` is assigned before the prompt, switchable between turns, not resolved per-turn.** Cached unless the user switches.
- **"Extending manifests"** exists in the docs, but composition that works today = **authoring-time** (one composed manifest per surface, e.g. Air India references plugins across products) resolving to one active manifest — NOT two live manifests layered. This is the inheritance chain above.
- Satya Deep raised the **fat-manifest context cost** (more tool descriptions = more tokens); the Air India custom manifest balances it by composing per use-case.

**The unresolved tension (Pedro's wedge):** an *exhaustive* all-AEM manifest = ~the full AEM skill population in one manifest, which collides with the **10-15-visible / overlap→50% ceiling** (Ian Boston's separate skill-selection thread, 06-23). Reasor wants exhaustive (no self-serve for custom); Boston posts the ceiling; Ankush/Satya push composed-per-customer. **Pedro's overlap audit (128 skills / 4 repos) is what resolves it either way** — a clean non-deferred set for the single manifest, OR authorable scoped manifests if it splits by surface (composition needs the overlap map to write cleanly). **Pedro's reply posted 07-01** claiming the non-deferred-set curation layer on Reasor's PR ([[project_aem_agents_intelligence]]). Ties [[feedback_dont_conflate_pattern_with_object]] — two Ians, don't merge them.
