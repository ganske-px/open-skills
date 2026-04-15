# Full Decision Cycle Workflow

> Complete 5-framework decision process for strategic or high-stakes decisions.

## When to Use

- Strategic decisions with long-term impact
- High-stakes choices (significant cost, risk, or irreversibility)
- Decisions requiring stakeholder buy-in
- Complex situations with multiple viable options
- When documentation and audit trail are important

**Time investment:** ~60-90 minutes for full cycle

---

## The Sequence

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        FULL DECISION CYCLE                               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│   1. CYNEFIN          2. RAPID           3. MATRIX                      │
│   ┌─────────┐        ┌─────────┐        ┌───────────┐                   │
│   │Classify │   →    │ Assign  │   →    │  Compare  │                   │
│   │ Domain  │        │  Roles  │        │  Options  │                   │
│   └─────────┘        └─────────┘        └───────────┘                   │
│   (~10 min)          (~10 min)          (~20 min)                       │
│                                                                          │
│                                                                          │
│   4. PRE-MORTEM      5. OODA                                            │
│   ┌───────────┐      ┌─────────┐                                        │
│   │  Stress   │  →   │ Execute │                                        │
│   │   Test    │      │ & Loop  │                                        │
│   └───────────┘      └─────────┘                                        │
│   (~15 min)          (~10 min setup, then ongoing)                      │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Phase 1: Cynefin Classification (~10 min)

**Goal:** Understand what type of problem this is to choose appropriate response.

### Steps:
1. State the decision to be made
2. Answer classification questions:
   - Is cause-effect obvious?
   - Do best practices exist?
   - How many valid solutions?
   - Can we predict outcomes?
3. Determine domain: Clear, Complicated, Complex, or Chaotic

### Output:
```markdown
**Domain Classification:** [Clear/Complicated/Complex/Chaotic]
**Rationale:** [Why this classification]
**Response Pattern:** [Sense-Categorize-Respond / Sense-Analyze-Respond / Probe-Sense-Respond / Act-Sense-Respond]
```

### Checkpoint:
- If **Clear:** Consider skipping to OODA (execute known solution)
- If **Chaotic:** Skip to OODA immediately (stabilize first)
- If **Complicated/Complex:** Continue full cycle

---

## Phase 2: RAPID Assignment (~10 min)

**Goal:** Establish clear ownership and accountability.

### Steps:
1. Identify who should fill each role
2. Verify ONE D (decision maker)
3. Confirm A roles are necessary (legal/compliance only)
4. Document P (implementers) and I (input sources)

### Output:
```markdown
**RAPID Assignment:**
- R (Recommend): [Name/Role]
- A (Agree/Veto): [Name/Role or "None"]
- P (Perform): [Name/Role]
- I (Input): [Names/Roles]
- D (Decide): [ONE Name/Role]

**Escalation Path:** [If D cannot resolve]
```

### Checkpoint:
- D must be a single person
- A should be empty for most decisions
- R should have access to information needed

---

## Phase 3: Decision Matrix (~20 min)

**Goal:** Objectively compare options against weighted criteria.

### Steps:
1. List 2-5 viable options
2. Identify 4-8 evaluation criteria
3. Assign weights (total 100%)
4. Score each option on each criterion (1-5 scale)
5. Calculate weighted totals
6. Identify winner and analyze sensitivity

### Output:
```markdown
**Options:**
1. [Option A]
2. [Option B]
3. [Option C]

**Matrix Results:**
| Criterion | Weight | Opt A | Opt B | Opt C |
|-----------|--------|-------|-------|-------|
| [Crit 1]  | X%     |       |       |       |
| [Crit 2]  | X%     |       |       |       |
| ...       |        |       |       |       |
| **Total** | 100%   | X.XX  | X.XX  | X.XX  |

**Winner:** [Option] with score [X.XX]
**Margin:** [Close/Clear/Decisive]
**Sensitivity:** [Stable/Sensitive to X]
```

### Checkpoint:
- If margin is very close, consider hybrid options
- Note any criteria where losing option scored higher

---

## Phase 4: Pre-Mortem (~15 min)

**Goal:** Stress-test the leading option by imagining failure.

### Steps:
1. Set future failure scenario (6-12 months out)
2. Generate failure reasons (aim for 10+)
3. Score each risk: Likelihood × Impact
4. Prioritize (L×I ≥ 13 = high priority)
5. Develop mitigations for high-priority risks
6. Make go/no-go recommendation

