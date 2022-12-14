import tkinter
from tkinter import *
from PyQt6 import Qt6   # or PySide
parent = Tk()
parent.geometry("400x250+400+100")



redbutton = Button(parent, text="Dễ", fg="red",command=clicked)
redbutton.place(x=50, y=50)
greenbutton = Button(parent, text="Black", fg="black")
greenbutton.pack(side=RIGHT)
bluebutton = Button(parent, text="Blue", fg="blue")
bluebutton.pack(side=TOP)
blackbutton = Button(parent, text="Green", fg="green")
blackbutton.pack(side=BOTTOM)
# win = tkinter.Toplevel(parent)
# center(win)
parent.mainloop()