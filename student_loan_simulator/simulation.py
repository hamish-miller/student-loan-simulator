"""
Model the total repayment.
"""

from collections import namedtuple
import json
import os

RESULTS_FILE = "results.json"
ANALYSIS_FILE = "analysis.json"

MAX_YEARS = 30
MAX_MONTHS = MAX_YEARS * 12

Repayment = namedtuple("Repayment", ("monthly", "total"))


def _total_repaid(student_loan, voluntary_repayment):
    student_loan.reset()
    student_loan.set_voluntary_payment(voluntary_repayment)
    months = 0

    while student_loan.balance > 0 and months < MAX_MONTHS:
        student_loan.recalculate_balance()
        months += 1

    if student_loan.balance < 0:
        student_loan.fix_overpay()

    return Repayment(voluntary_repayment, student_loan.total_repaid)


def simulate(student_loan):
    repayments = range(0, student_loan.initial_balance, 10)

    total_repayments = [_total_repaid(student_loan, r) for r in repayments]

    student_loan.reset()

    return total_repayments


def analyse_repayments(repayments):
    default = repayments[0]
    maximum = max(repayments, key=lambda r: r.total)

    threshold_itr = (r for r in repayments[1:] if r.total <= default.total)
    threshold = next(threshold_itr, None)

    return {
        "default": default,
        "maximum": maximum,
        "threshold": threshold,
    }


def save_results(repayments, analysis, output_dir):
    results_path = os.path.join(output_dir, RESULTS_FILE)
    results = {"repayments": repayments}

    with open(results_path, 'w') as f:
        json.dump(results, f)

    analysis_path = os.path.join(output_dir, ANALYSIS_FILE)

    with open(analysis_path, 'w') as f:
        json.dump(analysis, f)
