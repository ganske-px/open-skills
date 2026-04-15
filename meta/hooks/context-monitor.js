#!/usr/bin/env node

/**
 * context-monitor — PostToolUse hook
 *
 * Tracks tool call count per session as a proxy for context window consumption.
 * Emits a WARNING when estimated remaining context drops to ≤35%, and a CRITICAL
 * alert at ≤25%. Uses a debounce of 5 tool calls between repeated warnings at the
 * same severity level; severity escalation (WARNING → CRITICAL) bypasses debounce.
 *
 * Session state is persisted to a temp file at:
 *   /tmp/claude-context-monitor-<session_hash>.json
 *
 * INSTALLATION
 * ------------
 * Hook type : PostToolUse
 * Matcher   : .* (all tools)
 *
 * In your .claude/settings.json (or settings.local.json):
 *
 *   "hooks": {
 *     "PostToolUse": [
 *       {
 *         "matcher": ".*",
 *         "hooks": [
 *           {
 *             "type": "command",
 *             "command": "node /path/to/context-monitor.js"
 *           }
 *         ]
 *       }
 *     ]
 *   }
 */

const fs = require('fs');
const crypto = require('crypto');

// Approximate context budget: ~200 tool calls is roughly 80% of a 200k-token window.
// These are heuristic thresholds, not exact measurements.
const TOOL_CALL_BUDGET = 200;
const WARNING_THRESHOLD = 0.35;  // warn when ≤35% context remaining
const CRITICAL_THRESHOLD = 0.25; // critical when ≤25% context remaining
const DEBOUNCE_CALLS = 5;        // minimum tool calls between same-severity warnings

/**
 * Returns the path to the per-session state file.
 * Falls back to 'default' if no session ID env var is set.
 */
function getStateFile() {
  const sessionId = process.env.SESSION_ID || process.env.CLAUDE_SESSION_ID || 'default';
  const hash = crypto.createHash('sha256').update(sessionId).digest('hex').slice(0, 12);
  return `/tmp/claude-context-monitor-${hash}.json`;
}

/**
 * Loads persisted state from disk. Returns a fresh default state on any read error.
 */
function loadState(stateFile) {
  try {
    return JSON.parse(fs.readFileSync(stateFile, 'utf8'));
  } catch {
    return { toolCalls: 0, lastWarnAt: 0, lastSeverity: null };
  }
}

/**
 * Persists state to disk. Silently ignores write failures (e.g. read-only fs).
 */
function saveState(stateFile, state) {
  try {
    fs.writeFileSync(stateFile, JSON.stringify(state));
  } catch {
    // Ignore write failures
  }
}

function main() {
  // Consume stdin (required by the hook protocol) but the payload is not needed here.
  try {
    fs.readFileSync('/dev/stdin', 'utf8');
  } catch {
    // Ignore — stdin may be empty or unavailable in some environments
  }

  const stateFile = getStateFile();
  const state = loadState(stateFile);

  state.toolCalls += 1;

  const remaining = 1 - (state.toolCalls / TOOL_CALL_BUDGET);
  const callsSinceLastWarn = state.toolCalls - state.lastWarnAt;

  // Determine current severity level
  let severity = null;
  if (remaining <= CRITICAL_THRESHOLD) {
    severity = 'CRITICAL';
  } else if (remaining <= WARNING_THRESHOLD) {
    severity = 'WARNING';
  }

  // Emit a message if within a threshold AND either:
  //   (a) the debounce window has elapsed, or
  //   (b) severity has escalated from WARNING to CRITICAL
  const severityEscalated = severity === 'CRITICAL' && state.lastSeverity === 'WARNING';
  const debounceExpired = callsSinceLastWarn >= DEBOUNCE_CALLS;
  const shouldEmit = severity !== null && (debounceExpired || severityEscalated);

  if (shouldEmit) {
    state.lastWarnAt = state.toolCalls;
    state.lastSeverity = severity;

    const pct = Math.round(remaining * 100);
    const used = state.toolCalls;
    const icon = severity === 'CRITICAL' ? '🔴' : '🟡';

    const message = [
      `${icon} context-monitor [${severity}]: ~${pct}% context remaining (${used}/${TOOL_CALL_BUDGET} tool calls used)`,
      '',
      severity === 'CRITICAL'
        ? '  Consider wrapping up this session and continuing in a new one. Save any key state before exiting.'
        : '  Context is getting tight. Focus on essential actions and avoid broad exploratory reads.',
    ].join('\n');

    saveState(stateFile, state);
    console.log(JSON.stringify({ decision: 'approve', message }));
    return;
  }

  saveState(stateFile, state);
  console.log(JSON.stringify({ decision: 'approve' }));
}

main();
