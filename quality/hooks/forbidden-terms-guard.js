#!/usr/bin/env node

/**
 * Forbidden Terms Guard
 *
 * Advisory PreToolUse hook for Write|Edit operations.
 * Scans .md file writes for forbidden terms and suggests correct replacements.
 *
 * Configuration: Edit the FORBIDDEN_TERMS object below with your domain terminology.
 *
 * Matcher: PreToolUse on Write|Edit
 * Type: Advisory (warns but does not block)
 *
 * Installation: Add to your .claude/settings.json:
 * {
 *   "hooks": {
 *     "PreToolUse": [
 *       {
 *         "matcher": "Write|Edit",
 *         "hooks": [
 *           {
 *             "type": "command",
 *             "command": "node quality/hooks/forbidden-terms-guard.js"
 *           }
 *         ]
 *       }
 *     ]
 *   }
 * }
 */

const fs = require('fs');
const path = require('path');

// ---------------------------------------------------------------------------
// CONFIGURATION
// Edit this object to define your domain's forbidden terms and replacements.
//
// Format: "wrong term": "correct term"
//
// The key is a regex pattern (case-insensitive). The value is the preferred
// replacement. A brief reason is shown in the warning message.
//
// Examples by domain:
//   SaaS product:     "users": "customers"
//   Healthcare:       "patients": "members"
//   Legal:            "contract": "agreement"
//   Marketplace:      "buyer": "customer", "seller": "vendor"
//   Internal tooling: "ticket": "issue"
// ---------------------------------------------------------------------------
const FORBIDDEN_TERMS = {
  // Add your forbidden terms here:
  // "wrong term": { replacement: "correct term", reason: "why this matters" },
  //
  // Example (uncomment and adapt):
  // "client": { replacement: "customer", reason: "Align with company glossary" },
  // "bug": { replacement: "issue", reason: "Neutral language preferred in external docs" },
};

// ---------------------------------------------------------------------------
// Files to skip (by basename). Add filenames that define or discuss terms
// and should not be checked against themselves.
// ---------------------------------------------------------------------------
const SKIP_FILES = [
  'GLOSSARY.md',
  'glossary.md',
  'TERMS.md',
  'terms.md',
  'CLAUDE.md',
  'CLAUDE.local.md',
];

// ---------------------------------------------------------------------------
// Main logic — no edits needed below this line
// ---------------------------------------------------------------------------

function buildPattern(term) {
  // Escape special regex characters in the term
  const escaped = term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  return new RegExp(`\\b${escaped}\\b`, 'gi');
}

function main() {
  let input;
  try {
    input = JSON.parse(fs.readFileSync('/dev/stdin', 'utf8'));
  } catch {
    process.stdout.write(JSON.stringify({ decision: 'approve' }) + '\n');
    return;
  }

  const toolName = input.tool_name || '';
  const filePath = input.tool_input?.file_path || '';

  if (!['Write', 'Edit'].includes(toolName)) {
    process.stdout.write(JSON.stringify({ decision: 'approve' }) + '\n');
    return;
  }

  // Only check markdown files
  if (!filePath.endsWith('.md')) {
    process.stdout.write(JSON.stringify({ decision: 'approve' }) + '\n');
    return;
  }

  // Skip designated files
  const basename = path.basename(filePath);
  if (SKIP_FILES.includes(basename)) {
    process.stdout.write(JSON.stringify({ decision: 'approve' }) + '\n');
    return;
  }

  // Get the content being written
  const content = input.tool_input?.content || input.tool_input?.new_string || '';
  if (!content) {
    process.stdout.write(JSON.stringify({ decision: 'approve' }) + '\n');
    return;
  }

  // Skip if no terms are configured
  if (Object.keys(FORBIDDEN_TERMS).length === 0) {
    process.stdout.write(JSON.stringify({ decision: 'approve' }) + '\n');
    return;
  }

  const warnings = [];

  for (const [term, config] of Object.entries(FORBIDDEN_TERMS)) {
    const pattern = buildPattern(term);
    const matches = content.match(pattern);
    if (matches) {
      const replacement = typeof config === 'string' ? config : config.replacement;
      const reason = typeof config === 'string' ? '' : (config.reason || '');
      const detail = reason ? ` (${reason})` : '';
      warnings.push(`"${matches[0]}" → use "${replacement}"${detail}`);
    }
  }

  if (warnings.length === 0) {
    process.stdout.write(JSON.stringify({ decision: 'approve' }) + '\n');
    return;
  }

  const message = [
    `forbidden-terms-guard: ${warnings.length} terminology issue(s) detected in ${basename}:`,
    '',
    ...warnings.map(w => `  • ${w}`),
    '',
    'These are advisory warnings — the write will proceed. Edit FORBIDDEN_TERMS in',
    'quality/hooks/forbidden-terms-guard.js to configure your domain glossary.',
  ].join('\n');

  process.stdout.write(JSON.stringify({ decision: 'approve', message }) + '\n');
}

main();
