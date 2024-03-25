import unittest
from src.mathematical.relations.ordered_pair import OrderedPair
from src.mathematical.relations import CartesianProduct


class CartesianProductTest(unittest.TestCase):
    def test_pair1(self):
        pair1 = OrderedPair(1, 3)
        pair2 = OrderedPair(1, 2)
        cartesian_product = CartesianProduct([pair1, pair2])
        self.assertEqual([1, 2], cartesian_product.ordered_pairs[1].pair)

    def test_product_not_empty(self):
        pair1 = OrderedPair(1, 3)
        pair2 = OrderedPair(1, 2)
        product = CartesianProduct([pair1, pair2])._of_two_sets()
        self.assertEqual([(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2)], product)

    def test_product_empty(self):
        pair1 = OrderedPair(0, 0)
        pair2 = OrderedPair(0, 0)
        product = CartesianProduct([pair1, pair2])._of_two_sets()
        self.assertEqual([(0, 0)], product)

    def test_cartesian_product(self):
        ordered_pairs = [OrderedPair(1, 2), OrderedPair(5, 6), OrderedPair(3, 4)]
        product = CartesianProduct(ordered_pairs)._of_three_sets()
        self.assertEqual([[1, 5, 3],
                          [1, 5, 4],
                          [1, 6, 3],
                          [1, 6, 4],
                          [2, 5, 3],
                          [2, 5, 4],
                          [2, 6, 3],
                          [2, 6, 4]], product)


if __name__ == '__main__':
    unittest.main()
