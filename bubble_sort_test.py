import unittest
from bubble_sort import BubbleSort


class BubbleSortTest(unittest.TestCase):

    def test_sort_valid_list(self, lis=[1, 6, 3, 0, 12, 5, -1]):
        obj = BubbleSort(lis)

        self.assertEqual(obj.sort(), lis.sort())


if __name__ == '__main__':
    unittest.main()
