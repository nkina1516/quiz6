from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius**2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side**2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

class ShapeCalculator:
    @staticmethod
    def calculate_area(shape):
        area = shape.get_area()
        return round(area, 3)

# Example usage:
circle = Circle(5)
square = Square(4)
rectangle = Rectangle(3, 6)

area = ShapeCalculator.calculate_area(circle)
print(f"The area of the {type(circle).__name__} is: {area}")

area = ShapeCalculator.calculate_area(square)
print(f"The area of the {type(square).__name__} is: {area}")

area = ShapeCalculator.calculate_area(rectangle)
print(f"The area of the {type(rectangle).__name__} is: {area}")