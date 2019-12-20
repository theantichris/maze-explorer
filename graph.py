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

def build_excavation_site():
    excavation_site = Graph()

    # Make rooms
    entrance = Vertex("entrance")
    ante_chamber = Vertex("ante-chamber")
    kings_room = Vertex("king's room")
    grand_gallery = Vertex("grand gallery")
    treasure_room = Vertex("treasure room")

    # Add rooms to maze
    excavation_site.add_vertex(entrance)
    excavation_site.add_vertex(ante_chamber)
    excavation_site.add_vertex(kings_room)
    excavation_site.add_vertex(grand_gallery)
    excavation_site.add_vertex(treasure_room)

    # Add paths between rooms
    excavation_site.add_edge(entrance, ante_chamber, 7)
    excavation_site.add_edge(entrance, kings_room, 3)
    excavation_site.add_edge(kings_room, ante_chamber, 1)
    excavation_site.add_edge(grand_gallery, ante_chamber, 2)
    excavation_site.add_edge(grand_gallery, kings_room, 2)
    excavation_site.add_edge(treasure_room, ante_chamber, 6)
    excavation_site.add_edge(treasure_room, grand_gallery, 4)

    excavation_site.print_map()

    return excavation_site
