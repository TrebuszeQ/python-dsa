import unittest
from src.mathematical.polynomials.horner_method import horner_method


class MyTestCase(unittest.TestCase):
    def test_horner_method(self):
        self.assertEqual(-2.0, horner_method(1, -5, 1))


if __name__ == '__main__':
    unittest.main()
