import heapq

def prim(graph, start):

    visited = set()

    minimum_spanning_tree = []

    priority_queue = [(0, start, None)]

    total_weight = 0

    while priority_queue:

        weight, current, previous = heapq.heappop(priority_queue)

        if current in visited:
            continue

        visited.add(current)

        if previous is not None:
            minimum_spanning_tree.append((previous, current, weight))
            total_weight += weight

        for neighbour, edge_weight in graph[current]:

            if neighbour not in visited:

                heapq.heappush(
                    priority_queue,
                    (edge_weight, neighbour, current)
                )

    return minimum_spanning_tree, total_weight