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