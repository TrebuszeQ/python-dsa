from tabulate import tabulate


class BooleanAlgebra:
    truth_table = []

    @staticmethod
    def make_table_of_truth_to_range_and_print(from_value, to_value, boolean_function, q=None, title="Truth Table"):
        truth_table = []
        res = None
        headers = []

        if q is None:
            for x in range(from_value, to_value):
                tt, headers = boolean_function(x)
                headers.insert(x, "no.")
                truth_table.append(tt)

                res = 1 if tt[len(tt)-1] == 1 else 0

        else:
            for x in range(from_value, to_value):
                y = x
                tt, headers = boolean_function(x, y)
                tt.insert(x, "no.")
                truth_table.append(tt)
                truth_table.append(BooleanAlgebra.truth_table)

                res = 1 if tt[len(tt) - 1] == 1 else 0

        # title = boolean_function.__name__() + "truth table"
        BooleanAlgebra.print_table_of_truth(truth_table, headers, res, title=title)
        return [truth_table, res]

    @staticmethod
    def print_table_of_truth(truth_table, headings, res, title="Truth Table"):
        print(title)
        print(tabulate(truth_table, headers=headings, tablefmt="grid"))
        print(f"result: {res}")
        print()

    @staticmethod
    def double_negation(x):
        p = 1 if x > 0 else 0
        np = 0 if p > 1 else 1
        res_str = "[~(~p)] <=> p"

        l_str = "~(~p)"
        l = (1 - (1 - p))

        r_str = "p"
        r = p

        res = 1 - (l - r) ** 2
        headers = ["no.", "p", "~p", l_str, r_str, res_str]
        return [[np, p, l, r, res], headers]

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
    def excluded_middle(x):
        p = 1 if x > 0 else 0
        np = 0 if x > 1 else 1
        res_str = "[p | (~p)] <=> 1"

        l_str = "[p | (~p)]"
        l = 1 - (1 - p) * (1 - (1 - p))

        r_str = "1"
        r = 1

        res = (1 - (l - r) ** 2)
        headers = ["no.", "p", "~p", l_str, r_str, res_str]
        return [[np, p, l, r, res], headers]

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
        headers = ["no.", "p", "~p", l_str, r_str, res_str]
        return [[np, p, l, r, res], headers]

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
        headers = ["no.", "p", "~p", l_str, r_str, res_str]
        return [[np, p, l, r, res], headers]

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
        headers = ["no.", "p", "~p", l_str, r_str, res_str]
        return [[np, p, l, r, res], headers]

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
        headers = ["no.", "p", "~p", l_str, r_str, res_str]
        return [[np, p, l, r, res], headers]

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
        headers = ["no.", "p", "~p", l_str, r_str, res_str]
        return [[np, p, l, r, res], headers]

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
        headers = ["no.", "p", "~p", "q", "~q", l_str, r_str, res_str]
        return [[np, p, q, nq, l, r, res], headers]

    @staticmethod
    def first_law_of_simplification(x, y):
        p = 1 if x > 0 else 0
        np = 0 if x > 1 else 1
        q = 1 if y > 0 else 0
        nq = 0 if y > 1 else 1
        res_str = "(~q) => (q => p)"

        l_str = "q"
        l = q

        r_str = "(q => p)"
        r = 1 - (p & 1 - q)

        res = 1 - (l & (1 - r))
        headers = ["no.", "p", "~p", "q", "~q", l_str, r_str, res_str]
        return [[np, p, q, nq, l, r, res], headers]

    @staticmethod
    def second_law_of_simplification(x, y):
        p = 1 if x > 0 else 0
        np = 0 if x > 1 else 1
        q = 1 if y > 0 else 0
        nq = 0 if y > 1 else 1
        res_str = "(q) => (p => q)"

        l_str = "(q & p)"
        l = (q & p)

        r_str = "(q)"
        r = 1 - (q & (1 - np))

        res = 1 - (l & (1 - r))
        headers = ["no.", "p", "~p", "q", "~q", l_str, r_str, res_str]
        return [[np, p, q, nq, l, r, res], headers]
