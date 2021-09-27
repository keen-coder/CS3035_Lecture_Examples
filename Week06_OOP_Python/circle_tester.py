from circle import Circle

radius = float(input("Enter a radius: "))

circle1 = Circle(radius)

print("radius of Circle is:", circle1.get_radius())

print(circle1)

print(repr(circle1))