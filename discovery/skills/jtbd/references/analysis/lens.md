# Retrospective Analysis Through the JTBD Lens

## When to Use

You have existing data (feedback, interviews, surveys, analytics events)
and want to identify the jobs being signaled — without conducting new interviews.

## Accepted Inputs

| Source | How to treat |
|--------|-------------|
| Feedback log / support tickets | Read all entries; look for situation + frustration patterns |
| Existing interview transcripts | Apply `references/interview/extraction.md` |
| Churn analysis (analytics events) | Identify drop-off moments as signals of a job not accomplished |
| Support comments / user messages | Look for frustration with the current state (Push) |
| NPS detractors | Strong signal of a job not accomplished or unbalanced forces |

## Process

### Step 1 — Inventory Available Data

List each source and its coverage:
- How many records / interviews?
- What time period?
- What customer profile is represented?

### Step 2 — Extract Job Candidates

For each record or feedback entry, identify:
- **Situation:** when did it happen? what was the context?
- **Frustration:** what was not working?
- **Desire:** what was the person trying to achieve?

Draft job candidates in `When → I want → So I can` format.

### Step 3 — Group and Saturate

Group similar job candidates together. A job "saturates" when it appears in 3+ independent sources.

Classify each job by:
- **Frequency:** how many times did it appear?
- **Evidence level:**
  1. Verified quantitative data (analytics query with documented source)
  2. Direct customer voice (real quote with context)
  3. Qualitative observation (interview notes)
  4. Proxy / inference (related metric)
  5. Team intuition — do NOT use as the basis for a job statement

### Step 4 — Identify Evidence Gaps

For jobs with weak evidence (level 4–5), mark:
`[INSUFFICIENT EVIDENCE — conduct JTBD interviews to validate]`

### Step 5 — Prioritize by Frequency and Evidence

Order the job list by:
1. Frequency of appearance
2. Evidence level
3. Connection to business metrics (churn, NPS, SLA)

## Output

Save to `{workspace}/research/jtbd/YYYY-MM-DD-<topic>-jobs.md` using the same format as `references/interview/extraction.md`.

Add an evidence gaps section:

```
## Evidence Gaps

| Job | Current evidence | What is missing |
|-----|-----------------|-----------------|
| [job label] | Level 4 — 2 feedback entries | 3+ interviews to saturate |
```
