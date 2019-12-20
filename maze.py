from room import Room

class Maze:
    def __init__(self):
        self.rooms = {}

    def add_room(self, room):
        self.rooms[room.name] = room

    def add_path(self, from_room, to_room, weight=0):
        self.rooms[from_room.name].add_path(to_room, weight)
        self.rooms[to_room.name].add_path(from_room, weight)

    def explore(self):
        print("Exploring the graph...\n")

        path_total = 0
        current_room_name = "entrance"

        print("\nStarting off at the {}".format(current_room_name))

        while current_room_name != "treasure room":
            current_room = self.rooms[current_room_name]
            valid_choices = []
            for connected_room, weight in current_room.paths.items():
                connected_room = connected_room[0]
                valid_choices.append(connected_room)
                print("enter {} for {}: {} cost".format(connected_room, connected_room, weight))

            print("You have accumulated: {} cost".format(path_total))

            choice = input("\nWhich room do you move to? ")

            if choice not in valid_choices:
                print("Please select from these letters: {}".format(valid_choices))
            else:
                for connected_room in current_room.paths.keys():
                    if connected_room.startswith(choice):
                        current_room_name = self.rooms[connected_room].name
                        path_total += current_room.paths[connected_room]

                print("\n*** You have chosen: {} ***\n".format(current_room_name))

        print("You made it to the treasure room with {} cost".format(path_total))


    def print_map(self):
        print("\nMAZE LAYOUT\n")

        for key in self.rooms:
            print("{} connected to...".format(key))
            room = self.rooms[key]
            for connected_room, weight in room.paths.items():
                print("=> {}: cost is {}".format(connected_room, weight))
            print("")
        print("")

def build_maze():
    excavation_site = Maze()

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
