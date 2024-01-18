from cli import Cli

class NewtonZero:
    @staticmethod
    def _find_zero(a, b, d, m):
        pass

    @staticmethod
    def _find_tangent(x0, x, b):
        derivative = 3 * x * x - 2 * x * x - 1
        zero = -2

    @staticmethod
    def newton():
        a, b = Cli.read_range_float("Wprowadz granice dolna przedzialu [typu float].\n",
                                    "Wprowadz granice gorna przedzialu [typu float].\n")
        i = 1
        x = a





