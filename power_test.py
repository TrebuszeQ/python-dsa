import unittest

# my
from power import Power

class PowerTest(unittest.TestCase):
    def test_ipower(self):
        self.assertEqual(32768, Power.ipower(2.0, 15))


if __name__ == '__main__':
    unittest.main()
