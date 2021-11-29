import tkinter
from tkinter import Tk, Button

def main():


    tkinter.NoDefaultRoot()

    win1 = Tk()  # two independent root windows
    win2 = Tk()  # not the best option

    Button(win1, text='WINDOW 1', command=win1.destroy).pack()
    Button(win2, text='WINDOW 2', command=win2.destroy).pack()

    win1.mainloop()

if __name__ == "__main__":
    main()
