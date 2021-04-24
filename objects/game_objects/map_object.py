class MapObject:

    def __init__(self, name='', description='', color=None, char=None, options=[], area=1000, tile_structure=None):
        self.name = name
        self.description = description
        self.char = char
        self.color = color
        self.options = options
        self.area = area
        self.structures = []
        self.settlement = []
        self.tile_structure = tile_structure
