# This example shows how we could apply a number of transformations to a string
# to get it in the format that we want and eventually return a Decimal object.

from decimal import *

# The following function replaces all '$' and ',' characters with the empty
# string and returns the result as a Decimal object.

# This function uses a postfix function (replace) mixed with a prefix function
# Decimal
def format_string(text: str):
    if text is None: return None
    return Decimal(text.replace('$', '').replace(',',''))

# We can rewrite this example so that when we call the function, we only use
# prefix function calls. -
def replace(text, ch1, ch2):
    return text.replace(ch1, ch2)

# Now we would call the function using only prefix function calls
text = '$1,000,000.00'
result = Decimal(replace(replace(text, '$', ''), ',', ''))


# A third way to define the function could be as follows:
def remove(text, chars):
    if chars:
        return remove(text.replace(chars[0], ''), chars[1:])
    return text

# then we only need to call
result = remove(text, '$,')