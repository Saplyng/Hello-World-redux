class Fish:
    breathes_in_water = True
    skin = "scales"

    def __init__(self, fish_name, fish_color):
        self.name = fish_name
        self.color = fish_color

    def move(self, speed):
        print(self.name + " is moving " + speed + "!")
