# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def __str__(self):
        return f'{self.name} at {self.current_room}'

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

    def look(self, obj):
        pass

    def take(self, obj):
        success = False
        for item in self.current_room.contents:
            if obj == item.name:
                self.inventory.append(item)
                self.current_room.contents.remove(item)
                # print(f'Got {obj}!')
                item.on_take()
                success = True
                break
        if not success:
            for item in self.inventory:
                if obj == item.name:
                    print(f"You already have {obj}!")
        if not success:
            print(f"No {obj} to take.")
            
    def drop(self, obj):
        success = False
        for item in self.inventory:
            if obj == item.name:
                self.current_room.contents.append(item)
                self.inventory.remove(item)
                item.on_drop()
                success = True
                break
        if not success:
            print(f"You don't have {obj}.")

    def execute(self, command):
        words = command.split()
        verb = words[0]
        obj = ' '.join(words[1:])
        if verb == 'look':
            self.look(obj)
        if verb == 'get' or verb == 'take':
            self.take(obj)
        if verb == 'drop':
            self.drop(obj)
