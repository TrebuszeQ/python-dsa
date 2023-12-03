import math


def odczytaj_wejscie_float(message):
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

    return value_float


def odczytaj_trzy_zmienne_float():
    values = [0.0, 0.0, 0.0]
    wspolczynniki: chr = ["a", "b", "c"]
    for i in range(0, 3):
        values[i] = odczytaj_wejscie_float("Wprowadz wartosc " + wspolczynniki[i] + ":\n")
    return values


def oblicz_delte(a, b, c):
    return (b * b) - 4 * (a * c)


def oblicz_rownanie(values):
    a, b, c = values

    if a.__eq__(0):
        print("To jest rownanie liniowe.\n", -c / b)
        return False

    else:
        delta = oblicz_delte(a, b, c)

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
    oblicz_rownanie(odczytaj_trzy_zmienne_float())

