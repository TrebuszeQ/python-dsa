import unittest
from unittest.mock import patch
from app.algebra.prime_numbers.inverse_prime_sum_with_spacing import sum_inverted_primes_with_spacing


class SumInversePrimeWithSpacingTests(unittest.TestCase):
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=1)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=1000000)
    def test_sum_inverse_primes_valid_1_1m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 1.5784669751768943)

    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=2)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=1000000)
    def test_sum_inverse_primes_valid_2_1m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 1.175330672125438)

    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=3)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=1000000)
    def test_sum_inverse_primes_valid_3_1m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 0.9672560179593346)

    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=4)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=1000000)
    def test_sum_inverse_primes_valid_4_1m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 0.8626940527116524)

    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=5)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=1000000)
    def test_sum_inverse_primes_valid_5_1m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 0.784682334703699)

    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=6)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=1000000)
    def test_sum_inverse_primes_valid_6_1m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 0.741564074031592)

    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=7)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=1000000)
    def test_sum_inverse_primes_valid_7_1m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 0.7017309820523377)

    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=10)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=1000000)
    def test_sum_inverse_primes_valid_10_1m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 0.6348901330110017)

    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=20)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=1000000)
    def test_sum_inverse_primes_valid_20_1m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 0.5)

    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=50)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=1000000)
    def test_sum_inverse_primes_valid_20_1m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 0.5203884450925245)

    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=100)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=1000000)
    def test_sum_inverse_primes_valid_100_1m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 0.5087578678548416)

    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=1000)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=1000000)
    def test_sum_inverse_primes_valid_1000_1m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 0.5005034194055528)

    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=5000)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=1000000)
    def test_sum_inverse_primes_valid_5000_1m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 0.5000611791704742)

    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=10000)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=1000000)
    def test_sum_inverse_primes_valid_10000_1m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 0.5000230378919792)

    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=1)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=10000000)
    def test_sum_inverse_primes_valid_1_10m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 1.6555278916360612)

    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=2)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=10000000)
    def test_sum_inverse_primes_valid_2_10m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 1.2267047999500047)

    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=3)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=10000000)
    def test_sum_inverse_primes_valid_3_10m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 1.0057862012956975)

    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=4)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=10000000)
    def test_sum_inverse_primes_valid_4_10m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 0.8935182895270217)

    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=5)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=10000000)
    def test_sum_inverse_primes_valid_5_10m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 0.8103696734287238)

    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=6)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=10000000)
    def test_sum_inverse_primes_valid_6_10m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 0.7635818004602971)

    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=7)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=10000000)
    def test_sum_inverse_primes_valid_7_10m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 0.7209958485617317)

    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=10)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=10000000)
    def test_sum_inverse_primes_valid_10_10m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 0.6489008222008228)

    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=20)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=10000000)
    def test_sum_inverse_primes_valid_20_10m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 0.5)

    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=50)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=10000000)
    def test_sum_inverse_primes_valid_20_10m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 0.5234100520089466)

    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=100)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=10000000)
    def test_sum_inverse_primes_valid_100_10m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 0.5102834753385417)

    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=1000)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=10000000)
    def test_sum_inverse_primes_valid_1000_10m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 0.5006572639150931)

    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=5000)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=10000000)
    def test_sum_inverse_primes_valid_5000_10m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 0.5000921531490286)

    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=10000)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=10000000)
    def test_sum_inverse_primes_valid_10000_10m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 0.5000388050183333)

    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=1)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=50000000)
    def test_sum_inverse_primes_valid_1_50m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 1.7031156684639315)

    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=2)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=50000000)
    def test_sum_inverse_primes_valid_2_50m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 1.2584299644964403)

    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=3)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=50000000)
    def test_sum_inverse_primes_valid_3_50m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 1.0295801197231094)

    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=4)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=50000000)
    def test_sum_inverse_primes_valid_4_50m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 0.9125534282556389)

    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=5)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=50000000)
    def test_sum_inverse_primes_valid_5_50m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 0.8262322257011913)

    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=6)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=50000000)
    def test_sum_inverse_primes_valid_6_50m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum,  0.7771783481287037)

    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=7)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=50000000)
    def test_sum_inverse_primes_valid_7_50m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 0.7328927777851436)

    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=10)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=50000000)
    def test_sum_inverse_primes_valid_10_50m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 0.6575531270787647)

    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=20)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=50000000)
    def test_sum_inverse_primes_valid_20_50m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 0.5)

    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=50)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=50000000)
    def test_sum_inverse_primes_valid_20_50m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 0.5252762805153434)

    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=100)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=50000000)
    def test_sum_inverse_primes_valid_100_50m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 0.5112258627882955)

    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=1000)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=50000000)
    def test_sum_inverse_primes_valid_1000_50m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 0.5007523932362291)

    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=5000)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=50000000)
    def test_sum_inverse_primes_valid_5000_50m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 0.5001112312560261)

    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_spacing", return_value=10000)
    @patch("app.algebra.prime_numbers.inverse_prime_sum_with_spacing._read_upper_limit", return_value=50000000)
    def test_sum_inverse_primes_valid_10000_50m(self, read_spacing, read_upper_limit):
        inv_sum = sum_inverted_primes_with_spacing()
        self.assertEqual(inv_sum, 0.5000483250206618)


if __name__ == '__main__':
    unittest.main()
