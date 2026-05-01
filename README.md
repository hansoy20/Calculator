# Distributed Order Processing — PDC Lab 1

## Members
- Member 1: [Hans Aldrich Saguilayan] — Environment Setup
- Member 2: [Keith Austria] — Task Distribution
- Member 3: [Gian Paolo Oga] — Shared Memory & Delays
- Member 4: [Seth Palgan] — Synchronization & Documentation

## How to Run
```bash
mpirun -np 4 python order_system.py
```

## Reflection Questions

**1. How did you distribute orders among worker processes?
We used a round-robin method. The main process (rank 0) sends each order to workers one by one in a repeating pattern, so the tasks are shared evenly among all workers.

**2. What happens if there are more orders than workers?
If there are more orders than workers, some workers will handle multiple orders. The system just loops back and continues assigning new orders to the first workers again, so everything still gets processed.

**3. How did processing delays affect the order completion?
Each worker had a random delay using time.sleep(), so orders didn’t finish in the same order they were assigned. Some workers finished faster than others, making the completion order unpredictable.

**4. How did you implement shared memory, and where was it initialized?
We used Manager().list() from Python’s multiprocessing module to create shared memory. It was set up in the main process (rank 0) and then shared with the workers so they could all access the same list.

**5. What issues occurred when multiple workers wrote to shared memory simultaneously?
When several workers tried to write at the same time, it caused problems like mixed or incomplete data. This is called a race condition.

**6. How did you ensure consistent results when using multiple processes?
We used a lock (manager.Lock()) to control access. A worker must get the lock before writing to the shared list and release it after. This makes sure only one worker writes at a time, keeping the data correct.