# INDEXING STRINGS--------------------------------------------------------------

# Strings are defined as an ordered collection of characters.  Unlike Java,
# Python allows indexing of strings using bracket [ ] notation.

# Strings start at index 0 just like other languages

# Indexing in Python allows for negative indexes:
#   This adds the negative value to the length of the string
#   Think of it like counting backwards from the end

# Example:
s = 'spam'

s[0]    # returns s
s[-1]   # returns m
s[2]    # returns a
s[-2]   # also returns a

# SLICING STRINGS---------------------------------------------------------------

# Slicing refers to a generalized form of indexing and returns an entire
# substring of a string

# Slicing has the following format s[i:j] where s is a string, i is the starting
# index and j is the ending index.

#    The lower bound i is always included in the slice, the upper bound j is
#    never included.

#    Boundary indexes can be omitted, i defaults to 0, j to the length of the
#    string.

#    s[1:3] fetches the substring starting at index 1 up to but not including
#    index 3
#    s[1:] fetches the substring at index 1 through the end
#    s[:3] fetches the substring at index 0 up to but not including 3
#    s[:-1] fetches items at offset 0 up to but not including the last item
#    s[:] fetches the entire string (essentially makes a copy of the string)

# Examples:

s = 'KNIGHTS WHO SAY NI'  # len(s) = 18

print(s[:])     #prints the entire string
print(s[8:11])  #prints 'WHO'
print(s[12:])   #prints 'SAY NI'
print(s[:7])    #prints 'KNIGHTS'
print(s[:-7])   #prints 'KNIGHTS WHO'

#-------------------------------------------------------------------------------

# EXTENDED SLICING--------------------------------------------------------------

# Extended slicing has the form s[i:j:k] where s, i, and j, are the same as the
# previous, but k is the step (or stride), which defaults to 1. This allows you
# to skip over k items and reverse the order.

s = 'KNIGHTS WHO SAY NI'

print(s[::2])   #prints only chars at even indexes 'KIHSWOSYN'
print(s[1::2])  #prints only chars at odd indexes 'NGT H A I'
print(s[::-1])  #prints the string in reverse 'IN YAS OHW STHGINK'

#-------------------------------------------------------------------------------

# OTHER STRING METHODS----------------------------------------------------------

# The str object comes with all kinds of built-in methods.
#
# Consult the help(str) command in an interactive session to see what methods
# are available.

print(help(str))





