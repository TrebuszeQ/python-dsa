import unittest

# my
from insertion_sort import InsertionSort
from src.dsa.random_int_array import RandomIntArray


class InsertionSortTestCase(unittest.TestCase):
    def setUp(self):
        self.arr = RandomIntArray.gen_1d_arr(20)

    def test_sort_valid(self):
        arr = RandomIntArray.gen_1d_arr(20)
        arr_2 = InsertionSort.sort(arr)
        arr_3 = sorted(arr)
        print(arr_3)
        self.assertEqual(arr_3, arr_2)

    def test_flag_sort_valid(self):
        arr = RandomIntArray.gen_1d_arr(20)
        arr_2 = InsertionSort.sort_flag_count(arr)[0]
        arr_3 = sorted(arr)
        print(arr_3)
        self.assertEqual(arr_3, arr_2)


if __name__ == '__main__':
    unittest.main()
