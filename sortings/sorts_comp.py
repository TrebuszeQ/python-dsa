from sortings import BubbleSort, InsertionSort, SelectionSort, QuickSort
from cli import Cli

# sortings comparison
class SortsComp:
    @staticmethod
    def print_arr(lis, intro, outro):
        if intro is not None:
            print(intro)

        for i in range(len(lis)):
            print(i, ". ", lis[i])

        if outro is not None:
            print(outro)

    @staticmethod
    def _run_all_unsorted(arr):
        res_bub = BubbleSort.sort(arr)
        res_ins = InsertionSort.sort(arr)
        res_sel = SelectionSort.sort(arr)
        res_qui = QuickSort.sort(arr, 0, (len(arr)-1))

        return res_bub, res_ins, res_sel, res_qui

    @staticmethod
    def _run_all_sorted(arr):
        res_bub = BubbleSort.sort(arr)
        res_ins = InsertionSort.sort(arr)
        res_sel = SelectionSort.sort(arr)
        res_qui = QuickSort.sort(arr, 0, (len(arr) - 1))

        return res_bub, res_ins, res_sel, res_qui

    @staticmethod
    def compare():

