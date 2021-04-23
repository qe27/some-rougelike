import tcod

from objects.game_objects.map_object import MapObject


class Plain(MapObject):

    def __init__(self, name='Great plains', description='Great plains description', color=tcod.green, char=None, options={}):
        super(MapObject, self).__init__()
        self.name = name
        self.description = description
        self.color = color
        self.options = options
        self.char = '"'
        self.type = 'Plain'
