import unittest
from src.relations.ordered_pair import OrderedPair
from src.relations.cartesian_product_2 import CartesianProduct2


class CartesianProductTest(unittest.TestCase):
    def test_cartesian_product(self):
        ordered_pairs = [OrderedPair(1, 3), OrderedPair(1, 3), OrderedPair(3, 4)]
        self.assertEqual([(1, 1, 3),
                          (1, 1, 4),
                          (1, 2, 3),
                          (1, 2, 4),
                          (1, 3, 3),
                          (1, 3, 4),
                          (2, 1, 3),
                          (2, 1, 4),
                          (2, 2, 3),
                          (2, 2, 4),
                          (2, 3, 3),
                          (2, 3, 4),
                          (3, 1, 3),
                          (3, 1, 4),
                          (3, 2, 3),
                          (3, 2, 4),
                          (3, 3, 3),
                          (3, 3, 4)], CartesianProduct2(ordered_pairs).product)
