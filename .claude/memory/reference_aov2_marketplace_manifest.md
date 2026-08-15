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

## 🟢🔑 2026-08-14 — THE OFFICIAL DOC SAYS IT IN ONE LINE. QUOTE THE DOC, NOT THE INFERENCE.

**The question that keeps being asked:** if we declare `aem-aia-extensions` in the `cx-coworker` manifest, do all its plugins come in automatically, or do we list them one by one? **Answer: one by one.** And AO's own developer reference states it, so this never needs to be argued from a code read again.

**📕 The two pages, both public-internal:**
- **Manifests** — https://aep-ao.pages.adobeitc.com/developer-reference/manifests/ (source `docs/public/site/developer-reference/manifests.md` in `Adobe-Experience-Platform/aep-ai`)
- **Plugins & Marketplaces** — https://aep-ao.pages.adobeitc.com/developer-reference/plugins/ (source `docs/public/site/developer-reference/plugins.md`)

**🔑 The field table, verbatim, and the second row is the sentence to cite:**

| Field | Description | End-user impact |
|---|---|---|
| `plugins` | Pre-installed plugins (`ref: name@marketplace`) | **Active out of the box** — users get these skills without changing settings |
| `known_marketplaces` | Registered marketplace repos | Makes plugin catalogs **browsable** in Settings > Plugins **(does not auto-install)** |

**The five-step lifecycle from the plugins page** — Register marketplace → Sync content → **Install plugin into manifest** → Bootstrap on startup → Auto-update on sync. **Declaring the marketplace is step 1; step 3 is what loads.**

**⚠️ Three fields nobody in the AEM threads has mentioned, all documented on the same page:**
- **`visible_marketplaces`** — *"Manifest-declared marketplaces are hidden from Settings > Marketplaces by default; only allow-listed ones appear."* **`cx-coworker.yaml` does not carry the key** (verified on `main` 2026-08-14), so `aem-aia-extensions` will not show on that tab. Display only, plugins stay installable — **but someone checking AEM's presence via that tab will see nothing and report a failure.**
- **`marketplace_hiding: disabled`** — the documented escape hatch that turns the allowlist off entirely.
- **`plugin_deduplication_strategy`** — *"Earliest-listed marketplace in `known_marketplaces` wins; off by default."* ⚠️ **`cx-coworker` has it ON (`overwrite`)**, with ~21 marketplaces declared, so **where `aem-aia-extensions` is inserted in that list decides who wins a plugin-name collision.** Insert high.

**🔴 CODEOWNERS, read live 2026-08-14 — and it CORRECTS the team name recorded further down this file.**
```
# Base manifests — changes affect all customers. High blast radius, requires explicit approval.
config/**/manifests/cx-coworker.yaml @Adobe-Experience-Platform/aep-ai-review-bypass
```
The 07-14/07-17 entries below say `@Adobe-Experience-Platform/aep-ai-ao-committers`. **Today's file says `aep-ai-review-bypass`.** Either it was renamed or it was misread; **use `aep-ai-review-bypass` and re-check before quoting.** Membership is not listable without `admin:org`, which Pedro's account lacks. ⚠️ **There is NO CODEOWNERS rule for the `.ao/manifests/` copy.**

**⚠️ THERE ARE TWO COPIES OF THE MANIFEST AND ONE HAS ALREADY DRIFTED.** `.ao/manifests/aep-aia/cx-coworker.yaml` and `config/aep-aia/environments/{dev,stage,prod}/manifests/cx-coworker.yaml`. The `.ao/` copy carries its own admission that the gateway MCP servers were *"synced from config/aep-aia/environments/prod/manifests/cx-coworker.yaml"* and that **"this `.ao/` copy never got the backport"**. **Which one the runtime reads is unknown** — Pedro asked the architects on 2026-08-14 10:28 (`#p42-architecture`, ts `1786696117.382779`), unanswered at time of writing.

**🔑 WHO WRITES THE PR: THE PRODUCT TEAM, NOT A COWORKER ENGINEER.** The last 15 commits on the prod `cx-coworker.yaml` are each authored by the owning product team (Target by `psangra_adobe`, GenStudio by `jedelson_adobe`, data-validation by `psnep_adobe`, …). **AEM has done it five times**, all Governance: `gprendi_adobe` (Gerald Prendi) ×3 and `amoratinos_adobe` (Alejandro Moratinos) ×2. **`pfaffm_adobe` (Marc Pfaff) has authored zero** — he approved one and is CODEOWNER on `governance_mcp.yaml`, a different path. Approvals observed in practice: `lnonino_adobe`, `slohiya_adobe`, `trifan_adobe`, and the AEM authors approving each other.

