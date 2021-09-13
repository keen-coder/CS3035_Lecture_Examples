#----------------------------------LIST BASICS----------------------------------

# Python does not have a native array structure as you would find in most other
# languages.

# Python has a list:
#    This is a flexible, ordered collection of objects and can contain any kind
#    of object (even other lists).

# Lists are mutable so they support "in-place changes".

# NOTE: Lists do not need to contain the same type of items, but it is best
# that they do in order to avoid complicated logic / runtime errors.

#-------------------------------------------------------------------------------

#--------------------------------CREATING LISTS---------------------------------

# List literals are creating using square brackets [ ].

# Creating a list of integers.
list1: list = [1, 2, 3]

# Creating a list of strings.
list2: list = ['python', 'lists', 'are', 'fun']

# Creating an empty list.
list3: list = []

# Creating a list of mixed data types.  Typically this should be avoided.
list4: list = [1, 'python', 4.345, [4, 2, 8], True]

#-------------------------------------------------------------------------------

#---------------------LENGTH, CONCATENATION, AND REPETITION---------------------

list1: list = [1, 2, 3]
list2: list = [4, 5, 6, 7]

# Find the length of a list using the built-in length 'len()' function.
print(len(list1))  # prints 3
print(len(list2))  # prints 4

# Lists can be concatenated together using the addition '+' operator
list3: list = list1 + list2
print(list3)  # prints [1, 2, 3, 4, 5, 6, 7]

# Lists can also be repeated using the multiplication '*' operator
list3: list = list2 * 3
print(list3)  # prints [4, 5, 6, 7, 4, 5, 6, 7, 4, 5, 6, 7]

# The repetition operator is great for initializing a list with default values.
list4: list = [0] * 10
print(list4)  # prints [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#-------------------------------------------------------------------------------

#-------------------------LIST MEMBERSHIP AND ITERATION-------------------------

# Lists respond to the same sequence operations as strings.

# The 'in' operator can be used to test membership, if something is contained
# in the list.

list1: list = [42, 6, 1, 78, 100, 92, 38]
print(78 in list1)  # prints True
print(7 in list1)   # prints False

# Typically you use a for loop to iterate over a list.  A for loop in Python
# requires an iterable sequence to iterate over.

for x in list1:
    print(x, end=' ')  # prints 42 6 1 78 100 92 38
print() # print new line character at the end.

sum: int = 0
for x in list1:
    sum += x
print(sum)  # prints 357

#-------------------------------------------------------------------------------

#-----------------------------------INDEXING------------------------------------

# Since lists are iterable structures, they also support indexing.

# Using indexing syntax [index], you can get a value from the list
# The value that you get is whatever type of object lives in the list at the
# requested index
# NOTE: Lists are zero-indexed.
# Negative indexes also work the same as with strings.
list1: list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(list1[6])  # prints 70
print(list1[-6])  # prints 50

# You can even combine the range() function with a for loop to iterate over
# a list using indexing
# NOTE: This is not the preferred way to iterate over a list.  See previous
# example using the in operator.
for i in range(0, len(list1)):
    print(list1[i], end=' ')   # prints 10 20 30 40 50 60 70 80 90 100
print()

#-------------------------------------------------------------------------------

#-------------------------SLICING AND EXTENDED SLICING--------------------------

# Lists also support slicing and extended slicing following the same rules as
# strings.

# Slicing and extended slicing always return a new list that is shallow copied.
# Syntax: list_name[start:end:step]

# See notes on string slicing.

list1: list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print('slicing')
print(list1[:])        # prints [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(list1[4:])       # prints [50, 60, 70, 80, 90, 100]
print(list1[:6])       # prints [10, 20, 30, 40, 50, 60]
print(list1[3:7])      # prints [40, 50, 60, 70]
print(list1[::-1])     # prints [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
print(list1[::2])      # prints [10, 30, 50, 70, 90]
print(list1[1::2])     # prints [20, 40, 60, 80, 100]
print(list1[10:0:-3])  # prints [100, 70, 40]

#-------------------------------------------------------------------------------

