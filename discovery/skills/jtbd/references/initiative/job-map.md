# Job Map — Mapping Jobs for an Initiative

## What Is a Job Map

A job map is the universal sequence of steps any person executes when trying to accomplish a job — regardless of which solution they use. It reveals where the biggest pains and opportunities are.

## The 8 Universal Steps (Ulwick)

| Step | What it represents | Key question |
|------|-------------------|--------------|
| 1. Define | Plan and prepare for the job | "What does the person need to decide or define before starting?" |
| 2. Locate | Find necessary inputs | "What does the person need to locate or gather?" |
| 3. Prepare | Organize the inputs | "What needs to be configured, prepared, or assembled?" |
| 4. Confirm | Verify readiness | "What does the person confirm before executing?" |
| 5. Execute | Carry out the core job | "What is the main action?" |
| 6. Monitor | Track progress | "How does the person check whether things are going well?" |
| 7. Modify | Correct and adjust | "What does the person do when something goes unexpectedly?" |
| 8. Conclude | Wrap up and record | "How does the person close out and record the result?" |

## How to Build the Job Map

### Step 1 — Define the main job

Write the primary job statement for the initiative:

```
When [circumstance],
I want [progress],
So I can [outcome].
```

### Step 2 — Fill in each step

For each of the 8 steps, describe:
- What the person does today (current state)
- What the main pains are in this step (evidence)
- What the proposed solution changes in this step

### Step 3 — Extract Desired Outcomes per step

Each step of the job map generates 1–5 **desired outcome statements** — measurable results the customer wants to achieve at that step. These outcomes are the unit of measure for the opportunity score.

**Desired outcome statement format (Strategyn):**

```
[Direction] + [metric] + [object] + [context]
```

Common directions: Minimize, Reduce, Increase, Maximize, Avoid, Ensure.

**Generic B2B examples:**

| Step | Desired Outcome |
|---|---|
| Define | Minimize the time it takes to **determine which provider is the best fit** for a new engagement |
| Locate | Reduce the likelihood of **missing a required document** before submitting the request |
| Confirm | Minimize the time it takes to **verify that all criteria are met** before proceeding |
| Execute | Reduce the likelihood of **a qualified candidate being incorrectly rejected** |
| Monitor | Minimize the time it takes to **identify which requests are stuck** in the pipeline |
| Modify | Reduce the number of **manual interventions needed** to correct an incomplete result |

**Rules:**
- Outcomes are from the customer's point of view, not the company's
- Outcomes are solution-independent (they do not mention features)
- Each outcome must be measurable (can be rated by importance × satisfaction)
- 1–5 outcomes per step is the ideal range; simple steps may have 1, complex steps up to 5

### Step 4 — Identify critical steps and outcomes

Mark each step with:
- **High pain / Low satisfaction** → priority opportunity
- **High pain / High satisfaction** → existing differentiator to protect
- **Low pain / Any satisfaction** → do not prioritize

For each critical step, the desired outcomes are direct candidates for the opportunity score (see `opportunity-score.md`).

## Job Map Template

```
# Job Map — [Initiative] — [Date]

**Main job:**
> When [circumstance], I want [progress], So I can [outcome].

**Primary persona:** [who performs the job]

| Step | Current state | Pains identified | Evidence | What the proposed solution does |
|------|--------------|-----------------|----------|---------------------------------|
| 1. Define | [description] | [pains] | [source] | [proposal] |
| 2. Locate | | | | |
| 3. Prepare | | | | |
| 4. Confirm | | | | |
| 5. Execute | | | | |
| 6. Monitor | | | | |
| 7. Modify | | | | |
| 8. Conclude | | | | |

## Desired Outcomes per Step

| Step | # | Desired Outcome | Dimension (F/E/S) |
|------|---|----------------|-------------------|
| 1. Define | 1.1 | [Direction] + [metric] + [object] + [context] | F |
| 1. Define | 1.2 | | |
| 2. Locate | 2.1 | | |
| [...] | | | |

## Priority Steps

| Step | Pain | Current satisfaction | Priority | # Outcomes |
|------|------|---------------------|----------|------------|
| [step] | High | Low | CRITICAL | [N outcomes in this step] |
```

Save to `{workspace}/initiatives/{initiative-name}/jtbd-job-map.md`.
