#-------------------------OBJECT ORIENTED PYTHON BASICS-------------------------

# Classes in Python are very easy to implement with a minimal amount of new
# syntax.

# Classes provide all of the standard features you would expect to see in
# Object-Oriented Programming:
#   inheritance (base classes and derived classes)
#   constructors
#   instantiation
#   operator overloading (a feature borrowed from C++)
#   and other features

#-------------------------------------------------------------------------------

#------------------DEFINING CLASSES AND THE 'CLASS' STATEMENT-------------------

# Class definitions are like function definitions and must be executed before
# they have any effect.
#   Typically this means importing the module which contains the class definition.
#
# Class names should follow the normal naming conventions:
#   capitalize the first letter of the class name
#   capitalize the first letter of any subsequent words

# Classes are defined using the 'class' statement:

# Example:

class MyPythonClass:
    pass
#-------------------------------------------------------------------------------

#-----------------------------A FIRST CLASS EXAMPLE-----------------------------

class Person:
    __num_people = 0

    def __init__(self, name, age=None, phone=None):
        self.__name = name;
        self.__age = age;
        self.__phone = phone;

        Person.__num_people += 1

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    @staticmethod
    def get_num_people():
        return Person.__num_people

#-------------------------------------------------------------------------------

#---------------------CLASS CONSTRUCTORS AND INSTANCE DATA----------------------

# The __init__ function serves as the one and only constructor of a class.

# Python does not support traditional function / method overloading.
#   -You can overload functions in python based on number of parameters, but not
#    types of parameters.
#   -Typically the most pythonic way of allowing options with constructors is
#    to play around with the various types of parameters which we previously
#    covered.

# The __init__ function parameters can use all of the same options as regular
# functions. (positional parameters, default values, *args, and **kwargs)

# Inside the __init__ function is where you create and initialize any instance
# attributes (data fields) and perform any other necessary initialization code
# for your class.
#
# Instance data SHOULD NOT be created outside of the constructor or without using
# the 'self' keyword, if this happens the data is no longer instance data.

# Below the init method makes use of various types of parameters
# NOTE: the word 'self' as the first parameter of the __init__ function.
def __init__(self, name, age=None, phone=None):
    self.__name = name;
    self.__age = age;
    self.__phone = phone;

    Person.__num_people += 1
#-------------------------------------------------------------------------------

#------------------------------THE 'SELF' KEYWORD-------------------------------

# The self keyword is exactly like "this" in other languages.
#
# self refers to an instance of the class.
#
# In python you MUST always use self to refer to something that is related to
# an instance inside of the class definition, so using self is always required.
#
# 'self' must ALWAYS be the first parameter to the __init__ method or any
#  other instance methods.

def __init__(self, name, age=None, phone=None):
    self.__name = name;
    self.__age = age;
    self.__phone = phone;

    Person.__num_people += 1

def get_name(self):
    return self.__name

def set_name(self, name):
    self.__name = name

#-------------------------------------------------------------------------------

#---------------------DOES PYTHON HAVE PRIVATE ATTRIBUTES?----------------------

# Unlike Java, python does not have the same type of public, private, protected
# access for class attributes.

# The concept of "private" instance variables that cannot be accessed outside of
# a class does not exist in python.

# One of my favorite quotes I found online is
#   "Python makes a lot of assumptions. One being that you're not an idiot"

# Conventionally any name that begins with a single underscore prefix (_name)
# is supposed to be treated as a non-public part of the API and should be
# considered an implementation detail that is subject to change without notice.
#   Any data field or method could be prefixed with a single underscore.
#
# In other words, we are all mature programmers (I hope!!) and we should not
# touch anything beginning with a single underscore outside of the class.
# If you do, you do so at the risk of breaking your code should the author of
# the class decide to change how that private data is represented.

# Example:
class ClassWithPrivateStuff:
    def __init__(self, value, color):
        # Here _value and _color both start with a single underscore, so they are
        # to be treated as if they are private.
        self._value = value
        self._color = color

    # Here _some_private_method starts with a single underscore and should NEVER
    # be invoked outside of this class.
    def _some_private_method(self):
        pass

# For programmers who want something closer to private, Python provides a
# 'sort-of-private' mechanism called 'name mangling'

