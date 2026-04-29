from mpi4py import MPI
from multiprocessing import Manager
import time
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    # Initialize shared memory
    manager = Manager()
    shared_orders = manager.list()

    orders = [
        {"id": i, "item": item}
        for i, item in enumerate(
            ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard", "Mouse"], start=1
        )
    ]

    # Send orders to workers
    for i, order in enumerate(orders):
        worker_rank = (i % (size - 1)) + 1
        comm.send((order, shared_orders), dest=worker_rank, tag=i)
        print(f"Master sent Order {order['id']} to Worker {worker_rank}")

    # Send stop signal
    for worker in range(1, size):
        comm.send((None, None), dest=worker, tag=99)

    # Wait and collect results
    comm.Barrier()
    print("\n=== Completed Orders ===")
    for o in shared_orders:
        print(o)

else:
    while True:
        data = comm.recv(source=0)
        order, shared_orders = data
        if order is None:
            break

        delay = random.uniform(0.5, 2.0)
        time.sleep(delay)  # Simulate processing time

        result = f"Order {order['id']} ({order['item']}) processed by Worker {rank}"
        shared_orders.append(result)
        print(result)

    comm.Barrier()