# The following is from using help(print):
# print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

# Prints the values to a stream, or to sys.stdout by default.
# Optional keyword arguments:
# file: a file - like object(stream); defaults to the current sys.stdout.
# sep: string inserted between values, default a space.
# end: string appended after the last value, default a newline.
# flush: whether to forcibly flush the stream.

# The print function can print any literal or variable value.
x = 10
print(x)
print('hello world')

# The print function can take a comma-separated list of values and will print
# these values concatenated together with a separator character.  The default
# separator character is a space ' '.
print(1, 2, 3, 4, 5)
a = 'hello'
b = 'world'

print(a, b)

# You CAN use the + operator to concentate values together for output.  However,
# Python does not allow implicit conversion of objects from one type to another.
# You must use one of the builtin conversion functions.
result = 42
print('The result is: ' + result) # This line will cause a runtime error.
print('The result is: ' + str(result)) # Notice the str().

# Other conversion functions int() and float()

# The newline character can be suppressed or changed to any other character.

# Printing all values on one line.  We are using the end parameter and assigning
# it a new character (the empty string).
print(1, end='')
print(2, end='')
print(3, end='')

# You can also change the separator character using the sep argument.
area_code = 323
prefix = 343
suffix = 5555
print(area_code, prefix, suffix, sep='-')











