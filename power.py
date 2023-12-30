# my
import cli
from cli import Cli


class Power:
    @staticmethod
    def ipower(base, n):
        i = 0
        res = base
        if Cli.is_float(base) and Cli.is_int(n):
            for num in range(n - 1):
                i += 1
                res *= base

            Power._print_results(f"Potega o podstawie {base} i wykladniku {n} wynosi {res}. Licznik wynosi {i}.\n")
            return res

        else:
            print("Podstawa, badz wykladnik potegi maja nieprawidlowa wartosc.\n")
            return False

    @staticmethod
    def rpower(base, res, n, i):
        if i.__eq__(0) and i.__ne__(n) and Cli.is_float(base) and Cli.is_int(n):
            i += 1
            res = base * base
            return Power.rpower(base, res, n, i)

        elif i.__ne__(0) and i.__ne__(n) and Cli.is_float(base) and Cli.is_int(n):
            i += 1
            res *= base
            return Power.rpower(base, res, n, i)

        elif i.__eq__(n):
            Power._print_results(f"Potega o podstawie {base} i wykladniku {n} wynosi {res}. Licznik wynosi {i}.\n")
            return base

        else:
            print("Podstawa, badz wykladnik potegi maja nieprawidlowa wartosc.\n")
            return False

    @staticmethod
    def _print_results(message):
        print(message)


