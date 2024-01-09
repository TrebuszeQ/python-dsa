import unittest

# my
from floats import Floats


class FloatsTestCase(unittest.TestCase):
    def test_sum_n(self):
        self.assertNotEqual(Floats._sum(), (1000000 * 1.23456789))


if __name__ == '__main__':
    unittest.main()
