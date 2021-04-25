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
        self.resource_sources = []

    def get_structures_by_output_type(self, resource_type):
        # TODO: return also production structures outputs
        structures_of_type = []
        for i in self.resource_sources:
            if i.resource_type == resource_type:
                structures_of_type.extend(i)
        return structures_of_type

