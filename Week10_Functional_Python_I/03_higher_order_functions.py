#----------------------------HIGHER-ORDER FUNCTIONS-----------------------------

# Demonstrates how the builtin max() function is a higher order function and
# how it behaves can be modified by supplying another function as an argument

# Data to process
# A list of tuples of (year, avg rainfall in inches)
# NOTE: This data is made up and is not accurate

year_rainfall = [(2000, 29.87), (2001, 30.12), (2002, 30.6), (2003, 30.66),
                 (2004, 31.33), (2005, 32.62), (2006, 32.73), (2007, 33.5),
                 (2008, 32.84), (2009, 33.02), (2010, 32.92)]

# The built-in max() function can be applied to the data to return the tuple
# with the maximum year.
# The default behavior is to return the tuple that has the maximum value in
# tuple[0] (tuple position 0)
print(max(year_rainfall)) # will print (2010, 32.92)

# The max() function is a higher order function and will allow us to supply another
# function as an argument, thus changing the behavior of how the max function
# computes its output.

# We can supply the function in three ways:
#  1. An inline lambda function (the function is passed directly into the max() function)
#  2. First assigning the lambda to a name and then passing the name to max()
#  3. Creating a def function instead of a lambda and passing the name of the def
#     to the max() function.

# Using an inline lambda function
max_result1 = max(year_rainfall, key=lambda data: data[1])
print(max_result1) # prints (2007, 33.5)

# Assigning the lambda to a name
max_by_rainfall1 = lambda data: data[1]
max_result2 = max(year_rainfall, key=max_by_rainfall1)
print(max_result2) # prints (2007, 33.5)

# Using a def function
def max_by_rainfall2(data):
    return data[1]

max_result3 = max(year_rainfall, key=max_by_rainfall2)
print(max_result3) # prints (2007, 33.5)


















#-------------------------------------------------------------------------------