import time
import random

# Generate datasets
small_data = [random.randint(1, 1000000) for _ in range(1000)]
medium_data = [random.randint(1, 1000000) for _ in range(100000)]
large_data = [random.randint(1, 1000000) for _ in range(1000000)]

# Special case: already sorted and reverse sorted
already_sorted = list(range(1, 1001))
reverse_sorted = list(range(1000, 0, -1))


def insertion_sort(arr):
    data = arr.copy()
    for i in range(1, len(data)):
        current = data[i]
        j = i - 1
        while j >= 0 and data[j] > current:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = current
    return data


def run_test(label, dataset):
    start = time.time()
    sorted_data = insertion_sort(dataset)
    end = time.time()
    print(f"{label}: {end - start:.4f} seconds")
    return sorted_data


run_test("Small (1,000)", small_data)
run_test("Medium (100,000)", medium_data)
run_test("Reverse Sorted (1,000)", reverse_sorted)
run_test("Large (1,000,000)", large_data)