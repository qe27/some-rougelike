class GameObject:

    def __init__(self, char, color, name, blocks=True, tile=None):
        """
        TODO: support object links, options, etc
        """
        self.char = char
        self.color = color
        self.name = name
        self.blocks = blocks
        self.tile = tile
