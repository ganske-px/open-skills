# Quick Decision Workflow

> Abbreviated decision process for time-sensitive or lower-stakes decisions.
> ~15-25 minutes vs ~65 minutes for full cycle.

## When to Use

- Time-sensitive decisions (need answer today)
- Lower stakes (easily reversible)
- Domain is clear (not in Disorder)
- Limited options (2-3 choices)
- Stakeholders aligned on criteria
- No complex political dynamics

**Do NOT use quick workflow for:**
- High-stakes or irreversible decisions
- Strategic direction changes
- Decisions requiring extensive buy-in
- Unclear or contested problem framing

---

## Quick Decision Flow

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Quick      │ →   │   Rapid     │ →   │   Light     │ →   │   Action    │
│  Domain     │     │   D Only    │     │   Compare   │     │   Plan      │
│  Check      │     │             │     │             │     │             │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
   (3 min)            (3 min)            (10 min)            (5 min)
```

---

## Phase 1: Quick Domain Check (3 min)

**Question:** "What type of problem is this?"

| If... | Then... |
|-------|---------|
| Known solution exists | Clear → Execute directly |
| Need expert analysis | Complicated → Continue quick flow |
| Experimental/emergent | Complex → Consider if quick flow appropriate |
| Crisis/chaos | Chaotic → Skip to Act immediately |

**Quick classification:**
```
Domain: [Clear/Complicated/Complex/Chaotic]
Confidence: [High/Medium/Low]
```

**If Low confidence:** Consider full decision cycle instead.

---

## Phase 2: Rapid D Only (3 min)

For quick decisions, focus only on **D** (Decision Maker).

**Questions:**
1. Who will make this call?
2. Do they have authority for this scope?
3. Who needs to know afterward?

**Output:**
```
D (Decide): [Name]
Inform after: [Names]
```

Skip full RAPID mapping unless role confusion exists.

---

## Phase 3: Light Comparison (10 min)

### Option A: Quick Matrix (if 3+ options)

Use simplified 3-criteria matrix:

```markdown
| Criterion | Option A | Option B | Option C |
|-----------|----------|----------|----------|
| [Main criterion 1] | +/=/- | +/=/- | +/=/- |
| [Main criterion 2] | +/=/- | +/=/- | +/=/- |
| [Main criterion 3] | +/=/- | +/=/- | +/=/- |
| **Quick winner** | | | |
```

Scoring:
- **+** = Better than alternatives
- **=** = About equal
- **-** = Worse than alternatives

### Option B: Pros/Cons (if 2 options)

```markdown
**Option A: [Name]**
+ [Pro 1]
+ [Pro 2]
- [Con 1]
- [Con 2]

**Option B: [Name]**
+ [Pro 1]
+ [Pro 2]
- [Con 1]
- [Con 2]

**Lean:** [Option]
**Key differentiator:** [What makes the difference]
```

### Quick Risk Check

Instead of full pre-mortem, ask one question:

> "If this fails in 3 months, what's the most likely reason?"

Document top 2-3 risks only:
```markdown
**Top Risks:**
1. [Risk 1] - Mitigation: [Brief]
2. [Risk 2] - Mitigation: [Brief]
```

---

## Phase 4: Action Plan (5 min)

Define immediate next steps:

```markdown
**Decision:** [The choice]
**Why:** [One sentence rationale]

**Next Steps:**
1. [Action 1] - [Owner] - [By when]
2. [Action 2] - [Owner] - [By when]

**Check-in:** [When to review if working]
**Rollback trigger:** [What would cause us to reverse]
```

---

## Quick Decision Template

```markdown
# Quick Decision: [Title]

**Date:** YYYY-MM-DD
**D:** [Decision maker]
**Time constraint:** [Why quick needed]

## Domain Check
**Type:** [Clear/Complicated/Complex]
**Confidence:** [High/Medium/Low]

## Options
1. [Option A] - [One line description]
2. [Option B] - [One line description]

## Quick Comparison
| Criterion | Opt A | Opt B |
|-----------|-------|-------|
| [Main 1]  | +/-/= | +/-/= |
| [Main 2]  | +/-/= | +/-/= |
| [Main 3]  | +/-/= | +/-/= |

## Top Risks
1. [Risk 1] → [Mitigation]
2. [Risk 2] → [Mitigation]

## Decision
**Choice:** [Option selected]
**Rationale:** [One sentence]

## Action
| Step | Owner | By |
|------|-------|-----|
| | | |

**Review:** [Date]
**Rollback if:** [Condition]
```

---

## Skip Conditions

These conditions allow skipping parts of even the quick workflow:

### Skip Domain Check When:
- You're certain it's Clear or Complicated
- Same type of decision has been made before

### Skip Comparison When:
- One option is obviously superior
- Decision is primarily about timing, not alternatives

### Skip Risk Check When:
- Decision is easily reversible (< 1 day to undo)
- Failure impact is minimal

---

## Escalation to Full Cycle

Upgrade to full decision cycle if during quick process you discover:
- Domain is actually Complex or ambiguous
- More than 3 viable options emerge
- Stakeholders disagree on criteria
- High-impact risk surfaces
- Political dynamics require formal process
- D asks for more thorough analysis

---

## Time Comparison

| Phase | Quick | Full |
|-------|-------|------|
| Domain classification | 3 min | 10 min |
| Role assignment | 3 min | 10 min |
| Option comparison | 10 min | 20 min |
| Risk assessment | (included) | 15 min |
| Action planning | 5 min | 10 min |
| **Total** | **~20 min** | **~65 min** |

---

## Agent Guidance

When an agent uses quick decision workflow:

1. Verify time constraint or lower stakes (justify quick approach)
2. Run quick domain check — escalate if Complex/Chaotic
3. Confirm D only — don't map full RAPID
4. Use simplified comparison (3 criteria max)
5. Ask single pre-mortem question
6. Define concrete next steps
7. Set explicit review point

**Quick decision output should fit on one page.**

---

## References

- `./full-decision-cycle.md` - When to escalate
- `../frameworks/cynefin.md` - Domain classification details
- `../frameworks/rapid.md` - Full role assignment if needed
