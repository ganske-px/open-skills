# Cross-File Consistency Checklist

Validation rules for multiple CLAUDE.md files in a project.

## Path Notation (10 points)

All files should use consistent path notation.

| Check | Points |
|-------|--------|
| Uniform `@path/` or `./path/` | 5 |
| No mixed notations in same file | 3 |
| Paths resolve correctly | 2 |

**Detection:**
```bash
# Find all path patterns
grep -oh "@[a-zA-Z_-]*/" *.md | sort -u
grep -oh "\./[a-zA-Z_-]*/" *.md | sort -u
```

**Good:** All use `@docs/`, `@agents/`
**Bad:** Mix of `@docs/`, `./docs/`, `docs/`

## Inheritance Chain (15 points)

Parent-child relationships must be explicit.

| Check | Points |
|-------|--------|
| Root inherits nothing or explicit global | 5 |
| Subdirectory files reference parent | 5 |
| No circular inheritance | 5 |

**Required pattern in child files:**
```markdown
Inherits from: @../CLAUDE.md
```

**Verification:**
```bash
# Find inheritance declarations
grep -r "Inherits\|Extends\|Parent:" **/*CLAUDE*.md
```

## Permission Alignment (20 points)

No conflicts in ALWAYS/ASK/NEVER across hierarchy.

| Check | Points |
|-------|--------|
| Child doesn't ALWAYS what parent NEVERs | 10 |
| Child doesn't NEVER what parent ALWAYS | 5 |
| Permissions only get stricter down chain | 5 |

**Critical violation:** Child allows what root forbids

**Detection:**
```bash
# Extract NEVER items from root
# Compare against ALWAYS in children
```

## Agent Definition Standards (15 points)

All agent files should follow same structure.

| Check | Points |
|-------|--------|
| Consistent frontmatter format | 5 |
| Standard sections present | 5 |
| Naming convention followed | 5 |

**Expected agent structure:**
```markdown
---
name: agent-{role}
description: ...
---

# Agent Name

## Role
## Responsibilities
## Tools
## Boundaries
```

## Duplicate Detection (15 points)

Same information shouldn't appear multiple places.

| Check | Points |
|-------|--------|
| No duplicated rules | 5 |
| No repeated commands | 5 |
| No copied code blocks | 5 |

**Detection:**
```bash
# Find similar lines across files
# Flag exact duplicates >3 lines
```

## Terminology Consistency (10 points)

Same concepts should use same terms.

| Check | Points |
|-------|--------|
| Consistent naming (agent vs bot vs assistant) | 4 |
| Consistent actions (deploy vs release vs ship) | 3 |
| Consistent paths (src vs source) | 3 |

## Cross-Reference Validity (15 points)

All references must resolve.

| Check | Points |
|-------|--------|
| Internal links work | 5 |
| External file refs exist | 5 |
| Agent refs point to real agents | 5 |

**Verification:**
```bash
# Extract all file references
grep -oh "@[a-zA-Z/_-]*\.md" *.md | while read f; do
  [ -f "${f#@}" ] || echo "Missing: $f"
done
```

## Total Score

```
Path Notation:    /10
Inheritance:      /15
Permissions:      /20
Agent Standards:  /15
No Duplicates:    /15
Terminology:      /10
Cross-Refs:       /15
──────────────────────
Total:            /100
```

## Common Consistency Issues

| Issue | Fix |
|-------|-----|
| Mixed path notation | Pick one, search-replace |
| Missing inheritance | Add "Inherits from:" to children |
| Permission conflict | Resolve toward stricter |
| Duplicate rules | Extract to shared doc, reference |
| Broken cross-refs | Update paths or create missing files |
