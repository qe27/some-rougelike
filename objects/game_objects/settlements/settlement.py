from objects.game_objects.map_object import MapObject


class Settlement(MapObject):

    def __init__(self, name, description, color=None, char=None, options={}):
        super(MapObject, self).__init__()
        self.name = name
        self.description = description
        self.color = color
        self.options = options
        self.char = 'S'
        self.population = options.get('population')
        # if options.get()['population']:
        #     self.population = options['population']
        # else:
        #     self.population = 0
        self.type = 'Settlement'
