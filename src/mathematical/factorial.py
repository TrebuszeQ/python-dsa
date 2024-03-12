from datetime import datetime
from sys import getsizeof
# my
from cli import Cli


class Factorial:

    # silnia rekursywna
    @staticmethod
    def recursive(n):
        if n == 0:
            return 1

        else:
            return n * Factorial.recursive(n - 1)

    # silnia rekursywna z obliczaniem czasu
    @staticmethod
    def recursive_timed(n):
        start = datetime.now()
        return Factorial.recursive(n), Factorial._get_time_diff(start)

    # silnia iteracyjna
    @staticmethod
    def iterative(n):
        factorial = 1
        if n >= 1:
            while n != 1:
                factorial = factorial * n
                n -= 1

        return factorial

    # silnia iteracyjna z obliczaniem czasu
    @staticmethod
    def iterative_timed(n):
        start = datetime.now()
        return Factorial.iterative(n), Factorial._get_time_diff(start)

    # silnia iteracyjna z obliczaniem czasu i rozszerzonymi komunikatami
    @staticmethod
    def iterative_verbose(n):
        start = datetime.now()

        factorial = 1
        if n >= 1:
            while n != 1:
                factorial = factorial * n
                n -= 1
                print('type(n):', type(n), 'sizeof(n):', getsizeof(n), 'type(S):', type(factorial), 'sizeof(S):',
                      getsizeof(factorial))

        return factorial, Factorial._get_time_diff(start)

    # wyswietla wyniki i czas obliczen
    @staticmethod
    def print_timed(inp, factorial, time, recursive):
        if recursive:
            print(f"Silnia rekursywna z {inp} wynosi {factorial}.\nProgram trwal ~{time:f} sekund.\n")

        else:
            print(f"Silnia iteracyjna z {inp} wynosi {factorial}.\nProgram trwal ~{time:f} sekund.\n")

    # kalkuluje roznice czasowa
    @staticmethod
    def _get_time_diff(start):
        return datetime.now().__sub__(start).total_seconds()

    # wyswietla menu
    @staticmethod
    def menu():
        opt = 0

        options = ("1. Algorytm rekursywny.",
                   "2. Algorytm rekursywny z mierzeniem czasu.",
                   "3. Algorytm iteracyjny.",
                   "4. Algorytm iteracyjny z mierzeniem czasu.",
                   "5. Algorytm iteracyjny z mierzeniem czasu i rozszerzonymi komunikatami.",
                   "6. Wyjscie.\n")

        while opt != len(options):
            Cli.print_menu("Dostepne opcje programu silnia:\n", None, options)
            opt = abs(Cli.try_read_input_int("Podaj numer odpowiadajacy opcji.\n"))

            match opt:
                case 1:
                    arg = abs(Cli.try_read_input_int("Podaj dodatnia liczbe calkowita .\n"))
                    print(f"Silnia z {arg} wynosi {Factorial.recursive(arg)}.\n")

                case 2:
                    arg = abs(Cli.try_read_input_int("Podaj dodatnia liczbe calkowita.\n"))
                    factorial, time_diff = Factorial.recursive_timed(arg)
                    Factorial.print_timed(arg, factorial, time_diff, True)

                case 3:
                    arg = abs(Cli.try_read_input_int("Podaj dodatnia liczbe calkowita.\n"))
                    print(f"Silnia z {arg} wynosi {Factorial.iterative(arg)}.\n")

                case 4:
                    arg = abs(Cli.try_read_input_int("Podaj dodatnia liczbe calkowita.\n"))
                    factorial, time_diff = Factorial.iterative_timed(arg)
                    Factorial.print_timed(arg, factorial, time_diff, False)

                case 5:
                    arg = abs(Cli.try_read_input_int("Podaj dodatnia liczbe calkowita.\n"))
                    factorial, time_diff = Factorial.iterative_verbose(arg)
                    Factorial.print_timed(arg, factorial, time_diff, False)

                case 6:
                    exit(1)


if __name__.__eq__("__main__"):
    Factorial.menu()



