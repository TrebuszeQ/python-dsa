import unittest

from app.services.graph_maker_service import GraphMaker


class MyTestCase(unittest.TestCase):
    points_arr = [0, 2], [1, 3], [2, 7], [3, 11], [4, 17], [5, 23], [6, 31], [7, 47]
    graph_maker = GraphMaker(points_arr)

    def test_max_y(self):
        self.assertEqual(47, self.graph_maker.max_y)

    def test_min_y(self):
        self.assertEqual(0, self.graph_maker.min_y)

    def test_max_x(self):
        self.assertEqual(7, self.graph_maker.max_x)

    def test_draw_y(self):
        self.graph_maker.draw_y(6)


if __name__ == '__main__':
    unittest.main()
