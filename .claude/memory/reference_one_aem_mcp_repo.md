---
name: one-aem-mcp-repo-tanju
description: "The One AEM MCP server repo (adobe-rnd/aem-sites-content-service) — Tanju's catalog/skills/discovery/Eval-Semantics source. Unblocks Pedro's overlap-audit cross-check."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 68d0ac63-90d4-4fb0-bd76-dbe7aac3e148
---

**Repo:** https://github.com/adobe-rnd/aem-sites-content-service (org `adobe-rnd`, github.com)

**What it is:** the **One AEM MCP server** codebase — Tanju Erinmez's project. The customer/partner MCP interface all AEM agents are being pushed to consolidate behind (Pedro's convening lane). Shared by Tanju 2026-07-01 after the 1-1 walkthrough.

**What's inside (per the 2026-07-01 Tanju 1-1 mechanism walkthrough):**
- **Domains** — subject categories (sites / search / forms / assets / insights), arbitrary + bottom-up, built off the API registry (GA endpoints; more may sit in another branch), NOT normalized.
- **Skills + recipes** — skills = action-based (copy-a-page, get-page-properties), generated via Claude from experience-leak use cases; recipes = code-snippet blueprints for the LLM. Origin = wrap APIs without re-implementing tools (ingest API registry → summarize the OpenAPI YAML → base knowledge).
- **Skill header format** — title / what-it-does / capability / area / audience tags / aliases / single-step chaining hints = what's returned to the LLM. Ingested into a semantically-searchable catalog. Structurally aligns with Pedro's overlap-audit `domain` / `when-to-use` fields.
- **2-part discovery** — best-10 semantic hits + LLM self-dedup; domain/category fallback if too narrow. Selection = "a walking decision tree, max 3 hops; more = a regression signal to improve the catalog."
- **"Eval Semantics"** — the weekly catalog-balance check (3 metrics). Architecture/principles ingested as docs (self-describing).
- **Selection monitoring + CI/CD auto-improve loop** — mismatch = multiple lookups; a scheduled GitHub job ingests logs → suggests → auto-PRs skill improvements → auto-deploy.

**Why it matters for Pedro:**
- **Unblocks the overlap-audit cross-check** — pull Tanju's semantic-ranking / conflict-probability output to cross-validate the static lexical pairs → feed Ian's confusion-pairs (H-007).
- **The piggyback play** — get his overlap-audit header fields (`domain` / `when-to-use` / `when-not` / keywords) improved by Tanju's CI/CD loop = the audit rides the platform's own auto-improve pipeline ([[reference_aov2_marketplace_manifest]], leadership/ "Govern a Consistency Layer Over Primitives You Don't Own").

⚠️ Internal Adobe repo — never push its content to personal GitHub or external services ([[feedback_no_internal_to_personal_repos]]). Fetch at runtime via the `pedrofer_adobe` gh account (github.com, no VPN), don't store internal skill content in the local audit repo.

Related: [[reference_skyline_p42_orglist]] (org-classification list every report filters on), the local `GitHub/adbe-skill-audit` POC repo (reproduces the overlap audit).
