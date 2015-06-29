#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'krajcovic'

from tkinter import*

root = Tk()
spamVar = StringVar()
spamChB  =Checkbutton(root, text='Spam?',
                      variable=spamVar,
                      onvalue='yes', offvalue='no')
spamChB.pack()
root.mainloop()

print(spamVar.get())