from tkinter import *



def main():
    msg = Message(text="HAPPY HALLOWEEN", width=200)
    msg.config(bg='black', fg='orange',
               font=('times', 16, 'italic'))
    msg.pack(fill=BOTH, expand=YES)
    mainloop()


if __name__ == "__main__":
    main()
