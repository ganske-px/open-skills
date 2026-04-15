# discovery/

The complete continuous discovery toolkit. Covers the full research workflow: opportunity definition, interview planning, interview facilitation, feedback synthesis, JTBD extraction, and opportunity scoring. Designed to run as a coherent system or as individual tools depending on where you are in the process.

## What's Included

```
discovery/
  skills/
    discovery-kickoff/     # Orchestrates the full discovery cycle from one prompt
    jtbd/                  # Jobs-to-Be-Done: interview planning, job mapping, opportunity scoring
    research-plan/         # Design a research plan (method, sample, questions, timeline)
    research-interview/    # Conduct and document user interviews
    research-feedback/     # Analyze and triage user feedback (tickets, surveys, NPS)
    synthesize-research/   # Synthesize findings across sources into structured insights
  agents/
    jtbd-facilitator.md    # Autonomous agent for JTBD interview facilitation
    ost-facilitator.md     # Autonomous agent for Opportunity Solution Tree facilitation
  hooks/
    evidence-guard.js      # Blocks output that references claims without evidence citations
    staleness-alert.js     # Warns when research cited in context is older than a threshold
```

**6 skills, 2 agents, 2 hooks.**

## Skills

### discovery-kickoff
The orchestrator. Takes a single prompt — "start discovery for [topic]" — and coordinates the full cycle: evidence gathering, JTBD extraction, opportunity sizing, and research planning. Produces a structured discovery brief ready for team review. Use this when starting a new discovery cycle from scratch.

### jtbd
Implements the full Jobs-to-Be-Done methodology:
- **Extract jobs**: Identify functional, emotional, and social jobs from research data
- **Job mapping**: Map job steps (define, locate, prepare, confirm, execute, monitor, modify, conclude)
- **Opportunity scoring**: Score job steps on importance and satisfaction to surface high-opportunity areas
- **Outcome statements**: Write well-formed outcome statements for each opportunity
Use this when you have research data and want to turn it into a prioritized opportunity map.

### research-plan
Design a research plan before running any research. Outputs a structured plan with: research question, method selection rationale, participant criteria, screener questions, sample size, timeline, and success criteria. Prevents common mistakes like under-sampling, mismatched methods, or unclear research questions.

### research-interview
Support before, during, and after user interviews. Pre-session: builds an interview guide with open-ended questions and follow-up probes. During: provides facilitation reminders and question suggestions. Post-session: structures raw notes into observations, quotes, and themes.

### research-feedback
Analyze existing user feedback from any source: support tickets, feature requests, NPS responses, app store reviews, survey open-ends. Extracts themes, counts frequency, identifies sentiment, and surfaces the most actionable signals. Good for continuous listening when you cannot run interviews.

### synthesize-research
Cross-source synthesis. Takes research from multiple types and sources, applies thematic analysis and triangulation, and produces a structured synthesis: key findings (with evidence and confidence levels), user segments, opportunity areas, and recommendations. See also the `user-research-synthesis` starter command for the full methodology reference.

## Agents

### jtbd-facilitator.md
An autonomous sub-agent that runs a JTBD interview end-to-end. Given a participant description and research question, it generates and asks probing questions, captures observations, extracts job statements, and produces a structured interview summary. Deploy when you want to run exploratory interviews at scale.

### ost-facilitator.md
An autonomous sub-agent for building and maintaining an Opportunity Solution Tree. Given a desired outcome, it helps map the opportunity space, evaluate solutions against opportunities, and identify assumption tests. Useful for making the connection between research findings and product bets explicit.

## Hooks

### evidence-guard.js
Runs as a post-tool hook. Scans generated output for unsubstantiated claims — market size assertions, user behavior generalizations, metric references — and blocks or flags content that lacks evidence citations. Configurable: set the sensitivity level and which claim patterns to check.

### staleness-alert.js
Runs as a context hook. When research documents older than a configurable threshold (default: 90 days) are loaded into context, it emits a warning. Prevents stale research from being treated as current truth without explicit acknowledgment.

## Dependency Graph

```
research-plan
     ↓
research-interview ──→ research-feedback
     ↓                       ↓
     └─────────→ synthesize-research
                       ↓
                      jtbd
                       ↓
             discovery-kickoff (orchestrates all)
```

The hooks run passively across all skills:
```
evidence-guard.js  ← wraps all output-producing skills
staleness-alert.js ← wraps all context-loading operations
```

## Quick Start

**Start a new discovery cycle:**
```
> start discovery for improving activation rates in our self-serve onboarding flow
```
`discovery-kickoff` orchestrates the full cycle: it will ask what evidence you have, extract jobs, identify opportunities, and produce a discovery brief.

**Plan a round of user interviews:**
```
> help me design a research plan to understand why enterprise users churn in the first 90 days
```
`research-plan` walks you through method selection, participant criteria, and question design.

**Synthesize existing research:**
```
> I have notes from 8 customer interviews and 3 months of support tickets — synthesize them into findings
```
`synthesize-research` processes multi-source input and produces findings with evidence and confidence levels.

## Installation

```bash
cp -r discovery/skills/* your-project/.claude/skills/
cp -r discovery/agents/* your-project/.claude/agents/
cp -r discovery/hooks/* your-project/.claude/hooks/
```

Register hooks in `.claude/settings.json`:
```json
{
  "hooks": {
    "PostToolUse": [
      { "matcher": "*", "hooks": [{ "type": "command", "command": "node .claude/hooks/evidence-guard.js" }] }
    ]
  }
}
```
