import unittest
from app.calculus.definite_sum import DefiniteSum


class DefiniteSumTest(unittest.TestCase):
    def test_definite_sum(self):
        self.assertEqual(6, DefiniteSum.definite_sum(3))  # add assertion here


if __name__ == '__main__':
    unittest.main()
