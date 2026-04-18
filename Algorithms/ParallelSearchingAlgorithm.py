import time
import random
from multiprocessing import Process, Queue

small_data = [random.randint(1, 1000000) for _ in range(1000)]
medium_data = [random.randint(1, 1000000) for _ in range(100000)]
large_data = [random.randint(1, 1000000) for _ in range(1000000)]

reverse_sorted = list(range(1000, 0, -1))

def worker(sub_data, target, q, offset):
    for i in range(len(sub_data)):
        if sub_data[i] == target:
            q.put(offset + i)
            return
    q.put(-1)

def parallel_search(data, target):
    chunk_size = len(data) // 4
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    q = Queue()
    processes = []

    for i, chunk in enumerate(chunks):
        offset = i * chunk_size
        p = Process(target=worker, args=(chunk, target, q, offset))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    results = [q.get() for _ in processes]
    found = [r for r in results if r != -1]

    if found:
        return min(found)
    return -1

def run_test(label, dataset, target):
    start = time.time()
    result = parallel_search(dataset, target)
    end = time.time()
    if result != -1:
        print(f"{label}: Found {target} at index {result} | Time: {end - start:.4f} seconds")
    else:
        print(f"{label}: {target} not found | Time: {end - start:.4f} seconds")

if __name__ == "__main__":
    target = random.randint(1, 1000000)
    print("=== Parallel Linear Search ===")
    print(f"Searching for: {target}")
    run_test("Small (1,000)", small_data, target)
    run_test("Medium (100,000)", medium_data, target)
    run_test("Large (1,000,000)", large_data, target)
    run_test("Reverse Sorted (1,000)", reverse_sorted, target)