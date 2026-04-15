# Common Hook Patterns

Production-tested patterns from the Vercel plugin and GSD (get-shit-done).

## 1. Auto-Format After Write

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{
        "type": "command",
        "command": "jq -r '.tool_response.filePath // .tool_input.file_path' | { read -r f; prettier --write \"$f\"; } 2>/dev/null || true"
      }]
    }]
  }
}
```

## 2. Run Tests After Code Change

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{
        "type": "command",
        "command": "jq -r '.tool_input.file_path // .tool_response.filePath' | grep -E '\\.(ts|js)$' && npm test || true"
      }]
    }]
  }
}
```

## 3. Guard Protected Files (PreToolUse)

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{
        "type": "command",
        "command": "jq -r '.tool_input.file_path // \"\"' | grep -qE '\\.(env|secret|key)' && echo '{\"continue\": false, \"stopReason\": \"Cannot modify sensitive files\"}' && exit 2 || true"
      }]
    }]
  }
}
```

## 4. Inject Context (Advisory Pattern)

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{
        "type": "command",
        "command": "jq -r '.tool_input.file_path // \"\"' | grep -qE '\\.test\\.' && echo '{\"hookSpecificOutput\": {\"hookEventName\": \"PostToolUse\", \"additionalContext\": \"Test file modified. Run tests before committing.\"}}' || true"
      }]
    }]
  }
}
```

## 5. Log All Bash Commands

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Bash",
      "hooks": [{
        "type": "command",
        "command": "jq -r '.tool_input.command' >> ~/.claude/bash-log.txt"
      }]
    }]
  }
}
```

## 6. Context Monitor (GSD Pattern)

Monitor context window usage and warn the agent:

```json
{
  "hooks": {
    "PostToolUse": [{
      "hooks": [{
        "type": "command",
        "command": "node /path/to/context-monitor.js",
        "timeout": 10
      }]
    }]
  }
}
```

The script reads context metrics, applies thresholds, and injects WARNING/CRITICAL via `additionalContext`.

## 7. Prompt Injection Guard (GSD Pattern)

Detect prompt injection in file writes:

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{
        "type": "command",
        "command": "node /path/to/prompt-guard.js"
      }]
    }]
  }
}
```

The script checks for patterns like "ignore previous instructions", suspicious Unicode, XML role tags.

## 8. Workflow Guard

Alert when edits happen outside expected workflow:

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{
        "type": "command",
        "command": "node /path/to/workflow-guard.js"
      }]
    }]
  }
}
```

## 9. Async Background Task

Run something in the background without blocking:

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{
        "type": "command",
        "command": "node /path/to/background-task.js",
        "async": true
      }]
    }]
  }
}
```

## 10. One-Time Setup Hook

Run once on first trigger, then auto-remove:

```json
{
  "hooks": {
    "SessionStart": [{
      "hooks": [{
        "type": "command",
        "command": "echo '{\"systemMessage\": \"Welcome! Hooks are active.\"}'",
        "once": true
      }]
    }]
  }
}
```

## Design Principles (from GSD)

1. **Advisory-only by default** — hooks return exit 0, never block unless explicitly designed to
2. **Stdin timeout guard** — always handle missing/slow stdin (3-10s timeout)
3. **Early exit** — check relevance first, skip processing if not relevant
4. **Bridge files** — use `/tmp/` files for inter-hook communication, never direct
5. **Debounce** — suppress repeated warnings (but let severity escalation bypass debounce)
6. **TTL on bridge data** — ignore data older than 60s to avoid acting on stale state
7. **Single responsibility** — one hook, one job
8. **Fail-safe** — errors should not break the workflow; wrap in try/catch or `|| true`
9. **Silent on clean scan** — don't write stdout if there's nothing to report
10. **Respect env vars** — check `CLAUDE_CONFIG_DIR` and other runtime environment variables
