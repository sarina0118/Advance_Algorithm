def is_safe(vertex, graph, path, position):

    # Check if there is an edge
    if graph[path[position - 1]][vertex] == 0:
        return False

    # Check if vertex already exists in the path
    if vertex in path:
        return False

    return True


def hamiltonian_util(graph, path, position):

    if position == len(graph):

        if graph[path[position - 1]][path[0]] == 1:
            return True

        return False

    for vertex in range(1, len(graph)):

        if is_safe(vertex, graph, path, position):

            path[position] = vertex

            if hamiltonian_util(graph, path, position + 1):
                return True

            path[position] = -1

    return False


def hamiltonian_cycle(graph):

    path = [-1] * len(graph)

    path[0] = 0

    if not hamiltonian_util(graph, path, 1):
        return None

    path.append(path[0])

    return path