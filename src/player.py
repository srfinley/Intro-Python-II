# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return f'Player at {self.current_room}'

    def check_direction(self, direction):
        if direction == 'n':
            return self.current_room.n_to
        elif direction == 'e':
            return self.current_room.e_to
        elif direction == 's':
            return self.current_room.s_to
        elif direction == 'w':
            return self.current_room.w_to
        else:
            return False

    def go(self, direction):
        if self.check_direction(direction):
            self.current_room = self.check_direction(direction)
        else:
            print("You can't go that way.")