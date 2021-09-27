from rectangle import Rectangle


# Name Mangling
# in MyClass
# __my_variable = 10
# _MyClass__my_variable




def main():
    rect1 = Rectangle(9.3, 23.78)
    rect2 = Rectangle(5, 3)

    print(rect1)
    print(rect2)

    print(repr(rect1))
    print(repr(rect2))

    # print(rect1.get_num_rects())
    # print(rect2.get_num_rects())
    #
    # Rectangle.set_num_rects(10)
    #
    # print(rect1.get_num_rects())
    # print(rect2.get_num_rects())



if __name__ == "__main__":
    main()
