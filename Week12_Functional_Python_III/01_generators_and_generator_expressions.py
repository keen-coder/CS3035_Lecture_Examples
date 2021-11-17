# Here is an example of a simple generator function
def simple_gen():
    x = 1
    print('First iteration of generator function.')
    yield x

    x += 1
    print('Second iteration of generator function.')
    yield x

    x += 1
    print('Third iteration of generator function.')
    yield x

# Invoke the genrator and assign it to a variable.  This will create an iterator
# object using the previous generator definition, but will not start executing
# the generator just yet.
gen = simple_gen()

# Using the next() function we tell the generator to execute one time and return
# the next value.  The generator then pauses after the yield statement and waits
# for subsequent calls to it using next().
print(next(gen))

print(next(gen))

print(next(gen))

# print(next(gen)) # This line will cause a StopIteration exception to be raised.

# The genenerator is done at this point.  If we want to "restart" the generator
# we need to create a new iterator object from a call to the generator.


# We can also use a loop to iterator over the generator since it is an iterable
# sequence.  The for loop will automatically stop when the exception is raised.

for x in simple_gen():
    print(x)


# Generators can be written using a loop or using recursion.
# Here are two examples which reverse a string.

def str_reverse_i(text):
    for ch in range(len(text) - 1, -1, -1):
        yield(text[ch])

def str_reverse_r(text):
    if not text:
        return

    yield text[len(text) - 1]
    yield from str_reverse_r(text[:len(text) - 1])

for ch in str_reverse_i("python is fun"):
    print(ch)

for ch in str_reverse_r("hello world"):
    print(ch)

# Generators can also be created from Generator expressions.  These have the
# same syntax as List comprehensions, but replace the [ ] with ( )

b = (x**2 for x in range(1, 30))

print(next(b))
print(next(b))
print(next(b))
print(next(b))

# WHY USE GENERATORS?

# They are easy to implement and simplify the syntax of creating an iterator
# The other way of creating an iterator is to use a class as follows

class PowTwo:
    def __init__(self, max=0):
        self.n = 0
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration

        result = 2 ** self.n
        self.n += 1
        return result

# There is way more syntax here than necessary and we can simplify this with a
# generator.

def PowTwoGen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1

# Generators are also more memory efficient.  If you want to generate a large
# sequence of values that don't necessarily need to be stored in memory (maybe you
# are sending the results to a data base or file output), generators only create
# one value in memory at a time.

# Generators can also be used to represent an infinite stream of data which cannot
# be stored in memory.

# In the following example we generator an infinite series of even numbers.

def all_even():
    n = 0
    while True:
        yield n
        n += 2

# Generators can also be given to other generators to perform some task.
# Since all the data does not need to be stored in memory we only need to keep the
# final result.

def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

def square(nums):
    for num in nums:
        yield num**2

print(sum(square(fibonacci_numbers(10))))
