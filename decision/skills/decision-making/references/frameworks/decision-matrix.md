# Decision Matrix (Weighted Scoring)

> Structured framework for objectively comparing multiple options against defined criteria.

## When to Use

**Good fit:**
- Multiple viable options exist
- Criteria for evaluation are identifiable
- Need to reduce emotional/political bias
- Stakeholders disagree on "best" option
- Want documented rationale

**Poor fit:**
- Crisis situation (Chaotic domain) — act first
- Single obvious option
- Criteria fundamentally incomparable
- Decision already made emotionally — will game the matrix

---

## 5-Step Process

### Step 1: Define Options

List 2-5 realistic options. Include:
- Status quo / do nothing (if applicable)
- At least 2 alternatives
- "Hybrid" option if relevant

**Rules:**
- Options must be mutually exclusive
- Each must be genuinely viable
- No "straw man" options added to look good by comparison

---

### Step 2: Identify Criteria

List 4-8 evaluation criteria. Common categories:

| Category | Example Criteria |
|----------|------------------|
| Cost | Initial cost, TCO, maintenance |
| Time | Time to implement, time to value |
| Risk | Technical risk, business risk, security |
| Capability | Features, scalability, flexibility |
| Strategic | Alignment with goals, future optionality |
| People | Skill availability, team preference, learning curve |
| Quality | Reliability, performance, user experience |

**Rules:**
- Criteria must be independent (no double-counting)
- Criteria must be evaluable (can assign meaningful scores)
- Include both quantitative and qualitative

---

### Step 3: Assign Weights

Distribute 100% across criteria based on relative importance.

**Methods:**

**Simple ranking:**
1. Rank criteria by importance
2. Assign weights proportionally (most important ~30%, least ~5%)

**Pairwise comparison:**
Compare each criterion against every other. Count "wins."

**Stakeholder consensus:**
Each stakeholder assigns weights → average or discuss divergence.

**Rules:**
- Total must equal 100%
- No criterion above 40% (or it dominates)
- No criterion below 5% (or why include?)
- Document rationale for weights

---

### Step 4: Score Options

Rate each option against each criterion on consistent scale.

**Recommended: 1-5 Scale**

| Score | Meaning |
|-------|---------|
| 1 | Poor — Fails to meet criterion |
| 2 | Below average — Partially meets |
| 3 | Acceptable — Adequately meets |
| 4 | Good — Exceeds expectations |
| 5 | Excellent — Fully satisfies |

**Rules:**
- Score relative to the criterion, not absolute
- Allow half-points (3.5) if needed
- Document reasoning for non-obvious scores
- Use same evaluator(s) for consistency
- Separate facts from opinions

---

### Step 5: Calculate Weighted Total

For each option:
```
Weighted Score = Σ (Criterion Score × Criterion Weight)
```

**Example calculation:**
```
Option A:
  Cost (25%):      4 × 0.25 = 1.00
  Time (20%):      3 × 0.20 = 0.60
  Risk (20%):      4 × 0.20 = 0.80
  Capability (35%): 3 × 0.35 = 1.05
  ─────────────────────────────────
  Total:           3.45
```

---

## Matrix Template

```markdown
## Decision Matrix: [Decision Title]

**Date:** YYYY-MM-DD
**Evaluator(s):** [Names]

### Options
1. [Option A] - [Brief description]
2. [Option B] - [Brief description]
3. [Option C] - [Brief description]

### Weighted Scoring

| Criterion | Weight | Opt A | Opt B | Opt C | Notes |
|-----------|--------|-------|-------|-------|-------|
| [Criterion 1] | 25% | | | | |
| [Criterion 2] | 20% | | | | |
| [Criterion 3] | 20% | | | | |
| [Criterion 4] | 20% | | | | |
| [Criterion 5] | 15% | | | | |
| **TOTAL** | 100% | | | | |

### Weighted Totals

| Option | Weighted Score | Rank |
|--------|----------------|------|
| Option A | X.XX | |
| Option B | X.XX | |
| Option C | X.XX | |

### Analysis

**Winner:** [Option] with score of [X.XX]

**Gap analysis:** [How close were the top options?]

**Sensitivity check:** [Would changing weights change winner?]

### Recommendation

[Final recommendation with rationale]
```

---

## Sensitivity Analysis

Before finalizing, test robustness:

1. **Weight sensitivity:** Shift weights ±10% on key criteria. Does winner change?
2. **Score sensitivity:** Change uncertain scores ±1. Does winner change?
3. **Criterion removal:** Remove lowest-weighted criterion. Does winner change?

**If winner changes easily:**
- Decision is close — gather more data
- Re-examine criterion definitions
- Consider hybrid approaches

**If winner is stable:**
- Proceed with confidence
- Document in decision record

---

## Common Pitfalls

### Gaming the Matrix
**Problem:** Adjusting criteria/weights to justify pre-chosen option
**Fix:** Define criteria BEFORE evaluating options; have different people do each

### Too Many Criteria
**Problem:** Analysis paralysis, diluted weights
**Fix:** Maximum 8 criteria; merge related ones

### False Precision
**Problem:** Scores of 3.7 vs 3.8 treated as meaningful
**Fix:** Use whole numbers; acknowledge margin of error

### Missing Criterion
**Problem:** Important factor not captured
**Fix:** Pre-mortem check: "If we chose this and it failed, what would we have missed?"

### Incomparable Criteria
**Problem:** Mixing apples and oranges
**Fix:** Each criterion should be evaluable on same scale

### Anchoring
**Problem:** First option scored influences all others
**Fix:** Score all options on one criterion before moving to next

---

## Integration with Other Frameworks

### With Cynefin
- **Clear domain:** Matrix often overkill — just follow best practice
- **Complicated domain:** Full matrix analysis appropriate
- **Complex domain:** Light matrix for initial direction; expect to iterate

### With RAPID
- **R** builds and presents the matrix
- **I** may contribute scoring or criteria
- **D** makes final call (can override matrix result with rationale)

### With Pre-Mortem
After matrix identifies winner, pre-mortem stress-tests that option.

---

## Agent Application

When an agent creates a decision matrix:

1. Confirm decision is in Complicated domain (worth full analysis)
2. List options — verify mutual exclusivity
3. Identify criteria — check independence
4. Propose weights — get stakeholder input
5. Score objectively — note uncertainty
6. Calculate and present results
7. Highlight sensitivity if scores are close
8. Pass winner to pre-mortem for stress-testing

**Output should include:**
- Clear winner with score
- Margin of victory
- Sensitivity assessment
- Recommendation with confidence level

---

## References

- Kepner-Tregoe Decision Analysis
- Multi-Criteria Decision Analysis (MCDA)
- Pugh Matrix / Decision Matrix templates
