import tcod

from objects.game_objects.structures.structure import Structure


class Farmfield(Structure):
    type = 'Farmfield'

    def __init__(self, name='Crop field', description='Big field with a scarecrow', color=tcod.red, char=None, options={}):
        super(Structure, self).__init__()
        self.name = name
        self.description = description
        self.color = color
        self.options = options
        self.char = '\''
        self.size = 10
        self.type = 'Farmfield'
