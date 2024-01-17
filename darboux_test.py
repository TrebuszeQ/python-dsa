import unittest

#my
from darboux import Darboux


class DarbouxTestCase(unittest.TestCase):
    # def test_find_zero(self):
    #     print(Darboux._find_zero(2, 6, 1))

    def test_find_zero_invalid(self):
        self.assertFalse(Darboux._find_zero(2, 36, 1, 0))

    def test_find_zero_valid(self):
        self.assertTrue(Darboux._find_zero(2, 6, 6, 0))

    def test_darboux_invalid(self):
        Darboux.darboux()


if __name__ == '__main__':
    unittest.main()
