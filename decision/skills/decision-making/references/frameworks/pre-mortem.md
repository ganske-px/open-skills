# Pre-Mortem Analysis

> Prospective hindsight technique to identify risks BEFORE committing to a decision.
> Research shows pre-mortems improve risk forecasting accuracy by ~30%.

## Core Concept

**Post-mortem:** After failure, ask "What went wrong?"
**Pre-mortem:** Before starting, assume failure already happened, ask "What went wrong?"

The psychological shift from "What could go wrong?" to "What DID go wrong?" unlocks different thinking:
- Overcomes optimism bias
- Makes it safe to voice concerns
- Surfaces risks people were reluctant to mention
- Leverages hindsight bias constructively

---

## The Pre-Mortem Prompt

> "Imagine it's [6 months / 1 year] from now. We chose [Option X].
> It has failed spectacularly.
>
> What went wrong? Why did we not see it coming?"

---

## 5-Step Process

### Step 1: Assume Failure

Set the scene explicitly:
- State the decision/project
- Set a future timeframe
- Declare it has FAILED completely
- Ask participants to imagine they're looking back

**Script:**
> "We're now in [future date]. We committed to [decision].
> It didn't just underperform — it failed completely.
> We're conducting a post-mortem. What happened?"

---

### Step 2: Generate Failure Reasons

Each participant independently lists reasons for failure:
- No discussion yet
- Quantity over quality
- Include "unlikely" scenarios
- Think across categories (technical, people, market, etc.)

**Prompt questions:**
- What technical problems occurred?
- What did we misunderstand about the situation?
- What assumptions proved wrong?
- What external factors blindsided us?
- What internal conflicts derailed us?
- What did we know but ignore?

---

### Step 3: Categorize Risks

Group failure reasons into categories:

| Category | Example Risks |
|----------|---------------|
| Technical | System failures, integration issues, scalability |
| People | Skill gaps, turnover, resistance, communication |
| Process | Timeline, dependencies, handoffs, approvals |
| External | Market changes, competitor moves, regulations |
| Resources | Budget, tools, access, vendor reliability |
| Assumptions | Untested beliefs that proved false |

---

### Step 4: Prioritize by Likelihood × Impact

Score each risk:

**Likelihood (L):** 1-5 scale
| Score | Probability |
|-------|-------------|
| 1 | Unlikely (<10%) |
| 2 | Possible (10-25%) |
| 3 | Moderate (25-50%) |
| 4 | Likely (50-75%) |
| 5 | Almost certain (>75%) |

**Impact (I):** 1-5 scale
| Score | Severity |
|-------|----------|
| 1 | Negligible — Minor inconvenience |
| 2 | Low — Some rework needed |
| 3 | Moderate — Significant delay/cost |
| 4 | High — Major setback |
| 5 | Critical — Project failure |

**Priority Score = L × I**

| L×I Score | Priority | Action |
|-----------|----------|--------|
| 1-5 | Low | Accept or monitor |
| 6-12 | Medium | Mitigate if feasible |
| 13-19 | High | Must have mitigation plan |
| 20-25 | Critical | Consider go/no-go |

---

### Step 5: Develop Mitigations

For high-priority risks (L×I ≥ 13):

1. **Prevent:** Can we eliminate the risk entirely?
2. **Detect:** Can we see it coming early?
3. **Mitigate:** Can we reduce likelihood or impact?
4. **Accept:** If unavoidable, what's our response plan?

**Mitigation template:**
```
Risk: [Description]
L×I: [Score]
Owner: [Who monitors this?]
Prevention: [How to avoid?]
Detection: [Early warning signals?]
Response: [If it happens, what do we do?]
Review: [When to reassess?]
```

---

## Pre-Mortem Template

```markdown
## Pre-Mortem Analysis: [Decision/Project]

**Date:** YYYY-MM-DD
**Participants:** [Names]
**Decision:** [What we're stress-testing]
**Assumed failure date:** [Future date]

### Failure Scenario

> "It's [date]. We committed to [decision]. It has failed.
> We're conducting a post-mortem."

### Identified Risks

| # | Risk Description | Category | L | I | L×I | Priority |
|---|------------------|----------|---|---|-----|----------|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| ... | | | | | | |

### High-Priority Risks (L×I ≥ 13)

#### Risk: [Name]
- **L×I:** [Score]
- **Owner:** [Person responsible for monitoring]
- **Prevention:** [How to avoid]
- **Detection:** [Early warning signs]
- **Response:** [Contingency plan]
- **Review date:** [When to reassess]

[Repeat for each high-priority risk]

### Go/No-Go Assessment

**Critical risks (L×I ≥ 20):** [Count]
**High risks (L×I 13-19):** [Count]
**Acceptable risk profile?** [Yes/No]
**Recommendation:** [Proceed / Proceed with mitigations / Reconsider]

### Pre-Mortem Learnings

[Key insights from the exercise]
[Assumptions challenged]
[Information gaps identified]
```

---

## Common Failure Patterns for AI/Software Projects

Use these as prompts during brainstorming:

### Technical Failures
- Integration with existing systems failed
- Performance didn't scale as expected
- Data quality issues undermined results
- Security vulnerability discovered
- Technical debt accumulated faster than expected
- Key dependency deprecated or changed

### People Failures
- Key team member left mid-project
- Skills gap larger than anticipated
- Stakeholder lost interest/sponsorship
- Team resistance to new approach
- Communication breakdown between teams

### Process Failures
- Timeline was unrealistic from start
- Dependencies weren't properly mapped
- Testing was inadequate
- Change management neglected
- Documentation insufficient for handoff

### External Failures
- Market conditions changed
- Competitor released similar solution
- Regulatory requirements shifted
- Vendor went out of business
- Customer needs evolved

### Assumption Failures
- "Users will adopt it" — they didn't
- "It will save time" — it added complexity
- "We can do it in-house" — we couldn't
- "The API will be stable" — it wasn't
- "Management will support it" — priorities changed

---

## Integration with Other Frameworks

### With Cynefin
- **Complex domain:** Extensive pre-mortem essential (unknown unknowns)
- **Complicated domain:** Standard pre-mortem
- **Clear domain:** Brief pre-mortem or skip
- **Chaotic domain:** Skip initially; do post-stabilization

### With Decision Matrix
Run pre-mortem AFTER matrix identifies preferred option:
1. Matrix → Winner selected
2. Pre-mortem → Stress-test winner
3. If acceptable risks → Proceed
4. If unacceptable risks → Reconsider options

### With RAPID
- **R** typically facilitates pre-mortem
- **I** participants contribute risk identification
- **D** ultimately decides if risk profile is acceptable

---

## Agent Application

When an agent conducts a pre-mortem:

1. Confirm a decision/option has been selected
2. Set future timeframe (typically 6 months - 1 year)
3. Generate failure scenarios across categories
4. Score L×I for each risk
5. Identify high-priority risks (L×I ≥ 13)
6. Propose mitigations for high-priority
7. Provide go/no-go recommendation

**Output should include:**
- Risk register with L×I scores
- Mitigation plans for critical/high risks
- Overall risk profile assessment
- Clear recommendation

**Pre-mortem is NOT complete until:**
- At least 10 distinct risks identified
- Each risk has L and I scores
- High-priority risks have mitigation plans
- Go/no-go recommendation provided

---

## References

- Klein, G. "Performing a Project Premortem" (HBR, 2007)
- Klein, G. "The Power of Intuition" (2003)
- Mitchell, D.J. et al. "Back to the future: Temporal perspective in the explanation of events" (1989)
