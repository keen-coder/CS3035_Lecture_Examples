# All comments in Python begin with the # character.
# Python does not have multi-line comments.

# Comment Notes from PEP 8:
#  "Comments that contradict the code are worse than no comments. Always make a
#  priority of keeping the comments up-to-date when the code changes!"
#
#  "Comments should be complete sentences.  If a comment is a phrase or sentence,
#  its first word should be capitalized, unless it is an identifier that
#  begins with a lower case letter (never alter the case of identifiers!)."
#
#  "If a comment is short, the period at the end can be omitted.  Block comments
#  generally consist of one or more paragraphs built out of complete
#  sentences, and each sentence should end in a period."
#
#  "You should use two spaces after a sentence-ending period."

# BLOCK COMMENTS:---------------------------------------------------------------
#  "Block comments generally apply to some (or all) code that follows them,
#  and are indented to the same level as that code.  Each line of a block
#  comment starts with a # and a single space (unless it is indented text
#  inside the comment)."
#
#  "Paragraphs inside a block comment are separated by line containing a
#  single #."

# EXAMPLES OF BLOCK COMMENTS ---------------------------------------------------

# This is a block comment which describes the following block of code.  In this
# comment I would describe anything I need to say about the function in order
# to explain its use to someone reading my code.  Notice each line of the
# starts with the # sign and how each comment is indented to the same level as
# the block of code that follows.
def my_function1(x):

    # This is a block comment which would describe what this if/else block
    # is doing.  Notice this time how the comments are indented at the same level
    # as the if/else block of code which follows.
    if x == 2:
        pass
    else:
        pass

    return None

"""
You can also use a multi-line string (a string that begins and ends with three 
single or double quotes) as a comment.  These strings are allowed to span 
multiple lines.  We will talk more about these when we discuss strings.  The 
preferred and more common way of commenting is by just using the # character.
"""
def my_function2():
    pass
#-------------------------------------------------------------------------------

# INLINE COMMENTS----------------------------------------------------------------
#  "Use inline comments sparingly."

#  "An inline comment is a comment on the same line as a statement. Inline
#  comments should be separated by at least two spaces from the statement. They
#  should start with a # and a single space."

# Inline comments are unnecessary and, in fact, distracting if they state the
# obvious.  Don't do this:

x = x + 1  # Increment x

# But sometimes, inline comments can be useful.
x = x + 1  # Compensate for border value


