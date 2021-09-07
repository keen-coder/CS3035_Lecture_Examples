import math

def main():    # again does NOT have to be called main, but helps to identify
               # the entry point of your program.

    valid = False

    radius = 0

    while not valid:
        if radius <= 0:
            radius = float(input("Enter a radius value for a circle: "))
        else:
            valid = True

    print('The area is: ', area(radius))


def area(radius):
    return math.pow(radius, 2) * math.pi

if __name__ == '__main__':
    main()





