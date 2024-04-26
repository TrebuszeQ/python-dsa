import math
from tabulate import tabulate


class BooleanAlgebra:

    @property
    def p(self):
        return self._p

    @property
    def q(self):
        return self._q

    @property
    def res(self):
        return self._res

    @property
    def truth_table(self):
        return self._truth_table

    def __init__(self, num):
        self._p = 1 if num > 0 else 0
        self._q = None
        self._np = 1 - self._p
        self._nq = None
        self._res = None
        self._truth_table = []

    @staticmethod
    def _is_0_or_1(num):
        return 1 if num > 0 else 0

    def __set_table_of_truth(self, l, r):
        eq = 1 if l == r else 0
        self._truth_table = [[self._np, self._p, l, r, eq], [self._p, self._np, l, r, eq]] if self._q is None \
            else [[self._np, self._p, self._nq, self._q, l, r, eq], [self._p, self._np, self._nq, self._q, l, r, eq]]

    def print_table_of_truth(self, title="Truth Table"):
        if self._q is None:
            head = ["p", "~p", "l", "r", "l <=> r"]
            indent = 34

        else:
            head = ["p", "~p", "q", "~q", "l", "r", "l <=> r"]
            indent = 43

        print(title)
        print(tabulate(self._truth_table, headers=head, tablefmt="grid"))
        print("".ljust(indent), self.res)
        print()

    def inversion(self):
        return 1 - (1 - self._p)

    def double_negation(self, print_table: bool = True):
        l = (1 - (1 - self._p))
        r = self._p
        self._res = 1 - (l - r)**2
        self.__set_table_of_truth(l, r)
        if print_table:
            self.print_table_of_truth("Law of Double Negation")
        return self._res

    def excluded_middle(self, print_table: bool = True):
        l = 1 - (1 - self._p) * (1 - (1 - self._p))
        r = 1
        self._res = (1 - (l - r) ** 2)
        self.__set_table_of_truth(l, r)
        if print_table:
            self.print_table_of_truth("Law of Excluded Middle")
        return self._res

    def contradiction(self, print_table: bool = True):
        l = (1 - (self._p & self._np))
        r = 1
        self._res = (1 - (l - r) ** 2)
        self.__set_table_of_truth(l, r)
        if print_table:
            self.print_table_of_truth("Law of Contradiction")
        return self._res

    # Prawo idempotentności alternatywy
    def alternative_simplification(self, print_table: bool = True):
        l = (self._p | self._p)
        r = self._p
        self._res = (1 - (l - r) ** 2)
        self.__set_table_of_truth(l, r)
        if print_table:
            self.print_table_of_truth("Law of Alternative Simplification")
        return self._res

    def conjuction_simplification(self, print_table: bool = True):
        l = (self._p & self._p)
        r = self._p
        self._res = (1 - (l - r) ** 2)
        self.__set_table_of_truth(l, r)
        if print_table:
            self.print_table_of_truth("Law of Conjuction Simplification")
        return self._res

    def first_clavius(self, print_table: bool = True):
        l = self._p
        r = self._np
        self._res = (1 - (l - r) ** 2)
        self.__set_table_of_truth(l, r)

        l2 = self._res
        r2 = self._np
        self._res = (1 - (l2 - r2) ** 2)
        self.__set_table_of_truth(l2, r2)
        if print_table:
            self.print_table_of_truth("First Law of Clavius")
        return self._res

    def second_clavius(self, print_table: bool = True):
        l = self._np
        r = self._p
        self._res = (1 - (l - r) ** 2)

        l2 = self._res
        r2 = self._p
        self._res = (1 - (l2 - r2) ** 2)
        self.__set_table_of_truth(l2, r2)
        if print_table:
            self.print_table_of_truth("Second Law of Clavius")
        return self._res
