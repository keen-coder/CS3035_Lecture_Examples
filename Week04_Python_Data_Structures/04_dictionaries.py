#-------------------------------DICTIONARY BASICS-------------------------------

# A dictionary in Python is a data structure which allows you to store key/value
# pairs, similar to hashmaps or hashtables in other languages.

# Dictionaries are mutable.

# A dictionary is an unordered collection which fetches its values by a given
# key and not with a given index.
#
# The keys and values can be any type
#
# NOTE: items in a dictionary are in a pseudo-random order and are not
# guaranteed to be sorted.

#-------------------------------------------------------------------------------

#-----------------------------CREATING DICTIONARIES-----------------------------

# When creating a dictionary use curly braces { }

# Starting with an empty dictionary and adding one entry at a time.

D = {}
D['name'] = 'Bob'
D['age'] = 40

# Same as above, but in a more concise syntax
D = {'name': 'Bob', 'age': 40}

# Creating a nested dictionary
D = {'employee': {'name': 'Bob', 'age': 40}}

#-------------------------------------------------------------------------------

#-------------------------------FETCHING A VALUE--------------------------------

D = {'name': 'Bob', 'age': 40}
print(D['name']) # prints 'Bob'

D = {'employee1': {'name': 'Bob', 'age': 40}, 'employee2': {'name': 'Mary', 'age': 32}}
print(D['employee1']['age']) # prints 40

#-------------------------------------------------------------------------------

#-------------------LENGTH, MEMBERSHIP, KEYS(), AND VALUES()--------------------

# The len() function will tell you the number of entries
D = {'name': 'Bob', 'age': 40}
print(len(D))   # prints 2

# The 'in' can test if a key exists.
print('age' in D)       # prints True
print('address' in D)   # prints False

# The keys() method returns all of the keys in the dictionary as a list.
print(list(D.keys()))   # prints ['age', 'name']

# The values() method returns all of the values in the dictionary as a list.
print(list(D.values()))

#-------------------------------------------------------------------------------

#------------------------CHANGING DICTIONARIES IN PLACE-------------------------

# Dictionaries are mutable, so they support in-place changes.

D = {'eggs': 3, 'spam': 2, 'ham': 1}

# To change an entry, look up its entry by the key and assign a new value
D['ham'] = 'good'   # dictionaries can mix types
print(D)  # prints {'eggs': 3, 'spam': 2, 'ham': 'good'}

# To delete an entry, use the del operator followed by the dictionary entry
# retrieved by key.
del D['eggs']
print(D)  # prints {'spam': 2, 'ham': 'good'}

# Adding a new entry is as simple as assigning a new value to a new key in the
# same dictionary.
D['brunch'] = 'Bacon'
print(D)  # prints {'spam': 2, 'ham': 'good', 'brunch': 'Bacon'}

#-------------------------------------------------------------------------------

#----------------------DICTIONARY METHODS AND OTHER NOTES-----------------------

# Dictionaries have many other methods you can discover with the help(dict)
# command.

# Other things to NOTE:
#    Sequence operations do not work because a dictionary is a mapping not a
#    sequence and have no inherent ordering.

#    Keys need not always be strings:
#       Anything can be a key except for other mutable objects such as lists,
#       sets, and other dictionaries.
#       Custom classes can be keys if they define the proper protocol methods
#       (have to tell Python their values are 'hashable').  Google for examples.

#-------------------------------------------------------------------------------