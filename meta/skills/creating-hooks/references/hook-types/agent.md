# Agent Hook

Runs a mini-agent with access to tools to verify conditions. More powerful than prompt hooks — the agent can read files, run commands, and reason about results.

## Schema

```json
{
  "type": "agent",
  "prompt": "Verify that unit tests pass for the modified file. $ARGUMENTS",
  "timeout": 60,
  "model": "claude-sonnet-4-5",
  "statusMessage": "Running verification agent...",
  "once": false
}
```

## Fields

| Field | Required | Default | Description |
|-------|----------|---------|-------------|
| `type` | Yes | — | Must be `"agent"` |
| `prompt` | Yes | — | Agent instructions. `$ARGUMENTS` is replaced with hook input JSON. |
| `timeout` | No | 60s | Timeout in seconds |
| `model` | No | Haiku | Model to use. Defaults to fast/cheap model. |
| `statusMessage` | No | none | Custom spinner message |
| `once` | No | `false` | If true, runs once then auto-removes |

## Availability

**Only works on tool events:**
- `PreToolUse`
- `PostToolUse`
- `PermissionRequest`

## How It Works

1. Claude Code spawns a mini-agent with the given prompt
2. The agent has access to tools (Read, Bash, Grep, etc.)
3. The agent investigates and makes a decision
4. The agent's conclusion controls whether the tool proceeds

## Use Cases

### Post-write test runner
```json
{
  "type": "agent",
  "prompt": "A file was just written. $ARGUMENTS. Check if there are related test files. If found, run the tests and report results. If tests fail, explain what broke.",
  "timeout": 120,
  "model": "claude-sonnet-4-5",
  "statusMessage": "Running tests..."
}
```

### Security audit
```json
{
  "type": "agent",
  "prompt": "Audit this code change for security issues. $ARGUMENTS. Check for: hardcoded secrets, SQL injection, XSS, command injection. Read the file and analyze.",
  "timeout": 90
}
```

## When to Use Agent vs Prompt vs Command

| Scenario | Use |
|----------|-----|
| Need to read/write files during check | `agent` |
| Need to run shell commands during check | `agent` |
| Multi-step reasoning with tool access | `agent` |
| Simple yes/no evaluation | `prompt` |
| Deterministic check | `command` |

## Cost Consideration

Agent hooks are the most expensive type — they spin up a full agent with tools. Use only when the verification truly requires multi-step tool access. Most workflow enforcement is better served by `command` hooks.
