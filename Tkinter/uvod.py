#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'krajcovic'

from tkinter import *
from tkinter.ttk import *
# from tkinter.messagebox import *
# from tkinter.filedialog import *
# from tkinter.colorchooser import *

pictures = {}


def example_01(root):
    w = Label(root, text="Hello Tkinter!")
    w.pack()


def example_02(root):
    # global pictures
    pictures["logo"] = PhotoImage(file="images/python.gif")
    w1 = Label(root, image=pictures["logo"])
    w1.pack(side="right")
    explanation = """V soucasnosti jsou podporovany
pouze formaty GIF a PPM/PGM.
Existuje alre rozhrani, ktere umoznuje
snadne vlozeni dalsich formatu"""
    w2 = Label(root, justify=LEFT, padding=16, text=explanation).pack(side="left")


if __name__ == "__main__":
    root = Tk()
    # example_01(root)
    example_02(root)
    root.mainloop()
