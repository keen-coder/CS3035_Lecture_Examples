class Pair:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def __str__(self):
        return f'({self.__a} , {self.__b})'

    def __repr__(self):
        return f'Pair({self.__a} , {self.__b})'

    def __add__(self, other):
        if isinstance(other, Pair):
            aResult = self.__a + other.__a
            bResult = self.__b + other.__b
            return Pair(aResult, bResult)
        elif isinstance(other, int):
            aResult = self.__a + other
            bResult = self.__b + other
            return Pair(aResult, bResult)

    def __radd__(self, other):
        aResult = self.__a + other
        bResult = self.__b + other
        return Pair(aResult, bResult)

    def __iadd__(self, other):
        if isinstance(other, Pair):
            self.__a += other.__a
            self.__b += other.__b
            return self
        elif isinstance(other, int):
            self.__a += other
            self.__b += other
            return self

    def __gt__(self, other):
        return self.__ge__(other)

    def __ge__(self, other):
        return self.__a >= other.__a and self.__b >= other.__b

    def __neg__(self):
        self.__a *= -1
        self.__b *= -1
        return self

    def __pos__(self):
        if (self.__a < 0):
            self.__a *= -1

        if (self.__b < 0):
            self.__b *= -1

        return self

    def __eq__(self, other):
        return (self.__a == other.__a and self.__b == other.__b)

    def __pow__(self, other):
        self.__a **= other
        self.__b **= other
        return self

    def __getitem__(self, index):
        if index == 0:
            return self.__a
        elif index == 1:
            return self.__b

    def __setitem__(self, index, value):
        if index == 0:
            self.__a = value
        elif index == 1:
            self.__b = value


