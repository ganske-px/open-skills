# Codebase Audit Report Template

Use this format when scanning all CLAUDE.md files in a project.

---

## Template

```markdown
## Codebase CLAUDE.md Audit

**Files Scanned:** {file_count}
**Overall Grade:** {overall_grade} ({average_score}/100)
**Date:** {audit_date}

### Summary

| Grade | Count | Files |
|-------|-------|-------|
| A | {a_count} | {a_files} |
| B | {b_count} | {b_files} |
| C | {c_count} | {c_files} |
| D | {d_count} | {d_files} |
| F | {f_count} | {f_files} |

### File Scores

| File | Lines | Grade | Score | Top Issue |
|------|-------|-------|-------|-----------|
{file_rows}

### Critical Issues Across Codebase

{critical_issues}

### Consistency Problems

{consistency_issues}

### IAEx Assessment

| Metric | Score | Status |
|--------|-------|--------|
| Discovery | {discovery}/25 | {discovery_status} |
| Navigation | {navigation}/25 | {navigation_status} |
| Commands | {commands}/20 | {commands_status} |
| Conventions | {conventions}/15 | {conventions_status} |
| Safety | {safety}/15 | {safety_status} |
| **Total** | **{iaex_total}/100** | **{iaex_grade}** |

### Recommendations

{recommendations}

### Priority Actions

{priority_actions}
```

---

## Field Definitions

### Summary Fields
- `file_count`: Total CLAUDE.md files found
- `overall_grade`: Grade based on average score
- `average_score`: Mean of all file scores
- `audit_date`: ISO date of audit

### File Rows Format
```markdown
| /path/to/CLAUDE.md | 85 | B | 78 | Missing NEVER section |
```

### Critical Issues Format
```markdown
1. **{file_path}**
   - {issue_description}
   - Impact: {impact}
   - Priority: {high/medium/low}
```

### Consistency Issues Format
```markdown
- **Path Notation:** {description}
  - Files affected: {list}
  - Fix: {recommendation}

- **Permission Conflict:** {description}
  - Conflicting files: {list}
  - Resolution: {recommendation}
```

### Recommendations Format
```markdown
1. **{category}:** {recommendation}
   - Effort: {low/medium/high}
   - Impact: {low/medium/high}
```

### Priority Actions Format
```markdown
1. [ ] {action_item} — {file_path}
2. [ ] {action_item} — {file_path}
```

---

## Example Output

```markdown
## Codebase CLAUDE.md Audit

**Files Scanned:** 12
**Overall Grade:** B (76/100)
**Date:** 2025-01-15

### Summary

| Grade | Count | Files |
|-------|-------|-------|
| A | 2 | CLAUDE.md, .claude/CLAUDE.md |
| B | 5 | src/, api/, lib/, tests/, docs/ |
| C | 3 | scripts/, tools/, deploy/ |
| D | 1 | legacy/ |
| F | 1 | experimental/ |

### File Scores

| File | Lines | Grade | Score | Top Issue |
|------|-------|-------|-------|-----------|
| CLAUDE.md | 58 | A | 92 | None |
| .claude/CLAUDE.md | 45 | A | 90 | None |
| src/CLAUDE.md | 120 | B | 82 | Large code block |
| api/CLAUDE.md | 95 | B | 78 | Vague instructions |
| lib/CLAUDE.md | 88 | B | 75 | Missing references |
| tests/CLAUDE.md | 65 | B | 77 | No WHY section |
| docs/CLAUDE.md | 110 | B | 76 | Duplication |
| scripts/CLAUDE.md | 180 | C | 65 | Too long |
| tools/CLAUDE.md | 156 | C | 62 | Missing permissions |
| deploy/CLAUDE.md | 200 | C | 60 | No NEVER section |
| legacy/CLAUDE.md | 280 | D | 45 | Multiple issues |
| experimental/CLAUDE.md | 350 | F | 32 | Exceeds limit |

### Critical Issues Across Codebase

1. **deploy/CLAUDE.md**
   - Missing NEVER section with production safeguards
   - Impact: Agents may perform destructive operations
   - Priority: High

2. **experimental/CLAUDE.md**
   - 350 lines exceeds 300 line maximum
   - Impact: Context overflow, missed instructions
   - Priority: High

### Consistency Problems

- **Path Notation:** Mixed @path/ and ./path/ usage
  - Files affected: src/, api/, lib/
  - Fix: Standardize on @path/ notation

- **Permission Conflict:** deploy/ allows what root forbids
  - deploy/CLAUDE.md: ALWAYS push to main
  - CLAUDE.md: NEVER push directly to main
  - Resolution: Remove from deploy/ALWAYS, add to ASK

### IAEx Assessment

| Metric | Score | Status |
|--------|-------|--------|
| Discovery | 22/25 | Good |
| Navigation | 20/25 | Good |
| Commands | 18/20 | Good |
| Conventions | 10/15 | Needs work |
| Safety | 8/15 | Needs work |
| **Total** | **78/100** | **B** |

### Recommendations

1. **Security:** Add NEVER sections to all subdirectory files
   - Effort: Low
   - Impact: High

2. **Consistency:** Standardize path notation across all files
   - Effort: Medium
   - Impact: Medium

3. **Size:** Split experimental/CLAUDE.md into focused files
   - Effort: High
   - Impact: High

### Priority Actions

1. [ ] Add NEVER section — deploy/CLAUDE.md
2. [ ] Split or reduce — experimental/CLAUDE.md
3. [ ] Resolve permission conflict — deploy/CLAUDE.md
4. [ ] Standardize paths — src/, api/, lib/
5. [ ] Add conventions doc — link from all files
```
