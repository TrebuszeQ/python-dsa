from dataclasses import dataclass


@dataclass(repr=True)
class HardcodedOta:

    @property
    def c(self):
        return self._c

    @property
    def value(self):
        return self._value

    def __init__(self, arr: list[int]):
        self._c = [int] * len(arr)
        self.__set_c(arr)
        c = self._c

    # in place
    def __set_c(self, arr: list[int]):
        for i in range(len(arr)):
            num = arr[i]
            val = num if i == 0.0 else (num - arr[i - 1]) * 1.0
            self._c.append(val)

    def __set_value(self, arr: list[int]):
        c = self._c
        to_bin = self.__to_bin
        s = 0
        for num in arr:
            num_bin = to_bin(num)

            s += c[0] + c[1] * to_bin(arr[0]) + (c[1] + c[2]) * arr[1] + (c[3] - c[1]) * arr[1] * arr[0] + (
                c[1] + c[2] + c[3] + c[4]) * arr[2] + (c[5] - c[1]) * arr[2] * arr[0] + (c[6] + c[5] - c[2] - c[1]) \
                * arr[2] * arr[0] + (c[6] + c[5] - c[2] - c[1]) * arr[2] * arr[1] + (c[7] - c[5] - c[3] + c[1]) * \
                arr[2] * arr[1] * arr[0]

    def __to_bin(self, num: int):
        return bin(num)[2:]
