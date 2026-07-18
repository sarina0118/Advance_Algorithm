from city_graph import Graph
from dijkstra import dijkstra
from prim import prim
from bellman_ford import bellman_ford


graph = Graph()

graph.add_edge("Kathmandu", "Pokhara", 200)
graph.add_edge("Kathmandu", "Butwal", 250)
graph.add_edge("Pokhara", "Chitwan", 150)
graph.add_edge("Butwal", "Chitwan", 80)
graph.add_edge("Butwal", "Nepalgunj", 120)
graph.add_edge("Chitwan", "Birgunj", 100)
graph.add_edge("Birgunj", "Kathmandu", 180)


print("-" * 30)
print("TRANSPORTATION NETWORK")
print("-" * 30)

graph.display()


print("\n" + "-" * 30)
print("DIJKSTRA'S ALGORITHM")
print("-" * 30)

distances = dijkstra(graph.graph, "Kathmandu")

for city, distance in distances.items():
    print(f"{city}: {distance}")


print("\n" + "-" * 30)
print("PRIM'S ALGORITHM")
print("-" * 30)

mst, total_weight = prim(graph.graph, "Kathmandu")

print("Minimum Spanning Tree:\n")

for source, destination, weight in mst:
    print(f"{source} --> {destination} ({weight})")

print("\nTotal Weight:", total_weight)
print("\n" + "-" * 30)
print("BELLMAN-FORD (Negative Cycle Test)")
print("-" * 30)

negative_graph = Graph()

negative_graph.add_edge("A", "B", 4)
negative_graph.add_edge("B", "C", -6)
negative_graph.add_edge("C", "A", 1)

bellman_ford(negative_graph.graph, "A")


print("\n" + "-" * 30)
print("BELLMAN-FORD ALGORITHM")
print("-" * 30)

distances = bellman_ford(graph.graph, "Kathmandu")

if distances is not None:
    for city, distance in distances.items():
        print(f"{city}: {distance}")