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

## Weekly table, exact dates (v2, 2026-10-13)

Weeks Monday to Sunday. AOv1 = external customers (Skyline list), from the weekly `all_agents.html` reports; when a later report revised a week, the revised value is used (W31: 283/450/1,921 first, 305/482/2,017 revised; W37: 159/223/1,002 first, 160/224/1,003 revised). Coworker dashboard values are read off the weekly chart (approximate), scope (internal included or not) not stated. sub-192 = Sites section only, internal included, exact.

| Week | Dates | AOv1 ext orgs | AOv1 ext users | AOv1 ext interactions | Coworker dashboard users / orgs / interactions (≈) | sub-192 Sites users / interactions |
|---|---|---|---|---|---|---|
| W30 | Jul 20–26 | 274 | 409 | 1,837 | ≈3 / 3 / 20 | – |
| W31 | Jul 27–Aug 2 | 305 | 482 | 2,017 | ≈5 / 4 / 45 | – |
| W32 | Aug 3–9 | 295 | 477 | 1,775 | ≈2 / 2 / 10 | – |
| W33 | Aug 10–16 | 287 | 477 | 1,456 | ≈8 / 5 / 35 | 15 / 99 |
| W34 | Aug 17–23 | 272 | 436 | 1,211 | ≈10 / 4 / 45 | 53 / 853 |
| W35 | Aug 24–30 | 288 | 455 | 1,510 | ≈20 / 9 / 135 | 64 / 1,503 |
| W36 | Aug 31–Sep 6 | 287 | 447 | 1,369 | ≈39 / 19 / 270 | 111 / 1,690 |
| W37 | Sep 7–13 | 160 | 224 | 1,003 | ≈72 / 46 / 450 | 104 / 1,144 |
| W38 | Sep 14–20 | 176 | 269 | 941 | ≈109 / 72 / 810 | 170 / 2,103 |
| W39 | Sep 21–27 | no data | no data | no data | ≈160 / 115 / 710 | 168 / 789 |
| W40 | Sep 28–Oct 4 | no data | no data | no data | ≈228 / 151 / 950 | 208 / 851 |
| W41 | Oct 5–11 | no data | no data | no data | ≈249 / 156 / 1,200 | 242 / 1,468 |

## AOv1 monthly external users (Pedro's 09-15 screenshot), added 2026-10-13

Source: `aem-agent-reports/reports/portfolio/current/briefing.html` (rolling 4 weeks Aug 24 to Sep 20). Screenshot copied to `20261013-rubin-coworker-reporter/aov1-customers-20260915.png`.

Monthly distinct external users per agent (Sep = month to date):

| Agent | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep (partial) |
|---|---|---|---|---|---|---|---|---|
| Discovery | 569 | 1,080 | 1,913 | 931 | 964 | 921 | 903 | 394 |
| Experience Production | 19 | 479 | 1,812 | 666 | 705 | 670 | 625 | 275 |
| Experience Development | 292 | 330 | 445 | 263 | 306 | 315 | 254 | 123 |
| Governance | 12 | 162 | 238 | 161 | 211 | 199 | 185 | 90 |
| Content Optimization | 20 | 80 | 159 | 72 | 71 | 77 | 62 | 32 |

External interactions per month, all agents: Apr 10,504 · May 6,083 · Jun 7,856 · Jul 8,008 · Aug 6,290.

Rolling 4 weeks Aug 24 to Sep 20, all agents, distinct: **562 orgs, 1,258 users** (MoM −11.8% orgs, −24.9% users). Implied prior 4 weeks (computed from MoM, not read): ~637 orgs, ~1,675 users.

Reading: per-agent lines overlap (45% cross-agent), so they do not add up. Monthly is about 3x weekly (weekly external users ran ~450 in W30 to W36). Compare Coworker to AOv1 only at the same window.
