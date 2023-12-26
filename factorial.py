# my
from cli import Cli


class Factorial:
    @staticmethod
    def recursive(val, i, factorial):
        if val == 0 or val == 1:
            return 1

        elif i.__eq__(val):
            return factorial

        else:
            if factorial == 0:
                factorial = 1
            factorial += factorial * i
            i += 1
            return Factorial.recursive(val, i, factorial)

    @staticmethod
    def iterable(n):
        factorial = 1
        if n > 1:
            while n != 0:
                factorial += factorial * n
                n -= 1

        return factorial


if __name__.__eq__("__main__"):
    arg = abs(Cli.try_read_input_int("Podaj liczbe calkowita dodatnia.\n"))

    res = Factorial.recursive(arg, 0, 0)
    print(f"Rekursywna silnia z {arg} wynosi {res}.\n")

    res = Factorial.iterable(arg)
    print(f"Iteratywna silnia z {arg} kroków wynosi {res}.\n")



