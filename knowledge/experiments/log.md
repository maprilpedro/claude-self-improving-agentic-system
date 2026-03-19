# Experiment Log

> Track all experiments: A/B tests, discovery experiments, process experiments.

## Experiment Types
- **Product**: A/B tests, feature experiments
- **Discovery**: User research experiments
- **Process**: Internal PM process experiments
- **Knowledge**: Testing this system's effectiveness

## Status Key
- **Designed**: Experiment planned, not started
- **Running**: Currently collecting data
- **Analyzing**: Data collected, being interpreted
- **Complete**: Results documented and applied

## EXP-001: First Book Ingestion into PM Knowledge System

- **Type**: Knowledge
- **Status**: Complete
- **Date started**: 2026-03-19
- **Date completed**: 2026-03-19

### Hypothesis
> Book ingestion can systematically extract actionable PM knowledge and populate the knowledge system with source-attributed, structured insights.

### Design
- **What we're testing**: Whether a full book (Gallo, *Presentation Secrets of Steve Jobs*, ~9,400 lines) can be processed into the knowledge taxonomy (domain, patterns, false beliefs, tools, hypotheses)
- **Control**: Empty knowledge system
- **Variant**: Knowledge system populated with book insights
- **Success metric**: All knowledge files populated with source-attributed entries that follow the established templates
- **Guardrail metrics**: No copyright-infringing full-text reproduction. Only extracted insights and frameworks.
- **Duration**: Single session

### Results
- **Primary metric**: All 7 knowledge files updated with structured entries
- **Files updated**: domain/README.md (11 entries across 6 categories), patterns/README.md (9 entries: 2 decision patterns, 6 frameworks, 2 stakeholder templates, 3 anti-patterns), false-beliefs/catalog.md (5 cataloged beliefs), tools/decision-matrix.md (6 new communication tools + updated tables), hypotheses/active.md (3 hypotheses), experiments/log.md (this entry)
- **Guardrail metrics**: All entries are synthesized insights, not reproduced text. Source attributed throughout.
- **Unexpected findings**: The book is overwhelmingly about communication and stakeholder management. Almost every insight maps directly to the user's Senior Director visibility gap. Hypothesis H-003 emerged organically.

### Decision
- **Action taken**: Knowledge system populated. Git commit to follow.
- **Knowledge updated**: All knowledge files
- **Follow-up**: Apply H-003 (visibility gap hypothesis) in real presentations. Consider ingesting additional books on executive presence, stakeholder influence, or strategic communication.
