class WorldMapObject:

    def __init__(self, name='', description='', color=None, options=[], char=None):
        self.name = name
        self.description = description
        self.color = color
        self.options = options
        self.char = char

    def go_to(self):
        print('going to object')

    def get_description(self):
        print('description: ' + self.description)

    get_funcs = {'Go to': go_to,
                 'Get Description': get_description}
