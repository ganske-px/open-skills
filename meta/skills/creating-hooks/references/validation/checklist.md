# Hook Validation Checklist

Follow this checklist after creating any hook. Each step catches a different failure class.

## Step 1: Dedup Check

Before writing, check if a hook already exists for the same event+matcher:

```bash
# Read target settings file
cat .claude/settings.json | jq '.hooks'
```

If a hook exists on the same event+matcher, ask the user: keep, replace, or add alongside.

## Step 2: JSON Syntax Validation

After writing, validate the JSON is valid and the hook is correctly nested:

```bash
# Validate syntax + extract your hook's command
jq -e '.hooks.PostToolUse[] | select(.matcher == "Write|Edit") | .hooks[] | select(.type == "command") | .command' .claude/settings.json
```

- Exit 0 + prints command = correct
- Exit 4 = matcher doesn't match anything
- Exit 5 = malformed JSON or wrong nesting
- **A broken settings.json silently disables ALL settings from that file**

## Step 3: Pipe-Test the Command

Synthesize the stdin payload and pipe it directly:

### For PreToolUse/PostToolUse on Write|Edit:
```bash
echo '{"session_id":"test","tool_name":"Edit","tool_input":{"file_path":"/path/to/real/file.txt"}}' | <your-command>
```

### For PreToolUse/PostToolUse on Bash:
```bash
echo '{"session_id":"test","tool_name":"Bash","tool_input":{"command":"ls"}}' | <your-command>
```

### For Stop/UserPromptSubmit/SessionStart:
```bash
echo '{"session_id":"test"}' | <your-command>
```

**Check:**
- Exit code (0 for advisory, 2 for blocking)
- Side effect happened (file formatted, test ran, log written)
- stdout is valid JSON (if returning control output)

## Step 4: Prove the Hook Fires

Only for tool-based events that can be triggered in the current session:

### For formatter hooks (PostToolUse + Write|Edit):
1. Introduce a detectable violation via Edit (bad indentation, missing semicolon)
2. Re-read the file
3. Confirm the hook fixed it

### For any other hook:
1. Temporarily prefix the command: `echo "$(date) hook fired" >> /tmp/claude-hook-check.txt; <original-command>`
2. Trigger the matching tool (Edit for Write|Edit, harmless `true` for Bash)
3. Read the sentinel file: `cat /tmp/claude-hook-check.txt`
4. **Clean up:** revert the prefix and delete the sentinel file

### If proof fails but pipe-test and jq passed:
The settings watcher may not be watching `.claude/`. Tell the user to:
- Open `/hooks` in the Claude Code UI (reloads config)
- Or restart the session

## Step 5: Edge Cases

After basic validation, test edge cases:

| Test | How | Expected |
|------|-----|----------|
| Empty stdin | `echo '' \| <command>` | Exit 0, no crash |
| Missing field | `echo '{}' \| <command>` | Exit 0, no crash |
| Non-matching file | Use a file the hook shouldn't match | Hook should skip silently |
| Timeout | If hook has timeout, ensure it completes within limit | No hanging |
| Concurrent execution | Two rapid tool calls | No race conditions with bridge files |

## Common Failures

| Symptom | Cause | Fix |
|---------|-------|-----|
| Hook never fires | Invalid JSON in settings file | Run jq validation |
| Hook fires but no effect | Command fails silently | Remove `\|\| true`, test raw command |
| Hook fires on wrong tools | Matcher too broad | Narrow the regex |
| Hook blocks unexpectedly | Missing `\|\| true` in advisory hook | Add error suppression |
| Hook hangs | No timeout + stdin waiting | Add timeout guard |
| Hook fires once then stops | `"once": true` set | Remove if not intended |
| Hook fires but context not injected | Wrong `hookEventName` in output | Match to actual event name |
| Settings completely broken | Invalid JSON in settings file | Validate with `jq .` |

## Quick Validation One-Liner

Validate all hooks in a settings file at once:

```bash
jq -e '.hooks | to_entries[] | .key as $event | .value[] | .hooks[] | {event: $event, type: .type, command: (.command // .prompt // .url)}' .claude/settings.json
```

This extracts every hook's event, type, and command/prompt/url. If it fails, the JSON structure is broken.
