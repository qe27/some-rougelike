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

    def setTile(self, tile):
        old_tile = self.tile
        self.tile = tile
        # if old_tile.objects:
        #     for obj in old_tile.objects:
        #         if (obj == self):
        old_tile.objects.remove(self)
        self.tile.objects.append(self)
