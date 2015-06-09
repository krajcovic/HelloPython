#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'krajcovic'

import string
import math

s = 'Ahoj svete'
print(str(s))
print(`s`)

print(str(0.1))
print(`0.1`)

x = 10 * 3.25
y = 200 * 200

p = [x, y]
ps = repr(p)
print(p)
print(ps)

#Konvertovani retezcu prida uvozovky a zpetna lomitka:
ahoj = 'ahoj svete\n'
ahojs = `ahoj`
print(ahoj)
print(ahojs)


for x in range(1,11):
    print(string.rjust(`x`,2), string.rjust(`x*x`, 3), string.rjust(`x*x*x`, 4))

for x in range(9,20):
    print(string.ljust(`x`, 1)[0:1])

print(string.zfill('12', 5))
print(string.zfill('-3.14', 7))
print(string.zfill(round(math.pi,2), 5))

for x in range(1, 11):
    print '%2d %3d %4d' % (x, x*x, x*x*x)


print('Hodnota Ludolfova cisla je priblizne %5.20f %5.2f' % (math.pi,math.pi))

tabulka = {'Adolf': 4127, 'Beta': 4098, 'Cyril': 863778}
for jmeno, telefon in tabulka.items():
    print('%-10s ==> %10d' % (jmeno, telefon))

tabulka = {'Adolf': 4127, 'Beta': 4098, 'Cyril': 863778}
print('Beta: %(Beta)d; Adolf %(Adolf)d; Cyril %(Cyril)d' % tabulka)

ahoj = 'Vitame vas'
print('Mame pro vas nasledujici zpravu: %(ahoj)s!' % vars())





