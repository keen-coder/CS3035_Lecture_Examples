# FUNCTION BASICS---------------------------------------------------------------

# This module will teach you about functions in Python.  Functions are basically
# Methods from Java, but Python makes a distinction between the two.  A function
# in Python is defined in a module by itself (outside of class) whereas a method
# is a function define in a class.  Functions work exactly the same as they do
# in Java / C++ but of course with different syntax.

# Function Syntax:
#   def function_name(parameter_list):
#       statements
#       statements
#       return optional_return_value


# Function Examples

# "Void" function with no parameters
def function1():
    print('hello world')

# "Void function with parameters
def function2(x, y, z):
    print(x + y + z)

# "Value-returning" function with no parameters
def function3():
    return 10

# "Value-returning" function with parameters
def product(a, b, c):
    return a * b * c

#-------------------------------------------------------------------------------

# FUNCTION CALLING / INVOCATION

# You call a function just like you do in Java or C++
# If your Python module contains code outside of any function definition, then
# the function must be defined BEFORE you can call that function.  So the function
# call in the following lines of code would not work if the sum() function
# was not defined previously.
def sum(a, b, c, d):
    return a + b + c + d

result = sum(1, 2, 3, 4)  # This function call would not work if sum was not
print(result)             # previously defined.

# However, any code INSIDE of a function can call any other function no matter
# where in the module the called function was defined.

def compute():
    a = 10
    b = 20
    c = 50
    printValues(a, b, c)  # Notice how this line calls a function which is defined
                          # later in the code.

def printValues(a, b, c):
    print('a =', a, 'b =', b, 'c =', c)

compute();  #  To call the compute() function at the module level, compute()
            #  must be previously defined.
#-------------------------------------------------------------------------------

# ADDITIONAL FUNCTION NOTES-----------------------------------------------------

# The def statement is an executable statement.
#    In Java or C++ function / methods exist when the code is compiled.
#    In Python, a function does not exist until Python reaches and executes the def.
#    You can even use nested def statements # inside of Python if/else structures.
#    def statements are coded in Python module files and are executed to generate
#    functions when the module they are defined in is first imported.

# The def statement creates an object and assigns it to a name when the def
# statement is executed.

# Arguments are passed by assignment.  Changes to immutable argument values
# inside of a function will not change the values outside of the function.
# Changes to mutable argument values inside of a function will change the values
# outside of the function.

def argument_test1(x):
    x = 10

x = 100
print(x)
argument_test1(x)
print(x)  # No change to the value of x since x is an immutable integer.

def argument_test2(list):
    list[0] = 50

list = [1, 2, 3, 4, 5]
print(list)
argument_test2(list)
print(list)  # The first value in the list changes since list is a mutable object.

# Arguments are passed by position, unless you say otherwise.  Without doing
# anything special, when you pass arguments to a function, the function reads them
# from left to right and assigns them to the parameter names from left to right.
def passing_arguments(name, age, like):
    print('My name is', name, 'and I am', age, 'years old and I like', like)
passing_arguments('John', 22, 'pancakes')

# Arguments can also be passed by name using the syntax name=value.  When passed
# this way, arguments can be passed in any order.
passing_arguments(age=43, like='lasagna', name='Sue')

#-------------------------------------------------------------------------------

# LOCAL VARIABLES---------------------------------------------------------------

# Any variable that is defined within a function definition is a local variable
# what scope local to that function.

# Here num and title are both local variables available only in the function.
def local_variables():
    num = 10
    title = 'Lone Wolf'