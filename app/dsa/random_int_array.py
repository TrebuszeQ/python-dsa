from random import randint
from dataclasses import dataclass


@dataclass(repr=True)
class RandomIntArray(list[int]):
    @staticmethod
    def gen_1d_arr(n, min_seed, max_seed):
        res = [randint(min_seed, max_seed) for i in range(n)]
        return res


def gen_1d_random_int_array(n, min_seed, max_seed):
    return [randint(min_seed, max_seed) for i in range(n)]
