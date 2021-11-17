# This example shows how we can make a class for callable objects.
# Callable objects are created when the class that instantiates that object
# implements the __call__() method.

# Example:
#   If class MyClass implements the __call__() method to take two integers and return
#   some value, then I can do the following:

#   mc = MyClass(arguments) create an instance of the class
#   mc(5, 8) since the class implements the __call__() method, the object that
#   the class creates is now a callable object and can be treated like a function.

# The following example from the book creates a Callable class with the Strategy
# Design pattern to compute Mersenne Primes in one of 3 ways.  Each instance of
# the class accepts a different algorithm for computing the primes.

# NOTE: a Mersenne Prime is a prime number p when it equals 2^n - 1

from typing import Callable

# The typing module in Python is used to indicate more advanced type hints.
# Recall that a type hint is a 'hint' you can add to your code to tell what data type
# a variable, or parameter, or return value might have.  Remember that these are not
# enforced.

# The Callable class is used to indicate type hints for functions that are pass as
# arguments.

# The Callable type hint has the following format:
#   Callable[[param_type1, param_type2, ...], return_value_type]

class Mersenne:
    def __init__(self, algorithm: Callable[[int], int]) -> None:
        self.pow2 = algorithm

    def __call__(self, arg: int) -> int:
        return self.pow2(arg) - 1

# The following defines three algorithms that we can pass to our class constructor
# each of which computes Mersenne Primes in a different way

# This algorithm computes the mersenne prime by using the left bitshift operator.
# Bitwise operators work on the bits of a value and when you left shift it is the same
# as multiplying by 2.
def shifty(b: int) -> int:
    return 1 << b

# This algorithm uses naive recursion to compute the mersenne prime.
def multy(b: int) -> int:
    if b == 0: return 1
    return 2 * multy(b-1)

# This algorithm uses a divide and conquer strategy that will perform log2(b)
def faster(b: int) -> int:
    if b == 0: return 1
    if b%2 == 1: return 2 * faster(b-1)
    t = faster(b//2)
    return t*t

# Now we can instantiate the class in three ways passing each of these algorithms
# to the constructor of the class.
m_shifty = Mersenne(shifty)
m_multy = Mersenne(multy)
m_faster = Mersenne(faster)

# And here we use the object that was created as a callable object to compute mersenne prime
# 2^7 - 1 = 127

print(m_shifty(7))
print(m_multy(7))
print(m_faster(7))
















