# IAEx (Intelligent Agent Experience) Metrics

Checklist for evaluating how AI-friendly a codebase is.

## Discovery (25 points)

Can an agent quickly understand the project?

| Criterion | Points | Check |
|-----------|--------|-------|
| CLAUDE.md exists at root | 5 | `test -f CLAUDE.md` |
| README.md with quick start | 5 | `grep -l "quick start\|getting started" README.md` |
| Clear entry points documented | 5 | Key files listed |
| Directory structure explained | 5 | Structure section present |
| Dependencies documented | 5 | package.json, requirements.txt, etc. |

## Navigation (25 points)

Can an agent find what it needs?

| Criterion | Points | Check |
|-----------|--------|-------|
| Consistent file naming | 5 | kebab-case or camelCase throughout |
| Logical directory structure | 5 | src/, tests/, docs/ pattern |
| Index files in directories | 5 | index.ts, __init__.py, etc. |
| Cross-references work | 5 | Links/paths resolve |
| No orphan files | 5 | All files reachable from entry |

## Commands (20 points)

Can an agent run standard operations?

| Criterion | Points | Check |
|-----------|--------|-------|
| Build command documented | 4 | `npm build`, `make`, etc. |
| Test command documented | 4 | `npm test`, `pytest`, etc. |
| Lint command documented | 4 | `npm lint`, `ruff`, etc. |
| Dev server command | 4 | `npm dev`, `python -m`, etc. |
| Deploy/release process | 4 | CI/CD or manual steps |

**Verification:**
```bash
grep -E "npm |yarn |pnpm |python |make |cargo " CLAUDE.md
```

## Conventions (15 points)

Are patterns consistent and documented?

| Criterion | Points | Check |
|-----------|--------|-------|
| Code style documented | 3 | Not linter rules, high-level patterns |
| Naming conventions clear | 3 | Component names, file names |
| Error handling pattern | 3 | Try/catch, Result types |
| Testing patterns | 3 | Unit, integration, e2e |
| Git workflow | 3 | Branch naming, commit style |

## Safety Rails (15 points)

Are dangerous operations protected?

| Criterion | Points | Check |
|-----------|--------|-------|
| NEVER section exists | 5 | Explicit forbidden actions |
| Env vars documented | 3 | .env.example or similar |
| Sensitive paths marked | 3 | Credentials, keys identified |
| Pre-commit hooks | 2 | .husky, pre-commit config |
| Branch protection noted | 2 | main/master rules |

## Agent-Specific Features

### Skill Availability
- [ ] Custom skills in `.claude/skills/`
- [ ] Skills documented in CLAUDE.md
- [ ] Skills have proper SKILL.md format

### Agent Definitions
- [ ] Agents in `.claude/agents/`
- [ ] Agents follow naming convention
- [ ] Agent responsibilities clear

### Context Engineering
- [ ] Progressive disclosure used
- [ ] Large context in external files
- [ ] `@notation` for file references

## IAEx Score Calculation

```
Discovery:   /25
Navigation:  /25
Commands:    /20
Conventions: /15
Safety:      /15
────────────────
Total:       /100
```

## IAEx Grade Thresholds

| Score | Grade | Meaning |
|-------|-------|---------|
| 90-100 | A | Agent-optimized |
| 75-89 | B | Agent-friendly |
| 60-74 | C | Agent-usable |
| 40-59 | D | Agent-hostile |
| 0-39 | F | Agent-incompatible |

## Common IAEx Improvements

| Issue | Fix |
|-------|-----|
| No CLAUDE.md | Create with WHY-WHAT-HOW template |
| Missing commands | Add Commands section |
| No safety rails | Add NEVER section |
| Poor navigation | Add directory structure doc |
| Inconsistent conventions | Document and enforce patterns |
