

# Here is an example of a function which creates some global input and output
# file objects

# In functional programming we want to avoid things like that as much as possible.

def init_files(in_file_name: str, out_file_name: str):
    global in_file, out_file
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')


# A better way to handle this is by using a 'with' statement.  The with statement
# when used with file I/O will open the file, if available.  You can then process
# the file in the block of code underneath the width statement and then the file
# will be automatically closed after the with block is exited.


with open('my_file.txt') as file:
    data = file.read() #read the data
    # process the data and do something with it
    # This part will be written using functional techniques.












