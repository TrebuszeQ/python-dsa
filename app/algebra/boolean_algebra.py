

class BooleanAlgebra:
    @staticmethod
    def _print_single_table_of_truth(p):
        if p == 0:
            truth_table_p = [1, 1, 0, 0]
            truth_table_neg_p = [0, 0, 1, 1]

        elif p == 1:
            truth_table_p = [0, 0, 1, 1]
            truth_table_neg_p = [1, 1, 0, 0]

        res_table =  

    @staticmethod
    def _print_double_truth_table(p, q):
        truth_table_p = [1, 1, 0, 0]
        truth_table_q = [1, 0, 1, 0]

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
        p = int(BooleanAlgebra.to_bin(num)[0])
        left = -(-p)
        right = p
        res = 1 - (left - right)**2
        return

