from cli import Cli


# twierdzenie o przyjmowaniu wartosci posrednich Darboux
class Darboux:

    # funkcja f(x) jest ciągła w przedziale <a,b>
    # w przedziale <a,b> znajduje się dokładnie jeden pierwiastek
    # funkcja przyjmuje różne znaki na końcach przedziału: f(a)*f(b)<0

    @staticmethod
    def _bisection_recursive(a, b, d):

        try:
            x = (a + b) / 2
            f = Darboux._calculate_func(x)

            if abs(f) <= d:
                print(f"Miejsce zerowe funkcji dazy do {x} z dokladnoscia do {d}.\n")
                return True

            elif f * Darboux._calculate_func(a) > 0:
                return Darboux._bisection_recursive(a, x, d)

            else:
                return Darboux._bisection_recursive(x, b, d)

        except RecursionError:
            return False

    @staticmethod
    def _find_zero_count(a, b, d, c):
        c += 1

        try:
            x = (a + b) / 2
            f = Darboux._calculate_func(x)

            if abs(f) <= d:
                print(f"Miejsce zerowe funkcji dazy do {x} z dokladnoscia do {d}.\n")
                return True, c

            elif f * Darboux._calculate_func(a) > 0:
                return Darboux._find_zero_count(a, x, d, c)

            else:
                return Darboux._find_zero_count(x, b, d, c)

        except RecursionError:
            return False, c

    @staticmethod
    def _get_count(i, c):
        print(i + c)
        return i + c

    @staticmethod
    def _calculate_func(x):
        return x * x * x - x * x - x + 2

    @staticmethod
    def _take_point(a, b):
        d = Cli.try_read_input_float(f"Podaj punkt w przedziale <{a}, {b}>.\n")

        while d < a or d > b:
            d = Cli.try_read_input_float(f"Podaj punkt w przedziale <{a}, {b}>.\n")

        return d

    @staticmethod
    def _has_darboux_point(a, b):
        if a == b:
            return False

        fa = Darboux._calculate_func(a)
        fb = Darboux._calculate_func(b)

        if fa == 0 or fb == 0:
            return True

        if fa * fb < 0:
            return True

        else:
            return False

    @staticmethod
    def darboux():
        a, b = Cli.read_interval_closed_float("Podaj lewostronna granice przedzialu.\n",
                                              "Podaj prawostronna granice przedzialu.\n")
        d = Darboux._take_point(a, b)
        Darboux._bisection_recursive(a, b, d)
        return False

    # @staticmethod
    # def darboux():
    #     a, b = Cli.read_interval_closed_float("Podaj lewostronna granice przedzialu.\n",
    #                                           "Podaj prawostronna granice przedzialu.\n")
    #
    #     i = a
    #     while i == b:
    #         if Darboux._has_darboux_point(a, b):
    #             fc = Darboux._calculate_func(i)
    #             if fc == 0:
    #                 return True
    #
    #             i += 0.001
    #
    #     return False
