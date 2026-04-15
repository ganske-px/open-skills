# Tool Lifecycle Events

Events that fire around tool execution. These are the most commonly used hooks.

## PreToolUse

Fires **before** a tool executes. Can block execution, modify input, or control permissions.

**Matcher:** Tool name regex (e.g., `Write|Edit`, `Bash`, `Read`)
**Hook types:** command, prompt, agent
**Stdin:**
```json
{
  "session_id": "abc123",
  "tool_name": "Write",
  "tool_input": {
    "file_path": "/path/to/file.txt",
    "content": "file content here"
  }
}
```

**Special output fields (command hooks):**
```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow",       // "allow", "deny", or "ask"
    "permissionDecisionReason": "File is safe",
    "updatedInput": { "file_path": "/corrected/path.txt" },
    "additionalContext": "Warning text injected into model context"
  }
}
```

**Exit code 2** blocks the tool from executing.

### Common matchers

| Matcher | Matches |
|---------|---------|
| `Write` | File creation/overwrite |
| `Edit` | File editing (string replacement) |
| `Write\|Edit` | Both write operations |
| `Bash` | Shell command execution |
| `Read` | File reading |
| `Glob` | File pattern matching |
| `Grep` | Content search |
| `Agent` | Subagent spawning |

---

## PostToolUse

Fires **after** a tool executes successfully.

**Matcher:** Tool name regex
**Hook types:** command, prompt, agent
**Stdin:**
```json
{
  "session_id": "abc123",
  "tool_name": "Write",
  "tool_input": {
    "file_path": "/path/to/file.txt",
    "content": "file content here"
  },
  "tool_response": {
    "filePath": "/path/to/file.txt",
    "success": true
  }
}
```

**Key difference from PreToolUse:** includes `tool_response` with the tool's output.

**Common uses:**
- Auto-format after write (`prettier --write`)
- Run tests after code change
- Inject reminders into model context
- Log operations

---

## PostToolUseFailure

Fires **after** a tool fails.

**Matcher:** Tool name regex
**Hook types:** command, prompt, agent
**Stdin:** Same as PostToolUse but `tool_response` contains error information.

**Common uses:**
- Log failures
- Suggest fixes via `additionalContext`

---

## PermissionRequest

Fires when Claude Code would normally show a permission prompt to the user.

**Matcher:** Tool name regex
**Hook types:** command, prompt, agent

**Special output fields:**
```json
{
  "hookSpecificOutput": {
    "hookEventName": "PermissionRequest",
    "permissionDecision": "allow",
    "permissionDecisionReason": "Pre-approved by policy"
  }
}
```

Can auto-approve or auto-deny operations without user interaction.

---

## Tool Input Fields by Tool

| Tool | `tool_input` fields |
|------|-------------------|
| `Write` | `file_path`, `content` |
| `Edit` | `file_path`, `old_string`, `new_string`, `replace_all` |
| `Read` | `file_path`, `offset`, `limit` |
| `Bash` | `command`, `description`, `timeout` |
| `Glob` | `pattern`, `path` |
| `Grep` | `pattern`, `path`, `glob`, `type`, `output_mode` |
| `Agent` | `prompt`, `description`, `subagent_type` |
