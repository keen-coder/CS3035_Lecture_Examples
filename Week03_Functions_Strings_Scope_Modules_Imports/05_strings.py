# STRING BASICS-----------------------------------------------------------------

# Strings in python are immutable.

# String Literals:
#   strings are created by surrounding a sequence of characters in either
#   single quotes '' or double quotes ""
#   the convention seems to be to use single quotes
#   either one does not matter they both produce the same string

#-------------------------------------------------------------------------------

# ESCAPE SEQUENCES--------------------------------------------------------------

# Python has escape characters (sequences) just like other langauges.
# See the linked page on canvas for a full list.

#-------------------------------------------------------------------------------

# LENGTH OF A STRING------------------------------------------------------------

# Python has a built in len() function to find the length of an object.
# len() works on strings as well as other data structures.

# Example:
s1 = 'Monty'
s2 = 'Python'

print(len(s1))  # length is 5
print(len(s2))  # length is 6

#-------------------------------------------------------------------------------

# STRING CONCATENATION AND REPETITION-------------------------------------------

# + concatenates two strings
#   NOTE: if one of the operands is not a string, you will need to convert
#   the nonstring to a string using the str() conversion function.

# * can be used to repeat a string.

# Example:
s1 = 'Monty'
s2 = 'Python'
num = 10

s3 = s1 + ' ' + s2    # is 'Monty Python'
s4 = 'result is ' + str(num)

print(s1 * 3)         # prints MontyMontyMonty

#-------------------------------------------------------------------------------

# ITERATING OVER A STRING AND MEMBERSHIP----------------------------------------


#-------------------------------------------------------------------------------
# The in operator can be used to test whether or not an item is a substring
# of a string.
#   returns True or False depending on if the substring is found or not.

# It can also be used with a for loop to iterate over each character of a string.

# Example:

s1 = 'Monty'
s2 = 'Python'

print('ont' in s1)  # prints True
print('ont' in s2)  # prints False

for c in s1:
    print(c, end=' ')  # prints 'M o n t y'

