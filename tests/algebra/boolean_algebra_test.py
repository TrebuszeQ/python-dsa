import unittest
from app.algebra.boolean_algebra import BooleanAlgebra


class MyTestCase(unittest.TestCase):

    def test_law_of_double_negation_valid(self):
        result = BooleanAlgebra.double_negation(3)
        self.assertEqual(result, 1)

    def test_law_of_excluded_middle_valid(self):
        result = BooleanAlgebra.excluded_middle(3)
        self.assertEqual(result, 1)

    def test_law_of_contradiction(self):
        result = BooleanAlgebra.excluded_middle(3)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
