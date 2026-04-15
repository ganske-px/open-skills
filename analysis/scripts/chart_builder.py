#!/usr/bin/env python3
"""
Chart Builder
=============
Generates static charts following the Storytelling with Data (SWD) methodology.
Input: data contract JSON. Output: PNG or SVG file at output_path.

Usage
-----
    from chart_builder import build_chart

    contract = {
        "chart_type": "bar_vertical",   # see CHART_DISPATCH for all types
        "title": "Group A has 6x higher rejection rate",
        "subtitle": "Rejection rate — Jan 2026",
        "source": "database — results_table",
        "collected_at": "2026-01-01",
        "highlight": "group_a",         # label to highlight in red
        "output_format": "png",         # png | svg
        "output_path": "/tmp/my_chart", # extension added automatically
        "data": {
            "labels": ["group_a", "group_b"],
            "values": [0.23, 0.036]
        }
    }
    output_file = build_chart(contract)

Supported Chart Types
---------------------
    bar_vertical         — vertical bar chart (labels on x-axis)
    bar_horizontal       — horizontal bar chart (labels on y-axis)
    line                 — single time-series line
    line_multi           — multiple lines; data["series"] = [{label, values}, ...]
    slope                — slope chart for two time points; data["series"] required
    scatter              — scatter plot; data requires "x", "y", optional "labels"
    dot_plot             — lollipop/dot chart (ranking)
    heatmap              — heatmap matrix; data requires "matrix", "x_labels", "y_labels"
    waterfall            — waterfall chart for contribution analysis
    confidence_interval  — horizontal CI visualization (pairs with probability_calculator.py)

Data Contract
-------------
    chart_type    str    — one of the types above
    title         str    — chart title (left-aligned, bold)
    subtitle      str    — optional subtitle beneath title
    source        str    — data source label for footnote
    collected_at  str    — YYYY-MM-DD for footnote
    highlight     str    — label to emphasize with COLOR_HIGHLIGHT (#E8533F by default)
    output_format str    — "png" (default) or "svg"
    output_path   str    — file path without extension
    data          dict   — chart-type-specific data keys (see per-function docstrings)

SWD Style Principles Applied
-----------------------------
    - Neutral color (#C8C8C8) for non-highlighted elements
    - Single highlight color (#E8533F, configurable) for the story element
    - Minimal chart junk: no top/right spines, no grid by default
    - Left-aligned title, subtitle in muted color
    - Data labels directly on elements — no legend when possible

Dependencies
------------
    matplotlib, seaborn, numpy
    Install: pip install matplotlib seaborn numpy
"""
import json
import sys
import math
from pathlib import Path

import matplotlib
matplotlib.use('Agg')  # headless rendering
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import numpy as np

# ---------------------------------------------------------------------------
# SWD color palette (configurable defaults)
# ---------------------------------------------------------------------------
COLOR_NEUTRAL   = '#C8C8C8'
COLOR_HIGHLIGHT = '#E8533F'   # SWD highlight — override via contract["highlight_color"]
COLOR_TEXT      = '#2D2D2D'
COLOR_SUBTITLE  = '#767676'
FONT_FAMILY     = 'DejaVu Sans'


# ---------------------------------------------------------------------------
# Shared style helper
# ---------------------------------------------------------------------------

def apply_swd_base(ax, title, subtitle=None):
    """Remove chart junk and apply SWD base style to any chart axis."""
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_color('#E0E0E0')
    ax.spines['bottom'].set_color('#E0E0E0')
    ax.yaxis.grid(False)
    ax.xaxis.grid(False)
    ax.tick_params(colors=COLOR_SUBTITLE, length=0)
    ax.set_title(title, fontsize=13, fontweight='bold', color=COLOR_TEXT,
                 pad=16, loc='left', wrap=True)
    if subtitle:
        ax.annotate(subtitle, xy=(0, 1.02), xycoords='axes fraction',
                    fontsize=9, color=COLOR_SUBTITLE)


# ---------------------------------------------------------------------------
# Chart renderers
# ---------------------------------------------------------------------------

