# Bridge: JTBD → PR/FAQ

## Direct Mapping

| JTBD Artifact | PR/FAQ Section | How to use |
|---------------|----------------|-----------|
| Primary job statement | Problem (opening paragraph) | The job describes the problem from the customer's point of view, not the solution's |
| Push (Forces of Progress) | Why now? | High Push = real urgency; cite evidence |
| Pull (Forces of Progress) | Value proposition | What the customer already recognizes as attractive |
| Anxiety (Forces of Progress) | Risks and mitigation | What the solution needs to explicitly address |
| Job map — critical steps | Key capabilities | Prioritize features that address steps with the highest opportunity score |
| Opportunity score | Priority justification | High score = important problem poorly served today |
| Job stories | Customer Voice | Use real quotes when available; `[JTBD-DERIVED]` when inferred |

## Usage Rules

1. **Job statement → Problem:** Rewrite the PR/FAQ problem section in job format. Not "the product needs X", but "the customer, when Y, wants Z, in order to achieve W".

2. **Customer Voice:** Use real quotes from interviews when available. If the job was inferred from data (analysis mode), mark with `[JTBD-DERIVED: inferred from N feedback entries/interviews]`. Never fabricate quotes.

3. **Opportunity score as a filter:** Features that do not address the top 3 jobs by opportunity score need an explicit justification to be included in scope.

4. **Forces → Adoption strategy:** Anxiety and Habit identified must appear in the PR/FAQ as risks and in the execution plan as onboarding attention points.

## Integration Example

**Job statement:**
> When I need to onboard a new service provider for a high-value client engagement,
> I want to confirm their qualifications meet requirements,
> So I can start the engagement without compliance exposure.

**In the PR/FAQ — Problem:**
> Organizations that need to onboard service providers for high-value engagements today rely on manual processes or third-party checks that can take up to 48 hours. The core job — confirming a provider's qualifications within the engagement SLA — is underserved. [Data needed: current P80 SLA, target SLA].

**In the PR/FAQ — Customer Voice:**
> "I needed to know if the provider was cleared before we signed the contract. There was no way to wait two days." — [Operations Manager, JTBD interview]
