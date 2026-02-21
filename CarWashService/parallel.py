from concurrent.futures import ThreadPoolExecutor
import time

# Define tasks
def wash(car): 
    time.sleep(2)
    print(f"{car} washed")

def rinse(car): 
    time.sleep(1)
    print(f"{car} rinsed")

def dry(car): 
    time.sleep(1.5)
    print(f"{car} dried")

def interior_clean(car): 
    time.sleep(2)
    print(f"{car} interior cleaned")

# Function to process one car through all stages
def process_car(car):
    wash(car)
    rinse(car)
    dry(car)
    interior_clean(car)

# List of cars
cars = ['Car1', 'Car2', 'Car3']

# Parallel processing
start = time.time()
with ThreadPoolExecutor(max_workers=4) as executor:  # 4 workers = 4 stages
    executor.map(process_car, cars)
end = time.time()

parallel_time = end - start
print("Parallel time:", parallel_time)
print("Speedup:", round(seq_time / parallel_time, 2))