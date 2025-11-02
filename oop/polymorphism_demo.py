# polymorphism_demo.py

import math

# Base class
class Shape:
    """Base class for all shapes."""

    def area(self):
        """Calculate the area of the shape. Must be overridden by derived classes."""
        raise NotImplementedError("Subclasses must implement this method")


# Derived class - Rectangle
class Rectangle(Shape):
    """Rectangle shape with length and width."""

    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        """Calculate area of rectangle: length * width"""
        return self.length * self.width


# Derived class - Circle
class Circle(Shape):
    """Circle shape with a radius."""

    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        """Calculate area of circle: π * r^2"""
        return math.pi * self.radius ** 2


from polymorphism_demo import Shape, Rectangle, Circle

def main():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()
