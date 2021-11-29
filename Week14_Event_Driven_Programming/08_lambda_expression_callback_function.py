import sys
from tkinter import *


def main():

    widget = Button(None, text='Hello event world',
                    command=(lambda: print('Hello lambda world')))
    widget.pack()
    widget.mainloop()


if __name__ == "__main__":
    main()
