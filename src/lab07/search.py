def linear_search(values, target):
    for position, value in enumerate(values):
        if value == target:
            return position
    return -1


def binary_search(ordered_values, target):
    left = 0
    right = len(ordered_values) - 1
    while left <= right:
        middle = (left + right) // 2
        if ordered_values[middle] == target:
            return middle
        if ordered_values[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1


def two_sum_brute(values, target):
    length = len(values)
    for first_index in range(length):
        for second_index in range(first_index + 1, length):
            if values[first_index] + values[second_index] == target:
                return (first_index, second_index)
    return None


def two_sum_fast(values, target):
    seen = {}
    for position, value in enumerate(values):
        needed = target - value
        if needed in seen:
            return (seen[needed], position)
        seen[value] = position
    return None