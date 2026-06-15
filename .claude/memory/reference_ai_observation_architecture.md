---
name: reference_ai_observation_architecture
description: "The AO/Coworker agent observability architecture (OTel → LangFuse/MLFlow → DaaS NEXT Databricks → Rubin) = the V2 agent-data substrate that displaces Felix's AOv1 Co-Pilot pipeline."
metadata: 
  node_type: memory
  type: reference
  originSessionId: beda40f7-b409-4f4c-89f0-77971617cb07
---

Source: Confluence **AEMCSMC "AI Observation"** (pageId 3682236772) + 2 architecture diagrams, pasted by Pedro 2026-06-15 (couldn't fetch — 401 on private account). This is the canonical **observability / agent-trace architecture for AO / Coworker Harness** — i.e. how the V2 agent data that feeds Rubin is actually collected. Pairs with [[project_aem_agents_intelligence]] 2026-06-10 p42-architecture entry (Rubin replaced the AOv1 observation mechanism).

## Requirements / constraints
- OTel, annotated with AO attributes, must be sent **to AO** via its **AO Adobe Pipeline Topic** AND to its **LangFuse OTel collector** (ref: `ao-operator-sdk-python/.../ZEROTOTRACING.md`). DX-AI-Lib→AO traffic detail in **"AO Generative Credits Consumption V2"** (the credits/usage source — ties [[reference_powerbi_token_usage]]).
- OTel collectors/stores: workable availability, no dropped traffic (e.g. **99.9%**).
- OTel collectors + **primary stores must be in-region.** Only **aggregated** (non-sensitive) data may cross region boundaries.

## Ownership
- **A2A/MCP owners (the agent teams)** instrument: enable the **DX AO Tracing Lib** (annotations on methods → OTel to AO Collectors) + ship OTel to the **eNO OTel GW** via auto-instrumentation.
- **SRE team** owns: an **eNO OTel GW per cluster** (→ initially **Mystique LangFuse prod in VA7**, then **MLFlow per region** asap); **per-region MLFlow** backed by dedicated per-region **Azure Databricks** storage (+ Azure PgSQL) to keep data in-region.
- **DaaS Next team** owns the **DaaS Next Export pipeline** → exports into **DaaS Next / DPaaS Databricks**.
- **Dual-logging:** 100% of traces logged to BOTH locations (AO LangFuse + Pipeline Topic AND eNO OTel GW). Ideally only DX-AO-conversation-triggered traces route to DX AO.

## Flow (per cluster) — diagram 1
Agent namespace (`Dx AO Lib` + `Tracing Lib`; **LangFuse SDK preferred — supports OTel export**) → cluster **OTel Collector** → **P42 Monitoring Namespace** OTel Collector → fans to **Langfuse** (Clickhouse/Postgres/Zookeeper) + **otel2delta** + **MLflow** (OAuth Proxy/Postgres) → **Azure Storage Account, 1 per cluster** (`langfuse` / `oteltraces` / `mlflow`) → **DPaaS Databricks** (DaaS-owned, reads `oteltraces`; region-segregated). Top: **AO LangFuse** + **AO Pipeline Topic** → **AO Databricks**.

## DaaS NEXT regional→central aggregation — diagram 2
Per region: Agents → OTel Collector → traces/logs → **Storage Account (JSON, per cluster)** → **daily ETL transform (JSON→Delta)** → shared **Storage Account**: `raw` → **aggregate** → `regional aggregated` (**may cross region boundaries**) → **external location** → **Databricks Unity Catalog** → **central aggregator** merges external aggregated Delta tables → **central table** → managed → **central aggregated** Storage (West US / OR1?). DaaS NEXT-owned.

## PM read (why Pedro cares)
- This is the **V2 / Coworker agent-data substrate**: **OTel traces → LangFuse + MLFlow → DaaS NEXT (DPaaS Databricks / Unity Catalog) → Rubin.** Confirms Namita's "V2 reporting path = Langfuse (Ilya's V1↔V2 bridge)".
- **Felix's AOv1 Co-Pilot-chats pipeline is NOT in this picture** = the displacement made concrete (the AAI substrate is AOv1-data-bound, depreciating). The judge layer = DaaS NEXT's Agent Success Evaluation Framework (on Databricks) → [[H-005]] pressure.
- The **in-region / aggregate-only-crosses** rule = Ian Boston's + Michael Marth's data-residency constraint, operationalized.
- **Pedro's play:** don't defend the pipeline — **own the reporting *definition* on this substrate** (what skill/app-level success means in Rubin), with Soumya Sharma + Angela Han + Ilya. Same own-the-definition move as the AAI substrate + Yanira's success-definition wiki.
