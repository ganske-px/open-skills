#!/usr/bin/env python3
"""
HTML Story Builder — Plotly-based interactive data narratives following the
Storytelling with Data (SWD) methodology.

Input:  A data contract dict (or JSON file) containing chart data, narrative
        sections (context, so-what, next steps), and output path.
Output: A self-contained, standalone HTML file with interactive Plotly charts,
        styled sections, and an optional appendix with data provenance.

Supported chart types:
    bar_vertical, bar_horizontal, line, line_multi, slope,
    scatter, confidence_interval, waterfall

Usage examples:

    # Build from a Python dict
    from html_story_builder import build_html_story

    story = {
        "chart_type": "bar_vertical",
        "title": "Feature adoption by user segment",
        "subtitle": "30-day activation rate — Q1",
        "source": "Product analytics — events table",
        "collected_at": "2025-01-15",
        "highlight": "power_users",
        "output_path": "/tmp/adoption_story",
        "data": {
            "labels": ["power_users", "casual_users", "new_users"],
            "values": [0.82, 0.45, 0.21],
        },
        "narrative": {
            "context": "Activation rates vary significantly across user segments.",
            "so_what": "Power users activate at 4x the rate of new users, suggesting onboarding is the key lever.",
            "next_steps": [
                "Run a targeted onboarding experiment for new users",
                "Interview 5 power users to understand their activation path",
            ],
            "appendix_query": "SELECT segment, COUNT(*) FROM activations GROUP BY segment",
        },
    }
    output_file = build_html_story(story)
    print(f"Story saved to: {output_file}")


    # Multi-chart story
    multi = {
        "title": "Monthly retention trends",
        "subtitle": "Cohort comparison — last 6 months",
        "source": "Data warehouse — retention_cohorts",
        "collected_at": "2025-01-15",
        "output_path": "/tmp/retention_story",
        "charts": [
            {
                "chart_type": "line_multi",
                "title": "Retention by cohort",
                "highlight": "Jan cohort",
                "data": {
                    "labels": ["Week 1", "Week 2", "Week 4", "Week 8"],
                    "series": [
                        {"label": "Jan cohort", "values": [1.0, 0.72, 0.55, 0.41]},
                        {"label": "Feb cohort", "values": [1.0, 0.68, 0.50, 0.38]},
                    ],
                },
            },
        ],
        "narrative": {
            "context": "Retention has been declining across cohorts.",
            "so_what": "The Jan cohort outperforms Feb by ~8% at week 8 — investigate what changed.",
            "next_steps": ["Compare onboarding flows between Jan and Feb cohorts"],
        },
    }
    output_file = build_html_story(multi)
"""
import json
from pathlib import Path
from datetime import datetime

import plotly.graph_objects as go
import plotly.io as pio

# SWD color palette — neutral grey for context, accent red for emphasis
COLOR_NEUTRAL = '#C8C8C8'
COLOR_HIGHLIGHT = '#E8533F'
COLOR_TEXT = '#2D2D2D'
COLOR_SUBTITLE = '#767676'
COLOR_BG = '#FFFFFF'

SWD_PLOTLY_TEMPLATE = {
    'layout': {
        'font': {'family': 'Inter, Helvetica Neue, sans-serif', 'color': COLOR_TEXT},
        'paper_bgcolor': COLOR_BG,
        'plot_bgcolor': COLOR_BG,
        'xaxis': {
            'showgrid': False,
            'zeroline': False,
            'linecolor': '#E0E0E0',
            'tickfont': {'size': 11, 'color': COLOR_SUBTITLE},
        },
        'yaxis': {
            'showgrid': False,
            'zeroline': False,
            'linecolor': '#E0E0E0',
            'tickfont': {'size': 11, 'color': COLOR_SUBTITLE},
        },
        'margin': {'t': 40, 'b': 40, 'l': 40, 'r': 40},
        'hoverlabel': {
            'bgcolor': 'white',
            'bordercolor': '#E0E0E0',
            'font': {'size': 12},
        },
    }
}


