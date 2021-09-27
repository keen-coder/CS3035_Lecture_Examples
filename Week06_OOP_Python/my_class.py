class MyClass:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def __add__(self, other):
        a_sum = self._a + other._a
        b_sum = self._b + other._b

        return MyClass(a_sum, b_sum)

    def __sub__(self, other):
        a_diff = self._a - other._a
        b_diff = self._b - other._b

        return MyClass(a_diff, b_diff)

    def __str__(self):
        return f'({self._a}, {self._b})'


















