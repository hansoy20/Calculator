import time
import random

small_data = [random.randint(1, 1000000) for _ in range(1000)]
medium_data = [random.randint(1, 1000000) for _ in range(100000)]
large_data = [random.randint(1, 1000000) for _ in range(1000000)]

reverse_sorted = list(range(1000, 0, -1))

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def run_test(label, dataset):
    start = time.time()
    sorted_data = merge_sort(dataset)
    end = time.time()
    print(f"{label}: {end - start:.4f} seconds")
    return sorted_data

print("=== Sequential Merge Sort ===")
run_test("Small (1,000)", small_data)
run_test("Medium (100,000)", medium_data)
run_test("Large (1,000,000)", large_data)
run_test("Reverse Sorted (1,000)", reverse_sorted)