import functools

# An easy example of showing how the reduce function works is by applying the
# sum to an entire list.

# Reduce can take a defined function, built-in, or lambda.

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def my_sum(x, y):
    return x + y

# Remember that reduce returns a single value

result = functools.reduce(my_sum, L, 0)
print(result)

# Example Check if all values are True or False
L = [True, True, True, True]
result = functools.reduce(lambda x, y: x and y, L)
print(result)

L = [False, False, False, False]
result = functools.reduce(lambda x, y: not x and not y, L)
print(result)

# Using reduce to find the maximum:
L = [386, 25, 1024, 732, 14, 8, 6085, 201, 72]
print(functools.reduce(lambda x, y: x if x > y else y, L))
