import time


def wash(car): 
    time.sleep(2)  
    print(f"{car} washed")

def rinse(car): 
    time.sleep(1)  
    print(f"{car} rinsed")

def dry(car): 
    time.sleep(1.5)  # Simulates drying
    print(f"{car} dried")

def interior_clean(car): 
    time.sleep(2)  # Simulates interior cleaning
    print(f"{car} interior cleaned")

# Sequential processing of cars
def sequential_cars(cars):
    start = time.time()
    for car in cars:
        wash(car)
        rinse(car)
        dry(car)
        interior_clean(car)
    end = time.time()
    return end - start

# List of cars
cars = ['Car1', 'Car2', 'Car3']
seq_time = sequential_cars(cars)
print("Sequential time:", seq_time)