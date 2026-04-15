# quality/

Automated guard hooks that enforce quality standards on every Claude Code session. Install these once and they run in the background — catching terminology violations and file routing errors before they reach your codebase or documents.

## What's Included

```
quality/
  hooks/
    forbidden-terms-guard.js    # Blocks output containing configured forbidden terms
    output-path-validator.js    # Validates that files are written to the correct locations
```

**2 hooks.**

No skills or agents — quality enforcement is fully automatic.

## Hooks

### forbidden-terms-guard.js
Scans all generated text output for terms on a configurable forbidden list. When a match is found, it blocks the output and returns an error message explaining which term was used and what the preferred alternative is.

**Configuration** (at the top of the file):
```javascript
const FORBIDDEN_TERMS = [
  { term: "users", preferred: "customers", context: "customer-facing docs" },
  { term: "bug", preferred: "defect", context: "formal reports" },
  // add your own...
];
const APPLY_TO = ["Write", "Edit"];  // which tools to guard
```

**When to use this hook:**
- You have a style guide or brand guide with specific terminology rules
- You are migrating from one term to another (e.g., "clients" → "customers")
- You want to enforce legal/compliance language (e.g., avoid "guarantee" in marketing copy)
- You are working in a regulated domain where specific terms have legal implications

### output-path-validator.js
Validates that files written by Claude Code go to the correct locations based on file type and content. Prevents common routing mistakes: research going into the wrong folder, specs landing in the wrong project, temporary files persisting in production directories.

**Configuration** (at the top of the file):
```javascript
const ROUTING_RULES = [
  { pattern: "*.spec.md", allowedPaths: ["specs/", "docs/specs/"] },
  { pattern: "*.research.md", allowedPaths: ["research/"] },
  { pattern: "*.tmp.*", blockedPaths: ["src/", "docs/"] },
  // add your own...
];
```

**When to use this hook:**
- Your workspace has a structured folder convention that matters (wiki, knowledge base, spec repository)
- You want to prevent accidental writes to sensitive directories
- You are onboarding a new team member and want to enforce structure automatically
- You have CI/CD checks that depend on files being in the right locations

## Dependency Graph

```
forbidden-terms-guard.js    output-path-validator.js
         ↓                            ↓
    (PostToolUse: Write/Edit)   (PostToolUse: Write)
         ↓                            ↓
     blocks output              validates path
     + explains fix              + blocks if wrong
```

Both hooks are completely independent — install one or both. They run at the same hook point (`PostToolUse`) and can be chained.

## How They Relate to Other Disciplines

Quality hooks are the enforcement layer for conventions defined elsewhere:
- `strategy/hooks/data-marker-audit.js` enforces evidence citation rules in strategy documents
- `strategy/hooks/workflow-guard.js` enforces structural completeness in strategy documents
- `discovery/hooks/evidence-guard.js` enforces evidence requirements in research output
- `quality/hooks/forbidden-terms-guard.js` enforces terminology across all output
- `quality/hooks/output-path-validator.js` enforces file routing across all writes

Install the `quality/` hooks for general-purpose enforcement. Install the discipline-specific hooks when you need enforcement scoped to a particular workflow.

## Quick Start

**Enforce terminology rules:**
Edit `forbidden-terms-guard.js` — add your forbidden terms and their preferred alternatives to the `FORBIDDEN_TERMS` array at the top of the file. Save and register the hook.

**Enforce folder structure:**
Edit `output-path-validator.js` — add your routing rules to the `ROUTING_RULES` array. Map file patterns to allowed or blocked paths. Save and register the hook.

Both hooks have inline comments explaining every configurable option.

## Installation

```bash
cp quality/hooks/forbidden-terms-guard.js your-project/.claude/hooks/
cp quality/hooks/output-path-validator.js your-project/.claude/hooks/
```

Register in `.claude/settings.json`:
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          { "type": "command", "command": "node .claude/hooks/forbidden-terms-guard.js" },
          { "type": "command", "command": "node .claude/hooks/output-path-validator.js" }
        ]
      },
      {
        "matcher": "Edit",
        "hooks": [
          { "type": "command", "command": "node .claude/hooks/forbidden-terms-guard.js" }
        ]
      }
    ]
  }
}
```

After registering, the hooks run automatically on every `Write` or `Edit` — no manual invocation needed.
