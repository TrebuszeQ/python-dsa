from cli import Cli


class IntegerSum:
    @staticmethod
    def sum_integer_len(value):
        sumi = 0
        for i in range(str.__len__(value)):
            sumi += i

        return sumi





