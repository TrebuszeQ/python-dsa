from cli import Cli


class Darboux:

    # funkcja f(x) jest ciągła w przedziale <a,b>
    # w przedziale <a,b> znajduje się dokładnie jeden pierwiastek
    # funkcja przyjmuje różne znaki na końcach przedziału: f(a)*f(b)<0

    @staticmethod
    def _take_range_float():
        a = 0
        b = 0

        while a >= b:
            a = Cli.try_read_input_float("Podaj wartosc dolna przedzialu [typu float].\n")
            b = Cli.try_read_input_float("Podaj wartosc gorna przedzialu [typu float].\n")
            if a >= b:
                print("a nie moze byc wieksze badz rowne od b.")
        return a, b

    @staticmethod
    def _find_zero_case_2(b):
        return Darboux._find_zero_case_2(b)

    @staticmethod
    def _find_zero_case_1(a):
        return Darboux._find_zero_case_1(a)

    @staticmethod
    def _find_zero(a, b, d, c):
        c += 1
        try:
            x = (a + b) / 2
            f = x * x * x - x * x - x + 2

            if abs(f) <= d:
                print(x, " z dokladnoscia ", d)
                return True, c

            elif f * (a * a * a - a * a - a + 2) > 0:
                return Darboux._find_zero(a, x, d, c)

            else:
                print("Case 3")
                return Darboux._find_zero(x, b, d, c)

        except RecursionError:
            return False, c

    @staticmethod
    def darboux():
        c = 0
        i = 0

        # here
        res = (False, 0)

        while not res:
            a, b = Darboux._take_range_float()
            d = Cli.try_read_input_float("Podaj dokladnosc [typu float].\n")

            res = Darboux._find_zero(a, b, d, c)
            i += 1
            print(i + c)

            if res is False:
                print("Funkcja nie ma miejsc zerowych w przedziale.\n")

        return res



