# Output Format: Executive Memo

## What it is

A 1–3 page written document read asynchronously before a decision meeting. Based on the Amazon 6-pager model (compact version). Allows the meeting to focus on debate and decision, not presentation.

## When to use

- Strategic decisions requiring exec approval
- Before alignment meetings with C-level
- Recommendations that need a written record
- Any situation where the audience needs to think before reacting

## Template

```markdown
# [Title = recommendation in 1 sentence]

**Date:** YYYY-MM-DD
**Author:** [name]
**Decision needed:** [what we need the person to approve/decide]
**Deadline:** [when we need the decision and why]

---

## TL;DR

[3–5 bullets — what the person needs to know if they have 2 minutes]
- Recommendation: [concrete action]
- Why now: [urgency]
- Expected impact: [number or outcome]
- Biggest risk: [and how we manage it]
- Next step if approved: [action + owner + deadline]

---

## Context

[1–2 paragraphs. What is happening. Why this topic arose now.
Do not explain what the audience already knows — go straight to what is new or different.]

## Problem

[What specifically is wrong or missing. Data that quantifies it.
If there is no data: [DATA NEEDED: ...]]

## Recommendation

[The proposed action, in enough detail for approval.
Not the process — the decision.]

## Supporting Arguments

**1. [Strongest argument]**
[Evidence / data]

**2. [Second argument]**
[Evidence / data]

**3. [Third argument]**
[Evidence / data]

## Alternatives Considered

| Option | Why discarded |
|---|---|
| [Alternative A] | [criterion, not opinion] |
| [Alternative B] | [criterion] |

## Risks and Mitigation

| Risk | Probability | Mitigation |
|---|---|---|
| [Risk 1] | High/Medium/Low | [action] |
| [Risk 2] | ... | ... |

## Success Criteria

[How we will know it worked. Specific metric with deadline.]

## Next Steps (if approved)

| Action | Owner | Deadline |
|---|---|---|
| [Action 1] | [name] | [date] |
| [Action 2] | [name] | [date] |

---

## Appendix — Data and Sources

[SQL / HogQL queries / analysis links used to support the document]
[Mandatory if any number appears in the document]
```

## Quality rules

- **TL;DR at the top** — someone with 2 minutes reads only this; someone who will debate reads everything
- **Explicit recommendation** — not "let's discuss", but "I recommend X"
- **Max 3 pages** — if it doesn't fit, the thinking is not mature
- **Plain language** — exec memos are not the place for technical jargon
- **Data with source** — Appendix mandatory for any number
- **`[DATA NEEDED: ...]`** for gaps — never invent

## How to use in the meeting

The exec memo is read BEFORE the meeting (silent reading in the first 5–10 minutes, or sent in advance). The meeting starts with questions — not with a presentation.

If the memo needs to be presented verbally: use `verbal-brief.md` as a complement.
