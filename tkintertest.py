from tkinter import *
import sys


class mainWindow(object):
    def __init__(self, master):
        self.l = Label(text="Hello World")
        self.l.pack()
        self.e = Entry()
        self.e.pack()
        self.b = Button(text="Ok", command=self.cleanup)
        self.b.pack()

    def cleanup(self):
        self.value = self.e.get()
        print(self.value)
        root.destroy()


if __name__ == "__main__":
    root = Tk()
    m = mainWindow(root)
    root.mainloop()
