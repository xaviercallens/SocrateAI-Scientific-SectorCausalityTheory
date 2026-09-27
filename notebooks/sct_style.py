"""Shared plotting style and paths for the Sector Causality Theory notebooks.

Colors are the first three categorical slots of a CVD-validated palette (blue, orange, aqua), used
in that fixed order and never cycled. Aqua sits below 3:1 contrast on the light surface, so every
figure that uses it also carries direct labels and a printed table of the plotted numbers.
"""
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt

REPO = Path(__file__).resolve().parent.parent
DATA = REPO / "data"
FIGURES = REPO / "notebooks" / "figures"
FIGURES.mkdir(parents=True, exist_ok=True)

BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
INK, INK_2, MUTED, GRID = "#0b0b0b", "#52514e", "#8a8984", "#e6e5e1"
SURFACE = "#fcfcfb"


def apply():
    mpl.rcParams.update({
        "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "savefig.facecolor": SURFACE,
        "axes.edgecolor": MUTED, "axes.labelcolor": INK_2, "text.color": INK,
        "xtick.color": INK_2, "ytick.color": INK_2,
        "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.8,
        "axes.spines.top": False, "axes.spines.right": False,
        "lines.linewidth": 2.0, "lines.markersize": 7,
        "font.size": 11, "axes.titlesize": 12, "axes.titleweight": "bold",
        "legend.frameon": False, "figure.dpi": 110, "savefig.dpi": 150, "axes.axisbelow": True,
    })


def save(fig, name):
    """Save a figure to notebooks/figures/<name>.png and return the path."""
    path = FIGURES / f"{name}.png"
    fig.savefig(path, bbox_inches="tight")
    return path


def plain_log_ticks(axis, ticks):
    """Replace matplotlib's 4×10^0-style log tick labels with plain numbers at chosen positions."""
    from matplotlib.ticker import FixedLocator, FuncFormatter, NullLocator
    axis.set_major_locator(FixedLocator(ticks))
    axis.set_minor_locator(NullLocator())
    axis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:g}"))
