# Extracting Job Statements from Transcripts

## Input

Transcript or notes from a JTBD interview.

## Extraction Process

### Step 1 — Identify Candidate Moments

Look for patterns in the text:
- "when X happens..." / "every time..."
- "I needed to..." / "I was trying to..."
- "the problem is that..." / "what bothered me was..."
- "at the end of the day what I want is..."
- "if I could do X, then..."

Flag each candidate passage.

### Step 2 — Draft Candidate Job Statement

For each passage, attempt to fill in:

```
When [identified circumstance],
I want [identified progress],
So I can [implicit or explicit outcome].
```

If the outcome does not appear in the quote, infer it carefully and mark with `[inferred]`.

### Step 3 — Classify Dimension

For each job statement, classify:
- **F** = Functional (what to do)
- **E** = Emotional (how to feel)
- **S** = Social (how to be perceived)

A single situation can generate 3 job statements (one per dimension). This is expected.

**Prompt:** If after extraction >50% of the jobs are functional with no E or S dimension identified, pause and ask the PM:

> "Most of the jobs I extracted are functional. Would you like to explore the emotional and social dimensions? That's often where differentiation lives — in how the person feels or how they're perceived, not just what they do."

If the PM agrees, consult `references/frameworks/dimensions.md` for the probing questions and try to derive E/S from the same interview passages. If there is not enough material, record as a gap: `[E/S DIMENSION NOT EXPLORED — revisit in next interview]`.

### Step 4 — Validate with Checklist

For each job statement:
- [ ] Is the circumstance specific (not generic)?
- [ ] Is the progress free of solution references?
- [ ] Does the outcome connect to real value?
- [ ] Is the job solution-independent (could it be accomplished another way)?
- [ ] Is it a single job (not two jobs merged together)?

Discard or split any that do not pass.

### Step 5 — Extract Forces of Progress

Separate passages by force:

| Push | Pull | Anxiety | Habit |
|------|------|---------|-------|
| [passage] | [passage] | [passage] | [passage] |

## Output — Jobs File Format

Save to `{workspace}/research/jtbd/YYYY-MM-DD-<topic>-jobs.md`:

```
# Jobs Identified — [Topic] — [Date]

**Interviewees:** [N interviews / profile]
**Situation explored:** [description]

## Job Statements

### Job 1 — [short label]
**Dimension:** Functional / Emotional / Social
> When [circumstance],
> I want [progress],
> So I can [outcome].
**Source:** Interview [ID/date], passage: "[direct quote]"
**Confidence:** High / Medium / Low

[repeat for each job]

## Forces of Progress

| Force | Evidence |
|-------|----------|
| Push | [passages] |
| Pull | [passages] |
| Anxiety | [passages] |
| Habit | [passages] |

## Jobs Without Sufficient Evidence

[Jobs that surfaced but need more interviews to validate]
```
