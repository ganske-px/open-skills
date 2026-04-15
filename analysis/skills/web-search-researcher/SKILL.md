---
name: web-search-researcher
description: Deep web research for questions requiring current, competitive, or external information. Use when you need market benchmarks, competitive analysis, industry trends, regulatory data, or information not available internally. Do NOT use for internal data (analytics/SQL/databases) — use data-research. Do NOT use to synthesize already-collected research — use synthesize-research.
---

# web-search-researcher

Spawns a specialized subagent to answer questions that require current, competitive, or external information.

## When to Use

| Situation | Example |
|---|---|
| Market benchmarks | "What is the typical SLA for background checks in the insurance sector?" |
| Competitive analysis | "How do competing platforms qualify service providers?" |
| Trend validation | "Is open finance being applied in logistics risk scoring?" |
| Best practices | "Decision engine frameworks for operational risk management" |
| Regulatory data | "GDPR requirements for storing biometric data" |
| Analogies from other sectors | "How did the banking sector reduce credit analysis time with automation?" |
| External technical validation | "Alternatives to hard-coded enums for provider extension in Laravel" |

**Triggers:** "research about X", "market benchmark for X", "competitive analysis of X", "how does the market do X", "external data about X", "what exists about X"

## How to Invoke

Spawn the subagent passing the structured question:

```
Agent(
  subagent_type="web-search-researcher",
  description="Research: [topic in 3-5 words]",
  prompt="""
<context>
[Workspace context — product, initiative, or problem under analysis]
</context>

<query>
[Specific and well-formulated research question]
</query>

<output_format>
Expected structure:
- Summary (3-5 main bullets)
- Detailed Findings (sources with links, relevant quotes)
- Specific benchmarks when available
- Gaps or Limitations
</output_format>
"""
)
```

## Workflow Integrations

| Skill / Agent that invokes | When to use |
|---|---|
| `discovery-kickoff` | "What does the market or industry already know about this?" |
| `ideation` | Phase 1 — analogies from other sectors (disruptive mode) |
| `product-decision` | External benchmarks to calibrate importance/satisfaction |
| `competitive-analysis` | Main backbone |
| `initiative-research` | Main backbone |

## Anti-Patterns

- Do not use for internal data (analytics, SQL, databases) — those go to `data-research`
- Do not pass vague queries ("research about risk") — the more specific, the better the result
- Results are web snapshots — always note the collection date in the final artifact
- Only cite sources that the subagent returned with a real link — never rewrite as a fact without a source

## Persistence

The caller saves the results to:

```
{workspace}/research/market/{slug}-{date}.md
```

Example: `research/market/sla-background-check-logistics-2026-03-11.md`

The file path created is returned at the end of execution.

## Expected Output

Structure of the generated file:

```markdown
# [TOPIC] — Market Research / External Intelligence
Collection date | Related initiative | Central question

## Summary
[3-5 main bullets]

## Detailed Findings
[sources with links, publication dates, relevant quotes]

## Benchmarks
[table with numerical metrics when available]

## Gaps and Limitations

## How to Use This Data

> Snapshot notice with collection date
```