#---------------------------------COPYING LISTS---------------------------------

# Return a copy of the list using slicing
# NOTE: This is a shallow copy.  If the list contains immutable data types
# then we do not have to worry about changing the original data.  However, if
# the list contains mutable data, changing the data in the copy will change
# the data in the original.

# This example makes a copy of a list of immutable data using slicing.
list1: list = [10, 11, 12, 13, 14, 15, 16]
result: list = list1[:]  # Slicing to produce a 'shallow copy'
result[2] = 50  # Change the value at index 2, will not affect original.
print('list1:\t', list1)    # prints [10, 11, 12, 13, 14, 15, 16]
print('result:\t', result)  # prints [10, 11, 50, 13, 14, 15, 16]

# This example makes a copy of a list of mutable data using slicing.  Since this
# is a list of lists, and the inner lists themselves are mutable, changes to
# the inner lists in a shallow copy, will make the same changes to all copies.
list1: list = [[1, 2, 3], [4, 5, 6]]
result: list = list1[:]  # Use slicing to create a shallow copy.
result[0][1] = 30
print('list1:\t', list1)    # prints [[1, 30, 3], [4, 5, 6]]
print('result:\t', result)  # prints [[1, 30, 3], [4, 5, 6]]

# If you want to deep copy the data in a list, you will want to use the
# deepcopy() function from the copy module
import copy
list1: list = [[1, 2, 3], [4, 5, 6]]
result: list = copy.deepcopy(list1)  # Use the deepcopy() function.
result[0][1] = 30
print('list1:\t', list1)    # prints [[1, 2, 3], [4, 5, 6]]
print('result:\t', result)  # prints [[1, 30, 3], [4, 5, 6]]

#-------------------------------------------------------------------------------

#----------------------------MULTI-DIMENSIONAL LISTS----------------------------

# Since lists can hold any type of object, that means they can also hold other
# lists.  This is similar to how a multi-dimensional array works in Java where
# a 2D array in Java is just an array of arrays.  In Python they are a list of
# lists.

table: list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Multi-dimensional lists support double indexing just like java.
print(table[1][1])  # prints 5

# You can iterate over a multi-dimensional list using indexing
for row in range(0, len(table)):
    for col in range(0, len(table[row])):
        print(table[row][col], end=' ')
    print()

# A much cleaner approach is to just use the in operator for membership
# and don't use the range() function
for row in table:       # row will hold each inner list as the outer loop iterates
    for col in row:     # col will hold each value of the current row as the inner loop iterates.
        print(col, end=' ')
    print()

#-------------------------------------------------------------------------------

#---------------CHANGING LISTS IN PLACE WITH INDEXING AND SLICING---------------

# Lists can be changed by assigning a single value to a particular index or by
# assigning multiple values to an entire section (slice).

list1 = ['spam', 'Spam', 'SPAM!']

# Assign a new value to the given index
list1[1] = 'eggs'
print(list1)    # prints ['spam', 'eggs', 'SPAM!']

# Assign a slice of values to the corresponding positions
# Make not that this replaces what was already there, it does not do an insertion.
list1[0:2] = ['eat', 'more']
print(list1)    # prints ['eat', 'more', 'SPAM!']

# More Examples:
list1 = [1, 2, 3]
list1[1:2] = [4, 5]
print(list1)    # prints [1, 4, 5, 3]

list1 = [1, 2, 3]
list1[1:1] = [6, 7]
print(list1)    # prints [1, 6, 7, 2, 3]

list1 = [1, 2, 3, 4]
list1[1:3] = []
print(list1)    # prints [1, 4]

list1 = [1, 2]
list1[:0] = [3, 4, 5]
print(list1)    # prints [3, 4, 5, 1, 2]

list1 = [1, 2]
list1[len(list1):] = [3, 4, 5]
print(list1)    # prints [1, 2, 3, 4, 5]

#-------------------------------------------------------------------------------

#---------------------------------LIST METHODS----------------------------------

# The list module has many methods that can be useful for processing lists.

# Look at the help(list) documentation and try the methods out for yourself.

#-------------------------------------------------------------------------------






