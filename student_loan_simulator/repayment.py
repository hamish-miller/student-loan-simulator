"""
Student loan repayment thresholds history.

Sources:
    https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2019-to-2020
    https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2018-to-2019
    ...
"""

from statistics import mean


# Plan 2
repayment_thresholds = {
    "2019-2020": 25725,
    "2018-2019": 25000,
    "2017-2018": 21000,
    "2016-2017": 21000,
}

REPAYMENT_THRESHOLD_ESTIMATE = int(mean(repayment_thresholds.values()))

REPAYMENT_PERCENT = 9


def automatic_repayment(salary):
    liable_salary = salary - REPAYMENT_THRESHOLD_ESTIMATE

    return (liable_salary * (REPAYMENT_PERCENT / 100)) / 12


# Unused but provided
repayment_thresholds_plan_1 = {
    "2019-2020": 18935,
    "2018-2019": 18330,
    "2017-2018": 17775,
    "2016-2017": 17495,
}
