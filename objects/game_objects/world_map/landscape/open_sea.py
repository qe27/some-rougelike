import tcod

from objects.game_objects.world_map.world_map_object import WorldMapObject


class OpenSea(WorldMapObject):
    type = 'open_sea'

    def __init__(self, name='Open sea', description='This is an open sea', color=tcod.dark_blue, char=None, options={}):
        super(WorldMapObject, self).__init__()
        self.name = name
        self.description = description
        self.color = color
        self.options = options
        self.char = '~'
        self.type = OpenSea.type
