# Opportunity Scoring — Prioritizing Jobs

## The Formula

```
Opportunity Score = Importance + max(Importance - Satisfaction, 0)
```

- **Importance:** how important this job/step is to the customer (0–10)
- **Satisfaction:** how well the current solution serves this job/step (0–10)
- **Theoretical maximum score:** 20 (importance 10, satisfaction 0)
- **Minimum score:** = Importance (when satisfaction ≥ importance)

## Interpretation

| Score | Interpretation |
|-------|---------------|
| 15–20 | Critical opportunity — underserved, high importance |
| 10–14 | Relevant opportunity — worth investigating and prioritizing |
| 5–9 | Moderate opportunity — monitor |
| < 5 | Overserved or low importance — do not prioritize |

## How to Collect the Data

### Option A — Quantitative survey (ideal)
Run a survey with customers:
- "How important is it for you to be able to [job/step]?" (0–10)
- "How well do current solutions serve this job?" (0–10)

### Option B — Qualitative estimate (acceptable with caveats)
Use evidence from interviews and feedback to estimate importance and satisfaction.
Mark as `[ESTIMATED — validate with survey]`.

## From Steps to Outcomes: the Unit of Measure

The opportunity score works best when applied to **desired outcomes** (extracted from the job map) rather than entire steps. A step like "Execute" may contain 3 outcomes with very different priorities.

**Flow:**
1. Build the job map with 8 steps (see `job-map.md`)
2. Extract desired outcomes per step (1–5 per step)
3. Measure importance × satisfaction for each outcome (not the whole step)
4. Calculate opportunity score per outcome
5. Outcomes with score > 10 are the priority opportunities

If the job map does not yet have desired outcomes, the agent must propose them before calculating scores.

## Opportunity Score Template

```
# Opportunity Score — [Initiative] — [Date]

**Main job:**
> When [circumstance], I want [progress], So I can [outcome].

**Method:** Quantitative survey / Qualitative estimate [choose one]
**N:** [number of respondents or interviews]

## Scores by Desired Outcome

| Step | # | Desired Outcome | Imp (0–10) | Sat (0–10) | Score | Priority |
|------|---|----------------|-----------|-----------|-------|---------|
| Define | 1.1 | [outcome statement] | [X] | [Y] | [score] | High/Med/Low |
| Define | 1.2 | [outcome statement] | | | | |
| Locate | 2.1 | [outcome statement] | | | | |
| [...] | | | | | | |

## Top Opportunities

1. [outcome with highest score] (Step: [step]) — Score: [X] — [brief evidence]
2. [second] — Score: [X]
3. [third] — Score: [X]

## Heat Map by Step

| Step | Outcomes | Avg score | Most critical outcome |
|------|----------|-----------|-----------------------|
| Define | [N] | [avg] | [outcome with highest score] |
| Locate | | | |
| [...] | | | |

## Gaps

[Outcomes without sufficient data for a reliable score — mark with `[DATA NEEDED]`]
```

Save to `{workspace}/initiatives/{initiative-name}/jtbd-opportunity-score.md`.
