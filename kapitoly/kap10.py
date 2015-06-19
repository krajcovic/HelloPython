#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'krajcovic'

from math import pi
from kapitoly.seqtools import *

tuple = ('a', 'b', 'c', 'd', 'e','f')
print(type(tuple))
t1 = ('a',)
print(type(tuple))

a = "ahoj"
b = 5
print(a, b)
a, b = b, a
print(a, b)

def kruh(r):
    c = 2 * pi * r # Obvod kruhu
    a = pi * r ** 2 # Plocha kruhu
    return (r, c, a)

print(kruh(10))

my_list = ['a', 'b', 'd', 'e']
print(my_list)
insert_in_middle('c', my_list)
print(my_list)

my_tuple = ('a', 'b', 'd', 'e')
print(my_list)
insert_in_middle('c', my_tuple)
print(my_list)


basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
tup = (1,2,3,"alpha", 2)
st = set((1,2,3, "alpha",2))
print(st)

fr = frozenset('alcatraz')
print(fr)

print(set)