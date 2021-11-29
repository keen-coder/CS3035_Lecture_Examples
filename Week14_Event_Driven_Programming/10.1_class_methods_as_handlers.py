import sys
from tkinter import *

class HelloClass:
    def __init__(self):
        widget = Button(None, text='CLICK',
			    command=self.quit)
        widget.pack()

    def quit(self):
        print('Hello class method world')
        sys.exit()

def main():
    HelloClass()
    mainloop()

if __name__ == "__main__":
    main()
