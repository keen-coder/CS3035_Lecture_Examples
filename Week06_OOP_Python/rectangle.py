class Rectangle:
    __num_rects = 0

    def __init__(self, width=1.0, height=1.0):
        self.__width = 1.0
        self.set_width(width)
        self.__height = height

    def set_width(self, width):
        if (width <= 0):
            print("ERROR: Width can't be negative or 0.")
            print("Width value not changed.")
        else:
            self.__width = width

    def get_width(self):
        return self.__width

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

    def area(self):
        return self.__width * self.__height

    @staticmethod
    def get_num_rects():
        return Rectangle.__num_rects

    @staticmethod
    def set_num_rects(value):
        Rectangle.__num_rects = value

    def __str__(self):
        # output = 'Rectangle:'
        # output += '\n\tWidth: ' + str(self.__width)
        # output += '\n\tHeight: ' + str(self.__height)
        return f'''Rectangle:
\tWidth: {self.__width}
\tHeight: {self.__height}
'''


    def __repr__(self):
        return f'Rectangle({self.__width}, {self.__height})'
       # return 'Rectangle(' + str(self.__width) + ', ' + str(self.__height) + ')'