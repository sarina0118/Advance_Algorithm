import random
from city_graph import Graph


def generate_graph(num_vertices, num_edges):

    graph = Graph()

    vertices = []

    for i in range(num_vertices):
        vertex = f"City_{i}"
        vertices.append(vertex)
        graph.add_vertex(vertex)

    for _ in range(num_edges):

        source = random.choice(vertices)
        destination = random.choice(vertices)

        while destination == source:
            destination = random.choice(vertices)

        weight = random.randint(1, 100)

        graph.add_edge(source, destination, weight)

    return graph