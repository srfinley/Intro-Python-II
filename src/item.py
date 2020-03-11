class Item():
    """Any object that can be taken from a room by a player"""
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name
