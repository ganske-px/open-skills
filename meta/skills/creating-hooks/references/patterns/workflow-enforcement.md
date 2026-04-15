# Workflow Enforcement Patterns

Patterns for using hooks to enforce agent and skill workflows at runtime.

## Problem

Skills and agents define workflows via instructions (SKILL.md, agent definitions), but the model can drift from these instructions. Hooks provide runtime enforcement — they observe actual tool calls and inject corrections or blocks.

## Pattern 1: Skill Step Validation

Ensure a skill's steps are followed in order.

**How:** Track progress in a bridge file. Each PostToolUse hook checks if the expected step happened.

```bash
#!/usr/bin/env bash
# PostToolUse hook: track-skill-steps.sh
INPUT=$(timeout 5 cat 2>/dev/null || echo '{}')
FILE=$(echo "$INPUT" | jq -r '.tool_input.file_path // ""')
SESSION=$(echo "$INPUT" | jq -r '.session_id // "unknown"')
STATE_FILE="/tmp/skill-state-${SESSION}.json"

# Initialize state if missing
[ ! -f "$STATE_FILE" ] && echo '{"step": 0}' > "$STATE_FILE"

CURRENT_STEP=$(jq -r '.step' "$STATE_FILE")

# Example: if writing to /output/ without completing research first
if echo "$FILE" | grep -q '/output/' && [ "$CURRENT_STEP" -lt 1 ]; then
  echo "{\"hookSpecificOutput\": {\"hookEventName\": \"PostToolUse\", \"additionalContext\": \"WARNING: You are writing output without having completed the research step first. The skill workflow requires completing research before writing final output.\"}}"
fi
```

## Pattern 2: Quality Gate

Block a tool call unless prerequisites are met.

```bash
#!/usr/bin/env bash
# PreToolUse hook: quality-gate.sh
INPUT=$(timeout 5 cat 2>/dev/null || echo '{}')
TOOL=$(echo "$INPUT" | jq -r '.tool_name // ""')
FILE=$(echo "$INPUT" | jq -r '.tool_input.file_path // ""')

# Block document creation if required placeholders are present
if echo "$FILE" | grep -qE 'SPEC|spec|RFC|rfc'; then
  CONTENT=$(echo "$INPUT" | jq -r '.tool_input.content // ""')
  if echo "$CONTENT" | grep -q '\[REQUIRED\]'; then
    # Advisory: warn but don't block
    echo "{\"hookSpecificOutput\": {\"hookEventName\": \"PreToolUse\", \"additionalContext\": \"This document contains [REQUIRED] placeholders. Consider filling them before finalizing.\"}}"
  fi
fi
```

## Pattern 3: Agent Workflow Orchestration

When an agent has a defined workflow (skill steps), hooks enforce transitions.

**Architecture:**
```
Agent executes skill
  └── Step 1: Read context files
       └── PostToolUse (Read) → hook records "context loaded"
  └── Step 2: Analyze data
       └── PostToolUse (Bash) → hook records "analysis done"
  └── Step 3: Write output
       └── PreToolUse (Write) → hook checks prerequisites
           ├── Prerequisites met → allow
           └── Prerequisites missing → inject warning
```

## Pattern 4: Cross-Skill Coordination

When multiple skills need to coordinate (e.g., `creating-skills` calls `creating-hooks`):

```bash
#!/usr/bin/env bash
# PostToolUse hook: cross-skill-tracker.sh
INPUT=$(timeout 5 cat 2>/dev/null || echo '{}')
FILE=$(echo "$INPUT" | jq -r '.tool_input.file_path // ""')

# Detect skill file creation
if echo "$FILE" | grep -q '\.claude/skills/.*/SKILL.md'; then
  SKILL_NAME=$(echo "$FILE" | sed 's|.*\.claude/skills/\([^/]*\)/.*|\1|')
  # Remind about hooks integration
  echo "{\"hookSpecificOutput\": {\"hookEventName\": \"PostToolUse\", \"additionalContext\": \"New skill '$SKILL_NAME' created. Consider: does this skill need hooks for runtime enforcement? If yes, use creating-hooks to add them.\"}}"
fi
```

## Pattern 5: Prompt Engineering Guard

When `prompt-engineering` creates agent definitions, ensure they include workflow hooks:

```bash
#!/usr/bin/env bash
INPUT=$(timeout 5 cat 2>/dev/null || echo '{}')
FILE=$(echo "$INPUT" | jq -r '.tool_input.file_path // ""')

# Detect agent definition creation
if echo "$FILE" | grep -q '\.claude/agents/'; then
  CONTENT=$(echo "$INPUT" | jq -r '.tool_input.content // ""')
  if ! echo "$CONTENT" | grep -qi 'hook\|workflow enforcement\|runtime guard'; then
    echo "{\"hookSpecificOutput\": {\"hookEventName\": \"PostToolUse\", \"additionalContext\": \"Agent definition created without mentioning hooks or workflow enforcement. Consider using creating-hooks to add runtime guards that enforce this agent's expected behavior.\"}}"
  fi
fi
```

## Pattern 6: AI Audit Integration

When `ai-audit` runs, it should check hook quality:

**Audit checklist for hooks:**
1. Every hook has a timeout guard
2. No hook suppresses errors without logging
3. Blocking hooks always include stopReason
4. Advisory hooks use additionalContext (not systemMessage)
5. Matchers are specific (not catch-all)
6. Bridge files have TTL checks
7. Settings JSON is valid (jq -e validation)
8. No duplicate hooks for same event+matcher

## Combining Advisory + Blocking

A common pattern is two hooks on the same event — one advisory, one blocking:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "node advisory-check.js",
            "statusMessage": "Checking..."
          },
          {
            "type": "command",
            "command": "node hard-block.js",
            "statusMessage": "Validating..."
          }
        ]
      }
    ]
  }
}
```

The advisory hook injects warnings; the blocking hook only fires on critical violations.
