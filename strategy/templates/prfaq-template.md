# PR/FAQ Template — Product Initiatives

The PR/FAQ is the minimum document required to start a product initiative. It precedes any technical spec, wireframe, or sprint planning. It can (and should) start incomplete — but every gap must be explicitly marked.

**Non-negotiable rules:**
- `[DATA NEEDED: ...]` — use whenever a data point is missing. Never invent.
- Real proxy metrics are accepted, as long as confidence is declared.
- **Customer voice is required.** Use real quotes from interviews, surveys, comments, or support tickets. If none are available, write `[NO CUSTOMER VOICE — required before advancing]` and treat it as a blocker.
- **Never invent customer quotes.** A false quote is worse than no quote.
- The document is self-contained: anyone must understand it without prior context.

---

# PR/FAQ: [Initiative Name]

**Status:** [draft | in-review | approved | in-progress | completed | paused]
**Phase:** [discovery | definition | execution | measurement]
**Owner:** [Name of responsible PM]
**Start date:** YYYY-MM-DD

---

## PART 1 — PRESS RELEASE

*The PR simulates a public announcement of the already-launched product. Write as if it were today, but in the future. One page. Customer language, not internal team language.*

---

### [Product/Feature Name] — [Main benefit in one line]

**[City], [Fictional launch date]** — [Product/feature name] is here for [target audience] who [central problem]. Starting today, [description of what changes in the customer's life in one or two sentences].

**The problem it solves**

[Paragraph describing the current state. What does the customer need to do today? Why is it difficult, expensive, slow, or risky? Quantify if possible — use real data or mark as `[DATA NEEDED]`. Maximum 3-4 sentences.]

**What changes**

[Paragraph describing the solution from the customer's point of view. Do not describe the technology — describe the experience. What can the customer do now that they could not do before? How do they feel? Maximum 3-4 sentences.]

**Customer voice**

> "[Real customer quote, extracted from an interview, survey, comment, or support ticket. Attribute to a generic persona: 'Operations manager at a mid-size company' — never to the customer's real name without authorization.]"

> [NO CUSTOMER VOICE — required before advancing]
> *Use the line above if no real quote is available. Treat as a blocker.*

**Internal voice**

> "[Quote from leadership or PM about what this initiative represents strategically. May be elaborated, but must be real or based on a declared position.]"
> — [Name, title]

**Availability**

[When and for whom will it be available? Gradual rollout? Beta customers? `[DATA NEEDED]` if not defined.]

---

## PART 2 — FAQ

*FAQs deepen what the PR cannot answer. Split into external (customer) and internal (team and leadership) questions. Maximum ~5 pages combined.*

---

### External FAQ — Customer Questions

**Q: Who is this product for?**

[Describe the primary and secondary audience. Which personas benefit most? Which are excluded? Be specific — "companies with more than 50 orders/month" is better than "companies".]

---

**Q: What exactly changes in my day-to-day?**

[Describe the before and after from an operational point of view. Use the current flow vs. the new flow. Be concrete — avoid "easier" without explaining what that means in practice.]

---

**Q: Do I need to do anything to start using it?**

[Migration, configuration, training, onboarding. If not defined: `[DATA NEEDED]`.]

---

**Q: What happens to the current process during the transition?**

[Backward compatibility, coexistence period, impact on historical data. If not defined: `[DATA NEEDED]`.]

---

**Q: [Domain-specific question for this initiative]**

[Add FAQs specific to the problem at hand.]

---

### Internal FAQ — Team and Leadership Questions

**Q: Why now? What changed to make this a priority?**

[What is happening in the business, market, or data that makes this the right moment? If the answer is "nothing changed, it was always important", question the prioritization.]

---

**Q: How does this connect to our North Star?**

[Trace the causal path: this initiative → intermediate metric → growth driver → North Star. If the path is indirect or speculative, say so.]

---

**Q: What needs to be true for this initiative to work?**

[List the premises that sustain the logic. For each one, indicate: (1) whether it is a fact or hypothesis; (2) how it would be tested/invalidated. This is the list of implicit risks.]

| Premise | Fact or hypothesis? | How to validate |
|---|---|---|
| [Premise 1] | Hypothesis | [Experiment or data that would confirm it] |
| [Premise 2] | Fact (source: [source]) | — |

---

**Q: What are the biggest risks?**

[Be honest. Technical, adoption, market, and timing risks. For each risk, indicate the estimated probability (high/medium/low) and the planned mitigation.]

| Risk | Probability | Mitigation |
|---|---|---|
| [Risk 1] | High | [What we do if it occurs] |
| [Risk 2] | Medium | [What we do if it occurs] |

---

**Q: What are we explicitly NOT doing in this initiative?**

[Negative scope is as important as positive scope. What is excluded and why? What scope decisions have already been made?]

---

**Q: How will we know it worked?**

[Primary metrics and guardrails. For each metric: current baseline (or `[DATA NEEDED]`), target, timeline, and measurement method.]

| Metric | Baseline | Target | Timeline | How to measure |
|---|---|---|---|---|
| [Primary metric] | [Current data or DATA NEEDED] | [Goal] | [e.g., 90 days post-launch] | [Source] |
| [Guardrail] | [Current data] | Do not regress | Continuous | [Source] |

---

**Q: What is the smallest experiment to validate the riskiest premise?**

[Describe the validation MVP: what would be built, with whom, in how much time, and what the result would tell us about the viability of the full initiative.]

---

## Open Questions

List here the questions that need answers before advancing to execution. For each one, indicate who can answer and what it would unblock.

| Question | Owner | What it would unblock |
|---|---|---|
| [Question 1] | [Name / team] | [What becomes unblocked when answered] |
| [Question 2] | [Name / team] | [What becomes unblocked when answered] |

---

## Related Documents

- [Link to supporting data analysis]
- [Link to qualitative research / interviews]
- [Link to prototype or wireframe]
- [Link to predecessor or successor initiative]

---

## Revision History

| Version | Date | Author | What changed |
|---|---|---|---|
| v0.1 | YYYY-MM-DD | [Name] | Initial draft |
| v0.2 | YYYY-MM-DD | [Name] | [Changes] |