**⏱️ THE ONLY REAL PRECEDENT FOR AN INITIAL ADD, AND IT IS THE NUMBER TO PLAN WITH.** `aep-ai#5773`, *"feat(cx-coworker): enable experience-governance plugin OOTB on prod"*, Gerald Prendi. One reviewer, **Alex Trifan**: `CHANGES_REQUESTED` 2026-07-03, `APPROVED` 2026-07-10, merged 2026-07-10. **Roughly ten days from open to merge.** Everything faster in the history is a **version bump on an already-present plugin**, which is a different operation. ⚠️ **What Trifan asked to change was never read — do that before seven teams open the same shape of PR.**

**🔴🔑 ADDENDUM 2026-08-15 — THREE AXES GET CONFLATED, AND THE THIRD IS THE ONE THAT DECIDES. Verified on `main`.**
- **AO deployment environment** (`config/aep-aia/environments/{dev,stage,prod}/`) — chosen by which shell the user opens.
- **AEM environment** — **independent**. `api_configs.aem` is `kind: dynamic` with `host_allowlist: adobeaemcloud.com` and the description *"Pass the full https AEM author URL as path"*, so a **stage manifest can drive a prod AEM author**. Same for `aem_delivery`.
- **IMS org** — the gate nobody checks first. A prod org lives in `environments/prod/segments/`; the stage shell authenticates against stage IMS. **`38931D6666E3ECDA0A495E80@AdobeOrg` (AEM Showcase) is in prod `aem-orgs.yaml` + `aem-onboarding-orgs.yaml` and in ZERO of the 30 stage segment files.** → **A prod org cannot be tested on the stage shell, whatever the manifest says.** Cross-ref [[reference_coworker_enablement]], which already carried the segment rule.

**🔴 `prod/cx-coworker.yaml` DECLARES NO `api_configs` AT ALL.** dev and stage each declare one block of ten. **So porting the plugin list to prod without also porting `api_configs` ships AEM skills that cannot call AEM.** On prod, `aem` / `aem_discovery` / `cm` are carried by **`aem-aia`**, not by `cx-coworker`. **This is the uncosted half of the "just push it to prod" plan.**

**⚙️ WHICH API CONFIGS FOLLOW THE ENVIRONMENT, AND WHICH DO NOT.** `aem` and `aem_delivery` are `kind: dynamic` → environment-free. **`cm` is environment-bound on two independent grounds**: `base_url_env: CLOUD_MANAGER_URL` follows the deployment, **and** the client key differs (`agent-orchestrator-stage` in dev+stage vs `aep-agent-orchestrator` in prod `aem-aia`) — two distinct registrations, so Cloud Manager, pipeline-troubleshooter and anything on `cm`/`cm_pat`/`cm_logs` cannot reach a prod program from AO stage. **`aem_discovery` is undecidable from the repo** — identical key (`aem-assets-frontend-1_assetsui`) in every environment, and `AEM_DISCOVERY_URL` is server-side. **Only AO ops can answer it.**

**🟢 THE ESCAPE HATCH THAT ALREADY EXISTS AND AEM DOES NOT USE.** The prod manifest carries per-server `env_overrides` with a `stage:` branch, commented *"stage IMS users (incl. dev cluster)"* — CJA, Experimentation, AJO, ajob2b-prime, GenStudio, Marketo and Workfront all declare one. **Copy the pattern instead of inventing a stage-shell plan.**

**🔴🔑 AND THERE IS NO PROCESS DOC.** The reference documents the *fields* and a CLI/API `plugins/install` that targets a local manifest. **Nothing documents the human path for the versioned prod manifest** — who opens the PR, who approves, how long it takes, that there are two copies. **Pedro is about to run seven teams through that path; writing the missing ten lines and getting them merged into `developer-reference` puts his name on the doc everyone follows afterwards.** Cheap, real gap, and unclaimed.

## 🔴🔑 CORRECTION 2026-07-17 — READ THIS BLOCK FIRST. Three things below were verified against `Adobe-Experience-Platform/ao` @ `main` on 2026-07-17 and three earlier claims in this file are wrong or over-stated.

