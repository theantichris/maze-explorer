from vertex import Vertex

class Graph:
    def __init__(self):
        self.graph_dict = {}

    def add_vertex(self, vertex):
        self.graph_dict[vertex.value] = vertex

    def add_edge(self, from_node, to_node, weight=0):
        self.graph_dict[from_node.value].add_edge(to_node, weight)
        self.graph_dict[to_node.value].add_edge(from_node, weight)

    def explore(self):
        print("Exploring the graph...\n")

    def print_map(self):
        print("\nMAZE LAYOUT\n")

        for key in self.graph_dict:
            print("{} connected to...".format(key))
            vertex = self.graph_dict[key]
            for adjacent_vertex, weight in vertex.edges.items():
                print("=> {}: cost is {}".format(adjacent_vertex, weight))
            print("")
        print("")

def build_graph():
    graph = Graph()
    graph.print_map()

    return graph