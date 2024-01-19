from cli import Cli
from dsa.random_int_array import RandomIntArray
from sortings.bubble_sort import BubbleSort


class Sortings:
    @staticmethod
    def menu():
        Cli.menu([
            {"name": "1. Metoda bąbelkowa.", "function": BubbleSort.sort, "func_args": RandomIntArray.gen_1d_arr(20)},
            {"name": "6. Wyjscie.", "function": None, "func_args": None},
        ], "Menu glowne.", None)
