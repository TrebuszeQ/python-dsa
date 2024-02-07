import unittest

from stack import Stack


class MyTestCase(unittest.TestCase):
    def test_empty_empty(self):
        stack = Stack(None)
        self.assertEqual(True, stack.empty())

    def test_empty_full(self):
        stack = Stack([1, 2, 3])
        self.assertEqual(False, stack.empty())

    def test_push_valid_on_empty(self):
        stack = Stack(None)
        self.assertEqual([4], stack.push(4))

    def test_push_valid_arr_full(self):
        stack = Stack([1, 2, 3])
        self.assertEqual([1, 2, 3, 1], stack.push(1))


if __name__ == '__main__':
    unittest.main()
