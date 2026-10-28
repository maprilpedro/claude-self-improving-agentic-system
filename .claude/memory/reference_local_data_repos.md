---
name: reference_local_data_repos
description: Where Pedro's usage data lives on disk — the AOv1 interactions SQLite DB and the Rubin/Coworker report repo. Check here before saying "no access to the data".
metadata:
  type: reference
---

**Before answering "I can't see usage data", check these repos.** Pedro corrected Claude on 2026-09-25 ("tu as accès à toutes les données sur AOv1").

- **AOv1 (all AEM agent interactions)** → `~/GitHub/aem-agent-reports/database/copilot_interactions.db` (SQLite, ~10.5 GB). Fetched from the Copilot API (7 regions) by Pedro's pipeline; data from 2026-01-01, last fetch 2026-09-21 as of 09-25. Tables `interactions` (`ims_org_id`, `created_timestamp`, `created_ims_user_id`, `agent_identifier`…) and `organizations` (`org_name`, `category` = SKU / TryBeforeBuy / Partner / Explorer from the Skyline P42 list [[reference_skyline_p42_orglist]], `classification` = External / Internal). Open read-only (`sqlite3 -readonly`). Repo `CLAUDE.md` documents the pipeline.
- **Coworker (Rubin)** → `~/GitHub/adbe-coworker-rubin-reports/` — `rubin-reports/` raw exports, `reports/` outputs (weekly briefing HTML, ad hoc CSVs such as the 2026-09-24 champions org/skill files).
- **Old AOv1 exports** → `~/GitHub/aem-agent-data/` (CSV exports dated 2026-03-27, stale).
- **Program ↔ org lookup** → **fluffyjaws.adobe.com** (an Adobe chat Pedro queries himself). Asked "program 90156" on 2026-10-28, it returned the owner (SLALOM, LLC) and the IMS org ID in one answer, and offers the environments. Pedro: "plus facile". For "which org owns program N" or "is this org the customer or a sandbox", suggest he asks it before any manual comparison across Rubin and aemcs-workspace. The Rubin daily exports (sub-192) carry org names; the full IMS org ID shows in some days only (09-11 to 09-13 for Slalom).

⚠️ Querying any of these is code → [[feedback_claude_does_not_code]]: ask Pedro to lift the rule for the case, or hand back the query spec. Reading an existing CSV/HTML output is fine.
