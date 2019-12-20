from room import Room

class Maze:
    def __init__(self):
        self.rooms = {}
        self.path_total = 0
        self.current_room_name = 'entrance'

    def add_room(self, room):
        self.rooms[room.name] = room

    def add_path(self, from_room, to_room, weight=0):
        self.rooms[from_room.name].add_path(to_room, weight)
        self.rooms[to_room.name].add_path(from_room, weight)

    def build_choices(self, current_room):
        valid_choices = []
        for connected_room, weight in current_room.paths.items():
            key = connected_room[0]
            valid_choices.append(key)
            print("enter {} for {}: {} cost".format(key, connected_room, weight))
        return valid_choices

    def move_to_room(self, current_room, choice):
        for connected_room in current_room.paths.keys():
            if connected_room.startswith(choice):
                self.current_room_name = self.rooms[connected_room].name
                self.path_total += current_room.paths[connected_room]

        print("\n***You are now in the {} ***\n".format(self.current_room_name))
    
    def explore_maze(self):
        print("Exploring the maze...\n")
        print("You are in the {}\n".format(self.current_room_name))

        while self.current_room_name != "treasure room":
            current_room = self.rooms[self.current_room_name]
            valid_choices = self.build_choices(current_room)
            print("\nYou have accumulated: {} cost".format(self.path_total))
            choice = input("\nWhich room do you move to? ")

            if choice not in valid_choices:
                print("Please select from these letters: {}".format(valid_choices))
            else:
                self.move_to_room(current_room, choice)

        print("You made it to the treasure room with {} cost".format(self.path_total))

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
    maze = Maze()

    # Make rooms
    entrance = Room("entrance")
    ante_chamber = Room("ante-chamber")
    kings_room = Room("king's room")
    grand_gallery = Room("grand gallery")
    treasure_room = Room("treasure room")

    # Add rooms to maze
    maze.add_room(entrance)
    maze.add_room(ante_chamber)
    maze.add_room(kings_room)
    maze.add_room(grand_gallery)
    maze.add_room(treasure_room)

    # Add paths between rooms
    maze.add_path(entrance, ante_chamber, 7)
    maze.add_path(entrance, kings_room, 3)
    maze.add_path(kings_room, ante_chamber, 1)
    maze.add_path(grand_gallery, ante_chamber, 2)
    maze.add_path(grand_gallery, kings_room, 2)
    maze.add_path(treasure_room, ante_chamber, 6)
    maze.add_path(treasure_room, grand_gallery, 4)

    return maze

