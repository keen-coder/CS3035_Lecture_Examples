"""
Unit testing of functions.

This module shows how to use the Examples: section of your function docstrings
to perform unit tests on your functions.

"""
import doctest

def power(x, y):
    """
    Calculates x to the power of y
    
    Args:
        x (int): base
        y (int): exponent
    
    Returns:
        int: x**y
    
    Examples:
        >>> power(2, 4)
        16
                 
        >>> power(3, 7)
        2187
        
        >>> [power(x, 2) for x in range(1, 6)]
        [1, 4, 9, 16, 25]
    """ 
    return x ** y

doctest.testmod()