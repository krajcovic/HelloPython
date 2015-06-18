#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'krajcovic'

import random

nested = ["hello", 2.0, 5, [10, 2]]
print(nested)

elem = nested[3]
print(elem)
print(elem[0])
print(nested[3][1])

# Matice
matrix = [[1, 2, 3, ], [4, 5, 6], [7, 8, 9]]
print(matrix)


def make_matrix(rows, columns):
    """
    >>> make_matrix(3, 5)
    [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    >>> make_matrix(4, 2)
    [[0, 0], [0, 0], [0, 0], [0, 0]]
    >>> m = make_matrix(4,2)
    >>> m[1][1] = 7
    >>> m
    [[0, 0], [0, 7], [0, 0], [0, 0]]

    :param rows:
    :param columns:
    :return:
    """

    matrix = []
    for row in range(rows):
        matrix += [[0] * columns]

    return matrix

def rand(high):
    for i in range(high):
        x = random.random()
        print(x)
    print(x*high)

def getRoundedRand(hight):
    temp = random.random()
    return [int(temp * hight), temp]

def randList(count):
    l = list()
    for i in range(count):
        l.append(getRoundedRand(10))

    return l

if __name__ == '__main__':
    import doctest

    doctest.testmod()

    m = make_matrix(4, 3)
    print(m)
    m[1][2] = 7
    print(m)

    rand(5)
    counter = [0] * 10
    # print(counter)
    for item in randList(10):
        counter[item[0]] += 1
        # print(item)

    for i, count in enumerate(counter):
        print(i, ">>>", count)

