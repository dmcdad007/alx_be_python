# polymorphism_demo.py

import math

class Shape:
    """Base class representing a generic shape."""

    def area(self):
        """Calculate the area of the shape.
        This method should be overridden by derived classes."""
        raise NotImplementedError("Subclasses must override the area() method.")


class Rectangle(Shape):
    """Derived class representing a rectangle."""

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Return the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    """Derived class representing a circle."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return math.pi * (self.radius ** 2)
