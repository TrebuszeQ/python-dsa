import unittest
import sys
from math import pow

# my
from factorial import Factorial


class MyTestCase(unittest.TestCase):
    # def test_iterative(self):
    #     # self.assertEqual((1202423401 * pow(10, 65657059)), Factorial.iterable(10000000))
    #     self.assertEqual(6402373705728000, Factorial.iterative(18))
    #
    # def test_recursive(self):
    #     self.assertEqual(6402373705728000, Factorial.recursive(18))
    #
    # # zad 4.1 testuje wartosc 2, 20, 50, 100
    # def test_iterative_2(self):
    #     self.assertEqual(2, Factorial.iterative(2))
    #
    # # zad 4.1 testuje wartosc 20
    # def test_iterative_20(self):
    #     self.assertEqual(2432902008176640000, Factorial.iterative(20))
    #
    # # zad 4.1 testuje wartosc 50
    # def test_iterative_50(self):
    #     self.assertAlmostEqual(30414093201713378043612608166064768844377641568960512000000000000, Factorial.iterative(50))
    #
    # # zad 4.1 testuje wartosc 100
    # def test_iterative_100(self):
    #     self.assertAlmostEqual(93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
    #                            , Factorial.iterative(100))

    def test_iterative_v_2(self):
        self.assertEqual(2, Factorial.iterative_verbose(2))

    # zad 4.1 testuje wartosc 20
    def test_iterative_v_20(self):
        self.assertEqual(2432902008176640000, Factorial.iterative_verbose(20))

    # zad 4.1 testuje wartosc 50
    def test_iterative_v_50(self):
        self.assertAlmostEqual(30414093201713378043612608166064768844377641568960512000000000000, Factorial.iterative_verbose(50))

    # zad 4.1 testuje wartosc 100
    def test_iterative_v_100(self):
        self.assertAlmostEqual(93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
                               , Factorial.iterative_verbose(100))


if __name__ == '__main__':
    unittest.main()
