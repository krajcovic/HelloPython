#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'krajcovic'

def fib(n):
    """
    Vytiskne fibonacciho rozvoj
    :param n: Maximalni rozsah
    :return:
    """
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a+b

def yes_no(vyzva, opakovani = 4, upozorneni = 'Zbyva vam X pokusu'):
    """

    :param vyzva:
    :param opakovani:
    :param upozorneni:
    :return:
    """
    while 1:
        ok = raw_input(vyzva)
        if ok in ('y', 'ye', 'yes'): return 1
        if ok in ('n', 'no'): return 0
        opakovani = opakovani - 1
        if opakovani < 0: raise IOError, 'Ignorant user'
        print upozorneni, opakovani


def f(a, L=[]):
    L.append(a)
    return L

def g(a, L=None):
    """

    :param a:
    :param L:
    :return:
    """
    if L is None: L = []
    L.append(a)
    return L

def myprint(format, *args):
    """

    :param format:
    :param args:
    :return:
    """
    print(format % args)

def big_burger(druh, *args, **keywords):
    """

    :param druh:
    :param args:
    :param keywords:
    :return:
    """
    print "-- Mate", druh, "?"
    print "-- Prominte, ", druh, " dosly."
    for arg in args: print arg
    print "-" * 40
    for key in keywords.keys(): print key, ":", keywords[key]


def inc(n):
    """

    :param n:
    :return:
    """
    return lambda x: x+n

f = inc(0)
print f(1)
print f(3)
print f(1)
print "*"*40

soucet = lambda a, b: a+b
print soucet(3,5)

big_burger("cheesburgery", "Velice se omlouvam, pane.", "Opravdu se velice omlouvam, pane.", zakaznik="Adam", prodavac="Bedrich", obchod="Domaci Burgery")

print f(1)
print f(2)
print f(3)

print g(1)
print g(2)
print g(3)


yes_no("test 4x: ")
yes_no("test 1x: ", 1)

f = fib
f(2000)


