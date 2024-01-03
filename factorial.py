from datetime import datetime, timedelta
from freezegun import freeze_time
# my
from cli import Cli


class Factorial:
    @staticmethod
    def recursive(val, i, factorial):
        if val.__lt__(1):
            return 1

        elif i.__lt__(val):
            if factorial == 0:
                factorial = 1
            factorial += factorial * i
            i += 1
            return Factorial.recursive(val, i, factorial)

        return factorial

    @staticmethod
    def recursive_timed(val, i, factorial, start):
        if i == 0:
            start = datetime.now()

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
    def iterable_timed(n):
        return Factorial.iterable(n), Factorial._get_time_diff(datetime.now())

    @staticmethod
    def print_timed(inp, factorial, time, recursive):
        if recursive:
            print(f"Silnia z {inp} wynosi {factorial}.\nRekursywny program trwal ~{time:f} sekund.\n")

        else:
            print(f"Silnia z {inp} wynosi {factorial}.\nIteratywny program trwal ~{time:f} sekund.\n")

    @staticmethod
    def _get_time_diff(start):
        return datetime.now().__sub__(start).total_seconds()

    @staticmethod
    def menu():
        opt = 0
        options = ("1. Algorytm rekursywny.",
                   "2. Algorytm iteracyjny.",
                   "3. Algorytm rekursywny z mierzeniem czasu.",
                   "4. Algorytm iteracyjny z mierzeniem czasu.",
                   "5. Wyjscie.\n")
        while opt != 5:
            Cli.print_menu("Dostepne opcje programu silnia:\n", None, options)
            opt = abs(Cli.try_read_input_int("Podaj numer opcji.\n"))

            match opt:
                case 1:
                    arg = abs(Cli.try_read_input_int("Podaj dodatnia liczbe calkowita .\n"))
                    print(f"Silnia z {arg} wynosi {Factorial.recursive(arg, 0, 0)}.\n")

                case 2:
                    arg = abs(Cli.try_read_input_int("Podaj dodatnia liczbe calkowita.\n"))
                    print(f"Silnia z {arg} wynosi {Factorial.iterable(arg)}.\n")

                case 3:
                    arg = abs(Cli.try_read_input_int("Podaj dodatnia liczbe calkowita.\n"))
                    factorial, time_diff = Factorial.recursive_timed(arg, 0, 0, datetime.now())
                    Factorial.print_timed(arg, factorial, time_diff, True)

                case 4:
                    arg = abs(Cli.try_read_input_int("Podaj dodatnia liczbe calkowita.\n"))
                    factorial, time_diff = Factorial.iterable_timed(arg)
                    Factorial.print_timed(arg, factorial, time_diff, False)

                case 5:
                    exit(1)


if __name__.__eq__("__main__"):
    Factorial.menu()



