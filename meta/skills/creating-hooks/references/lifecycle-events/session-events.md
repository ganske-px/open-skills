# Session Lifecycle Events

Events tied to session lifecycle — start, end, stop, compact, prompt submit.

## SessionStart

Fires when a new session begins.

**Matcher:** None
**Hook types:** command only
**Stdin:** `{ "session_id": "abc123" }`

**Common uses:**
- Check for updates
- Initialize session state
- Set environment variables
- Inject baseline context

---

## SessionEnd

Fires when a session ends.

**Matcher:** None
**Hook types:** command only
**Stdin:** `{ "session_id": "abc123" }`

**Common uses:**
- Clean up temp files
- Save session metrics
- Flush audit logs

---

## Stop

Fires when Claude stops generating (including on clear, resume, compact).

**Matcher:** None
**Hook types:** command only

**Output:**
```json
{
  "systemMessage": "Session complete! Remember to commit.",
  "decision": "block"  // optional — prevents stop
}
```

**Common uses:**
- Display summary to user
- Remind about uncommitted changes
- Block stop if work is incomplete

---

## UserPromptSubmit

Fires when the user submits a prompt.

**Matcher:** None
**Hook types:** command only
**Stdin:** `{ "session_id": "abc123" }`

**Common uses:**
- Inject context based on prompt analysis
- Log user prompts
- Trigger workflow routing

---

## PreCompact

Fires before context compaction.

**Matcher:** `"manual"` or `"auto"`
**Hook types:** command only

**Common uses:**
- Save important context before compaction
- Warn about context loss

---

## PostCompact

Fires after context compaction.

**Matcher:** `"manual"` or `"auto"`
**Hook types:** command only
**Stdin:** Includes compaction summary.

**Common uses:**
- Inject critical context back after compaction
- Log what was compacted

---

## SubagentStart

Fires when a subagent is spawned.

**Matcher:** None (matches all subagents)
**Hook types:** command only

**Common uses:**
- Inject bootstrap context into subagents
- Track subagent spawning

---

## SubagentStop

Fires when a subagent completes.

**Matcher:** None
**Hook types:** command only

**Common uses:**
- Sync state from subagent back to parent
- Log subagent results

---

## Other Events

| Event | When | Matcher | Notes |
|-------|------|---------|-------|
| `Notification` | On notifications | Notification type | command only |
| `InstructionsLoaded` | When CLAUDE.md loaded | None | command only |
| `ConfigChange` | When settings change | None | command only |
| `WorktreeCreate` | When worktree created | None | command only |
| `WorktreeRemove` | When worktree removed | None | command only |
| `StopFailure` | When stop fails | None | command only |
| `Setup` | Initial setup | None | command only |
| `TeammateIdle` | Teammate goes idle | None | command only |
| `TaskCompleted` | Task finishes | None | command only |
| `Elicitation` | Elicitation event | None | command only |
| `ElicitationResult` | Elicitation response | None | command only |
