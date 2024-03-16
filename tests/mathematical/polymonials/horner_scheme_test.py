import unittest
from src.mathematical.polymonials.horner_scheme import horner_scheme


class MyTestCase(unittest.TestCase):
    def test_horner_scheme(self):
        self.assertEqual(4.0, horner_scheme(2, -6, 2))


if __name__ == '__main__':
    unittest.main()
