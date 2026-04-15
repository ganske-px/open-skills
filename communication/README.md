# communication/

Skills for turning product work into clear, compelling communication. Covers data-driven storytelling, launch documentation, executive summaries, and text quality enforcement. Designed to close the gap between doing the work and communicating it effectively.

## What's Included

```
communication/
  skills/
    launch-docs/      # Deploy briefings, FAQs, and release notes for feature launches
    spell-checker/    # Grammar, style, and terminology consistency enforcement
    storytelling/     # Data-driven narratives following Storytelling with Data principles
    tldr/             # Executive summaries and TL;DRs from long documents
  agents/
    (see note below)
  hooks/
    commit-summary.js # Auto-generates a plain-language summary of each git commit
```

**4 skills, 1 hook.**

Note: The `agents/` directory is present for future additions. The `storytelling` and `launch-docs` skills are the primary workhorses here — no autonomous agents are required because these workflows benefit from human-in-the-loop iteration.

## Skills

### storytelling
Creates data-driven narratives following the Storytelling with Data (SWD) methodology:
- **Context**: Who is the audience? What decision does this narrative support?
- **Conflict**: What is the tension or insight the data reveals?
- **Resolution**: What should the audience believe or do?

Enforces SWD principles: one key message per slide/section, data ink ratio, pre-attentive attributes for emphasis, and the "so what" test for every chart. Works with data you provide — tables, metrics, research summaries — and structures them into a narrative arc.

Pairs with the `html_story_builder.py` script in `analysis/` to generate standalone interactive HTML narratives from the same data.

### launch-docs
Generates the three core launch documents:
- **Deploy briefing**: Technical rundown for the team doing the deploy — what is changing, rollout steps, rollback plan, monitoring checkpoints, and on-call contacts.
- **Release notes**: Customer-facing changelog entry — what is new, who benefits, how to get started. No jargon.
- **Launch FAQ**: Internal Q&A covering anticipated questions from support, sales, and leadership — "what does this do?", "who gets it?", "what are the limitations?", "what do I tell customers who ask about X?"

### spell-checker
Enforces grammar, style, and terminology consistency across any written output:
- Catches grammatical errors and awkward phrasing
- Flags passive voice, jargon, and overly complex sentences
- Enforces a configurable terminology list (words to avoid, preferred alternatives)
- Checks for consistency: same term used different ways across a document
- Does not impose a house style — adapts to the document's existing tone

### tldr
Produces executive summaries and TL;DRs from long documents:
- Extracts the 3-5 most important points
- Identifies decisions made, decisions needed, and action items
- Formats for the target audience (executive, engineering, customer)
- Optionally produces a one-sentence headline and a structured bullets version

## Hook

### commit-summary.js
Runs as a post-commit hook. After each git commit, generates a plain-language summary of what changed and why — suitable for pasting into a standup, slack update, or changelog. Reads the commit diff and message, and produces a 2-3 sentence human-readable summary. Configurable: set the audience (technical or non-technical) and length.

## Dependency Graph

```
storytelling ──→ tldr (for narrative summaries)
     ↓
launch-docs (uses storytelling structure for release notes)
     ↓
spell-checker (quality pass on all output)
     ↓
commit-summary.js (passive, post-commit)
```

A typical launch communication workflow:
```
strategy/prfaq-writer → launch-docs → spell-checker → tldr (for exec summary)
```

## Quick Start

**Create a data-driven story for a metrics review:**
```
> create a story about our Q1 retention data — we saw a 12% improvement in week-4 retention after the onboarding redesign
```
`storytelling` structures the narrative with context, insight, and recommendation. Optionally generates an interactive HTML version via `html_story_builder.py`.

**Write launch documents for a feature:**
```
> write a deploy briefing, release notes, and launch FAQ for our new bulk export feature launching next Tuesday
```
`launch-docs` produces all three documents tailored to their respective audiences.

**Summarize a long research document:**
```
> write a TL;DR of this 12-page research synthesis for our VP — she has 5 minutes
```
`tldr` extracts the key points and formats them for executive consumption.

**Check a draft for quality:**
```
> proofread this stakeholder update and flag any jargon, inconsistencies, or awkward phrasing
```
`spell-checker` reviews the text and produces a marked-up version with specific suggestions.

## Installation

```bash
cp -r communication/skills/* your-project/.claude/skills/
cp communication/hooks/commit-summary.js your-project/.claude/hooks/
```

Register the hook in `.claude/settings.json`:
```json
{
  "hooks": {
    "PostToolUse": [
      { "matcher": "Bash", "hooks": [{ "type": "command", "command": "node .claude/hooks/commit-summary.js" }] }
    ]
  }
}
```
