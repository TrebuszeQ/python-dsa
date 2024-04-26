import unittest
from app.algebra.boolean_algebra import BooleanAlgebra


class MyTestCase(unittest.TestCase):

    def test_law_of_double_negation_valid(self):
        algebra = BooleanAlgebra(3)
        result = algebra.double_negation()
        self.assertEqual(result, 1)

    def test_law_of_excluded_middle_valid(self):
        algebra = BooleanAlgebra(3)
        result = algebra.excluded_middle()
        self.assertEqual(result, 1)

    def test_law_of_contradiction_valid(self):
        algebra = BooleanAlgebra(3)
        result = algebra.contradiction()
        self.assertEqual(result, 1)

    def test_law_of_alternative_simplification_valid(self):
        algebra = BooleanAlgebra(3)
        result = algebra.alternative_simplification()
        self.assertEqual(result, 1)

    def test_law_of_conjuction_simplification_valid(self):
        algebra = BooleanAlgebra(3)
        result = algebra.conjuction_simplification()
        self.assertEqual(result, 1)

    def test_first_law_of_clavius_valid(self):
        algebra = BooleanAlgebra(3)
        result = algebra.first_clavius()
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
