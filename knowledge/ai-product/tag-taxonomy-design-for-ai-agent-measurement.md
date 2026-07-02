# Tag Taxonomy Design for AI Agent Measurement

_Section: AI Product Risks — part of `ai-product/`; router = README.md._
- **Date identified**: 2026-04-08
- **Source**: Tag review of suggested_tags.csv with Felix Delval, April 8, 2026.
- **Insight**: Tag taxonomies for AI agent measurement fail in predictable ways. The common failure modes, and their fixes:
  1. **Duplicate intent** — multiple tags with identical descriptions (e.g., Check-status, View-status, Progress-tracking all meaning "check translation status"). Produces noise, not signal. Fix: consolidate to one canonical tag per intent.
  2. **Object name vs intent name** — tags named after data objects (Languages, Locale) rather than what the user was trying to do. Misleads analysts and makes filtering unreliable. Fix: name tags by user intent, not by the object the user mentioned.
  3. **Overpromising scope** — tag names that imply a broader meaning than the description provides (e.g., asset-lifecycle implies creation + versioning + archiving, but description only covers expiration). Fix: align name to actual scope, or broaden the scope to match the name.
  4. **Naming convention mismatch** — mixing Title-Case and lowercase-kebab in the same system makes grouping, filtering, and display inconsistent. Fix: normalize to one convention. lowercase-kebab is standard for machine-readable tags.
  5. **Tag names as sentences** — long descriptive names (e.g., search-result-used-in-next-interaction) are unsearchable and unwieldy. Fix: compress to 2-3 word concepts (chained-search, search-result-reused).
  6. **Shadow tags** — a broad catch-all tag that overlaps with multiple specific tags. The catch-all gets applied first and the specific tags get underused. Fix: either remove the catch-all or make it the parent in a hierarchy.
- **Application**: Before publishing a tag taxonomy for cross-agent measurement, run it through these six failure modes. If any apply, fix before rollout — retroactive taxonomy cleanup is expensive.
