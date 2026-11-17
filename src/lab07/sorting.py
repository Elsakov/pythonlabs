def bubble_sort(values):
    result = list(values)
    length = len(result)
    for pass_index in range(length):
        has_swapped = False
        for compare_index in range(0, length - pass_index - 1):
            if result[compare_index] > result[compare_index + 1]:
                result[compare_index], result[compare_index + 1] = (
                    result[compare_index + 1],
                    result[compare_index],
                )
                has_swapped = True
        if not has_swapped:
            break
    return result


def insertion_sort(values):
    result = list(values)
    for current_index in range(1, len(result)):
        current_value = result[current_index]
        scan_index = current_index - 1
        while scan_index >= 0 and result[scan_index] > current_value:
            result[scan_index + 1] = result[scan_index]
            scan_index -= 1
        result[scan_index + 1] = current_value
    return result


def selection_sort(values):
    result = list(values)
    length = len(result)
    for position in range(length):
        min_index = position
        for scan_index in range(position + 1, length):
            if result[scan_index] < result[min_index]:
                min_index = scan_index
        result[position], result[min_index] = result[min_index], result[position]
    return result


def merge_sort(values):
    result = list(values)
    length = len(result)
    block_size = 1
    while block_size < length:
        for block_start in range(0, length, 2 * block_size):
            left_part = result[block_start:block_start + block_size]
            right_part = result[
                block_start + block_size:block_start + 2 * block_size
            ]
            merged = []
            left_index = 0
            right_index = 0
            while left_index < len(left_part) and right_index < len(right_part):
                if left_part[left_index] <= right_part[right_index]:
                    merged.append(left_part[left_index])
                    left_index += 1
                else:
                    merged.append(right_part[right_index])
                    right_index += 1
            merged.extend(left_part[left_index:])
            merged.extend(right_part[right_index:])
            result[block_start:block_start + 2 * block_size] = merged
        block_size *= 2
    return result


def counting_sort(values, minimum, maximum):
    counters = [0] * (maximum - minimum + 1)
    for value in values:
        counters[value - minimum] += 1
    result = []
    for current_value, amount in enumerate(counters, start=minimum):
        result.extend([current_value] * amount)
    return result