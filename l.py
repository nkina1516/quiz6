from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def getArea(self):
        pass

class CalculateArea(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape, CalculateArea):
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        print("Calculating the area of a circle")
        return self.calculate_area()

    def calculate_area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape, CalculateArea):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        print("Calculating the area of a rectangle")
        return self.calculate_area()

    def calculate_area(self):
        return self.width * self.height

class Triangle(Shape, CalculateArea):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def getArea(self):
        print("Calculating the area of a triangle")
        return self.calculate_area()

    def calculate_area(self):
        return 0.5 * self.base * self.height

class Polygon(Shape):
    def __init__(self, sides, length):
        self.sides = sides
        self.length = length

    def getArea(self):
        print("Equation to find area of this polygon is unknown")

def calculateArea(shape):
    if isinstance(shape, Shape):
        return shape.getArea()
    else:
        print("This shape doesn't have a calculable area.")

circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 4)
polygon = Polygon(6, 5)

print(calculateArea(circle))  # Prints the area of the circle
print(calculateArea(rectangle))  # Prints the area of the rectangle
print(calculateArea(triangle))  # Prints the area of the triangle
calculateArea(polygon)  # Prints the message about unknown area calculation
