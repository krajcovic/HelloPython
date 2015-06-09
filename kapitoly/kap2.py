#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'krajcovic'

# print(n=7)
print(7+5)

P = 1000000
r = 0.02
n = 1
t = 100

A = P * (1 + r / n) ** (n*t)
print(A)

print(type('Hello, World'))
print(type("Hello World"))

print(type(17))


print(int("32"))
# print(int("ahoj"))

print(type(True))
print(type(False))
print(type("true"))
print(type("false"))

secs_celk = int(input("Zadejte vterin celkem:"))
hodiny = secs_celk // 3600
secs_navic = secs_celk % 3600

minuty = secs_navic // 60
sekundy = secs_navic % 60

print("Celkem vterin: ", secs_celk)
print("Hodin, minut, vterin", hodiny, minuty, sekundy)

