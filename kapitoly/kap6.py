#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'krajcovic'

import pydoc
import kapitoly.module1 as module1
import kapitoly.module2 as module2
import keyword
import string
import sys
import calendar


# from kapitoly.module1 import *
# from kapitoly.module2 import *

def copy_file(source, destination):
    infile = open(source, "r")
    outfile = open(destination, "w")

    while True:
        text = infile.read(50)
        if text == "":
            break

        outfile.write(text)

    infile.close()
    outfile.close()

    return
print(calendar.calendar(2008))

for i in range(2000, 2010):
    print(i, " is leap year: ", calendar.isleap(i))

print(sys.platform)
print(sys.path)
print(sys.version)
print(sys.argv)
print(dir(sys))


print(string.capwords("what's all this, then, amen"))

myfile = open("test.dat", "w")
print(myfile)
myfile.write("Now is the time ")
myfile.write("to close the file")
myfile.close()

myfile = open("test.dat", "r")
print(myfile)
print(myfile.read())
myfile.close()

print(keyword.iskeyword("for"))
print(keyword.iskeyword("all"))
print(keyword.kwlist)

print(module1.question)
print(module1.answer)
print(module2.question)
print(module2.answer)

print((module2.myage - module1.myage) == (module2.year - module1.year))

print("My name is %s" % __name__)

# print(question)
# print(question)
