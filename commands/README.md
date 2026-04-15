# Starter Commands

Starter commands are ready-to-use prompt templates for common product management workflows. Install them as Claude Code slash commands and invoke them by name — each one encodes a structured methodology so you get consistent, high-quality outputs without writing prompts from scratch.

## What Are Starter Commands?

A starter command is a markdown file with YAML frontmatter that Claude Code loads as a slash command. Each file contains:

- **`name`**: The command identifier (how you call it)
- **`description`**: What the command does and when to use it
- **Prompt content**: The methodology, frameworks, and output format the command follows

Commands are designed to be invoked conversationally. Most will ask clarifying questions before generating output, so you can start with a rough idea and refine as you go.

## Installation

Copy the command files into your project's `.claude/commands/` directory:

```bash
# Install all starter commands
cp commands/*.md your-project/.claude/commands/

# Install a single command
cp commands/feature-spec.md your-project/.claude/commands/
```

Once installed, invoke a command in Claude Code by typing `/` followed by the command name, for example:

```
/feature-spec SSO login for enterprise customers
/roadmap-update
/synthesize-research
```

## Commands

### Competitive Intelligence

| Command | Description |
|---|---|
| `competitive-analysis` | Analyze competitors with feature comparison matrices, positioning analysis, and strategic implications. Use when researching a competitor, comparing product capabilities, assessing competitive positioning, or preparing a competitive brief for product strategy. |
| `competitive-brief` | Generate a concise competitive brief for a specific competitor or market context. Use when preparing for a sales call, responding to a competitive threat, or onboarding someone to the competitive landscape. |

### Feature Development

| Command | Description |
|---|---|
| `feature-spec` | Write structured product requirements documents (PRDs) with problem statements, user stories, requirements, and success metrics. Use when speccing a new feature, writing a PRD, defining acceptance criteria, prioritizing requirements, or documenting product decisions. |
| `write-spec` | Write a feature spec or PRD from a problem statement, feature idea, or user request. Use when speccing a new feature, writing a PRD, defining scope and acceptance criteria, or drafting requirements for engineering and design. |

### Metrics

| Command | Description |
|---|---|
| `metrics-review` | Review and interpret product metrics — identify trends, surface anomalies, and generate hypotheses. Use when analyzing a metrics dashboard, investigating a metric change, preparing for a data review, or building a metrics narrative. |
| `metrics-tracking` | Set up or review a metrics tracking plan for a feature or product area. Use when defining what to measure for a new feature, auditing an existing tracking plan, or aligning on metrics with engineering and data teams. |

### Roadmap

| Command | Description |
|---|---|
| `roadmap-management` | Plan and prioritize product roadmaps using frameworks like RICE, MoSCoW, and ICE. Use when creating a roadmap, reprioritizing features, mapping dependencies, choosing between Now/Next/Later or quarterly formats, or presenting roadmap tradeoffs to stakeholders. |
| `roadmap-update` | Update or reprioritize an existing product roadmap — add items, change statuses, shift timelines, or build one from scratch. Use when running a roadmap review, reacting to changed priorities, or preparing a roadmap update for stakeholders. |

### Research

| Command | Description |
|---|---|
| `synthesize-research` | Synthesize user research from interviews, surveys, and feedback into structured insights and recommendations. Use when analyzing interview notes, survey responses, or mixed-method research to identify themes, prioritize findings, and drive product decisions. |
| `user-research-synthesis` | Synthesize qualitative and quantitative user research into structured insights and opportunity areas. Use when analyzing interview notes, survey responses, support tickets, or behavioral data to identify themes, build personas, or prioritize opportunities. |

### Stakeholder Communication

| Command | Description |
|---|---|
| `stakeholder-comms` | Draft stakeholder updates tailored to audience — executives, engineering, customers, or cross-functional partners. Use when writing weekly status updates, monthly reports, launch announcements, risk communications, or decision documentation. |
| `stakeholder-update` | Generate a stakeholder update tailored to audience and cadence — weekly, monthly, launch, or ad-hoc. Use when preparing a regular status update, announcing a launch, communicating a pivot, or drafting an executive summary. |

## Usage Notes

- **Commands are conversational.** Most commands ask follow-up questions. Start with a rough prompt; the command will gather what it needs.
- **Commands reference each other.** For example, `synthesize-research` points to `user-research-synthesis` for deeper methodology, and `stakeholder-update` points to `stakeholder-comms` for audience-specific templates. Installing all 12 commands gives you the full cross-referenced system.
- **Commands work without connected tools.** If your project tracker, knowledge base, or analytics tool is not connected, commands fall back to asking you for the relevant context directly.
- **Commands are starting points, not locked workflows.** If a command's output is not quite right, tell it what to change. Every command supports iterative refinement.
