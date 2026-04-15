# decision/

Structured decision-making for product managers. One skill that detects the type of decision you are facing and applies the right framework automatically — from daily trade-offs to strategic bets.

## What's Included

```
decision/
  skills/
    decision-making/    # Unified decision skill with 5 frameworks
```

**1 skill, 5 frameworks.**

## The decision-making Skill

A single skill that handles the full range of product decisions by first classifying the decision type (using Cynefin), then routing to the most appropriate framework.

### Frameworks

**Cynefin Classification** — The entry point. Before choosing a decision method, classify the problem:
- **Simple/Clear**: Cause and effect are obvious. Apply best practice.
- **Complicated**: Cause and effect require analysis. Apply expert judgment.
- **Complex**: Cause and effect only visible in retrospect. Run experiments.
- **Chaotic**: No clear cause and effect. Act to stabilize, then sense.

**RAPID** — For organizational decisions involving multiple stakeholders. Maps who Recommends, who Agrees, who Performs, who Inputs, and who Decides. Surfaces unclear ownership and resolves decision-making gridlock.

**Weighted Decision Matrix** — For multi-criteria comparisons (e.g., build vs buy, vendor selection, platform choice). Score each option on weighted criteria to produce a defensible ranking. Includes sensitivity analysis to test how robust the result is.

**Pre-Mortem** — For stress-testing a decision before committing. Imagine it is one year later and the decision failed catastrophically. What went wrong? Surfaces risks that confirmation bias tends to suppress.

**OODA Loop** — For fast-moving competitive or operational situations. Observe, Orient, Decide, Act. Useful when speed matters more than completeness, and when the situation is changing faster than a full analysis can keep up.

### Output
Every decision session produces a **Decision Record** — a structured document capturing: the decision statement, context, options considered, framework applied, recommendation with rationale, risks, and dissenting views. Designed to be shared with stakeholders and referenced later.

## Dependency Graph

```
Cynefin Classification
        ↓ (routes to)
┌───────────────────────────────────┐
│ Simple    → best practice         │
│ Complicated → RAPID or Matrix     │
│ Complex   → Pre-Mortem + OODA     │
│ Chaotic   → OODA                  │
└───────────────────────────────────┘
        ↓ (all produce)
  Decision Record
```

The skill handles the routing automatically — you describe the decision and it picks the right framework.

## Quick Start

**Navigate a build vs buy decision:**
```
> help me decide between building a custom analytics pipeline and buying a third-party tool
```

**Resolve a cross-functional decision with unclear ownership:**
```
> we need to decide whether to sunset our legacy API — three teams are involved and nobody agrees
```

**Stress-test a strategic decision:**
```
> run a pre-mortem on our plan to expand into the enterprise segment this quarter
```

**Handle a competitive emergency:**
```
> our biggest competitor just launched a feature we've been planning for 6 months — what do we do?
```

## Installation

```bash
cp -r decision/skills/* your-project/.claude/skills/
```

No hooks or agents required. The skill is fully self-contained.
