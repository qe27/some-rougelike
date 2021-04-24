import tcod

from objects.game_objects.map_object import MapObject


class River(MapObject):

    def __init__(self, name='Nile', description='Egyptian river', color=tcod.blue, char=None, options={}):
        super().__init__()
        self.name = name
        self.description = description
        self.color = color
        self.options = options
        self.char = 'r'
        self.type = 'River'
