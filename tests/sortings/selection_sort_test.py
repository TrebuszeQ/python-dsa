import unittest

# my
from selection_sort import SelectionSort
from src.dsa.random_int_array import RandomIntArray


class SelectionSortCase(unittest.TestCase):
    def setUp(self):
        self.arr = RandomIntArray.gen_1d_arr(20)

    def test_sort_valid(self):
        print(sorted(self.arr))
        self.assertEqual(sorted(self.arr), SelectionSort.sort(self.arr))\


    def test_sort2_count_valid(self):
        print(sorted(self.arr))


if __name__ == '__main__':
    unittest.main()
