# strategy/

Strategic product work: structured ideation, evidence-based decision-making, PR/FAQ writing, and initiative health checking. Skills in this discipline connect discovery findings to product bets and help you communicate strategy in writing.

## What's Included

```
strategy/
  skills/
    ideation/          # Structured brainstorming with divergent/convergent phases
    product-decision/  # Evidence-based product decisions: prioritization, gating, MVP definition
  agents/
    ideation-agent.md      # Autonomous agent for running ideation sessions
    initiative-checker.md  # Autonomous agent for auditing initiative health
    prfaq-writer.md        # Autonomous agent for drafting PR/FAQ documents
  hooks/
    data-marker-audit.js   # Flags invented data or missing evidence citations in strategy docs
    workflow-guard.js      # Enforces required sections in strategy documents before completion
  templates/
    prfaq-template.md      # Standard PR/FAQ template with required sections and guidance
```

**2 skills, 3 agents, 2 hooks, 1 template.**

## Skills

### ideation
Runs structured brainstorming in two phases:
- **Divergent phase**: Generates a broad range of ideas using multiple lenses (user jobs, analogies, constraints, first principles, edge cases). Suspends judgment — every idea is captured.
- **Convergent phase**: Evaluates ideas on feasibility, impact, and novelty. Applies hidden-face analysis to surface ideas that look weak on the surface but have hidden strategic value.
- **Output**: A scored idea matrix with top candidates, rationale, and recommended next steps for each.

### product-decision
Handles evidence-based product decisions at multiple stages:
- **Opportunity prioritization**: Given a set of opportunities, apply ICE/RICE or a weighted matrix to rank them. Requires evidence — will not score opportunities on assumptions alone.
- **Solution selection**: Given opportunities and proposed solutions, evaluate solution fit against user needs, strategic alignment, and feasibility.
- **Initiative gating**: Given an initiative at a milestone, evaluate whether evidence justifies proceeding, pivoting, or stopping.
- **MVP definition**: Given a solution direction, define the smallest version that tests the core assumption.

## Agents

### ideation-agent.md
Autonomous agent that runs a full ideation session. Given a problem statement or "How Might We" question, it generates 20-30 ideas across multiple lenses, clusters them by theme, evaluates each on a 2x2 (impact vs feasibility), and produces a prioritized idea brief. Deploy when you want high-volume ideation without facilitating manually.

### initiative-checker.md
Audits the health of active initiatives. Given a set of initiative documents (PR/FAQs, specs, or briefs), it checks for: clear problem statement, evidence of customer need, measurable success criteria, owner assignment, and decision history. Produces a health report with a status for each initiative and specific gaps to address.

### prfaq-writer.md
Drafts PR/FAQ documents from a problem statement or idea. Follows the Amazon PR/FAQ structure: press release (what shipped, who benefits, why it matters, key features, quotes) + FAQ (external and internal). Enforces the rule that invented data must be marked as `[DATA NEEDED]` and missing customer evidence as `[NO CUSTOMER VOICE]`.

## Hooks

### data-marker-audit.js
Runs as a post-tool hook on strategy documents. Scans for numerical claims, market size assertions, and customer behavior statements. If a claim lacks a source citation or a `[DATA NEEDED]` marker, it flags the document and blocks completion. Configurable claim patterns at the top of the file.

### workflow-guard.js
Enforces that required sections exist before a strategy document is considered complete. Default required sections: Problem Statement, Customer Need, Success Metrics, Risks. Configurable per document type. Prevents strategy documents from shipping with structural gaps.

## Template

### prfaq-template.md
The standard PR/FAQ template. Includes: press release structure, internal FAQ structure, guidance notes for each section, and markers for required vs optional content. Use this directly or through the `prfaq-writer` agent.

## Dependency Graph

```
discovery/synthesize-research
         ↓ (feeds evidence to)
    product-decision ──→ initiative-checker.md
         ↓
       ideation ──→ ideation-agent.md
         ↓
   prfaq-writer.md
         ↓ (validated by)
data-marker-audit.js + workflow-guard.js
```

The hooks guard the output of all writing-producing skills in this discipline:
```
data-marker-audit.js  ← runs on all strategy document output
workflow-guard.js     ← runs before any strategy document is finalized
```

## Quick Start

**Generate ideas for a product opportunity:**
```
> how might we help small business owners understand which features their customers actually use?
```
`ideation` runs divergent and convergent phases and produces a prioritized idea matrix.

**Decide between two strategic bets:**
```
> help me choose between investing in an AI-powered onboarding flow vs a self-serve analytics dashboard
```
`product-decision` asks for evidence on each option, applies a weighted framework, and produces a decision record.

**Write a PR/FAQ for a new initiative:**
```
> write a PR/FAQ for a feature that lets teams export audit logs in real time
```
`prfaq-writer` agent drafts the full document, marking any gaps that require customer evidence or data.

**Audit initiative health before a planning cycle:**
```
> check the health of all active initiatives before our Q2 planning session
```
`initiative-checker` agent scans initiative documents and produces a health report with status and gaps.

## Installation

```bash
cp -r strategy/skills/* your-project/.claude/skills/
cp -r strategy/agents/* your-project/.claude/agents/
cp -r strategy/hooks/* your-project/.claude/hooks/
cp strategy/templates/prfaq-template.md your-project/.claude/templates/
```

Register hooks in `.claude/settings.json`:
```json
{
  "hooks": {
    "PostToolUse": [
      { "matcher": "Write", "hooks": [
        { "type": "command", "command": "node .claude/hooks/data-marker-audit.js" },
        { "type": "command", "command": "node .claude/hooks/workflow-guard.js" }
      ]}
    ]
  }
}
```
