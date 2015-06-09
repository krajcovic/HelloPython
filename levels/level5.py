#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'krajcovic'

import hashlib

a = [66.6, 333, 333, 1, 1234.5]
print a.count(333), a.count(66.6) , a.count('x')


def f(x): return x % 2 != 0 and x % 3 != 0
def cube(x): return x**3

print filter(f, range(2, 25))
print map(cube, range(1, 11))
print map(None, range(8), map(cube, range(8)))

a = range(8)
b = [3] * len(a)
print map(None, a, map(cube, b))

def add(x,y): return x+y

print reduce(add, range(1,10))
print reduce(add, a, 3.3)


ovoce = ['  banan', ' rajce', ' protlak    ']
print [zbran.strip() for zbran in ovoce]
vec = [2, 4,6]
print [num**2 for num in vec]

print [num**2 for num in vec if num != 2]
print [[num, num**5] for num in vec if num != 2]

print a
del a[2:4]
print a

m = hashlib.md5()
m.update('sakra')
tupple = 1, 2, 'ahoj',  m.digest(), 'k cemu to je',
print tupple

slovnik = {1: "jedna", 2: "dve", 3:"tri"}
print slovnik
