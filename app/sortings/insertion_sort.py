class InsertionSort:
    @staticmethod
    def sort(arr):

        for i in range(1, len(arr)):

            key = arr[i]
            j = i - 1

            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1

            arr[j + 1] = key

        print(arr)
        return arr

    @staticmethod
    def sort_count(arr):
        comp_count = 0
        swap_count = 0

        for i in range(2, len(arr) - 1):
            key = arr[i]
            arr[i] = key
            swap_count += 1

            j = i - 1
            comp_count += 1
            while key < arr[j]:
                arr[j + 1] = arr[j]
                swap_count += 1
                j = j - 1

            arr[j + 1] = key
            swap_count += 1

        print(arr)
        return arr, comp_count, swap_count

    @staticmethod
    def sort_flag_count(arr):
        comp_count = 0
        swap_count = 0

        for i in range(1, len(arr) - 1):
            flag = False

            j = i + 1
            comp_count += 2
            while flag is False or j >= 1:

                comp_count += 1
                if arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                    swap_count += 1

                else:
                    flag = True

                j -= 1

        print(arr)
        return arr, comp_count, swap_count
