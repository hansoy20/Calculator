import threading
import time

# Shared data and lock for thread safety
total_sum = 0
grade_count = 0
lock = threading.Lock()

def compute_partial_sum(grades, thread_id):
    """Calculate partial sum of grades in a thread"""
    global total_sum, grade_count
    
    partial_sum = sum(grades)
    count = len(grades)

    time.sleep(0.1)

    with lock:
        total_sum += partial_sum
        grade_count += count
        print(f"[Thread {thread_id}] Processed {count} grade(s): {grades} | Partial sum: {partial_sum}")

def validate_grade(grade):
    """Validate if grade is within acceptable range"""
    try:
        grade = float(grade)
        if 0 <= grade <= 100:
            return grade
        else:
            print(f"Warning: Grade {grade} is out of range (0-100). Skipping.")
            return None
    except ValueError:
        print(f"Error: '{grade}' is not a valid number. Skipping.")
        return None

def main():
    global total_sum, grade_count
    
    print("=" * 50)
    print("   MULTITHREADED GWA CALCULATOR")
    print("=" * 50)
    
    # Get user input
    print("\nEnter grades separated by spaces (0-100):")
    user_input = input("> ")
    
    # Validate and filter grades
    raw_grades = user_input.split()
    grades_list = [g for g in (validate_grade(grade) for grade in raw_grades) if g is not None]
    
    if not grades_list:
        print("\nError: No valid grades entered!")
        return
    
    print(f"\nValid grades: {grades_list}")
    print(f"Total grades to process: {len(grades_list)}\n")

    total_sum = 0
    grade_count = 0

    num_threads = min(4, len(grades_list))
    chunk_size = len(grades_list) // num_threads
    
    print(f"Using {num_threads} thread(s) for processing...\n")

    threads = []
    start_time = time.time()
    
    for i in range(num_threads):

        start_idx = i * chunk_size
        if i == num_threads - 1:

            end_idx = len(grades_list)
        else:
            end_idx = start_idx + chunk_size
        
        grade_chunk = grades_list[start_idx:end_idx]

        t = threading.Thread(
            target=compute_partial_sum, 
            args=(grade_chunk, i + 1),
            name=f"Worker-{i+1}"
        )
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    
    end_time = time.time()

    print("\n" + "=" * 50)
    if grade_count > 0:
        gwa = total_sum / grade_count
        print(f"FINAL GWA: {gwa:.2f}")
        print(f"Total grades processed: {grade_count}")
        print(f"Processing time: {(end_time - start_time):.4f} seconds")
    else:
        print("No grades to calculate!")
    print("=" * 50)

if __name__ == "__main__":
    main()