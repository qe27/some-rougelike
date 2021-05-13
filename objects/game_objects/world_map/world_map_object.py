import math

import global_variables


class WorldMapObject:

    def go_to(self):
        vector = (- int(global_variables.player.ship.wm_location[0]) + self.tile.x, - int(global_variables.player.ship.wm_location[1]) + self.tile.y)
        length = math.sqrt(vector[0] * vector[0] + vector[1] * vector[1])
        global_variables.player.ship.direction = (vector[0]/length, vector[1]/length)


    def get_description(self):
        print('description: ' + self.description)

    def __init__(self, name='', description='', color=None, options=[], char=None):
        self.name = name
        self.description = description
        self.color = color
        self.options = options
        self.char = char
        self.tile = None

    def get_funcs(self):
        return {'Go to': self.go_to, 'Get Description': self.get_description}
