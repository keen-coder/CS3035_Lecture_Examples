from class_a import ClassA

class ClassB(ClassA):

    def __init__(self, x: int, text: str, value: float):
        super().__init__(x, text)
        # Alternatively, you can invoke the super class constructor through the
        # class name.  NOTE: That when invoked this way, self must be the first
        # argument in the constructor invocation
        # ClassA.__init__(self, x, text)
        self.__value = value

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value

    def __str__(self):
        to_str = f'{super().__str__()}\n'
        to_str += f'value = {self.__value}'

        return to_str

    def __repr__(self):
        return f'ClassB({repr(super().get_x())}, {repr(super().get_text())}, {repr(self.__value)})'