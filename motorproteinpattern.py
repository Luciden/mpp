#!/usr/bin/python
from Tkinter import *

OUTFILE = "pattern.txt"

outputFile = open(OUTFILE, "wb")
points = []


def write_coordinate(c):
    outputFile.write(str(c))
    outputFile.write('\n')


def write_coordinates(x, y, z):
    write_coordinate(x)
    write_coordinate(y)
    write_coordinate(z)


def create_point(event):
    c.create_oval(event.x, event.y, event.x+1, event.y+1, fill="black")

    points.append(event.x)
    points.append(event.y)


def new_file():
    pass


def open_file():
    pass


def gui_make_menu(root):
    menu = Menu(root)
    root.config(menu=menu)

    filemenu = Menu(menu)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="New", command=new_file)
    filemenu.add_command(label="Open ...", command=open_file)
    filemenu.add_separator()
    filemenu.add_cascade(label="Quit", command=root.quit)

    menu.add_separator()

    functionmenu = Menu(menu)
    menu.add_cascade(label="Functions", menu=functionmenu)
    functionmenu.add_command(label="X", command=None)
    functionmenu.add_command(label="Y", command=None)


if __name__ == "__main__":
    write_coordinates(1.0, 2.0, 3.0)

    root = Tk()

    gui_make_menu(root)

    w = Label(root, text="Hello Tkinter!")
    w.pack()

    c = Canvas(root, bg="white", width="480", height="320")
    c.configure(cursor="crosshair")
    c.pack()
    c.bind('<Button-1>', create_point)

    root.mainloop()
