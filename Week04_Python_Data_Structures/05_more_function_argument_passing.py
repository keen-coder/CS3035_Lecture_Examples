#-----------------------FUNCTION ARGUMENT PASSING BASICS------------------------

# Arguments are automatically passed to local variable names (parameters) in the
# function parameter list.

# Recall, everything in python is an object so there really is no sense of
# pass-by-value or pass-by-reference. but the concept is similar:

# If an object is immutable it is LIKE pass-by-value, changing the object inside
# of the function will not change the object outside of the function.

# If an object is mutable, it is LIKE pass-by-reference, changing the object
# inside of the function WILL change the object outside of the function.

#-------------------------------------------------------------------------------

#----------------------PREVENTING MUTABLE ARGUMENT CHANGES----------------------

# If you want to prevent any changes to a mutable object inside your function,
# you should pass an explicit copy of the object to the function.
# Example:
def change(list):
    list[0] = 10

# If the list contains immutable objects, you can use slicing to pass a copy.
L = [1, 2, 3]
change(L[:]) # [:] makes a copy of the list

# If the list contains mutable objects, use the deep copy method from the copy
# module.
import copy
change(copy.deepcopy(L))

# You could also make a copy of the parameter inside of the function
def change(list):
	list_copy = copy.deepcopy(list)

L = [1, 2, 3]
change(L)

#-------------------------------------------------------------------------------

#--------------------FUNCTION PARAMETERS WITH DEFAULT VALUES--------------------

# Normal function parameters can be given default values in the function header.

# If a function is called without enough arguments to fill all of the parameters
# (from left to right), the default value will be used.

# Function definition with default values for each parameter
def f(a=5, b=6, c=7):
    print(a, b, c)

f()            # Displays 5, 6, 7
f(1)           # Displays 1, 6, 7
f(1, 2)        # Displays 1, 2, 7
f(1, 2, 3)     # Displays 1, 2, 3

#-------------------------------------------------------------------------------

#-------------------------------KEYWORD ARGUMENTS-------------------------------

# When you call a function, you can also use key / value pairs as arguments.

# These have the form parameter_name = value

# When used in this way you can pass arguments in any order and the value of
# the argument will be matched to the name.

# NOTE: This type of argument passing can also have default values for the parameters.

#function definition
def f(a=5, b=6, c=7):
    print(a, b, c)

#function calls
f(a=1, b=2, c=3)   # Displays 1, 2, 3
f(c=3, a=1, b=2)   # Displays 1, 2, 3
f(1, c=3)          # Displays 1, 6, 3

#-------------------------------------------------------------------------------

#-------------THE *ARGS PARAMETER (VARIABLE LENGTH PARAMETER LISTS)-------------


# Functions can also have a single parameter with an asterisk in front of the
# parameter name.

# The convention is to call this parameter *args.

# This parameter is similar to a variable-length parameter list in Java
# (the ... parameter), and allows you to specify any number of arguments to
# your function.
#
# This special parameter collects any unmatched parameters/arguments and stores
# them in a Tuple (more on these later).

# A Tuple can be accessed with many of the same features as a list.

def f(*args):
    for y in args:
        print(y, end=' ')
    print()

f()            # Displays nothing
f(1)           # Displays 1
f(1, 2)        # Displays 1, 2
f(1, 2, 3)     # Displays 1, 2, 3
f(1, 2, 3, 4)  # Displays 1, 2, 3, 4

#-------------------------------------------------------------------------------

#----------------------------THE **KWARGS PARAMETER-----------------------------

# Functions may also have a single parameter with a double asterisk in front of
# the parameter name.

# This special parameter will accept any number of key/value pairs and pass them
# to the function as a dictionary.

# Conventionally, this parameter has the name **kwargs

def f(**kwargs):
    print(kwargs)

#function call
f(a=1, b=2, c=3)  # prints {'b': 2, 'a': 1, 'c': 3}
#-------------------------------------------------------------------------------

#----------------------------------OTHER NOTES----------------------------------

# With a list and dictionary, you have two ways to pass these items to a
# function.
#    1. You can either pass them as a whole data structure
#    2. You can unpack the items of the data structure into individual
#    parameters (each item becomes its own argument to a function)

# use * before the argument name for list in the function call

# use ** before the argument name for a dictionary in the function call

def f(a, b, c):
    print(a, b, c)

list1 = [1, 2, 3]
D = {'a' : 1, 'b' : 2, 'c' : 3}

f(*list1)  # prints 1, 2, 3
f(**D)     # prints 1, 2, 3
#-------------------------------------------------------------------------------

#----------------------COMBINING DIFFERENT PARAMETER TYPES----------------------

# You can mix and match all of these different types of parameters in a function
# definition or call. The order they must appear is very important.

# For a function header / definition parameters must appear in this order:
#    1. any normal parameters (positional parameters) (name)
#    2. any default parameters (name=value)
#    3. variable-length parameter (*name)
#    4. variable-length keyword parameter (**name)

# For a function call arguments must appear in this order:
#    1. any positional arguments (name)
#    2. any keyword arguments (name=value)
#    3. the unpacking list argument (*name)
#    4. the unpacking dictionary argument (**name)

# Example function with all types in the correct order
def f(a, b, c=10, s1='python', *args, **kwargs):
    pass

# Example function call with all types in the correct order
def my_function(a, b, c, s1, e, f, g, x, y, z):
    print(a, b, c, s1, e, f, g, x, y, z)

list1 = [11, 12, 13]
D = {'x': 8000, 'y': 9000, 'z': 10000}

my_function(7, 42, s1='java', c=77, *list1, **D)
#-------------------------------------------------------------------------------