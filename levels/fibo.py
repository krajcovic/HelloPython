#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'krajcovic'
__name__ = 'fibo'

def fib(n):
    """
    Vytiskne fibonacciho rozvoj
    :param n: Maximalni rozsah
    :return:
    """
    a, b = 0, 1
    while b < n:
        print(b, end = '\t')
        a, b = b, a+b


def fib2(n):
    """
    Vrati Fibonacciho rozvou do cisla n
    :param n:
    :return:
    """
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b

    return result