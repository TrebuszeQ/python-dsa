

class QuickSort:
    @staticmethod
    def sort(arr, i, j):
        pivot = QuickSort._pick_pivot_last(arr)
        j = i - 1
        if arr[i] < pivot and arr[j] > arr[i]:


    @staticmethod
    def _pick_pivot_last(arr):
        return arr.__len__() - 1
