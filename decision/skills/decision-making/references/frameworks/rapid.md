# RAPID Decision Framework

> Role assignment framework ensuring clear ownership and accountability in decisions.

## The Five Roles

### R — Recommend

**Question:** Who gathers facts, analyzes options, and proposes a course of action?

**Responsibilities:**
- Collect relevant data
- Analyze options objectively
- Present recommendation with supporting rationale
- Flag risks and trade-offs
- Does NOT make final decision

**Characteristics:**
- Usually closest to the work
- Has domain knowledge
- May be individual or team
- Should have skin in the game

---

### A — Agree (Veto Power)

**Question:** Who has formal authority to block the decision?

**Responsibilities:**
- Review for compliance, legal, or regulatory issues
- Can formally block implementation
- Must provide reasons for disagreement
- Should be used sparingly

**Characteristics:**
- Typically legal, compliance, security, finance
- Veto is binary (agree or disagree)
- NOT for "I would do it differently"
- Empty for most decisions

**Warning:** Too many A's = gridlock. Reserve for genuine compliance/legal requirements.

---

### P — Perform

**Question:** Who executes after the decision is made?

**Responsibilities:**
- Implement the decision
- Execute according to agreed plan
- Raise blockers discovered during implementation
- Does NOT revisit the decision

**Characteristics:**
- May be same person as R
- Often a team rather than individual
- Must accept D's decision once made

---

### I — Input

**Question:** Who should be consulted before deciding?

**Responsibilities:**
- Provide expertise, perspective, or context
- Offer opinions when asked
- Cannot block decision
- Should be heard, not necessarily followed

**Characteristics:**
- Stakeholders affected by outcome
- Domain experts
- Can be broad group
- Not accountable for decision

**Warning:** Too many I's = analysis paralysis. Keep focused.

---

### D — Decide

**Question:** Who makes the final call?

**Responsibilities:**
- Makes the final decision
- Accountable for outcome
- Resolves disagreements
- Commits resources
- Signs off on go/no-go

**Characteristics:**
- **MUST BE ONE PERSON** (never a group)
- Has authority matching scope
- Willing to be accountable
- Cannot delegate the decision itself

---

## Critical Rules

### Rule 1: ONE D Always

Every decision has exactly ONE Decide owner. Never:
- "The team decides"
- "Leadership decides"
- "We'll figure it out together"

If no clear D → elevate to find one.

### Rule 2: A is Rare

Agreement/veto should only exist for:
- Legal requirements
- Regulatory compliance
- Security mandates
- Financial thresholds requiring approval

NOT for:
- Style preferences
- Risk aversion
- Political cover

### Rule 3: R Does the Work

Recommender does heavy lifting. D shouldn't need to repeat analysis.

### Rule 4: P Accepts D

Once D decides, P implements without relitigating. Disagreement happens before D decides, not after.

### Rule 5: I Gets Heard, Not Final Say

Input contributors are consulted, their input considered, but they don't control outcome.

---

## RAPID Assignment Template

```markdown
## RAPID for: [Decision Title]

| Role | Person/Team | Notes |
|------|-------------|-------|
| R | | Who analyzes and recommends? |
| A | | Veto authority (if any)? |
| P | | Who implements? |
| I | | Who to consult? |
| D | | WHO MAKES FINAL CALL? |

**D Authority Level:** [Budget/Scope limits for this D]
**Escalation Path:** If D cannot resolve, escalate to: [Higher D]
```

---

## Common Patterns by Decision Type

### Technical Architecture
- **R:** Lead engineer or architect
- **A:** Security (if applicable), rarely used
- **P:** Engineering team
- **I:** Affected teams, DevOps, Product
- **D:** Tech lead or CTO (based on scope)

### Feature Prioritization
- **R:** Product manager
- **A:** None typically
- **P:** Engineering team
- **I:** Sales, Customer Success, Engineering
- **D:** Product lead or CPO

### Budget Allocation
- **R:** Department head
- **A:** Finance (above threshold)
- **P:** Department teams
- **I:** Affected stakeholders
- **D:** Executive owner or CEO

### Vendor Selection
- **R:** Procurement or project lead
- **A:** Legal (contract terms), Security (data handling)
- **P:** Implementation team
- **I:** End users, Finance, IT
- **D:** Budget owner

### Hiring
- **R:** Hiring manager
- **A:** HR (compliance only)
- **P:** HR (offer process), Hiring manager (onboarding)
- **I:** Interview panel, Team
- **D:** Hiring manager (usually) or their manager

### Incident Response
- **R:** On-call engineer
- **A:** None during crisis
- **P:** Incident team
- **I:** Affected stakeholders
- **D:** Incident commander

---

## Integration with Cynefin

| Cynefin Domain | RAPID Adaptation |
|----------------|------------------|
| **Clear** | Standard RAPID, D often delegated low |
| **Complicated** | Emphasize R and I (need expert input) |
| **Complex** | D must be comfortable with uncertainty; multiple R probes |
| **Chaotic** | Centralize D authority, minimize I consultation |

---

## Common Failures

### Multiple D's
**Symptom:** Decision never gets made, endless meetings
**Fix:** Escalate to single accountable person

### Missing D
**Symptom:** Everyone assumes someone else is deciding
**Fix:** Explicitly assign before proceeding

### A for Everything
**Symptom:** Every stakeholder has veto, nothing moves
**Fix:** Reserve A for true compliance requirements

### R Without Authority
**Symptom:** Recommender can't access information or resources
**Fix:** Ensure R has what they need to do proper analysis

### Ignoring I
**Symptom:** Stakeholders feel blindsided, resistance to implementation
**Fix:** Document how input was considered (even if not followed)

### P Relitigating
**Symptom:** Implementers revisit decision during execution
**Fix:** Clear escalation path if P discovers new blocking info

---

## Agent Application

When an agent needs to assign RAPID:

1. Identify decision scope and type
2. Ask: "Who is accountable if this fails?" → That's your D
3. Ask: "Who has the data to analyze this?" → That's your R
4. Ask: "Who must execute this?" → That's your P
5. Ask: "Who would be angry if not consulted?" → Those are your I's
6. Ask: "Are there legal/regulatory blockers?" → Only those are A's

If D is unclear, the decision is not ready to be made. Escalate.

---

## References

- Bain & Company: RAPID Decision Making
- Rogers, P. & Blenko, M. "Who Has the D?" (HBR, 2006)
