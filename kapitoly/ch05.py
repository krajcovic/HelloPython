#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'krajcovic'
# __name__ = '__main__'

import math

def compare(a, b):
    """
    >>> compare(5, 4)
    1
    >>> compare(7, 7)
    0
    >>> compare(2,3)
    -1

    :param a:
    :param b:
    :return:
    """
    if a == b:
        return 0
    elif a > b:
        return 1
    else:
        return -1

def hypotenuse(a, b):
    """
    >>> hypotenuse(3, 4)
    5.0
    >>> hypotenuse(12, 5)
    13.0
    >>> hypotenuse(7,24)
    25.0

    :param a:
    :param b:
    :return:
    """

    return math.sqrt(a**2 + b**2)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
