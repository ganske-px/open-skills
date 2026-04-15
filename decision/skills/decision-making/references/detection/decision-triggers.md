# Decision Triggers

> When to activate the decision-making skill and which framework(s) to invoke.

## Explicit Triggers

User directly signals a decision moment:

### General Decision Signals
- "help me decide"
- "should I/we"
- "which option"
- "what's the best approach"
- "compare X and Y"
- "weighing options"
- "decision needed"
- "what would you recommend"
- "pros and cons of"
- "trade-offs between"

### Cynefin-Specific Triggers
- "what type of problem is this"
- "is this simple or complicated"
- "how should we approach this"
- "what's the right response"
- "is this predictable"
- "do we need to experiment"

### RAPID-Specific Triggers
- "who should decide"
- "who owns this"
- "who has final say"
- "decision authority"
- "who needs to approve"
- "accountability for"

### Matrix-Specific Triggers
- "compare options objectively"
- "weighted comparison"
- "evaluate against criteria"
- "score these options"
- "which is better by what measure"

### Pre-Mortem-Specific Triggers
- "what could go wrong"
- "stress-test this"
- "identify risks"
- "why might this fail"
- "devil's advocate"
- "poke holes in this"
- "what are we missing"

### OODA-Specific Triggers
- "how do we iterate"
- "execution plan"
- "what's our loop"
- "monitor and adjust"
- "pivot criteria"
- "feedback cycle"

---

## Implicit Triggers

Context suggests a decision moment without explicit request:

### Multiple Paths Mentioned
When user or conversation reveals:
- "We could do A or B"
- "There are a few approaches"
- "Options include..."
- Listing alternatives without choosing

**Action:** Offer to help structure the decision

### Trade-offs Being Discussed
When conversation involves:
- "On one hand... on the other"
- "The advantage is X but the downside is Y"
- Comparing benefits and drawbacks
- Mentioning conflicting priorities

**Action:** Offer decision matrix approach

### Stakeholder Disagreement
When discussion reveals:
- Different team members prefer different options
- Conflicting recommendations
- Unclear who should make the call
- "Marketing wants X but Engineering wants Y"

**Action:** Offer RAPID clarification

### Uncertainty About Next Steps
When user expresses:
- "I'm not sure what to do next"
- "There are several directions"
- "We're stuck deciding"
- Hesitation or analysis paralysis

**Action:** Offer structured decision support

### Resource Allocation Questions
When discussion involves:
- "Where should we invest"
- "Which project gets priority"
- "Budget allocation"
- "Team allocation"

**Action:** Offer full decision cycle

### Risk Awareness
When user mentions:
- "I'm worried about"
- "What if this doesn't work"
- "The risk is"
- "We need to be careful about"

**Action:** Offer pre-mortem analysis

### Execution Planning
When conversation moves to:
- "How do we implement this"
- "What's the plan"
- "Next steps after deciding"
- "How do we track progress"

**Action:** Offer OODA framework

---

## Framework-Specific Activation

| Signal | Primary Framework | Secondary |
|--------|-------------------|-----------|
| Problem type unclear | Cynefin | - |
| Ownership unclear | RAPID | Cynefin |
| Multiple options | Matrix | Pre-mortem |
| Risk concerns | Pre-mortem | OODA |
| Implementation | OODA | Pre-mortem |
| Strategic choice | Full cycle | - |
| Quick tactical | Quick workflow | - |

---

## Suppression Signals

Do NOT activate decision-making skill when:

### Information-Only Requests
- "Tell me about X"
- "What is X"
- "How does X work"
- "Explain Y"

User wants information, not decision support.

### Decision Already Made
- "We've decided to do X"
- "We're going with Y"
- "The choice is made"

Skip to execution (OODA only if needed).

### Execution Guidance Needed
- "How do I implement X"
- "Steps to do Y"
- "Guide me through Z"

This is OODA Act phase, not full decision.

### Simple Binary with Obvious Answer
- Question with clear best answer
- No real trade-off
- Expertise question, not decision

Provide direct answer.

### Rhetorical Questions
- "Why would anyone choose X"
- "Isn't Y obviously better"
- User seeking validation, not analysis

Validate or gently redirect if flawed.

### Out of Scope
- Personal life decisions (unless specifically asked for frameworks)
- Ethical dilemmas (handle carefully, different from business decisions)
- Predictions about external events (not decisions)

---

## Activation Response

When trigger detected, agent should:

### For Explicit Triggers:
1. Acknowledge the decision need
2. Offer appropriate framework(s)
3. Ask if user wants structured support

Example:
> "This sounds like a decision that would benefit from structured analysis. Would you like me to walk through a decision framework? I can help classify the problem type, compare options, or stress-test a preferred choice."

### For Implicit Triggers:
1. Note the decision signal observed
2. Gently offer support without assuming
3. Wait for confirmation

Example:
> "I notice you're weighing several options here. Would it help to structure this as a formal comparison, or would you prefer to work through it conversationally?"

### For Suppression Signals:
1. Do not activate decision framework
2. Respond to the actual request
3. Note if decision support might be relevant later

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────────────┐
│                   DECISION TRIGGER QUICK CHECK                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ACTIVATE when user says/implies:                               │
│  ✓ "help me decide" / "should we"                               │
│  ✓ "compare" / "which option"                                   │
│  ✓ "who decides" / "who owns"                                   │
│  ✓ "what could go wrong"                                        │
│  ✓ "how do we iterate"                                          │
│  ✓ Multiple options mentioned without choice                    │
│  ✓ Trade-offs being discussed                                   │
│  ✓ Stakeholder disagreement                                     │
│                                                                  │
│  SUPPRESS when user wants:                                      │
│  ✗ Information only                                             │
│  ✗ Execution guidance (decision made)                           │
│  ✗ Simple answer with no trade-off                              │
│  ✗ Validation of existing choice                                │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## References

- `../../SKILL.md` - Main router
- `../frameworks/` - Individual framework details
- `../workflows/` - Full and quick decision processes
