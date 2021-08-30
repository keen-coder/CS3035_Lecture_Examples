# Variables in Python are weakly-typed.  Meaning you DO NOT declare the variable
# data type as you would in strongly-typed languages like Java or C++.

# The type of the variable lives with the value (object) NOT with the name.  We
# will talk about this more later.

THIS_IS_A_CONSTANT = 54.732

x = 10
pi = 3.14159265
s1 = 'This is a string in python.'          # single quote string
s2 = "This is also a string in python."     # double quote string

#-------------------------------------------------------------------------------

# Python does not have constants in the way that other languages do.  In python,
# a constant is identified by its name being written in all cap.  There is no
# way to define a constant to enforce that its value can be changed.  All python
# progammers agree to treat any variable name declared in all caps as a constant
# and never change its value.

THIS_IS_A_CONSTANT = 54.732

#-------------------------------------------------------------------------------

# Because variables are weakly-typed in Python, you can technically do the
# following:

a = 32            # Variable 'a' is currently an integer.
a = 50.234812     # Variable 'a' is not a float.
a = 'hello world' # Variable 'a' is now a string.

# However, you should !!!NOT!!! do this.  It makes your code hard to follow,
# maintain, and debug.  This is very frowned upon by fellow python programmers.

#-------------------------------------------------------------------------------

# Integer types in pythong have infinite precision (no limit on size of value)
# However, the larger the values, the longer it will take to perform any
# mathematical operations.
num1 = 58463256586946354576899789687546346385
num2 = 46576896947365236487340597239857588432098472039487543
print(num1 * num2)

#-------------------------------------------------------------------------------

# Float types have double precision (same as double in Java)
f1 = 42.7456787678778876878788787787658765
f2 = 100.57465867
print(f1 * f2)

#-------------------------------------------------------------------------------

# Arithmetic Operators
num3 = 37
num4 = 10

print('37 + 10 =', num3 + num4)   # Addition
print('37 - 10 =',num3 - num4)    # Subtraction
print('37 * 10 =',num3 * num4)    # Multiplication
print('37 / 10 =',num3 / num4)    # Floating-point Division
print('37 // 10 =',num3 // num4)  # Integer Division (Floor Division)
print('37 % 10 =', num3 % num4)   # Remainder Division
print('37 ** 10 =',num3 ** num4)  # Power

# NOTE: Python DOES NOT have ++ or -- operators.

# MIXED-TYPE OPERATIONS
# Operations on two int values, the result will be an int.
# Operations on two float values, the result will be a float.
# Operations on an int and a float, the int value will be temporarily converted
#    to a float and the result of the operation will be a float.

#-------------------------------------------------------------------------------

# Augmented Assignment Operators
x += 10
x -= 10
x *= 10
x /= 10
x //= 10
x %= 10
x **= 10







