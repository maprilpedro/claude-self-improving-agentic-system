# AEM Experience Hub — Analytics Workspace
**Date captured:** 2026-04-02  
**Workspace:** https://experience.adobe.com/#/@amc/platform/analytics/#/workspace/edit/67222440447f9c0ccc136c8d  
**Data source:** PDH WebSDK + Contractual + Health Metrics  
**Default date range:** Dec 28, 2025 – Mar 28, 2026 (13 full weeks)

---

## Panels in the workspace (top to bottom)

1. **Freeform table (6)** — Compares two segments side by side:
   - `aem-home-ui` (EH): **288 people** over full period
   - `experience-platform-self-service-ui-landing`: 0 people (no data)
   - Rows: Page Detail URLs — all experience.adobe.com variants

2. **Dormant Users** — Active in past 3 months but not past 2 weeks

3. **New frequency**

4. **Conversions by feature (Comp to prev window)**

5. **Adoption Funnel**

6. **AEM User Base - Experience Hub Adoption Funnel** ← key panel, collapsed

7. **User template**

8. **Flow (2)** — aem-home-ui starting point, App Id pathing, external users only (User is internal flag = False), Feb 22–Mar 14, 2026

9. **Area stacked (3)** — Weekly trend Dec 28–Mar 28:
   - EH (aem-home-ui): peaks 15–22 people/week
   - experience-platform-self-service-ui-landing: near zero

10. **Flow (11)** — cloudManagerUI starting point, 0 path views (empty/broken)

11. **Freeform table (4)** — collapsed

12. **Flow: aemshell > ddam** — collapsed

13. **Experience Manager Assets flow** — collapsed

14. **Submitted prompts** — note says "not sent from AEM Home, to see if we can filter"

15. **Sites Optimizer**

16. **EDS Announcements**

17. **Alpha Tenants - Historic AEM Usage**

18. **AEM - All Tenants** ← total AEM user base, collapsed

19. **AEM - Internal vs external people**

20. **AEM application flows** — Segments: "Experience Hub - External Alpha Orgs" + "EH - CloudManager2AEM", last 13 weeks
    - Contains: Freeform table (5), Sites instance referrals trend, Flow: cloudManagerUI > aemshell, AEM Author

21. **AEM Home flow** — collapsed

22. **Cloud Manager Starting Flows** — collapsed

23. **Experience Manager Home (OLD Cards) Starting Flows** — experienceManagerUI = 0 path views (old version, dead)

24. **Experience Manager Assets referrals trend** — collapsed

25. **Bar chart + Freeform table** — Feb 22–Mar 14, 2026:
    - Total: **698 people** over 21 days
    - Daily range: 6–63 people/day
    - Weekday pattern clear (weekends drop to 6–10)

26. **Prompt categories by persona** — loading/no data visible

27. **Top clicked prompts** — collapsed

---

## Key flow data (Screenshot 3)
**aem-home-ui → next app (People flow, 3,228 path views):**
| Destination | Count | % |
|---|---|---|
| ai-assistant | 1,051 | 32% |
| aemshell | 542 | 17% |
| cloudManagerUi | 460 | 14% |
| heimdall-security-mte | 232 | 7% |
| landing | 162 | 5% |
| +35 more | 781 | 24% |

---

## What's available for EH users vs total AEM users

- **EH unique people:** 288 (full period) or 698 (Feb 22–Mar 14 specific panel)
- **Total AEM users:** "AEM - All Tenants" segment EXISTS in the workspace (panel 18) but is collapsed — number not visible in screenshots
- **"AEM User Base - Experience Hub Adoption Funnel"** panel exists (panel 6) — collapsed, likely already attempts this ratio
- Segments available: "Experience Hub - External Alpha Orgs", "EH - CloudManager2AEM"

---

## Gaps noted
- experienceManagerUI (old EH) = 0 path views — confirms migration to aem-home-ui complete
- experience-platform-self-service-ui-landing = 0 people — that surface has no traffic
- cloudManagerUI starting flow = 0 path views (may be broken or wrong date range)
