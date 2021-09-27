import math

class Circle:
    __number_of_circles = 0

    def __init__(self, radius=1.0):
        self.__radius = radius
        Circle.__number_of_circles += 1

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        if radius > 0:
            self.__radius = radius
        else:
            print('Radius cannot be negative. Value unchanged.')

    def area(self):
        return math.pow(self.__radius, 2) * math.pi

    def __str__(self):
        output = 'Circle:\n'

        output += '\tRadius: ' + str(self.__radius)
        output += '\n\tArea: ' + str(self.area())
        output += '\n\tNum Circles: ' + str(Circle.__number_of_circles)

        return output

    def __repr__(self):
        return 'circle.Circle(' + str(self.__radius) + ')'

    @staticmethod
    def get_number_of_circles():
        return Circle.__number_of_circles