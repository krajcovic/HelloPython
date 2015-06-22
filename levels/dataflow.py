#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'krajcovic'



a = ['cat', 'dog', 'cow']
for x in a:
    print(x, len(x))

a.append('defenestrace')

for x in a[:]:
    if len(x) > 10:
        a.insert(0, x)

print(a)

for x in range(len(a)):
    print(x, a[x])

exit(0)

x = int(input("Zadejte cele číslo: "))
if x > 0:
    print ('Větší než nula')
elif x == 0:
    print ('Přesná nula')
else:
    print ('Negative')
