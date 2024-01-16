import unittest

#my
from darboux import Darboux


class DarbouxTestCase(unittest.TestCase):
    def test_find_zero(self):
        print(Darboux.find_zero(2, 36, 1, 0))


if __name__ == '__main__':
    unittest.main()
