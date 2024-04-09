import unittest

# my
from power import Power


class PowerTest(unittest.TestCase):
    def test_ipower_valid(self):
        self.assertEqual(32768, Power.ipower(2, 15))

    def test_ipower_invalid_base(self):
        self.assertFalse(Power.ipower("e", 2))

    def test_ipower_invalid_exponent(self):
        self.assertFalse(Power.ipower(22.5, 3.1))

    def test_rpower_valid(self):
        self.assertEqual(32768, Power.rpower(2, 0, 15, 0))

    def test_rpower_invalid_base(self):
        self.assertFalse(Power.rpower(None, 0, 2, 0))

    def test_rpower_invalid_exponent(self):
        self.assertFalse(Power.rpower(4.5, 0, None, 0))

    def test_two_ipower(self):
        self.assertEqual(4, Power.two_ipower(2))

    def test_two_rpower(self):
        self.assertEqual(4, Power.two_rpower(2, 0, 0))


if __name__ == '__main__':
    unittest.main()