def bar_vertical(ax, data, highlight, contract):
    """Vertical bar chart. data: {labels, values}"""
    labels = data['labels']
    values = data['values']
    hl_color = contract.get('highlight_color', COLOR_HIGHLIGHT)
    colors = [hl_color if l == highlight else COLOR_NEUTRAL for l in labels]
    bars = ax.bar(labels, values, color=colors, width=0.6, zorder=2)
    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2,
                bar.get_height() + max(values) * 0.01,
                f'{val:.1%}' if max(values) <= 1 else f'{val:,.0f}',
                ha='center', va='bottom', fontsize=9, color=COLOR_TEXT, fontweight='bold')
    ax.set_yticks([])
    ax.spines['left'].set_visible(False)


def bar_horizontal(ax, data, highlight, contract):
    """Horizontal bar chart. data: {labels, values}"""
    labels = data['labels']
    values = data['values']
    hl_color = contract.get('highlight_color', COLOR_HIGHLIGHT)
    colors = [hl_color if l == highlight else COLOR_NEUTRAL for l in labels]
    bars = ax.barh(labels, values, color=colors, height=0.6)
    for bar, val in zip(bars, values):
        ax.text(bar.get_width() + max(values) * 0.01,
                bar.get_y() + bar.get_height() / 2,
                f'{val:.1%}' if max(values) <= 1 else f'{val:,.0f}',
                va='center', fontsize=9, color=COLOR_TEXT, fontweight='bold')
    ax.set_xticks([])
    ax.spines['bottom'].set_visible(False)
    ax.invert_yaxis()


def line(ax, data, highlight, contract):
    """Single time-series line. data: {labels, values}"""
    hl_color = contract.get('highlight_color', COLOR_HIGHLIGHT)
    ax.plot(data['labels'], data['values'],
            color=hl_color, linewidth=2.5, marker='o', markersize=5)
    ax.annotate(
        f"{data['values'][-1]:.1%}" if max(data['values']) <= 1 else f"{data['values'][-1]:,.0f}",
        xy=(len(data['labels']) - 1, data['values'][-1]),
        xytext=(8, 0), textcoords='offset points',
        fontsize=9, color=hl_color, fontweight='bold'
    )
    ax.set_xticks(range(len(data['labels'])))
    ax.set_xticklabels(data['labels'], fontsize=9)


def line_multi(ax, data, highlight, contract):
    """Multiple lines. data: {labels, series: [{label, values}, ...]}"""
    series = data.get('series', [])
    hl_color = contract.get('highlight_color', COLOR_HIGHLIGHT)
    for s in series:
        color = hl_color if s['label'] == highlight else COLOR_NEUTRAL
        lw = 2.5 if color == hl_color else 1.5
        ax.plot(data['labels'], s['values'], color=color, linewidth=lw,
                marker='o', markersize=4 if color == COLOR_NEUTRAL else 5,
                label=s['label'])
        ax.annotate(s['label'], xy=(len(data['labels']) - 1, s['values'][-1]),
                    xytext=(6, 0), textcoords='offset points',
                    fontsize=8, color=color,
                    fontweight='bold' if color == hl_color else 'normal')
    ax.set_xticks(range(len(data['labels'])))
    ax.set_xticklabels(data['labels'], fontsize=9)


def slope(ax, data, highlight, contract):
    """Slope chart for two time points. data: {labels (2 items), series: [{label, values (2)}, ...]}"""
    labels = data['labels']
    series = data.get('series', [])
    hl_color = contract.get('highlight_color', COLOR_HIGHLIGHT)
    x = [0, 1]
    for s in series:
        color = hl_color if s['label'] == highlight else COLOR_NEUTRAL
        lw = 2.5 if color == hl_color else 1.2
        ax.plot(x, s['values'], color=color, linewidth=lw, marker='o', markersize=6)
        fmt = '.1%' if max(s['values']) <= 1 else ',.0f'
        ax.annotate(f"{s['label']}\n{s['values'][0]:{fmt}}",
                    xy=(0, s['values'][0]), xytext=(-12, 0),
                    textcoords='offset points', ha='right', fontsize=8, color=color)
        ax.annotate(f"{s['values'][1]:{fmt}}",
                    xy=(1, s['values'][1]), xytext=(8, 0),
                    textcoords='offset points', ha='left', fontsize=8, color=color)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=10, fontweight='bold')
    ax.set_yticks([])
    ax.spines['left'].set_visible(False)
    ax.set_xlim(-0.3, 1.3)


