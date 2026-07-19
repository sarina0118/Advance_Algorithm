import csv
import os
import random
import time
from concurrent.futures import ThreadPoolExecutor

from merge_sort import merge_sort
from parallel_merge_sort import parallel_merge_sort


def generate_data(size):
    return [random.randint(1, 100000) for _ in range(size)]


os.makedirs("outputs", exist_ok=True)

csv_file = open(
    "outputs/performance_task5.csv",
    "w",
    newline=""
)

writer = csv.writer(csv_file)

writer.writerow([
    "Dataset Size",
    "Threads",
    "Sequential Time",
    "Parallel Time",
    "Speedup"
])


for size in [1000, 5000, 10000]:

    print("\n" + "-" * 30)
    print(f"Testing {size} numbers")
    print("-" * 30)

    data = generate_data(size)

    start = time.perf_counter()
    merge_sort(data.copy())
    sequential_time = time.perf_counter() - start

    print("Sequential:", sequential_time)

    for threads in [1, 2, 4, 8]:

        start = time.perf_counter()

        with ThreadPoolExecutor(max_workers=threads) as executor:
            future = executor.submit(parallel_merge_sort, data.copy())
            future.result()

        parallel_time = time.perf_counter() - start

        speedup = sequential_time / parallel_time

        print(
            f"{threads} Threads: {parallel_time:.6f} sec | "
            f"Speedup: {speedup:.2f}"
        )

        writer.writerow([
            size,
            threads,
            sequential_time,
            parallel_time,
            speedup
        ])

csv_file.close()

print("\nPerformance results saved to outputs/performance_task5.csv")