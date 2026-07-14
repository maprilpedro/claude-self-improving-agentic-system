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

## 🔴 CORRECTION 2026-07-14 — MANIFEST ROUTING IS PER **USER**, NOT PER ORG. Read this before saying "one manifest per customer".

**Source, read at the source:** **Felix Delval's PR `ao#6710`** ("Add AEM Sites Trial user allowlist routing to Experience Production Agent", opened 2026-07-14), which explicitly **mirrors the `coca-cola-orgs-allowlist` / `coca-cola-user-allowlist` and `comcast` patterns already in prod**.

**The mechanism, verbatim from the PR:** an **org-scoped segment** (`members: [<org id>]`) uses **`member_metadata.specific_segment`** to narrow down to a **`scope_kind: user`** segment keyed on **`user.email`**. A manifest-targeting rule is inserted **ahead of** the org's default rule (e.g. `aem-orgs-to-aem-aia`), and **targeting rules are evaluated first-match**, so the narrower allowlist wins for those users while every other user in the org is unaffected.

- **→ A single ORG can run two manifests at once, split across its users.** Allowlisted users of AEM Sites Trial get `experience-production-agent`; everyone else on the same org keeps `aem-aia`.
- **→ "One manifest at a time" is still true — but the unit is the USER SESSION, not the customer.** ⚠️ **Do not say "customer X cannot have both manifests." Say "a single user cannot have both in one session, and routing is per user, so someone has to decide which users get which."**
- **Why it matters, concretely (2026-07-14, AMEX):** `multi-cf-edits` (the only real CF-editing skill) is in the **`epa`** marketplace; `discovery` (the only content-search skill) is in **`aia-extensions`** (the central manifest). Verified in `adbe-skill-audit/data/skills.json`. So one user cannot edit *and* discover fragments today — but the org can be split. **That distinction is the difference between a wall and a routing decision.**
- **The AEM side already commits to this config themselves** — `scoman_adobe` (Sergiu Coman) pushed to `config/aep-aia/.../segments` on 07-13. **There is no CODEOWNER on the segments path**, only on `config/**/manifests/cx-coworker.yaml` (→ `@Adobe-Experience-Platform/aep-ai-ao-committers`). **So these PRs have no automatic approver, which is why Felix's sat unreviewed.** Who to ping: **Ankush Malhotra (`amalhotr_adobe`)** — he wrote the Coca-Cola pattern and pushed to these exact files twice on 07-14; **Dan Moldovan (`dmoldova_adobe`)** for the targeting-rule half (he did `cx-coworker-prada`).

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
| `Adobe-AEM-Foundation/aem-experience-catalyst` (excat) | ⚠️ see correction | full standalone app (docker, deploy, operator) |
| `adobe-aem-forms/forms-skills` | ❌ | custom packaging (`publish.sh`, `.mcp.json`) — not a marketplace |

→ Forms + excat must be repackaged to `marketplace.json` (or standalone-skill upload) to enter AOv2 at all. Today only AIA + EPA are registrable.

