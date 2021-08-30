# BOOLEAN LITERALS--------------------------------------------------------------

# Boolean literals in Python are capitalized.
# The literals True and False are special objects that represent the value 0 or 1.
a = False  # False has a value of 0
b = True   # True has a value of 1

#-------------------------------------------------------------------------------

# RELATIONAL OPERATORS-------------------------------------------------------------

# Python supports the following relational operators: >, >=, <, <=, ==, !=
# Returns a value of True or False
x = 10
y = 20

print(x > y)    # Greater than
print(x >= y)   # Greater than or equal to
print(x < y)    # Less than
print(x <= y)   # Less than or equal to
print(x == y)   # Equal to
print(x != y)   # Not equal to

#-------------------------------------------------------------------------------

# LOGICAL OPERATORS AND COMPOUND BOOLEAN EXPRESSIONS----------------------------

# Python supports the following logical operators: and, or, not
# NOTE: Boolean AND and OR both return the OBJECT on the left or right side of the
#   operator, NOT a value of True or False. If the object returned needs further
#   evaluation to True or False, then the object is evaluated to True or False
#   based on its intrinsic True or False value. ***See notes below.
x = 10
y = 20
z = 30
print ((x < y) and (y < z))  # Logical AND, both operands must be true for a true result.
print ((z > x) or (z > y))   # Logical OR, one side must be true for a true result.
print (not (y > z))          # Logical NEGATION, flips true to false and false to true.

# Python also supports compound boolean expressions in the following format:
print(x < y < z)   # Equivalent to (x < y) and (y < z)
print(x > y <= z)  # Equivalent to (x > y) and (y <= z)

#-------------------------------------------------------------------------------

# ADDITIONAL BOOLEAN NOTES-----------------------------------------------------------------

# The built-in function bool() can convert any object to its boolean equivalent.

# ALL Python objects have an intrinsic Boolean value of True or False.

# Any nonzero number or nonempty object is True.
s1 = 'hello world'
print(bool(100))  # Prints True because 100 is a nonzero number
print(bool(s1))   # Prints True because s1 is a nonempty object.

#  Zero numbers, empty objects, the special object None all have a value of False.
s2 = None
s3 = ''
print(bool(0))    # Prints False because 0 is a zero number.
print(bool(s2))   # Prints False because s2 is an empty object.
print(bool(None)) # Prints False because the special object None has a value of False.
print(bool(s3))   # Prints False because s3 is an empty string.

# Comparisons and equality tests are applied recursively to data structures.
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]
list3 = [5, 2, 3, 4, 5]
print(list1 == list2)   # Prints True, applies == operator recursively to each value in the list.
                        # Stops when it reaches the end of the list or the first False is found.
print(list3 > list1)    # Prints True, applies > operator recursively to each value in the list.
                        # Stops when it reaches the end of the list or the first True or False is found.

# Boolean operators stop evaluating (short-circuit) as soon as a result is known.
x = 10
y = 20
z = 10

# The following expression returns True.  However, because of the short-circuit
# behavior, only the left side of the or operator is evaluated.
b1 = (x == z) or (y < z)

# The following expression returns False. However, because of the short-circuit
# behavior, only the left side of the and operator is evaluated.
b2 = (x == y) and (x == z)

# ***Logical operators AND and OR return an OBJECT, NOT a True or False value.
# What the heck does this actually mean?
# The object returned will either be the object on the left side of the operator
# or the right side of the operator. If you test the result of AND or OR in an if
# or other type of statement, the result will be what you expect (since every object
# has a value of True or False).

# Example for OR:
# The or operator is evaluated from left to right, the first object that
# evaluates to true is returned.  If neither object is true, the second object
# is returned.
x = 10
y = 20
z = 10

# This expression will print True. The first expression, (x == 10) is evaluated
# to be True.  Since the left side is True (short-circuit) the left side
# expression is returned and assigned to b1.  So now b1 has the subexpression
# (x == 10). When b1 is printed, (x == 10) is evaluated and will print True.
b1 = (x == 10) or (x == z)
print(b1)

# What happens if we use other types of objects on either side of the or? Here,
# you need to remember the rule that ALL objects in Python have an intrinsic value
# of True or False.  Since a nonempty string evaluates to True, the first object
# is True, therefore the expression is True and the first object is returned.
# The result will print 'hello world'
b2 = 'hello world' or 'python is quirky'
print(b2)
print(bool(b2))

# In this example, we are comparing an empty string with a nonempty string.
# The first operand is False (since empty objects have a value of False in Python),
# So the second operand is returned.  We therefore print 'python is quirky'.
b3 = '' or 'python is quirky'
print(b3)

# NOTE: The AND operator works the same way as far as what gets returned. You can
# study AND on your own.

#-------------------------------------------------------------------------------

# IF / ELSE STRUCTURES------------------------------------------------------------

# Basic if statement:
x = 10
# Note the syntax:
#   No ( ) around the condition.
#   No curly braces.
#   Place a colon after the condition.
#   All statements that belong under the if condition should be properly indented.
if x == 10:
    print('x is 10')

# NOTE if you have a basic if statement with only one line of code following,
# You can write it all on one line.  The previous example can be rewritten as:
if x == 10: print('x is 10')


# if-else statement:
if x == 10:
    print('x is 10')
    print('hello world')
else:
    print('x is not 10')
    print('java is dead to me')

# Multiway if/else statements

# NOTE: The syntax is not else if it is elif
# You can have as many elif block as necessary.
if x == 10:
    print('x is 10')
    print('hello world')
elif x == 20:
    print('something')
elif x == 30:
    print('something')
else:
    print('x is not 10')
    print('java is dead to me')

# Ternary if/else expression:
# This is an inline if/else statement usually used to assign one of two choices
# to a variable.
# Syntax: a = result1 if condition else result2
# This is equivalent to the following:
#    if condition:
#       a = result1
#    else:
#       a = result2

a = 'x is 10' if x == 10 else 'x is not 10'
print(a)