#!/usr/bin/env python

__author__ = 'krajcovic'

a, b = 0, 1
while b < 10000:
    print b,
    a, b = b, a + b

i = 256 ** 2
print '\nHodnota i je = ', i
