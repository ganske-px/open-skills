# Example: Opportunity Score — Evaluating and Onboarding a New Service Provider

> This is a filled-in opportunity score calculated from desired outcomes of a job map. All scores are qualitative estimates — marked as `[ESTIMATED]`. Use it as a reference for format and analysis.

**Main job:**
> When I receive a request to bring on a new service provider for a client engagement,
> I want to assess their qualifications with confidence and speed,
> So I can start the engagement without compliance exposure or unnecessary delay.

**Method:** Qualitative estimate (feedback, technical context, flow analysis)
**`[ESTIMATED — validate with quantitative importance/satisfaction survey]`**

---

## Scores by Desired Outcome

| Step | # | Desired Outcome | Imp | Sat | Score | Prior. |
|------|---|----------------|-----|-----|-------|--------|
| Define | 1.1 | Minimize the time to determine which candidate has the highest chance of qualification | 9 | 2 | 16 | High |
| Define | 1.2 | Reduce the likelihood of selecting a candidate who will be rejected | 9 | 3 | 15 | High |
| Define | 1.3 | Increase confidence that the selected candidate is the best available option (**E**) | 8 | 2 | 14 | High |
| Locate | 2.1 | Minimize data sources the manager needs to consult manually | 6 | 5 | 7 | Mod. |
| Locate | 2.2 | Reduce the likelihood of submitting incomplete documentation | 7 | 4 | 10 | Rel. |
| Prepare | 3.2 | Reduce the likelihood of wasting effort on a candidate who will be rejected | 9 | 2 | 16 | High |
| Prepare | 3.3 | Avoid the frustration of losing alternative candidates while waiting (**E**) | 8 | 2 | 14 | High |
| Confirm | 4.1 | Increase confidence that submission will result in approval before committing (**E**) | 9 | 1 | 17 | High |
| Confirm | 4.2 | Minimize the anxiety of not knowing the outcome before submitting (**E**) | 8 | 1 | 15 | High |
| Confirm | 4.3 | Ensure the manager can justify the choice to the client if questioned (**S**) | 8 | 3 | 13 | High |
| Execute | 5.1 | Minimize the time between submission and final decision | 9 | 4 | 14 | High |
| Execute | 5.2 | Reduce submissions that require manual intervention | 9 | 5 | 13 | High |
| Monitor | 6.2 | Reduce the uncertainty about why a submission is pending (**E**) | 7 | 2 | 12 | Rel. |
| Monitor | 6.3 | Ensure the manager can provide a status update to the client (**S**) | 7 | 3 | 11 | Rel. |
| Modify | 7.1 | Minimize the effort to understand what caused a rejection | 9 | 2 | 16 | High |
| Modify | 7.2 | Reduce the time to determine if a rejection is correctable | 8 | 2 | 14 | High |
| Conclude | 8.2 | Increase the ability to reuse a past assessment for future engagements | 8 | 1 | 15 | High |

*Table reduced to the most relevant outcomes (score ≥ 10 or dimension insight). The full job map contains 23 outcomes.*

---

## Top 5 Opportunities

| # | Outcome | Step | Score | Why it matters |
|---|---------|------|-------|----------------|
| 1 | Confidence before committing | Confirm | 17 | No pre-check exists. Manager submits and hopes. This is the sharpest gap. |
| 2 | Determine best candidate | Define | 16 | Manager chooses in the dark. A fit score before submission inverts the dynamic. |
| 3 | Avoid wasted effort on rejected candidate | Prepare | 16 | Most frequently articulated pain in feedback — the submit-reject-restart cycle. |
| 4 | Understand rejection cause | Modify | 16 | Binary result with no decomposition. Manager cannot tell if the issue is correctable. |
| 5 | Reuse past assessment | Conclude | 15 | Portability of the profile — high effort to reconstruct for repeat engagements. |

---

## Heat Map by Step

| Step | Outcomes | Avg score | Most critical outcome |
|------|----------|-----------|-----------------------|
| Define | 3 | 15.0 | 1.1 — Determine best candidate (16) |
| Confirm | 3 | 15.0 | 4.1 — Confidence before committing (17) |
| Modify | 3 | 14.0 | 7.1 — Understand rejection cause (16) |
| Prepare | 3 | 13.0 | 3.2 — Avoid wasted effort (16) |
| Execute | 3 | 12.7 | 5.1 — Time to decision (14) |
| Monitor | 3 | 11.0 | 6.2 — Reduce uncertainty (12) |
| Conclude | 3 | 10.7 | 8.2 — Reuse assessment (15) |
| Locate | 2 | 8.5 | 2.2 — Incomplete docs (10) |

---

## Analysis by Dimension

| Dimension | # Outcomes | Avg score | Insight |
|-----------|-----------|-----------|---------|
| Functional | 14 | 12.6 | Foundation of the problem — speed, rework, automation |
| Emotional | 5 | 14.8 | **Higher scores than functional** — confidence and anxiety are the sharpest pains |
| Social | 4 | 11.8 | Relevant — justifying decisions to clients and auditors |

**Insight:** Emotional outcomes average 14.8 vs. 12.6 for functional. Differentiation is not only in "approving faster" (functional) — it is in making the manager feel **confident** in the decision (emotional). A solution that resolves speed but not anxiety leaves an opening for competitors.

---

## Gaps

- **`[DATA NEEDED: quantitative survey]`** — scores are estimates. Validate with a survey of N≥30 operations managers.
- **`[NO CUSTOMER VOICE]`** at the Confirm and Monitor steps — evidence inferred from flow analysis, not interviews.
- Outcome 8.2 (reuse) has a high score but overlaps with a related initiative — verify whether they should be scoped together.

---

## What This Example Demonstrates

1. **Outcomes as the scoring unit** — not entire steps. The "Prepare" step has 3 outcomes with scores ranging from 9 to 16 — a step average hides the real opportunity.
2. **Heat map** — quick view of where the gaps are by step. Define and Confirm lead.
3. **Dimension analysis** — shows that emotional outcomes (E) are more underserved than functional ones (F). An essential provocation for PMs who default to feature-thinking.
4. **Explicit gaps** — every score is `[ESTIMATED]`, customer voice gaps are flagged, cross-initiative overlap is identified.
5. **Formula applied:** `Score = Importance + max(Importance - Satisfaction, 0)`. Score 17 = importance 9 + (9-1) = maximum gap.
