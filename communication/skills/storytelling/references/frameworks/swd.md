# Framework: SWD — Storytelling with Data (Knaflic)

## Core principle

Data without context is noise. Context without data is opinion. SWD is the method for transforming data into a visual argument the audience understands and retains.

## The 6 SWD lessons applied

### 1. Context before data
Before showing any number, answer:
- Who is this for?
- What do we want the person to do or know afterwards?
- What is the most important data — and why does it matter now?

### 2. Choose the right visual

| Data | Chart type |
|---|---|
| Comparison between categories | `bar_vertical` (≤6) / `bar_horizontal` (>6 or long labels) |
| Time trend | `line` |
| Two points in time | `slope` |
| Relationship between variables | `scatter` |
| Few categories with precision | `dot_plot` |
| Output from probability-analysis | `confidence_interval` |
| Never | pie chart |

### 3. Eliminate clutter

Remove everything that carries no information:
- Gridlines → only if they help reading exact values
- Chart borders → remove
- Legends → replace with inline labels when ≤ 3 series
- Decorative colors → neutral palette, 1 highlight color

### 4. Direct attention

- **1 highlight element per chart** — color `#E8533F`
- **Everything else in gray** — `#C8C8C8`
- Direct annotation on the main element (not in the legend)

### 5. Think like a designer

- Alignment creates order
- White space is part of the design
- Size communicates importance
- Title = the message (never the description of the data)

### 6. Tell the story

Required structure:
```
CONTEXT   → why this data matters
FINDING   → what the data shows (= chart title)
SO WHAT   → implication for the product/business
NEXT STEP → what we do with this
```

## Non-negotiable rules

| Rule | Detail |
|---|---|
| Title = message | "Approvals fell 18%" not "Approval Rate by Month" |
| 1 highlight color | `#E8533F` for the main; `#C8C8C8` for the rest |
| No pie | Pie chart never — bar is always more precise |
| No dual Y-axis | Two separate charts |
| Appendix mandatory | Query/source always present — non-negotiable |
| Max 5 charts per HTML | If more, question whether it's a story or a dashboard |

## Contextual rules

| Decision | Criterion |
|---|---|
| Show confidence interval | Always when data comes from `probability-analysis` |
| Vertical vs horizontal bar | Horizontal when labels > 20 chars or > 6 categories |
| Line vs bar | Line for continuous time; bar when individual point matters |
| Annotation vs legend | Inline when ≤ 3 series |

## Integration with chart_builder

```python
import sys
sys.path.insert(0, 'analysis/scripts')
from chart_builder import build_chart       # for standalone PNG
from html_story_builder import build_html_story  # for full story
```

## Integration with skills

- Data not available → `data-research` before any visual
- Comparisons/rates/probabilities → `probability-analysis` before comparing groups
- CI calculated → use `confidence_interval` chart_type mandatorily
