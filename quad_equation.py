import math
# my
from cli import Cli

# # sprawdza czy wartosc jest typu float
# def is_float(arg):
#     if type(arg) is float:
#         return True
#
#     else:
#         return False
#
#
# # probuje odczytac wejscie float
# def try_read_input_float(message):
#     value: str
#     truth = False
#
#     while truth is False:
#         value = input(message)
#         value_float = None
#
#         try:
#             value_float = float(value)
#             truth = is_float(value_float)
#
#             if truth:
#                 return value_float
#
#             else:
#                 raise ValueError
#
#         except ValueError or ...:
#             print("Wprowadzono nieprawidlowa wartosc.\n")
#
#
# # probuje odczytac wartosc float 3 razy i zwraca tablice
# def read_float_triple():
#     values = [0.0, 0.0, 0.0]
#     variables: chr = ["a", "b", "c"]
#
#     for i in range(0, values.__len__()):
#         values[i] = try_read_input_float("Wprowadz wartosc " + variables[i] + ":\n")
#
#     return values


# oblicza i zwraca delte
def get_delta(a, b, c):
    return (b * b) - 4 * (a * c)


# oblicza i zwraca wynik rownania
def get_equation(values):
    a, b, c = values

    if a.__eq__(0):
        print("To jest rownanie liniowe.\n", -c / b)
        return False

    else:
        delta = get_delta(a, b, c)

        if delta < 0:
            print("Brak rozwiazan.\n")
            return None

        elif delta > 0:
            x1 = ((-b - math.sqrt(delta)) / (2 * a))
            x2 = ((-b + math.sqrt(delta)) / (2 * a))
            print("Dwa pierwiastki", x1, x2)
            return [x1, x2]

        else:
            print("Jeden pierwiastek", -b / (2 * a))
            return True


if __name__ == "__main__":
    get_equation(Cli.read_float_triple())

