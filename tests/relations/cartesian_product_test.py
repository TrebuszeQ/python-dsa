import unittest
from src.relations.ordered_pair import OrderedPair
from src.relations.cartesian_product import CartesianProduct


class CartesianProductTest(unittest.TestCase):
    def test_pair1(self):
        pair1 = OrderedPair(1, 3)
        pair2 = OrderedPair(1, 2)
        cartesian_product = CartesianProduct(pair1, pair2)
        self.assertEqual([1, 3], cartesian_product.pair1.ordered_pair)

    def test_product_not_empty(self):
        pair1 = OrderedPair(1, 3)
        pair2 = OrderedPair(1, 2)
        self.assertEqual([(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2)], CartesianProduct(pair1, pair2).product)

    def test_product_empty(self):
        pair1 = OrderedPair(0, 0)
        pair2 = OrderedPair(0, 0)
        self.assertEqual([(0, 0)], CartesianProduct(pair1, pair2).product)


if __name__ == '__main__':
    unittest.main()
