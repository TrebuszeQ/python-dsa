import unittest
from src.relations.ordered_pair import OrderedPair
from src.relations.cartesian_product import CartesianProduct


class CartesianProductTest(unittest.TestCase):
    def test_product(self):
        pair1 = pair2 = OrderedPair(1, 2)
        self.assertEqual(CartesianProduct(pair1, pair2), [1, 2])


if __name__ == '__main__':
    unittest.main()
