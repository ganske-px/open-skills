---
name: decision-making
description: |
  Unified decision-making skill that helps agents identify decision moments and apply appropriate frameworks.

  Triggers: "help me decide", "should I/we", "which option", "compare X and Y",
  "what type of problem", "who should decide", "what could go wrong", "stress-test this",
  "how do we iterate", "decision needed", "weighing options"

  Provides: Cynefin classification, RAPID ownership, Decision Matrix comparison,
  Pre-Mortem risk analysis, OODA execution loops
---

# Decision-Making Skill

## Quick Router

```
USER NEED                          → FRAMEWORK              → REFERENCE
─────────────────────────────────────────────────────────────────────────
"What type of problem is this?"    → Cynefin                → frameworks/cynefin.md
"Who should decide?"               → RAPID                  → frameworks/rapid.md
"Compare options objectively"      → Decision Matrix        → frameworks/decision-matrix.md
"What could go wrong?"             → Pre-Mortem             → frameworks/pre-mortem.md
"How do we execute/iterate?"       → OODA                   → frameworks/ooda.md
"Full strategic decision"          → Full Cycle             → workflows/full-decision-cycle.md
"Quick decision needed"            → Quick Decision         → workflows/quick-decision.md
```

## Framework Sequence

For comprehensive decisions, apply frameworks in this order:

```
┌─────────┐    ┌─────────┐    ┌──────────┐    ┌───────────┐    ┌──────┐
│ CYNEFIN │ →  │  RAPID  │ →  │  MATRIX  │ →  │ PRE-MORTEM│ →  │ OODA │
└─────────┘    └─────────┘    └──────────┘    └───────────┘    └──────┘
  Classify       Assign         Compare        Stress-test      Execute
  Domain        Ownership       Options        Decision         & Iterate
```

**Why this order:**
1. **Cynefin** determines appropriate response pattern
2. **RAPID** clarifies who owns what roles
3. **Matrix** objectively compares if multiple options exist
4. **Pre-Mortem** stress-tests the leading choice
5. **OODA** guides execution and iteration

## Domain Quick Reference

### Cynefin Domains → Response Patterns

| Domain | Characteristics | Response | Agent Behavior |
|--------|-----------------|----------|----------------|
| **Clear** | Known knowns, best practices exist | Sense→Categorize→Respond | Execute established procedure |
| **Complicated** | Known unknowns, expertise needed | Sense→Analyze→Respond | Consult experts, multiple valid solutions |
| **Complex** | Unknown unknowns, emergent patterns | Probe→Sense→Respond | Safe-to-fail experiments |
| **Chaotic** | No patterns, crisis | Act→Sense→Respond | Stabilize first, analyze later |
| **Disorder** | Domain unclear | → Gather info to classify | Ask clarifying questions |

### RAPID Roles Summary

| Role | Question | Accountability |
|------|----------|----------------|
| **R**ecommend | Who analyzes and proposes? | Provide data, options, recommendation |
| **A**gree | Who has formal veto? | Use sparingly; regulatory/legal |
| **P**erform | Who implements? | Execute after D decides |
| **I**nput | Who should be consulted? | Provide perspective, no veto |
| **D**ecide | Who makes final call? | ONE person, accountable for outcome |

### Decision Matrix Quick Setup

```
Option      | Criterion 1 (w:X) | Criterion 2 (w:Y) | ... | Weighted Total
------------|-------------------|-------------------|-----|---------------
Option A    | Score × Weight    | Score × Weight    |     | Sum
Option B    | Score × Weight    | Score × Weight    |     | Sum
```

### Pre-Mortem Prompt

> "Imagine it's 6 months from now. This decision has failed spectacularly.
> What went wrong? Why did we not see it coming?"

### OODA Loop

```
    ┌─────────────────────────────────────────┐
    │                  ORIENT                  │
    │  (Most critical: mental models, biases) │
    └─────────────────────────────────────────┘
           ↗                           ↘
    ┌─────────┐                    ┌─────────┐
    │ OBSERVE │                    │ DECIDE  │
    └─────────┘                    └─────────┘
           ↖                           ↙
              ┌─────────────────────┐
              │        ACT          │
              └─────────────────────┘
                        ↓
                     [LOOP]
```

## Decision Detection

**Explicit signals** (user states decision needed):
- "help me decide", "should I/we", "which option", "what's the best approach"

**Implicit signals** (context suggests decision moment):
- Multiple viable paths mentioned
- Trade-offs being discussed
- Stakeholder disagreement
- Uncertainty about next steps
- Resource allocation questions

**Suppress skill when:**
- User wants information only, not decision support
- Decision already made, execution guidance needed → use OODA only
- Simple binary with obvious answer

See: `references/detection/decision-triggers.md`

## Output Format: Decision Record

Every significant decision should produce a record:

```markdown
# Decision Record: [Title]

**Date:** YYYY-MM-DD
**Domain:** Clear | Complicated | Complex | Chaotic
**Decision Maker (D):** [Name/Role]

## Context
[What prompted this decision? What constraints exist?]

## Options Considered
1. [Option A] - [Brief description]
2. [Option B] - [Brief description]
3. [Option C] - [Brief description]

## Analysis
[Matrix scores or key comparisons]

## Risks Identified (Pre-Mortem)
| Risk | Likelihood (1-5) | Impact (1-5) | L×I | Mitigation |
|------|------------------|--------------|-----|------------|
| ...  | ...              | ...          | ... | ...        |

## Decision
[The choice made and rationale]

## RAPID Assignment
- **R:** [Who recommended]
- **A:** [Who had veto, if any]
- **P:** [Who will implement]
- **I:** [Who was consulted]
- **D:** [Who decided]

## Success Criteria
[How will we know this worked?]

## Review Date
[When to evaluate outcomes]
```

## Anti-Patterns to Avoid

See: `references/anti-patterns.md`

**Most common:**
- Skipping Cynefin classification (treating complex as complicated)
- Multiple "D" owners in RAPID (decision by committee)
- Analysis paralysis in Matrix (too many criteria)
- Superficial Pre-Mortem (only obvious risks)
- Skipping Orient phase in OODA

## Usage Examples

### Example 1: Strategic Choice
```
User: "Should we build or buy the analytics platform?"

Agent:
1. Load cynefin.md → Classify as Complicated (multiple valid solutions, expertise needed)
2. Load rapid.md → Assign roles (CTO as D, Engineering as R, Finance as I)
3. Load decision-matrix.md → Compare build vs buy on criteria
4. Load pre-mortem.md → Stress-test leading option
5. Generate Decision Record
```

### Example 2: Quick Tactical
```
User: "Which testing framework should we use?"

Agent:
1. Load quick-decision.md → Abbreviated process
2. Quick Matrix comparison
3. Brief Decision Record
```

### Example 3: Crisis
```
User: "Production is down, multiple possible causes"

Agent:
1. Load cynefin.md → Recognize Chaotic domain
2. Skip analysis frameworks
3. Load ooda.md → Act first to stabilize, then investigate
```

## References

- `references/frameworks/cynefin.md` - Domain classification
- `references/frameworks/rapid.md` - Ownership assignment
- `references/frameworks/decision-matrix.md` - Option comparison
- `references/frameworks/pre-mortem.md` - Risk stress-testing
- `references/frameworks/ooda.md` - Execution loop
- `references/workflows/full-decision-cycle.md` - Complete process
- `references/workflows/quick-decision.md` - Abbreviated version
- `references/detection/decision-triggers.md` - When to activate
- `references/anti-patterns.md` - Common mistakes
