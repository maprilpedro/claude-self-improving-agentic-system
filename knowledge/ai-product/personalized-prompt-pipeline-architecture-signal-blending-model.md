# Personalized Prompt Pipeline Architecture — Signal Blending Model

_Section: AI Product Risks — part of `ai-product/`; router = README.md._
- **Date identified**: 2026-04-08
- **Source**: Fu Chi (AEP) 1:1s, March 25 and April 7, 2026.
- **Insight**: A real-world personalized prompt recommendation system for an enterprise AI product runs on three layers of signal, dynamically blended. In AEP's implementation for AEM: (1) user history — each user's own past prompts and topics, most weight when history is sufficient; (2) org signals — aggregate behavior of peers in the same org, used as fallback when user history is thin; (3) global signals — product-wide behavior, used when neither user nor org history is available. The blend shifts automatically based on how much signal exists for each user.
- **Pipeline structure**: Prompts collected → cleaned (remove irrelevant/out-of-scope) → converted to embeddings → K-means clustering → topic reports per app. Output: ranked CSV/table of user IDs + top relevant prompts per user.
- **Variety mechanism**: The system penalizes overly similar prompts in the ranking to avoid a narrow recommendation set. Users are exposed to both highly relevant and adjacent topics.
- **Persona limitation**: As of April 2026, the system does not model personas or detailed user profiles — only behavioral clusters (content authoring, asset focus, Cloud Manager usage). Persona modeling is planned but not yet prioritized.
- **Critical distinction — prompts vs widgets**: Prompt recommendations come from this pipeline. Widget recommendations require separate work: query the Analytics DB directly, aggregate agent usage per user, then map to widget suggestions. These are two different data flows with two different outputs.
- **Application**: When designing a personalization layer for an AI product surface, separate the prompt recommendation problem from the widget/navigation recommendation problem early. They have different data sources, different models, and different engineering paths.
