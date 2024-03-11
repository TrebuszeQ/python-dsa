# my
import cli
from cli import Cli


class Power:

    @staticmethod
    def _test_exp(n):
        if Cli.is_int(n):
            return True

        return False

    @staticmethod
    def _test_base(base):
        if Cli.is_float(base):
            return True

        elif Cli.is_int(base):
            return base * 1.0

        return False

    @staticmethod
    def ipower(base, n):
        i = 0
        res = base

        try:
            if Cli.is_float(base.__float__()) and Cli.is_int(n):
                for num in range(n - 1):
                    i += 1
                    res *= base

                print(f"Potega o podstawie {base} i wykladniku {n} wynosi {res}. Licznik wynosi {i}.\n")
                return res

        except BaseException or ValueError or AttributeError or TypeError or ...:
            print("Podstawa, badz wykladnik potegi maja nieprawidlowa wartosc.\n")
            return False

    @staticmethod
    def rpower(base, res, n, i):
        try:
            if i.__eq__(0) and Cli.is_float(base.__float__()) and Cli.is_int(n):
                i += 1
                res = base * base
                return Power.rpower(base, res, n, i)

            elif i.__ne__(0) and i.__ne__(n - 1) and Cli.is_float(base.__float__()) and Cli.is_int(n):
                i += 1
                res *= base
                return Power.rpower(base, res, n, i)

            elif i.__eq__(n - 1):
                print(f"Potega o podstawie {base} i wykladniku {n} wynosi {res}. Licznik wynosi {i}.\n")
                return res

        except BaseException or ValueError or AttributeError or TypeError or ...:
            print("Podstawa, badz wykladnik potegi maja nieprawidlowa wartosc.\n")
            return False

    @staticmethod
    def two_ipower(base):
        i = 0
        res = base

        try:
            if Cli.is_float(base.__float__()):
                i += 1
                res *= base
                print(f"Potega o podstawie {base} i wykladniku 2 wynosi {res}. Licznik wynosi {i}.\n")
                return res

        except BaseException or ValueError or AttributeError or TypeError or ...:
            print("Podstawa, badz wykladnik potegi maja nieprawidlowa wartosc.\n")
            return False

    @staticmethod
    def two_rpower(base, res, i):
        try:
            if i.__eq__(0) and Cli.is_float(base.__float__()):
                i += 1
                res = base * base
                return Power.rpower(base, res, 2, i)

            elif i.__ne__(0) and i.__ne__(1) and Cli.is_float(base.__float__()):
                i += 1
                res *= base
                return Power.rpower(base, res, 2, i)

            elif i.__eq__(1):
                print(f"Potega o podstawie {base} i wykladniku 2 wynosi {res}. Licznik wynosi {i}.\n")
                return res

        except BaseException or ValueError or AttributeError or TypeError or ...:
            print("Podstawa, badz wykladnik potegi maja nieprawidlowa wartosc.\n")
            return False

