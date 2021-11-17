# The map() function can be used to apply a given function to each value of an
# iterable.

L = [1, 2, 3, 4, 5]

def mult10(x):
    return x * 10

# NOTE that the map function returns a lazily-evaluated iterator.  If you want
# to iterate over the result you can use a for loop or the next() function.
result = map(mult10, L)

print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

# You can also take the iterator and convert it to a list, set, or other iterable
result = list(map(mult10, L))

print(result)

# You can also supply a lambda function to map()

result = list(map(lambda x: x * -1, L))
print(result)

# You can also use multiple iterables.  Make sure that the function you give
# to map accepts a parameter for each iterable.

planet_names = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_radii_km = [2440, 6052, 6371, 3390, 69911, 58232, 25362, 24622]
planet_avg_temp_f =[800, 880, 61, -20, -218, -320, -331, -218]


def format_data(name, radius, temp):
    return name + ": Radius = " + str(radius) + "km, AvgTemp = " + str(temp) + "F"

result = map(format_data, planet_names, planet_radii_km, planet_avg_temp_f)

for data in result:
    print(data)











