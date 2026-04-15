# Improvement Plan Template

Use this format to create actionable improvement plans after audit.

---

## Template

```markdown
## CLAUDE.md Improvement Plan

**Target:** {file_or_scope}
**Current Grade:** {current_grade} ({current_score}/100)
**Target Grade:** {target_grade}
**Estimated Changes:** {change_count}

### Quick Wins (Do First)

{quick_wins}

### Structural Changes

{structural_changes}

### Content Improvements

{content_improvements}

### Follow-up Items

{followup_items}

### Verification Checklist

{verification_checklist}
```

---

## Section Formats

### Quick Wins
Low-effort, high-impact changes. Do these immediately.

```markdown
1. **{title}** — Line {n}
   - Current: `{current}`
   - Change to: `{proposed}`
   - Points gained: +{points}

2. **{title}** — Line {n}
   - Current: `{current}`
   - Change to: `{proposed}`
   - Points gained: +{points}
```

### Structural Changes
Changes to file organization or sections.

```markdown
1. **Add {section_name}**
   - Location: After line {n}
   - Content:
     ```markdown
     {section_content}
     ```
   - Points gained: +{points}

2. **Extract to external file**
   - Move: Lines {start}-{end}
   - To: `{target_path}`
   - Replace with: `See {reference}`
   - Points gained: +{points}
```

### Content Improvements
Specific wording or instruction changes.

```markdown
1. **Replace vague instruction**
   - Line {n}: `{old}`
   - Change to: `{new}`
   - Why: {rationale}

2. **Add missing detail**
   - Section: {section_name}
   - Add: `{content}`
   - Why: {rationale}
```

### Follow-up Items
Changes that require more investigation or depend on others.

```markdown
- [ ] Verify {assumption} before changing {item}
- [ ] Coordinate with {team/person} on {change}
- [ ] Create {external_doc} to enable extraction
- [ ] Update {related_file} for consistency
```

### Verification Checklist
Run after implementing changes.

```markdown
- [ ] File passes all quality checks
- [ ] Line count within limits
- [ ] All sections present
- [ ] No vague instructions remain
- [ ] Cross-references work
- [ ] Permissions don't conflict with parent
- [ ] Re-run audit shows target grade
```

---

## Example Output

```markdown
## CLAUDE.md Improvement Plan

**Target:** /project/CLAUDE.md
**Current Grade:** C (65/100)
**Target Grade:** B (75+)
**Estimated Changes:** 8

### Quick Wins (Do First)

1. **Remove vague "best practices"** — Line 23
   - Current: `Follow best practices for error handling`
   - Change to: `Wrap external calls in try/catch; log errors with context`
   - Points gained: +4

2. **Add missing NEVER section** — After line 80
   - Current: No NEVER section
   - Change to: Add standard NEVER template
   - Points gained: +5

3. **Fix path notation** — Lines 45, 52, 67
   - Current: `./docs/api.md`
   - Change to: `@docs/api.md`
   - Points gained: +2

### Structural Changes

1. **Add NEVER section**
   - Location: After line 80 (end of ASK section)
   - Content:
     ```markdown
     ## NEVER
     - Commit API keys, passwords, or tokens
     - Push directly to main without PR
     - Skip failing tests
     - Delete production data
     ```
   - Points gained: +5

2. **Extract architecture diagram**
   - Move: Lines 55-75 (code block)
   - To: `@docs/architecture.md`
   - Replace with: `See architecture details: @docs/architecture.md`
   - Points gained: +4

### Content Improvements

1. **Replace vague code quality instruction**
   - Line 23: `Write clean, maintainable code`
   - Change to:
     ```markdown
     - Functions ≤25 lines
     - Max 3 parameters per function
     - Extract repeated code (3+ occurrences)
     ```
   - Why: Provides measurable criteria

2. **Add specific test requirement**
   - Section: HOW
   - Add: `Every PR must include tests for new code`
   - Why: Missing testing guidance

3. **Clarify deployment permission**
   - Line 78: `Be careful with deployments`
   - Change to: `Deployments require explicit user confirmation (ASK)`
   - Why: Vague, should be in ASK section

### Follow-up Items

- [ ] Create @docs/architecture.md before extracting diagram
- [ ] Verify NEVER items don't conflict with CI/CD needs
- [ ] Update .claude/agents/ files to reference new NEVER section
- [ ] Check if src/CLAUDE.md needs corresponding updates

### Verification Checklist

- [ ] Line count ≤100 (target: reduce from 145)
- [ ] All 6 sections present (WHY/WHAT/HOW/ALWAYS/ASK/NEVER)
- [ ] Zero vague instructions
- [ ] All @references/ paths resolve
- [ ] No code blocks >10 lines
- [ ] Re-run /ai-audit shows grade B or higher
```

---

## Point Estimation Guide

| Change Type | Typical Points |
|-------------|----------------|
| Add missing section | +5 |
| Fix vague instruction | +2 to +4 |
| Extract large code block | +2 to +4 |
| Fix path notation | +1 to +2 |
| Add file:line reference | +1 |
| Remove linter duplication | +2 |
| Add progressive disclosure | +3 |
