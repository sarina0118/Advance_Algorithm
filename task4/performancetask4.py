import csv
import os
import random
import time

from graph import Graph
from greedy_coloring import greedy_coloring
from local_search import local_search


def generate_graph(vertices, edges):

    graph = Graph()

    for i in range(vertices):
        graph.add_vertex(str(i))

    count = 0

    while count < edges:

        u = str(random.randint(0, vertices - 1))
        v = str(random.randint(0, vertices - 1))

        if u != v and v not in graph.graph[u]:

            graph.add_edge(u, v)
            count += 1

    return graph


os.makedirs("outputs", exist_ok=True)

csv_file = open(
    "outputs/performance_task4.csv",
    "w",
    newline=""
)

writer = csv.writer(csv_file)

writer.writerow([
    "Vertices",
    "Edges",
    "Algorithm",
    "Colors Used",
    "Execution Time"
])


for vertices, edges in [
    (20, 40),
    (50, 120),
    (100, 300)
]:

    print("\n" + "-" * 40)
    print(f"Testing Graph ({vertices} vertices, {edges} edges)")
    print("-" * 40)

    graph = generate_graph(vertices, edges)

    start = time.perf_counter()
    greedy = greedy_coloring(graph)
    greedy_time = time.perf_counter() - start

    greedy_colors = len(set(greedy.values()))

    print("Greedy:", greedy_time)

    writer.writerow([
        vertices,
        edges,
        "Greedy",
        greedy_colors,
        greedy_time
    ])

    start = time.perf_counter()
    local = local_search(graph)
    local_time = time.perf_counter() - start

    local_colors = len(set(local.values()))

    print("Local Search:", local_time)

    writer.writerow([
        vertices,
        edges,
        "Local Search",
        local_colors,
        local_time
    ])


csv_file.close()

print("\nPerformance results saved to outputs/performance_task4.csv")