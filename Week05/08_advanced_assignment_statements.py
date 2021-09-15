#------------------------------SEQUENCE ASSIGNMENT------------------------------

# The values inside of a tuple or list can be assigned to a series of variables
# based on position of the variables / values
#
# Two terms to consider: packing (taking a bunch of separate values and
# combining them into a sequence) and unpacking (taking a sequence of values
# and assigning them to individual variables)

# Positional tuple assignment (unpacking)
spam, ham = ('yum', 'Good')

# Positional list assignment (unpacking)
[spam, ham] = ['yum', 'Good']

# Works with strings too (really any iterable object)
a, b, c = "123"

# The number of variables on the left, must match the number of variables on the
# right.

# The following produces a compile error
a, b = [1, 2, 3]

# This works too
string = 'SPAM'
a, b, c, d = string

#-------------------------------------------------------------------------------

#--------------------------EXTENDED SEQUENCE UNPACKING--------------------------

# What if you don't have enough variables on the left-hand side? Normally this
# is a compile error, unless you specify otherwise.

# A variable with a single * in front of the name can "collect" any extra values
# not assigned to other variables.

L = [1, 2, 3, 4]

a, *b = L
print(a)    # prints 1
print(b)    # prints [2, 3, 4]

*a, b = L
print(a)    # prints [1, 2, 3]
print(b)    # prints 4

a, *b, c = L
print(a)    # prints 1
print(b)    # prints [2, 3]
print(c)    # prints 4

a, b, *c = L
print(a)    # prints 1
print(b)    # prints 2
print(c)    # prints [3, 4]

#-------------------------------------------------------------------------------

#------------------EXTENDED SEQUENCE UNPACKING, COMMON ERRORS-------------------

# The following are some common errors with extended sequence unpacking

seq = '1234'

# SyntaxError: two starred expressions in assignment
# You are only allowed to have one starred expression
a, *b, c, *d = seq

# ValueError: too many values to unpack (expected 2)
# Not enough single variables on the left to fully unpack the sequence on the right.
a, b = seq

# SyntaxError: starred assignment target must be in a list or tuple.
# The variables on the left must be part of a list or tuple.
*a = seq

# The previous error can be fixed by the following
*a, = seq

#-------------------------------------------------------------------------------