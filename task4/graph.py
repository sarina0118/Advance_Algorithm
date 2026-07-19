class Graph:

    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, source, destination):

        self.add_vertex(source)
        self.add_vertex(destination)

        self.graph[source].append(destination)
        self.graph[destination].append(source)

    def vertices(self):
        return list(self.graph.keys())

    def neighbours(self, vertex):
        return self.graph[vertex]

    def display(self):

        print("Graph:\n")

        for vertex in self.graph:
            print(vertex, "->", self.graph[vertex])