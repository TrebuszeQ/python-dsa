class InsertionSort:
    @staticmethod
    def sort(arr):

        for i in range(len(arr)):
            j = i - 1

            while j >= 0:
                # debugging purpose
                # lol = arr[j+1]
                # lol2 = arr[j]
                if arr[j+1] < arr[j]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                j -= 1

        print(arr)
        return arr
