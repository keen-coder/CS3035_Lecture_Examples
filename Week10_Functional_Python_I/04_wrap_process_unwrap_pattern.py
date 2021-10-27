#--------------------------WRAP-PROCESS-UNWRAP PATTERN--------------------------

# This example tries to demonstrate the wrap, process, unwrap design pattern

# NOTE: In this example we use the map() built-in function. The map() function
# returns a map object (which is an iterator) containing the results.  The map()
# function applies a given function to each piece of data.

year_rainfall = [(2000, 29.87), (2001, 30.12), (2002, 30.6), (2003, 30.66),
                 (2004, 31.33), (2005, 32.62), (2006, 32.73), (2007, 33.5),
                 (2008, 32.84), (2009, 33.02), (2010, 32.92)]

# The following line of code prints out the max average rainfall value by using
# the prescribed design pattern
print( max(map(lambda data: (data[1], data), year_rainfall))[1] )

# In the following example I am going to break the entire operation down into
# steps:

# The Wrap step:
result1 = map(lambda data: (data[1], data), year_rainfall)

# The processing step:
maximum = max(result1)

# The Unwrapping Step:
unwrapped = maximum[1]

# Lets break this down very carefully

# In the WRAP step, the map() function transforms each tuple from the orignal data
# into a new tuple where each tuple looks like:
#    (29.87, (2000, 29.87)), (30.12, (2001, 30.12)), ...
# Since we want to apply this design pattern to finding the max rainfall, we need
# to creatively restructure the data so the max() function applies to the rainfall
# and not the year.

# In the PROCESSING step, the restructured data is given to the max() function
# which will now return the result based on the maximum rainfall value.

# We "unwrap" the result by using the indexing syntax [1] to give us the second
# value of the wrapped tuple. The second value is the data in its original form.

#-------------------------------------------------------------------------------