**1. AIR INDIA DOES NOT COMPOSE ACROSS MARKETPLACES. Do not cite it as the composition precedent.** `cx-coworker-air-india.yaml` declares **one** marketplace, `Adobe-Experience-Platform/rtcdp-aia-marketplace` at **ref `air-india`** (a dedicated branch), and all 11 plugins resolve to it, including `aem-experience-production@air-india-marketplace`. That is a **copy-everything-into-a-branch** pattern, effectively a fork. The line further down this file — *"Air India references plugins across products"* — is true about product **domains** and **false about the mechanism**. ⚠️ Citing it argues FOR a fork, which is the opposite of Ian Boston's consume-vs-fork principle.

**2. THE REAL MULTI-MARKETPLACE PROOF, AND AEM ALREADY DOES IT.** `known_marketplaces` is a list and plugin refs are `plugin@marketplace`, so one manifest legitimately pulls from several. Verified in prod:
- **`aem-aia.yaml` itself declares TWO marketplaces** — `Adobe-AEM-Foundation/aem-aia-extensions` + `Adobe-AEM-Foundation/governance-agent-marketplace`. **AEM's own central manifest already composes. Adding EPA's marketplace is adding a row to a list that already has two, not inventing a pattern.**
- `cx-coworker.yaml` pulls across **different GitHub orgs** — `aia-extensions` (Adobe-Experience-Platform), `cja-extensions` (AdobeAnalytics), `target-extensions` (Adobe-TnT), `ajo-marketplace` (Adobe-CJM), `experimentation-extensions`, `product-support-marketplace`, `data-validation-extensions`.
- `cx-coworker-wells-fargo.yaml` combines a dedicated branch (`rtcdp-aia-marketplace` @ `wells-fargo`) **with** a shared product marketplace (`cja-extensions`) — the closest analog to a scoped AEM manifest.

**3. `ao#5773` (Governance) IS MERGED — 2026-07-10.** This file said OPEN / CHANGES_REQUESTED as of 07-03. Title: *"feat(cx-coworker): enable experience-governance plugin OOTB on prod"*. **`experience-governance@governance-agent-marketplace` is installed in `aem-aia` today.** → ✅ **This also clears the 07-15 watch questioning Pedro's "Governance is ready, full migration from their side" claim to the Coworker team. He was right.**

**4. MARKETPLACE ≠ MANIFEST, DEMONSTRATED ON AEM'S OWN FILE.** `aem-aia` installs **8 plugins**: 7 from `aem-aia-extensions` (`discovery`, `cloud-manager-api`, `update-profile-api`, `aem-cloud-manager-ops`, `aem-release-management`, `experience-replication`, `aem-pipeline-troubleshooter`) + `experience-governance` from the governance marketplace. The **marketplace ships 10**. So ~3 of the marketplace's plugins are **not live in the manifest**. ⚠️ **The skill audit counts the MARKETPLACE, so it over-counts what actually runs.** Same figure as excat (60 skills, referenced by no manifest). **Count in the marketplace, but only manifest co-presence can collide.**
✅ **RESOLVED 2026-07-17 — One AEM MCP IS still wired into `aem-aia`**, but under a separate **`mcp_servers:`** section (`source: https://mcp.adobeaemcloud.com/adobe/mcp/aem`), **not** in `plugins:`. The "aem-aia = extensions + One AEM MCP baseline" line stands (Reasor PR `ao#5388`). **Note the shape: a manifest carries `known_marketplaces` + `plugins` + `mcp_servers` + `api_configs` as separate sections — do not look for an MCP in the plugin list.**

## 🟡 CORRECTION 2026-07-14, RESCOPED 2026-07-17 BY PEDRO — PER-USER ROUTING IS AN EXCEPTION MECHANISM, NOT THE DEFAULT AND NOT THE STEADY STATE.

**The 07-14 header said "manifest routing is per USER, not per org". That over-claims and Pedro corrected it.** The **default rule is org-level** (e.g. `aem-orgs-to-aem-aia`). A **per-user allowlist is a narrower rule inserted AHEAD of it**, for **named customers only** (Coca-Cola, AEM Sites Trial). It is a carve-out, and **it goes away after the all-customers migration.** → Say "routing is org-level, with per-user allowlists as named exceptions during the transition". The mechanics below are still accurate; only the headline was wrong.

