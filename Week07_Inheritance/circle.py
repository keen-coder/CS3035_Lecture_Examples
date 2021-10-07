from shape import Shape
import math
from comparable import Comparable
import doctest

class Circle(Shape, Comparable):

    def __init__(self, color='grey', is_filled=False, radius=1.0):
        super().__init__(color, is_filled)

        # Shape.__init__(self, color, is_filled)
        self.__radius = radius

    def area(self):
        """

        Examples:
            >>> Circle.area()
            >>> c.area()
            5.6
        """
        return math.pi * math.pow(self.__radius, 2)

    def compare_to(self, other):
        if self.__radius == other.__radius:
            return 0
        elif self.__radius < other.__radius:
            return -1
        else:
            return 1

    def __str__(self):
       return f'{super().__str__()}, radius = {self.__radius}'

if __name__ == '__main__':
    doctest.testmod()