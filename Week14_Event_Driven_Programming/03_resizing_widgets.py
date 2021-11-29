from tkinter import *

def main():
    root = Tk()
    widget = Button(root, text='Hello GUI world!', overrelief='sunken', bg='#22d48f').pack(side=BOTTOM,fill=Y, expand=YES)
    root.mainloop()


if __name__ == "__main__":
    main()
