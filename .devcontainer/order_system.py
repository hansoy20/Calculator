from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    # Master generates 6 orders
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

    # Distribute orders to workers using round-robin
    for i, order in enumerate(orders):
        worker_rank = (i % (size - 1)) + 1  # Workers are ranks 1, 2, 3
        comm.send(order, dest=worker_rank, tag=i)
        print(f"Master > Sent Order {order['id']} ({order['item']}) to Worker {worker_rank}")

    # Send stop signal to all workers
    for worker in range(1, size):
        comm.send(None, dest=worker, tag=99)

    print("\nMaster: All orders distributed.")

else:
    # Workers receive orders from master
    while True:
        order = comm.recv(source=0)
        if order is None:
            break
        print(f"  Worker {rank} Received Order {order['id']}: {order['item']}")