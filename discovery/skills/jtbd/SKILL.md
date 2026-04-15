---
name: jtbd
description: Implements the full Jobs-to-Be-Done framework. Use when the user says "JTBD interview", "interview guide", "map jobs for [initiative]", "job map", "analyze research with JTBD", "forces of progress", "opportunity score", "job story", or "hire/fire analysis". Do NOT use to synthesize research without a JTBD lens — use synthesize-research instead. Do NOT use for general discovery — use discovery-kickoff instead.
---

# JTBD — Jobs to Be Done

Complete skill for applying the JTBD framework across the product work cycle.
Covers: interview planning, job extraction, retrospective analysis of existing data, and opportunity mapping for initiatives.

## Core Principles

- Customers "hire" products to get a job done — they don't buy features
- Job statement: `When [circumstance] → I want [progress] → So I can [outcome]`
- Every job has three dimensions: **functional** (what to do), **emotional** (how to feel), **social** (how to be perceived)
- **Forces of Progress**: Push (current frustration) + Pull (attraction to the new solution) vs. Anxiety (fear of change) + Habit (comfort with the current way)
- **Hiring/Firing**: customers hire and fire solutions. Understanding both sides is essential
- Never fabricate customer data. If there is no evidence, mark `[NO CUSTOMER VOICE — collect]`

## Decision Tree — Which Mode to Use?

```
What is your starting point?
│
├─ Do you want to PLAN an interview or EXTRACT jobs from a transcript?
│  → Interview Mode
│  → Read: references/interview/guide.md + references/interview/extraction.md
│
├─ Do you have existing research, feedback, or data and want to apply a JTBD lens?
│  → Analysis Mode
│  → Read: references/analysis/lens.md + references/analysis/forces.md
│
└─ Do you have a specific INITIATIVE and want to map jobs, score opportunities,
   and connect to a PR/FAQ?
   → Initiative Mode
   → Read: references/initiative/job-map.md + references/initiative/opportunity-score.md
            + references/initiative/prfaq-bridge.md
```

## Where to Save Artifacts

| Artifact | Destination |
|----------|-------------|
| Job statements extracted from interviews | `{workspace}/research/jtbd/YYYY-MM-DD-<topic>-jobs.md` |
| Forces of Progress from research | `{workspace}/research/jtbd/YYYY-MM-DD-<topic>-forces.md` |
| Initiative job map | `{workspace}/initiatives/{initiative-name}/jtbd-job-map.md` |
| Initiative opportunity score | `{workspace}/initiatives/{initiative-name}/jtbd-opportunity-score.md` |
| Job stories for PR/FAQ | "Customer Voice" section of the initiative's PR/FAQ |

## Framework References

- Job statement format and examples: `references/frameworks/job-statements.md`
- F/E/S dimensions guide + prompts: `references/frameworks/dimensions.md`
- Desired outcomes per step (Strategyn): documented in `references/initiative/job-map.md` (section "Step 3")
- Filled job map example: `references/initiative/examples/job-map-example.md`
- Opportunity score example: `references/initiative/examples/opportunity-score-example.md`

## Anti-Patterns

- Never cite fabricated customer voice — use `[NO CUSTOMER VOICE — collect]`
- Never confuse a job with a solution ("the job is to use the app" is wrong — the job is the progress the app enables)
- Never skip Forces of Progress when analyzing churn or low adoption
- Never generate an opportunity score without data on both importance AND satisfaction
- Do not write job statements in solution mode ("I want to use feature X") — always in progress mode

## Integration with OST and Initiative Context

JTBD and CDH (Continuous Discovery Habits) are complementary — each solves a different part of the problem:

| JTBD provides | CDH/OST structures |
|---|---|
| Job statements (what the customer wants to accomplish) | Opportunities in the tree |
| Forces of Progress (push/pull/anxiety/habit) | Evidence backing each opportunity |
| Opportunity score (importance × satisfaction) | Prioritization across opportunities |
| Job map (steps to accomplish the job) | Candidate solutions per job stage |

**Integration flow between the two frameworks:**

1. **JTBD Interview Mode** → captures jobs during CDH interviews (Timeline Interview format in `research-interview`)
2. **JTBD Analysis Mode** → transforms feedback data into structured jobs that feed the OST
3. **JTBD Initiative Mode** → maps opportunities + prioritizes via opportunity score → feeds directly into the OST
4. **OST with sufficient evidence** → triggers initiative creation → PR/FAQ writer uses job statements as customer voice

**End goal:** every job statement extracted should appear, at some point, in:
- An opportunity in the OST (with associated evidence)
- Customer voice in the PR/FAQ (citation or job story)
- A critical assumption (if the job is not yet satisfied by the proposed solution)

Without this chain, JTBD becomes a theoretical exercise — not a product decision driver.
