# Story Type: Technical Dependencies / Challenges

## When to use
- Present technical debt that blocks the product
- Propose architecture migration or new integration
- Explain why a feature takes longer than it seems
- Align engineering + product on build/buy/partner trade-offs
- "Why we need to do X before Y"

## Framework: Problem-Solution with Explicit Trade-offs

Technical credibility comes from honesty about constraints and uncertainties — not from optimism. A technical audience detects bullshit instantly.

### Required structure

```
1. CURRENT STATE — the technical pain today
   → Concrete: "today, to add a new partner we need a code change and deploy"
   → Evidence: cycle time, incidents, observed limitations
   → Don't exaggerate, don't minimize — be precise

2. WHY THIS MATTERS FOR THE PRODUCT
   → Connect the technical constraint to user/business impact
   → "This blocks [feature X] that [customer Y] needs"
   → Non-technical audience needs this bridge

3. CONSTRAINTS AND PREMISES
   → What cannot change (infrastructure, team, deadline, contracts)
   → What is still uncertain — name what we don't know
   → [DATA NEEDED: ...] for real gaps

4. OPTIONS CONSIDERED
   → Minimum 2 real paths (not strawmen to make the preferred look good)
   → For each option: what it solves, what it doesn't, cost, risk
   → Trade-off table is more honest than narrative

5. RECOMMENDATION
   → Which option, why, with which premises
   → What changes if a premise changes
   → Next steps: owner, deadline, dependencies

6. RISKS AND PLAN B
   → What could go wrong
   → What we do if it does
```

## Skills to invoke

| When | Skill |
|---|---|
| Analyzing trade-offs between technical options | `decision-making` — use Decision Matrix or Cynefin |
| Current impact data (SLAs, incidents, cycle time) | `data-research` |
| End-user impact | `synthesize-research` — what users complain about |
| Build/buy/partner decision | `product-decision` |

## Non-negotiable rules

- **Name the uncertainties.** "We don't know X" is stronger than pretending you do
- **Real trade-offs.** Every solution has a cost — presenting it as "perfect solution" destroys credibility
- **Connect to product.** Product/business audience needs to understand the impact, not the technical details
- **Data in Appendix.** If citing performance/incident metrics, the query/source must be available
- **`[DATA NEEDED: ...]`** for any unconfirmed number

## Collection questions

1. "What is the main technical constraint? In one sentence, what is not possible today?"
2. "What product feature is being blocked by this?"
3. "What options have already been considered or discarded?"
4. "Who needs to approve or be aligned? (CTO, engineering, PM, business)"
5. "What is the confidence level on the effort estimate?"

## Recommended output

| Audience | Preferred format |
|---|---|
| Engineering + PM | `deck-outline` with trade-off table as the center |
| CTO / technical leadership | `exec-memo` with explicit recommendation at the top |
| Business stakeholder | Simplified `deck-outline` — focus on product impact, not technical details |

## Trade-off table (template)

| Option | Solves | Doesn't solve | Effort | Risk |
|---|---|---|---|---|
| Option A | ... | ... | S/M/L | High/Medium/Low |
| Option B | ... | ... | ... | ... |

## Anti-patterns

- Presenting only the preferred option — technical audience notices and loses trust
- Estimates without uncertainty range — "3 weeks" without context is misinformation
- Technical jargon for business audience without impact bridge
- Omitting existing technical debt that affects the proposed solution
