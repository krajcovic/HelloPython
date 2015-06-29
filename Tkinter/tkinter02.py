#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *
# from tkinter.ttk import *

__author__ = 'krajcovic'




class Hello:
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi = Button(frame, text="Nazdar!", command=self.say_hi)
        self.hi.pack(side=RIGHT)

    def say_hi(self):
        print("Nazdarek kasparek")


root = Tk()
app = Hello(root)
root.mainloop()
