def bellman_ford(graph, start):

    distances = {}

    for vertex in graph:
        distances[vertex] = float("inf")

    distances[start] = 0

    vertices = list(graph.keys())
    for _ in range(len(vertices) - 1):

        for vertex in graph:

            for neighbour, weight in graph[vertex]:

                if (
                    distances[vertex] != float("inf")
                    and distances[vertex] + weight < distances[neighbour]
                ):

                    distances[neighbour] = (
                        distances[vertex] + weight
                    )
    for vertex in graph:

        for neighbour, weight in graph[vertex]:

            if (
                distances[vertex] != float("inf")
                and distances[vertex] + weight < distances[neighbour]
            ):

                print("Negative weight cycle detected!")
                return None

    return distances