from dataclasses import dataclass


@dataclass(repr=True)
class OtaN7:

    @property
    def _degree(self):
        return self.__degree

    @property
    def points_arr(self):
        return self._points_arr

    def __init__(self, arr: list[int]):
        self._points_arr = None
        self.__degree = len(bin(len(arr)))
        self._points_arr =

    def __make_c_arr(self, arr: list[int]):
        c_arr = [int] * self.__degree

        for i in range(len(arr)):
            num = arr[i]
            val = num if i == 0.0 else (num - arr[i - 1]) * 1
            c_arr.append(val)

        return c_arr

    def __make_points_arr(self):
        def points_arr(self, arr: list[int]):
            c = self.__make_c_arr(arr)
            self._points_arr = [[int][int]] * self.__degree

            for i in range(self._degree):
                num = arr[i]
                a = self.__make_bin_arr(num)
                self._points_arr[i][0] = i
                self._points_arr[i][1] = c[0] + c[1] * a[0] + (c[1] + c[2]) * a[1] + (c[3] - c[1]) * a[1] * a[0] + (
                        c[1] + c[2] + c[3] + c[4]) * a[2] + (c[5] - c[1]) * a[2] * a[0] + (c[6] + c[5] - c[2] - c[1]) \
                                      * a[2] * a[0] + (c[6] + c[5] - c[2] - c[1]) * a[2] * a[1] + (
                                                  c[7] - c[5] - c[3] + c[1]) * \
                                      a[2] * a[1] * a[0]

    def __make_bin_arr(self, num):
        bit = self.__to_bin(num)
        return [int(bit[i]) for i in range(len(bit))]

    def __to_bin(self, num: int):
        return format(num, f"0{self.__degree}b")
