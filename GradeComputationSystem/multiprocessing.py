import multiprocessing
import time

def compute_gwa(grades):
    """Calculates GWA. Pure function, easier to test and parallelize."""
    if not grades:
        return 0.0
    
    
    return sum(grades) / len(grades)

def main():
    print("=== Optimized Multiprocessing Grade System ===")
    user_input = input("Enter grades (separate with spaces): ")
    
    try:
        grades_list = [float(x) for x in user_input.split()]
        if not grades_list:
            raise ValueError("No grades entered.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    start_time = time.perf_counter()

    
    print("\n--- Processing Individual Grades ---")
    with multiprocessing.Pool() as pool:
        # We wrap each grade in a list because your original function expected a list
        results = pool.map(compute_gwa, [[g] for g in grades_list])
        
        for i, res in enumerate(results):
            print(f"[Process {i+1}] Grade Verified: {res:.2f}")

    
    print("\n--- Overall GWA Calculation ---")
    with multiprocessing.Pool(processes=1) as pool:
        async_result = pool.apply_async(compute_gwa, (grades_list,))
        final_gwa = async_result.get()

    end_time = time.perf_counter()
    
    print("-" * 30)
    print(f"Final GWA: {final_gwa:.2f}")
    print(f"Total Execution Time: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()