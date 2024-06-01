import app.utils.input_readers as input_readers


def sum_per_incremental():
    pass


def __read_s():
    value = 0
    allowed = [2, 3, 4, 5, 6, 7, 10, 20, 50, 100, 1000, 5000, 10000]
    while value not in allowed:
        value = input_readers.try_read_input_int("Insert one of the following incremental values: [2, 3, 4, 5, 6, 7, 10, 20, 50, 100, 1000, 5000, 10000]")

    return value


def __read_upper_limit():
    value = 0
    allowed = [1000000, 10000000, 50000000]
    while value not in allowed:
        value = input_readers.try_read_input_int("Choose upper limit from: [1m, 10m, 50m].")

    return value


def __print_sum_of_opposites(s, upper_lim):
    print(f"Sum of opposites of prime numbers per increment of {s} to {upper_lim}")