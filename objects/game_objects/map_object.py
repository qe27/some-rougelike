class MapObject:

    def __init__(self, name, description, color=None, char=None, options=[]):
        self.name = name
        self.description = description
        self.char = char
        self.color = color
        self.options = options