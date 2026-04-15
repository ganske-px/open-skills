#!/usr/bin/env node

/**
 * evidence-guard — PreToolUse advisory hook
 *
 * Checks initiative documents (PR/FAQ and similar) for missing references to
 * evidence artifacts (research, analysis, feedback) and excessive gap markers.
 * Advisory-only: emits a warning message but does not block the action.
 *
 * Hook type: PreToolUse
 * Matcher: Write|Edit
 *
 * How to configure in .claude/settings.json:
 * {
 *   "hooks": {
 *     "PreToolUse": [{
 *       "matcher": "Write|Edit",
 *       "hooks": [{
 *         "type": "command",
 *         "command": "node discovery/hooks/evidence-guard.js"
 *       }]
 *     }]
 *   }
 * }
 *
 * Configuration:
 * Edit the CONFIG object below to adapt to your workspace layout.
 * - evidencePaths: path fragments that, when present in document content,
 *   indicate a reference to evidence artifacts exists.
 * - maxGapMarkers: how many total gap markers are acceptable before warning.
 * - gapMarkerPatterns: the marker strings to count as evidence gaps.
 * - initiativeDocPatterns: filename patterns that trigger the evidence check.
 */

const fs = require('fs');

// ---------------------------------------------------------------------------
// Configuration — edit this block to adapt to your workspace
// ---------------------------------------------------------------------------
const CONFIG = {
  /** Path fragments whose presence in document content counts as evidence references */
  evidencePaths: ['analysis/', 'research/', 'feedback'],

  /** Maximum acceptable total gap markers before a warning is emitted */
  maxGapMarkers: 5,

  /** Gap marker strings to detect and count */
  gapMarkerPatterns: [
    '[DATA NEEDED]',
    '[NO CUSTOMER VOICE]',
    '[UNVALIDATED ASSUMPTION]',
  ],

  /** Filename substrings that cause evidence checking to trigger */
  initiativeDocPatterns: ['PRFAQ', 'PR-FAQ', 'initiative', 'OST'],

  /** Optional: label for the OST reference hint in warning messages */
  ostHint: 'OST',
};
// ---------------------------------------------------------------------------

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
  const content = input.tool_input?.content || '';

  // Only check Write and Edit operations
  if (!['Write', 'Edit'].includes(toolName)) {
    console.log(JSON.stringify({ decision: 'approve' }));
    return;
  }

  // Only check files whose names match initiative document patterns
  const basename = (filePath.split('/').pop() || '').toUpperCase();
  const isInitiativeDoc = CONFIG.initiativeDocPatterns.some(p =>
    basename.includes(p.toUpperCase())
  );

  if (!isInitiativeDoc) {
    console.log(JSON.stringify({ decision: 'approve' }));
    return;
  }

  if (!content) {
    console.log(JSON.stringify({ decision: 'approve' }));
    return;
  }

  const warnings = [];

  // Check for references to evidence paths
  const hasEvidenceRef = CONFIG.evidencePaths.some(p => content.includes(p));

  if (!hasEvidenceRef) {
    const pathList = CONFIG.evidencePaths.join(', ');
    warnings.push(
      `Document does not reference any evidence artifacts (${pathList}). ` +
        'Consider linking analyses or research in a "Related Documents" section.'
    );
  }

  // Count gap markers
  const markerCounts = CONFIG.gapMarkerPatterns.map(pattern => ({
    pattern,
    count: (content.split(pattern).length - 1),
  }));

  const totalGaps = markerCounts.reduce((sum, m) => sum + m.count, 0);

  if (totalGaps > CONFIG.maxGapMarkers) {
    const breakdown = markerCounts
      .filter(m => m.count > 0)
      .map(m => `${m.count}x ${m.pattern}`)
      .join(', ');
    warnings.push(
      `Document has ${totalGaps} gap markers (${breakdown}). ` +
        'Consider running data-research or customer interviews to fill the most critical gaps before advancing.'
    );
  }

  // Check for OST reference hint
  const hasOSTRef = content.includes(CONFIG.ostHint);

  if (warnings.length === 0) {
    console.log(JSON.stringify({ decision: 'approve' }));
    return;
  }

  const gapSummary = markerCounts
    .map(m => `${m.count} ${m.pattern}`)
    .join(', ');

  const lines = [
    'evidence-guard: Evidence check for initiative document:',
    '',
    ...warnings.map(w => `  * ${w}`),
    '',
    `Summary: ${gapSummary}.`,
  ];

  if (!hasOSTRef) {
    lines.push(
      `  Tip: no ${CONFIG.ostHint} reference found — consider creating an OST if discovery has not been structured yet.`
    );
  }

  const message = lines.filter(Boolean).join('\n');

  console.log(
    JSON.stringify({
      decision: 'approve',
      message,
    })
  );
}

main();
