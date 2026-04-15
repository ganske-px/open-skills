---
name: storytelling
description: Generates quick inline charts from data (direct mode) or escalates to storytelling-agent for full narratives. INVOKE when asked to "create a chart", "visualize this data", "show me in a chart". For "presentation", "deck", "story", "vision", "roadmap", "strategic decision", "convince stakeholder" — escalate to storytelling-agent. Do NOT use for summarizing documents — use tldr. Do NOT use for LinkedIn/blog posts — use content-writer.
---

# Storytelling — Lightweight Skill

Generates quick inline charts (SWD) or escalates to storytelling-agent when the request requires narrative, multiple frameworks, or a specific audience.

## When to use this skill (do not escalate)

- "give me a chart of these numbers"
- "visualize this"
- Single chart with a clear message
- Data already available in context

## When to escalate to `storytelling-agent`

**Any of these signals → escalate:**
- Presentation, deck, slides, PowerPoint
- Narrative, story, full story
- Stakeholder, board, C-level, customer, all-hands
- Product vision, north star, product future
- Roadmap, next cycle, what we're building
- Strategic decision, bet, prioritization between options
- Technical problem to present, technical dependency
- Reorg, team structure change, team change
- Convince someone, get approval, alignment
- Multiple charts or data cuts
- "How do I tell this story"
- Request mentions HTML

**Before escalating, collect two fields if not already clear. One question at a time — wait for the answer before asking the next.**

**Question 1 — Audience** (if not specified in the request): call the `AskUserQuestion` tool with:
- question: "Who is this presentation for?"
- options: ["Board / C-level", "Engineering / technical team", "Squad / product team", "Customers", "All-hands / broad team"]
- type: select

With the answer in hand, **Question 2 — Main message** (if vague or absent): call the `AskUserQuestion` tool with:
- question: "What is the main message? What should the person know or do at the end?"
- type: text (open field)

If both are already clear in the request, escalate directly without asking.

**How to escalate:**
```
Agent tool:
  subagent_type: "storytelling-agent"
  description: "create story about [topic]"
  prompt: "[full context + story type + audience + main message + available data]"
```

---

## Direct Mode (single chart — data available)

### 1. Identify chart_type

| Data | Type |
|---|---|
| Comparison between categories | `bar_vertical` (≤6) / `bar_horizontal` (>6) |
| Time trend | `line` |
| Two points in time | `slope` |
| Relationship between variables | `scatter` |
| Few categories with precision | `dot_plot` |
| Output from probability-analysis | `confidence_interval` |

### 2. Build data contract and run

```python
import sys
sys.path.insert(0, 'analysis/scripts')
from chart_builder import build_chart

CONTRACT = {
    "chart_type": "bar_vertical",
    "title": "main message (the finding)",
    "subtitle": "context",
    "source": "origin",
    "collected_at": "YYYY-MM-DD",
    "highlight": "main_label",
    "output_format": "png",
    "output_path": "/tmp/chart_<slug>",
    "data": {
        "labels": [],
        "values": [],
        "ci_lower": [],
        "ci_upper": []
    }
}
path = build_chart(CONTRACT)
print(f"Chart: {path}")
```

Run: `python3 /tmp/story_<slug>.py`

### 3. Deliver
- File path + title (the message, not the description)
- Explain SWD choices the first time in the session; afterwards, silent

## Consultive Mode (vague request)

**One question at a time. Wait for the answer before asking the next.**

**Question 1 — Message:** call the `AskUserQuestion` tool with:
- question: "What is the main message you want the chart to convey?"
- type: text (open field)

**Question 2 — Audience** (with the message in hand): call the `AskUserQuestion` tool with:
- question: "Who will see this chart?"
- options: ["Myself / internal use", "Squad / product team", "Board / stakeholder", "Customer"]
- type: select

→ If audience = Board/stakeholder/Customer with narrative request: escalate to storytelling-agent

**Question 3 — Data** (if not provided): call the `AskUserQuestion` tool with:
- question: "What's the status of the data?"
- options: ["I have it — I'll share", "I need to collect it"]
- type: select

→ If "I need to collect it": call `data-research` before generating the chart

## Non-negotiable SWD Rules

- Title = main message ("Approvals fell 18%", not "Approval Rate by Month")
- `highlight` = color `#E8533F`; all other elements → `#C8C8C8`
- Never pie chart
- Never dual Y-axis

## Integration with other skills

- Data not available → `data-research` first
- Comparisons/rates → `probability-analysis` first
- CI chart → always `confidence_interval` chart_type
