import csv
import os
import time

from graph_genetor import generate_graph
from dijkstra import dijkstra
from prim import prim
from bellman_ford import bellman_ford


os.makedirs("outputs", exist_ok=True)

csv_file = open("outputs/performance_results.csv", "w", newline="")

writer = csv.writer(csv_file)

writer.writerow([
    "Vertices",
    "Edges",
    "Algorithm",
    "Execution Time (seconds)"
])


def test_algorithms(vertices, edges):

    print("\n" + "-" * 40)
    print(f"Testing Graph ({vertices} vertices, {edges} edges)")
    print("-" * 40)

    graph = generate_graph(vertices, edges)

    start_vertex = "City_0"

    # Dijkstra
    start = time.perf_counter()
    dijkstra(graph.graph, start_vertex)
    dijkstra_time = time.perf_counter() - start

    print("Dijkstra:", dijkstra_time)

    writer.writerow([
        vertices,
        edges,
        "Dijkstra",
        dijkstra_time
    ])

    # Prim
    start = time.perf_counter()
    prim(graph.graph, start_vertex)
    prim_time = time.perf_counter() - start

    print("Prim:", prim_time)

    writer.writerow([
        vertices,
        edges,
        "Prim",
        prim_time
    ])

    # Bellman-Ford
    start = time.perf_counter()
    bellman_ford(graph.graph, start_vertex)
    bellman_time = time.perf_counter() - start

    print("Bellman-Ford:", bellman_time)

    writer.writerow([
        vertices,
        edges,
        "Bellman-Ford",
        bellman_time
    ])


test_algorithms(100, 300)
test_algorithms(1000, 3000)
test_algorithms(5000, 15000)

csv_file.close()

print("\nPerformance results saved to outputs/performancetask2_results.csv")