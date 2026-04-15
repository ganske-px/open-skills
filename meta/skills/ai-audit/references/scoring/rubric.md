# Scoring Rubric

Complete scoring system for CLAUDE.md audits.

## Dimension Weights

| Dimension | Weight | Max Points |
|-----------|--------|------------|
| Size | 15% | 15 |
| Structure | 20% | 20 |
| Permission Model | 15% | 15 |
| Specificity | 20% | 20 |
| Conciseness | 15% | 15 |
| References | 15% | 15 |
| **Total** | **100%** | **100** |

## Size Scoring (15 points)

```
Lines    Points    Rationale
≤60      15        Ideal - forces prioritization
61-100   13        Good - still focused
101-150  10        Acceptable - getting long
151-200  7         Warning - needs trimming
201-300  4         Poor - split required
>300     0         Failing - too long for context
```

## Structure Scoring (20 points)

### WHY Component (7 points)
```
Purpose statement present:     3 pts
Target audience defined:       2 pts
Key constraints listed:        2 pts
```

### WHAT Component (7 points)
```
Tech stack listed:            3 pts
Directory structure:          2 pts
Key files identified:         2 pts
```

### HOW Component (6 points)
```
Build/run commands:           2 pts
Code conventions:             2 pts
Test/verify commands:         2 pts
```

## Permission Model (15 points)

```
ALWAYS section:               5 pts
ASK section:                  5 pts
NEVER section:                5 pts
```

**Grade caps:**
- Missing NEVER (root file): max C
- Conflicting permissions: max D

## Specificity Scoring (20 points)

### Positive (add points)
```
Each measurable instruction:  +2 pts (max 10)
Examples:
- "Functions ≤20 lines"
- "Use snake_case for variables"
- "Every API endpoint needs test"
```

### Negative (subtract points)
```
Each vague instruction:       -2 pts
Examples:
- "write clean code"
- "follow best practices"
- "be careful with..."
- "proper error handling"
```

### File References (10 points)
```
Uses file:line references:    5 pts
Uses @path/ notation:         3 pts
Links to external docs:       2 pts
```

## Conciseness Scoring (15 points)

### No Duplication (8 points)
```
No linter rule duplication:   4 pts
No formatter rules:           2 pts
No git hook duplication:      2 pts
```

**Penalty detection patterns:**
- `semicolon`, `indent`, `spacing`: Prettier territory
- `camelCase`, `PascalCase`: ESLint/naming rules
- `pre-commit`, `husky`: Tool handles it

### Information Density (7 points)
```
Headers every 20 lines:       3 pts
No code blocks >10 lines:     2 pts
No repeated information:      2 pts
```

## References Scoring (15 points)

### Progressive Disclosure (10 points)
```
References external docs:     4 pts
Uses @docs/ or similar:       3 pts
Explicit inheritance:         3 pts
```

### External Links (5 points)
```
Architecture doc:             2 pts
API documentation:            2 pts
Contributing guide:           1 pt
```

## Grade Thresholds

| Score | Grade | Status | Action |
|-------|-------|--------|--------|
| 90-100 | A | Excellent | Maintain |
| 75-89 | B | Good | Minor tweaks |
| 60-74 | C | Acceptable | Needs work |
| 40-59 | D | Poor | Significant rewrite |
| 0-39 | F | Failing | Start fresh |

## Grade Caps (Overrides)

Regardless of point total, cap grade at:

| Condition | Max Grade |
|-----------|-----------|
| >300 lines | D |
| No NEVER section (root) | C |
| Permission conflicts | D |
| Contradictory instructions | C |
| >50% vague instructions | C |

## Bonus Points (Up to +5)

```
Proactive examples:           +2
Clear anti-patterns section:  +2
Agent-specific optimizations: +1
```

## Score Calculation Formula

```
base_score = (
  size_points +
  structure_points +
  permission_points +
  specificity_points +
  conciseness_points +
  reference_points
)

final_score = min(100, base_score + bonus_points)
grade = apply_caps(calculate_grade(final_score))
```

## Example Scoring

**File: CLAUDE.md (85 lines)**

```
Size:         10/15  (85 lines - acceptable)
Structure:    16/20  (missing some WHAT items)
Permissions:  15/15  (all sections present)
Specificity:  14/20  (some vague terms)
Conciseness:  12/15  (one large code block)
References:   10/15  (good progressive disclosure)
────────────────────
Total:        77/100
Grade:        B
```
