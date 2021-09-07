# PYTHON CODE CAN BE EXECUTED IN TWO GENERAL WAYS-------------------------------

# A Python module can be run 'directly' from the command line or by running it
# from an IDE.

# A Python module can be run 'indirectly' by importing said module.
#   Recall that a module must be executed in order to generate and make its
#   attributes available from importing.

# Python modules are not required to have a main function:
#    We can create a main-like function that will kick-off the execution of our
#    program as long as the module is executed directly (from the command line,
#    ide, etc.).

#-------------------------------------------------------------------------------

# THE __name__ ATTRIBUTE--------------------------------------------------------

# Python defines a special string attribute called __name__ in every module.
#   NOTE: those are two underscore characters on both ends of 'name'

# The value assigned to the __name__ attribute will differ depending on how the
# module was executed:
#   if the module is executed directly the value of name will be '__main__'
#   if the module is executed indirectly the value of the name will be
#   '__module_name__'

#-------------------------------------------------------------------------------

# TESTING FOR '__main__'--------------------------------------------------------
# We can use the previously defined facts about the __name__ attribute to run a
# "main" function whenever our program is executed directly.

# Example:

def main(): # does not have to be called main its just a convention
    print("Program executed directly")

if __name__ == '__main__':
    main()


# You should use this technique as much as possible, especially if your program
# includes a lot of modules.

# This helps to identify which module should be executed first in order to
# kick-off your entire program.

# see example: compute_area.py