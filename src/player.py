# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room ):
        self.name = name
        self.current_room = current_room

    def move(self, direction):
        if direction in ['n', 's', 'e', 'w']:
            next_room = self.current_room.get_room_in_direction(direction)
            if next_room is not None:
                self.current_room = next_room
                print(self.current_room)
            else: 
                print('Cannot move in that direction')