def scatter(ax, data, highlight, contract):
    """Scatter plot. data: {x, y, optional labels, optional x_label, optional y_label}"""
    x = data['x']
    y = data['y']
    labels = data.get('labels', [])
    hl_color = contract.get('highlight_color', COLOR_HIGHLIGHT)
    colors_list = (
        [hl_color if l == highlight else COLOR_NEUTRAL for l in labels]
        if labels else COLOR_NEUTRAL
    )
    ax.scatter(x, y, c=colors_list, s=60, alpha=0.8, zorder=2)
    if labels:
        for xi, yi, lbl in zip(x, y, labels):
            if lbl == highlight:
                ax.annotate(lbl, (xi, yi), xytext=(6, 4),
                            textcoords='offset points', fontsize=8, color=hl_color)
    ax.set_xlabel(data.get('x_label', ''), fontsize=9, color=COLOR_SUBTITLE)
    ax.set_ylabel(data.get('y_label', ''), fontsize=9, color=COLOR_SUBTITLE)


def dot_plot(ax, data, highlight, contract):
    """Dot/lollipop chart for ranking. data: {labels, values}"""
    labels = data['labels']
    values = data['values']
    hl_color = contract.get('highlight_color', COLOR_HIGHLIGHT)
    y_pos = range(len(labels))
    colors = [hl_color if l == highlight else COLOR_NEUTRAL for l in labels]
    ax.hlines(y_pos, 0, values, colors='#E0E0E0', linewidth=1)
    ax.scatter(values, y_pos, c=colors, s=80, zorder=3)
    for i, (val, lbl) in enumerate(zip(values, labels)):
        fmt = f'{val:.1%}' if max(values) <= 1 else f'{val:,.0f}'
        ax.text(val + max(values) * 0.02, i, fmt, va='center',
                fontsize=9, color=COLOR_TEXT,
                fontweight='bold' if lbl == highlight else 'normal')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, fontsize=9)
    ax.set_xticks([])
    ax.spines['bottom'].set_visible(False)
    ax.invert_yaxis()


def heatmap(ax, data, highlight, contract):
    """Heatmap. data: {matrix (2D list), x_labels, y_labels}"""
    matrix = np.array(data['matrix'])
    x_labels = data.get('x_labels', [])
    y_labels = data.get('y_labels', [])
    sns.heatmap(matrix, ax=ax, annot=True,
                fmt='.1f' if matrix.max() > 1 else '.2f',
                cmap='RdYlGn_r', linewidths=0.5, linecolor='white',
                xticklabels=x_labels, yticklabels=y_labels,
                cbar=False, annot_kws={'size': 8})
    ax.tick_params(axis='both', length=0, labelsize=8)


def waterfall(ax, data, highlight, contract):
    """Waterfall chart. data: {labels, values}. First and last bars treated as totals."""
    labels = data['labels']
    values = data['values']
    hl_color = contract.get('highlight_color', COLOR_HIGHLIGHT)
    running = 0
    bottoms = []
    for v in values:
        bottoms.append(running if v >= 0 else running + v)
        running += v
    colors = [hl_color if v < 0 else '#4CAF50' for v in values]
    colors[0] = COLOR_NEUTRAL
    colors[-1] = COLOR_NEUTRAL
    bars = ax.bar(labels, [abs(v) for v in values], bottom=bottoms, color=colors, width=0.6)
    for bar, val, bot in zip(bars, values, bottoms):
        ax.text(bar.get_x() + bar.get_width() / 2,
                bot + abs(val) + max(abs(v) for v in values) * 0.01,
                f'{val:+,.0f}', ha='center', va='bottom', fontsize=8, color=COLOR_TEXT)


