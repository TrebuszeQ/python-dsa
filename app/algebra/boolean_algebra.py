from tabulate import tabulate


class BooleanAlgebra:
    @staticmethod
    def _print_single_table_of_truth(p, np, l, r, res):
        eq = 1 if l == r else 0

        truth_table = [[p, np, l, r, eq], [np, p, l, r, eq]]

        head = ["p", "~p", "l", "r", "l <=> r"]
        print(tabulate(truth_table, headers=head, tablefmt="grid"))
        print("".ljust(34), res)
        print()

    @staticmethod
    def _print_double_table_of_truth(p, np, q, nq, l, r, res):
        eq = 1 if l == r else 0

        truth_table = [[p, np, q, nq, l, r, eq], [np, p, q, nq, l, r, eq]]

        head = ["p", "~p", "q", "~q", "l", "r", "l <=> r"]
        print(tabulate(truth_table, headers=head, tablefmt="grid"))
        print("".ljust(43), res)
        print()

    @staticmethod
    def to_bin(num):
        return bin(num)[2:]

    @staticmethod
    def to_bin_array(num):
        binary = BooleanAlgebra.to_bin(num)
        return [int(bit) for bit in binary]

    # p v (~p) <=> 1
    # @staticmethod
    # def excluded_middle(num):
    #     a0 = BooleanAlgebra.to_bin_array(num)[0]
    #     return 1 - (1 - a0) * (1 - (1 - a0))

    @staticmethod
    def inversion(num):
        return BooleanAlgebra.to_bin(~(~num))

    @staticmethod
    def double_negation(num):
        p = 1 if num > 0 else 0
        np = 0 if num > 0 else 1
        l = ~np
        r = p
        res = 1 - (p - l)**2
        BooleanAlgebra._print_single_table_of_truth(p, np, l, r, res)
        return res

    @staticmethod
    def double_negation(num):
        p = 1 if num > 0 else 0
        np = 0 if num > 0 else 1
        l = np
        r = p
        res = 1 - (p - l) ** 2
        BooleanAlgebra._print_single_table_of_truth(p, np, l, r, res)
        return res

    @staticmethod
    def excluded_middle(num):
        p = 1 if num > 0 else 0
        np = 0 if num > 0 else 1

        l = p | np
        r = 1
        res = 1 - (p - l) ** 2
        BooleanAlgebra._print_single_table_of_truth(p, np, l, r, res)
        return res

    @staticmethod
    def contradiction(num):
        p = 1 if num > 0 else 0
        np = 0 if num > 0 else 1

        l = ~(p & np)
        l = 0 if l < 0 else 0
        r = 1
        res = 1 - (p - l) ** 2
        BooleanAlgebra._print_single_table_of_truth(p, np, l, r, res)