def make_plotly_chart(contract: dict) -> go.Figure:
    """Build a Plotly Figure from a data contract dict.

    Args:
        contract: Dict with keys chart_type, data, highlight, and chart-specific fields.

    Returns:
        A styled Plotly Figure ready to embed in HTML.
    """
    chart_type = contract.get('chart_type', 'bar_vertical')
    data = contract['data']
    highlight = contract.get('highlight', '')
    labels = data.get('labels', [])
    values = data.get('values', [])
    colors = [COLOR_HIGHLIGHT if l == highlight else COLOR_NEUTRAL for l in labels]
    fmt = '.1%' if values and max(values) <= 1 else ',.0f'

    fig = go.Figure()
    layout_extra = {}

    if chart_type in ('bar_vertical', 'bar_horizontal'):
        orientation = 'h' if chart_type == 'bar_horizontal' else 'v'
        x_data, y_data = (values, labels) if orientation == 'h' else (labels, values)
        fig.add_trace(go.Bar(
            x=x_data,
            y=y_data,
            orientation=orientation,
            marker_color=colors,
            text=[f'{v:{fmt}}' for v in values],
            textposition='outside',
            hovertemplate='%{y}: %{x}<extra></extra>' if orientation == 'h'
                          else '%{x}: %{y}<extra></extra>',
        ))
        if orientation == 'h':
            layout_extra['xaxis'] = {'visible': False}
            layout_extra['yaxis'] = {'autorange': 'reversed'}
        else:
            layout_extra['yaxis'] = {'visible': False}

    elif chart_type in ('line', 'line_multi'):
        series_list = data.get('series', [{'label': '', 'values': values}])
        for s in series_list:
            color = COLOR_HIGHLIGHT if s['label'] == highlight or not s['label'] else COLOR_NEUTRAL
            fig.add_trace(go.Scatter(
                x=labels,
                y=s['values'],
                mode='lines+markers',
                name=s['label'],
                line={'color': color, 'width': 3 if color == COLOR_HIGHLIGHT else 1.5},
                marker={'size': 6},
                hovertemplate=f"{s['label']}: %{{y}}<extra></extra>",
            ))
        layout_extra['showlegend'] = len(series_list) > 1

    elif chart_type == 'slope':
        series_list = data.get('series', [])
        for s in series_list:
            color = COLOR_HIGHLIGHT if s['label'] == highlight else COLOR_NEUTRAL
            fig.add_trace(go.Scatter(
                x=labels,
                y=s['values'],
                mode='lines+markers+text',
                name=s['label'],
                line={'color': color, 'width': 3 if color == COLOR_HIGHLIGHT else 1.5},
                marker={'size': 8},
                text=[f"{s['label']}: {s['values'][0]:{fmt}}", f"{s['values'][1]:{fmt}}"],
                textposition=['middle left', 'middle right'],
            ))

    elif chart_type == 'scatter':
        fig.add_trace(go.Scatter(
            x=data['x'],
            y=data['y'],
            mode='markers',
            text=data.get('labels', []),
            marker={
                'color': [
                    COLOR_HIGHLIGHT if l == highlight else COLOR_NEUTRAL
                    for l in data.get('labels', [''] * len(data['x']))
                ],
                'size': 10,
                'opacity': 0.8,
            },
            hovertemplate='%{text}<br>x: %{x}, y: %{y}<extra></extra>',
        ))
        layout_extra['xaxis'] = {
            **SWD_PLOTLY_TEMPLATE['layout']['xaxis'],
            'title': data.get('x_label', ''),
        }
        layout_extra['yaxis'] = {
            **SWD_PLOTLY_TEMPLATE['layout']['yaxis'],
            'title': data.get('y_label', ''),
        }

    elif chart_type == 'confidence_interval':
        ci_lower = data.get('ci_lower', values)
        ci_upper = data.get('ci_upper', values)
        for i, (lbl, val, lo, hi) in enumerate(zip(labels, values, ci_lower, ci_upper)):
            color = COLOR_HIGHLIGHT if lbl == highlight else COLOR_NEUTRAL
            fig.add_trace(go.Scatter(
                x=[lo, hi],
                y=[lbl, lbl],
                mode='lines',
                line={'color': color, 'width': 6},
                opacity=0.4,
                showlegend=False,
                hoverinfo='skip',
            ))
            fig.add_trace(go.Scatter(
                x=[val],
                y=[lbl],
                mode='markers+text',
                marker={'color': color, 'size': 12},
                text=[f'{val:.1%}'],
                textposition='middle right',
                name=lbl,
                showlegend=False,
                hovertemplate=f'{lbl}: {val:.1%} [{lo:.1%}–{hi:.1%}]<extra></extra>',
            ))
        layout_extra['xaxis'] = {'tickformat': '.0%', 'showgrid': False}

    elif chart_type == 'waterfall':
        fig.add_trace(go.Waterfall(
            x=labels,
            y=values,
            measure=['relative'] * (len(values) - 1) + ['total'],
            connector={'line': {'color': '#E0E0E0'}},
            increasing={'marker': {'color': '#4CAF50'}},
            decreasing={'marker': {'color': COLOR_HIGHLIGHT}},
            totals={'marker': {'color': COLOR_NEUTRAL}},
            text=[f'{v:+,.0f}' for v in values],
            textposition='outside',
        ))

    # Deep-merge layout_extra into the template: nested dicts are merged, scalars override
    merged = {**SWD_PLOTLY_TEMPLATE['layout']}
    for k, v in layout_extra.items():
        if k in merged and isinstance(merged[k], dict) and isinstance(v, dict):
            merged[k] = {**merged[k], **v}
        else:
            merged[k] = v
    fig.update_layout(**merged)
    return fig


