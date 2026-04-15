#!/usr/bin/env node

/**
 * workflow-guard — PreToolUse advisory hook
 *
 * Detects writes to the initiative directory when prior discovery evidence
 * (research, analysis, feedback) appears to be missing. Warns the user but
 * does not block the action.
 *
 * Advisory-only: emits a warning message but does not block.
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
 *         "command": "node strategy/hooks/workflow-guard.js"
 *       }]
 *     }]
 *   }
 * }
 *
 * Configuration:
 * Edit the CONFIG object below to adapt to your workspace layout.
 * - initiativePath: directory (relative to cwd) where initiatives live.
 *   A write to a NEW sub-directory inside this path triggers the check.
 * - requiredEvidence: list of directories (relative to cwd) that should
 *   contain at least one file to count as evidence being present.
 */

const fs = require('fs');
const path = require('path');

// ---------------------------------------------------------------------------
// Configuration — edit this block to adapt to your workspace
// ---------------------------------------------------------------------------
const CONFIG = {
  /** Directory where initiatives live (relative to process.cwd()) */
  initiativePath: 'initiatives/',

  /**
   * Evidence directories to check (relative to process.cwd()).
   * At least one must be non-empty for the guard to be satisfied.
   */
  requiredEvidence: ['research/', 'analysis/', 'feedback'],
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

  // Only check Write and Edit operations
  if (!['Write', 'Edit'].includes(toolName)) {
    console.log(JSON.stringify({ decision: 'approve' }));
    return;
  }

  // Normalize the initiative path for comparison (strip leading slash if any)
  const normInitPath = CONFIG.initiativePath.replace(/^\//, '');

  // Only check writes that target the initiative directory
  if (!filePath.includes(normInitPath)) {
    console.log(JSON.stringify({ decision: 'approve' }));
    return;
  }

  // Extract the initiative name (the first path segment inside initiativePath)
  const escapedPath = normInitPath.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const match = filePath.match(new RegExp(`${escapedPath}([^/]+)`));
  if (!match) {
    console.log(JSON.stringify({ decision: 'approve' }));
    return;
  }

  const initiativeName = match[1];
  const initiativeDir = path.join(process.cwd(), normInitPath, initiativeName);

  // Only warn when creating a brand-new initiative (directory does not exist yet)
  if (fs.existsSync(initiativeDir)) {
    console.log(JSON.stringify({ decision: 'approve' }));
    return;
  }

  // Check each required evidence directory
  const missingEvidence = [];

  for (const evidencePath of CONFIG.requiredEvidence) {
    const dir = path.join(process.cwd(), evidencePath);
    let hasContent = false;

    if (fs.existsSync(dir)) {
      try {
        const entries = fs.readdirSync(dir).filter(f => !f.startsWith('.'));
        hasContent = entries.length > 0;
      } catch {
        // ignore
      }
    }

    if (!hasContent) {
      missingEvidence.push(evidencePath);
    }
  }

  if (missingEvidence.length === 0) {
    // All evidence directories have content — no warning needed
    console.log(JSON.stringify({ decision: 'approve' }));
    return;
  }

  const warnings = missingEvidence.map(p =>
    `"${p}" is empty or does not exist — no evidence found there.`
  );

  const message = [
    `workflow-guard: New initiative "${initiativeName}" is being created without complete discovery evidence:`,
    '',
    ...warnings.map(w => `  * ${w}`),
    '',
    'This is not a blocker — but initiatives without prior discovery tend to accumulate more [DATA NEEDED] and [NO CUSTOMER VOICE] markers.',
    'If you have already done discovery in another tool, you can safely ignore this warning.',
  ].join('\n');

  console.log(
    JSON.stringify({
      decision: 'approve',
      message,
    })
  );
}

main();
