#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'krajcovic'
__name__ = 'wiky.py'

a = range(1,100)
print(a)

b = list(range(1,100))
print(b)

data = [1,3,2,3,1]
for i in data:
    print(i, '->', data.count(i))