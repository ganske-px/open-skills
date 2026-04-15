# Framework: SCR — Situation-Complication-Resolution

## When to use

When you need to present a problem and a solution path. Especially useful for: diagnostic presentations, initiative proposals, status updates with plan changes.

Difference from Pyramid: SCR is a narrative structure (tells a linear story). Pyramid is an argumentative structure (proves a thesis). Use SCR when the context is not yet shared by the audience.

## Structure

### S — Situation (Stable state)

The starting point. Context the audience already knows or can accept as true without evidence.

**Rules:**
- Brief — 1 to 3 sentences
- Neutral — no value judgment yet
- Shared — if the audience disagrees with S, the entire argument collapses

**Example:**
"Our platform today processes ~2,000 verification searches per day. The flow has 4 steps, of which 3 are manual."

---

### C — Complication (What changed / The problem)

The tension that makes the current situation unsustainable or suboptimal. The "but" or "however" of the story.

**Rules:**
- Specific — data or evidence that quantifies the problem
- Urgent — why this matters now
- One central problem — not a list
- Can be external (market, regulation) or internal (capacity, quality)

**Example:**
"With 40% volume growth, the analysis team is at its limit. Average approval time rose from 2h to 6h, affecting the contract conversion rate."

---

### R — Resolution (What we do)

The response to the complication. Can be a recommendation, a plan, or a proposal.

**Rules:**
- Directly connected to C — the solution resolves the specific problem raised
- With success criterion: how do we know it worked?
- With clear next step: who does what by when

**Example:**
"We propose automating steps 2 and 4 using configurable rules. This reduces approval time from 6h to 90min and frees the team to focus on cases that genuinely need human analysis."

---

## SCR complete as narrative arc

```
OPENING (Pathos — optional but powerful)
  Customer story that lives the Complication
  "Company X waited 6 hours for approval of a $200k contract"

SITUATION
  Stable context, brief, without judgment

COMPLICATION
  The data that proves the situation is problematic
  [SWD chart if available]

RESOLUTION
  The proposal with success criterion
  → Connect to `pyramid.md` if there are multiple supporting arguments

CLOSING
  Return to the opening story with resolution
  "With automation, Company X receives approval in 90 minutes"
```

## SCR vs Pyramid — when to use each

| Criterion | SCR | Pyramid |
|---|---|---|
| Shared context | No — need to build | Yes — can skip ahead |
| Main objective | Create understanding of the problem | Convince to take a decision |
| Audience | Doesn't know the problem yet | Already knows the problem, needs a recommendation |
| Tone | Narrative | Argumentative |
| Combination | SCR to introduce → Pyramid to recommend | — |

## Anti-patterns

- Situation too long — audience loses attention before Complication
- Complication without data — "we're having difficulties" is not Complication, it's opinion
- Resolution that doesn't solve the C raised — audience notices the disconnect
- Jumping straight to R without S and C — works if audience shares the context, otherwise creates rejection
