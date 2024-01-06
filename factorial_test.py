import unittest
from math import pow

# my
from factorial import Factorial


class MyTestCase(unittest.TestCase):
    def test_iterable(self):
        # self.assertEqual((1202423401 * pow(10, 65657059)), Factorial.iterable(10000000))
        self.assertEqual(6402373705728000, Factorial.iterable(18))

    def test_recursive(self):
        self.assertEqual(6402373705728000, Factorial.recursive(18))


if __name__ == '__main__':
    unittest.main()
