import csv
import os
import time

from city import City
from bst import BinarySearchTree
from avl import AVLTree
from min_heap import MinHeap
from hash_table import HashTable


def load_cities(filename):
    cities = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            city = City(
                row["Name"],
                float(row["X_Coordinate"]),
                float(row["Y_Coordinate"]),
                int(row["Population"]),
                float(row["Distance"])
            )

            cities.append(city)

    return cities



os.makedirs("outputs", exist_ok=True)
csv_file = open("outputs/performance_results.csv", "w", newline="")
writer = csv.writer(csv_file)

writer.writerow([
    "Dataset",
    "Data Structure",
    "Insert Time",
    "Search Time",
    "Delete/Remove Time"
])


def test_performance(filename):

    print("\n" + "-" * 30)
    print("Testing:", filename)
    print("-" * 30)

    cities = load_cities(filename)

    target_city = cities[len(cities) // 2].name

    
    bst = BinarySearchTree()

    start = time.perf_counter()
    for city in cities:
        bst.insert(city)
    bst_insert = time.perf_counter() - start

    start = time.perf_counter()
    bst.search(target_city)
    bst_search = time.perf_counter() - start

    start = time.perf_counter()
    bst.delete(target_city)
    bst_delete = time.perf_counter() - start

    
    avl = AVLTree()

    start = time.perf_counter()
    for city in cities:
        avl.insert(city)
    avl_insert = time.perf_counter() - start

    start = time.perf_counter()
    avl.search(target_city)
    avl_search = time.perf_counter() - start

    start = time.perf_counter()
    avl.delete(target_city)
    avl_delete = time.perf_counter() - start

    
    heap = MinHeap()

    start = time.perf_counter()
    for city in cities:
        heap.insert(city)
    heap_insert = time.perf_counter() - start

    start = time.perf_counter()
    heap.remove_min()
    heap_remove = time.perf_counter() - start

    
    table = HashTable()

    start = time.perf_counter()
    for city in cities:
        table.insert(city)
    hash_insert = time.perf_counter() - start

    start = time.perf_counter()
    table.search(target_city)
    hash_search = time.perf_counter() - start

    start = time.perf_counter()
    table.delete(target_city)
    hash_delete = time.perf_counter() - start

    print("\nBST")
    print("Insert :", bst_insert)
    print("Search :", bst_search)
    print("Delete :", bst_delete)

    print("\nAVL Tree")
    print("Insert :", avl_insert)
    print("Search :", avl_search)
    print("Delete :", avl_delete)

    print("\nMin Heap")
    print("Insert :", heap_insert)
    print("Remove :", heap_remove)

    print("\nHash Table")
    print("Insert :", hash_insert)
    print("Search :", hash_search)
    print("Delete :", hash_delete)
    print()

    dataset = os.path.basename(filename)

    writer.writerow([
        dataset,
        "BST",
        bst_insert,
        bst_search,
        bst_delete
    ])

    writer.writerow([
        dataset,
        "AVL Tree",
        avl_insert,
        avl_search,
        avl_delete
    ])

    writer.writerow([
        dataset,
        "Min Heap",
        heap_insert,
        "N/A",
        heap_remove
    ])

    writer.writerow([
        dataset,
        "Hash Table",
        hash_insert,
        hash_search,
        hash_delete
    ])

test_performance("data/cities_100.csv")
test_performance("data/cities_1000.csv")
test_performance("data/cities_10000.csv")

csv_file.close()
print("\nPerformance results saved to outputs/performance_results.csv")