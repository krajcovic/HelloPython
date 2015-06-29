#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'krajcovic'

from tkinter import *
import threading


def example02(form):
    v = IntVar()
    v.set(1)  # počáteční volba, zde Python

    languages = [
        ("Python",1),
        ("Perl",2),
        ("Java",3),
        ("C++",4),
        ("C",5)
    ]

    def ShowChoice():
        print (v.get(), "-->", languages[v.get()-1][0])

    Label(form, text="""Choose your favourite
                     programming language:""",
          justify = LEFT, padx = 20).pack()

    for txt, val in languages:
        Radiobutton(form, text=txt, padx = 20,
                    variable=v, command=ShowChoice,
                    value=val).pack(anchor=W)


def example01(form):
    v = IntVar()
    Label(form,
          text="""Choose a programming language:""",
          justify=LEFT, padx=20).pack()
    Radiobutton(form, text="Python", padx=20,
                variable=v, value=1).pack(anchor=W)
    Radiobutton(form, text="Perl", padx=20,
                variable=v, value=2).pack(anchor=W)

form1 = Tk()
example02(form1)
# thread1 = threading.Thread(target = form1.mainloop, daemon=True)
# thread1.start()
form1.mainloop()


form2 = Tk()
example01(form2)
# thread2 = threading.Thread(target = form2.mainloop, daemon=True)
# thread2.start()
form2.mainloop()