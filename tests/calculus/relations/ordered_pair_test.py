import unittest
from app.calculus.relations.ordered_pair import OrderedPair


class OrderedPairTest(unittest.TestCase):
    def test_get_predecessor(self):
        self.assertEqual(0, OrderedPair(0, 1).predecessor)

    def test_get_successor(self):
        self.assertEqual(1, OrderedPair(0, 1).successor)

    def test_get_collection(self):
        pair = OrderedPair(2, 7)
        self.assertEqual([2, 3, 4, 5, 6, 7], pair.collection)


if __name__ == '__main__':
    unittest.main()
