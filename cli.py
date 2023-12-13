class Cli:

    @staticmethod
    # sprawdza czy wartosc jest typu float
    def is_float(arg):
        if type(arg) is float:
            return True

        else:
            return False

    @staticmethod
    def is_int(arg):
        if type(arg) is int:
            return True

        else:
            return False

    @staticmethod
    def try_read_input_int(message):
        value: str
        truth = False

        while truth is False:
            value = input(message)
            value_int = None

            try:
                value_int = int(value)
                truth = Cli.is_int(value_int)

                if truth:
                    return value_int

                else:
                    raise ValueError

            except ValueError or ...:
                print("Wprowadzono nieprawidlowa wartosc.\n")

    @staticmethod
    # probuje odczytac wejscie float
    def try_read_input_float(message):
        value: str
        truth = False

        while truth is False:
            value = input(message)
            value_float = None

            try:
                value_float = float(value)
                truth = Cli.is_float(value_float)

                if truth:
                    return value_float

                else:
                    raise ValueError

            except ValueError or ...:
                print("Wprowadzono nieprawidlowa wartosc.\n")

    @staticmethod
    # probuje odczytac wartosc float 3 razy i zwraca tablice
    def read_float_triple():
        values = [0.0, 0.0, 0.0]
        variables: chr = ["a", "b", "c"]

        for i in range(0, values.__len__()):
            values[i] = Cli.try_read_input_float("Wprowadz wartosc " + variables[i] + ":\n")

        return values
