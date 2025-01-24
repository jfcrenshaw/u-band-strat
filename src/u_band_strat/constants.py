"""constants for plotting"""

from pathlib import Path

data_dir = Path(__file__).parents[2] / "data"
fig_dir = Path(__file__).parents[2] / "figures"

single_col = (3.3, 3.2)
double_col = (7, 3)
colors = dict(
    u="C4",
    g="C0",
    r="C2",
    i="C1",
    z="C3",
    y="C5",
    black="#262626",
)
cmaps = dict(
    u="Purples",
    g="Blues",
    r="Greens",
    i="Oranges",
    z="Reds",
)
det_bands = dict(
    u="r",
    g="i",
    r="z",
    i="z",
    z="y",
)
