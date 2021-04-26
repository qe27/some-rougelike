class Structure:

    def __init__(self, name, description, color=None, char=None, options=[], map_object=None):
        self.name = name
        self.description = description
        self.char = char
        self.color = color
        self.options = options
        self.map_object = map_object

    def get_object_description(self):
        return {'Change name': self.change_name, 'Get description': self.get_description_function}

    def change_name(self):
        print('change name function was called')

    def get_description_function(self):
        print('get description function was called')