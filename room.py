class Room:
    def __init__(self, name):
        self.name = name
        self.paths = {}

    def __repr__(self):
        return self.name

    def add_path(self, to_room, weight=0):
        self.paths[to_room.name] = weight
