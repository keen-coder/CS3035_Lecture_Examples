from tkinter import *

def real_handler(button_num):
    if button_num == 1:
        print("Button 1 was pressed!")
    elif button_num == 2:
        print("Button 2 was pressed!")



def main():

    button1 = Button(None, text='Button 1',
                     command=lambda: real_handler(1))
    button2 = Button(None, text='Button 2',
                     command=lambda: real_handler(2))
    button1.pack()
    button2.pack()

    mainloop()


if __name__ == "__main__":
    main()
