# Dual-Track Source Tracking — Slack Parent vs JIRA Parent

_Section: Artifact Architecture — part of `patterns/`; router = README.md._
- **Source**: Pedro session, April 28, 2026 (H2 2026 HC Rollup analysis)
- **Date**: 2026-04-28
- **Observation**: When mapping H2 2026 roadmap items to their parent initiatives, two sources gave conflicting answers. The Slack canvas (curated source doc, manually grouped under section headers like "DX Initiative: Adobe LLMO (LLMO-4023)") said one thing. The JIRA "implements" relationships (formal record, fetched via MCP) said another. For most items the two agreed. For LLMO-4141 they diverged: Slack said LLMO-4023, JIRA said DX-1134 (Closed). Both are useful artifacts; neither is enough on its own.
- **Pattern**: When a planning surface is curated by humans (slides, Slack canvases, Confluence pages) AND backed by a structured system (JIRA, Linear, Asana), the two diverge over time because curation reflects current intent while the structured system reflects formal record. Track both side-by-side in coordination artifacts. Mismatches are signals — usually that the formal record needs updating to match new intent (or that intent is drifting from what's been formalized).
- **Design rule**: For any "what is this item part of?" column in a planning rollup, show both the human-curated source (Slack Parent / Slide Parent / Doc Parent) and the structured source (JIRA Parent / Linear Parent). When they match, the columns reinforce. When they disagree, you have a finding worth surfacing.
- **When it applies**: Cross-team planning where curated summaries exist alongside ticket trackers. PM rollups for executive review. Initiative-to-roadmap mappings.
- **When it fails**: If the human-curated source is the only authority (no formal system) or if the structured system is the only one used (no narrative summary), there's nothing to dual-track. One column is enough.