**Source, read at the source:** **Felix Delval's PR `ao#6710`** ("Add AEM Sites Trial user allowlist routing to Experience Production Agent", opened 2026-07-14), which explicitly **mirrors the `coca-cola-orgs-allowlist` / `coca-cola-user-allowlist` and `comcast` patterns already in prod**.

**The mechanism, verbatim from the PR:** an **org-scoped segment** (`members: [<org id>]`) uses **`member_metadata.specific_segment`** to narrow down to a **`scope_kind: user`** segment keyed on **`user.email`**. A manifest-targeting rule is inserted **ahead of** the org's default rule (e.g. `aem-orgs-to-aem-aia`), and **targeting rules are evaluated first-match**, so the narrower allowlist wins for those users while every other user in the org is unaffected.

- **→ A single ORG can run two manifests at once, split across its users.** Allowlisted users of AEM Sites Trial get `experience-production-agent`; everyone else on the same org keeps `aem-aia`.
- **→ "One manifest at a time" is still true — but the unit is the USER SESSION, not the customer.** ⚠️ **Do not say "customer X cannot have both manifests." Say "a single user cannot have both in one session, and routing is per user, so someone has to decide which users get which."**
- **Why it matters, concretely (2026-07-14, AMEX):** `multi-cf-edits` (the only real CF-editing skill) is in the **`epa`** marketplace; `discovery` (the only content-search skill) is in **`aia-extensions`** (the central manifest). Verified in `adbe-skill-audit/data/skills.json`. So one user cannot edit *and* discover fragments today — but the org can be split. **That distinction is the difference between a wall and a routing decision.**
- **The AEM side already commits to this config themselves** — `scoman_adobe` (Sergiu Coman) pushed to `config/aep-aia/.../segments` on 07-13. **There is no CODEOWNER on the segments path**, only on `config/**/manifests/cx-coworker.yaml` (→ `@Adobe-Experience-Platform/aep-ai-ao-committers`). **So these PRs have no automatic approver, which is why Felix's sat unreviewed.** Who to ping: **Ankush Malhotra (`amalhotr_adobe`)** — he wrote the Coca-Cola pattern and pushed to these exact files twice on 07-14; **Dan Moldovan (`dmoldova_adobe`)** for the targeting-rule half (he did `cx-coworker-prada`).

## 🔑 HOW AN ORG/USER ACTUALLY GETS A MANIFEST — segments + targeting rules (read on `main` 2026-07-17)

**Two objects, and most people in the room only know about one.**

**1. The SEGMENT** (`config/aep-aia/environments/prod/segments/<name>.yaml`) says WHO. Two shapes:
- **org-scoped** — `scope_kind: organization`, `member_attribute: id`, `members: [<IMS org id>@AdobeOrg]` (e.g. `air-india-orgs.yaml`).
- **user-scoped** — `scope_kind: user` + `conditions` on `user.email` / `organization.id` (e.g. `adobe-users.yaml`, `demo-users.yaml`). A segment can also `add` a **role** via its own `actions:` block — that is how `demo-users` grants `aep_ao_demo_presenter`.

