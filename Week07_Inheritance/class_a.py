class ClassA:

    def __init__(self, x: int, text: str):
        self.__x = x
        self.__text = text

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_text(self):
        return self.__text

    def x_plus_ten(self):
        self.__x += 10

    def __str__(self):
        return f'x = {self.__x}, text = {self.__text}'

    def __repr__(self):
        return f'ClassA({repr(self.__x)}, {repr(self.__text)})'





