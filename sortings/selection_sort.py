

class SelectionSort:

    # funkcja sortujaca
    @staticmethod
    def sort(arr):
        if len(arr) > 0:

            for i in range(len(arr)):
                pos = i
                min = arr[i]
                j = i

                while j < len(arr):
                    if arr[j] < min:
                        min = arr[j]
                        pos = j

                    j += 1

                arr[i], arr[pos] = arr[pos], arr[i]

        print(arr)
        return arr
