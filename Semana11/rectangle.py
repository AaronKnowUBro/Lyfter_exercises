class Rectangle:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Negative value exists. Width and height must be positive numbers.")
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height) 

def width_input():
    print ("Please enter the width of the rectangle: ")
    return float(input())

def height_input():
    print ("Please enter the height of the rectangle: ")
    return float(input())

try:
    width = width_input()
    height = height_input()
    rectangle = Rectangle(width, height)
    print("Area of the rectangle:", rectangle.get_area())
    print("Perimeter of the rectangle:", rectangle.get_perimeter())
except ValueError as e:
    print("Error:", e)