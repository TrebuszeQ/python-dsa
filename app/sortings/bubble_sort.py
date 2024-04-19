
class BubbleSort:
    # worst case O(N^2), in place, stable
    @staticmethod
    def sort(arr):
        for i in range(len(arr)):

            j = i + 1
            for j in range(0, len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        print(arr)
        return arr

    @staticmethod
    def sort_down_to_count(arr):
        comp_count = 0
        swap_count = 0

        for i in range(1, len(arr) - 1):
            for j in range(len(arr) - 1, i, -1):
                comp_count += 1

                if arr[j - 1] > arr[j]:
                    arr[j - 1], arr[j] = arr[j], arr[j - 1]
                    swap_count += 1

        print(arr)
        return arr, comp_count, swap_count

    # deliberately i = 1
    @staticmethod
    def sort_count(arr):
        comp_count = 0
        swap_count = 0

        i = 1
        for i in range(len(arr) - 1):
            comp_count += 1

            j = i + 1
            for j in range(0, len(arr) - i - 1):
                comp_count += 1

                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swap_count += 1

        print(arr)
        return arr, comp_count, swap_count
