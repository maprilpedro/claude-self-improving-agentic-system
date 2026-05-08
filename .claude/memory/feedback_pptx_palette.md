---
name: PPTX color palette — Adobe template only
description: Allowed colors for any pptx Pedro reviews. White, light grey, dark grey, red, black ONLY. No green, blue, pink, or other tints.
type: feedback
originSessionId: c3970bb1-0fc5-47cd-80ee-cd157b1b93c6
---
**Rule.** Every pptx generated for Pedro uses only these 5 colors:

| Role | Hex | RGB |
|---|---|---|
| White | `#FFFFFF` | (255, 255, 255) |
| Light grey (cell tint, callout backgrounds) | `#E8E8E8` | (232, 232, 232) |
| Dark grey (secondary text, swimlane labels) | `#6E6E6E` | (110, 110, 110) |
| Adobe red (accents, parallel/important headers) | `#EB1000` | (235, 16, 0) |
| Black/near-black (primary text, headers) | `#1A1A1A` | (26, 26, 26) |

**Why:** Pedro feedback 2026-05-05 — *"some tables have green background, it's a no — white, light grey, dark grey, red and black are only colors to use as per template."* Earlier draft used `#FFF0EE` (very pale red) and `#EEF4FF` (very pale blue) for joint/parallel cell tints; both flagged as "ugly green" / off-template. Even faint colored tints break the AEM corporate template look.

**How to apply:**
- Cell-row tinting → `#E8E8E8` (light grey).
- Header strips → `#1A1A1A` (dark) or `#EB1000` (red) for emphasis.
- Avoid all other tints. If you find yourself reaching for a "soft pastel" or "subtle hint of color," go to white instead.
- Build script `/tmp/build_aov2_deck.py` constants `JOINT_BG` and `PARALLEL_BG` both = `#E8E8E8` — keep that pattern.
