1. Differentiate Task and Data Parallelism
Task Parallelism occurs when different, distinct operations are executed concurrently, often on the same data . This is demonstrated in Part A, where different deduction functions (SSS, Tax, etc.) are performed on a single employee's salary .

Data Parallelism occurs when the same operation is applied to multiple different data elements simultaneously. This is demonstrated in Part B, where one payroll function is applied to the entire list of five employees.

Justification: Task parallelism is used when the workload consists of independent sub-tasks for a single entity, while data parallelism is used to distribute a repetitive workload across a large dataset.


2. concurrent.futures Managed Execution
submit(): This method schedules a single callable (function) to be executed and immediately returns a Future object.

map(): This method is used to apply a specific function to every item in an iterable (like a list) in parallel, returning the results in order.

Future objects: These represent a "promise" of a result that may not be completed yet; they allow the program to check the status or retrieve the result once the task finishes.

Purpose of with: Using a context manager (with) ensures that the Executor automatically shuts down and waits for all pending tasks to complete before moving forward, preventing resource leaks.

3. ThreadPoolExecutor, GIL, and CPU Cores
Analysis: In Python, the Global Interpreter Lock (GIL) prevents multiple native threads from executing Python bytecodes at once.

True Parallelism?: No, true parallelism did not occur in the ThreadPoolExecutor. Because the payroll tasks are CPU-bound, the GIL forced the threads to take turns on a single CPU core rather than running simultaneously on multiple cores.

4. ProcessPoolExecutor and True Parallelism
True Parallelism: ProcessPoolExecutor achieves true parallelism because it creates entirely separate memory spaces for each task.

GIL Behavior: Each process has its own Python interpreter and its own GIL; therefore, multiple processes can run on multiple CPU cores at the exact same time without interfering with each other.

5. Scalability (5 to 10,000 Employees)
Better Approach: Data Parallelism using ProcessPoolExecutor scales significantly better for 10,000 employees.

Why: While threads have less "overhead," they are bottlenecked by the GIL. Processes can distribute the massive workload across all available physical CPU cores, making them much more efficient for large-scale data processing.


6. Real-World Payroll Example
Task Parallelism: Within a single paycheck calculation, you could concurrently calculate different complex benefits (e.g., healthcare, stock options, and retirement contributions) using a ThreadPoolExecutor.

Data Parallelism: When generating monthly paychecks for a global company with 100,000 employees, you would use a ProcessPoolExecutor to process thousands of employees at once across server clusters