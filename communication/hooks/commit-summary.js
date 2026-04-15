#!/usr/bin/env node

/**
 * commit-summary — PreToolUse advisory hook
 *
 * Before a `git commit` command, categorizes staged files by directory prefix
 * and emits a human-readable changelog summary as an advisory message.
 * The commit is always approved — this hook never blocks.
 *
 * Hook type: PreToolUse
 * Matcher: Bash(git commit*)
 *
 * Configuration:
 *   Edit CONFIG.categories to map directory prefixes to human-readable labels.
 *   Files that do not match any prefix are counted but not listed separately.
 *
 * @module commit-summary
 */

'use strict';

const fs = require('fs');
const { spawnSync } = require('child_process');

/**
 * @typedef {Object} Config
 * @property {Record<string, string>} categories - Map of path prefix to display label.
 */

/** @type {Config} */
const CONFIG = {
  categories: {
    'docs/': 'Documentation',
    'src/': 'Source Code',
    'tests/': 'Tests',
    '.claude/': 'AI Configuration',
  },
};

/**
 * Reads JSON from stdin and returns the parsed object.
 * Returns null on parse failure.
 *
 * @returns {object|null}
 */
function readInput() {
  try {
    return JSON.parse(fs.readFileSync('/dev/stdin', 'utf8'));
  } catch {
    return null;
  }
}

/**
 * Returns the list of staged file paths via `git diff --cached --name-only`.
 * Uses spawnSync with a fixed argument list — no shell interpolation.
 * Returns an empty array if the command fails.
 *
 * @returns {string[]}
 */
function getStagedFiles() {
  const result = spawnSync('git', ['diff', '--cached', '--name-only'], {
    encoding: 'utf8',
  });
  if (result.status !== 0 || result.error) return [];
  return (result.stdout || '').trim().split('\n').filter(Boolean);
}

/**
 * Categorizes an array of file paths against CONFIG.categories.
 * Returns a map of label to matched file paths, plus an uncategorized count.
 *
 * @param {string[]} files
 * @returns {{ categorized: Record<string, string[]>, uncategorized: number }}
 */
function categorizeFiles(files) {
  const categorized = {};
  let uncategorized = 0;

  for (const file of files) {
    let matched = false;
    for (const [prefix, label] of Object.entries(CONFIG.categories)) {
      if (file.startsWith(prefix)) {
        if (!categorized[label]) categorized[label] = [];
        categorized[label].push(file);
        matched = true;
        break;
      }
    }
    if (!matched) uncategorized++;
  }

  return { categorized, uncategorized };
}

/**
 * Builds the advisory message string from categorized files.
 *
 * @param {string[]} stagedFiles
 * @param {{ categorized: Record<string, string[]>, uncategorized: number }} categorization
 * @returns {string}
 */
function buildMessage(stagedFiles, { categorized, uncategorized }) {
  const total = stagedFiles.length;
  const categorizedCount = total - uncategorized;
  const lines = [];

  for (const [label, files] of Object.entries(categorized)) {
    lines.push(`  ${label} (${files.length}):`);
    for (const f of files) {
      lines.push(`    - ${f}`);
    }
  }

  if (uncategorized > 0) {
    lines.push(`  Other (${uncategorized}): not listed`);
  }

  return [
    `commit-summary: ${total} file(s) staged, ${categorizedCount} categorized:`,
    '',
    ...lines,
  ].join('\n');
}

/**
 * Main entry point.
 */
function main() {
  const input = readInput();

  if (!input) {
    process.stdout.write(JSON.stringify({ decision: 'approve' }));
    return;
  }

  const toolName = input.tool_name || '';
  const command = input.tool_input?.command || '';

  if (toolName !== 'Bash') {
    process.stdout.write(JSON.stringify({ decision: 'approve' }));
    return;
  }

  if (!command.match(/git\s+commit/)) {
    process.stdout.write(JSON.stringify({ decision: 'approve' }));
    return;
  }

  const stagedFiles = getStagedFiles();

  if (stagedFiles.length === 0) {
    process.stdout.write(JSON.stringify({ decision: 'approve' }));
    return;
  }

  const categorization = categorizeFiles(stagedFiles);
  const hasCategorizedFiles = Object.keys(categorization.categorized).length > 0;

  if (!hasCategorizedFiles) {
    process.stdout.write(JSON.stringify({ decision: 'approve' }));
    return;
  }

  const message = buildMessage(stagedFiles, categorization);
  process.stdout.write(JSON.stringify({ decision: 'approve', message }));
}

main();
