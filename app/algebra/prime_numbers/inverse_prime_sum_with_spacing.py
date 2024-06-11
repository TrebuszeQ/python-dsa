import app.utils.input_readers as input_readers
from app.algebra.prime_numbers.eratosthenes_sieve import EratosthenesSieve


def sum_inverted_primes_with_spacing():
    increment = _read_spacing()
    end = _read_upper_limit()
    sieve = EratosthenesSieve(end)
    primes = sieve.find_primes()
    sigma = _sum_inverse_primes(primes, increment)
    return sigma


def _read_spacing():
    value = 0
    allowed = [2, 3, 4, 5, 6, 7, 10, 20, 50, 100, 1000, 5000, 10000]
    while value not in allowed:
        value = input_readers.try_read_input_int("Insert one of the following incremental values: [2, 3, 4, 5, 6, 7, 10, 20, 50, 100, 1000, 5000, 10000]")

    return value


def _read_upper_limit():
    value = 0
    allowed = [50, 1000000, 10000000, 50000000]
    while value not in allowed:
        value = input_readers.try_read_input_int("Choose upper limit from: [1m, 10m, 50m].")

    return value


def _print_sum_of_opposites(s, upper_lim):
    print(f"Sum of opposites of prime numbers per increment of {s} to {upper_lim}")


def _sum_inverse_primes(primes, increment):
    sigma = 0
    for i in range(0, len(primes), increment):
        prime = primes[i]
        inverse_prime = 1.0/prime
        sigma += inverse_prime

    return sigma
