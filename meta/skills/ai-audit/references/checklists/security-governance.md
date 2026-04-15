# Security & Governance Checklist

Audit for security practices and governance in CLAUDE.md files.

## NEVER Section (25 points)

Root CLAUDE.md must have explicit prohibitions.

| Check | Points |
|-------|--------|
| NEVER section exists | 10 |
| Credential exposure forbidden | 5 |
| Destructive operations listed | 5 |
| Production access restricted | 5 |

**Required items in root NEVER:**
```markdown
## NEVER
- Commit API keys, passwords, tokens, or secrets
- Push directly to main/master branch
- Delete production data without backup
- Bypass CI/CD checks
- Skip failing tests to deploy
```

**Detection:**
```bash
grep -A 20 "^## NEVER" CLAUDE.md
```

## Sensitive Paths (20 points)

Sensitive locations must be documented.

| Check | Points |
|-------|--------|
| .env files mentioned | 5 |
| Credential paths identified | 5 |
| Config with secrets marked | 5 |
| Production configs flagged | 5 |

**Common sensitive paths:**
- `.env`, `.env.local`, `.env.production`
- `credentials/`, `secrets/`, `keys/`
- `config/production.json`
- `*.pem`, `*.key`

## Access Control (20 points)

Permission boundaries defined.

| Check | Points |
|-------|--------|
| Production vs dev environments | 5 |
| Database access rules | 5 |
| External API restrictions | 5 |
| File system boundaries | 5 |

**Questions to answer:**
- Can agent modify production?
- Can agent access all databases?
- Can agent call external APIs freely?
- Can agent write anywhere on disk?

## Audit Trail (15 points)

Changes should be traceable.

| Check | Points |
|-------|--------|
| Git workflow documented | 5 |
| PR requirements stated | 5 |
| Review process defined | 5 |

**Expected patterns:**
```markdown
## Git Workflow
- All changes via PR
- Requires 1 approval
- CI must pass
```

## Dependency Security (10 points)

Third-party risks managed.

| Check | Points |
|-------|--------|
| Dependency update policy | 4 |
| Security scan mentioned | 3 |
| Version pinning strategy | 3 |

## Data Handling (10 points)

PII and sensitive data rules.

| Check | Points |
|-------|--------|
| PII handling documented | 4 |
| Data retention rules | 3 |
| Logging restrictions | 3 |

**Key concerns:**
- No PII in logs
- No sensitive data in error messages
- Proper encryption for storage

## Total Score

```
NEVER Section:     /25
Sensitive Paths:   /20
Access Control:    /20
Audit Trail:       /15
Dependencies:      /10
Data Handling:     /10
────────────────────────
Total:             /100
```

## Security Grade Impact

| Finding | Max Grade |
|---------|-----------|
| No NEVER section (root) | C |
| Credentials in repo | F |
| No production protection | D |
| Missing audit trail | C |

## Remediation Templates

### Missing NEVER Section
```markdown
## NEVER
- Commit files containing API keys, passwords, or tokens
- Push directly to main branch without PR
- Delete or modify production databases
- Disable or skip security checks
- Log sensitive user data (PII, passwords)
```

### Missing Sensitive Paths
```markdown
## Sensitive Files
- `.env*` - Environment variables, may contain secrets
- `config/production.json` - Production configuration
- `credentials/` - Service account keys (gitignored)
```

### Missing Access Control
```markdown
## Access Boundaries
- **Production:** Read-only, changes via CI/CD only
- **Database:** Dev/staging only, prod requires approval
- **External APIs:** Sandboxed endpoints only
- **File System:** Project directory only
```
