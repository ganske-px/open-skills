# open-skills

An open collection of battle-tested Claude Code skills, agents, hooks, and scripts — organized by discipline, ready to use.

## What is this?

**open-skills** is a curated library of Claude Code extensions built from real production workflows. Each skill encodes a methodology — a repeatable way to solve a class of problems — so you get consistent, high-quality outputs without reinventing the wheel every session.

Nothing here is tied to any company, product, or domain. These are pure methodology tools: decision frameworks, discovery workflows, research synthesis patterns, storytelling structures, and quality guards. They work for any team building any product.

The repo is organized by **discipline**, so you can install exactly what you need. Want just the discovery toolkit? Copy one folder. Need everything? Copy them all. Each piece is standalone with zero hidden dependencies.

## Disciplines

| Discipline | Description | Skills | Agents | Hooks | Scripts |
|---|---|---|---|---|---|
| [meta](meta/) | Building and auditing skills, hooks, and prompts | 4 | — | 1 | — |
| [decision](decision/) | Structured decision-making (Cynefin, RAPID, Matrix, Pre-Mortem, OODA) | 1 | — | — | — |
| [discovery](discovery/) | Continuous discovery: JTBD, OST, research planning and synthesis | 6 | 2 | 2 | — |
| [strategy](strategy/) | Strategic product work: ideation, PR/FAQ, initiative verification | 2 | 3 | 2 | — |
| [communication](communication/) | Storytelling (SWD), launch docs, TL;DR, text quality | 4 | 2 | 1 | — |
| [analysis](analysis/) | Technical analysis, statistical probability, web research, charts | 3 | 1 | — | 3 |
| [quality](quality/) | Guard hooks for terminology enforcement and file routing | — | — | 2 | — |

Plus 12 [starter commands](commands/) for competitive analysis, feature specs, metrics, roadmaps, and stakeholder comms.

## Installation

```bash
# Install an entire discipline (e.g., discovery)
cp -r discovery/skills/* your-project/.claude/skills/
cp -r discovery/agents/* your-project/.claude/agents/
cp -r discovery/hooks/* your-project/.claude/hooks/

# Install just one skill
cp -r meta/skills/decision-making your-project/.claude/skills/

# Install starter commands
cp commands/*.md your-project/.claude/commands/
```

Each skill, agent, and hook is self-contained. No shared dependencies, no global config, no setup scripts. Copy and use.

## Quick Start

Here are three high-impact skills to try first:

### 1. decision-making

Help you navigate any decision — from daily trade-offs to strategic bets. Type "help me decide between X and Y" and the skill walks you through Cynefin classification, option comparison, and risk stress-testing. Outputs a structured decision record you can share with stakeholders.

```
> help me decide between building a custom auth system and using a third-party provider
```

### 2. discovery-kickoff

Orchestrates a full discovery cycle from a single prompt. Type "start discovery for [topic]" and it coordinates evidence gathering, JTBD extraction, and research planning — producing a structured discovery brief ready for team review.

```
> start discovery for improving onboarding completion rates
```

### 3. prompt-engineering

Build better prompts and agent definitions. Type "create an agent for [task]" to get a structured agent with techniques, frameworks, anti-patterns, and test scenarios. Also works for refining existing prompts.

```
> create an agent for code review that catches security issues
```

## What's Inside Each Discipline

### meta/

Tools for building and auditing the skills themselves. **prompt-engineering** helps you craft effective prompts. **creating-skills** and **creating-hooks** encode best practices for extending Claude Code. **ai-audit** scores and improves CLAUDE.md files and codebase AI-friendliness.

### decision/

A unified **decision-making** skill that detects what kind of decision you're facing (simple, complicated, complex, or chaotic via Cynefin) and applies the right framework: RAPID for organizational decisions, weighted matrices for multi-criteria comparisons, pre-mortems for risk assessment, OODA for fast-moving situations.

### discovery/

The complete continuous discovery toolkit. **discovery-kickoff** orchestrates the full cycle. **jtbd** implements Jobs-to-Be-Done from interview planning through job mapping and opportunity scoring. **research-plan**, **research-interview**, **research-feedback**, and **synthesize-research** handle the entire research workflow from planning through synthesis.

### strategy/

**ideation** runs structured brainstorming with divergent/convergent phases and hidden-face analysis. **product-decision** handles evidence-based product decisions: opportunity prioritization, solution selection, initiative gating, and MVP definition.

### communication/

**storytelling** creates data-driven narratives following Storytelling with Data principles. **launch-docs** generates deploy briefings, FAQs, and release notes. **tldr** produces executive summaries. **spell-checker** enforces grammar, style, and terminology consistency.

### analysis/

**probability-analysis** computes Bayesian inference, confidence intervals, and statistical comparisons. **tech-lead** reviews code architecture and technical decisions. **web-search-researcher** conducts deep web research for benchmarks, competitive intelligence, and market trends.

### quality/

Guard hooks that run automatically to enforce terminology standards, validate evidence citations, and route files to correct locations. Config-driven — edit the rules at the top of each hook file.

### commands/

Twelve starter prompt templates covering common product management workflows: competitive analysis, feature specs, metrics reviews, roadmap updates, stakeholder communications, and more.

## Philosophy

**Built from real work.** Every skill was built to solve an actual problem, tested in production workflows, and refined over months of daily use. Nothing here is theoretical.

**Methodology over implementation.** We ship the thinking framework; you adapt to your context. A decision-making skill doesn't decide for you — it ensures you consider the right dimensions and document your reasoning.

**Standalone by design.** Each skill works independently. Install one or install all. No initialization rituals, no shared state, no dependency chains. Copy a folder and start using it.

**English-first, industry-agnostic.** No company jargon, no domain assumptions. Skills use generic placeholders and let you bring your own context. Works for SaaS, hardware, platforms, agencies — any team that builds products.

## Contributing

PRs welcome. Each contribution should follow these principles:

- **Generic and standalone** — no company-specific references, no external dependencies
- **English** — all content in English
- **Well-documented** — clear trigger descriptions, usage examples, and expected outputs
- **Battle-tested** — built from real workflows, not hypothetical scenarios

Use `meta/skills/creating-skills` to build new skills following best practices, and `meta/skills/ai-audit` to verify quality before submitting.

### Structure

Each skill follows this pattern:

```
discipline/skills/skill-name/
  skill-name.md          # Main skill definition (triggers, instructions, output format)
  references/            # Supporting knowledge the skill needs
    frameworks/          # Decision trees, scoring rubrics, classification systems
    examples/            # Worked examples for few-shot learning
    templates/           # Output templates
```

Agents, hooks, and scripts follow similar conventions within their discipline directories.

## License

MIT — see [LICENSE](LICENSE) for details.
