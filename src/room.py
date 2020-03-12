# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self, name, description, is_light=True):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.contents = []
        self.is_light = is_light

    def __str__(self):
        s = ''
        if self.is_light:
            s = f'{self.name} \n {self.description}'
            if self.contents:
                s += '\nThese items are here: '
                for item in self.contents:
                    s += str(item)
                    s += ', '
        else:
            s = "It's pitch black!"
        return s
