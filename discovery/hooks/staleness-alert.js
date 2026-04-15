#!/usr/bin/env node

/**
 * staleness-alert — PreToolUse advisory hook (fires once per session)
 *
 * On the first invocation of the session, scans a configurable directory for
 * stale items (sub-directories whose newest file has not been modified within
 * the configured thresholds). Emits a summary message but does not block.
 *
 * Uses a session-scoped flag file (/tmp) to ensure it fires only once per
 * Claude Code session.
 *
 * Hook type: PreToolUse
 * Matcher: Read|Glob|Grep  (fires on the first read-type action of the session)
 *
 * How to configure in .claude/settings.json:
 * {
 *   "hooks": {
 *     "PreToolUse": [{
 *       "matcher": "Read|Glob|Grep",
 *       "hooks": [{
 *         "type": "command",
 *         "command": "node discovery/hooks/staleness-alert.js"
 *       }]
 *     }]
 *   }
 * }
 *
 * Configuration:
 * Edit the CONFIG object below to adapt to your workspace layout.
 * - watchPath: directory (relative to cwd) whose sub-directories are scanned.
 * - yellowDays: days without update before a yellow (warning) flag is raised.
 * - redDays: days without update before a red (critical) flag is raised.
 */

const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

// ---------------------------------------------------------------------------
// Configuration — edit this block to adapt to your workspace
// ---------------------------------------------------------------------------
const CONFIG = {
  /** Directory to scan for stale items (relative to process.cwd()) */
  watchPath: 'initiatives/',

  /** Days without modification before a yellow warning is raised */
  yellowDays: 14,

  /** Days without modification before a red critical flag is raised */
  redDays: 30,
};
// ---------------------------------------------------------------------------

function getSessionFlag() {
  const sessionId =
    process.env.SESSION_ID || process.env.CLAUDE_SESSION_ID || 'default';
  const hash = crypto
    .createHash('sha256')
    .update(sessionId)
    .digest('hex')
    .slice(0, 12);
  return `/tmp/claude-staleness-${hash}.flag`;
}

function main() {
  // Consume stdin (required by hook protocol; content is not used)
  try {
    fs.readFileSync('/dev/stdin', 'utf8');
  } catch {
    // ignore
  }

  // Only fire once per session
  const flagFile = getSessionFlag();
  if (fs.existsSync(flagFile)) {
    console.log(JSON.stringify({ decision: 'approve' }));
    return;
  }

  // Write session flag before doing any work
  try {
    fs.writeFileSync(flagFile, Date.now().toString());
  } catch {
    // If we cannot write the flag, proceed anyway (best-effort once-per-session)
  }

  // Resolve watch directory
  const watchDir = path.join(process.cwd(), CONFIG.watchPath);
  if (!fs.existsSync(watchDir)) {
    console.log(JSON.stringify({ decision: 'approve' }));
    return;
  }

  const now = Date.now();
  const DAY_MS = 86400000;

  const staleItems = [];

  try {
    const entries = fs.readdirSync(watchDir, { withFileTypes: true });

    for (const entry of entries) {
      if (!entry.isDirectory()) continue;

      const itemDir = path.join(watchDir, entry.name);
      let newestMtime = 0;

      // Find the newest file modification time within the item folder
      try {
        const files = fs.readdirSync(itemDir);
        for (const file of files) {
          try {
            const stat = fs.statSync(path.join(itemDir, file));
            if (stat.mtimeMs > newestMtime) {
              newestMtime = stat.mtimeMs;
            }
          } catch {
            // ignore individual file errors
          }
        }
      } catch {
        continue;
      }

      if (newestMtime === 0) continue;

      const daysAgo = Math.floor((now - newestMtime) / DAY_MS);

      if (daysAgo >= CONFIG.yellowDays) {
        staleItems.push({
          name: entry.name,
          daysAgo,
          critical: daysAgo >= CONFIG.redDays,
        });
      }
    }
  } catch {
    console.log(JSON.stringify({ decision: 'approve' }));
    return;
  }

  if (staleItems.length === 0) {
    console.log(JSON.stringify({ decision: 'approve' }));
    return;
  }

  // Sort by staleness (most stale first)
  staleItems.sort((a, b) => b.daysAgo - a.daysAgo);

  const criticalCount = staleItems.filter(i => i.critical).length;

  const lines = staleItems.map(i => {
    const level = i.critical ? '[RED]' : '[YELLOW]';
    return `  ${level} ${i.name} — ${i.daysAgo} days without update`;
  });

  const summaryLines = [
    `staleness-alert: ${staleItems.length} item(s) in "${CONFIG.watchPath}" need attention:`,
    '',
    ...lines,
    '',
  ];

  if (criticalCount > 0) {
    summaryLines.push(
      `  ${criticalCount} item(s) over ${CONFIG.redDays} days — consider closing or resuming them.`
    );
  }

  summaryLines.push(
    `  Items between ${CONFIG.yellowDays} and ${CONFIG.redDays} days may just need a check-in.`
  );

  const message = summaryLines.filter(Boolean).join('\n');

  console.log(JSON.stringify({ decision: 'approve', message }));
}

main();
