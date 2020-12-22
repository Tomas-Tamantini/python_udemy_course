from abc import ABC, abstractmethod
from math import pi


class PlanarShape(ABC):

    @property
    @abstractmethod
    def perimeter(self):
        return

    @property
    @abstractmethod
    def area(self):
        return

    def __str__(self):
        return f'\tArea: {self.area}\n\tPerimeter: {self.perimeter}'


class Rectangle(PlanarShape):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height

    @property
    def perimeter(self):
        return 2 * (self._width + self._height)

    def __str__(self):
        return f'Attributes:\n\tWidth: {self._width}\n\tHeight: {self._height}\n' + super().__str__()


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(width=side_length, height=side_length)

    def __str__(self):
        return f'Attributes:\n\tSide length: {self._width}\n' + PlanarShape.__str__(self)


class Circle(PlanarShape):
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return pi * self._radius * self._radius

    @property
    def perimeter(self):
        return 2 * pi * self._radius

    def __str__(self):
        return f'Attributes:\n\tRadius: {self._radius}\n' + super().__str__()
