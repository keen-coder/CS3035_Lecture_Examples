#---------------------------------TUPLE BASICS----------------------------------

# Tuples are a simple grouping of objects, an ordered collection of arbitrary
# objects

# Work just like lists, but tuples are immutable.

# Usually written as a series of items in parenthesis ()

# Accessed by indexes

#-------------------------------------------------------------------------------

#--------------------------------CREATING TUPLES--------------------------------

# Creating an empty Tuple
T = ()

# A one-item Tuple
# Without the comma this would simply be an expression
T = (7,)

x = (7)

# A four-item Tuple
T = (7, 'Ni', 1.2, 'Holy Hand Grenade')

# Nested Tuples
T = ('Knights', ('Monty', 'Python'))

# Converting an iterable to a Tuple using the tuple() function
T = tuple('spam')

#-------------------------------------------------------------------------------

#----Creating a List of Tuple------

characters = ['a', 'b', 'c', 'd']
values = [4.657, 90.723, 20.456, 31.78]

result = []

for index in range(len(characters)):
    result.append( (characters[index], values[index]) )

for item in result():
    print(item)

#----------------------------OTHER TUPLE OPERATIONS-----------------------------

# Tuples support concatenation, repetition, indexing, and slicing.
# remember, since tuples are immutable, any of these operations would return a
# new tuple in memory.

# For a look at the functions tuples have, use the command help(tuple).

#-------------------------------------------------------------------------------