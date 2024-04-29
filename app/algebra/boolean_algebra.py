from tabulate import tabulate


class BooleanAlgebra:
    truth_table = []

    @staticmethod
    def make_table_of_truth_to_range(max_range, boolean_function, q=False):
        truth_table = []

        if q is False:
            for x in range(max_range):
                boolean_function(x, print_table=False)
                truth_table.append(BooleanAlgebra.truth_table)

        else:
            for x in range(max_range):
                boolean_function(x, x, print_table=False)
                truth_table.append(BooleanAlgebra.truth_table)

        return truth_table

    # @staticmethod
    # def make_table_of_truth(p, np, l, r, res, q=None, nq=None):
    #     truth_table = [[1, np, p, l, r, res]] if q is None \
    #         else [[1, np, p, nq, q, l, r, res]]
    #
    #     return truth_table
    #
    @staticmethod
    def make_table_of_truth(p, np, l, r, res, q=None, nq=None):
        truth_table = [[1, np, p, l, r, res], [2, p, np, l, r, res]] if q is None \
            else [[1, np, p, nq, q, l, r, res], [2, p, np, nq, q, l, r, res]]

        return truth_table

    @staticmethod
    def print_table_of_truth(truth_table, headings, res, title="Truth Table"):
        print(title)
        print(tabulate(truth_table, headers=headings, tablefmt="grid"))
        print(f"result: {res}")
        print()

    # @staticmethod
    # def print_table_of_truth(truth_table, res, res_str, l_str, r_str, q=None, title="Truth Table"):
    #     if q is None:
    #         head = ["no.", "p", "~p", l_str, r_str, res_str]
    #
    #     else:
    #         head = ["no.", "p", "~p", "q", "~q", l_str, r_str, f"{l_str} <=> {r_str}"]
    #
    #     print(title)
    #     print(tabulate(truth_table, headers=head, tablefmt="grid"))
    #     print(f"result: {res}")
    #
    #     print()

    @staticmethod
    def inversion(p):
        return 1 - (1 - p)

    @staticmethod
    def double_negation(x):
        p = 1 if x > 0 else 0
        np = 0 if x > 1 else 1
        res_str = "[~(~p)] <=> p"

        l_str = "~(~p)"
        l = (1 - (1 - p))

        r_str = "p"
        r = p

        res = 1 - (l - r) ** 2
        
        return res

    @staticmethod
    def excluded_middle(x):
        p = 1 if x > 0 else 0
        np = 0 if x > 1 else 1
        res_str = "[p | (~p)] <=> 1"

        l_str = "[p | (~p)]"
        l = 1 - (1 - p) * (1 - (1 - p))

        r_str = "1"
        r = 1

        res = (1 - (l - r) ** 2)
        return res

    @staticmethod
    def contradiction(x):
        p = 1 if x > 0 else 0
        np = 0 if x > 1 else 1
        res_str = "[~(p & ~p)] <=> 1"

        l_str = "~(p & ~p)"
        l = (1 - (p & np))

        r_str = "1"
        r = 1

        res = (1 - (l - r) ** 2)
        return res

    # Prawo idempotentności alternatywy
    @staticmethod
    def alternative_simplification(x):
        p = 1 if x > 0 else 0
        np = 0 if x > 1 else 1
        res_str = "(p | p) <=> p"

        l_str = "(p | p)"
        l = (p | p)

        r_str = "p"
        r = p

        res = (1 - (l - r) ** 2)
        return res

    @staticmethod
    def conjuction_simplification(x):
        p = 1 if x > 0 else 0
        np = 0 if x > 1 else 1
        res_str = "(p & ~p) <=> p"

        l_str = "(p & p)"
        l = (p & p)

        r_str = "p"
        r = p

        res = (1 - (l - r) ** 2)
        return res

    @staticmethod
    def first_law_of_clavius(x):
        p = 1 if x > 0 else 0
        np = 0 if x > 1 else 1
        res_str = "(p => ~p) => ~p"

        l_str = "(p => ~p)"
        l = 1 - (p & (1 - np))

        r_str = "(~p)"
        r = np

        res = (1 - (l - r) ** 2)
        truth_table = BooleanAlgebra.make_table_of_truth(p, np, l, r, res)
        return res

    @staticmethod
    def second_law_of_clavius(x):
        p = 1 if x > 0 else 0
        np = 0 if x > 1 else 1
        res_str = "(~p => p) => p"

        l_str = "(~p => p)"
        l = 1 - (np & (1 - p))

        r_str = "p"
        r = p

        res = (1 - (l - r) ** 2)
        truth_table = BooleanAlgebra.make_table_of_truth(p, np, l, r, res)
        return res

    @staticmethod
    def law_of_duns_scotus(x, y):
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
        return res

    @staticmethod
    def first_law_of_simplification(x, y):
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
        return res

    @staticmethod
    def second_law_of_simplification(x, y):
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
        return res
