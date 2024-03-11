import unittest

# my
from random_int_array import RandomIntArray


class MyTestCase(unittest.TestCase):
    def test_gen_1d_arr(self):
        self.assertTrue(RandomIntArray.gen_1d_arr(20).__len__() == 20)


if __name__ == '__main__':
    unittest.main()
