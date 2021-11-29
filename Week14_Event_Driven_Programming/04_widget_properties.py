from tkinter import *



def main():

    widget = Label()
    widget['text'] = 'Hello GUI world!'
    #widget['bg'] = '#22d48f'
    widget['activebackground'] = '#9f1ce6'
    widget['relief'] = 'ridge'
    widget.pack(side=TOP)
    mainloop()

if __name__ == "__main__":
    main()
