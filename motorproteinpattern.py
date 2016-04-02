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

if __name__ == "__main__":
    write_coordinates(1.0, 2.0, 3.0)

    root = Tk()

    w = Label(root, text="Hello Tkinter!")
    w.pack()

    c = Canvas(root, bg="white", width="480", height="320")
    c.configure(cursor="crosshair")
    c.pack()
    c.bind('<Button-1>', create_point)

    root.mainloop()
