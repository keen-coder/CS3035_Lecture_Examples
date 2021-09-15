import random

#------------------------------LIST COMPREHENSIONS------------------------------

# List comprehensions are a concise way to build a list based on applying an
# operation to each element of the list.

# List comprehensions are very powerful and can save you a lot of code if mastered.

# General Syntax: [operation for item in list if condition]
#    operation: an operation you want to apply to every element of the list,
#      the result will be a new item in the result list
#    for item in list: this is a for loop which iterates through a given list.
#      comprehensions can have any number of for loops, each one listed is
#      considered to be "nested" inside of the previous one.
#    if condition: this is an optional clause which will only apply the
#      operation if the condition is met.

# Example: Building a list of random numbers using a loop vs using a comprehension.

# Using a loop:
list1: list = []
total_numbers: int = 10
count: int = 1

while count <= total_numbers:
    list1.append(random.randint(0, 20))
    count += 1

print(list1)

# Using a list comprehension we can shorten the syntax significantly
# Typically when you want to built a list from nothing using comprehension,
# you will need to use the range() function in some way.
list1 = [random.randint(0, 20) for x in range(10)]
print(list1)

# MORE EXAMPLES
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = ['a', 'b']
list3 = ['d', 'e']

# Create a new list where each item is multiplied by 10
result = [x * 10 for x in list1]
print(result)  # prints [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Create a new list with only the odd elements
result = [x for x in list1 if x % 2 != 0]
print(result)  # prints [1, 3, 5, 7, 9]

# Apply one comprehension to two lists like using nested for loops
result = [x + y for x in list2 for y in list3]
print(result)  # prints ['ad', 'ae', 'bd', 'be']

#-------------------------------------------------------------------------------

#--------------------------OPERATIONS USING FUNCTIONS---------------------------

# The operation part of a list comprehension can be the result of any python
# function, or even a custom function that you wrote.

def crazy_case(text: str) -> str:
    result = ''
    count = 1
    for c in text:
        result += c.upper() if count % 2 == 0 else c
        count+=1
    return result

colors = ['cyan','dark magenta', 'cornsilk', 'steel blue', 'green']

result = [crazy_case(color) for color in colors]

print(result)  # prints ['cYaN', 'dArK MaGeNtA', 'cOrNsIlK', 'sTeEl bLuE', 'gReEn']

#-------------------------------------------------------------------------------

#---------------------------------CONDITIONALS----------------------------------

# List comprehensions can have conditions with either an if or if else

# EXAMPLE: Create a list of only even numbers from 2 to 30
list1 = [x for x in range(2, 31) if x % 2 == 0]
print(list1)  # prints [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]

# Multiple if conditions can be used to mean BOTH must be true.
list1 = [5, -10, 6, 20, 50, 21, -42, 46, 11, 31, 101, -1000, 32, 88]
result = [x for x in list1 if x % 2 == 0  if x > 0]

print(result)  # prints [6, 20, 50, 46, 32, 88]

# An if/else type syntax can also be used
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = [(number + 1 if number % 2 == 0 else number - 1) for number in list1 if number > 50]
print(result)  # prints [1, 0, 3, 2, 5, 4, 7, 6, 9, 8]

#-------------------------------------------------------------------------------

#--------------------------NESTED LIST COMPREHENSIONS---------------------------

# You can have nested comprehensions which are usually uses for generating
# multi-dimensional lists.

table = [[j for j in range(5)] for i in range(3)]
print(table)

#-------------------------------------------------------------------------------

# NOTE: There are many more ways to utilize list comprehensions.  We may see
# some of these throughout the semester.  Google and research on your own and
# look at many many examples of how people are using list comprehensions.