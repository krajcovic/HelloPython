#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'krajcovic'

from tkinter import *


if __name__ == "__main__":
    root = Tk()

    whatever_you_do = "Cokoliv udelate je nedulezite, ale je velmi dulezite, ze to udelate"
    msg = Message(root, text = whatever_you_do)
    msg.config(bg = "lightgreen", font=('times', 24, 'italic'))
    msg.pack();

    root.mainloop()