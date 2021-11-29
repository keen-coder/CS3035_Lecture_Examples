from tkinter import *

class MyClass:
    def __init__(self, x):
        self.x = x

    def printX(self):
        print(self.x)

def main():
    mc = MyClass(42)
    bt1 = Button(text="Press me", command=mc.printX)
    bt1.pack()
    mainloop()







if __name__ == "__main__":
    main()
