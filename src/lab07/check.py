import random
from src.lab07.sorting import (
    bubble_sort, insertion_sort, selection_sort, merge_sort,
)
from src.lab07.search import (
    linear_search, binary_search, two_sum_brute, two_sum_fast,
)


def check_sorting(sorting_function, attempts=100):
    for attempt_number in range(attempts):
        length = random.randint(0, 50)
        values = [random.randint(-100, 100) for _ in range(length)]
        original = list(values)
        result = sorting_function(values)
        assert result == sorted(values), (
            f"{sorting_function.__name__} ошиблась на {values}: {result}"
        )
        assert values == original, (
            f"{sorting_function.__name__} изменила исходный список"
        )


def check_search():
    for attempt_number in range(100):
        length = random.randint(0, 50)
        values = [random.randint(-100, 100) for _ in range(length)]
        target = random.randint(-100, 100)

        try:
            expected_result = values.index(target)
        except ValueError:
            expected_result = -1
        actual_result = linear_search(values, target)
        assert actual_result == expected_result, (
            f"linear_search({values}, {target}) = {actual_result}, "
            f"ожидалось {expected_result}"
        )

        ordered_values = sorted(values)
        try:
            expected_result = ordered_values.index(target)
        except ValueError:
            expected_result = -1
        actual_result = binary_search(ordered_values, target)
        assert actual_result == expected_result, (
            f"binary_search({ordered_values}, {target}) = {actual_result}, "
            f"ожидалось {expected_result}"
        )


def check_two_sum(attempts=100):
    for attempt_number in range(attempts):
        length = random.randint(0, 30)
        values = [random.randint(-50, 50) for _ in range(length)]
        target = random.randint(-100, 100)
        brute_result = two_sum_brute(values, target)
        fast_result = two_sum_fast(values, target)

        if brute_result is None:
            assert fast_result is None, (
                f"two_sum_fast нашёл {fast_result}, brute — None на {values}, "
                f"target={target}"
            )
        else:
            first_index, second_index = brute_result
            assert values[first_index] + values[second_index] == target
            if fast_result is not None:
                fast_first, fast_second = fast_result
                assert values[fast_first] + values[fast_second] == target, (
                    f"two_sum_fast вернул неверную пару {fast_result} "
                    f"на {values}, target={target}"
                )


if __name__ == "__main__":
    random.seed(42)
    for sorting_function in (
        bubble_sort, insertion_sort, selection_sort, merge_sort,
    ):
        check_sorting(sorting_function)
    check_search()
    check_two_sum()
    print("OK: все проверки пройдены")