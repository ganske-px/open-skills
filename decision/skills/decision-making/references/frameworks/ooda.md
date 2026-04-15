# OODA Loop

> Execution and iteration framework for decision-action cycles.
> Created by military strategist John Boyd for fighter pilot combat; broadly applicable.

## The Four Phases

```
         ┌─────────────────────────────────────────┐
         │              ORIENT                      │
         │  Synthesis, mental models, cultural     │
         │  traditions, previous experience,       │
         │  unfolding circumstances                │
         └─────────────────────────────────────────┘
                ↗                           ↘
         ┌─────────┐                    ┌─────────┐
         │ OBSERVE │ ← Feedback ─────── │ DECIDE  │
         └─────────┘                    └─────────┘
                ↖                           ↙
              ┌───────────────────────────────┐
              │             ACT               │
              └───────────────────────────────┘
                            ↓
                         [LOOP]
```

---

### 1. OBSERVE

**Purpose:** Gather raw information about the environment and situation.

**Activities:**
- Collect data from multiple sources
- Monitor relevant metrics and signals
- Note changes from previous observations
- Identify what you don't know

**Agent behavior:**
- Actively seek current state information
- Cross-reference multiple data sources
- Document observations explicitly
- Distinguish facts from interpretations

**Questions:**
- What is actually happening right now?
- What data do we have? What's missing?
- What has changed since last observation?
- What are others (competitors, users) doing?

---

### 2. ORIENT

**Purpose:** Make sense of observations through analysis and synthesis.

> **This is the most critical phase.** Poor orientation leads to wrong decisions regardless of data quality.

**Activities:**
- Analyze observations against mental models
- Synthesize information into coherent picture
- Challenge assumptions and biases
- Consider multiple interpretations
- Update understanding of the situation

