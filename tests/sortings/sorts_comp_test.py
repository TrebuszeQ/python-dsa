import unittest
import random

# my
from bubble_sort import BubbleSort
from insertion_sort import InsertionSort
from selection_sort import SelectionSort
from quick_sort import QuickSort


class SortsCompCase(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.arr = SortsCompCase.gen_arr(20)

    @staticmethod
    def gen_arr(n):
        arr = [-1]

        # random.seed(1)
        for i in range(0, n):
            arr.append(random.randint(0, 999))

        return arr

    # arr = gen_arr(20)
    # formatuje wyswietlanie tablicy przed i po sortowaniu

    @staticmethod
    def _print_arr(arr, intro, outro):
        if intro is not None:
            print(intro)
            print()

        for i in range(len(arr)):
            print(f'{i:2}: {arr[i]:5}')

        if outro is not None:
            print(outro)
            print()

    @staticmethod
    def print_arr_comp_fm(i, arr1, arr2):
        print(f'{i:2}: {arr1[i]:5} {arr2[i]}:5')

    @staticmethod
    def _run_all_unsorted(arr):
        res = []

        res_bub = BubbleSort.sort_count(arr)
        res.append([res_bub[1], res_bub[2]])
        SortsCompCase._print_arr(res_bub[0], "Sortowanie babelkowe.\n", None)

        res_ins = InsertionSort.sort2_count(arr)
        res.append([res_ins[1], res_ins[2]])
        SortsCompCase._print_arr(res_ins[0], "Sortowanie przez wstawianie.\n", None)

        res_ins_grd = InsertionSort.sort_guard_count(arr)
        res.append([res_ins_grd[1], res_ins_grd[2]])
        SortsCompCase._print_arr(res_ins_grd[0], "Sortowanie przez wstawianie ze straznikiem.\n", None)

        res_ins_fg = InsertionSort.sort_flag_count(arr)
        res.append([res_ins_fg[1], res_ins_fg[2]])
        SortsCompCase._print_arr(res_ins_fg[0], "Sortowanie wstawianie z flaga.\n", None)

        res_sel = SelectionSort.sort2_count(arr)
        SortsCompCase._print_arr(res_sel[0], "Sortowanie przez wyszukiwanie.\n", None)
        res.append([res_sel[1], res_sel[2]])

        res_qui = QuickSort.sort(arr, 0, (len(arr) - 1))
        SortsCompCase._print_arr(res_sel[0], "Sortowanie szybkie.\n", None)
        res.append([res_qui[1], res_qui[2]])

        return res

    @staticmethod
    def _run_all_sorted(arr):
        res_bub = BubbleSort.sort_count(arr)[0]
        res_ins = InsertionSort.sort(arr)
        res_sel = SelectionSort.sort(arr)
        res_qui = QuickSort.sort(arr, 0, (len(arr) - 1))

        return res_bub, res_ins, res_sel, res_qui

    def test_something(self):
        SortsCompCase._run_all_unsorted(arr=self.arr)
        SortsCompCase._run_all_sorted(arr=self.arr)


if __name__ == '__main__':
    unittest.main()
