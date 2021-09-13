#-----------------------------THE RANGE() FUNCTION------------------------------

# The range() function can generate an iterable collection of numbers on the fly.

# Syntax: range(start, stop, step)
#    start: optional, integer specifying the start position, default 0
#    stop: integer specifying the end position (non-inclusive)
#    step: optional, integer specifying the incrementation, default 1

# The range function returns a range() object NOT a list
result = range(1, 10)
print(result)  # prints range(1, 10)

# Examples:
for x in range(10):
    print(x, end=' ') # prints 0 1 2 3 4 5 6 7 8 9
print()

for x in range(42, 64, 2):
    print(x, end=' ') # prints 42 44 46 48 50 52 54 56 58 60 62
print()

# As shown in the lists.py examples, you can use the range function to mimic a
# more traditional for loop using an iteration variable

# Iterating over a list using range and an iteration variable
# NOTE This is not the 'pythonic' way to iterate over a list.
list1 = ['a', 'b', 'c', 'd', 'e']

for i in range(0, len(list1)):
    print(list1[i], end=' ')  # print a b c d e
print()

# range() can be used to generate a list
# here we use the list() function to convert the range() object into a list

list1 = list(range(23, 37))
print(list1)  # prints [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]

#-------------------------------------------------------------------------------