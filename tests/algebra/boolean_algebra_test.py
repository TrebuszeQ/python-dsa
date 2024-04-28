import unittest
from app.algebra.boolean_algebra import BooleanAlgebra


class MyTestCase(unittest.TestCase):

    def test_law_of_double_negation_valid(self):
        result = BooleanAlgebra.double_negation(3)
        self.assertEqual(result, 1)

    def test_law_of_excluded_middle_valid(self):
        result = BooleanAlgebra.excluded_middle(3)
        self.assertEqual(result, 1)

    def test_law_of_contradiction_valid(self):
        result = BooleanAlgebra.contradiction(3)
        self.assertEqual(result, 1)

    def test_law_of_alternative_simplification_valid(self):
        result = BooleanAlgebra.alternative_simplification(3)
        self.assertEqual(result, 1)

    def test_law_of_conjuction_simplification_valid(self):
        result = BooleanAlgebra.conjuction_simplification(3)
        self.assertEqual(result, 1)

    def test_first_law_of_clavius_valid(self):
        result = BooleanAlgebra.first_law_of_clavius(3)
        self.assertEqual(result, 1)

    def test_second_law_of_clavius_valid(self):
        result = BooleanAlgebra.second_law_of_clavius(3)
        self.assertEqual(result, 1)

    def test_law_of_duns_scotus(self):
        result = BooleanAlgebra.law_of_duns_scotus(3, 4)
        self.assertEqual(result, 1)

    def test_first_law_of_simplification(self):
        result = BooleanAlgebra.first_law_of_simplification(3, 4)
        self.assertEqual(result, 1)
        self.assertEqual(result, 1)

    def test_second_law_of_simplification(self):
        result = BooleanAlgebra.second_law_of_simplification(3, 4)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
