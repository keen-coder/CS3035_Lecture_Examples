from tkinter import Label

def main():
    widget = Label(None, text='Hello GUI world!', bg='#22d48f')
    widget.pack()
    widget.mainloop()


if __name__ == "__main__":
    main()
