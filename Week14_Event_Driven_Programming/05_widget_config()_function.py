from tkinter import *

def main():

    root = Tk()
    widget = Label(root)
    widget.config(text='Hello GUI world!')
    widget.config(bg='#22d48f')
    widget.pack(side=TOP, expand=YES, fill=BOTH)
    root.title('gui1g.py')
    root.mainloop()


if __name__ == "__main__":
    main()
