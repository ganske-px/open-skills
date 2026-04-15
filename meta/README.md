# meta/

Tools for building, auditing, and improving the skills themselves. If you want to extend this library — or audit your own Claude Code setup — start here.

## What's Included

```
meta/
  skills/
    ai-audit/           # Score and improve CLAUDE.md files and codebase AI-readiness
    creating-hooks/     # Best practices for writing Claude Code hooks
    creating-skills/    # Best practices for writing Claude Code skills
    prompt-engineering/ # Craft effective prompts and agent definitions
  hooks/
    context-monitor.js  # Monitors context window usage and warns before overflow
```

**4 skills, 1 hook.**

## Skills

### prompt-engineering
Build and refine prompts and agent definitions. Given a task description, generates a structured agent or prompt using proven techniques: role definition, chain-of-thought scaffolding, few-shot examples, output format specification, and anti-pattern avoidance. Also works for improving existing prompts by diagnosing weaknesses and applying targeted improvements.

### creating-skills
Encodes the conventions and best practices for writing new Claude Code skills. Use when building a skill from scratch — it walks you through trigger design, instruction structure, output format, and the references folder layout. Produces a complete skill scaffold ready to populate.

### creating-hooks
Encodes the conventions for writing Claude Code hooks (pre-tool, post-tool, stop). Use when you need to enforce a rule automatically — terminology standards, file routing validation, mandatory sections. Produces a hook with configurable rules at the top, clear error messages, and documentation.

### ai-audit
Scores a CLAUDE.md file or codebase for AI-readiness: clarity of instructions, completeness of context, structural quality, and absence of anti-patterns. Outputs a letter grade with a detailed breakdown and specific improvement recommendations. Useful for reviewing your own setup or contributing to this library.

## Hook

### context-monitor.js
Runs as a post-tool hook to monitor context window token usage. When usage approaches a configurable threshold (default: 80%), it emits a warning so you can compact context or start a new session before hitting the limit. Config at the top of the file.

## Dependency Graph

```
prompt-engineering
    ↓ (used by)
creating-skills ──→ ai-audit
creating-hooks  ──→ ai-audit
```

- **Start with `prompt-engineering`** if you are new to writing prompts or agents.
- **Use `creating-skills` or `creating-hooks`** when scaffolding a new extension.
- **Run `ai-audit`** on the result to verify quality before adding it to the library.
- **`context-monitor.js`** is standalone — install it once, works passively in the background.

## Quick Start

**Build a new agent for code review:**
```
> create an agent for code review that catches security issues and bad patterns
```
The `prompt-engineering` skill will produce a structured agent definition with role, techniques, anti-patterns, and test scenarios.

**Audit your CLAUDE.md:**
```
> audit my CLAUDE.md for AI-readiness
```
The `ai-audit` skill scores your file and gives you specific, prioritized improvements.

**Build a new skill:**
```
> help me create a new skill for generating retrospective reports
```
The `creating-skills` skill walks you through structure, triggers, output format, and the references folder layout.

## Installation

```bash
cp -r meta/skills/* your-project/.claude/skills/
cp meta/hooks/context-monitor.js your-project/.claude/hooks/
```

Register hooks in your `.claude/settings.json`:
```json
{
  "hooks": {
    "PostToolUse": [
      { "matcher": "*", "hooks": [{ "type": "command", "command": "node .claude/hooks/context-monitor.js" }] }
    ]
  }
}
```
