class SelectionSort:

    # funkcja sortujaca
    @staticmethod
    def sort(arr):
        for i in range(0, len(arr)):
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

    @staticmethod
    def sort2(arr):

        for i in range(1, len(arr) - 1):
            mini = i

            for j in range(i, len(arr)):
                if arr[mini] > arr[j]:
                    mini = j

            arr[i], arr[mini] = arr[mini], arr[i]

        return arr

    @staticmethod
    def sort2_count(arr):
        comp_count = 0
        swap_count = 0

        for i in range(1, len(arr) - 1):
            mini = i

            for j in range(i, len(arr)):
                comp_count += 1
                if arr[mini] > arr[j]:
                    mini = j

            arr[i], arr[mini] = arr[mini], arr[i]
            swap_count += 1

        print(arr)
        return arr, comp_count, swap_count
