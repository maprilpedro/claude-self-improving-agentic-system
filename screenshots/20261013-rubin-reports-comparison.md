# Rubin, two views of the same week (2026-10-06 → 10-13), compared 2026-10-13

Sources: Rubin "CX Enterprise Coworker" dashboard, 12 screenshots in `screenshots/20261013-rubin-coworker-reporter/` (filter: 68 skill families, 7d 06.10–13.10, refresh every 12h) vs Pedro's Report Builder subscription `sub-192` "AEM Coworker - Skills Usage" (HTML, window last 7 days, scope Commercial, regions All, skills `aem*`, data as of 10-13 06:06 UTC; file in ~/Downloads).

| Metric | Pedro's report (aem*, "Commercial") | Rubin dashboard (68 families) |
|---|---|---|
| Weekly active users | 576 (−9% WoW) | 280 (+15.7%) |
| Active orgs | 293 (−12%) | 171 in the customer table |
| Interactions | 3,445 (−6%) | 1.5K (+44.6%) |
| Chat sessions | 983 | 377 (+5.9%) |
| Avg response | 114.4 s | 93.6 s (VA7 only) |
| Frustration / abandonment | 3.5% / 11.1% of chats | 1.92% / 30.77% of unresolved chats (VA7 only); AI insight 2.5% / 8.5% |

Exact org matches: LGCNS Korea 71 interactions / 1 user, VC BRANDS 65, MACYS 49, IBM DX Platforms 37, HOBBY LOBBY 27, EVONIK 22, Jazeera 3 users.
Near: Intuit 63 vs 55, Lumen 34 vs 40, Jazeera 103-136 vs 126, Trane 29 vs 42, Abbvie 19 vs 30, Suncorp 23 vs 18.
Absent from the dashboard customer list: Newell Brands (146 / 15 users in Pedro's report, the top external org there), all Adobe demo / internal / trial orgs.

## Against the last AOv1 report (added 2026-10-13)

Last AOv1 report: `~/GitHub/aem-agent-reports/reports/week_20260914/all_agents.html`, 2026-W38 (Sep 14–20), generated 09-21. The AOv1 DB was last fetched 09-21, so there is no AOv1 data for 10-06 → 10-13.

| Week | Source | Users | Orgs | Interactions |
|---|---|---|---|---|
| W38 Sep 14–20 | AOv1, external (Skyline list) | 269 | 176 | 941 |
| W38 | AOv1, all | 301 | 194 | 1,060 |
| W38 | Rubin dashboard, 68 families (read off the chart) | ~110 | ~70 | ~800 |
| W38 | sub-192, Sites section only, incl. internal | 170 | n/a | 2,103 (enablement session 09-17 that week) |
| W38 | Rubin digest "GEM & AO1" (memory, 09-22) | 57 | n/a | 129 |
| Oct 06–13 | Rubin dashboard, customer view | 280 | 171 | 1.5K |

ABAC = 354 of the 1,060 AOv1 interactions in W38 (one third), and ABAC has no Coworker equivalent.
