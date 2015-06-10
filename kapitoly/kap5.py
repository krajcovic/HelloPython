#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'krajcovic'

import math
import doctest

def countdown(n):
    while n > 0:
        print(n)
        n = n-1
    print("Pal!")

def sequence(n):
    while n != 1:
        # print(n, end=", ")
        print(n)
        if n % 2 == 0:       # n is even
            n //= 2

        else:              # n is odd
            n = int(n*3+1)

def num_digits(n):
    count = 0
    while n:
        count += 1
        n = n//10
    return count

def binary_table(n):
    x = 1
    while x < n:
        print(x, '\t', 2**x)
        x += 1


def sqrt(n):
    """
    >>> sqrt(25)
    5.0

    :param n:
    :return:
    """
    approx = n/2.0
    better = (approx + n/approx)/2.0
    while better != approx:
        approx = better
        better = (approx + n/approx)/2.0

    return approx

def test_nine(x):
    """

    :param x:
    :return:
    """

    # print(x * 9, "==", (x -1) * 10 + (10 -x), end=" = ")
    return x * 9 == (x -1) * 10 + (10 -x)

for i in range(10000):
    if not test_nine(i):
        print(test_nine(i))
print("-----------------------------")

doctest.testmod(verbose=False)
print("-----------------------------")

print(sqrt(10))
print("-----------------------------")

binary_table(32)
print("-----------------------------")

# countdown(10)
sequence(3)
# sequence(math.factorial(100))

print("-----------------------------")
print(num_digits(780))

