#-----------------------------FIRST-CLASS FUNCTIONS-----------------------------

# Recall the def statement is used to create / define a function.  In python,
# this actually creates a function OBJECT.
def example(a, b, **kwargs):
    return a*b

# The following prints '<class 'function'>' indicating that example belongs to
# the object type 'function'
print(type(example))

# We can also get a list of the parameters to the function
print(example.__code__.co_varnames) # prints ('a', 'b', 'kwargs')

# We can also get the number of arguments
print(example.__code__.co_argcount) # prints 2

# NOTE this example doesn't really teach us anything new about functional
# programming in Python.  It is merely to demonstrate that functions are first-class
# citizens of the language and can be manipulated just like other objects.  Any
# functional language requires this to be true.

#-------------------------------------------------------------------------------

mersenne = lambda x: 2**x - 1