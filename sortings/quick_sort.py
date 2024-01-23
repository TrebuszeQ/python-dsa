

class QuickSort:
    @staticmethod
    def _pick_pivot_last(arr):
        return arr[arr.__len__() - 1]

    @staticmethod
    def _sort(arr, i):

        if arr[i + 1] is not None and arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            i += 1
            return QuickSort._sort(arr, i)

        elif arr[i + 1] is None:
            return arr

    @staticmethod
    def sort(arr):
        res = QuickSort._partition(QuickSort._pick_pivot_last(arr), arr)
        res[0].extend(res[1])
        print(res[0])
        return res[0]

    @staticmethod
    def _partition(pivot, arr):
        res = [[], []]

        i = 0
        while i < len(arr):
            if arr[i] >= pivot:
                res[1].append(arr[i])
            else:
                res[0].append(arr[i])
            i += 1

        return res
