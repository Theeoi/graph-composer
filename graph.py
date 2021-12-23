import random

class Vertex(object):
    def __init__(self, value):
        self.value = value # The word from text input
        self.adjacent = {}
        self.neighbors = []
        self.neighbor_weights = []

    def add_edge_to(self, vertex, weight=0):
        self.adjacent[vertex] = weight

    def increment_edge(self, vertex):
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1 # Get adjacent-number and increment

    def get_adjacent_nodes(self):
        pass

    def get_probability_map(self):
        for (vertex, weight) in self.adjacent.items():
            self.neighbors.append(vertex)
            self.neighbor_weights.append(weight)

    def next_word(self):
        return random.choices(self.neighbors, self.neighbor_weights)[0]



class Graph(object):
    def __init__(self):
        self.vertices = {}

    def get_vertex_values(self):
        return set(self.vertices.keys())

    def add_vertex(self, value):
        self.vertices[value] = Vertex(value)

    def get_vertex(self, value):
        if value not in self.vertices: # Create new Vertex if word not in graph.
            self.add_vertex(value)
        return self.vertices[value] # Else return the object.

    def get_next_word(self, current_vertex):
        return self.vertices[current_vertex.value].next_word()

    def generate_probability_mappings(self):
        for vertex in self.vertices.values():
            vertex.get_probability_map()
