# CLAUDE.md Quality Checklist

Scoring criteria for CLAUDE.md file quality.

## Size (15 points max)

| Condition | Points | Note |
|-----------|--------|------|
| ≤60 lines | 15 | Ideal - concise and focused |
| 61-150 lines | 12 | Good - may need trimming |
| 151-300 lines | 8 | Acceptable - consider extraction |
| >300 lines | 0 | Too long - requires splitting |

**Check command:**
```bash
wc -l <file>
```

## Structure (20 points max)

### WHY Section (7 points)
Answers: Purpose, audience, constraints

| Present | Points |
|---------|--------|
| Clear purpose statement | 3 |
| Target audience defined | 2 |
| Key constraints listed | 2 |

**Patterns to find:**
- `## WHY`, `## Purpose`, `## About`
- "This project...", "The goal...", "Used for..."

### WHAT Section (7 points)
Answers: Stack, structure, key files

| Present | Points |
|---------|--------|
| Tech stack listed | 3 |
| Directory structure | 2 |
| Key files identified | 2 |

**Patterns to find:**
- `## WHAT`, `## Stack`, `## Structure`
- Framework names, file paths

### HOW Section (6 points)
Answers: Commands, conventions, verification

| Present | Points |
|---------|--------|
| Build/run commands | 2 |
| Code conventions | 2 |
| Test/verify commands | 2 |

**Patterns to find:**
- `## HOW`, `## Commands`, `## Development`
- Backtick commands, `npm`, `python`, etc.

## Permission Model (15 points max)

| Section | Points | Description |
|---------|--------|-------------|
| ALWAYS | 5 | Safe auto-approve operations |
| ASK | 5 | High-impact, needs confirmation |
| NEVER | 5 | Security constraints |

**Required patterns:**
```markdown
## ALWAYS
- [safe operations]

## ASK
- [risky operations]

## NEVER
- [forbidden actions]
```

**Critical:** Root CLAUDE.md missing NEVER = max grade C

## Specificity (20 points max)

### Actionable Instructions (10 points)

**Good (2 pts each):**
- Measurable: "Functions ≤20 lines"
- Specific: "Use `getUserById()` not `get()`"
- Verifiable: "Every public method has test"

**Bad (0 pts, -2 penalty each):**
- Vague: "write clean code"
- Abstract: "follow best practices"
- Unmeasurable: "be careful with..."

**Detection patterns:**
```bash
# Vague terms (penalty)
grep -i "best practice\|clean code\|be careful\|proper\|appropriate\|good\|nice" <file>
```

### File References (10 points)

| Format | Points |
|--------|--------|
| `file:line` references | 5 |
| Uses `@path/` notation | 3 |
| Links to external docs | 2 |

**Good:** `See authentication in src/auth.ts:45`
**Bad:** Large inline code blocks

## Conciseness (15 points max)

### No Linter Duplication (8 points)

Deduct points for duplicating what tools handle:
- Prettier/ESLint formatting rules: -4
- TypeScript type rules: -2
- Git workflow rules covered by hooks: -2

**Detection:**
```bash
grep -i "semicolon\|indent\|spacing\|trailing\|camelcase\|pascal" <file>
```

### Information Density (7 points)

| Condition | Points |
|-----------|--------|
| No wall of text (headers every 20 lines) | 3 |
| No inline code blocks >10 lines | 2 |
| No repeated information | 2 |

## References (15 points max)

### Progressive Disclosure (10 points)

| Practice | Points |
|----------|--------|
| References external docs for details | 4 |
| Uses `@docs/` or `@references/` | 3 |
| Inherits from parent explicitly | 3 |

### External Documentation (5 points)

| Has | Points |
|-----|--------|
| Architecture doc reference | 2 |
| API doc reference | 2 |
| Contributing guide reference | 1 |

## Total Scoring

```
Size:        /15
Structure:   /20
Permissions: /15
Specificity: /20
Conciseness: /15
References:  /15
─────────────────
Total:       /100
```

## Grade Assignment

| Score | Grade | Action |
|-------|-------|--------|
| 90-100 | A | Maintain |
| 75-89 | B | Minor fixes |
| 60-74 | C | Needs work |
| 40-59 | D | Significant rewrite |
| 0-39 | F | Start over |
