import sys
from tkinter import *


def kill_program():
    print('Terminating Program')
    sys.exit()

def main():

    widget = Button(None, text="DON'T CLICK ME", command=kill_program)
    widget.pack()
    widget.mainloop()


if __name__ == "__main__":
    main()
