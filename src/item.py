class Item():
    """Any object that can be taken from a room by a player"""
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name

    def on_take(self):
        print(f'You have picked up {self.name}.')

    def on_drop(self):
        print(f'You have dropped {self.name}.')

class LightSource(Item):
    """An item that illuminates a dark room"""
    def on_drop(self):
        print("It's not wise to drop your source of light!")
        super().on_drop()