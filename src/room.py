# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        string = ""
        string += f'You are currently in {self.name} -- {self.description}\n'
        string += f'Available Exits : {self.get_exits()}'
        return string

    def get_exits(self):
        exits = []
        if self.n_to is not None:
            exits.append('n')
        if self.s_to is not None:
            exits.append('s')
        if self.w_to is not None:
            exits.append('w')
        if self.e_to is not None:
            exits.append('e')
        return exits

    def get_room_in_direction(self, direction):
        "get the room in this direction"
        if direction == 'n':
            return self.n_to
        if direction == 's':
            return self.s_to
        if direction == 'e':
            return self.e_to
        if direction == 'w':
            return self.w_to
        else:
            return None