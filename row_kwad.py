import math


def read_input(message):
    value: str
    value_float = None

    while value_float is None:
        value = input(message)

        try:
            value_float = float(value)

        except ValueError:
            print("Wprowadzono nieprawidlowa wartosc.\n")

        except ...:
            print("Wprowadzono nieprawidlowa wartosc.\n")
            value_float = None
            break

    return value_float


def get_delta(a, b, c):
    return (b * b) - 4 * (a * c)


def get_results(a, b, delta):
    if delta < 0:
        print("Brak rozwiazan.\n")
        return None

    elif delta > 0:
        print("Dwa pierwiastki", ((-b - math.sqrt(delta)) / (2 * a)), ((-b + math.sqrt(delta)) / (2 * a)))
        return
    else:
        print("Jeden pierwiastek", -b / (2 * a))


def rownanie():
    options = ["a", "b", "c"]
    values = [0.0, 0.0, 0.0]
    i = 0
    for char in options:
        values[i] = read_input("Wprowadz wartosc " + char + ":\n")
        i += 1

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
            return x1, x2

        else:
            print("Jeden pierwiastek", -b / (2 * a))
            return True


if __name__ == "__main__":
    rownanie()

