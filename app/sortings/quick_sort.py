

class QuickSort:

    @staticmethod
    def _sort(arr, low, high):

        if low < high:
            part = QuickSort._hoare_partition(arr, low, high)
            QuickSort._sort(arr, low, part - 1)
            QuickSort._sort(arr, part + 1, high)

        else:
            pass

        return arr

    @staticmethod
    def sort(arr, low, high):
        res = QuickSort._sort(arr, low, high)

        print(res)
        return res

    @staticmethod
    def _hoare_partition(arr, low, high):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        return i + 1
