import unittest
from app.algebra.boolean_algebra import BooleanAlgebra


class MyTestCase(unittest.TestCase):

    def test_law_of_double_negation_valid(self):
        tt, result = BooleanAlgebra.make_table_of_truth_to_range_and_print(BooleanAlgebra.double_negation, title="Double Negation Truth Table")
        self.assertEqual(result, 1)

    def test_law_of_excluded_middle_valid(self):
        tt, result = BooleanAlgebra.make_table_of_truth_to_range_and_print(BooleanAlgebra.excluded_middle, title="Excluded Middle Truth Table")
        self.assertEqual(result, 1)

    def test_law_of_contradiction_valid(self):
        tt, result = BooleanAlgebra.make_table_of_truth_to_range_and_print(BooleanAlgebra.contradiction, title="Contradiction Truth Table")
        self.assertEqual(result, 1)

    def test_law_of_alternative_simplification_valid(self):
        tt, result = BooleanAlgebra.make_table_of_truth_to_range_and_print(BooleanAlgebra.alternative_simplification, title="Alternative Simplification Truth Table")
        self.assertEqual(result, 1)

    def test_law_of_conjuction_simplification_valid(self):
        tt, result = BooleanAlgebra.make_table_of_truth_to_range_and_print(BooleanAlgebra.conjuction_simplification, title="Conjuction Simplification Truth Table")
        self.assertEqual(result, 1)

    def test_first_law_of_clavius_valid(self):
        tt, result = BooleanAlgebra.make_table_of_truth_to_range_and_print(BooleanAlgebra.first_law_of_clavius, title="First Law of Clavius Truth Table")
        self.assertEqual(result, 1)

    def test_second_law_of_clavius_valid(self):
        tt, result = BooleanAlgebra.make_table_of_truth_to_range_and_print(BooleanAlgebra.second_law_of_clavius, title="Second Law of Clavius Truth Table")
        self.assertEqual(result, 1)

    def test_law_of_duns_scotus(self):
        tt, result = BooleanAlgebra.make_table_of_truth_to_range_and_print(BooleanAlgebra.law_of_duns_scotus, q=True, title="Law of Duns Scotus Truth Table")
        self.assertEqual(result, 1)

    def test_first_law_of_simplification(self):
        tt, result = BooleanAlgebra.make_table_of_truth_to_range_and_print(BooleanAlgebra.first_law_of_simplification, q=True, title="First Law of Simplification Truth Table")
        self.assertEqual(result, 1)

    def test_second_law_of_simplification(self):
        tt, result = BooleanAlgebra.make_table_of_truth_to_range_and_print(BooleanAlgebra.second_law_of_simplification, q=True, title="Second Law of Simplification Truth Table")
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
