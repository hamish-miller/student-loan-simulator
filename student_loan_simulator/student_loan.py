"""
StudentLoan class
"""

from .interest import interest_rate
from .repayment import automatic_repayment


class StudentLoan:
    def __init__(self, initial_balance, salary):
        self.initial_balance = initial_balance
        self.interest_rate = interest_rate(salary)
        self.automatic_repayment = automatic_repayment(salary)

        self.reset()


    def reset(self):
        self.balance = self.initial_balance
        self.total_repaid = 0
        self.voluntary_repayment = 0


    def set_voluntary_payment(self, voluntary_repayment):
        self.voluntary_repayment = voluntary_repayment


    def recalculate_balance(self):
        self._apply_interest()
        self._make_repayment()


    def _apply_interest(self):
        interest = self.balance * (self.interest_rate / 100) / 12

        self.balance += interest


    def _make_repayment(self):
        repayment = self.automatic_repayment + self.voluntary_repayment

        self.balance -= repayment
        self.total_repaid += repayment


    def fix_overpay(self):
        self.total_repaid -= abs(self.balance)
        self.balance = 0