**Orientation factors (Boyd's breakdown):**
- **Cultural traditions:** How our background shapes interpretation
- **Genetic heritage:** Innate patterns of thought
- **Previous experience:** What worked/failed before
- **New information:** Current observations
- **Analysis & synthesis:** Active reasoning

**Agent behavior:**
- Explicitly state interpretation of observations
- Identify relevant mental models being applied
- Note assumptions being made
- Consider alternative interpretations
- Flag uncertainty levels

**Questions:**
- What does this data mean?
- What patterns do we see?
- What are our assumptions?
- How might we be wrong?
- What would a competitor/critic see?

---

### 3. DECIDE

**Purpose:** Determine course of action from available options.

**Activities:**
- Generate options based on orientation
- Evaluate options against objectives
- Select best course of action
- Define success criteria
- Plan for contingencies

**Agent behavior:**
- Present options with rationale
- Make clear recommendation
- State expected outcomes
- Define decision criteria
- Set review/pivot points

**Questions:**
- What are our options?
- What's the best move given our orientation?
- What are we optimizing for?
- What will we do if wrong?

---

### 4. ACT

**Purpose:** Execute the decision and generate feedback.

**Activities:**
- Implement chosen action
- Execute with appropriate speed
- Observe effects of action
- Generate data for next OBSERVE phase

**Agent behavior:**
- Execute decisively once decided
- Monitor execution closely
- Collect feedback immediately
- Prepare for next loop iteration

**Questions:**
- Are we executing as planned?
- What effects are we seeing?
- What new information is emerging?
- When do we loop back?

---

## Key Concepts

### Tempo (Operating Inside Opponent's Loop)

The side with faster OODA cycles gains advantage:
- Observe faster → better situational awareness
- Orient faster → better understanding
- Decide faster → more timely choices
- Act faster → initiative and surprise

**Application:** In competitive situations, optimize for cycle speed while maintaining quality.

### Implicit Guidance and Control

As orientation improves, decisions become more intuitive:
- Experts loop Observe→Orient→Act (implicit decision)
- Beginners need full Observe→Orient→Decide→Act

**Application:** Build shared mental models so teams can act with less explicit coordination.

### Feedback Loops

OODA is not linear — multiple feedback paths exist:
- Action feeds into next Observation
- Observation can update Orientation directly
- Orient can trigger immediate Action in crisis

---

## OODA Cadences by Context

| Context | Cycle Time | Notes |
|---------|------------|-------|
| **Crisis/Chaotic** | Minutes to hours | Speed critical, accept imperfect information |
| **Competitive** | Hours to days | Outpace opponent's decision cycle |
| **Project** | Days to weeks | Regular iteration and adjustment |
| **Strategic** | Weeks to months | Deep orientation, careful decision |
| **Cultural change** | Months to years | Slow, deliberate orientation shifts |

---

## Orientation Biases to Recognize

Poor orientation often comes from unexamined biases:

| Bias | Description | Counter |
|------|-------------|---------|
| **Confirmation** | Seeking information that confirms beliefs | Actively seek disconfirming evidence |
| **Anchoring** | Over-weighting first information received | Deliberately consider alternatives |
| **Availability** | Overweighting recent/vivid events | Look at base rates and history |
| **Sunk cost** | Continuing due to past investment | Focus only on future value |
| **Groupthink** | Conforming to group opinion | Assign devil's advocate role |
| **Overconfidence** | Excessive certainty in judgments | State confidence levels explicitly |
| **Status quo** | Preferring current state | Force evaluation of change options |

---

## Integration with Other Frameworks

### With Cynefin

| Domain | OODA Application |
|--------|------------------|
| **Clear** | Fast, routine loops; minimal Orientation |
| **Complicated** | Deliberate Orientation with expert input |
| **Complex** | Rapid experimental loops; Probe→Sense = OODA |
| **Chaotic** | Fastest possible Act→Sense→Respond; Orient later |

### With RAPID

- **D** owns the Decide phase
- **R** supports Observe and Orient
- **P** executes Act phase
- **I** contributes to Orient

### With Pre-Mortem

Pre-mortem improves Orient phase by surfacing risks before Act.

### With Decision Matrix

Matrix is a structured Decide tool within the OODA loop.

---

## OODA for Teams

Individual OODA loops must sync with team loops:

```
     Individual           Team              Organization
    ┌─────────┐        ┌─────────┐         ┌─────────┐
    │  OODA   │ ←────→ │  OODA   │ ←─────→ │  OODA   │
    │ (fast)  │        │ (medium)│         │  (slow) │
    └─────────┘        └─────────┘         └─────────┘
```

**Alignment requirements:**
- Shared mental models (Orient alignment)
- Clear command intent (Decide alignment)
- Feedback flow upward (Observe sharing)
- Autonomy at appropriate level (Act empowerment)

---

## Agent Application

When an agent applies OODA:

### For ongoing execution:
1. **Observe:** Gather current state information
2. **Orient:** Interpret against context and goals
3. **Decide:** Recommend or make next action
4. **Act:** Execute and capture feedback
5. **Loop:** Start next cycle

### For decision support:
1. Help user **Observe** by gathering data
2. Support **Orient** by providing analysis and alternatives
3. Facilitate **Decide** by structuring options
4. Enable **Act** by providing clear next steps
5. Prepare for **Loop** by defining review points

### Output format:
```markdown
## OODA Cycle: [Iteration #/Context]

### Observe
- [Current state observation 1]
- [Current state observation 2]
- [Information gaps]

### Orient
- **Interpretation:** [What this means]
- **Key assumptions:** [What we're assuming]
- **Alternatives considered:** [Other interpretations]
- **Confidence level:** [High/Medium/Low]

### Decide
- **Recommended action:** [What to do]
- **Rationale:** [Why this choice]
- **Success criteria:** [How we'll know it worked]
- **Pivot trigger:** [When to reconsider]

### Act
- [Specific action steps]
- [Timeline]
- [Who does what]

### Next Loop
- **Review point:** [When]
- **Data to collect:** [What]
```

---

## References

- Boyd, J. "Patterns of Conflict" (1986)
- Boyd, J. "The Essence of Winning and Losing" (1996)
- Richards, C. "Certain to Win" (2004)
- Osinga, F. "Science, Strategy and War: The Strategic Theory of John Boyd" (2007)