# Any identifier that is prefixed with two underscores (__name) is textually
# replaced with _classname__name, when the code is compiled.

# This is done automatically and you do not have to worry about anything other
# than adding two underscores to the beginning of the attribute name.
#
# This can be helpful to avoid any name collisions with things that are supposed
# to be private, as well as hide these attributes from any IDE's which support
# code completion.
#
# DO NOTE: that name mangling still does not fully protect your data, if someone
# knows the name mangling scheme (most programmers will) then your data could still
# be directly accessed.

# Example:
class ClassWithNameMangling:
    def __init__(self, value, color):
        # Here __value and __color both start with a double underscore, so they are
        # to be treated as if they are private and their names are changed to
        # _ClassWithNameMangling__value and _ClassWithNameManling__color.
        self.__value = value
        self.__color = color

    # Here _some_private_method starts with a single underscore and should NEVER
    # be invoked outside of this class.  It's name will be changed to
    # _ClassWithNameMangling__some_private_method.
    def __some_private_method(self):
        pass

#-------------------------------------------------------------------------------

#---------GUIDO VAN ROSSUM'S THOUGHTS ON PYTHON'S LACK OF PRIVATE DATA----------

# Someone wrote to Guido van Rossum (Python's creator) one time to ask him about
# private data in python.

# Here is the text of the question:

'''
Dear BDFL (Benevolent Dictator for Life),

I'm writing my talk for a local PyCon (it is on Saturday - and I'm late as ever), 
and one of the questions I'm trying to answer is why Python doesn't have real 
information hiding the in the way of the C++ (or Ruby) ideas of public, 
protected and private.

Everything I've found online just mentions the state of what it is now, 
with leading underscore being considered private, and double underscore getting 
mangled with the classname, but these are still public (and we are consenting 
adults). Was there a particular driving force behind the access methods in 
Python? Or was it a collection of smaller things?

--Procrastinating in the Southern Hemisphere
'''

# And here was the response from Mr. Rossum:

'''
Dear Procrastinating,

There is actually some information hiding possible -- but only by writing C 
extensions. :-)

The main reason for making (nearly) everything discoverable was debugging: when 
debugging you often need to break through the abstractions (since bugs don't 
confine them to the nice abstractions you've created for your program :-) so I 
thought it would be handy to be able to see anything from the debugger. And 
since the debugger is written in Python itself (for flexibility and a number of 
other reasons) I figured the same would apply to other forms of programming -- 
after all, sometimes debugging doesn't imply using a debugger, it may just imply 
printing a certain value. Again, too much data hiding would make things more 
complicated here.

The other observation was that even in C++, there are usually ways around the 
data hiding (e.g. questionable casts). Which made me realize that apparently 
other languages could live just fine with less-than-perfect hiding, and that 
hiding was an advisory mechanism, not an enforcement mechanism. So Python could 
probably be just fine with even-less-than-perfect hiding. :-)

Good luck with your talk, and enjoy the event!
'''
#-------------------------------------------------------------------------------

#-------------------------------INSTANCE METHODS--------------------------------

# Python classes can have instance methods.

# Instance methods are methods that access / change any instance data in your
# class.

# Instance methods MUST have self as the first parameter to the method, ALWAYS
# no exceptions.

# Example:
class ClassWithInstanceMethods:
    def __init__(self, x):
        self.__x = 10

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

#-------------------------------------------------------------------------------

#-------------------------STATIC METHODS AND VARIABLES--------------------------

# Any variable defined outside of the constructor or another method is a static
# variable (class variable).

# These variables are shared among all instances of a class, and if one instance
# changes the variable, it will be changed for all instances.

# Static methods are methods which do not access ANY instance data or which use
# static data.  These methods cannot use self and cannot have self as a parameter
# to the method.

# Static methods should be identified using the @staticmethod annotation.
#
# When you want to refer to a static variable use ClassName.static_variable_name
# When you want to invoke a static method use ClassName.static_method_name()

# Example:

class ClassWithStaticStuff:
    __my_static_variable = 30

    def __init__(self):
        pass

    @staticmethod
    def my_static_method():
        return ClassWithStaticStuff.__my_static_variable

#-------------------------------------------------------------------------------