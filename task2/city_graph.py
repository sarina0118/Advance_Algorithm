class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, source, destination, weight):
        self.add_vertex(source)
        self.add_vertex(destination)

        self.graph[source].append((destination, weight))

    def display(self):
        print("Transportation Network:\n")

        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")