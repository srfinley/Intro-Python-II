# Write a class to hold player information, e.g. what room they are in
# currently.
from item import LightSource


class Player():
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def __str__(self):
        return f'{self.name} at {self.current_room}'

    def can_see(self):
        """Returns whether the player can see the room"""
        lit = self.current_room.is_light
        if not lit:
            for item in self.inventory:
                if isinstance(item, LightSource):
                    lit = True
                    break
        if not lit:
            for item in self.current_room.contents:
                if isinstance(item, LightSource):
                    lit = True
                    break
        return lit

    def examine_room(self):
        """Prints room, unless player can't see"""
        lit = self.can_see()
        if lit:
            print(self.current_room)
        else:
            print("It's pitch black!")

    def go(self, direction):
        """Changes current room to one in [direction], if possible"""
        if getattr(self.current_room, f'{direction}_to'):
            self.current_room = getattr(self.current_room, f'{direction}_to')
            self.examine_room()
        else:
            print("You can't go that way.")

    def look(self, obj):
        """Prints description of room or specified item"""
        if obj:
            success = False
            for item in self.inventory:
                if obj == item.name:
                    print(f"You're holding {obj}.")
                    print(item.description)
                    success = True
                    break
            if not success:
                for item in self.current_room.contents:
                    if obj == item.name:
                        print(f"There's {obj} here.")
                        print(item.description)
                        success = True
                        break
            if not success:
                print(f"No {obj} to look at.")
        else:
            self.examine_room()

    def take(self, obj):
        """Removes item(s) from room contents and adds to inventory"""
        success = False
        if self.can_see():
            if obj == "all":
                for item in self.current_room.contents:
                    item.on_take()
                    success = True
                self.inventory.extend(self.current_room.contents)
                self.current_room.contents = []

            for item in self.current_room.contents:
                if obj == item.name:
                    self.inventory.append(item)
                    self.current_room.contents.remove(item)
                    item.on_take()
                    success = True
                    break
            if not success:
                for item in self.inventory:
                    if obj == item.name:
                        print(f"You already have {obj}!")
            if not success:
                print(f"No {obj} to take.")
        else:
            print("Good luck finding that in the dark!")

    def drop(self, obj):
        """Removes item(s) from inventory and adds to room contents"""
        success = False
        if obj == "all":
            for item in self.inventory:
                self.current_room.contents.append(item)
                item.on_drop()
                success = True
            self.inventory = []
        for item in self.inventory:
            if obj == item.name:
                self.current_room.contents.append(item)
                self.inventory.remove(item)
                item.on_drop()
                success = True
                break
        if not success:
            print(f"You don't have {obj}.")

    def check_inventory(self):
        """Print contents of inventory"""
        if len(self.inventory) > 0:
            print("You have:")
            for item in self.inventory:
                print(item)
        else:
            print("You aren't carrying anything.")

    def id_item(self, obj):
        """Looks for an available item with full or partial name match"""
        for i in range(-len(obj), 0):
            # compares long input to short name
            # checks the full string, then cuts off each leading word to check
            # e.g. "the sword" can be interpreted as "sword"
            name = ' '.join(obj[i:])
            for item in self.inventory:
                if name == item.name:
                    return name
            for item in self.current_room.contents:
                if name == item.name:
                    return name
        # compare short input to long name
        name = ' '.join(obj)
        for item in self.inventory:
            if name in item.name:
                return item.name
        for item in self.current_room.contents:
            if name in item.name:
                return item.name
        return name

    def execute(self, command):
        """Redirects multiword commands to the appropriate function"""
        words = command.split()
        verb = words[0]
        obj = self.id_item(words[1:])
        # obj = ' '.join(words[1:])
        if verb == 'look':
            self.look(obj)
        if verb == 'get' or verb == 'take':
            self.take(obj)
        if verb == 'drop':
            self.drop(obj)
