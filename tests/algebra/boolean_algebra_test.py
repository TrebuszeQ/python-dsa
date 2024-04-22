import unittest
from app.algebra.boolean_algebra import BooleanAlgebra


class MyTestCase(unittest.TestCase):
    def test_law_of_excluded_middle_valid(self):
        binary = bin(5)[2:]
        self.assertEqual(BooleanAlgebra.excluded_middle(5), binary)

    def test_law_of_double_negation_valid(self):
        binary = bin(5)[2:]
        self.assertEqual(BooleanAlgebra.double_negation(5), binary)


if __name__ == '__main__':
    unittest.main()
