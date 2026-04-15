---
name: creating-hooks
description: Create and configure Claude Code hooks for automated workflow enforcement. Use when asked to "create a hook", "add a hook", "automate on file write", "run X after Y", "guard against Z", "enforce workflow", "add pre-commit check", or "validate tool output". Handles all 4 hook types, lifecycle events, settings.json, stdin/stdout contracts. Do NOT use to create skills — use creating-skills instead. Do NOT use to configure settings.json without hooks — use update-config instead.
---

# Creating Hooks

Hooks are automated commands that run at specific points in Claude Code's lifecycle. They observe, validate, guard, and enforce workflows without manual intervention.

## When to Use This Skill

- User asks to automate something ("when X happens, do Y")
- Creating an agent/skill that needs workflow enforcement
- Adding quality gates (format after write, test after edit, guard against mistakes)
- Called by `creating-skills` when the new skill needs hooks
- Called by `ai-audit` when auditing hook configuration quality
- Called by `prompt-engineering` when designing agent workflows that need runtime enforcement

## Quick Decision Tree

| Need | Hook Type | Lifecycle Event | Read |
|------|-----------|----------------|------|
| Run a shell command on trigger | `command` | varies | `references/hook-types/command.md` |
| LLM evaluates a condition | `prompt` | PreToolUse/PostToolUse/PermissionRequest only | `references/hook-types/prompt.md` |
| Agent with tools verifies something | `agent` | PreToolUse/PostToolUse/PermissionRequest only | `references/hook-types/agent.md` |
| POST to an external URL | `http` | varies | `references/hook-types/http.md` |
| Need to pick the right lifecycle event | — | — | `references/lifecycle-events/` |
| Need input/output contract details | — | — | `references/lifecycle-events/<event>.md` |
| Need patterns and examples | — | — | `references/patterns/` |
| Need to validate a hook works | — | — | `references/validation/checklist.md` |

## Workflow — Creating a Hook

Follow this sequence exactly:

### Phase 1: Requirements

1. **What triggers it?** Map to a lifecycle event (see Event Selection below)
2. **What does it do?** Map to a hook type (command/prompt/agent/http)
3. **Where does it live?** Pick the settings file scope:
   - `~/.claude/settings.json` — global, all projects
   - `.claude/settings.json` — project, shared via git
   - `.claude/settings.local.json` — project, personal (gitignored)
4. **Should it block or advise?** Advisory (exit 0 always) vs blocking (exit 2 or `continue: false`)

### Phase 2: Design

5. **Draft the hook JSON** — use the schema from `references/hook-types/<type>.md`
6. **Draft the command/prompt** — see `references/patterns/` for common patterns
7. **Define the matcher** — tool name regex for tool-based events (e.g., `Write|Edit`, `Bash`)

### Phase 3: Implementation

8. **Read the target settings file** — ALWAYS read before writing
9. **Merge the hook** — never replace existing hooks, always merge into arrays
10. **Validate JSON** — run jq validation (see `references/validation/checklist.md`)

### Phase 4: Verification

11. **Pipe-test the command** — synthesize stdin payload, pipe it, check result
12. **Prove the hook fires** — trigger the matching tool, verify side effect
13. **Clean up** — remove any test artifacts

Full verification protocol: `references/validation/checklist.md`

## Event Selection

| I want to... | Event | Matcher |
|---|---|---|
| Run something before a tool executes | `PreToolUse` | Tool name (`Bash`, `Write`, `Edit`, `Read`, etc.) |
| Run something after a tool succeeds | `PostToolUse` | Tool name |
| Run something after a tool fails | `PostToolUseFailure` | Tool name |
| Control permission decisions | `PermissionRequest` | Tool name |
| React when user submits a prompt | `UserPromptSubmit` | — |
| Run at session start | `SessionStart` | — |
| Run at session end | `SessionEnd` | — |
| Run when Claude stops generating | `Stop` | — |
| Run before context compaction | `PreCompact` | `manual` or `auto` |
| Run after context compaction | `PostCompact` | `manual` or `auto` |
| Run when a subagent starts | `SubagentStart` | — |
| Run when a subagent finishes | `SubagentStop` | — |
| Run when a notification fires | `Notification` | Notification type |
| Run when instructions are loaded | `InstructionsLoaded` | — |
| Run when config changes | `ConfigChange` | — |
| Run when a worktree is created | `WorktreeCreate` | — |
| Run when a worktree is removed | `WorktreeRemove` | — |

