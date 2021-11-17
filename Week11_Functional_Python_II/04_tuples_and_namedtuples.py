# This example shows how effective named tuples can be for making your code more
# eplicit.

# Scenario: You want to work with color values that are made up of RGB values.
# RGB stands for red, green, and blue and each has a value ranging from 0 to 255.
# When the RGB values are combined using light from pixels, they generate the colors
# that we visually see on a monitor.

# We could store our RGB values in a three-tuple as follows:

color1 = (0, 0, 0) # black
color2 = (0, 255, 255) # cyan
color3 = (50, 205, 50) # limegreen

# To chose the red, green, or blue value from these tuples, we can use basic
# indexing syntax.

print("red = ", color3[0])
print("green = ", color3[1])
print("blue = ", color3[2])

# This of course can be tedious and when used throughout your code it may not always
# be clear what exactly name[index] means within the logic of the code.

# We can of course help to make the code more readible by creating lambda functions
# to choose an RGB value from our three-tuples

red = lambda color: color[0]
green = lambda color: color[1]
blue = lambda color: color[2]

# This allows us to do the following:
print("red = ", red(color3))
print("green = ", green(color3))
print("blue = ", blue(color3))

# A better way might be to use an old style namedtuple from the collections module

from collections import namedtuple

# the syntax for creating a namedtuple is as follows
# namedtuple('tuple_name', 'value1_name value2_name ... value3_name'))
# Example:

Color = namedtuple('Color', 'red green blue color_name')

# Now we can create colors using our named tuple
color1 = Color(0, 0, 0, 'black')
color2 = Color(0, 255, 255, 'cyan')
color3 = Color(50, 205, 50, 'lime green')

# If we print the tuple, we get a nice looking output:
print(color3) # prints Color(red=0, green=0, blue=0, color_name='black')

# We can also access each value of the tuple using dot operator syntax:
print(color3.red)
print(color3.green)
print(color3.blue)
print(color3.color_name)

# Yet another technique we can use is the NamedTuple class from the typing module

from typing import NamedTuple

class Color(NamedTuple):
    red: int
    green: int
    blue: int
    color_name: str

# And now we can create and use this NamedTuple the same way as the previous example

color1 = Color(0, 0, 0, 'black')
color2 = Color(0, 255, 255, 'cyan')
color3 = Color(50, 205, 50, 'lime green')

print(color3)

print(color3.red)
print(color3.green)
print(color3.blue)
print(color3.color_name)











