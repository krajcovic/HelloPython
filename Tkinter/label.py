#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'krajcovic'

from tkinter import *

counter = 0
def counter_label(lable):
    def count():
        global counter
        counter += 1
        lable.config(text = str(counter))
        lable.after(1, count)

    count()

root = Tk()
root.title("Counting Seconds")
label = Label(root, fg = "green")
label.pack()
counter_label(label)

button = Button(root, text="Stop", width=25, command=root.destroy)
button.pack()

root.mainloop()