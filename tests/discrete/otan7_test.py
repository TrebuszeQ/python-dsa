import unittest
from app.discrete.otan7 import OtaN7


class DiscreteMathProject1(unittest.TestCase):

    def test_degree_valid(self):
        lis = [1, 2, 3, 4, 5, 6, 7]
        ota = OtaN7(lis)
        print(len(lis))
        self.assertEqual(ota._degree, len(lis))


if __name__ == '__main__':
    unittest.main()
