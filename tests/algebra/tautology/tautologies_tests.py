import unittest
from app.algebra.tautology.tautologies import Tautologies


class TautologiesTests(unittest.TestCase):

    def test_law_of_double_negation_valid(self):
        tt, result = Tautologies.make_table_of_truth_to_range_and_print(Tautologies.double_negation,
                                                                        title="Double Negation Truth Table")
        self.assertEqual(result, 1)

    def test_rule_of_excluded_middle_valid(self):
        tt, result = Tautologies.make_table_of_truth_to_range_and_print(Tautologies.excluded_middle,
                                                                        title="Excluded Middle Truth Table")
        self.assertEqual(result, 1)

    def test_law_of_contradiction_valid(self):
        tt, result = Tautologies.make_table_of_truth_to_range_and_print(Tautologies.contradiction,
                                                                        title="Contradiction Truth Table")
        self.assertEqual(result, 1)

    def test_law_of_alternative_simplification_valid(self):
        tt, result = Tautologies.make_table_of_truth_to_range_and_print(Tautologies.alternative_simplification,
                                                                        title="Alternative Simplification Truth Table")
        self.assertEqual(result, 1)

    def test_law_of_conjuction_simplification_valid(self):
        tt, result = Tautologies.make_table_of_truth_to_range_and_print(Tautologies.conjuction_simplification,
                                                                        title="Conjuction Simplification Truth Table")
        self.assertEqual(result, 1)

    def test_first_rule_of_clavius_valid(self):
        tt, result = Tautologies.make_table_of_truth_to_range_and_print(Tautologies.first_rule_of_clavius,
                                                                        title="First Rule of Clavius Truth Table")
        self.assertEqual(result, 1)

    def test_second_rule_of_clavius_valid(self):
        tt, result = Tautologies.make_table_of_truth_to_range_and_print(Tautologies.second_rule_of_clavius,
                                                                        title="Second Rule of Clavius Truth Table")
        self.assertEqual(result, 1)

    def test_rule_of_duns_scotus(self):
        tt, result = Tautologies.make_table_of_truth_to_range_and_print(Tautologies.rule_of_duns_scotus,
                                                                        q=True,
                                                                        title="Rule of Duns Scotus Truth Table")
        self.assertEqual(result, 1)

    def test_first_law_of_simplification(self):
        tt, result = Tautologies.make_table_of_truth_to_range_and_print(Tautologies.first_law_of_simplification,
                                                                        q=True,
                                                                        title="First Rule of Simplification Truth Table")
        self.assertEqual(result, 1)

    def test_second_law_of_simplification(self):
        tt, result = Tautologies.make_table_of_truth_to_range_and_print(Tautologies.second_rule_of_simplification,
                                                                        q=True,
                                                                        title="Second Rulecd of Simplification Truth Table")
        self.assertEqual(result, 1)

    def test_first_de_morgan_law(self):
        tt, result = Tautologies.make_table_of_truth_to_range_and_print(Tautologies.first_de_morgans_rule,
                                                                        q=True,
                                                                        title="First De Morgan's Rule Truth Table")
        self.assertEqual(result, 1)

    def test_second_de_morgan_law(self):
        tt, result = Tautologies.make_table_of_truth_to_range_and_print(Tautologies.second_de_morgan_law,
                                                                        q=True,
                                                                        title="Second De Morgan's Rule Truth Table")
        self.assertEqual(result, 1)

    def test_first_rule_of_implication(self):
        tt, result = Tautologies.make_table_of_truth_to_range_and_print(Tautologies.first_rule_of_implication,
                                                                        q=True,
                                                                        title="First Rule of Implication Truth Table")
        self.assertEqual(result, 1)

    def test_first_rule_of_exclusive_disjunction(self):
        tt, result = Tautologies.make_table_of_truth_to_range_and_print(Tautologies.first_rule_of_exclusive_disjunction,
                                                                        q=True,
                                                                        title="First Rule of Exclusive Disjunction Truth Table")
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
