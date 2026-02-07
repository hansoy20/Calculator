import threading

def compute_gwa(grades, thread_id):
    """Calculate GWA for a subset of grades"""
    gwa = sum(grades) / len(grades)
    print(f"[Thread {thread_id}] Calculated GWA: {gwa:.2f} from grades: {grades}")

def compute_overall_gwa(grades):
    """Calculate overall GWA using shared data and lock"""
    overall_gwa = sum(grades) / len(grades)
    return overall_gwa

print("Enter grades (separate with spaces):")
user_input = input()
grades_list = [float(x) for x in user_input.split()]

print("\n--- Individual Grade Processing ---")
threads = []
for i, grade in enumerate(grades_list):
    t = threading.Thread(target=compute_gwa, args=([grade], i+1))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("\n--- Overall GWA Calculation ---")
result = []
lock = threading.Lock()

def compute_and_store(grades, result_list, lock):
    """Compute GWA and store in shared list"""
    gwa = sum(grades) / len(grades)
    with lock:
        result_list.append(gwa)
        print(f"[Thread] Overall GWA: {gwa:.2f}")

overall_thread = threading.Thread(target=compute_and_store, args=(grades_list, result, lock))
overall_thread.start()
overall_thread.join()

print(f"\nFinal GWA: {result[0]:.2f}")
