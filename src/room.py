# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.contents = []

    def __str__(self):
        s = f'{self.name} \n {self.description}'
        if self.contents:
            s += '\nThese items are here: '
            for item in self.contents:
                s += str(item)
                s+= ', '
        return s
