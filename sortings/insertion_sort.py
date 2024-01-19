class InsertionSort:
    @staticmethod
    def insertion_sort(arr):

        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i] < arr[i-1]:
                    arr[i], arr[i-1] = arr[i-1], arr[i]
