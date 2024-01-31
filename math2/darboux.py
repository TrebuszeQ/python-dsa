from cli import Cli

# twierdzenie o przyjmowaniu wartosci posrednich Darboux
class Darboux:

    # funkcja f(x) jest ciągła w przedziale <a,b>
    # w przedziale <a,b> znajduje się dokładnie jeden pierwiastek
    # funkcja przyjmuje różne znaki na końcach przedziału: f(a)*f(b)<0

    @staticmethod
    def _find_zero_case_2(b):
        return Darboux._find_zero_case_2(b)

    @staticmethod
    def _find_zero_case_1(a):
        return Darboux._find_zero_case_1(a)

    @staticmethod
    def _find_zero(a, b, d):
        try:
            x = (a + b) / 2
            f = x * x * x - x * x - x + 2

            if abs(f) <= d:
                print(x, " z dokladnoscia ", d)
                return True

            elif f * (a * a * a - a * a - a + 2) > 0:
                return Darboux._find_zero(a, x, d)

            else:
                print("Case 3")
                return Darboux._find_zero(x, b, d)

        except RecursionError:
            return False

    @staticmethod
    def _find_zero_count(a, b, d, c):
        c += 1
        try:
            x = (a + b) / 2
            f = x * x * x - x * x - x + 2

            if abs(f) <= d:
                print(x, " z dokladnoscia ", d)
                return True, c

            elif f * (a * a * a - a * a - a + 2) > 0:
                return Darboux._find_zero_count(a, x, d, c)

            else:
                print("Case 3")
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
        d = Cli.try_read_input_float(f"Podaj punkt w przedziale <{a}, {b}>")

        while d < a or d > b:
            d = Cli.try_read_input_float(f"Podaj punkt w przedziale <{a}, {b}>")

        return d

    @staticmethod
    def _darboux():
        a, b = Cli.read_interval_closed_float("Podaj lewostronna granice przedzialu.\n", "Podaj prawostronna granice przedzialu.\n")
        d = Darboux._take_point(a, b)

        if a == b:
            return False

        fx = Darboux._calculate_func((a + b)/2)
        fa = Darboux._calculate_func(a)
        fb = Darboux._calculate_func(b)

        if fx == d:
            return fx

        elif fa < d < fb or fa > d > fb:
            return True

        else:
            return False
