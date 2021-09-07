# MODULE BASICS-----------------------------------------------------------------

# The .py source code file of a python program is what we refer to as a module.
# Modules can be imported to other modules using the import or from statements.

# Modules are a way to organize your code:
#   Modules can define a bunch of releated utility functions like the math module
#   defines common mathematical operations.

#   Modules can define classes when working with object oriented python.

#   Modules can define variables or constants that can then be imported.
#       Not always best practice, but can be useful on rare occasions.

#-------------------------------------------------------------------------------

# TYPICAL PYTHON PROGRAM STRUCTURE----------------------------------------------

# A python program usually consists of one or .py files that contain Python
# statements.  One of these .py files is usually a top-level file (or script) which
# contains the main flow of control of the program.  This is also the file that
# you normally execute to start the programing.

# In addition to the top-level script, you can have additional module files which
# do not execute on their own, but contain class definitions, function definitions
# and other names that can be imported into your main script file.

# Import statements allows your script file to access the "attributes" of the
# module, that is, the things defined within that module.


#-------------------------------------------------------------------------------

# HOW IMPORTS WORK--------------------------------------------------------------

# import statements perform three steps:

# 1. Find the module's source code file.
# 2. Compile the module if necessary (only does this if the module has not been
#    changed.
# 3. Run the module.  In order to generate the attributes in the module to bring
# them into the top-level script file, it must be executed from top to bottom.
# This will create any global variables, any functions, etc.  This also means
# if you have module level code written outside of any function, when you import
# the module, this code will execute as well and may so its output (if any).
# Typically modules that are truly meant to be imported should not contain code
# defined outside of a class or function.

# Imports also only happen once.

#-------------------------------------------------------------------------------

# import VS from----------------------------------------------------------------

# Using the import statement does the following:
#   import module_name
#     imports all the attributes of a module
#     to use any attribute you must fully qualify the attribute name with the
#     module name
#     most reliable form of import
#     ex: module_name.attribute_name

# EXAMPLE:

import math   # I have imported all attributes from the math module. To use
              # a function, I must qualify the name with the module name.

print(math.pow(5, 4))
print(math.sqrt(25))

# Using the from statement can import specific things from a module.
#   from module_name import attribute_name1, attribute_name2
#   from module_name import attribute_name1
#   from module_name import attribute_name2
#     imports only a specific attribute from a module
#     you do not have to fully qualify the attribute with the module name.
#     these types of imports can be problematic because you defeat the purpose of
#     the namespace and this can lead to name collisions.

# Example

from math import pow, sqrt
print(pow(5, 4))
print(sqrt(25))

# Using the from * statement will import all attributes from a module
#   from module_name import *
#     imports all of the attributes from the module
#     you do not have to fully qualify the attribute with the module name.
#     again, can lead to name collisions between different modules.

from math import *
print(pow(5, 4))
print(sqrt(25))