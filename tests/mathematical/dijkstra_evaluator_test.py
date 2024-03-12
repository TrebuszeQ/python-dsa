import unittest

from dijkstra_evaluator import DijkstraEvaluator


class MyTestCase(unittest.TestCase):

    def test_count_parentheses_valid(self):
        self.assertEqual((2, 2), DijkstraEvaluator._count_parentheses("(2*3+(1+2)/2)"))

    def test_count_parentheses_invalid(self):
        self.assertEqual((2, 3), DijkstraEvaluator._count_parentheses("(2*3+(1+2)/2))"))

    def test_check_parentheses_parity_valid(self):
        self.assertTrue(DijkstraEvaluator._check_parentheses_parity(2, 2))

    def test_check_parentheses_parity_invalid(self):
        self.assertFalse(DijkstraEvaluator._check_parentheses_parity(2, 3))

    def test_traverse_valid_integer(self):
        self.assertEqual(7.5, DijkstraEvaluator._traverse("(2*3+(1+2)/2)"))

    def test_traverse_valid_integer2(self):
        self.assertEqual(0, DijkstraEvaluator._traverse("(2*3/4-(1+2)/2)"))

    def test_traverse_valid_integer3(self):
        self.assertEqual(101, DijkstraEvaluator._traverse("(1+((2+3)*(4*5)))"))


if __name__ == '__main__':
    unittest.main()
