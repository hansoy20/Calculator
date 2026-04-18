import time
import random

small_data = [random.randint(1, 1000000) for _ in range(1000)]
medium_data = [random.randint(1, 1000000) for _ in range(100000)]
large_data = [random.randint(1, 1000000) for _ in range(1000000)]

reverse_sorted = list(range(1000, 0, -1))

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def run_test(label, dataset, target):
    start = time.time()
    result = linear_search(dataset, target)
    end = time.time()
    if result != -1:
        print(f"{label}: Found {target} at index {result} | Time: {end - start:.4f} seconds")
    else:
        print(f"{label}: {target} not found | Time: {end - start:.4f} seconds")

if __name__ == "__main__":
    target = random.randint(1, 1000000)
    print(f"Searching for: {target}")
    run_test("Small (1,000)", small_data, target)
    run_test("Medium (100,000)", medium_data, target)
    run_test("Large (1,000,000)", large_data, target)
    run_test("Reverse Sorted (1,000)", reverse_sorted, target)