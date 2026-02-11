"""
Gaussian vs Fat‑Tailed Distributions
------------------------------------

This module provides a clear, quantitative comparison between:

    • Normal (Gaussian)
    • Laplace (Double Exponential)
    • Student‑t

It includes:
    – PDF implementations
    – Tail‑behavior intuition
    – A comparison plot
    – Explanatory comments suitable for quant‑finance or statistics repos
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, laplace, t


# ============================================================
# 1. Probability Density Functions
# ============================================================

def pdf_normal(x, mu=0, sigma=1):
    """Gaussian PDF."""
    return norm.pdf(x, loc=mu, scale=sigma)


def pdf_laplace(x, mu=0, b=1):
    """Laplace (double exponential) PDF."""
    return laplace.pdf(x, loc=mu, scale=b)


def pdf_student_t(x, df=3):
    """Student‑t PDF with degrees of freedom df."""
    return t.pdf(x, df=df)


# ============================================================
# 2. Tail Explanation (Text)
# ============================================================

TAIL_EXPLANATION = """
Tail Behavior Summary
---------------------

1. Gaussian (Normal)
   - Tails decay as exp(-x^2)
   - Extremely thin tails
   - Extreme events are *rare*
   - Underestimates risk in finance

2. Laplace (Double Exponential)
   - Tails decay as exp(-|x|)
   - Heavier than Gaussian
   - Captures shocks, jumps, sparsity

3. Student‑t
   - Tails decay as power law: (1 + x^2/df)^(-(df+1)/2)
   - Very heavy tails for small df
   - Excellent for financial returns, robust modeling
"""


# ============================================================
# 3. Plotting Function
# ============================================================

def plot_distributions(xmin=-8, xmax=8, df=3, save_path=None):
    """
    Plot Normal vs Laplace vs Student‑t on the same axis.
    """

    x = np.linspace(xmin, xmax, 2000)

    plt.figure(figsize=(10, 6))
    plt.plot(x, pdf_normal(x), label="Normal (μ=0, σ=1)", linewidth=2)
    plt.plot(x, pdf_laplace(x), label="Laplace (μ=0, b=1)", linewidth=2)
    plt.plot(x, pdf_student_t(x, df=df), label=f"Student‑t (df={df})", linewidth=2)

    plt.yscale("log")  # log scale highlights tail differences
    plt.title("Gaussian vs Fat‑Tailed Distributions")
    plt.xlabel("x")
    plt.ylabel("PDF (log scale)")
    plt.grid(True, alpha=0.3)
    plt.legend()

    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")

    plt.show()


# ============================================================
# 4. Example Usage
# ============================================================

if __name__ == "__main__":
    print(TAIL_EXPLANATION)
    plot_distributions(df=3)