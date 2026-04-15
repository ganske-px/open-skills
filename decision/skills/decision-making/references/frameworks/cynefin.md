# Cynefin Framework

> Classification framework for understanding the nature of a problem before choosing a response strategy.

## The Five Domains

### 1. Clear (formerly Simple/Obvious)

**Characteristics:**
- Known knowns
- Cause and effect obvious to all
- Best practices exist and are well-documented
- Repeatable, predictable outcomes

**Response Pattern:** Sense → Categorize → Respond
```
[Observe situation] → [Match to known category] → [Apply best practice]
```

**Agent Behavior:**
- Identify and execute established procedure
- Don't reinvent; use proven solutions
- Document for consistency

**Examples:**
- Standard deployment process
- Invoice processing
- Password reset flow

---

### 2. Complicated

**Characteristics:**
- Known unknowns
- Cause and effect discoverable through analysis
- Multiple valid solutions exist
- Expertise required to understand

**Response Pattern:** Sense → Analyze → Respond
```
[Gather data] → [Expert analysis] → [Choose good practice]
```

**Agent Behavior:**
- Consult domain experts or specialist agents
- Allow time for proper analysis
- Accept that multiple valid solutions exist
- Document reasoning for chosen approach

**Examples:**
- System architecture decisions
- Performance optimization
- Vendor selection
- Tax strategy

---

### 3. Complex

**Characteristics:**
- Unknown unknowns
- Cause and effect only apparent in retrospect
- Patterns emerge through interaction
- No right answer discoverable in advance

**Response Pattern:** Probe → Sense → Respond
```
[Safe-to-fail experiment] → [Observe what emerges] → [Amplify success / Dampen failure]
```

**Agent Behavior:**
- Design safe-to-fail experiments
- Create conditions for patterns to emerge
- Be prepared to pivot
- Multiple parallel probes often valuable
- Retrospectives essential

**Examples:**
- Market strategy for new product
- Organizational culture change
- User behavior prediction
- Innovation initiatives

---

### 4. Chaotic

**Characteristics:**
- No patterns discernible
- High turbulence
- Crisis or emergency
- Need to establish order

**Response Pattern:** Act → Sense → Respond
```
[Take action to stabilize] → [Observe results] → [Adjust and continue]
```

**Agent Behavior:**
- Act first, analyze later
- Establish ANY order (imperfect ok)
- Look for patterns as stability returns
- Move situation toward Complex or Complicated
- Clear command authority essential

**Examples:**
- Production system down with unknown cause
- Security breach in progress
- Critical data loss
- PR crisis

---

### 5. Disorder (Center)

**Characteristics:**
- Unclear which domain applies
- Multiple interpretations possible
- Stakeholders may disagree on classification

**Response:**
- Gather more information
- Break problem into components
- Classify each component separately
- Default to treating as Complex if uncertain

---

## Classification Questions

Ask these to determine the domain:

| Question | Clear | Complicated | Complex | Chaotic |
|----------|-------|-------------|---------|---------|
| Is cause-effect obvious? | Yes | After analysis | Only in hindsight | Not discoverable |
| Do best practices exist? | Yes, well-known | Yes, expert-known | No, must experiment | No, must stabilize |
| How many valid solutions? | One best | Several good | Unknown | Any that works |
| Can we predict outcomes? | Yes | Largely | No | No |
| What expertise needed? | Procedural | Domain expert | Diverse perspectives | Crisis management |

## Domain Transition Signals

**Clear → Complicated:**
- Edge cases appear
- Best practice doesn't fit
- Experts disagree

**Complicated → Complex:**
- Analysis yields conflicting conclusions
- Experts fundamentally disagree
- Unexpected outcomes from "proven" approaches

**Complex → Chaotic:**
- Situation deteriorating rapidly
- No time for experimentation
- Immediate action required

**Chaotic → Complex:**
- Initial stability achieved
- Patterns beginning to emerge
- Breathing room for experimentation

**Any → Clear:**
- Pattern established and repeatable
- Solution documented
- Training possible

## Complacency Warning

**Complacent Slide:** Clear → Chaotic

When teams treat Complex/Complicated problems as Clear (applying rigid procedures), they can miss emerging changes until crisis hits.

Signs of complacent slide:
- "We've always done it this way"
- Ignoring anomalies
- Over-reliance on metrics
- Dismissing edge cases

## Agent Integration

When an agent detects a decision moment:

1. **Default assumption:** Disorder until classified
2. **Classification attempt:** Use questions above
3. **If uncertain:** Treat as Complex (safest default)
4. **If Clear:** Proceed with established procedure
5. **If Complicated:** Recommend consulting domain expert
6. **If Complex:** Propose safe-to-fail experiment
7. **If Chaotic:** Recommend immediate stabilization action

## Mapping to Other Frameworks

| Domain | RAPID Focus | Matrix Use | Pre-Mortem | OODA Cadence |
|--------|-------------|------------|------------|--------------|
| Clear | Standard roles | Rarely needed | Rarely needed | Fast, routine |
| Complicated | Emphasize R,I | Full analysis | Standard | Methodical |
| Complex | Flexible roles | Light/comparative | Extensive | Rapid iteration |
| Chaotic | Centralize D | Skip | Skip initially | Fastest possible |

## References

- Snowden, D. & Boone, M. "A Leader's Framework for Decision Making" (HBR, 2007)
- Cognitive Edge / Cynefin.io
