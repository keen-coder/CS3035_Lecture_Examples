from abc import ABC, abstractmethod

class Shape(ABC):
    # dunder = double underscore
    def __init__(self, color='grey', is_filled=False):
        self.__color = color;
        self.__is_filled = is_filled;

    def get_color(self):
        return self.__color

    @abstractmethod
    def area(self):
       pass

    def __str__(self):
        return f'color = {self.__color}, is_filled = {self.__is_filled}'







