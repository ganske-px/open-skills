---
name: ai-audit
description: |
  Audit and improve CLAUDE.md files and codebase AI-friendliness. Use when asked to
  "audit CLAUDE.md", "check AI-friendliness", "review agent configuration",
  "improve codebase for AI", "validate CLAUDE files", or "score documentation".
  Handles file scanning, consistency checks, scoring, and cross-file validation.
  Do NOT use to create or edit skills — use your prompt-engineering skill.
  Do NOT use to create hooks — use your hook-creation skill.
allowed_tools:
  - Read
  - Glob
  - Grep
  - Bash
  - Write
  - Edit
---

# AI Audit Skill

Audit CLAUDE.md quality and codebase AI-readiness.

## Quick Decision

| Request | Mode | Action |
|---------|------|--------|
| "audit this file" | Single | Deep analysis of specified CLAUDE.md |
| "check all CLAUDE files" | Codebase | Scan and score all files |
| "find inconsistencies" | Consistency | Cross-file validation |
| "check AI readiness" | IAEx | Agent experience metrics |
| "review permissions" | Security | NEVER section, governance |
| "improve [file]" | Fix | Apply suggested improvements |

## Workflow

### 1. Detect Mode

Parse user request for keywords:
- Single: "this", "file", specific path
- Codebase: "all", "scan", "codebase"
- Consistency: "inconsisten", "conflict", "cross"
- IAEx: "readiness", "experience", "agent"
- Security: "permission", "security", "never"

### 2. Gather Files

**Single Mode:**
```bash
# Use specified path or find nearest CLAUDE.md
```

**Codebase Mode:**
```bash
# Find all CLAUDE.md files
glob "**/*CLAUDE*.md"
```

### 3. Score Each File

For each file, apply checklists from `references/checklists/`:
- `claudemd-quality.md` - Core structure/content
- `iaex-metrics.md` - Agent experience
- `consistency.md` - Cross-file validation
- `security-governance.md` - Permission audit

Use rubric from `references/scoring/rubric.md` to calculate:
- Dimension scores (weighted)
- Total score (0-100)
- Grade (A/B/C/D/F)

### 4. Generate Report

Use templates from `references/templates/`:
- `report-single.md` for single file
- `report-codebase.md` for full scan
- `improvement-plan.md` for action items

### 5. Offer Improvements

If user requests fixes:
1. Apply non-destructive edits
2. Show diff preview before changes
3. Verify changes don't break functionality

## Scoring Dimensions

| Dimension | Weight | Key Checks |
|-----------|--------|------------|
| Size | 15% | ≤60 ideal, ≤300 max |
| Structure | 20% | WHY-WHAT-HOW present |
| Permission Model | 15% | ALWAYS/ASK/NEVER defined |
| Specificity | 20% | Actionable instructions |
| Conciseness | 15% | No linter duplication |
| References | 15% | Progressive disclosure |

## Grade Thresholds

| Grade | Score | Meaning |
|-------|-------|---------|
| A | 90-100 | Excellent, minimal improvements |
| B | 75-89 | Good, minor issues |
| C | 60-74 | Acceptable, needs work |
| D | 40-59 | Poor, significant issues |
| F | 0-39 | Failing, major rewrite needed |

## Anti-Patterns to Flag

**Critical (blocks grade A):**
- >300 lines
- Missing NEVER section in root file
- Permission conflicts in hierarchy
- Contradictory instructions

**Warnings (cap at grade B):**
- Vague instructions ("write clean code")
- Linter rule duplication
- Large code blocks (>10 lines inline)
- Wall of text (no headers after 20 lines)

**Suggestions (informational):**
- No file:line references
- Missing commands section
- Could extract to external doc

## Commands to Execute

### Find All CLAUDE Files
```bash
find . -name "*CLAUDE*.md" -type f | head -50
```

### Count Lines
```bash
wc -l <file>
```

### Check for Sections
```bash
grep -E "^##?\s+(WHY|WHAT|HOW|ALWAYS|ASK|NEVER)" <file>
```

### Find Vague Instructions
```bash
grep -i "best practice\|clean code\|be careful\|proper\|appropriate" <file>
```

### Find Large Code Blocks
```bash
awk '/```/{p=!p;if(p)n=NR}p&&NR-n>10{print FILENAME":"NR; exit}' <file>
```

## Output Format

Always output structured report with:
1. **Header** - File path, grade, score
2. **Critical** - Must fix issues
3. **Warnings** - Should fix issues
4. **Suggestions** - Could improve items
5. **Proposed Edits** - Concrete diff suggestions

## Proactive Triggers

Suggest audit when noticing:
- CLAUDE.md >200 lines being edited
- Same correction needed 2+ times in session
- New project initialization
- Agent definition changes
- Permission-related confusion

Output: `Consider running /ai-audit to check for improvement opportunities.`

## Reference Files

- `references/checklists/claudemd-quality.md` - Core quality checks
- `references/checklists/iaex-metrics.md` - Agent experience
- `references/checklists/consistency.md` - Cross-file validation
- `references/checklists/security-governance.md` - Security audit
- `references/scoring/rubric.md` - Point system
- `references/templates/report-single.md` - Single file output
- `references/templates/report-codebase.md` - Codebase scan output
- `references/templates/improvement-plan.md` - Action plan

## Integration

| Tool | Purpose |
|------|---------|
| Memory MCP | Track audit history, improvements over time |
| prompt-engineering skill | Fix low-scoring agent definitions |
| creating-skills skill | Improve poorly structured skills |

## Examples

**Single file audit:**
```
User: audit the root CLAUDE.md
→ Read CLAUDE.md
→ Apply all checklists
→ Calculate score
→ Output report-single format
```

**Codebase scan:**
```
User: check all CLAUDE files in this project
→ Glob **/*CLAUDE*.md
→ Score each file
→ Identify consistency issues
→ Output report-codebase format
```

**Fix mode:**
```
User: improve the agent definitions
→ Find .claude/agents/*.md
→ Audit each
→ Propose edits with diffs
→ Apply after confirmation
```
