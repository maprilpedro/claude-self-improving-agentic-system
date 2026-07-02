# Differentiation as Diagnostic Requirement

_Section: Stakeholder Communication Patterns — part of `patterns/`; router = README.md._
- **Date identified**: 2026-04-22
- **Source**: Varun Kalra (Discovery Agent validator) on why Discovery Agent's uniform "no results found" response breaks product-gap triage. Compared with Governance Agent's explicit "I cannot help with this" response.
- **Pattern**: You cannot fix what you cannot distinguish. When two fundamentally different failure modes produce the same observable output, triage is impossible and improvement work becomes random. Before a product can improve, its failure surface has to be at least as granular as the distinct causes you'd want to address. In Discovery Agent: "unsupported query" and "content doesn't exist" and "search quality failed" all return the same user-facing "no results found." A PM looking at the data can't tell which of the three is happening, so can't route the fix to the right team (scope owner vs content owner vs search-quality owner).
- **The diagnostic bar**: Your observable signals need to distinguish between things you would take different action on. If the action is identical regardless of cause, fine to collapse. If actions differ, the signal must differ. This is the minimum taxonomy requirement.
- **How to apply**: In any reporting or measurement work, when you see a single category that swallows multiple root causes, mark it. Ask "would I want to do different things for different instances of this?" If yes, split it. The single bucket is hiding a diagnostic problem even if your numbers look clean.
- **How to spot this in practice**: Watch for categories named by observed symptom ("error," "no result," "abandoned") rather than root cause. Symptom-named buckets are the canary. Root-cause-named buckets force the taxonomy to stay sharp.
- **Anti-pattern**: Accepting an uninformative category because the data "looks clean." Clean data with hidden causal mixing is worse than messy data with clear distinctions — the clean version gives false confidence.
- **Related**: Failure Taxonomy Quality vs Gap Split (patterns/); "No Results Found" Is a Product Gap in Agentic UX (ai-product/).
