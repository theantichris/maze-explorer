class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}

    def __repr__(self):
        return self.value

    def add_edge(self, vertex, weight=0):
        self.edges[vertex.value] = weight

    def get_edges(self):
        return self.edges.keys()