# The filter() function takes a function and an iterable, and returns an iterator
# that contains only the values that pass the the true / false test of the given
# function.

# Just like other higher order functions we can pass a predefined function
# a built-in, or a lambda to filter().

def is_cube(x):
    return round(x ** (1 / 3)) ** 3 == x

L = [1, 6, 8, 9, 15, 27, 42, 49, 56, 64, 75, 79, 90, 100, 113, 125]

result = filter(is_cube, L)

for x in result:
    print(x, end=" ")
print()

# You can also give the keyword None as the argument for the function in the filter()
# function.  This will filter out any values that python considers to be "false"

# Remember, that all object have an intrinsic value of True or False in Python

L = [5, -23, "", True, False, 0, 0.0, {}, []]

result = filter(None, L)
print(list(result))

# Example for class map each Planet data to a dictionary, put them in a list
# filter planets by temperature.

planet_names = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_radii_km = [2440, 6052, 6371, 3390, 69911, 58232, 25362, 24622]
planet_avg_temp_f =[800, 880, 61, -20, -218, -320, -331, -218]

def to_dictionary(name, radius, temp):
    return {'name' : name, 'radius' : radius, 'temp' : temp}

def hot_planets(planet_info):
    if (planet_info['temp'] > 0):
        return True
    else:
        return False

result = filter(hot_planets, map(to_dictionary, planet_names, planet_radii_km, planet_avg_temp_f))

# Alternatively you can break it up over multiple lines:

# map_result = map(to_dictionary, planet_names, planet_radii_km, planet_avg_temp_f)
# filter_result = filter(hot_planets, map_result)

for r in result:
    print(r)