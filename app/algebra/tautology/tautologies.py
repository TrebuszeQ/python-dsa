from tabulate import tabulate


class Tautologies:
    truth_table = []

    @staticmethod
    def make_table_of_truth_to_range_and_print(boolean_function, q=None, title="Truth Table"):
        truth_table = []
        res = 1
        headers = []

        if q is None:
            for i in range(1):
                tt, headers = boolean_function(i)
                tt.insert(0, i + 1)
                truth_table.append(tt)
                if tt[len(tt) - 1] == 0:
                    res = 0

        else:
            bin_arr = [[0, 0], [0, 1], [1, 0], [1, 1]]
            for arr in bin_arr:
                i, j = arr
                tt, headers = boolean_function(i, j)
                truth_table.append(tt)
                if tt[len(tt) - 1] == 0:
                    res = 0

        Tautologies.print_table_of_truth(truth_table, headers, res, title=title)
        return [truth_table, res]

    @staticmethod
    def print_table_of_truth(truth_table, headers, res, title="Truth Table"):
        print(title)
        print(tabulate(truth_table, headers=headers, tablefmt="grid"))
        print(f"result: {res}")
        print()

    @staticmethod
    def double_negation(p):
        np = 1 - p
        res_str = "[~(~p)] <=> p"

        l_str = "~(~p)"
        l = (1 - (1 - p))

        r_str = "p"
        r = p

        res = 1 - (r - l) ** 2
        headers = ["no.", "p", "~p", l_str, r_str, res_str]
        return [[p, np, l, r, res], headers]

    @staticmethod
    def inversion(p):
        return 1 - (1 - p)

    @staticmethod
    def excluded_middle(p):
        np = 1 - p
        res_str = "[p | (~p)] <=> 1"

        l_str = "[p | (~p)]"
        l = 1 - (1 - p) * (1 - (1 - p))

        r_str = "1"
        r = 1

        res = (1 - (r - l) ** 2)
        headers = ["no.", "p", "~p", l_str, r_str, res_str]
        return [[p, np, l, r, res], headers]

    @staticmethod
    def contradiction(p):
        np = 1 - p

        res_str = "[~(p & ~p)] <=> 1"

        l_str = "~(p & ~p)"
        l = (1 - (p & np))

        r_str = "1"
        r = 1

        res = (1 - (r - l) ** 2)
        headers = ["no.", "p", "~p", l_str, r_str, res_str]
        return [[p, np, l, r, res], headers]

    # Prawo idempotentności alternatywy
    @staticmethod
    def alternative_simplification(p):
        np = 1 - p
        res_str = "(p | p) <=> p"

        l_str = "(p | p)"
        l = (p | p)

        r_str = "p"
        r = p

        res = (1 - (r - l) ** 2)
        headers = ["no.", "p", "~p", l_str, r_str, res_str]
        return [[p, np, l, r, res], headers]

    @staticmethod
    def conjuction_simplification(p):
        np = 1 - p
        res_str = "(p & ~p) <=> p"

        l_str = "(p & p)"
        l = (p & p)

        r_str = "p"
        r = p

        res = (1 - (r - l) ** 2)
        headers = ["no.", "p", "~p", l_str, r_str, res_str]
        return [[p, np, l, r, res], headers]

    @staticmethod
    def first_rule_of_clavius(p):
        np = 1 - p
        res_str = "(p => ~p) => ~p"

        l_str = "(p => ~p)"
        l = 1 - (p * (1 - np))

        r_str = "(~p)"
        r = np

        res = 1 - (l * (1 - np))
        headers = ["no.", "p", "~p", l_str, r_str, res_str]
        return [[p, np, l, r, res], headers]

    @staticmethod
    def second_rule_of_clavius(p):
        np = 1 - p
        res_str = "(~p => p) => p"

        l_str = "(~p => p)"
        l = 1 - (np & (1 - p))

        r_str = "p"
        r = p

        res = 1 - (l * (1 - p))
        headers = ["no.", "p", "~p", l_str, r_str, res_str]
        return [[p, np, l, r, res], headers]

    @staticmethod
    def rule_of_duns_scotus(p, q):
        res_str = "(~p => p) => p"

        l_str = "(~q)"
        l = 1 - q

        r_str = "(q => p)"
        r = 1 - (q & (1 - p))

        res = 1 - (l * (1 - p))
        headers = ["no.", "p", "q", l_str, r_str, res_str]
        return [[p, q, l, r, res], headers]

    @staticmethod
    def first_law_of_simplification(p, q):
        res_str = "(~q) => (q => p)"

        l_str = "q"
        l = q

        r_str = "(q => p)"
        r = 1 - (p & 1 - q)

        res = 1 - (l * (1 - p))
        headers = ["no.", "p", "q", l_str, r_str, res_str]
        return [[p, q, l, r, res], headers]

    @staticmethod
    def second_rule_of_simplification(p, q):
        res_str = "(q) => (p => q)"

        l_str = "(q & p)"
        l = (q & p)

        r_str = "(q)"
        r = q

        res = 1 - (l * (1 - p))
        headers = ["no.", "p", "q", l_str, r_str, res_str]
        return [[p, q, l, r, res], headers]

    @staticmethod
    def first_de_morgans_rule(p, q):
        res_str = "~(q & p) <=> ((~q) | (~p))"

        l_str = "~(q & p)"
        l = 1 - (q & p)

        r_str = "((~q) | (~p))"
        r = (1 - q) | (1 - p)

        res = 1 - ((r - l) ** 2)
        headers = ["no.", "p", "q", l_str, r_str, res_str]
        return [[p, q, l, r, res], headers]

    @staticmethod
    def second_de_morgan_law(p, q):
        res_str = "(~(q | p)) <=> ((~q) & (~p))"

        l_str = "(~(q | p))"
        l = 1 - (q & p)

        r_str = "((~q) & (~p))"
        r = (1 - q) | (1 - p)

        res = 1 - ((r - l) ** 2)
        headers = ["no.", "p", "q", l_str, r_str, res_str]
        return [[p, q, l, r, res], headers]

    @staticmethod
    def first_rule_of_implication(p, q):
        res_str = "(q => p) <=> (p | (~q))"

        l_str = "(q => p)"
        l = 1 - (q * (1 - p))

        r_str = "(p | (~q))"
        r = 1 - (p | (1 - q))

        res = 1 - ((r - l) ** 2)
        headers = ["no.", "p", "q", l_str, r_str, res_str]
        return [[p, q, l, r, res], headers]

    @staticmethod
    def first_rule_of_exclusive_disjunction(p, q):
        res_str = "(q | p) <=> [(q & (~p)) | ((~q) & q)]"

        l_str = "(q | p)"
        l = (q | p)

        r_str = "[(q & (~p)) | ((~q) & q)]"
        r = (q * (1 - p) | ((1 - q) & q))

        res = 1 - ((r - l) ** 2)
        headers = ["no.", "p", "q", l_str, r_str, res_str]
        return [[p, q, l, r, res], headers]