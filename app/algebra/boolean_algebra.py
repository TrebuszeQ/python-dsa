

class BooleanAlgebra:

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
    def excluded_middle(num):
        return BooleanAlgebra.to_bin(num) or not BooleanAlgebra.to_bin(num)

    @staticmethod
    def double_negation(num):
        return not (not BooleanAlgebra.to_bin(num))
