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

        random.seed(1)
        for i in range(0, n):
            arr.append(random.randint(0, 999))

        return arr

    # arr = gen_arr(20)
    # formatuje wyswietlanie tablicy przed i po sortowaniu

    @staticmethod
    def print_arr_fm(i, arr1, arr2):
        print(f'{i:2}: {arr1[i]:5} {arr2[i]}:5')

    @staticmethod
    def _run_all_unsorted(arr):
        res_bub = BubbleSort.sort(arr)
        res_ins = InsertionSort.sort(arr)
        res_sel = SelectionSort.sort(arr)
        res_qui = QuickSort.sort(arr, 0, (len(arr) - 1))

        return res_bub, res_ins, res_sel, res_qui

    @staticmethod
    def _run_all_sorted(arr):
        res_bub = BubbleSort.sort(arr)
        res_ins = InsertionSort.sort(arr)
        res_sel = SelectionSort.sort(arr)
        res_qui = QuickSort.sort(arr, 0, (len(arr) - 1))

        return res_bub, res_ins, res_sel, res_qui

    def test_something(self):
        SortsCompCase._run_all_unsorted(arr=self.arr)
        SortsCompCase._run_all_sorted(arr=self.arr)


if __name__ == '__main__':
    unittest.main()
