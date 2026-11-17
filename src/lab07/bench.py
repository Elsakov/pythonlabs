import csv
import timeit
import random
from pathlib import Path
from src.lab07.sorting import (
    bubble_sort, insertion_sort, selection_sort, merge_sort,
)
from src.lab07.search import (
    linear_search, binary_search, two_sum_brute, two_sum_fast,
)


def generate_data(size):
    return [random.randint(0, 100_000) for _ in range(size)]


def bench_sorts(size, timeout=60.0):
    numbers = generate_data(size)
    results = []

    elapsed_time = timeit.timeit(lambda: sorted(numbers), number=1)
    results.append(("sort", size, "sorted", f"{elapsed_time:.4f}"))

    for sorting_function in (bubble_sort, insertion_sort, selection_sort):
        try:
            elapsed_time = timeit.timeit(
                lambda: sorting_function(numbers), number=1
            )
            if elapsed_time > timeout:
                elapsed_text = f">{timeout:.0f} с"
            else:
                elapsed_text = f"{elapsed_time:.4f}"
            results.append(
                ("sort", size, sorting_function.__name__, elapsed_text)
            )
        except Exception:
            results.append(
                ("sort", size, sorting_function.__name__, "ошибка")
            )

    elapsed_time = timeit.timeit(lambda: merge_sort(numbers), number=1)
    results.append(("sort", size, "merge_sort", f"{elapsed_time:.4f}"))

    return results


def bench_search():
    numbers = generate_data(100_000)
    ordered_numbers = sorted(numbers)
    queries = [random.randint(0, 100_000) for _ in range(10_000)]
    results = []

    elapsed_time = timeit.timeit(
        lambda: [linear_search(numbers, query) for query in queries],
        number=1,
    )
    results.append(
        ("search", 100_000, "linear_search", f"{elapsed_time:.4f}")
    )

    elapsed_time = timeit.timeit(
        lambda: [binary_search(ordered_numbers, query) for query in queries],
        number=1,
    )
    results.append(
        ("search", 100_000, "binary_search", f"{elapsed_time:.4f}")
    )

    elapsed_time = timeit.timeit(lambda: sorted(numbers), number=1)
    results.append(
        ("search", 100_000, "sort_for_binary", f"{elapsed_time:.4f}")
    )

    return results


def bench_two_sum():
    results = []
    for size in (1_000, 10_000):
        numbers = generate_data(size)
        target = numbers[0] + numbers[-1]

        elapsed_time = timeit.timeit(
            lambda: two_sum_brute(numbers, target), number=1
        )
        results.append(
            ("two_sum", size, "two_sum_brute", f"{elapsed_time:.4f}")
        )

        elapsed_time = timeit.timeit(
            lambda: two_sum_fast(numbers, target), number=1
        )
        results.append(
            ("two_sum", size, "two_sum_fast", f"{elapsed_time:.4f}")
        )

    return results


def print_table(results):
    print(f"{'task':<10} {'n':>8} {'impl':<20} {'seconds':>10}")
    print("-" * 52)
    for task, size, implementation, elapsed_text in results:
        print(
            f"{task:<10} {size:>8} {implementation:<20} {elapsed_text:>10}"
        )


def main():
    random.seed(42)

    all_results = []
    for size in (1_000, 10_000, 100_000):
        all_results.extend(bench_sorts(size))
    all_results.extend(bench_search())
    all_results.extend(bench_two_sum())

    print_table(all_results)

    Path("data/lab07").mkdir(parents=True, exist_ok=True)
    with open("data/lab07/bench.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(("task", "n", "impl", "seconds"))
        writer.writerows(all_results)

    print("\nРезультаты сохранены в data/lab07/bench.csv")


if __name__ == "__main__":
    main()