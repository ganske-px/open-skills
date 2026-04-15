---
name: research-plan
description: |
  Creates a new qualitative research plan for a product discovery topic.
  Guides the user through method selection and produces a structured plan file.

  Triggers: "create a research plan", "plan interviews about X", "design research for X",
  "I want to interview customers about X", "plan a usability study", "build an interview guide"

  Do NOT use to log a completed interview — use research-interview instead.
  Do NOT use to synthesize existing research — use synthesize-research instead.
---

# research-plan

Creates a new research plan in `{workspace}/research/plans/`.

## When to Use

- "create a research plan"
- "I'm going to interview [persona/segment] about [topic]"
- "I want to research customers about [topic]"
- "plan a usability study"
- "build an interview guide"

## Workflow

### 1. Collect minimum information

Ask the user (only for what was not provided in the prompt):

**Open fields:**
- Central research question or topic
- Related initiative (or "Exploratory" if none)
- Opportunity or assumption this research is meant to inform (if unknown, leave `[TO BE DEFINED]` and ask before creating the file — a plan with no decision to inform is unlikely to produce actionable data)
- Responsible owner

**Method selection** — if not specified by the user, call `AskUserQuestion` with:
- question: "What research method do you have in mind?"
- options:
  - "Qualitative interviews (behavior, motivation, 'why')"
  - "Survey / questionnaire (patterns at scale)"
  - "Fake-door / smoke test (validate demand before building)"
  - "A/B test / quantitative experiment"
  - "Not sure yet — help me choose"
- type: select

If "Not sure yet": invoke `decision-making` with Cynefin to classify the type of question and recommend the appropriate method.

### 2. Determine the file name

- Format: `PLAN-[TOPIC-SLUG]-[YYYY-MM-DD].md`
- Example: `PLAN-onboarding-friction-2026-04-15.md`
- Use the current system date.

### 3. Create the file

Create `{workspace}/research/plans/PLAN-[slug]-[date].md` with the structure below.
Fill in collected fields. Use `[REQUIRED DATA: ...]` for any gaps the user needs to complete.
Adapt the "Central Questions" section to the specific topic if enough context was provided.

```markdown
# Research Plan — [Topic]

**Status:** Draft
**Owner:** [name]
**Date:** [YYYY-MM-DD]
**Related initiative:** [initiative name or "Exploratory"]
**Opportunity / assumption being tested:** [TO BE DEFINED if unknown]

## Central Research Question

[The one question this plan must answer]

## Method

[Selected method + brief rationale]

## Target Participants

**Persona / segment:** [describe who you want to speak to]
**Number of sessions:** [REQUIRED DATA: planned count]
**Recruitment criteria:** [key inclusion/exclusion criteria]

## Central Questions

[5–8 open questions that map to the research question]

1.
2.
3.
4.
5.

## Interview Guide (Timeline Interview Format)

> Follow the Timeline Interview structure from the research-interview skill:
> Block 1 (Participant context) → Block 2 (Event timeline) → Block 3 (Forces of Progress)
> → Block 4 (Job Statement candidate) → Block 5 (OST connection)

[Draft questions per block — or leave placeholders for the interviewer to fill]

## Decisions This Research Will Inform

[REQUIRED DATA: list the decisions or bets that depend on this research — without this the plan should not be executed]

## Definition of Done

- [ ] [N] sessions completed
- [ ] Synthesis document produced
- [ ] Key insights connected to the relevant initiative or opportunity tree
```

### 4. Confirm

Inform the user of the file path and any fields still marked `[REQUIRED DATA: ...]`.

## Rules

- Never invent hypotheses — leave `[HYPOTHESIS TO BE DEFINED]` if the user did not provide one.
- The "Decisions this research will inform" field is mandatory — ask explicitly if the user does not know.
- If there is an active opportunity tree (OST) linked to the topic, the plan must address at least one opportunity or solution hypothesis — research disconnected from a decision tree produces data that cannot inform action.
- Structure the interview guide in **Timeline Interview** format (see the research-interview skill) — do not use STAR or generic interview scripts.

## Output

File created at `{workspace}/research/plans/PLAN-[slug]-[date].md` with status "Draft".
