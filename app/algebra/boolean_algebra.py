import math
from tabulate import tabulate

    p = 1 if num > 0 else 0
    np = 1 - p
    res = (1 - (l - p) ** 2)


    def _is_0_or_1(num):
        return 1 if num > 0 else 0

    def _print_single_table_of_truth(p, np, l, r, res):
        eq = 1 if l == r else 0

        truth_table = [[p, np, l, r, eq], [np, p, l, r, eq]]

        head = ["p", "~p", "l", "r", "l <=> r"]
        print(tabulate(truth_table, headers=head, tablefmt="grid"))
        print("".ljust(34), res)
        print()


    def _print_double_table_of_truth(p, np, q, nq, l, r, res):
        eq = 1 if l == r else 0

        truth_table = [[p, np, q, nq, l, r, eq], [np, p, q, nq, l, r, eq]]

        head = ["p", "~p", "q", "~q", "l", "r", "l <=> r"]
        print(tabulate(truth_table, headers=head, tablefmt="grid"))
        print("".ljust(43), res)
        print()


    def to_bin(num):
        return bin(num)[2:]


    def to_bin_array(num):
        binary = to_bin(num)
        return [int(bit) for bit in binary]

    # p v (~p) <=> 1
    # @staticmethod
    # def excluded_middle(num):
    #     a0 = BooleanAlgebra.to_bin_array(num)[0]
    #     return 1 - (1 - a0) * (1 - (1 - a0))


    def inversion(num):
        return to_bin(~(~num))


    def double_negation(num):
        p = 1 if num > 0 else 0
        np = 1 - p
        l = (1 - (1 - p))
        r = p
        res = 1 - (l - p)**2
        _print_single_table_of_truth(p, np, l, r, res)
        return res


    def excluded_middle(num):
        p = 1 if num > 0 else 0
        np = 1 - p
        l = 1 - (1 - p) * (1 - (1 - p))
        r = 1
        res = (1 - (l - p) ** 2)
        _print_single_table_of_truth(p, np, l, r, res)
        return res


    def contradiction(num):
        p = 1 if num > 0 else 0
        np = 1 - p
        l = 0 if ~(p & np) < 0 else 0
        r = 1
        res = (1 - (l - p) ** 2)
        _print_single_table_of_truth(p, np, l, r, res)
        return res
