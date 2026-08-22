from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self) -> float:
        pass

    @abstractmethod
    def calculate_area(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def calculate_perimeter(self) -> float:
        return 2 * math.pi * self.radius

    def calculate_area(self) -> float:
        return math.pi * (self.radius ** 2)


class Square(Shape):
    def __init__(self, side: float):
        self.side = side

    def calculate_perimeter(self) -> float:
        return 4 * self.side

    def calculate_area(self) -> float:
        return self.side ** 2


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def calculate_perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def calculate_area(self) -> float:
        return self.width * self.height


if __name__ == "__main__":
    circulo = Circle(5)
    cuadrado = Square(4)
    rectangulo = Rectangle(4, 6)

    figuras = [circulo, cuadrado, rectangulo]

    for figura in figuras:
        print(f"--- {figura.__class__.__name__} ---")
        print(f"Área: {figura.calculate_area():.2f}")
        print(f"Perímetro: {figura.calculate_perimeter():.2f}")