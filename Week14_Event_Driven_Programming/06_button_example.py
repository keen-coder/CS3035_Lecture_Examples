import sys
from tkinter import *

def main():
    widget = Button(None, text='CLICK ME!!!', command=sys.exit)
    # can also add a handler with one of the following two lines
    #   widget['command'] = sys.exit
    #   widget.config(command=sys.exit)
    widget.pack()
    widget.mainloop()

if __name__ == "__main__":
    main()
