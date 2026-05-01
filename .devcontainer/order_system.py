from __future__ import annotations

from mpi4py import MPI
import time
import random
from typing import Any, Optional

comm = MPI.COMM_WORLD
rank: int = comm.Get_rank()
size: int = comm.Get_size()

# Ensure we have at least 2 processes (1 master + 1 worker)
if size < 2:
    if rank == 0:
        print("Error: This program requires at least 2 MPI processes (1 master + 1 worker)")
        print("Usage: mpirun -np <n> python order_system.py  (where n >= 2)")
    exit(1)

if rank == 0:
    # Master process
    orders: list[dict[str, Any]] = [
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
        worker_rank: int = (i % (size - 1)) + 1
        comm.send(order, dest=worker_rank, tag=i)
        print(f"Master --> Sent Order {order['id']} ({order['item']}) to Worker {worker_rank}")

    # Send stop signal
    for worker in range(1, size):
        comm.send(None, dest=worker, tag=99)

    # Collect results from workers
    completed_orders: list[str] = []
    for worker in range(1, size):
        result: Optional[list[str]] = comm.recv(source=worker)
        if result is not None:
            completed_orders.extend(result)

    # Wait for all workers
    comm.Barrier()

    # Final output
    print("\n=== Final Completed Orders (Synchronized) ===")
    for completed in completed_orders:
        print(completed)
    print(f"\nTotal orders processed: {len(completed_orders)}")

else:
    # Worker processes
    processed_results: list[str] = []
    
    while True:
        data: Optional[Any] = comm.recv(source=0, tag=MPI.ANY_TAG)

        if data is None:
            break

        order: dict[str, Any] = data

        # Simulate processing delay
        delay: float = random.uniform(0.5, 2.0)
        print(f"  Worker {rank} processing Order {order['id']} ({order['item']})... ({delay:.1f}s)")
        time.sleep(delay)

        result: str = f"Order {order['id']} ({order['item']}) -- processed by Worker {rank}"
        processed_results.append(result)
        print(f"  Worker {rank} completed: {result}")

    # Send results back to master
    comm.send(processed_results, dest=0)

    comm.Barrier()