---
name: probability-analysis
description: Calculates probabilities from collected data. Use when you need P(A), P(A|B), confidence intervals, Bayesian distributions, Poisson rates, or statistical comparisons between groups. ONLY calculates — does not interpret, does not persist, does not write narrative. Do NOT use for product analytics (PostHog/SQL) — use data-research. Do NOT use for product metrics tracking — use metrics-tracking.
---

# Probability Analysis

Probability calculator. Receives data → normalizes into a data contract → executes Python script → returns structured JSON.

## Single Responsibility

**This skill only calculates. It does not interpret or persist.**

Output: JSON with probabilities, confidence intervals, and statistical metadata.
The caller is responsible for interpretation and persistence.

## When to Use

- "what is the probability of X given Y?"
- "what is the likelihood of Z happening?"
- "compare the rate of A vs B"
- "what is the expected rate of [event]?"
- "is there a significant difference between [group 1] and [group 2]?"

**Triggers:** "calculate probability", "confidence interval for X", "compare rates between groups"

## Calculation Types

| `calculation_type` | When to use | Method |
|---|---|---|
| `simple` | P(A) direct | Wilson CI |
| `conditional` | P(A\|B) — subgroup already filtered at collection time | Wilson CI |
| `bayesian` | Expected rate with uncertainty, history as prior | Beta posterior + HDI |
| `poisson` | Average events per unit of time | Garwood CI |
| `comparison` | Group A vs Group B — is there a difference? | Wilson + Chi-square + Relative Risk |

For `conditional`: filter the subgroup **in the data collection query** (not in Python). The group that arrives in the data contract is already the conditioned subgroup.

## Pipeline

### Step 1 — Identify the calculation type

Read the question and map it to the correct `calculation_type` from the table above.

### Step 2 — Collect data (if necessary)

If data has not been collected yet, use the `data-research` skill to collect it.

The required data is always: **population (n)** and **events of interest (successes)** per group.

### Step 3 — Build the Data Contract

```json
{
  "question": "question description in natural language",
  "calculation_type": "simple | conditional | bayesian | poisson | comparison",
  "confidence_level": 0.95,
  "source": "database | api | analytics | mixed | manual",
  "collected_at": "YYYY-MM-DD",
  "data": {
    "groups": [
      {
        "label": "descriptive_group_name",
        "n": 1000,
        "successes": 230
      }
    ],
    "prior": {
      "alpha": 1,
      "beta": 1
    }
  }
}
```

Contract rules:
- `groups` is always a list, even for `simple` (1 element)
- `prior` only required for `bayesian` — default `Beta(1,1)` = uniform prior (no prior information)
- For `bayesian` with history: `alpha = historical successes`, `beta = historical failures`
- For `poisson`: `n` = time units (days, weeks), `successes` = observed events
- For `comparison`: first group is "exposed", second is "control"
- `label` must be descriptive snake_case (e.g., `with_incident`, `without_incident`)
- Data period must be consistent across groups — otherwise add a warning

### Step 4 — Execute the Python script

Write a script in `/tmp/prob_<slug>.py` with the data contract embedded:

```python
import sys, json
sys.path.insert(0, 'analysis/scripts')
from probability_calculator import calculate

DATA = <data_contract_here>

result = calculate(DATA)
print(json.dumps(result, indent=2, ensure_ascii=False))
```

Execute via Bash:
```bash
python3 /tmp/prob_<slug>.py
```

The script is at `analysis/scripts/probability_calculator.py`.

### Step 5 — Return the result

Return the complete JSON. Do not add interpretation.

If `metadata.warnings` is not empty, show the warnings before the JSON.

## Output Schema

```json
{
  "question": "...",
  "calculation_type": "...",
  "results": [
    {
      "label": "group_name",
      "probability": 0.23,
      "ci_lower": 0.20,
      "ci_upper": 0.26,
      "ci_level": 0.95,
      "n": 1000,
      "successes": 230,
      "method": "wilson | bayesian-hdi | poisson-garwood"
    }
  ],
  "comparison": {
    "group_a": "name_a",
    "group_b": "name_b",
    "rate_a": 0.23,
    "rate_b": 0.036,
    "relative_risk": 6.38,
    "risk_difference": 0.194,
    "test": "chi-square",
    "chi2": 312.5,
    "p_value": 0.0001,
    "significant": true
  },
  "metadata": {
    "source": "database",
    "collected_at": "2026-03-06",
    "calculated_at": "2026-03-06",
    "confidence_level": 0.95,
    "warnings": []
  }
}
```

`comparison` is `null` for types other than `comparison`.

## Anti-Patterns

- Never invent `n` or `successes` — require them from collected data
- Never infer the period implicitly — always explicit in the contract
- Never omit `warnings` when present
- Never interpret the result — return JSON and stop
- Never mix different periods across groups without a warning

## Complete Example

**Question:** "Do users with a prior incident have a higher rejection rate?"

**Data contract:**
```json
{
  "question": "Do users with a prior incident have a higher rejection rate?",
  "calculation_type": "comparison",
  "confidence_level": 0.95,
  "source": "database",
  "collected_at": "2026-03-06",
  "data": {
    "groups": [
      { "label": "with_incident", "n": 1000, "successes": 230 },
      { "label": "without_incident", "n": 5000, "successes": 180 }
    ]
  }
}
```

**Expected output:**
```json
{
  "results": [
    { "label": "with_incident", "probability": 0.23, "ci_lower": 0.204, "ci_upper": 0.258 },
    { "label": "without_incident", "probability": 0.036, "ci_lower": 0.031, "ci_upper": 0.042 }
  ],
  "comparison": {
    "relative_risk": 6.3889,
    "risk_difference": 0.194,
    "p_value": 0.0001,
    "significant": true
  }
}
```
