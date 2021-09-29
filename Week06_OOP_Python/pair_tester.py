from pair import Pair

def main():
    p1 = Pair(3, 4)
    p2 = Pair(10, 7)
    p3 = p1 + p2 # p1.__add__(p2)
    p4 = p1 + 25 # p1.__add__(25)
    p5 = 25 + p1 # 25.__add(p1)

    print(f'{p1[0] = }')
    print(f'{p1[1] = }')

    p1[0] = 50
    p1[1] = 100

    print(p1)


    print(f'{p1 ** 2 = }')



    print(p3)
    print(p4)
    print(p5)




    p6 = Pair(10, 20)
    p7 = Pair(5, 15)
    p8 = Pair(5, -15)

    print(f'{p7 == p8 = }')

    print(p6 > p7)
    print(p7 > p6)
    print(p7 >= p8)

    p9 = Pair(100, -325)
    p10 = Pair(5, 5)

    p9 += p10

    print(p9)

    p9 += 20

    print(p9)

    p9 = -p9
    print(p9)
    p9 = +p9
    print(p9)









if __name__ == "__main__":
    main()
