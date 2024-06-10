def is_float(arg):
    if type(arg) is float:
        return True

    else:
        return False


def is_int(arg):
    if type(arg) is int:
        return True

    else:
        return False


def try_read_input_int(message):
    value: str
    truth = False

    while truth is False:
        value = input(message)
        print()

        try:
            value_int = int(value)
            truth = is_int(value_int)

            if truth:
                return value_int

            else:
                raise ValueError

        except ValueError or ...:
            print("Inserted value is not a valid one.\n")


def try_read_input_string(message):
    value: str = None

    while value is None or len(value) == 0:
        value = input(message)
        print()
    return value


def read_float_triple():
    values = [0.0, 0.0, 0.0]
    variables: chr = ["a", "b", "c"]

    for i in range(0, values.__len__()):
        values[i] = try_read_input_float("Input value no. " + variables[i] + ":\n")

    return values


def try_read_input_float(message):
    value: str
    truth = False

    while truth is False:
        value = input(message)
        print()

        try:
            value_float = float(value)
            truth = is_float(value_float)

            if truth:
                return value_float

            else:
                raise ValueError

        except ValueError or ...:
            print("Inserted value is not a valid one.\n")


def read_interval_open_float(msg1, msg2):
    a = 0
    b = 0

    while a >= b:
        a = try_read_input_float(msg1)
        print()
        b = try_read_input_float(msg2)

        if a >= b:
            print("a must be greater than b.")

    return a, b


def read_interval_closed_float(msg1, msg2):
    a = 3
    b = 0

    while a > b:
        a = try_read_input_float(msg1)
        b = try_read_input_float(msg2)

        if a > b:
            print("a must be lesser or equal than b.")

    return a, b
