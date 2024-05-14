import math
from app.utils.input_readers import read_float_triple


def get_delta(a, b, c):
    return (b * b) - 4 * (a * c)


def get_equation(values):
    a, b, c = values

    if a.__eq__(0):
        print("Not a quad equation but linear equation.\n", -c / b)
        return False

    else:
        delta = get_delta(a, b, c)

        if delta < 0:
            print("No resolutions.\n")
            return None

        elif delta > 0:
            x1 = ((-b - math.sqrt(delta)) / (2 * a))
            x2 = ((-b + math.sqrt(delta)) / (2 * a))
            print(f"Two resolutions: x1 = {x1}, x2 = {x2}")
            return [x1, x2]

        else:
            print(f"One resolution: {-b / (2 * a)}")
            return True


if __name__ == "__main__":
    get_equation(read_float_triple())

