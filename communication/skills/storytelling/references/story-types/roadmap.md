# Story Type: Roadmap — What Are We Building

## When to use
- Present the product plan for the next cycle
- Communicate priorities and delivery sequence
- Align stakeholder expectations on what's coming (and what isn't)
- Quarterly OKR and initiative review

## Framework: Now/Next/Later + Narrative Arc

A roadmap without narrative is a feature list. What transforms it into a story is the answer to "why in this order?" and "what was deliberately left out?"

### Required structure

```
1. ANCHOR IN THE NORTH STAR
   → Where we are on the journey toward the North Star
   → What this cycle's objective is (quarterly or semi-annual OKR)
   → 1 slide/section — quick, but cannot be missing

2. WHAT WE LEARNED (if it's a cycle review)
   → What was delivered, what wasn't and why
   → Learning that influences the next priorities
   → Honesty > positivity washing

3. NOW — WHAT WE'RE BUILDING NOW
   → Initiatives in execution with owner and delivery horizon
   → For each one: job-to-be-done served + success metric
   → Don't list tasks — list expected outcomes

4. NEXT — WHAT WE'LL BUILD NEXT
   → Initiatives prioritized for the next cycle
   → Explicit prioritization criterion (RICE, ICE, OST opportunity score)
   → "These enter when the Now ones finish" — not fixed dates

5. LATER — WHAT'S ON THE HORIZON
   → Signals and longer-term bets
   → Not yet committed — subject to change as we learn
   → Valuable for stakeholders planning dependencies

6. WHAT'S NOT HERE AND WHY (the most differentiating section)
   → 2–3 important things deliberately left out
   → Why: focus, resources, technical sequence, needed learning
   → "We're not doing X now because [criterion]" — demonstrates conscious choices
   → Prevents the question "and project Y they promised me?"
```

## Skills to invoke

| When | Skill |
|---|---|
| Initiative prioritization | `product-decision` — OST opportunity score, RICE |
| Jobs-to-be-Done for each initiative | `jtbd` — ensure each item serves a real job |
| Data supporting the priorities | `data-research` |
| Customer voice on priorities | `synthesize-research` + `research-feedback` |
| Sequence trade-off | `decision-making` — OODA or Decision Matrix |

## Non-negotiable rules

- **Connect each item to the user's job.** "Notifications" says nothing. "User resolves issue without calling support" says everything
- **Visible prioritization criterion.** Audience will ask "why not X before Y?" — have the answer ready
- **Dates are the roadmap's enemy.** Now/Next/Later by horizon is more honest than dates that will change
- **Initiatives = outcomes, not features.** "Launch penalty management" < "Manager covers penalty in < 5 min"
- **What's not here.** Required section — an unmanaged expectation absence turns into a bad surprise
- **Data in Appendix.** If citing metrics to justify prioritization, source available

## Collection questions

1. "What is the OKR or objective for this cycle?"
2. "What initiatives are currently in execution?"
3. "What was the criterion that determined this order? (impact, urgency, technical dependency)"
4. "What is in the backlog that stakeholders will ask why it's not here?"
5. "Is there a technical dependency that determines the sequence?"

## Recommended output

| Audience | Preferred format |
|---|---|
| Board / C-level | Simple `deck-outline` (Now/Next/Later visual) + `exec-memo` with prioritization criterion |
| Squad / product team | Detailed `deck-outline` with owners and mapped jobs |
| External stakeholders / commercial | Simplified `deck-outline` — outcomes and approximate timelines, no internal details |

## Recommended visualization (for `html-story` or `deck-outline`)

```
NOW          NEXT         LATER
─────────    ─────────    ─────────
Initiative A Initiative C Signal X
 └ outcome   └ outcome    (bet)
 └ owner
Initiative B Initiative D
 └ outcome   └ outcome
```

## Anti-patterns

- Roadmap as a feature list without a "why" narrative
- Fixed dates for Next/Later items — creates premature commitment
- Not showing what was discarded — audience doesn't know if what they requested was heard
- Roadmap that doesn't connect to the North Star — looks like a random list
- 12+ month outlook with feature-level precision — misleading about certainty level
