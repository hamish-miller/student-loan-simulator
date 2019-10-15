"""
Functions providing plotting functionality.
"""

import matplotlib; matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import datetime
import os


FIGURE_FILE = "graph.png"


def _ax_line(k, v, color):
    return {k: v, 'color': color, 'linestyle': '-', 'alpha': 0.3}

def _axvline(x, color):
    return _ax_line('x', x, color)

def _axhline(y, color):
    return _ax_line('y', y, color)


def make_plot(salary, initial_balance, repayments):
    default = repayments[0]
    maximum = max(repayments, key=lambda r: r.total)
    threshold = next((r for r in repayments[1:] if r.total <= default.total), None)

    x, y = [r.monthly for r in repayments], [r.total for r in repayments]

    # Figure
    fig = plt.figure()
    fig.suptitle("Total Repayment vs Voluntary Repayments")

    # Subplot
    ax = fig.add_subplot(111)
    ax.set_xlabel("Voluntary Payment per Month (£/mth)")
    ax.set_ylabel("Total Repayment (£)")
    ax.grid(True, which="both")

    ax.plot(x, y)

    # Horizontal lines
    ax.axhline(**_axhline(initial_balance, 'y'))
    ax.axhline(**_axhline(default.total, 'r'))
    ax.axhline(**_axhline(maximum.total, 'r'))

    # Vertical lines
    ax.axvline(**_axvline(maximum.monthly, 'r'))
    if threshold is not None:
        ax.axvline(**_axvline(threshold.monthly, 'g'))

    return fig


def save_plot(figure, output_dir):
    output_path = os.path.join(output_dir, FIGURE_FILE)

    figure.savefig(output_path)

