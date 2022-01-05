import random

class Vertex(object):
    def __init__(self, value):
        self.value: str = value # The word from text input
        self.adjacent: dict[Vertex, int] = {}
        self.neighbors: list[Vertex] = []
        self.neighbor_weights: list[int] = []

    def increment_edge(self, vertex: 'Vertex') -> None:
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1 # Get adjacent-number and increment

    def get_probability_map(self) -> None:
        for (vertex, weight) in self.adjacent.items():
            self.neighbors.append(vertex)
            self.neighbor_weights.append(weight)

    def next_word(self) -> 'Vertex':
        return random.choices(self.neighbors, self.neighbor_weights)[0]


class Graph(object):
    def __init__(self):
        self.vertices: dict[str, Vertex] = {}

    def get_vertex_values(self) -> set:
        return set(self.vertices.keys())

    def add_vertex(self, value: str) -> None:
        self.vertices[value] = Vertex(value)

    def get_vertex(self, value: str) -> Vertex:
        if value not in self.vertices: # Create new Vertex if word not in graph.
            self.add_vertex(value)
        return self.vertices[value] # Else return the object.

    def get_next_word(self, current_vertex: Vertex) -> Vertex:
        return self.vertices[current_vertex.value].next_word()

    def generate_probability_mappings(self) -> None:
        for vertex in self.vertices.values():
            vertex.get_probability_map()
