import csv
import os
import random
import time

from coin_change import coin_change_limited
from mice_to_holes import assign_mice_to_holes
from hamiltonian import hamiltonian_cycle


os.makedirs("outputs", exist_ok=True)

csv_file = open("outputs/performance_task3.csv", "w", newline="")
writer = csv.writer(csv_file)

writer.writerow([
    "Algorithm",
    "Input Size",
    "Execution Time (seconds)"
])


def test_coin_change():

    print("\nTesting Coin Change")

    for size in [20, 50, 100]:

        coins = [1, 2, 5, 10, 20]
        limits = [10, 10, 10, 10, 10]
        target = size

        start = time.perf_counter()
        coin_change_limited(coins, limits, target)
        execution_time = time.perf_counter() - start

        print(f"Target {size}: {execution_time}")

        writer.writerow([
            "Coin Change",
            size,
            execution_time
        ])


def test_mice_to_holes():

    print("\nTesting Mice to Holes")

    for size in [100, 1000, 5000]:

        mice = random.sample(range(size * 10), size)
        holes = random.sample(range(size * 10), size)

        start = time.perf_counter()
        assign_mice_to_holes(mice, holes)
        execution_time = time.perf_counter() - start

        print(f"{size} mice: {execution_time}")

        writer.writerow([
            "Assign Mice to Holes",
            size,
            execution_time
        ])


def test_hamiltonian():

    print("\nTesting Hamiltonian Cycle")

    for n in [4, 5, 6]:

        graph = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i != j:
                    graph[i][j] = 1

        start = time.perf_counter()
        hamiltonian_cycle(graph)
        execution_time = time.perf_counter() - start

        print(f"{n} vertices: {execution_time}")

        writer.writerow([
            "Hamiltonian Cycle",
            n,
            execution_time
        ])


test_coin_change()
test_mice_to_holes()
test_hamiltonian()

csv_file.close()

print("\nPerformance results saved to outputs/performance_task3.csv")