# CLAUDE.md — open-skills

Open collection of reusable Claude Code skills, agents, hooks, and scripts.

## Organization

This repo is organized by **discipline** — each directory is a self-contained collection:

| Discipline | What it covers |
|---|---|
| `meta/` | Building and auditing skills, hooks, and prompts |
| `decision/` | Structured decision-making frameworks |
| `discovery/` | Continuous discovery: JTBD, OST, research synthesis |
| `strategy/` | Ideation, PR/FAQ, initiative verification |
| `communication/` | Storytelling, launch docs, TL;DR, text quality |
| `analysis/` | Technical analysis, probability, web research, charts |
| `quality/` | Guard hooks for terminology and evidence |
| `commands/` | Starter prompt templates |

## Conventions

- All content is in **English**
- No company-specific references — everything is generic and industry-agnostic
- Skills use `{workspace}/` as a placeholder for the user's working directory
- Each skill/agent is standalone — install one or install all
- Hooks are config-driven — customize behavior by editing the config object at the top of each file

## Installation

Copy the discipline folders you want into your project's `.claude/` directory. See `README.md` for details.
