def funkcja(x):
    return x**3 - x**2 - x + 2

def metoda_bisekcji(a, b, dokladnosc):
    count = 0

    if funkcja(a) * funkcja(b) >= 0:
        print("Nieprawidłowy przedział")
        return None

    while (b - a) >= dokladnosc:
        count +=1
        print(count)
        c = (a + b) / 2

        if funkcja(c) == 0:
            break
        elif funkcja(c) * funkcja(a) < 0:
            b = c
        else:
            a = c

    return c


if __name__ == "__main__":
    print(metoda_bisekcji(-10, 10, 0.001))

