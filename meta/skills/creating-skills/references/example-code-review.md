# Complete Example: Code Review Skill

Walkthrough of creating a skill end-to-end using the 4-phase workflow.

## User Request
"Create a skill for managing code reviews"

## Phase 1: Discovery (Claude asks)

1. **Purpose**: What specific problem? → "Standardize review process, ensure checklist is followed"
2. **Triggers**: When to use? → "review code", "PR review", "check this PR"
3. **Workflow**: Steps? → "1. Get PR diff, 2. Check against standards, 3. Generate feedback"
4. **Resources**: Tools? → "Bash (git), Read, Write"
5. **Constraints**: What NOT to do? → "Don't auto-approve, don't modify code"
6. **Examples**: Success looks like? → "Structured feedback with categories"

## Phase 2: Design

- Name: `code-review`
- Description: "Perform standardized code reviews. Use when asked to 'review code', 'check this PR', or 'give feedback on changes'. Handles diff analysis, checklist verification, and structured feedback generation. Do NOT use when user wants to write or fix code (that's implementation, not review)."

## Phase 3: Implementation

```markdown
---
name: code-review
description: Perform standardized code reviews. Use when asked to 'review code', 'check this PR', or 'give feedback on changes'. Handles diff analysis, checklist verification, and structured feedback generation. Do NOT use when user wants to write or fix code.
allowed-tools: Bash, Read, Write, Grep
---

# Code Review

Standardized code review following team checklist.

## When to Use

- User asks to review code changes
- User mentions "PR review" or "code feedback"
- User shares a diff or branch for review

## Workflow

1. Get the diff (git diff or provided content)
2. Check each category in the review checklist
3. Note issues with severity (critical, warning, suggestion)
4. Generate structured feedback markdown

## Review Checklist

- [ ] No hardcoded secrets or credentials
- [ ] Error handling is present
- [ ] Tests cover new functionality
- [ ] No obvious performance issues
- [ ] Code follows project style guide

## Anti-Patterns

- Never auto-approve without human review
- Never modify the code directly during review
- Never skip the checklist

## Output Format

### Code Review: [PR/Branch Name]

**Summary**: [1-2 sentence overview]

**Critical Issues**:
- [issue with file:line reference]

**Warnings**:
- [issue with file:line reference]

**Suggestions**:
- [improvement idea]

**Checklist Status**: X/Y items passed
```

## Phase 4: Integration

Created: `.claude/skills/code-review/SKILL.md`
Updated: Team documentation to reference new skill
