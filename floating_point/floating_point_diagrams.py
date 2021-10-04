import numpy as np
from matplotlib.patches import Circle, Wedge, Polygon
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt

from mpl_sizes import get_format
from dataclasses import dataclass

import seaborn as sns

__all__ = [
    "get_format",
    "get_ax",
    "draw_floating_point_repr_as_boxes",
    "plot_precision",
    "formats",
    "FPFormat",
]


@dataclass
class FPFormat:
    name: str
    sign_bits: int
    exponent_bits: int
    significand_bits: int


def get_ax(
    figsize=None,
    nrows=1,
    ncols=1,
    right_spine=False,
    left_spine=True,
    top_spine=False,
    bottom_spine=True,
):
    if figsize is None:
        formatter = get_format("InfThesis")
        figsize = formatter.text_width_plot(aspect_ratio="normal")

    _, ax = plt.subplots(nrows, ncols, figsize=figsize)

    if nrows * ncols > 1:
        axs = ax.ravel()
    else:
        axs = [ax]

    for ax in axs:
        # Remove ticks and labels
        ax.tick_params(
            left=left_spine,
            labelleft=left_spine,
            bottom=bottom_spine,
            labelbottom=bottom_spine,
        )

        # Hide the right and top spines
        ax.spines["right"].set_visible(right_spine)
        ax.spines["top"].set_visible(top_spine)
        ax.spines["bottom"].set_visible(bottom_spine)
        ax.spines["left"].set_visible(left_spine)

    if nrows * ncols > 1:
        return axs
    else:
        return ax


def draw_floating_point_repr_as_boxes(fp_format, box_width=1):

    total_bits = (
        fp_format.sign_bits + fp_format.exponent_bits + fp_format.significand_bits
    )

    """
    Format the figure size
    """
    box_height = box_width
    figsize = (total_bits * box_width, box_height)
    ax = get_ax(figsize)
    ax.set_xlim(0, total_bits)
    ax.set_ylim(-0.5, box_height)  # room for annotations

    """
    Generate coloured boxes
    """
    sign_colour, exponent_colour, significant_colour = sns.color_palette("viridis", 3)

    colours = (
        [sign_colour] * fp_format.sign_bits
        + [exponent_colour] * fp_format.exponent_bits
        + [significant_colour] * fp_format.significand_bits
    )

    patches = []

    for i in np.arange(0, total_bits, box_width):
        polygon = Polygon(
            [
                [i + 0.1, 0],
                [i + 0.1, box_height],
                [i + box_width, box_height],
                [i + box_width, 0],
            ],
            closed=True,
            color=colours[i],
        )

        patches.append(polygon)

    patch_collection = PatchCollection(patches, match_original=True)
    ax.add_collection(patch_collection)

    return ax


def plot_precision(fp: FPFormat, ax=None):
    """Line plot of precision for a floating point representation

    Args:
        fp ([FPFormat]): [description]
        ax ([type], optional): [description]. Defaults to None.
    """
    x = []
    y = []

    for exponent in range(fp.exponent_bits):
        upper = 2 ** (exponent + 1)
        lower = 2 ** (exponent)
        precision = (upper - lower) / 2 ** (fp.significand_bits)

        x.append(lower)
        x.append(upper)

        y.append(1 / precision)
        y.append(1 / precision)

    if ax is None:
        formatter = get_format("InfThesis")
        ax = get_ax(
            formatter.text_width_plot(aspect_ratio="equal"),
            left_spine=True,
            bottom_spine=True,
        )

    ax.plot(x, y, label=fp.name)
    ax.fill_between(x, y, alpha=0.1)

    ax.set_xlabel("Exponent")
    ax.set_ylabel("Precision")


formats = [
    FPFormat("FP16", 1, 5, 10),
    FPFormat("BrainFloat16", 1, 8, 7),
    FPFormat("TensorFloat32", 1, 8, 10),
]




# +
"""
Actual plotting and figure saving happens here

1. Plot overlaps of the precisions
"""


for fpX in formats:
    ax = get_ax()
    plot_precision(fpX, ax=ax)
    
    ax.set_title(fpX.name)
    ax.set_yscale("log")

    plt.savefig(f"figs/{fpX.name}.pdf")
# -


