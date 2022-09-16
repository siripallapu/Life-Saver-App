import tkinter as tk

root = tk.Tk()

v = tk.IntVar()
v.set(0)  

from openpyxl import *
from tkinter import *


def one():
    import Part2.py
    exec(Part2.py)
     

def two():
    import Part2a.py
    exec(Part2a.py)
     

def three():
    import Part2b.py
    exec(Part2b.py)
         

def four():
    import Part2c.py
    exec(Part2c.py)

        
tk.Label(root,
         text="""Choose an OPTION""",
         justify = tk.LEFT,
         padx = 20).pack()

    

tk.Radiobutton(root,
               text="Emergency",
               indicatoron = 0,
               width = 20,
               padx = 20,
               variable=v,
               command= one,
               ).pack(anchor=tk.W)

tk.Radiobutton(root,
               text="Non-emergency",
               indicatoron = 0,
               width = 20,
               padx = 20,
               variable=v,
               command= two,
               ).pack(anchor=tk.W)

tk.Radiobutton(root,
               text="Covid-19",
               indicatoron = 0,
               width = 20,
               padx = 20,
               variable=v,
               command= three,
               ).pack(anchor=tk.W)

tk.Radiobutton(root,
               text="Other",
               indicatoron = 0,
               width = 20,
               padx = 20,
               variable=v,
               command= four,
               ).pack(anchor=tk.W)



 
root.mainloop()
