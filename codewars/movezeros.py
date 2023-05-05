def move_zeros(lst):
    non_zeros = []

    zeros = 0

    for elem in lst:
        if elem != 0 or elem is False:
            non_zeros.append(elem)
        else:
            zeros += 1

    non_zeros.extend([0] * zeros)

    return non_zeros