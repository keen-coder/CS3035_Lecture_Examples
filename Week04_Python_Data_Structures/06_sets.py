#----------------------------------SET BASICS-----------------------------------
# A python set is an unordered collection of unique and immutable objects that
# supports operations corresponding to mathematical set theory.

# Sets cannot have duplicate items no matter how many times a duplicate item is
# added to the set.

# Sets are mutable, iterable, and can grow or shrink depending on the needs
# of the program.

# Sets may only contain immutable object types.

# Sets in Python 3.X also support comprehensions.

#-------------------------------------------------------------------------------

#---------------------------------CREATING SETS---------------------------------

# Newer syntax in Python 3.X
S = {1, 2, 3, 4, 5}

# Older Syntax
S = set([1, 2, 3, 4, 5])

# Creating an empty set must use the set() function no matter the version of Python
S = set()

#-------------------------------------------------------------------------------

#--------------------------------SET OPERATIONS---------------------------------

S1 = {1, 2, 3}
S2 = {2, 3, 4}

# Set Union
print(S1 | S2)     # prints {1, 2, 3, 4}

# Set Intersection
print(S1 & S2)     # prints {2, 3}

# Set Difference
print(S1 - S2)     # prints {1}
print(S2 - S1)     # prints {4}

# Superset
print(S1 > S2)     # prints False

# Subset
print(S1 < S2)     # prints False

#-------------------------------------------------------------------------------

#----------------------------------SET METHODS----------------------------------

# use help(set) to see functions in the set module.

#-------------------------------------------------------------------------------