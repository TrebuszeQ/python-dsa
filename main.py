from cli import Cli
from dsa.dsa import Dsa
from sortings.sortings import Sortings
from math2.math2 import Math2
from data.dates import Dates
from other.other import Other

if __name__ == '__main__':
    Cli.menu([
        {"name": "1. Struktury i typy.", "function": Dsa.menu, "func_args": None},
        {"name": "2. Sortowanie.", "function": Sortings.menu, "func_args": None},
        {"name": "3. Matematyczne.", "function": Math2.menu, "func_args": None},
        {"name": "4. Data.", "function": Dates.menu, "func_args": None},
        {"name": "5. Rozne.", "function": Other.menu, "func_args": None},
        {"name": "6. Wyjscie.", "function": None, "func_args": None},
    ], "Menu glowne.", None)





