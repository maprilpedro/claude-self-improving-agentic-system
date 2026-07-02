# Parallel Artifact Streams Diverge — Always Check the Latest Version

_Section: Anti-Patterns — part of `patterns/`; router = README.md._
- **Date identified**: 2026-03-31
- **Observations**: (1) Pedro's .md product reports and Felix's HTML reports are two separate streams for the same data. Felix's HTML was more advanced and already had Quality/Gap split + JIRA column structure — features incorrectly assumed to be missing because only the .md reports were checked. (2) In multi-track reporting work, the track you're not actively working on can advance without your knowledge.
- **Pattern**: When two parallel artifact streams exist (e.g. fast PM reports + engineering-built dashboards), they drift apart over time. Assuming they're in sync without verification causes duplicated work, missed capabilities, and wrong gap analysis.
- **Fix**: Before declaring something missing, check the latest version of every artifact stream. Read the HTML, not just the markdown. The stream you didn't write moves independently.
- **Application**: Whenever doing a gap analysis against someone else's artifact, read their artifact first. Not the version you remember from last week — the current file.