CSS = """
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Inter', 'Helvetica Neue', sans-serif; background: #F4F4F4;
         color: #2D2D2D; line-height: 1.6; }
  .story { max-width: 900px; margin: 40px auto; background: white;
           border-radius: 8px; box-shadow: 0 2px 12px rgba(0,0,0,0.08); overflow: hidden; }
  .header { padding: 36px 40px 24px; border-bottom: 3px solid #E8533F; }
  .header h1 { font-size: 22px; font-weight: 700; color: #2D2D2D; margin-bottom: 8px; }
  .header .subtitle { font-size: 14px; color: #767676; }
  .header .meta { font-size: 12px; color: #AAAAAA; margin-top: 8px; }
  .section { padding: 28px 40px; }
  .section + .section { border-top: 1px solid #F0F0F0; }
  .section-label { font-size: 10px; font-weight: 700; text-transform: uppercase;
                   letter-spacing: 1.5px; color: #E8533F; margin-bottom: 12px; }
  .section p { font-size: 15px; color: #444; }
  .so-what { background: #FFF8F7; border-left: 4px solid #E8533F; padding: 20px 28px; margin: 0; }
  .so-what p { font-size: 15px; font-weight: 500; color: #2D2D2D; }
  .next-steps ul { list-style: none; padding: 0; }
  .next-steps ul li { padding: 6px 0; font-size: 14px; color: #444; }
  .next-steps ul li::before { content: '→ '; color: #E8533F; font-weight: bold; }
  .appendix { background: #F8F8F8; }
  .appendix pre { font-size: 11px; color: #767676; white-space: pre-wrap;
                  font-family: 'Fira Mono', 'Courier New', monospace; background: none; }
  .chart-container { padding: 8px 0; }
</style>
"""


