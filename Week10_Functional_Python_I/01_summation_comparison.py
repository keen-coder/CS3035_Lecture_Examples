

#-----------------------------PROCEDURAL SUMMATION------------------------------

def sum_list():
    sum = 0
    for n in range(1, 10):
        if n % 3 == 0 or n % 5 == 0:
            sum += n
    print(sum)

#-------------------------------------------------------------------------------

#---------------------------OBJECT-ORIENTED SUMMATION---------------------------

class SumList(list):
    def __init__(self, *args):
        super().__init__(args)

    def sum_list(self):
        sum = 0
        for n in self:
            if n % 3 == 0 or n % 5 == 0:
                sum += n

        return sum

myList = SumList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(myList.sum_list())

#-------------------------------------------------------------------------------

#-----------------------------FUNCTIONAL SUMMATION------------------------------

def sum_recursive(sequence):
    if len(sequence) == 0:
        return 0
    else:
        return sequence[0] + sum_recursive(sequence[1:])

def my_seq(value, end, filter_func):
    if value == end:
        return []
    elif filter_func(value):
        return [value] + my_seq(value+1, end, filter_func)
    else:
        return my_seq(value+1, end, filter_func)

# Filter function as a lambda function
multiple_3_5_lambda = lambda x: x % 3 == 0 or x % 5 == 0
even_numbers = lambda x: x % 2 == 0

# Filter function as a def function:
def multiple_3_5_def(x):
    return x % 3 == 0 or x % 5 == 0

# Generates lists with values: [3, 5, 6, 9, 10, 12, 15, 18]
my_list1 = my_seq(1, 20, multiple_3_5_lambda)
my_list2 = my_seq(1, 20, multiple_3_5_def)
my_list3 = my_seq(1, 20, lambda x: x % 3 == 0 or x % 5 == 0)
my_list4 = my_seq(1, 20, even_numbers)

print(sum_recursive(my_list1))
print(sum_recursive(my_list2))
print(sum_recursive(my_list3))

print(f'sum{my_list4} = {sum_recursive(my_list4)}')

functions = [multiple_3_5_lambda, even_numbers]

for f in functions:
    print(my_seq(1, 100, f))


#-------------------------------------------------------------------------------
