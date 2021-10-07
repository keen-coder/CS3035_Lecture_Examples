import circle
import doctest
from shape import Shape

doctest.testmod(circle)

c1 = circle.Circle(radius=7.5)
c2 = Circle(radius=7.5)

print(c2.compare_to(c1))