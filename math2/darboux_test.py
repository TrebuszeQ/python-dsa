import unittest

#my
from darboux import Darboux


class DarbouxTestCase(unittest.TestCase):
    # def test_find_zero(self):
    #     print(Darboux._find_zero(2, 6, 1))

    def test_find_zero_invalid(self):
        self.assertFalse(Darboux._bisection_recursive(2, 36, 1))

    @staticmethod
    def test_darboux_test_print_count():
        # print(Darboux._darboux())
        print(Darboux.darboux())


if __name__ == '__main__':
    unittest.main()
