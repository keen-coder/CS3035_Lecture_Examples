import random
import timeit
import math
from rectangle import Rectangle


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def my_sum(my_list):
    sum = 0
    for x in my_list:
        sum += x
    return sum

def main():

    amount = 5
    item = 'oranges'

    f_style1 = 'I have a bag of %s. There are %d in the bag.' % (item, amount)
    f_style2 = 'I have a bag of {}. There are {} in the bag'.format(item, amount)
    f_style3 = f'I have a bag of {item}. There are {amount} in the bag'

    print(f_style1)
    print(f_style2)
    print(f_style3)

    print(timeit.timeit(
    """ 
amount = 5
item = 'oranges'
'I have a bag of %s. There are %d in the bag.' % (item, amount)""", number=10000))

    print(timeit.timeit(
    """ 
amount = 5
item = 'oranges'
'I have a bag of {}. There are {} in the bag'.format(item, amount)""", number=10000))

    print(timeit.timeit(
        """ 
amount = 5
item = 'oranges'
f'I have a bag of {item}. There are {amount} in the bag'""", number=10000))

    x = 10
    y = 37

    print(f'The result is: {x * y}')
    print('The result is:', (x * y))
    print('The result is: ' + str( (x * y) ))

    my_list = [random.randint(26, 48) for x in range(10)]

    print(f'The list is {my_list}')
    print(f'my_list = {my_list}')
    print(f'{my_list = }') # This only works in Python 3.8+

    print(f'The list in reverse is {my_list[::-1]}')

    print('\n\n\n')

    print(f'5! = {factorial(5)}')
    print(f'{factorial(10) = }')

    print(f'The sum of values {my_list} is {my_sum(my_list)}')

    rec = Rectangle(6.7, 9.5)
    print(f'My rectangle is {repr(rec)}')
    print(f'Area of {repr(rec)} is {rec.area()}')

    pi2 = f'{math.pi:.2f}'
    pi3 = f'{math.pi:.3f}'
    pi4 = f'{math.pi:.4f}'
    pi5 = f'{math.pi:.5f}'

    print(pi2)
    print(pi3)
    print(pi4)
    print(pi5)

    print('\n\n')

    for x in range(1, 101):
        print(f'{x:} {x**2} {x**3}')

    print('\n\n')

    for x in range(1, 101):
        print(f'{x:03} {x**2:5} {x**3:7}')










if __name__ == "__main__":
    main()
