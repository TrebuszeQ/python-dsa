from app.discrete.ota import Ota


def algebraic_sort(ota: Ota):
    negated_arr = []
    for arr in ota.binary_array:
        subarray = []

        for bit in arr:
            if bit == 0:
                subarray.append(1)

            else:
                subarray.append(0)
        negated_arr.append(subarray)

    ota.binary_array = negated_arr
    ota.reset_points_arr()


