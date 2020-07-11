import tkinter as tk
from tkinter import Tk
from functools import partial
from tkinter import PhotoImage
import os


def changeInterface(dropDownText):
    print(dropDownText.get())
    

#create the root and the canvas
root = tk.Tk()
root.resizable(width=False, height=False)
canvas = tk.Canvas(root,height = 600, width = 900, bg="#691C1C")
canvas.pack()

#create main page image
im = r"C:\Users\vinee\Python\MainScreen.png"
photo = tk.PhotoImage(file = im)
my_img = canvas.create_image(450,200, anchor=tk.CENTER, image=photo)

#drop down
state = tk.StringVar()
state.set("---")
drop = tk.OptionMenu(root,state,"---","Texas")
drop.pack()
drop.place(x=450,y=450,anchor=tk.CENTER)

#select button
buttonCaller = partial(changeInterface,state)
sel = tk.Button(root,text="Select",padx = 10, pady = 5, fg = "white",bg="#691C1C",command = buttonCaller)
sel.pack()
sel.place(x=450,y=400,anchor=tk.CENTER)

#main loop
root.mainloop()



