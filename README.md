# Claude Self-Improving PM Knowledge System

A knowledge base for a Director of Product Management that compounds learning over time. Built to run inside Claude Code.

## What It Does

Every time you feed it a book, article, interview, or PM material, it extracts insights and stores them in structured knowledge files. Over time it builds a PM brain you can query, challenge, and build on.

The system routes knowledge into the right bucket automatically:

- New insight about PM practice → `knowledge/domain/`
- Recurring framework or decision pattern → `knowledge/patterns/`
- Hypothesis to test → `knowledge/hypotheses/active.md`
- Conventional wisdom that's wrong → `knowledge/false-beliefs/`
- Tool or method comparison → `knowledge/tools/`
- Experiment design or result → `knowledge/experiments/`

## Structure

```
knowledge/
  INDEX.md              # Start here. Routes every task to the right folder.
  domain/               # Core PM knowledge by practice area
  patterns/             # Recurring frameworks with supporting evidence
  hypotheses/
    active.md           # Hypotheses being tested
    resolved.md         # Confirmed or killed, with reasoning
  false-beliefs/        # PM conventional wisdom proven wrong
  tools/                # Decision matrix for PM methods and tools
  experiments/          # Experiment tracking and results
```

## How to Use It

Open the repo in Claude Code. Then talk to it:

- "Read this article and extract what's useful" — it updates knowledge files and commits
- "What do we know about stakeholder communication?" — it routes to domain/ and patterns/
- "Design an experiment to test whether X" — it checks hypotheses and experiments/
- "Prepare me for a skip-level" — it routes to Senior Director visibility knowledge

## Framing

Everything is filtered through one lens: a Director PM building visibility and credibility for a Senior Director promotion. Insights are not just catalogued — they're connected back to what makes a PM leader more effective and more visible.

## Sources Ingested

| Source | Type | Date |
|--------|------|------|
| Gallo, *Presentation Secrets of Steve Jobs* | Book | 2026-03-19 |
