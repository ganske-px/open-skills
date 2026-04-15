# Prompt Hook

Uses an LLM to evaluate a condition. The LLM decides whether to allow, block, or modify behavior.

## Schema

```json
{
  "type": "prompt",
  "prompt": "Is this code change safe? Context: $ARGUMENTS",
  "timeout": 60,
  "model": "claude-sonnet-4-5",
  "statusMessage": "Evaluating safety...",
  "once": false
}
```

## Fields

| Field | Required | Default | Description |
|-------|----------|---------|-------------|
| `type` | Yes | — | Must be `"prompt"` |
| `prompt` | Yes | — | Prompt text. `$ARGUMENTS` is replaced with hook input JSON. |
| `timeout` | No | 60s | Timeout in seconds |
| `model` | No | default small/fast model | Model to use (e.g., `"claude-sonnet-4-5"`) |
| `statusMessage` | No | none | Custom spinner message |
| `once` | No | `false` | If true, runs once then auto-removes |

## Availability

**Only works on tool events:**
- `PreToolUse`
- `PostToolUse`
- `PermissionRequest`

Does NOT work on: SessionStart, Stop, UserPromptSubmit, etc.

## How It Works

1. Claude Code replaces `$ARGUMENTS` with the hook's stdin JSON
2. The prompt is sent to the specified model (or default small model)
3. The model's response is parsed for a decision
4. The decision controls whether the tool proceeds

## Use Cases

### Code review guard
```json
{
  "type": "prompt",
  "prompt": "Review this code change for security vulnerabilities. The tool is $ARGUMENTS. If you find issues, respond with a warning. If safe, respond with approval.",
  "model": "claude-sonnet-4-5"
}
```

### Style enforcement
```json
{
  "type": "prompt",
  "prompt": "Does this file follow our coding standards? $ARGUMENTS. Respond with specific violations if any."
}
```

## When to Use Prompt vs Command

| Scenario | Use |
|----------|-----|
| Deterministic check (lint, format, test) | `command` |
| Subjective evaluation (code quality, naming) | `prompt` |
| Pattern matching (regex, file extension) | `command` |
| Natural language analysis (intent, safety) | `prompt` |
| Fast, no-latency check | `command` |
| Complex reasoning needed | `prompt` |

## Cost Consideration

Prompt hooks invoke an LLM on every matching tool call. This adds latency and cost. Use sparingly — prefer `command` hooks for deterministic checks.
