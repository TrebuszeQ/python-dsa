import unittest

# my
from factorial import Factorial


class MyTestCase(unittest.TestCase):
    def test_iterable(self):
        self.assertEqual(10000000, Factorial.iterable(10000000))

    def test_recursive(self):
        self.assertEqual(6402373705728000, Factorial.recursive(18, 0, 0))


if __name__ == '__main__':
    unittest.main()
