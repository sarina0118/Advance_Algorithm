def greedy_coloring(graph):

    colors = {}

    for vertex in graph.vertices():

        used_colors = set()

        for neighbour in graph.neighbours(vertex):

            if neighbour in colors:
                used_colors.add(colors[neighbour])

        color = 0

        while color in used_colors:
            color += 1

        colors[vertex] = color

    return colors