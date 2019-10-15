#!/usr/bin/env python
"""
Simulate the impact of making additional voluntary payments to a student loan.
"""

from .config import open_config, save_config
from .metadata import save_metadata
from .plotting import make_plot, save_plot
from .simulation import simulate, analyse_repayments, save_results
from .student_loan import StudentLoan

OUTPUT_DIR = "results"


def main():
    config = open_config()

    salary = config.getint("required", "salary")
    initial_balance = config.getint("required", "initial_balance")

    student_loan = StudentLoan(initial_balance, salary)

    repayments = simulate(student_loan)
    analysis = analyse_repayments(repayments)

    figure = make_plot(salary, initial_balance, repayments)

    save_config(config, OUTPUT_DIR)
    save_results(repayments, analysis, OUTPUT_DIR)
    save_plot(figure, OUTPUT_DIR)
    save_metadata(OUTPUT_DIR)


if __name__ == "__main__":
    main()