def build_html_story(contract: dict) -> str:
    """Build a standalone HTML story file from a data contract.

    The contract dict supports two modes:
    - Single chart: include chart_type, data, and highlight at the top level.
    - Multi-chart: include a "charts" list, each with its own chart_type/data/highlight.

    Args:
        contract: Dict with story metadata, chart data, narrative, and output_path.
                  See module docstring for full schema examples.

    Returns:
        Absolute path to the generated HTML file (output_path + ".html").

    Raises:
        KeyError: If required keys (data) are missing from a chart contract.
        OSError: If the output directory cannot be created.
    """
    title = contract.get('title', 'Analysis')
    subtitle = contract.get('subtitle', '')
    source = contract.get('source', '')
    collected_at = contract.get('collected_at', '')
    narrative = contract.get('narrative', {})
    context_text = narrative.get('context', '')
    so_what_text = narrative.get('so_what', '')
    next_steps = narrative.get('next_steps', [])
    appendix_query = narrative.get('appendix_query', '')
    charts = contract.get('charts', [contract])
    output_path = contract.get('output_path', '/tmp/story')
    generated_at = datetime.now().strftime('%Y-%m-%d')

    charts_html = ''
    for i, chart_contract in enumerate(charts):
        fig = make_plotly_chart(chart_contract)
        chart_title = chart_contract.get('title', '')
        charts_html += (
            '<div class="section">'
            '<div class="section-label">What the data shows</div>'
        )
        if chart_title and chart_title != title:
            charts_html += (
                f'<p style="font-size:14px;font-weight:600;margin-bottom:12px;">'
                f'{chart_title}</p>'
            )
        include_js = "cdn" if i == 0 else False
        charts_html += (
            f'<div class="chart-container">'
            f'{pio.to_html(fig, full_html=False, include_plotlyjs=include_js)}'
            f'</div></div>'
        )

    next_steps_html = ''
    if next_steps:
        items = ''.join(f'<li>{s}</li>' for s in next_steps)
        next_steps_html = f'''
        <div class="section next-steps">
          <div class="section-label">Next Steps</div>
          <ul>{items}</ul>
        </div>'''

    appendix_html = ''
    if appendix_query or source:
        appendix_html = f'''
        <div class="section appendix">
          <div class="section-label">Appendix — Data Provenance</div>
          <pre>Source: {source}\nCollected: {collected_at}\n\n{appendix_query}</pre>
        </div>'''

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  {CSS}
</head>
<body>
  <div class="story">
    <div class="header">
      <h1>{title}</h1>
      <div class="subtitle">{subtitle}</div>
      <div class="meta">Source: {source} &nbsp;|&nbsp; Collected: {collected_at} &nbsp;|&nbsp; Generated: {generated_at}</div>
    </div>
    {'<div class="section"><div class="section-label">Context</div><p>' + context_text + '</p></div>' if context_text else ''}
    {charts_html}
    {'<div class="so-what section"><div class="section-label">So What</div><p>' + so_what_text + '</p></div>' if so_what_text else ''}
    {next_steps_html}
    {appendix_html}
  </div>
</body>
</html>"""

    out_file = f"{output_path}.html"
    Path(out_file).parent.mkdir(parents=True, exist_ok=True)
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(html)
    return out_file


if __name__ == '__main__':
    # Quick smoke test — generates a single bar chart story
    test = {
        "chart_type": "bar_vertical",
        "title": "Feature activation rate by user segment",
        "subtitle": "30-day activation — Q1 2025",
        "source": "Product analytics — activation_events",
        "collected_at": "2025-01-15",
        "highlight": "power_users",
        "output_path": "/tmp/story_test",
        "data": {
            "labels": ["power_users", "casual_users", "new_users"],
            "values": [0.82, 0.45, 0.21],
        },
        "narrative": {
            "context": (
                "Activation rates vary significantly across user segments. "
                "Power users activate at much higher rates than new users."
            ),
            "so_what": (
                "Power users activate at nearly 4x the rate of new users, "
                "suggesting that onboarding — not the core product — is the key lever to improve."
            ),
            "next_steps": [
                "Run a targeted onboarding experiment for new users",
                "Interview 5 power users to understand their activation path",
                "Review drop-off points in the onboarding funnel",
            ],
            "appendix_query": (
                "SELECT segment, COUNT(*) AS total, SUM(activated) AS activated\n"
                "FROM user_activations\n"
                "WHERE period = '2025-01'\n"
                "GROUP BY segment"
            ),
        },
    }
    path = build_html_story(test)
    print(f"Story generated: {path}")
