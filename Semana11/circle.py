import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius ** 2)

c = Circle(10)
print("Área del círculo:", c.get_area())