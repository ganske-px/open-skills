# Example: Job Map — Evaluating and Onboarding a New Service Provider

> This is a filled-in job map example for a generic B2B operations context. Use it as a reference for format, depth, and quality standards. Adapt to your own domain.

**Main job:**
> When I receive a request to bring on a new service provider for a client engagement,
> I want to assess their qualifications with confidence and speed,
> So I can start the engagement without compliance exposure or unnecessary delay.

**Primary persona:** Operations Manager (responsible for vendor onboarding)

---

## Job Map — 8 Steps

| Step | Current state | Pains identified | Evidence | What the proposed solution does |
|------|-------------|-----------------|----------|---------------------------------|
| 1. Define | Manager receives the request and selects a provider by intuition — who is available, who "worked well before" | No visibility into the provider's qualification profile before submitting; wrong choice leads to rework | User feedback: "I need to see the basic profile before I commit to the evaluation process, otherwise I always end up starting over" | Predictive fit score visible BEFORE submission — manager sees confidence level and decides whether to proceed |
| 2. Locate | Gathers provider documents (ID, certifications, references) and checks client requirements from multiple sources | Requirements vary by client; data is scattered across multiple systems | Feedback: "the platform asks for documents that don't make sense for this type of engagement" | Score already uses enriched data from the engine — manager does not need to gather everything manually |
| 3. Prepare | Fills out the evaluation request form and submits | No predictive feedback; alternative candidates disappear once one is selected | Feedback: "when we select one candidate, the others vanish — they should stay available" | Score is visible at preparation time — manager can pivot to another candidate without rework |
| 4. Confirm | Tries to mentally confirm the provider will pass — relies on intuition and experience | No pre-check mechanism; new managers have no reference point; anxiety before submitting | [NO CUSTOMER VOICE — inferred from flow: there is no pre-check before submission] | The score IS the pre-check. High confidence = submit. Low confidence = find another candidate |
| 5. Execute | Evaluation submitted; enrichment engine queries sources, validation engine applies rules | Binary outcome with no gradation; pending cases go to manual review with long SLA | Internal data: average manual review SLA ~50 min; target for automated decision >90% | Probabilistic analysis with configurable threshold — reduces volume of manual reviews |
| 6. Monitor | Tracks status (pending → in review → completed); visibility limited to status, not reason | Does not know how long it will take or why it is pending | [NO CUSTOMER VOICE — collect in interviews with operations managers] | Score gives visibility into the factors driving the assessment, even during processing |
| 7. Modify | If rejected: gives up or tries to correct (updated document, different provider) | No clarity on which data point caused the shortfall; high rework to resubmit another candidate | User feedback about the cycle of submit → reject → delete → restart | Score decomposed by factor — manager sees WHAT caused the issue and whether it is correctable |
| 8. Conclude | Approved → onboarding → engagement starts. Rejected → find another candidate | Result does not feed learning; no history for future decisions; profile is not portable | Identified as a recurring pain in user interviews — portability of past assessments | Score creates a persistent profile — manager sees how a provider's risk profile evolves over time |

---

## Desired Outcomes per Step

| Step | # | Desired Outcome | Dim |
|------|---|----------------|-----|
| Define | 1.1 | Minimize the time it takes to determine which candidate has the highest chance of qualification | F |
| Define | 1.2 | Reduce the likelihood of selecting a candidate who will be rejected | F |
| Define | 1.3 | Increase confidence that the selected candidate is the best available option | E |
| Locate | 2.1 | Minimize the number of data sources the manager needs to consult manually | F |
| Locate | 2.2 | Reduce the likelihood of submitting incomplete documentation | F |
| Prepare | 3.1 | Minimize the time it takes to prepare a submission for a candidate | F |
| Prepare | 3.2 | Reduce the likelihood of wasting effort on a candidate who will be rejected | F |
| Prepare | 3.3 | Avoid the frustration of losing alternative candidates while waiting for a result | E |
| Confirm | 4.1 | Increase confidence that the submission will result in approval before committing | E |
| Confirm | 4.2 | Minimize the anxiety of not knowing the outcome before submitting | E |
| Confirm | 4.3 | Ensure the manager can justify the candidate choice to the client if questioned | S |
| Execute | 5.1 | Minimize the time between submission and final decision | F |
| Execute | 5.2 | Reduce the number of submissions that require manual intervention | F |
| Execute | 5.3 | Increase the percentage of decisions that are fully automated | F |
| Monitor | 6.1 | Minimize the time it takes to identify which submissions are stuck in the pipeline | F |
| Monitor | 6.2 | Reduce the uncertainty about why a submission is pending | E |
| Monitor | 6.3 | Ensure the manager can provide a status update to the client at any time | S |
| Modify | 7.1 | Minimize the effort required to understand what caused a rejection | F |
| Modify | 7.2 | Reduce the time it takes to determine if a rejection is correctable | F |
| Modify | 7.3 | Avoid the embarrassment of repeatedly submitting candidates who get rejected | S |
| Conclude | 8.1 | Minimize the time between approval and engagement start | F |
| Conclude | 8.2 | Increase the ability to reuse a past qualification assessment for future engagements | F |
| Conclude | 8.3 | Ensure the manager can demonstrate a rigorous approval process to auditors | S |

**Distribution:** 14 Functional, 5 Emotional, 4 Social.

---

## Priority Steps

| Step | Pain | Current satisfaction | Priority |
|------|------|---------------------|----------|
| 1. Define | High — operates without predictability | Low | CRITICAL |
| 4. Confirm | High — no pre-check, submission is a guess | Low | CRITICAL |
| 5. Execute | High — long SLA, binary result | Medium | CRITICAL |
| 7. Modify | High — rework, no clarity on cause | Low | CRITICAL |
| 3. Prepare | Medium — rework when candidate is wrong | Medium | RELEVANT |
| 6. Monitor | Medium — limited visibility | Medium | RELEVANT |
| 2. Locate | Medium — data scattered across systems | Medium | MODERATE |
| 8. Conclude | Low — works, but without learning | Medium | MODERATE |

---

## What This Example Demonstrates

1. **Real evidence at each step** — feedback with literal quotes, internal data with source. Where there is no evidence: `[NO CUSTOMER VOICE]`.
2. **Desired outcomes in Strategyn format** — `[Direction] + [metric] + [object] + [context]`. Solution-independent.
3. **Three dimensions tagged (F/E/S)** — mostly functional, but emotional and social outcomes appear at the most critical steps (Define, Confirm, Modify).
4. **Provocation on dimensions:** emotional outcomes (confidence, anxiety) are as or more relevant than functional ones (speed, rework) — differentiation lives there.
