#!/usr/bin/env node

/**
 * data-marker-audit — PostToolUse hook
 *
 * After any Write or Edit to a Markdown file, reads the saved file, counts
 * configured gap markers, and emits a summary of evidence gaps found.
 * Provides immediate feedback so the author knows what still needs validation.
 *
 * Advisory-only: emits an informational message but does not block.
 *
 * Hook type: PostToolUse
 * Matcher: Write|Edit
 *
 * How to configure in .claude/settings.json:
 * {
 *   "hooks": {
 *     "PostToolUse": [{
 *       "matcher": "Write|Edit",
 *       "hooks": [{
 *         "type": "command",
 *         "command": "node strategy/hooks/data-marker-audit.js"
 *       }]
 *     }]
 *   }
 * }
 *
 * Configuration:
 * Edit the CONFIG object below to add, rename, or remove gap markers.
 * Each entry has a `pattern` (exact string to search) and a `label` used
 * in the summary message.
 */

const fs = require('fs');
const path = require('path');

// ---------------------------------------------------------------------------
// Configuration — edit this block to adapt to your workspace
// ---------------------------------------------------------------------------
const CONFIG = {
  /**
   * Gap markers to detect in written Markdown files.
   * pattern: exact string to count (case-sensitive).
   * label:   human-readable label used in the output summary.
   */
  markers: [
    { pattern: '[DATA NEEDED]',              label: 'data gaps' },
    { pattern: '[NO CUSTOMER VOICE]',        label: 'missing customer voice' },
    { pattern: '[UNVALIDATED ASSUMPTION]',   label: 'unvalidated assumptions' },
    { pattern: '[NO STRUCTURED DISCOVERY]',  label: 'no structured discovery' },
  ],

  /** File name fragments to skip (templates, config files, etc.) */
  skipPatterns: ['TEMPLATE', 'CLAUDE.'],
};
// ---------------------------------------------------------------------------

function countOccurrences(content, pattern) {
  return content.split(pattern).length - 1;
}

function main() {
  let input;
  try {
    input = JSON.parse(fs.readFileSync('/dev/stdin', 'utf8'));
  } catch {
    console.log(JSON.stringify({ decision: 'approve' }));
    return;
  }

  const toolName = input.tool_name || '';
  const filePath = input.tool_input?.file_path || '';

  if (!['Write', 'Edit'].includes(toolName)) {
    console.log(JSON.stringify({ decision: 'approve' }));
    return;
  }

  if (!filePath.endsWith('.md')) {
    console.log(JSON.stringify({ decision: 'approve' }));
    return;
  }

  // Skip templates and config files
  const basename = path.basename(filePath);
  if (CONFIG.skipPatterns.some(p => basename.includes(p))) {
    console.log(JSON.stringify({ decision: 'approve' }));
    return;
  }

  // Read the file that was just written or edited
  let content;
  try {
    content = fs.readFileSync(filePath, 'utf8');
  } catch {
    console.log(JSON.stringify({ decision: 'approve' }));
    return;
  }

  // Count each marker
  const results = CONFIG.markers.map(m => ({
    pattern: m.pattern,
    label: m.label,
    count: countOccurrences(content, m.pattern),
  }));

  const totalGaps = results.reduce((sum, r) => sum + r.count, 0);

  if (totalGaps === 0) {
    console.log(JSON.stringify({ decision: 'approve' }));
    return;
  }

  const nonZero = results.filter(r => r.count > 0);
  const parts = nonZero.map(r => `${r.count}x ${r.label}`);

  // Determine severity: customer voice or unvalidated assumptions are higher priority
  const hasHighPriority = nonZero.some(
    r =>
      r.pattern === '[NO CUSTOMER VOICE]' ||
      r.pattern === '[UNVALIDATED ASSUMPTION]'
  );
  const severityLabel = hasHighPriority ? '[WARN]' : '[INFO]';

  const message = [
    `${severityLabel} data-marker-audit: ${basename} has ${totalGaps} evidence gap(s):`,
    `  ${parts.join(' | ')}`,
  ].join('\n');

  console.log(JSON.stringify({ decision: 'approve', message }));
}

main();
