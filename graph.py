from room import Room

class Graph:
    def __init__(self):
        self.graph_dict = {}

    def add_room(self, room):
        self.graph_dict[room.name] = room

    def add_path(self, from_room, to_room, weight=0):
        self.graph_dict[from_room.name].add_path(to_room, weight)
        self.graph_dict[to_room.name].add_path(from_room, weight)

    def explore(self):
        print("Exploring the graph...\n")

        path_total = 0
        current_room_name = "entrance"

        print("\nStarting off at the {}".format(current_room_name))

        while current_room_name != "treasure room":
            current_room = self.graph_dict[current_room_name]
            valid_choices = []
            for connected_room, weight in current_room.paths.items():
                key = connected_room[0]
                valid_choices.append(key)
                print("enter {} for {}: {} cost".format(key, connected_room, weight))

            print("You have accumulated: {} cost".format(path_total))

            choice = input("\nWhich room do you move to? ")

            if choice not in valid_choices:
                print("Please select from these letters: {}".format(valid_choices))
            else:
                for key in current_room.paths.keys():
                    if key.startswith(choice):
                        current_room_name = self.graph_dict[key].name
                        path_total += current_room.paths[key]

                print("\n*** You have chosen: {} ***\n".format(current_room_name))

        print("You made it to the treasure room with {} cost".format(path_total))


    def print_map(self):
        print("\nMAZE LAYOUT\n")

        for key in self.graph_dict:
            print("{} connected to...".format(key))
            room = self.graph_dict[key]
            for connected_room, weight in room.paths.items():
                print("=> {}: cost is {}".format(connected_room, weight))
            print("")
        print("")

def build_excavation_site():
    excavation_site = Graph()

    # Make rooms
    entrance = Room("entrance")
    ante_chamber = Room("ante-chamber")
    kings_room = Room("king's room")
    grand_gallery = Room("grand gallery")
    treasure_room = Room("treasure room")

    # Add rooms to maze
    excavation_site.add_room(entrance)
    excavation_site.add_room(ante_chamber)
    excavation_site.add_room(kings_room)
    excavation_site.add_room(grand_gallery)
    excavation_site.add_room(treasure_room)

    # Add paths between rooms
    excavation_site.add_path(entrance, ante_chamber, 7)
    excavation_site.add_path(entrance, kings_room, 3)
    excavation_site.add_path(kings_room, ante_chamber, 1)
    excavation_site.add_path(grand_gallery, ante_chamber, 2)
    excavation_site.add_path(grand_gallery, kings_room, 2)
    excavation_site.add_path(treasure_room, ante_chamber, 6)
    excavation_site.add_path(treasure_room, grand_gallery, 4)

    excavation_site.print_map()

    return excavation_site
