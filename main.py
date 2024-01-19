from cli import Cli
from dsa.dsa import Dsa
from sortings.sortings import Sortings
from math2.math2 import Math2
from data.dates import Dates
from other.other import Other

if __name__ == '__main__':
    opts = ("1. Struktury i typy danych.\n",
            "2. Sortowanie.\n",
            "3. Matematyczne.\n",
            "4. Data.\n",
            "5. Rozne.\n",
            "6. Wyjscie.\n")

    Cli.menu([
        {"name": "1. Struktury i typy.", "function": Dsa.menu, "func_args": None},
        {"name": "2. Sortowanie.", "function": Sortings.menu, "func_args": None},
        {"name": "3. Matematyczne.", "function": Math2.menu, "func_args": None},
        {"name": "4. Data.", "function": Dates.menu, "func_args": None},
        {"name": "5. Rozne.", "function": Other.menu, "func_args": None},
        {"name": "6. Wyjscie.", "function": None, "func_args": None},
    ], "Menu glowne.", None)

    # Cli.print_menu("Struktury danych i algorytmy.\n", "", opts)
    #
    # opt = 0
    # while opt != opts.__len__():
    #     opt = Cli.try_read_input_int("Podaj numer opcji [typu calkowitego].\n")
    #
    #     match opt:
    #         case 1:
    #             Dsa.menu()
    #
    #         case 2:
    #             Sortings.menu()
    #
    #         case 3:
    #             Math2.menu()
    #
    #         case 4:
    #             Data.menu()
    #
    #         case 5:
    #             Other.menu()





