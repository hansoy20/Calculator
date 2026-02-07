1. Which approach demonstrates true parallelism in Python? Explain.

Multiprocessing demonstrates true parallelism in Python. Each process runs in its own memory space and has its own Python interpreter. This allows multiple CPU cores to execute tasks at the same time. In contrast, threads share the same memory and are limited by the Global Interpreter Lock (GIL).

2. Compare execution times between multithreading and multiprocessing.

For small and simple tasks, multithreading may appear faster because creating threads has lower overhead. However, for CPU-intensive tasks, multiprocessing is usually faster since it utilizes multiple CPU cores. In our experiment, execution time depended on the workload and the number of inputs.


3. Can Python handle true parallelism using threads? Why or why not?

No, Python cannot achieve true parallelism using threads for CPU-bound tasks. This is because of the Global Interpreter Lock (GIL), which allows only one thread to execute Python bytecode at a time. As a result, threads are more suitable for I/O-bound tasks rather than CPU-heavy computations.

4. What happens if you input a large number of grades (e.g., 1000)? Which method is faster and why?

If a large number of grades is entered, multiprocessing is generally faster for CPU-bound computations because it distributes the workload across multiple CPU cores. Multithreading may not significantly improve performance due to the GIL. However, multiprocessing may also introduce additional overhead from creating many processes.

5. Which method is better for CPU-bound tasks and which for I/O-bound tasks?

Multiprocessing is better for CPU-bound tasks because it allows true parallel execution.
Multithreading is better for I/O-bound tasks, such as reading files or waiting for network responses, because threads can run while others are waiting for I/O operations.

6. How did your group apply creative coding or algorithmic solutions in this lab?

Our group improved the provided code by adding dynamic user input, structured functions, and execution time measurement. We ensured that results were stored safely and displayed clearly. We also analyzed performance differences between both methods and organized the code to make it more readable and efficient.
