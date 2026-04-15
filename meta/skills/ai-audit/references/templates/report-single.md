# Single File Audit Report Template

Use this format when auditing one CLAUDE.md file.

---

## Template

```markdown
## CLAUDE.md Audit: {file_path}

**Grade:** {grade} ({score}/100)
**Lines:** {line_count} ({size_status})

### Dimension Scores

| Dimension | Score | Notes |
|-----------|-------|-------|
| Size | {size}/15 | {size_note} |
| Structure | {structure}/20 | {structure_note} |
| Permissions | {permissions}/15 | {permissions_note} |
| Specificity | {specificity}/20 | {specificity_note} |
| Conciseness | {conciseness}/15 | {conciseness_note} |
| References | {references}/15 | {references_note} |

### Critical Issues ({critical_count})

{critical_issues}

### Warnings ({warning_count})

{warnings}

### Suggestions ({suggestion_count})

{suggestions}

### Proposed Edits

{edits}
```

---

## Field Definitions

### Header Fields
- `file_path`: Absolute or relative path to audited file
- `grade`: A/B/C/D/F based on score
- `score`: Total points out of 100
- `line_count`: `wc -l` result
- `size_status`: "ideal" / "acceptable" / "needs reduction"

### Issues Format

**Critical:**
```markdown
- **Line {n}:** {description}
  - Impact: {why this matters}
  - Fix: {what to do}
```

**Warnings:**
```markdown
- **Line {n}:** {description}
  - Suggestion: {recommendation}
```

**Suggestions:**
```markdown
- {description}
```

### Proposed Edits Format

```markdown
#### Edit {n}: {description}

**Location:** Line {start_line}-{end_line}

**Current:**
```{language}
{old_content}
```

**Proposed:**
```{language}
{new_content}
```

**Rationale:** {why_change}
```

---

## Example Output

```markdown
## CLAUDE.md Audit: /project/CLAUDE.md

**Grade:** B (78/100)
**Lines:** 145 (acceptable)

### Dimension Scores

| Dimension | Score | Notes |
|-----------|-------|-------|
| Size | 10/15 | 145 lines - consider extraction |
| Structure | 18/20 | Good WHY-WHAT-HOW |
| Permissions | 15/15 | All sections present |
| Specificity | 12/20 | 3 vague instructions |
| Conciseness | 10/15 | One large code block |
| References | 13/15 | Good external refs |

### Critical Issues (0)

None

### Warnings (2)

- **Line 45:** Vague instruction "write clean code"
  - Suggestion: Replace with measurable criteria

- **Line 89:** Code block exceeds 10 lines
  - Suggestion: Extract to external file, reference

### Suggestions (3)

- Add specific function length limit
- Reference architecture doc for structure details
- Add file:line format for key files

### Proposed Edits

#### Edit 1: Replace vague instruction

**Location:** Line 45

**Current:**
```markdown
- Write clean code and follow best practices
```

**Proposed:**
```markdown
- Functions ≤20 lines; extract helpers for longer logic
- Use descriptive names: `getUserById()` not `get()`
- Every public method requires unit test
```

**Rationale:** Provides measurable, verifiable criteria

#### Edit 2: Extract code block

**Location:** Lines 89-105

**Current:**
```markdown
```typescript
// 15 lines of example code
```
```

**Proposed:**
```markdown
See example implementation: `@docs/examples/auth.ts:1-15`
```

**Rationale:** Reduces CLAUDE.md size, uses file reference
```

---

## Notes for Output

1. Always include all sections, even if empty
2. Use consistent line number format: `Line {n}` or `Lines {start}-{end}`
3. Proposed edits should be copy-paste ready
4. Include rationale for every edit
5. Order issues by severity (critical first)
