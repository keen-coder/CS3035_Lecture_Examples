#https://realpython.com/python-formatted-output/
#https://zetcode.com/python/fstring/
import random
import math


#--------------------------------F-STRING BASICS--------------------------------

# Python 3.6 added a really cool feature called 'f-strings'

# An f-string is a special string that is prepended with the letter f and
# can help you to format the output of a string in many different ways

# Here is an f-string, but without any formatting yet
# You can use single, double, or triple quotes with f-stringsf
# NOTE: The f is OUTSIDE of the quotes

string1 = f'this is a f-string'
string2 = f"this is a f-string"
string3 = f'''this is a f-string'''

# The cool part of f-strings is that you can embed an expression inside of the
# the string, the expression will be evaluated, and its string representation
# will be returned and embedded in the resulting string.


# Embedded expressions must always be surrounded by { }
x = 4.89
y = 55.35

print(f'The value of x is {x} and the value of y is {y}')
# will print The value of x is 4.89 and the value of y is 55.35


#-------------------------------------------------------------------------------

#---------------------------OLD STYLE FORMAT STRINGS----------------------------

# Prior to python 3.6 there were two other ways of formatting strings.

# One was to use the % format type string and the other was the .format() method.

# These have been been superceded by f-strings since f-strings are implemented
# to be much faster to render and have a far simpler syntax.

# Below is a comparison of the three styles.

item = 'crayons'
color = 'green'
amount = 3

old_style1 = 'These %d %s are the color %s' % (amount, item, color)
old_style2 = 'These {} {} are the color {}'.format(amount, item, color)
new_style  = f'These {amount} {item} are the color {color}'

print(old_style1)
print(old_style2)
print(new_style)

#-------------------------------------------------------------------------------

#-------------------------USING EXPRESSION IN F-STRINGS-------------------------

# You can put expressions between the { } in an f-string.

boxes = 10
tissues = 25

print(f'There are a total of {boxes * tissues} in these boxes.')

#-------------------------------------------------------------------------------

#-------------------------DATA STRUCTURES AND F-STRINGS-------------------------

# Data structures can be use in f-strings

list1 = [1, 2, 3, 4, 5]
dict1 = {'name': 'alex', 'age' : 56}

print(f'list1 = {list1}')
print(f'dict1 = {dict1}')

# You can even do indexing, slicing, and other data structure related operations

print(f'list1[::-1] = {list1[::-1]}' )

#-------------------------------------------------------------------------------

#----------------------------FUNCTIONS AND F-STRINGS----------------------------

# Functions can even be called inside of f-strings.

def my_min(list1: list) -> int:

    min: int = list1[0]

    for x in list1:
        if x < min:
            min = x

    return min

list1 = [random.randint(100, 200) for x in range(10)]

print(f'The minimum value in list {list1} is {my_min(list1)}')

#-------------------------------------------------------------------------------

#-----------------------------F-STRINGS AND CLASSES-----------------------------

# As long as your class defines the __str__() or __repr__() methods, your f-string
# can accept an instance of that class type

from my_class import MyClass

mc = MyClass(12, 43)

print(f'mc = {mc}')

#-------------------------------------------------------------------------------

#----------------------FORMATTING NUMBER OF DECIMAL PLACES----------------------

# You can even format the number of decimal places of a floating point value.

# Syntax: f'{value:.#f}' Here # is the number of decimal places

# Will round to the nearest decimal

print(f'{math.pi:.2f}')
print(f'{math.pi:.3f}')
print(f'{math.pi:.4f}')
print(f'{math.pi:.5f}')
#-------------------------------------------------------------------------------

#------------------------FORMATTING WIDTH AND JUSTIFYING------------------------

# You can also specify a minimum width value after the colon in the { }

# If you put a 0 in front of the width, it will pad value with leading 0s

# By default things will be aligned to the left.

for x in range(1, 101):
    print(f'{x:03} {x*x:5} {x*x*x:7}')

# If you want to align things to the right, add a greater than sign after the :
# NOTE: < can be use to left align

for x in range(1, 101):
    print(f'{x:03} {x*x:<5} {x*x*x:<7}')
#-------------------------------------------------------------------------------