from datetime import datetime
from freezegun import freeze_time
# my
from cli import Cli


class Factorial:
    @staticmethod
    def recursive(val, i, factorial):
        if val == 0 or val == 1:
            return 1

        elif i.__lt__(val):
            if factorial == 0:
                factorial = 1
            factorial += factorial * i
            i += 1
            return Factorial.recursive(val, i, factorial)

        else:
            return factorial

    @staticmethod
    def recursive_timed(val, i, factorial, start):
        if i == 0:
            start = Factorial._get_start_time()

        if val == 0 or val == 1:
            return 1

        elif i.__lt__(val):
            if factorial == 0:
                factorial = 1
            factorial += factorial * i
            i += 1
            return Factorial.recursive_timed(val, i, factorial, start)

        else:
            return factorial, Factorial._get_time_diff(start)

    @staticmethod
    def iterable(n):
        factorial = 1
        if n >= 1:
            while n != 1:
                factorial = factorial * n
                n -= 1

        return factorial

    @staticmethod
    def print_timed(inp, factorial, time, recursive):
        if recursive:
            print(f"Silnia z {inp} wynosi {factorial}.\n Rekursywny algorytm trwal {time}.\n")

        else:
            print(f"Silnia z {inp} wynosi {factorial}.\n Iteratywny algorytm trwal {time}.\n")

    @staticmethod
    def _get_start_time():
        return freeze_time(datetime.now())

    @staticmethod
    def _get_time_diff(start):
        return datetime.now() - start

    @staticmethod
    def menu():
        Cli.print_menu("Mozliwe opcje klasy silnia:\n", None, """1. Algorytm rekursywny.\n
                                                              2. Algorytm iteracyjny.\n
                                                              3. Algorytm rekursywny z mierzeniem czasu.\n
                                                              4. Algorytm iteracyjny z mierzeniem czasu.\n""")
        opt = abs(Cli.try_read_input_int("Podaj numer opcji.\n"))
        arg = abs(Cli.try_read_input_int("Podaj dodatnia liczbe calkowita.\n"))
        match opt:
            case 1:
                factorial = Factorial.recursive(arg, 0, 0)
                print(f"Silnia z {arg} wynosi {factorial}.\n")

            case 2:
                factorial = Factorial.iterable(arg)
                print(f"Silnia z {arg} wynosi {factorial}.\n")

            case 3:
                factorial, time_diff = Factorial.recursive_timed(arg, 0, 0, Factorial._get_start_time())
                Factorial.print_timed(arg, factorial, time_diff, True)

            case 4:
                factorial, time_diff = Factorial.iterable_timed(arg, 0, 0, Factorial._get_start_time())
                Factorial.print_timed(arg, factorial, time_diff, False)





# if __name__.__eq__("__main__"):
#     arg = abs(Cli.try_read_input_int("Podaj dodatnia liczbe calkowita.\n"))
#
#     res = Factorial.recursive(arg, 0, 0)
#     print(f"Rekursywna silnia z {arg} wynosi {res}.\n")
#
#     res = Factorial.iterable(arg)
#     print(f"Iteratywna silnia z {arg} kroków wynosi {res}.\n")



