from greedy_coloring import greedy_coloring


def is_valid(graph, colors, vertex, color):

    for neighbour in graph.neighbours(vertex):
        if neighbour in colors and colors[neighbour] == color:
            return False

    return True


def local_search(graph):

    colors = greedy_coloring(graph)

    improved = True

    while improved:

        improved = False

        for vertex in graph.vertices():

            current_color = colors[vertex]

            for new_color in range(current_color):

                if is_valid(graph, colors, vertex, new_color):

                    colors[vertex] = new_color
                    improved = True
                    break

    return colors