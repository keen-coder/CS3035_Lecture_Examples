from tkinter import *

def fetch(entries):
    for entry in entries:
        print('Input => "%s"' % entry.get())

def makeform(root, fields):
    entries = []
    for field in fields:
        row = Frame(root) # make a new row
        lab = Label(row, width=5, text=field) # add label, entry
        ent = Entry(row)
        row.pack(side=TOP, fill=X) # pack row on top
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X) # grow horizontal
        entries.append(ent)
    return entries

def main():
    fields = ['Name', 'Job', 'Pay']
    root = Tk()
    ents = makeform(root, fields)
    Button(root, text='Fetch',
           command=(lambda: fetch(ents))).pack(side=LEFT)
    root.mainloop()

if __name__ == "__main__":
    main()