**2. The TARGETING RULE** (`config/aep-aia/environments/prod/config.yaml`, top-level `targeting_rules:`) maps segment → manifest:
```yaml
- rule_id: aem-orgs-to-aem-aia
  name: AEM orgs get AEM AIA manifest
  segment_id: aem-orgs
  resource: manifest
  manifest_id: aem-aia
  enabled: true
```
- **TWO rules per segment, not one.** One `resource: manifest`, one `resource: app` + `rule: allow_access`. Every live example does both (`aem-orgs`, `usbank-genai-va7`, …). A manifest rule alone does not grant app access.
- **FIRST-MATCH, so file order decides who wins.** Stated in their own comments: *"evaluate_allowlist is **first-match**, so any allow_access rule after it would **shadow** the trial's matched_segment_id"* (~line 499); *"**Must precede aem-orgs-to-aem-aia**: narrows AEM Sites Trial to allowlisted…"* (~line 223); *"Manifest rule must precede internal-nfr-orgs-to-cx-coworker-business-context"* (~line 12). → **A broad rule placed above a narrow one steals the narrow one's manifest.** A user-scoped rule on `@adobe.com` would take the manifest off every Adobe employee, AEM PMs included.
- **`adobe-users` is app-access ONLY** (`adobe-employee-app-access`), never a manifest rule. It covers `@adobe.com`, `@adobetest.com` **and `@adobeeventlab.com`**. **`demo-users`** grants `aep_ao_demo_presenter` to `@adobe.com` + `@techacct.adobe.com` only — **no eventlab** (⚠️ that asymmetry is likely why event-lab accounts cannot reach demo/manifest-switching; *inference, unconfirmed*). `namitak@adobe.com` + `juno@adobe.com` are the two `aep_ao_demo_strategy` addresses — **Namita owns that file, ask her, do not assert.**
- **The precedent for a user-scoped manifest audience:** `xlg-journey-users` → `cx-coworker-xlg-w-journey`. It exists in prod. Enrollment patterns are otherwise **hand-edited allowlists** (`coca-cola-user-allowlist`, `wells-fargo-visualization-users`, `amex-sandbox-allowlist`, `natwest-access-allowlist`) — so "a standing audience" means a yaml list **somebody owns and maintains**. Price that before claiming it.
- **⏱️ DEPLOY TIMING (`config/README.md`): config auto-deploys dev → stage → prod on merge to `main`, live within MINUTES**, and *"data-only config (segments, targeting rules, flags) is safe to merge anytime"*. → **A manifest + segment + rule PR merged today is testable today.** That kills the "no time before the deadline" objection.
- **⚠️ NO CODEOWNER** on the manifests/segments paths — only `config/**/manifests/cx-coworker.yaml` (→ `@Adobe-Experience-Platform/aep-ai-ao-committers`). **This is why Felix's `ao#6710` sat unreviewed. Always get a NAMED approver before opening a PR here** (worked 2026-07-17: naming the gap put Ken Russell in the room in 3 minutes).

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
> - **🔑 ZERO of the 22 SKILL.md files carry `domain`, and zero carry `when-to-use`** (verified 2026-07-09). ⚠️ **RE-READ FROM `adbe-skill-audit/data/audit.json` 2026-07-17 — the CATALOGUE-WIDE figures have moved and the round "0 of 102" is now WRONG outward. Live: 105 skills · `domain` = 2 (1.9%), both in `forms` · `when-to-use` = 36 (34.3%) · incomplete-on-both = 103 (98.1%) · 21 flagged pairs, 21 intra / 0 cross. Per marketplace: aia-extensions 25 skills (domain 0, wtu 3) · epa 18 (0, 0) · excat 60 (0, 31) · forms 2 (2, 2).
>
> ### 🔴🔑 SUPERSEDED 2026-07-22 — **DO NOT QUOTE THE 34.3%. THE CUSTOMER-FACING FIGURE IS ~11%.** (Reconciled into this file at the 2026-08-03 System Review; the two memory files had disagreed for 12 days and this is the one `/reply` hits first.)
>
> The 105 spans 4 catalogues, but **only 45 skills sit in Coworker-registered marketplaces** (aia-extensions 25 + epa 18 + forms 2). **On those 45: `when-to-use` = 5 (~11%), `domain` = 2 (both Forms).** The **34.3% is carried entirely by excat** (31 of its 60), and **excat is EDS migration tooling for developers, not customer-facing Coworker skills** — 53 of its 60 are AEM Edge Delivery Services developer tooling, 6 are the team's own repo workflow (`create-pr`, `update-changelog`, `dev-deploy-k8s`, `frontend-review`, `react-spectrum-s2`, `update-banner`), 1 is `excat-ui-tour`. **34.3% is the flattering number; ~11% is the true customer-facing figure and the stronger argument.** ⚠️ Also: the audit as run covers **3 of Felix's 8 AEM marketplaces, not 4 of 8** — extending it is a config edit in `scripts/fetch_skills.py` plus a pipeline run (done and posted 07-24). ⚠️ And **excat's absence from Felix's marketplace inventory is CORRECT, not a gap** — his list is scoped "AEM marketplaces in Coworker" and excat is referenced by no manifest. See [[project_aem_agents_intelligence]] 07-22 block. **The exactly-true sentence: "zero of the 25 skills in the shared aia-extensions marketplace carry `domain`; zero in EPA; 2 of 105 across all AEM, both Forms; 98% incomplete on both."** Every plugin is authored "AEM Team". **There is no agent attribution anywhere in the manifest data** — which is exactly why Ian Reasor, who co-owns this manifest, had to ask Pedro on 07-08 which agent two of the skills belong to. Skill→plugin is in the tree; plugin→agent is in nobody's head but the owning team's. This is the Playbook's `domain` ask, demonstrated by the manifest's own co-owner.
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
