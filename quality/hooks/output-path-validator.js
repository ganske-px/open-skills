#!/usr/bin/env node

/**
 * Output Path Validator
 *
 * Advisory PostToolUse hook for Write|Edit operations.
 * Validates that files are written to the expected directories based on
 * naming patterns. Warns when a file appears to land in the wrong location.
 *
 * Configuration: Edit the ROUTING_RULES object below with your workspace
 * conventions.
 *
 * Matcher: PostToolUse on Write|Edit
 * Type: Advisory (warns but does not block or undo)
 *
 * Installation: Add to your .claude/settings.json:
 * {
 *   "hooks": {
 *     "PostToolUse": [
 *       {
 *         "matcher": "Write|Edit",
 *         "hooks": [
 *           {
 *             "type": "command",
 *             "command": "node quality/hooks/output-path-validator.js"
 *           }
 *         ]
 *       }
 *     ]
 *   }
 * }
 */

const fs = require('fs');

// ---------------------------------------------------------------------------
// CONFIGURATION
// Edit this object to define your workspace's routing rules.
//
// Format:
//   {
//     pattern: /regex to match the filename or path/i,
//     expectedDir: "expected/directory/fragment/",
//     message: "Human-readable description of the rule",
//   }
//
// `pattern` is matched against the full file path.
// `expectedDir` is the directory fragment that must appear in the path.
// If the pattern matches but expectedDir does NOT appear in the path, a
// warning is emitted.
//
// Examples for a typical product workspace:
// ---------------------------------------------------------------------------
const ROUTING_RULES = [
  // Uncomment and adapt rules for your workspace:
  //
  // {
  //   pattern: /prfaq|pr-faq/i,
  //   expectedDir: "initiatives/",
  //   message: "PR/FAQs belong in initiatives/. Suggested path: initiatives/active/<name>/PRFAQ.md",
  // },
  // {
  //   pattern: /INTERVIEW-/i,
  //   expectedDir: "research/interviews/",
  //   message: "Interview notes belong in research/interviews/.",
  // },
  // {
  //   pattern: /MARKET-/i,
  //   expectedDir: "research/market/",
  //   message: "Market research belongs in research/market/.",
  // },
  // {
  //   pattern: /PLAN-/i,
  //   expectedDir: "research/plans/",
  //   message: "Research plans belong in research/plans/.",
  // },
  // {
  //   pattern: /OST\.md$/i,
  //   expectedDir: "research/discovery/",
  //   message: "Opportunity Solution Trees belong in research/discovery/<slug>/OST.md",
  // },
  // {
  //   pattern: /ANALYSIS-/i,
  //   expectedDir: "analysis/",
  //   message: "Analysis documents belong in analysis/.",
  // },
];

// ---------------------------------------------------------------------------
// File types to check. Add extensions you want validated.
// ---------------------------------------------------------------------------
const CHECKED_EXTENSIONS = ['.md', '.txt'];

// ---------------------------------------------------------------------------
// Main logic — no edits needed below this line
// ---------------------------------------------------------------------------

function main() {
  let input;
  try {
    input = JSON.parse(fs.readFileSync('/dev/stdin', 'utf8'));
  } catch {
    process.exit(0);
  }

  const filePath =
    input.tool_input?.file_path ||
    input.tool_response?.filePath ||
    '';

  if (!filePath) {
    process.exit(0);
  }

  // Only check configured file types
  const hasCheckedExtension = CHECKED_EXTENSIONS.some(ext =>
    filePath.toLowerCase().endsWith(ext)
  );
  if (!hasCheckedExtension) {
    process.exit(0);
  }

  // Skip if no rules are configured
  if (ROUTING_RULES.length === 0) {
    process.exit(0);
  }

  const warnings = [];

  for (const rule of ROUTING_RULES) {
    const pathMatchesPattern = rule.pattern.test(filePath);
    const pathContainsExpectedDir = filePath.toLowerCase().includes(
      rule.expectedDir.toLowerCase()
    );

    if (pathMatchesPattern && !pathContainsExpectedDir) {
      warnings.push(rule.message);
    }
  }

  if (warnings.length === 0) {
    process.exit(0);
  }

  const output = {
    hookSpecificOutput: {
      hookEventName: 'PostToolUse',
      additionalContext: [
        `output-path-validator: ${warnings.length} routing issue(s) for ${filePath}:`,
        '',
        ...warnings.map(w => `  • ${w}`),
        '',
        'These are advisory warnings. Edit ROUTING_RULES in',
        'quality/hooks/output-path-validator.js to configure your workspace conventions.',
      ].join('\n'),
    },
  };

  process.stdout.write(JSON.stringify(output) + '\n');
  process.exit(0);
}

main();
