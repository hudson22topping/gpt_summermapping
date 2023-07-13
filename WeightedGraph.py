class WeightedGraph:
    def __init__(self):
        self.vertices = set()  # Set of vertices
        self.edges = {}  # Dictionary to store edges and their weights
        self.modes_of_transportation = set()  # Set of modes of transportation
        self.time_values = {}  # Dictionary to store time values for each mode

    def add_vertex(self, vertex):
        self.vertices.add(vertex)

    def add_edge(self, start, end, weight):
        if start not in self.vertices or end not in self.vertices:
            raise ValueError("One or both vertices not found in the graph.")

        if start not in self.edges:
            self.edges[start] = {}

        self.edges[start][end] = weight

    def add_transportation_mode(self, mode, time_value):
        self.modes_of_transportation.add(mode)
        self.time_values[mode] = time_value