> ### 🔴 CORRECTION 2026-07-09 — the excat and forms rows above were both over-stated. Do not repeat them.
>
> - **excat DOES ship `marketplace.json`** — two of them, nested: `resources/plugins/aem-excat-plugin/excat-marketplace/.claude-plugin/marketplace.json` and `.../excat-extended/.claude-plugin/marketplace.json` (verified 2026-07-09 against the `adbe-skill-audit` working copy). The 06-26 gh check evidently looked at the repo root. **The defensible claim is narrower: excat is not wired into the central manifest.** It is referenced by no manifest (that part of the 06-26 finding still holds). Say "excat is not in the central manifest — it ships its own marketplace but isn't wired in", never "excat is an app, not a marketplace".
> - **Forms is a real marketplace** — `adobe-aem-forms/aemforms-aia-extensions`, "the one we are using in coworker" (Satya, 07-07), with a real `marketplace.json`, 1 plugin, 2 skills. The `forms-skills` repo in the table above is the WRONG repo (the audit's original mistake, already flagged in the section below). Pedro swapped the audit source on 07-07 (commit `6854b2c`).
> - **`aem-aia-extensions` ships 10 plugins, and the bare "7" was the practitioner count mislabelled.** Verified 2026-07-09 from the working copy. **7 `practitioner/` plugins carry 19 skills** (aem-coding-plugin 6, aem-pipeline-troubleshooter 5, aem-cloud-manager-ops 3, aem-release-management 2, experience-replication 1, discovery 1, aem-workflow-ops 1) and **3 `system/` plugins carry 1 API-reference skill each** (cloud-manager-api, update-profile-api, aem-workflow-api). 22 skills total, exact. Say "10 plugins, 7 of them practitioner". The figure never went out to Reasor — his thread quotes no plugin count.
> - **🔑 ZERO of the 22 SKILL.md files carry `domain`, and zero carry `when-to-use`** (verified 2026-07-09). Every plugin is authored "AEM Team". **There is no agent attribution anywhere in the manifest data** — which is exactly why Ian Reasor, who co-owns this manifest, had to ask Pedro on 07-08 which agent two of the skills belong to. Skill→plugin is in the tree; plugin→agent is in nobody's head but the owning team's. This is the Playbook's `domain` ask, demonstrated by the manifest's own co-owner.
> - **🔴 RESOLVED, AND THE SENT NUMBER IS WRONG. Pedro's 07-08 message to Reasor says "only 5 of those 18 pairs are actually installed together in this manifest." The 07-07 snapshot (the one it was built on) has 8 pairs with both sides in `aia-extensions`.** Snapshot series, both-sides-in-aia: 07-01 = 4, 07-03 = 4, 07-07 = **8**, 07-09 = **8** (total flagged pairs 18/17/18/19; catalogue 132→134→99→102 after the 07-07 forms-scope swap). Of the 8, four pair a practitioner skill with its own `system/` API-reference skill (update-profile-api ×2, cloud-manager-api, aem-workflow-api) which are arguably not competing alternatives; that leaves **4**, not 5. **No definition reconstructs 5.** The two *real* either/or risks Pedro named are both same-plugin and both stand. Correct the count the next time the thread moves — event-driven correction is the pattern that already won with Satya (source swap, 07-07).
>
> ### 🖼️ WHAT BERTRAND ACTUALLY ASKED (screenshot read 2026-07-09) — the Coworker MANIFEST PICKER, not repos

His 07-07 question "quite a few AEM manifests in Coworker today, who owns what?" is captioned by a screenshot of the Coworker UI's **"Search manifests…" dropdown**, section **Application**. Visible entries (list scrolls, EPA may be below the fold):

| Picker entry | Manifest / marketplace | Owner |
|---|---|---|
| AEM AI Assistant (Markdown-only) | ? | **unknown** |
| **AEM Coworker** ✅ (his selection) | `aem-aia.yaml` → `aem-aia-extensions` (22 skills / 10 plugins) + One AEM MCP | shared, multi-team; every plugin authored "AEM Team"; Pedro curates |
| AEM Content Fragments Coworker | `aem-content-fragments-extensions` (Adobe-AEM-Sites) | **unknown** |
| AEM Forms Experience Builder | `aemforms-aia-extensions` (adobe-aem-forms) | Hemanta Gupta building; Satya Deep Maheshwari's side |
| AEM Guides AI Assistant | `aem-guides-extensions` (OneAdobe) | **unknown** |
| AEM Onboarding Coworker | `ao-plugin-extensions-aem-onboarding` (AEM-Assets-Adobe) | Ian Reasor (said so in-thread) |

**The picker is the "who owns what" surface, and it carries no ownership.** A user picks a manifest with no idea whose skills they get. The checkmark also makes the one-manifest-active-at-a-time rule visible to Bertrand directly.

His 2nd screenshot = Discovery running in the AEM Coworker manifest against WKND author: 3 API calls, reads the asset-search spec, HYBRID semantic match on "water", 20 images returned as a **markdown table** (#, Title, Path, Format, Size) + a "Search summary" line he praised. **"Results in MD mode" = the renderer gap made visible** — no asset-grid/tile renderer ported, markdown is Tim Lynn's fallback tier. Discovery's *logic* works on Coworker; its *rendering* is the degraded tier.

⚠️ **Altitude lesson.** The first draft answered with repos and PR numbers. Bertrand was looking at a dropdown. Read the attached images before drafting a reply to a screenshot-led question.

### 🔴🔑 METHOD FLAW IN THE AUDIT'S HEADLINE CLAIM (found 2026-07-09) — "0 cross-agent overlap" is not established by the data

**The audit repo already knew.** `docs/marketplaces.md` on `aia-extensions`: *"Shared AI-Assistant catalogue — multiple agent teams contribute into it (e.g. Sergiu / EDA puts `quiet-hours`, `update-free` here, not in a separate EDA repo). So 'intra-agent' here can hide a cross-team pair — route a flagged pair to the contributing skill's owner, not a single 'AI Assistant owner.'"* That also **answers Reasor's second question**: `quiet-hours` / `update-free-periods` are **Sergiu's, EDA** (repo-doc sourced, not data-declared).
>
> The snapshot's `intra` flag is computed as **`a_market == b_market`**. There is no agent field on a pair, and no agent field on a skill (`skills[]` = name, marketplace, has_domain, has_when_to_use, desc_len, desc_hash). Verified: 0 of 19 pairs have `intra != (a_market == b_market)`.
>
> So **"all 19 intra-agent, 0 cross-agent" actually means "all 19 intra-*marketplace*."** That is only the same statement if one marketplace = one agent. It is not: `aem-aia-extensions` is by its own description the **shared, multi-team AI-Assistant catalogue**. Discovery's skill, EDA's pipeline troubleshooters and the release-management skills all sit inside it. A pair spanning two of those agents would be **cross-agent and still labelled `intra: true`.**
>
> And the audit cannot fix this from the data, because **0 of 102 skills carry `domain`** — the field that would record which agent owns a skill. **The audit cannot see agent boundaries at all.** The "0 cross-agent" headline has been stated publicly (Reasor thread, Satya thread, Ian Boston 07-06). It is not false, but it is unproven and over-stated. **Restate it as "0 cross-marketplace; cross-agent is unmeasurable until `domain` exists."** This turns the audit's weakest claim into the argument for the `domain` field — and it should come from Pedro, before a skeptic finds it.
> - **EPA's manifest PR `ao#6028` is MERGED (2026-07-07, Felix Delval)**, title "feat(manifest): add Experience Production Agent manifest (dev + stage + prod)". Note what that means: it added **another AEM manifest**, it did not fold EPA into `aem-aia`. Merging created more of exactly what Bertrand is seeing, not less.
> - **`ao#5773` (Governance) is OPEN with CHANGES_REQUESTED from `trifan_adobe` since 2026-07-03** — that one was right.
>
> **Method note.** These slipped because a live-gh spot-check on 06-26 was carried forward for two weeks as settled fact and reused in a draft to Bertrand. Re-verify PR states and file contents before quoting them outward; they drift.

## Implication for the empirical eval owed to Ian (see [[project_aem_agents_intelligence]] 06-26)

Do NOT consolidate marketplaces. Construct an **AEM manifest** that makes the candidate skills co-present, run the AEP selection eval over it. The manifest IS the test-harness scope. Ties [[reference_coworker]] + the skill-overlap audit (`GitHub/adbe-skill-audit`).

## Co-presence is a MANIFEST property, not a path/bridge property (2026-06-26, Bertrand thread)

Bertrand's worry: the AOv2 bridge (Plan B) "deports skills from where they'd be tested (Coworker, with all the others)." Technically it does **not** hold:
- The bridge still puts the migrated skills **into an AOv2 manifest** (EPA Plan B slide, verbatim: *"integrate this into an AOv2 manifest consumed by EPA as a technical agent through A2A"*). So the skills are co-present with that manifest's siblings either way.
- **Nothing runs as a lone skill.** "Isolated behind AIA" was a Claude mis-framing (corrected by Pedro). On Coworker, skills already run many-per-manifest today (e.g. `aem-aia` = **10 plugins** + inherited AEP; corrected 2026-07-09, was 7).
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
