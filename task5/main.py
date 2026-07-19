import random

from merge_sort import merge_sort
from parallel_merge_sort import parallel_merge_sort


numbers = [random.randint(1, 100) for _ in range(20)]

print("-" * 30)
print("ORIGINAL ARRAY")
print("-" * 30)
print(numbers)

print("\n" + "-" * 30)
print("SEQUENTIAL MERGE SORT")
print("-" * 30)

sorted_numbers = merge_sort(numbers.copy())
print(sorted_numbers)

print("\n" + "-" * 30)
print("PARALLEL MERGE SORT")
print("-" * 30)

parallel_sorted = parallel_merge_sort(numbers.copy())
print(parallel_sorted)

if sorted_numbers == parallel_sorted:
    print("\n Both algorithms produced the same result.")
else:
    print("\n Results are different.")