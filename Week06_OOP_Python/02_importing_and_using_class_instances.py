#-----------------------------IMPORTING YOUR CLASS------------------------------

# Typically a class would be written in one module, while the code which uses
# that class is written in a separate module (just like Java).

# You must import the module that contains your class if you want to use it in
# another module.

# Using a "from import" is ok with classes as long as you do not have any name
# collisions.

# Example using a normal import
import circle

# Example using a from import
from circle import Circle

#-------------------------------------------------------------------------------

#----------------------CREATING AND USING CLASS INSTANCES-----------------------

# Creating an instance of a Python class, is very similar to Object Oriented
# Java, except you do not use the new keyword.

# If you use a normal import, you must qualify the constructor with the module
# name
import circle

circle1 = circle.Circle(29.4)

# If you use a from import, you can drop the module name.
from circle import Circle

circle1 = Circle(4.78)

# Using public instance methods from your class follows the same dot operator
# syntax as in Java.

circle1 = Circle(5.6)
print(circle1.area())

# Accessing static methods should be done in a static way:
print(Circle.get_number_of_circles())


















#-------------------------------------------------------------------------------
