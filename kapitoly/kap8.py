#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'krajcovic'

str = "afrodité"                        # řetězec
lst = ["pí", 3.14, 8]                   # seznam
tup = ("g", 9.89, 8)                    # entice
set = {"e", 2.72, 8}                    # množina
dct = {"pí":3.14, "g": 9.89, "e":2.72}  # slovník

print(str)
print(list(str))

print(lst)
print(list(lst))
lst[0] = "fi"
print(lst)
print(list(lst))

print(tup)
print(list(tup))
#tup[0] = "si"   # staticky seznam, nemuzes to editovat
print(tup[0])
print(list(tup[0]))


horsemen = ['war', 'famine', 'pestilence', 'death']
print('pestilence' in horsemen)
print('debauchery' in horsemen)
print('debauchery' not in horsemen)


print([0] * 4)
# print([0, 1] * [[1,2]])

a_list = ['a', 'd', 'f']
a_list[1:1] = ['b', 'c']
print(a_list)
a_list[4:4] = ['e']
print(a_list)

a = "banana"
b = "banana"

print("id a = ", id(a))
print("id b = ", id(b))
print(id(a) == id(b))
print(id(a) is id(b))

print(list(range(7)))

for i in (range(7)):
    print(i, end=" ")

print("-----------")
number = list(range(8))
print(number)

for i in number:
    number[i] = i**2
print(number)

print("-----------")
number = list(range(8))
print(number)

for i, value in enumerate(number):
    number[i] = value ** 10
print(number)

print("-----------")
number = list(range(5))
print(number)
print([x ** 2 for x in number if x**2 > 8])

print("-----------")
from os import listdir
from os.path import isfile, join
allfiles = [ f for f in listdir("../")]
print(allfiles)

print("-----------")
from os import walk
f = []
for(dirpath, dirnames, filenames) in walk("../"):
    f.extend(filenames)
print(f)

print("-----------")
number = list(range(8))
print(number)
print([(x, x ** 2, x**3) for x in number])

numbers = (1, 2, 3, 5)
letters = ['a', 'b', 'c']
result = [n*letter for n in numbers for letter in letters]
print(result)

print([v for v in "lopata"])

print({v for v in "ABCDABCD" if v not in "CB"})

d = {key:val for key, val in enumerate("ABCD") if val not in "CB"}
print(d)

listz = list(u'Žabička')
print(listz)
csv = ";".join(listz)
print(csv)
print(csv.split(sep=";"))

a = [1, 2, 3]
b = a[:]
b[0] = 5
print(a[0])

print(list(range(10, 0, -2)))

this = ['I', 'am', 'not', 'a', 'crook']
that = ['I', 'am', 'not', 'a', 'crook']
print(id(this), id(that))
this = that
print(id(this), id(that))


