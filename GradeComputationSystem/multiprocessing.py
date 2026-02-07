import multiprocessing
import time

def compute_gwa_mp(grades, process_id):
    """Calculate GWA for a subset of grades using a separate Process"""
    gwa = sum(grades) / len(grades)
 
    time.sleep(0.1)
    print(f"[Process {process_id}] Calculated GWA: {gwa:.2f} from grades: {grades}")

def compute_overall_gwa_mp(grades, result_list):
    """Compute overall GWA and store in a shared list for processes"""
    gwa = sum(grades) / len(grades)
    result_list.append(gwa)
    print(f"\n[Process] Overall GWA Calculated: {gwa:.2f}")

if __name__ == "__main__":
   
    
    print("=== Multiprocessing Grade System ===")
    print("Enter grades (separate with spaces):")
    user_input = input()
    
    try:
        grades_list = [float(x) for x in user_input.split()]
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        exit()

    start_time = time.perf_counter()

    print("\n--- Individual Grade Processing (Processes) ---")
    processes = []
    for i, grade in enumerate(grades_list):
        
        p = multiprocessing.Process(target=compute_gwa_mp, args=([grade], i+1))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("\n--- Overall GWA Calculation (Processes) ---")
    
    
    with multiprocessing.Manager() as manager:
        shared_result = manager.list() 
        
        overall_p = multiprocessing.Process(
            target=compute_overall_gwa_mp, 
            args=(grades_list, shared_result)
        )
        
        overall_p.start()
        overall_p.join()

        end_time = time.perf_counter()
        
        if len(shared_result) > 0:
            print(f"Final GWA: {shared_result[0]:.2f}")
            print(f"Total Execution Time: {end_time - start_time:.4f} seconds")