Full event details with stdin/stdout contracts: read `references/lifecycle-events/<event>.md`

## Hook JSON Structure

```json
{
  "hooks": {
    "EVENT_NAME": [
      {
        "matcher": "ToolName|OtherTool",
        "hooks": [
          {
            "type": "command",
            "command": "your-command-here",
            "timeout": 60,
            "statusMessage": "Running..."
          }
        ]
      }
    ]
  }
}
```

**Key rules:**
- `matcher` is optional — omit it for events without tool context (SessionStart, Stop, etc.)
- `matcher` is a regex matched against tool names for tool-based events
- Multiple matchers can target the same event — they're separate array entries
- Multiple hooks under one matcher run sequentially
- `timeout` defaults vary by type (command: no default, prompt/agent: 60s)

## Stdin Contract (All Command Hooks)

All command hooks receive JSON via stdin:

```json
{
  "session_id": "abc123",
  "tool_name": "Write",
  "tool_input": {
    "file_path": "/path/to/file.txt",
    "content": "..."
  },
  "tool_response": { ... }  // PostToolUse only
}
```

## Stdout Contract (All Hooks)

Hooks can return JSON to control behavior:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PostToolUse",
    "additionalContext": "Text injected into model context"
  },
  "continue": true,
  "stopReason": "Message if continue=false",
  "systemMessage": "Message shown in UI",
  "suppressOutput": false
}
```

**Critical fields:**
- `additionalContext` — injects text into the model's context (the model "sees" this)
- `continue: false` — blocks execution (PreToolUse) or stops generation (Stop)
- `systemMessage` — shows message to user in the UI
- `suppressOutput` — hides stdout from transcript

## Anti-Patterns

1. **Never block silently** — if `continue: false`, always include `stopReason`
2. **Never replace hooks** — always merge into existing arrays in settings.json
3. **Never skip pipe-testing** — a hook that silently does nothing is worse than no hook
4. **Never hardcode paths** — use `$HOME`, `jq` extraction from stdin, or relative paths
5. **Never assume stdin exists** — always handle empty stdin gracefully (timeout guard)
6. **Never suppress errors in development** — add `|| true` only after pipe-test passes
7. **Never use blocking hooks for slow operations** — use `async: true` or `asyncRewake: true`
8. **Never mix advisory and blocking in one hook** — pick one philosophy per hook

## Integration with Other Skills

### From `creating-skills`
When a new skill needs automated enforcement:
1. Identify which workflow steps need runtime guarantees
2. Create hooks for: pre-validation (PreToolUse), post-validation (PostToolUse), or session guards (SessionStart)
3. Document hooks in the skill's SKILL.md under "## Required Hooks"

### From `ai-audit`
When auditing hook quality:
1. Read all settings files for hook definitions
2. Check each hook against the validation checklist (`references/validation/checklist.md`)
3. Verify stdin/stdout contracts match the event type
4. Check for common anti-patterns (see above)

### From `prompt-engineering`
When designing agent workflows:
1. Identify which agent behaviors need runtime enforcement (not just prompt instructions)
2. Create `prompt` or `agent` type hooks for LLM-evaluated guards
3. Create `command` type hooks for deterministic validation (format, lint, test)
4. Use `additionalContext` to inject workflow state back into the agent's context

## Limitations

- `prompt` and `agent` hook types only work on tool events (PreToolUse, PostToolUse, PermissionRequest)
- `http` hooks require `allowedHttpHookUrls` configuration for security
- Hooks that timeout are treated as "allow/proceed" (fail-safe)
- A broken settings.json silently disables ALL settings from that file
- `statusLine` is a separate top-level field, not inside `hooks`
- Hooks cannot communicate directly — use bridge files in `/tmp/` if needed
