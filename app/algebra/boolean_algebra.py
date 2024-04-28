import math
from tabulate import tabulate


class BooleanAlgebra:
    @staticmethod
    def make_table_of_truth_multiple_values(values_p: [], result, truth_table, values_q:[] =None):
        truth_table_multi = []

        if values_q is None:
            for value in values_p:
                truth_table_multi.append(truth_table)


    @staticmethod
    def make_table_of_truth(p, np, l, r, res, q=None, nq=None):
        truth_table = [[1, np, p, l, r, res], [2, p, np, l, r, res]] if q is None \
            else [[1, np, p, nq, q, l, r, res], [2, p, np, nq, q, l, r, res]]

        return truth_table

    @staticmethod
    def print_table_of_truth(truth_table, res, res_str, l_str, r_str, q=None, title="Truth Table"):
        if q is None:
            head = ["no.", "p", "~p", l_str, r_str, res_str]

        else:
            head = ["no.", "p", "~p", "q", "~q", l_str, r_str, f"{l_str} <=> {r_str}"]

        print(title)
        print(tabulate(truth_table, headers=head, tablefmt="grid"))
        print(f"result: {res}")

        print()

    @staticmethod
    def inversion(p):
        return 1 - (1 - p)

    @staticmethod
    def double_negation(x, print_table: bool = True):
        p = 1 if x > 0 else 0
        np = 0 if x > 1 else 1
        res_str = "[~(~p)] <=> p"

        l_str = "~(~p)"
        l = (1 - (1 - p))

        r_str = "p"
        r = p

        res = 1 - (l - r) ** 2
        truth_table = BooleanAlgebra.make_table_of_truth(p, np, l, r)

        if print_table:
            BooleanAlgebra.print_table_of_truth(truth_table, res, res_str, l_str, r_str, title="Law of Double Negation")

        return res

    @staticmethod
    def excluded_middle(x, print_table: bool = True):
        p = 1 if x > 0 else 0
        np = 0 if x > 1 else 1
        res_str = "[p | (~p)] <=> 1"

        l_str = "[p | (~p)]"
        l = 1 - (1 - p) * (1 - (1 - p))

        r_str = "1"
        r = 1

        res = (1 - (l - r) ** 2)
        truth_table = BooleanAlgebra.make_table_of_truth(p, np, l, r)
        if print_table:
            BooleanAlgebra.print_table_of_truth(truth_table, res, res_str, l_str, r_str, title="Law of Excluded Middle")

        return res

    @staticmethod
    def contradiction(x, print_table: bool = True):
        p = 1 if x > 0 else 0
        np = 0 if x > 1 else 1
        res_str = "[~(p & ~p)] <=> 1"

        l_str = "~(p & ~p)"
        l = (1 - (p & np))

        r_str = "1"
        r = 1

        res = (1 - (l - r) ** 2)
        truth_table = BooleanAlgebra.make_table_of_truth(p, np, l, r)
        if print_table:
            BooleanAlgebra.print_table_of_truth(truth_table, res, res_str, l_str, r_str, title="Law of Contradiction")

        return res

    # Prawo idempotentności alternatywy
    @staticmethod
    def alternative_simplification(x, print_table: bool = True):
        p = 1 if x > 0 else 0
        np = 0 if x > 1 else 1
        res_str = "(p | p) <=> p"

        l_str = "(p | p)"
        l = (p | p)

        r_str = "p"
        r = p

        res = (1 - (l - r) ** 2)
        truth_table = BooleanAlgebra.make_table_of_truth(p, np, l, r)
        if print_table:
            BooleanAlgebra.print_table_of_truth(truth_table, res, res_str, l_str, r_str, title="Law of Alternative Simplification")

        return res

    @staticmethod
    def conjuction_simplification(x, print_table: bool = True):
        p = 1 if x > 0 else 0
        np = 0 if x > 1 else 1
        res_str = "(p & ~p) <=> p"

        l_str = "(p & p)"
        l = (p & p)

        r_str = "p"
        r = p

        res = (1 - (l - r) ** 2)
        truth_table = BooleanAlgebra.make_table_of_truth(p, np, l, r)
        if print_table:
            BooleanAlgebra.print_table_of_truth(truth_table, res, res_str, l_str, r_str, title="Law of Conjuction Simplification")

        return res

    @staticmethod
    def first_law_of_clavius(x, print_table: bool = True):
        p = 1 if x > 0 else 0
        np = 0 if x > 1 else 1
        res_str = "(p => ~p) => ~p"

        l_str = "(p => ~p)"
        l = 1 - (p & (1 - np))

        r_str = "(~p)"
        r = np

        res = (1 - (l - r) ** 2)
        truth_table = BooleanAlgebra.make_table_of_truth(p, np, l, r)
        if print_table:
            BooleanAlgebra.print_table_of_truth(truth_table, res, res_str, l_str, r_str, title="First Law of Clavius")

        return res

    @staticmethod
    def second_law_of_clavius(x, print_table: bool = True):
        p = 1 if x > 0 else 0
        np = 0 if x > 1 else 1
        res_str = "(~p => p) => p"

        l_str = "(~p => p)"
        l = 1 - (np & (1 - p))

        r_str = "p"
        r = p

        res = (1 - (l - r) ** 2)
        truth_table = BooleanAlgebra.make_table_of_truth(p, np, l, r)
        if print_table:
            BooleanAlgebra.print_table_of_truth(truth_table, res, res_str, l_str, r_str, title="Second Law of Clavius")

        return res

    @staticmethod
    def law_of_duns_scotus(x, y, print_table: bool = True):
        p = 1 if x > 0 else 0
        np = 0 if x > 1 else 1
        q = 1 if y > 0 else 0
        nq = 0 if y > 1 else 1
        res_str = "(~p => p) => p"

        l_str = "(~q)"
        l = 1 - q

        r_str = "(q => p)"
        r = 1 - (q & (1 - p))

        res = 1 - (l & (1 - r))
        truth_table = BooleanAlgebra.make_table_of_truth(p, np, l, r, q, nq)
        if print_table:
            BooleanAlgebra.print_table_of_truth(truth_table, res, res_str, l_str, r_str, q, title="Law of Duns Scotus")

        return res

    @staticmethod
    def first_law_of_simplification(x, y, print_table: bool = True):
        p = 1 if x > 0 else 0
        np = 0 if x > 1 else 1
        q = 0 if y > 1 else 0
        nq = 0 if y > 1 else 1
        res_str = "(~q) => (q => p)"

        l_str = "q"
        l = q

        r_str = "(q => p)"
        r = 1 - (p & 1 - q)

        res = 1 - (l & (1 - r))
        truth_table = BooleanAlgebra.make_table_of_truth(p, np, l, r, q, nq)
        if print_table:
            BooleanAlgebra.print_table_of_truth(truth_table, res, res_str, l_str, r_str, q, title="First Law of Simplification")

        return res

    @staticmethod
    def second_law_of_simplification(x, y, print_table: bool = True):
        p = 1 if x > 0 else 0
        np = 0 if x > 1 else 1
        q = 0 if y > 1 else 0
        nq = 0 if y > 1 else 1
        res_str = "(q) => (p => q)"

        l_str = "(q & p)"
        l = (q & p)

        r_str = "(q)"
        r = 1 - (q & (1 - np))

        res = 1 - (l & (1 - r))
        truth_table = BooleanAlgebra.make_table_of_truth(p, np, l, r, q, nq)
        if print_table:
            BooleanAlgebra.print_table_of_truth(truth_table, res, res_str, l_str, r_str, q, title="Second Law of Simplification")

        return res
