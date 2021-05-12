class Ship:

    def __init__(self, hp, defence, model, speed):
        self.max_hp = hp
        self.current_hp = hp
        self.defence = defence
        self.model = model
        self.speed = speed
