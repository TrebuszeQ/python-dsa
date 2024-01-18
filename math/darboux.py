from cli import Cli


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
    def _get_count(i, c):
        print(i + c)
        return i + c

    @staticmethod
    def darboux():
        c = 0
        i = 0

        # here
        res = False

        while not res:
            a, b = Cli.read_range_float("Podaj wartosc dolna przedzialu [typu float].\n", "Podaj wartosc gorna przedzialu [typu float].\n")
            d = Cli.try_read_input_float("Podaj dokladnosc [typu float].\n")

            res, c = Darboux._find_zero(a, b, d, c)
            i += 1

            if res is False:
                print("Funkcja nie ma miejsc zerowych w przedziale.\n")

            all_c = Darboux._get_count(i, c)

        return all_c



