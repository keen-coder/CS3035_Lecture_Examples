""" Module with functions for strings, documented in google style.

This module demonstrates how to document your code using the Google style of
documentation.  Some of the things in this module may not make sense, but it
is purely an example for documenting your code.

Attributes:
    my_variable (int): Variable initializes to the value 42 which is the Answer
        to the Ultimate Question of Life, The Universe, and Everything.

"""
my_variable = 42

def string_as_list(string1: str) -> list:
    """Function to take a string and return the string as a list.

    Each character of the string will become one index of the list.

    Args:
        string1 (str): The input string to be converted to a list.

    Returns:
        list: The list containing each character of the string.
    """
    return [ch for ch in string1]

def reverse(string: str) -> str:
    """Function to return the reverse of a string.

    Args:
        string (str): The input string to be reversed.

    Returns:
        str: The reverse of the input string.
    """
    return string[::-1]

def repeat(string: str, n: int = 1) -> str:
    """Function to return a given string repeated n times.

    Args:
        string (str): The input string to be repeated.
        n (int, optional): The number of times to repeat the given string.
            This parameter is optional and its default value is 1.

    Returns:
        str: The resulting string that is all repetitions of the original string.
    """
    return string * n