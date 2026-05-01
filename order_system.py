from mpi4py import MPI
from multiprocessing import Manager
import time
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if size < 2:
    if rank == 0:
        print("Error: Requires at least 2 MPI processes")
        print("Usage: mpirun --oversubscribe -np 4 python order_system.py")
    exit(1)

if rank == 0:
    # Master process
    manager = Manager()
    shared_orders = manager.list()
    lock = manager.Lock()

    orders = [
        {"id": 1, "item": "Laptop"},
        {"id": 2, "item": "Phone"},
        {"id": 3, "item": "Tablet"},
        {"id": 4, "item": "Monitor"},
        {"id": 5, "item": "Keyboard"},
        {"id": 6, "item": "Mouse"},
    ]

    print(f"\nMaster: Generated {len(orders)} orders")
    print("Master: Distributing orders to workers...\n")

    # Send orders to workers
    for i, order in enumerate(orders):
        worker_rank = (i % (size - 1)) + 1
        comm.send(order, dest=worker_rank, tag=i)
        print(f"Master --> Sent Order {order['id']} ({order['item']}) to Worker {worker_rank}")

    # Send stop signal to all workers
    for worker in range(1, size):
        comm.send(None, dest=worker, tag=99)

    # Collect results from workers via MPI
    all_results = []
    for worker in range(1, size):
        worker_results = comm.recv(source=worker)
        if worker_results:
            all_results.extend(worker_results)

    # Store in shared memory using Lock
    print("\nMaster: Storing results in shared memory...\n")
    for result in all_results:
        with lock:
            shared_orders.append(result)
            print(f"  [LOCKED] Master stored: {result}")

    comm.Barrier()

    # Final output
    print("\n=== Final Completed Orders (Synchronized) ===")
    for completed in shared_orders:
        print(completed)
    print(f"\nTotal orders processed: {len(shared_orders)}")

else:
    # Worker processes
    processed = []

    while True:
        data = comm.recv(source=0, tag=MPI.ANY_TAG)

        if data is None:
            break

        order = data

        # Simulate processing delay
        delay = random.uniform(0.5, 2.0)
        print(f"  Worker {rank} processing Order {order['id']} ({order['item']})... ({delay:.1f}s)")
        time.sleep(delay)

        result = f"Order {order['id']} ({order['item']}) -- processed by Worker {rank}"
        processed.append(result)
        print(f"  Worker {rank} completed: {result}")

    # Send all results back to master
    comm.send(processed, dest=0)
    comm.Barrier()