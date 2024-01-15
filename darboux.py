from cli import Cli
class Darboux:

    # funkcja f(x) jest ciągła w przedziale <a,b>
    # w przedziale <a,b> znajduje się dokładnie jeden pierwiastek
    # funkcja przyjmuje różne znaki na końcach przedziału: f(a)*f(b)<0

    @staticmethod
    def find_zero(a, b, d, c):
        c += 1
        x = (a + b)/2
        f = x*x*x - x*x - x + 2

        if abs(f) <= d:
            print(x, 'z dokladnoscia ', d)

        elif ((a*a*a - a*a - a + 2) * f) < 0:
            return Darboux.find_zero(a, x, d, c)

        else:
            Darboux.find_zero(x, b, d, c)

