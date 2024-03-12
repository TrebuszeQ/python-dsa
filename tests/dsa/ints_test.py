import unittest
from unittest.mock import patch

# my
from ints import Ints


class IntsTestCase(unittest.TestCase):
    def test_sum_integer_len(self):
        result = Ints._sum_integer_len(555)
        self.assertEqual(15, result)


if __name__ == '__main__':
    unittest.main()
