import random

# my
from bubble_sort import BubbleSort
from insertion_sort import InsertionSort
from selection_sort import SelectionSort
from quick_sort import QuickSort


class SortsComp:
    @staticmethod
    def _gen_arr(n):
        arr = [-1]

        random.seed(1)
        for i in range(0, n):
            arr.append(random.randint(0, 999))

        return arr

    arr = _gen_arr(20)

    @staticmethod
    def _gen_unsorted_comparison_arr():
        return [
            {"Algo": "Bubble sort", "Array": BubbleSort.sort_down_to_count(SortsComp._gen_arr(20))},
            {"Algo": "Insertion sort with guard", "Array": InsertionSort.sort_count(SortsComp._gen_arr(20))},
            {"Algo": "Insertion sort with flag", "Array": InsertionSort.sort_flag_count(SortsComp._gen_arr(20))},
            {"Algo": "Selection sort", "Array": SelectionSort.sort2_count(SortsComp._gen_arr(20))},
            {"Algo": "Quick sort", "Array": QuickSort.sort(SortsComp._gen_arr(20), 0, (len(SortsComp._gen_arr(20)) - 1))}
        ]

    @staticmethod
    def _gen_sorted_comparison_arr(arr):
        return [
            {"Algo": "Bubble sort", "Array": BubbleSort.sort_down_to_count(arr)},
            {"Algo": "Insertion sort with guard", "Array": InsertionSort.sort_count(arr)},
            {"Algo": "Insertion sort with flag", "Array": InsertionSort.sort_flag_count(arr)},
            {"Algo": "Selection sort", "Array": SelectionSort.sort2_count(arr)},
            {"Algo": "Quick sort", "Array": QuickSort.sort(SortsComp._gen_arr(20), 0, (len(arr) - 1))}
        ]

    @staticmethod
    def print_comparison_table(arr, msg):
        print()
        print(msg)
        print(f"{'Algorytm':30}", f"{'Liczba porownan':20}", f"{'Liczba zamian':20}")
        print()

        for i in range(len(arr)):
            name = arr[i].__getitem__("Algo")
            current = arr[i].__getitem__("Array")
            print(f"{name:30}", f"{current[1]:0}", f"{current[2]:20}")

        print()

    @staticmethod
    def menu():
        SortsComp.print_comparison_table(SortsComp._gen_unsorted_comparison_arr(), "Porownanie wynikow sortowan na nieposortowanej tablicy")
        print()
        SortsComp.print_comparison_table(SortsComp._gen_sorted_comparison_arr(sorted(SortsComp.arr)), "Porownanie wynikow sortowan na posortowanej tablicy")


if __name__ == "__main__":
    SortsComp.menu()
