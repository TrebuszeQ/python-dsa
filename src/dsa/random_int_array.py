from random import randint


class RandomIntArray:
    @staticmethod
    def gen_1d_arr(n):
        res = []
        for i in range(n):
            res.append(randint(0, 1000))

        # print(res)
        return res

