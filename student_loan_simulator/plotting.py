"""
Functions providing plotting functionality.
"""

import matplotlib; matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import datetime
import os


FIGURE_FILE = "graph.png"


def _ax_line(k, v, color, label):
    return {k: v, 'color': color, 'linestyle': '-', 'alpha': 0.3, 'label': label}

def _axvline(x, color, label):
    return _ax_line('x', x, color, label)

def _axhline(y, color, label):
    return _ax_line('y', y, color, label)


def make_plot(salary, initial_balance, max_monthly_repayments, repayments):
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
    ax.set_xlim([0, max_monthly_repayments])
    ax.plot(x, y)

    # Horizontal lines
    ax.axhline(**_axhline(initial_balance, 'y', 'Initial balance'))
    ax.axhline(**_axhline(default.total, 'r', 'Default total'))
    ax.axhline(**_axhline(maximum.total, 'c', 'Maximum total'))

    # Vertical lines
    ax.axvline(**_axvline(maximum.monthly, 'm', 'Maximum monthly'))
    if threshold is not None:
        ax.axvline(**_axvline(threshold.monthly, 'g', 'Threshold monthly'))

    ax.legend(loc='best')

    return fig


def save_plot(figure, output_dir):
    output_path = os.path.join(output_dir, FIGURE_FILE)

    figure.savefig(output_path, dpi=300, pad_inches=0.5, bbox_inches="tight")

