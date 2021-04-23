import tcod

from objects.game_objects.map_object import MapObject


class Settlement(MapObject):

    def __init__(self, name='Moscow', description='Test Description', color=tcod.red, char=None, options={}):
        super(MapObject, self).__init__()
        self.name = name
        self.description = description
        self.color = color
        self.options = options
        self.char = 'S'
        self.population = options.get('population')
        self.type = 'Settlement'
