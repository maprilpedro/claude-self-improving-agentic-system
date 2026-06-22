---
name: reference_skyline_p42_orglist
description: The Skyline P42 README = the org-classification source of truth (External / Internal / TryBuy-Explorer) Raul maintains by hand. The list every AAI report filters on.
metadata:
  type: reference
---

The **org-classification source of truth** for AAI reporting lives in a git README, NOT a UI:

```
https://git.corp.adobe.com/experience-platform/skyline-rollout-cc/blob/main/p42/README.md
```

`experience-platform/skyline-rollout-cc`, folder `p42/`. Internal `git.corp.adobe.com` (VPN-only — not github.com, Claude can't fetch it).

**What it is:** the manually-maintained list that categorizes every org as External / Internal / TryBuy(Explorer→TBYB) / Partner. **Raul Hudea maintains it by hand.** Only orgs categorized External in this README count as External in the External Agents Briefing (`https://main--aem-agent-reports--aem-epa.aem.page/reports/external-agents/current/briefing`), so the briefing stays sparse until categorization catches up.

**Why it matters / the recurring trap:** every "numbers are off / fluctuating morning vs evening" episode traces back to a Raul-list manual refresh. The reports filter on this README, so portfolio org/user counts move when Raul re-categorizes (~18-20 flagged-external orgs that look internal lab/sandbox; Adobe Corp/Consulting sometimes mis-flagged). Pedro's stance: stick with the Raul list as gospel until classification is aligned, avoid display↔data divergence. The "refresh + automation" + API/MCP-source-vs-README lane is Pedro's ([[reference_aep_trybuy_artifacts]] is the upstream AEP side; AEM Grafana mapping = Jabin creator + Raul editor, manual SQL).

⚠️ At VP read-speed, pointing at "Raul maintains this list" reads as "I don't know" — lead with an ownership sentence ([[feedback_first_reply_ownership_sentence]]), not the git trail.
