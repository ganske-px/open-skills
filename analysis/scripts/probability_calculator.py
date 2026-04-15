#!/usr/bin/env python3
"""
Probability Calculator
======================
Parameterized probability calculator driven by a data contract.
Invoked by the probability-analysis skill.

Usage
-----
    from probability_calculator import calculate

    data = {
        "question": "Do users with a prior incident have a higher rejection rate?",
        "calculation_type": "comparison",   # simple | conditional | bayesian | poisson | comparison
        "confidence_level": 0.95,
        "source": "database",
        "collected_at": "2026-01-01",
        "data": {
            "groups": [
                {"label": "with_incident",    "n": 1000, "successes": 230},
                {"label": "without_incident", "n": 5000, "successes": 180}
            ]
        }
    }
    result = calculate(data)

Data Contract
-------------
    question         str   — natural-language question being answered
    calculation_type str   — one of: simple, conditional, bayesian, poisson, comparison
    confidence_level float — e.g. 0.95 (default)
    source           str   — data provenance label
    collected_at     str   — YYYY-MM-DD
    data.groups      list  — each entry: {label, n, successes}
    data.prior       dict  — {alpha, beta} only for bayesian (default: Beta(1,1))

Output Schema
-------------
    {
      "question": str,
      "calculation_type": str,
      "results": [
        {
          "label": str,
          "probability": float,
          "ci_lower": float,
          "ci_upper": float,
          "ci_level": float,
          "n": int,            # simple / conditional / comparison only
          "successes": int,    # simple / conditional / comparison only
          "method": str        # wilson | bayesian-hdi | poisson-garwood
        }
      ],
      "comparison": {          # null unless calculation_type == "comparison"
        "group_a": str,
        "group_b": str,
        "rate_a": float,
        "rate_b": float,
        "relative_risk": float | null,
        "risk_difference": float,
        "test": "chi-square",
        "chi2": float,
        "p_value": float,
        "significant": bool
      } | null,
      "metadata": {
        "source": str,
        "collected_at": str,
        "calculated_at": str,
        "confidence_level": float,
        "warnings": list[str]
      }
    }

Dependencies
------------
    Standard library: json, math, datetime
    Optional (improves accuracy): scipy, numpy

    If scipy is not available the calculator falls back to normal-approximation
    for Bayesian HDI and lookup-table p-values for chi-square.
"""
import json
import math
from datetime import datetime


# ---------------------------------------------------------------------------
# Core statistical functions
# ---------------------------------------------------------------------------

def wilson_ci(successes: int, n: int, z: float = 1.96) -> tuple:
    """Wilson score confidence interval for proportions."""
    if n == 0:
        return (0.0, 1.0)
    p = successes / n
    denom = 1 + z**2 / n
    center = (p + z**2 / (2 * n)) / denom
    margin = z * math.sqrt(p * (1 - p) / n + z**2 / (4 * n**2)) / denom
    return (max(0.0, center - margin), min(1.0, center + margin))


def bayesian_beta(alpha: float, beta_param: float, credible: float = 0.95) -> tuple:
    """Beta posterior: mean and HDI (highest density interval).

    Returns (mean, lower_bound, upper_bound).
    Uses scipy.stats.beta when available; falls back to normal approximation.
    """
    mean = alpha / (alpha + beta_param)
    try:
        from scipy import stats
        lower, upper = stats.beta.ppf(
            [(1 - credible) / 2, 1 - (1 - credible) / 2],
            alpha, beta_param
        )
    except ImportError:
        var = (alpha * beta_param) / ((alpha + beta_param) ** 2 * (alpha + beta_param + 1))
        std = math.sqrt(var)
        z = {0.90: 1.645, 0.95: 1.96, 0.99: 2.576}.get(credible, 1.96)
        lower = max(0.0, mean - z * std)
        upper = min(1.0, mean + z * std)
    return (mean, float(lower), float(upper))


