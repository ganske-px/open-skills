---
name: product-decision
description: Evidence-driven product decisions covering the critical moments from discovery through definition to execution. Use when the user says "prioritize opportunities", "choose between solutions", "should we bet on [initiative]", "define MVP", "do we have data to decide", "I need to decide if", "which solution to pursue", "which opportunity to tackle first", "is it worth moving forward with this", or "how do I choose between X and Y". Do NOT use when you still need to generate solutions — use ideation first. Do NOT use for generic decisions outside of product — use decision-making instead.
---

# product-decision

Skill for evidence-driven product decisions. Covers the critical moments of the discovery → definition → execution cycle.

## Decision Types

```
What type of decision is this?
│
├─ Prioritize opportunities in an opportunity space?
│  → Mode 1 — Opportunity Prioritization
│
├─ Choose between candidate solutions?
│  → Mode 2 — Solution Selection
│
├─ Advance from discovery to an initiative (PR/FAQ)?
│  → Mode 3 — Initiative Gate
│
└─ Define scope or MVP?
   → Mode 4 — Scope and MVP
```

## Core Principle

Every product decision must be grounded in data or customer voice. If the evidence does not exist:

1. Make the absence explicit — never decide in silence
2. Check whether the data is collectable today
3. If it is not collected: suggest instrumentation or research before deciding
4. If deciding with a gap: document the assumption and the risk in the PR/FAQ or opportunity space

**A decision with a declared assumption is better than a decision with a hidden assumption.**

---

## Mode 1 — Opportunity Prioritization

**When to use:** there are multiple opportunities and you need to decide which one to tackle first.

**Flow:**
1. List candidate opportunities with available evidence
2. For each opportunity, verify:
   - **Reach:** how many customers/users are affected?
   - **Importance:** how important is this job to the customer? (opportunity score)
   - **Current satisfaction:** is the customer already solving this well today? (Forces of Progress)
   - **Connection to outcome:** expected contribution to the product's North Star
3. If data does not exist for any criterion: mark as `[DATA NEEDED]` and suggest how to collect it
4. Calculate simplified score: `importance × (1 - current_satisfaction) × reach`
5. Present ranking with explicit justification of the choice

**Output:** priority opportunity documented with selection criteria on record.

---

## Mode 2 — Solution Selection

**When to use:** there are 2+ candidate solutions for an opportunity and you need to choose.

**Flow:**
1. List solutions with their explicit critical hypotheses
2. For the most critical hypothesis of each solution: check if there is data available
3. If no data: classify as untested premise — suggest the smallest possible experiment
4. **Invoke `decision-making`** to apply a Decision Matrix with the dimensions:
   - Expected impact on outcome
   - Confidence in available evidence
   - Implementation cost (relative estimate)
   - Reversibility (is the error correctable?)
5. **Invoke `decision-making`** to apply Pre-Mortem on the winning solution: "In 6 months, what caused this to fail?"
6. Document the decision and reasoning in the PR/FAQ

---

## Mode 3 — Initiative Gate (Discovery → PR/FAQ)

**When to use:** the team wants to move from discovery to definition (PR/FAQ).

**Invoke `decision-making`** to evaluate the state of the opportunity space before advancing. Frame it as: "Do we have sufficient evidence to bet on this initiative, or are there critical untested premises that would change the decision?"

**Convergence checklist:**
- [ ] Outcome validated with real baseline (not estimated)
- [ ] At least 1 opportunity with evidence from multiple independent sources
- [ ] 2+ solutions explored for the priority opportunity
- [ ] Critical hypothesis of the preferred solution tested (even if preliminary)
- [ ] Causal connection to the product North Star is explicit

**If checklist is incomplete:** do not block — use `decision-making` (Pre-Mortem) to classify the risk of each gap and declare in the PR/FAQ as `[UNVALIDATED PREMISE — high/medium/low risk]`.

**If data does not exist to validate baseline:** check whether the data is collected. If not → suggest instrumentation or communicate to the engineering team.

---

## Mode 4 — Scope and MVP

**When to use:** initiative is approved, need to define what is in/out of the MVP.

**Flow:**
1. List all elements of the proposed solution
2. For each element: "Is this necessary to validate the main hypothesis?" vs. "Desirable but not critical?"
3. MVP = the smallest set that allows confirming or denying the hypothesis
4. For each item outside the MVP: record in "Out of scope for this initiative" in the PR/FAQ
5. Verify that the MVP has measurable success metrics — confirm traceability

**Rule:** if the MVP is not sufficient to confirm or deny the main hypothesis, it is not an MVP — it is an incomplete experiment.

---

## When Data Does Not Exist

If in any mode above the required data does not exist:

1. **Check if it is collectable with the current stack** — check analytics tools, databases, existing reports
2. **If not collected**, suggest specific instrumentation:
   - User behavior event: instrument with your analytics tool
   - Structural database data: communicate to engineering team with data spec
   - Qualitative data: plan a research sprint before deciding
3. **Document the gap** in the relevant artifact: `[DATA NEEDED: description + instrumentation suggestion]`
4. **Do not paralyze the decision** — deciding with a declared premise is better than stalling the process

---

## Anti-Patterns

| Anti-pattern | What to do instead |
|---|---|
| Deciding by intuition without checking if data exists | Always check available data sources first |
| Treating absence of data as confirmation of hypothesis | Absence of evidence ≠ evidence of absence |
| Choosing the most complex solution because it seems complete | MVP first — validated hypothesis first |
| Deciding without documenting the reasoning | Every decision has a trail in the PR/FAQ or opportunity space |
| Using data without declaring the collection date | Data is a snapshot — declare when it was collected |
| Blocking the team due to lack of perfect data | Sufficient data + declared premise > paralysis |
