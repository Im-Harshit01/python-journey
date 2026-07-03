# A practice area calculator which uses the basics of OOPs 

import math


class Shape:

    def __init__(self):
        pass

    def get_area(self):
        """Calculates and returns the area of the shape."""
        raise NotImplementedError("Subclasses must implement this method")


class Circle(Shape):

    def __init__(self, radius):
        super().__init__()  # Initializes the parent Shape class
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius**2)


class Rectangle(Shape):

    def __init__(self, width, height):
        super().__init__()  # Initializes the parent Shape class
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


class Square(Rectangle):

    def __init__(self, side):
        # Passes the side length as both width and height to Rectangle
        super().__init__(side, side)


class Triangle(Shape):

    def __init__(self, base, height):
        super().__init__()  # Initializes the parent Shape class
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height


# Execution Block
if __name__ == "__main__":
    shapes = [
        Circle(radius=5),
        Rectangle(width=4, height=6),
        Square(side=4),
        Triangle(base=3, height=8),
    ]

    for shape in shapes:
        print(
            f"{shape.__class__.__name__} Area: {shape.get_area():.2f}"
        )
