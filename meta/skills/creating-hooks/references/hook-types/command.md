# Command Hook

The most common hook type. Runs a shell command and reads its stdout/stderr.

## Schema

```json
{
  "type": "command",
  "command": "your-shell-command-here",
  "shell": "bash",
  "timeout": 30,
  "statusMessage": "Running validation...",
  "once": false,
  "async": false,
  "asyncRewake": false
}
```

## Fields

| Field | Required | Default | Description |
|-------|----------|---------|-------------|
| `type` | Yes | — | Must be `"command"` |
| `command` | Yes | — | Shell command to execute |
| `shell` | No | `"bash"` | `"bash"` (uses $SHELL) or `"powershell"` (uses pwsh) |
| `timeout` | No | none | Timeout in seconds. Hook killed after this. |
| `statusMessage` | No | none | Custom spinner message while running |
| `once` | No | `false` | If true, hook runs once then auto-removes itself |
| `async` | No | `false` | If true, runs in background without blocking |
| `asyncRewake` | No | `false` | If true, runs in background and wakes model on exit code 2. Implies async. |

## Input

The command receives JSON via stdin:

```json
{
  "session_id": "abc123",
  "tool_name": "Write",
  "tool_input": { "file_path": "/path/file.txt", "content": "..." },
  "tool_response": { ... }  // PostToolUse only
}
```

Use `jq` to extract fields:

```bash
# Extract file path from Write/Edit
jq -r '.tool_input.file_path // .tool_response.filePath'

# Extract bash command
jq -r '.tool_input.command'

# Safe pattern: extract into variable then use
jq -r '.tool_input.file_path' | { read -r f; prettier --write "$f"; }
```

## Output

Return JSON on stdout to control behavior:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PostToolUse",
    "additionalContext": "Warning: file has lint errors"
  }
}
```

For PreToolUse, can also control permissions:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow",
    "permissionDecisionReason": "File is in allowed directory"
  }
}
```

Or modify tool input before execution:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "updatedInput": { "file_path": "/corrected/path.txt" }
  }
}
```

## Exit Codes

- **0** — Allow/proceed (default)
- **2** — Block/error (PreToolUse blocks tool, Stop blocks generation)
- **Other** — Treated as error, logged, but doesn't block

## Common Patterns

### Format after write
```bash
jq -r '.tool_response.filePath // .tool_input.file_path' | { read -r f; prettier --write "$f"; } 2>/dev/null || true
```

### Log all bash commands
```bash
jq -r '.tool_input.command' >> ~/.claude/bash-log.txt
```

### Guard: block writes to protected paths
```bash
FILE=$(jq -r '.tool_input.file_path // ""')
if echo "$FILE" | grep -qE '^\.(env|secret)'; then
  echo '{"continue": false, "stopReason": "Cannot write to sensitive files"}'
  exit 2
fi
```

### Inject context back to model
```bash
FILE=$(jq -r '.tool_input.file_path // ""')
if echo "$FILE" | grep -qE '\.test\.(ts|js)$'; then
  echo '{"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": "Test file modified. Remember to run the test suite."}}'
fi
```

## Timeout Guard Pattern

Always handle stdin timeout for robustness:

```bash
#!/usr/bin/env bash
# Read stdin with timeout
INPUT=$(timeout 5 cat 2>/dev/null || echo '{}')
# ... process $INPUT
```

Or in Node.js:

```javascript
const chunks = [];
const timer = setTimeout(() => { process.exit(0); }, 5000);
process.stdin.on('data', c => chunks.push(c));
process.stdin.on('end', () => {
  clearTimeout(timer);
  const input = JSON.parse(Buffer.concat(chunks).toString() || '{}');
  // ... process input
});
```
