#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'krajcovic'

import math
import random
import sys

import mojevoje

def novy_radek():
    print()

def hark(alfa, pi=3.14, *tup, **lib):
    print("Volne pozicni arugmenty: ", alfa)
    print("Keyword arugmenty: ", pi)
    print("Pozicni arg. entice: ", tup)
    print("Keyword arg. slovniku:" ,lib)

hark(5)
hark(5, 4, 3, fi = 8)
hark(5, a=8, b = 5)
hark(5, math.pi)

hark(5, 4, 1, 2, 3, 4, "tsest")

def test_args(a, b, c):
    print("Virbl: ", (b + c) * a)

slova = ("abra", "kadabra", "sakra")
slova = ("abra", "kadabra")
test_args(2, *slova)

pairs = {"b": "hola", "c":"hej"}
test_args(3, **pairs)

mojevoje.mocnina(5)
mojevoje.print_twice("kolese")

def f(n):
  return 3*n - 6
def g(n):
  return 5*n + 2
def h(n):
  return -2*n + 17
def doto(value, fun):
  return fun(value)

print(doto(7, f))
print(doto(7, g))
print(doto(7, h))
print(doto(7, str))