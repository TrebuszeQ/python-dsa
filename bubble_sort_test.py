import unittest
import copy
from bubble_sort import BubbleSort

class BubbleSortTest(unittest.TestCase):

    def test_sort_valid_list(self, lis=[1, 6, 3, 0, 12, 5, -1]):
        lis2 = copy.copy(lis)
        lis2.sort()
        self.assertEqual(lis2, BubbleSort.sort(lis))


if __name__ == '__main__':
    unittest.main()