def confidence_interval(ax, data, highlight, contract):
    """Horizontal confidence interval plot. Pairs with probability_calculator.py output.
    data: {labels, values (point estimates), ci_lower, ci_upper}
    """
    labels = data['labels']
    values = data['values']
    ci_lower = data.get('ci_lower', values)
    ci_upper = data.get('ci_upper', values)
    hl_color = contract.get('highlight_color', COLOR_HIGHLIGHT)
    y_pos = range(len(labels))
    colors = [hl_color if l == highlight else COLOR_NEUTRAL for l in labels]
    ax.hlines(y_pos, ci_lower, ci_upper, colors=colors, linewidth=3, alpha=0.4)
    ax.scatter(values, y_pos, c=colors, s=80, zorder=3)
    for i, (val, lo, hi, lbl) in enumerate(zip(values, ci_lower, ci_upper, labels)):
        ax.text(hi + 0.005, i, f'{val:.1%} [{lo:.1%}–{hi:.1%}]',
                va='center', fontsize=8, color=COLOR_TEXT,
                fontweight='bold' if lbl == highlight else 'normal')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, fontsize=9)
    ax.set_xticks([])
    ax.spines['bottom'].set_visible(False)
    ax.invert_yaxis()
    ax.set_xlim(0, max(ci_upper) * 1.4)


# ---------------------------------------------------------------------------
# Dispatch table
# ---------------------------------------------------------------------------

CHART_DISPATCH = {
    'bar_vertical':       bar_vertical,
    'bar_horizontal':     bar_horizontal,
    'line':               line,
    'line_multi':         line_multi,
    'slope':              slope,
    'scatter':            scatter,
    'dot_plot':           dot_plot,
    'heatmap':            heatmap,
    'waterfall':          waterfall,
    'confidence_interval': confidence_interval,
}


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def build_chart(contract: dict) -> str:
    """Build a chart from a data contract and save it to disk.

    Parameters
    ----------
    contract : dict
        Data contract (see module docstring for full schema).

    Returns
    -------
    str
        Absolute path of the saved file (e.g., /tmp/my_chart.png).

    Raises
    ------
    ValueError
        If chart_type is not recognized.
    """
    chart_type    = contract.get('chart_type', 'bar_vertical')
    title         = contract.get('title', '')
    subtitle      = contract.get('subtitle', '')
    data          = contract['data']
    highlight     = contract.get('highlight', '')
    output_format = contract.get('output_format', 'png')
    output_path   = contract.get('output_path', '/tmp/chart')

    if chart_type not in CHART_DISPATCH:
        raise ValueError(
            f"chart_type '{chart_type}' not supported. "
            f"Available types: {list(CHART_DISPATCH.keys())}"
        )

    fig, ax = plt.subplots(figsize=(10, 5))
    fig.patch.set_facecolor('white')

    CHART_DISPATCH[chart_type](ax, data, highlight, contract)
    apply_swd_base(ax, title, subtitle)

    source       = contract.get('source', '')
    collected_at = contract.get('collected_at', '')
    if source:
        fig.text(0.01, 0.01, f'Source: {source} — {collected_at}',
                 fontsize=7, color=COLOR_SUBTITLE, style='italic')

    plt.tight_layout(rect=[0, 0.04, 1, 1])

    out_file = f"{output_path}.{output_format}"
    Path(out_file).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out_file, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    return out_file


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    test_bar = {
        "chart_type": "bar_vertical",
        "title": "Group with incident has 6x higher rejection rate",
        "subtitle": "Rejection rate — Jan 2026",
        "source": "database — results_table",
        "collected_at": "2026-01-01",
        "highlight": "with_incident",
        "output_format": "png",
        "output_path": "/tmp/test_bar",
        "data": {
            "labels": ["with_incident", "without_incident"],
            "values": [0.23, 0.036]
        }
    }
    path = build_chart(test_bar)
    print(f"Bar chart saved: {path}")

    test_ci = {
        "chart_type": "confidence_interval",
        "title": "Rejection rate 6x higher in incident group (95% CI)",
        "subtitle": "Rejection rate — Jan 2026",
        "source": "probability_calculator.py",
        "collected_at": "2026-01-01",
        "highlight": "with_incident",
        "output_format": "png",
        "output_path": "/tmp/test_ci",
        "data": {
            "labels": ["with_incident", "without_incident"],
            "values": [0.23, 0.036],
            "ci_lower": [0.205, 0.031],
            "ci_upper": [0.257, 0.042]
        }
    }
    path2 = build_chart(test_ci)
    print(f"CI chart saved: {path2}")
