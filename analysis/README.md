# analysis/

Technical analysis tools for product managers who need to work with data, code, and external research. Covers statistical inference, code and architecture review, web research, and interactive data visualization.

## What's Included

```
analysis/
  skills/
    probability-analysis/    # Bayesian inference, confidence intervals, statistical comparisons
    tech-lead/               # Code architecture review and technical decision evaluation
    web-search-researcher/   # Deep web research for benchmarks, market data, and competitive intel
  agents/
    web-search-researcher.md # Autonomous agent for multi-step web research workflows
  scripts/
    chart_builder.py         # Generate SWD-styled static charts (bar, line, scatter, etc.)
    html_story_builder.py    # Build standalone interactive HTML narratives with Plotly charts
    probability_calculator.py# CLI tool for confidence intervals and Bayesian calculations
```

**3 skills, 1 agent, 3 scripts.**

## Skills

### probability-analysis
Applies statistical methods to product data:
- **Confidence intervals**: Given a sample size and observed rate, compute the 95% CI and interpret what it means for decision-making.
- **A/B test evaluation**: Given control and variant results, compute statistical significance and practical significance. Distinguish between "this is real" and "this matters."
- **Bayesian inference**: Update beliefs given new evidence. Useful for interpreting small samples or combining research findings.
- **Base rate awareness**: Flags when conclusions ignore base rates (e.g., "our conversion rate increased" without accounting for traffic quality changes).

Outputs include: the numerical result, a plain-language interpretation, and guidance on what the result implies for the decision at hand.

### tech-lead
Reviews code and technical decisions from a product architecture perspective:
- **Code review**: Assess a code diff or module for correctness, maintainability, security patterns, and scalability.
- **Architecture evaluation**: Given a proposed technical design, identify risks, tradeoffs, and missing considerations.
- **Build vs buy analysis**: Frame the technical dimensions of a build vs buy decision — integration complexity, maintenance burden, vendor risk, extensibility.
- **Technical debt assessment**: Given a codebase area, assess the level of technical debt and the risk of shipping new features on top of it.

Useful for PMs who want to develop technical fluency or prepare for engineering conversations.

### web-search-researcher
Conducts deep, structured web research:
- **Benchmark gathering**: Find industry benchmarks for conversion rates, retention, NPS, feature adoption, and other product metrics.
- **Competitive intelligence**: Research competitor features, pricing, positioning, and recent launches from public sources.
- **Market sizing**: Find and evaluate market size data, growth rates, and analyst estimates.
- **Academic and practitioner research**: Find relevant studies, articles, and case studies on specific topics.

Produces a structured research brief with: sources, key findings, confidence assessments, and gaps. See also the `commands/` directory for the `competitive-analysis` and `competitive-brief` starter commands which use this skill as a foundation.

## Agent

### web-search-researcher.md
An autonomous sub-agent that runs multi-step web research workflows. Given a research question, it plans a search strategy, executes searches iteratively, evaluates sources for credibility, synthesizes findings, and produces a structured research brief with citations. Deploy for research tasks that require more than a single search — competitive landscapes, market entry analysis, technical benchmarking.

## Scripts

### chart_builder.py
Generates SWD-styled static charts as PNG or SVG. Supports: bar (vertical and horizontal), line, scatter, slope, and small multiples. Applies the SWD color palette (neutral grey for context, accent red for emphasis). Takes a data dict as input and produces a publication-ready chart file.

Usage:
```python
from chart_builder import make_chart

make_chart({
    "chart_type": "bar_vertical",
    "title": "Feature adoption by segment",
    "highlight": "enterprise",
    "data": {"labels": ["enterprise", "smb", "startup"], "values": [0.78, 0.52, 0.31]},
    "output_path": "/tmp/adoption_chart",
})
```

### html_story_builder.py
Builds standalone, self-contained HTML files with interactive Plotly charts embedded alongside narrative sections (context, so what, next steps, appendix). Follows the SWD storytelling structure. The HTML file is fully standalone — no server required, works offline, can be emailed or shared as a file.

Supported chart types: `bar_vertical`, `bar_horizontal`, `line`, `line_multi`, `slope`, `scatter`, `confidence_interval`, `waterfall`.

Usage:
```python
from html_story_builder import build_html_story

path = build_html_story({
    "chart_type": "bar_vertical",
    "title": "Feature activation rate by user segment",
    "subtitle": "30-day activation — Q1 2025",
    "source": "Product analytics",
    "collected_at": "2025-01-15",
    "highlight": "power_users",
    "output_path": "/tmp/activation_story",
    "data": {
        "labels": ["power_users", "casual_users", "new_users"],
        "values": [0.82, 0.45, 0.21],
    },
    "narrative": {
        "context": "Activation rates vary significantly across segments.",
        "so_what": "Power users activate at 4x the rate of new users.",
        "next_steps": ["Run an onboarding experiment for new users"],
    },
})
```

### probability_calculator.py
CLI tool for statistical calculations. Provides: Wilson confidence intervals, z-test for proportions, chi-squared test for independence, and Bayesian beta-binomial updates. Designed for quick calculations without needing to open a notebook.

```bash
python probability_calculator.py --ci --n 200 --k 34
# → 95% CI: [0.120, 0.224]
```

## Dependency Graph

```
web-search-researcher (skill + agent)
         ↓ (feeds data to)
probability-analysis
         ↓ (results used in)
  chart_builder.py ──→ html_story_builder.py
                              ↓
               communication/storytelling
```

```
tech-lead
  (standalone — no dependencies on other analysis tools)
```

## Quick Start

**Evaluate whether an A/B test result is real:**
```
> my experiment showed 8.2% conversion for control and 9.1% for variant, with 1,200 users per arm — is this significant?
```
`probability-analysis` computes significance, practical effect size, and gives a plain-language recommendation.

**Research industry benchmarks before setting a goal:**
```
> what are typical week-4 retention rates for B2B SaaS products in the project management category?
```
`web-search-researcher` finds and synthesizes benchmark data from credible public sources.

**Review a technical design before committing:**
```
> here is our proposed architecture for the new webhook system — what are the risks and missing considerations?
```
`tech-lead` evaluates the design and surfaces technical concerns a PM should understand before signing off.

**Build an interactive data story:**
```python
from analysis.scripts.html_story_builder import build_html_story
# See script docstring for full usage examples
```

## Installation

```bash
cp -r analysis/skills/* your-project/.claude/skills/
cp -r analysis/agents/* your-project/.claude/agents/
cp -r analysis/scripts/* your-project/scripts/  # or wherever your scripts live
```

Script dependencies:
```bash
pip install plotly
```
