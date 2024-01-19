from cli import Cli
from dsa.random_int_array import RandomIntArray
from sortings.bubble_sort import BubbleSort
from sortings.insertion_sort import InsertionSort
from sortings.selection_sort import SelectionSort

class Sortings:
    @staticmethod
    def menu():
        arr = RandomIntArray.gen_1d_arr(20)
        Cli.menu([
            {"name": "1. Metoda bąbelkowa.", "function": BubbleSort.sort, "func_args": arr},
            {"name": "2. Metoda przez wstawianie.", "function": InsertionSort.sort, "func_args": arr},
            {"name": "3. Metoda przez wybieranie.", "function": SelectionSort.sort, "func_args": arr},
            {"name": "6. Wyjscie.", "function": None, "func_args": None},
        ], "Menu glowne.", None)
