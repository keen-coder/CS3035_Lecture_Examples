# WHILE LOOPS-------------------------------------------------------------------

# Syntax:
# while condition:
#   statements
# else:
#   statements

# While loops can have an optional else condition.  This else is executed if and
# only if the loop exits normally (without triggering a break statement).

x = 5
while x >= 1:
    print('loops are fun', x)
    x -= 1    # Review: Python does not have a ++ or -- operator.

print('\n')  # print a new line character

x = 5
while x >= 1:
    print('will the else execute?', x)
    x -= 1    # Review: Python does not have a ++ or -- operator.
else:
    print('yes it will since the loop exits normally')

print('\n')  # print a new line character

x = 5
while x >= 1:
    print('will the else execute?', x)
    if x == 3: break
    x -= 1    # Review: Python does not have a ++ or -- operator.
else:
    print('no, since the loop was exited by a break statement')

# NOTE: Python loops support the break and continue keywords and they function
# the same as in Java.

# Here is an example where the else can be useful for short-handing our code.
# Example 1:

index = 0
exists = False
list = [1, 2, 3, 4, 5, 6]

while not exists and index < len(list):
    x = list[index]
    if x == 10:
        print('found')
        exists = True
    else:
        index += 1

if not exists:
    print('not found')

# Example 2: Can be rewritten a bit shorter to use the else:

index = 0
list = [1, 2, 3, 4, 5, 6]

while index < len(list):
    x = list[index]
    if x == 10:
        print('found')
        break
    index += 1
else:
    print('not found')

#-------------------------------------------------------------------------------

# FOR LOOPS---------------------------------------------------------------------
# for loops in Python are basically for-each loops and do not behave like for
# loops in Java or C++.  We will come back to for loops later on.