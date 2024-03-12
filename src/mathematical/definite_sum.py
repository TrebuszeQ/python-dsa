from dataclasses import dataclass


@dataclass(repr=True)
class DefiniteSum:
    @classmethod
    def definite_sum(cls, num):
        s = 0
        i = 1

        for i in range(num - 1):
            s += num

        return s