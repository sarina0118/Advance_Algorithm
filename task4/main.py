from graph import Graph
from greedy_coloring import greedy_coloring
from local_search import local_search

graph = Graph()

graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "C")
graph.add_edge("B", "D")
graph.add_edge("C", "D")
graph.add_edge("C", "E")
graph.add_edge("D", "E")

print("-" * 30)
print("GRAPH")
print("-" * 30)

graph.display()

print("\n" + "-" * 30)
print("GREEDY COLORING")
print("-" * 30)

greedy_result = greedy_coloring(graph)

for vertex, color in greedy_result.items():
    print(f"{vertex}: Color {color}")

print("\n" + "-" * 30)
print("LOCAL SEARCH")
print("-" * 30)

local_result = local_search(graph)

for vertex, color in local_result.items():
    print(f"{vertex}: Color {color}")

print("\nNumber of colors used (Greedy):",
      len(set(greedy_result.values())))

print("Number of colors used (Local Search):",
      len(set(local_result.values())))