### Output:
```markdown
**Failure Scenario:** [Description]
**Future Date:** [When]

**Top Risks:**
| Risk | L | I | L×I | Mitigation |
|------|---|---|-----|------------|
| [Risk 1] | | | | |
| [Risk 2] | | | | |
| [Risk 3] | | | | |

**Critical Risks (L×I ≥ 20):** [Count]
**High Risks (L×I 13-19):** [Count]
**Risk Assessment:** [Acceptable/Concerning/Unacceptable]
**Recommendation:** [Proceed/Proceed with mitigations/Reconsider]
```

### Checkpoint:
- If any L×I ≥ 20 without mitigation, reconsider
- If pre-mortem surfaces fundamental issues, may return to Matrix

---

## Phase 5: OODA Setup (~10 min)

**Goal:** Establish execution framework and iteration plan.

### Steps:
1. Define first action steps
2. Set observation points and metrics
3. Establish loop cadence
4. Define pivot triggers

### Output:
```markdown
**Initial Actions:**
1. [Action 1] - Owner: [Name] - By: [Date]
2. [Action 2] - Owner: [Name] - By: [Date]
3. [Action 3] - Owner: [Name] - By: [Date]

**Observation Metrics:**
- [Metric 1]: Target [X], measured [how often]
- [Metric 2]: Target [X], measured [how often]

**Loop Cadence:** [Daily/Weekly/Monthly check-ins]
**Pivot Triggers:** [Conditions that would cause us to reconsider]
**First Review:** [Date]
```

---

## Complete Decision Record Template

```markdown
# Decision Record: [Title]

**Date:** YYYY-MM-DD
**Domain:** [Clear/Complicated/Complex/Chaotic]
**Decision Maker (D):** [Name/Role]

## 1. Context

[What prompted this decision? What constraints exist?]

## 2. Cynefin Classification

**Domain:** [Classification]
**Response Pattern:** [Pattern]
**Rationale:** [Why]

## 3. RAPID Assignment

| Role | Assigned To | Notes |
|------|-------------|-------|
| R | | |
| A | | |
| P | | |
| I | | |
| D | | |

## 4. Options Considered

1. **[Option A]** - [Description]
2. **[Option B]** - [Description]
3. **[Option C]** - [Description]

## 5. Decision Matrix

| Criterion | Weight | Opt A | Opt B | Opt C |
|-----------|--------|-------|-------|-------|
| | | | | |
| **TOTAL** | 100% | | | |

**Winner:** [Option] with [Score]

## 6. Pre-Mortem Analysis

### Top Risks

| Risk | L | I | L×I | Mitigation |
|------|---|---|-----|------------|
| | | | | |

### Risk Assessment
[Overall risk profile assessment]

## 7. Decision

**Choice:** [The decision made]
**Rationale:** [Why this choice]
**Confidence:** [High/Medium/Low]

## 8. Execution Plan (OODA)

### Initial Actions
| Action | Owner | Due |
|--------|-------|-----|
| | | |

### Metrics
| Metric | Target | Frequency |
|--------|--------|-----------|
| | | |

### Loop Cadence
[How often to review]

### Pivot Triggers
[What would cause reconsideration]

## 9. Success Criteria

[How will we know this decision was correct?]

## 10. Review Date

**First Review:** [Date]
**Retrospective:** [Date]
```

---

## Entry Points

Not every decision needs to start at Phase 1:

| Starting Point | When to Use |
|----------------|-------------|
| **Cynefin** | Unclear what kind of problem this is |
| **RAPID** | Know the domain, need role clarity |
| **Matrix** | Roles clear, need to compare options |
| **Pre-Mortem** | Decision selected, need to stress-test |
| **OODA** | Decision made, need execution structure |

---

## Time Allocation Summary

| Phase | Full Cycle | Abbreviated |
|-------|------------|-------------|
| Cynefin | 10 min | 3 min |
| RAPID | 10 min | 3 min |
| Matrix | 20 min | 8 min |
| Pre-Mortem | 15 min | 5 min |
| OODA Setup | 10 min | 5 min |
| **Total** | **~65 min** | **~24 min** |

---

## References

See individual framework files for detailed guidance:
- `../frameworks/cynefin.md`
- `../frameworks/rapid.md`
- `../frameworks/decision-matrix.md`
- `../frameworks/pre-mortem.md`
- `../frameworks/ooda.md`
