# SCOPE BASICS------------------------------------------------------------------

# Python has many levels of scopes which help to contain various names and
# identifiers in your program and prevent naming conflicts.  All names live in
# a namespace and each scope is essentially its own namespace.  Scope refers to
# the location of a name's assignment in your source code and where this assignment
# occurs determines which scope / namespace your name is in.

# All names assigned inside a function, are placed in that function's namespace.
#   Names assigned in a def can only be accessed within that def.
#   Names assigned in a def do not clash with variables outside of the def,
#   even if the variable inside and outside share the same name

# The scope of a variable is ALWAYS determined by where it is assigned.
#   LOCAL: variables assigned in a def are local to that function.
#   NONLOCAL: variables assigned in an enclosing def are nonlocal to nested functions.
#   GLOBAL: variables assigned at the module level outside of any def are global.

# Example: The following is allowed with no conflicts.

x = 42          # Global (module) Scope x

def func1():
    x = 88      # Local (function) Scope x

#-------------------------------------------------------------------------------

# MORE SCOPE INFORMATION--------------------------------------------------------

# When you write code outside of any functions, all the code is at the top level
# or module level scope.  Any names used would then be from the module scope or
# from the built-in scope.

# Functions define a local scope, modules define a global scope:
#   An enclosing module is a global scope.  Global variables become attributes of
#   that module if the module is imported or are simple variables within the module
#   itself

radius = 5.67  # Here radius is in the global scope and can be used like a
               # normal variable within this module.  If you were to import this
               # module, radius would be an attribute of this module and useable
               # inside the module doing the importing.

#   The global scope spans a single file only. Names are partitioned into modules
#   and you must always import a module to make that name available to another module
#   within your project.  So think "module" when you hear the word "global" in python.

#   Assigned names assigned in a function are local unless declared as global
#   or nonlocal.

#   Every time you call a function, you are creating new local scope.

#-------------------------------------------------------------------------------

# NAME RESOLUTION: THE LEGB RULE

# Scope can be summarized with the following three rules:
#   With a def statement:
#     1. Name assignments create or change local names by default.
#     2. Name references search at most four scopes: local, then enclosing
#     functions (if any), then global, then built-in.
#     3. Names declared using the global or local statements map assigned names
#     to enclosing module or function scopes.

# Python's name resolution mechanism is sometimes called the LEGB rule, named
# after the scope names.  When an name is defined in a function, Python searches
# each scope in the following order:
#    L: The local scope of the function.
#    E: The enclosing scope of any enclosing (nested) functions.
#    G: The global (module) scope.
#    B: The built-in scope.
#    The global or nonlocal statements can change how this works.

# Example:

a = 37          # Global scope, available from this line down to all scopes

def func2(y):   # The name func2 is global as it can be used anywhere in the
                # module after it has been defined.
                # The name y is local and is only accessible in this function.
    z = 4 + 8   # Local scope, z is only accessible in this function.
    return z

#-------------------------------------------------------------------------------

# THE BUILT-IN SCOPE------------------------------------------------------------
# The Built-in scope is just a built-in python module called builtins.  This module
# contains common functions useful to most python programs.

# You can use any name from builtins without having to import builtins, but
# the module name itself (builtins) is not automatically imported.  If you wanted
# to pass builtins to the dir() or help() functions, you need to import it first.
import builtins
print(dir(builtins))

# Because of the way python scoping works, it is technically possible for you to
# redefine a name from the builtins module to do something different.  This of
# course is bad practice and should be avoided as much as possible.


# The following is all the names from builtins, try to avoid redefining these.
# ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
# 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning',
# 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
# 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
# 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False',
# 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning',
# 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError',
# 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError',
# 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError',
# 'NameError', 'None', 'NotADirectoryError', 'NotImplemented',
# 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning',
# 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError',
# 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration',
# 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit',
# 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError',
# 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError',
# 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError',
# 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__',
# '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__',
# '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint',
# 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex',
# 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate',
# 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr',
# 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance',
# 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max',
# 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print',
# 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr',
# 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type',
# 'vars', 'zip']

#-------------------------------------------------------------------------------

# The global Statement----------------------------------------------------------

# This is a type of namespace declaration.  The global statement tells Python
# that a function plans to change one or more global names.  Global allows us to
# change names that live outside a def at the module (global) level

# Example 1:
x = 42          # Define global variable x

def func3():
    global x    # Declare that the x inside the function should refer to global
                # variable x.
    x = 100     # Now we can change the value of global variable x.  Without
                # the previous global declaration, x = 100 would create a local
                # version of variable x.

func3()
print(x)        # This would print 100.


# Example 2:

y = 2            # Global variables in module
z = 1            # Global variables in module
x = 0

def all_global():
    global x        # Declare x to be global.
    x = y + z       # No need to declare y, z: LEGB rule

# Try to minimize the use of global variables as much as possible.  Variables
# should always be defined inside of a function or class.

# Avoid global variable names where the same name appears in two different modules.
# This can have weird side-effects (ask to see during lecture).

#-------------------------------------------------------------------------------




