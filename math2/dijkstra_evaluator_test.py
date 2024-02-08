import unittest

from dijkstra_evaluator import DijkstraEvaluator


class MyTestCase(unittest.TestCase):
    def test_traverse_valid(self):
        self.assertEqual(7.5, DijkstraEvaluator._traverse("(2 * 3 + (1 + 2) / 2)"))  # add assertion here


if __name__ == '__main__':
    unittest.main()
