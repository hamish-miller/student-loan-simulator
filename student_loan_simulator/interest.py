"""
Interest rates history

Source:
    https://www.moneysavingexpert.com/students/repay-post-2012-student-loan/
"""

from statistics import mean

RPIs = {
    "2019-2020": 2.4,
    "2018-2019": 3.3,
    "2017-2018": 3.1,
    "2016-2017": 1.6,
    "2015-2016": 0.9,
    "2014-2015": 2.5,
    "2013-2014": 3.3,
    "2012-2013": 3.6,
}

RPI_ESTIMATE = mean(RPIs.values())

MIN_SALARY = 25725
MAX_SALARY = 46305
SALARY_RANGE = MAX_SALARY - MIN_SALARY

MAX_EXTRA_PERCENT = 3


def interest_rate(salary):
    if salary < MIN_SALARY:
        return RPI_ESTIMATE

    if salary > MAX_SALARY:
        return RPI_ESTIMATE + MAX_EXTRA_PERCENT

    extra_percent = ((salary - MIN_SALARY) / SALARY_RANGE) * MAX_EXTRA_PERCENT

    return RPI_ESTIMATE + extra_percent