def chi_square_test(group_a: dict, group_b: dict) -> dict:
    """Chi-square test for independence between two proportions.

    Returns test statistic, p-value, and significance flag.
    """
    a_s = group_a["successes"]
    a_n = group_a["n"]
    b_s = group_b["successes"]
    b_n = group_b["n"]
    a_f = a_n - a_s
    b_f = b_n - b_s
    total = a_n + b_n
    total_s = a_s + b_s
    total_f = a_f + b_f

    if total_s == 0 or total_f == 0:
        return {
            "test": "chi-square",
            "chi2": 0.0,
            "p_value": 1.0,
            "significant": False,
            "note": "no variation between groups"
        }

    e_a_s = a_n * total_s / total
    e_a_f = a_n * total_f / total
    e_b_s = b_n * total_s / total
    e_b_f = b_n * total_f / total

    chi2 = sum(
        (obs - exp) ** 2 / exp
        for obs, exp in [(a_s, e_a_s), (a_f, e_a_f), (b_s, e_b_s), (b_f, e_b_f)]
        if exp > 0
    )

    try:
        from scipy import stats
        p_value = float(1 - stats.chi2.cdf(chi2, df=1))
    except ImportError:
        # Lookup-table approximation (df=1 critical values)
        if chi2 > 10.83:
            p_value = 0.001
        elif chi2 > 6.63:
            p_value = 0.01
        elif chi2 > 3.84:
            p_value = 0.05
        else:
            p_value = 0.5

    return {
        "test": "chi-square",
        "chi2": round(chi2, 4),
        "p_value": round(p_value, 4),
        "significant": p_value < 0.05
    }


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def calculate(data: dict) -> dict:
    """Run the appropriate statistical calculation from a data contract.

    Parameters
    ----------
    data : dict
        Validated data contract (see module docstring for schema).

    Returns
    -------
    dict
        Results JSON following the output schema described in the docstring.
    """
    calc_type = data.get("calculation_type", "simple")
    groups = data["data"]["groups"]
    confidence_level = data.get("confidence_level", 0.95)
    z = {0.90: 1.645, 0.95: 1.96, 0.99: 2.576}.get(confidence_level, 1.96)

    warnings = []
    results = []
    comparison = None

    for group in groups:
        n = group["n"]
        s = group["successes"]
        label = group["label"]

        if n == 0:
            warnings.append(f"Group '{label}' has n=0 — skipped.")
            continue
        if n < 30:
            warnings.append(f"Small sample for '{label}' (n={n}). Intervals may be imprecise.")
        if s > n:
            warnings.append(f"Group '{label}': successes ({s}) > n ({n}). Check your data.")
            s = n

        if calc_type == "bayesian":
            prior = data["data"].get("prior", {"alpha": 1, "beta": 1})
            alpha_post = prior["alpha"] + s
            beta_post = prior["beta"] + (n - s)
            mean, ci_lower, ci_upper = bayesian_beta(alpha_post, beta_post, confidence_level)
            results.append({
                "label": label,
                "probability": round(mean, 4),
                "ci_lower": round(ci_lower, 4),
                "ci_upper": round(ci_upper, 4),
                "ci_level": confidence_level,
                "method": "bayesian-hdi",
                "posterior": {"alpha": alpha_post, "beta": beta_post}
            })

        elif calc_type == "poisson":
            # n = time units (days, weeks), successes = observed events
            rate = s / n
            try:
                from scipy import stats
                ci_lower = float(stats.chi2.ppf((1 - confidence_level) / 2, 2 * s) / 2)
                ci_upper = float(stats.chi2.ppf(1 - (1 - confidence_level) / 2, 2 * (s + 1)) / 2)
                # Normalize by n to express as a rate
                ci_lower /= n
                ci_upper /= n
            except ImportError:
                ci_lower, ci_upper = wilson_ci(s, n, z)
            results.append({
                "label": label,
                "rate_per_unit": round(rate, 4),
                "probability": round(rate, 4),
                "ci_lower": round(ci_lower, 4),
                "ci_upper": round(ci_upper, 4),
                "ci_level": confidence_level,
                "method": "poisson-garwood"
            })

        else:
            # simple, conditional, comparison — all use Wilson CI
            p = s / n
            ci_lower, ci_upper = wilson_ci(s, n, z)
            results.append({
                "label": label,
                "probability": round(p, 4),
                "ci_lower": round(ci_lower, 4),
                "ci_upper": round(ci_upper, 4),
                "ci_level": confidence_level,
                "n": n,
                "successes": s,
                "method": "wilson"
            })

    # Comparison block — only when calc_type == "comparison" and >= 2 groups
    if calc_type == "comparison" and len(groups) >= 2:
        g_a = groups[0]
        g_b = groups[1]
        p_a = g_a["successes"] / g_a["n"] if g_a["n"] > 0 else 0
        p_b = g_b["successes"] / g_b["n"] if g_b["n"] > 0 else 0
        rr = round(p_a / p_b, 4) if p_b > 0 else None
        rd = round(p_a - p_b, 4)
        chi = chi_square_test(g_a, g_b)
        comparison = {
            "group_a": g_a["label"],
            "group_b": g_b["label"],
            "rate_a": round(p_a, 4),
            "rate_b": round(p_b, 4),
            "relative_risk": rr,
            "risk_difference": rd,
            **chi
        }

    return {
        "question": data.get("question", ""),
        "calculation_type": calc_type,
        "results": results,
        "comparison": comparison,
        "metadata": {
            "source": data.get("source", "unknown"),
            "collected_at": data.get("collected_at", "unknown"),
            "calculated_at": datetime.now().strftime("%Y-%m-%d"),
            "confidence_level": confidence_level,
            "warnings": warnings
        }
    }


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    test = {
        "question": "Do users with a prior incident have a higher rejection rate?",
        "calculation_type": "comparison",
        "confidence_level": 0.95,
        "source": "test",
        "collected_at": "2026-01-01",
        "data": {
            "groups": [
                {"label": "with_incident",    "n": 1000, "successes": 230},
                {"label": "without_incident", "n": 5000, "successes": 180}
            ]
        }
    }
    print(json.dumps(calculate(test), indent=2, ensure_ascii=False))
