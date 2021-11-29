from tkinter import *

class HelloButton(Button):
    def __init__(self, parent=None, **config):
        Button.__init__(self, parent, **config)
        self.pack()  # could config style too
        self.config(command=self.callback)

    def callback(self):  # default press action
        print('Goodbye world...')  # replace in subclasses
        self.quit()

def main():
    HelloButton(text='Hello subclass world').mainloop()


if __name__ == "__main__":
    main()
