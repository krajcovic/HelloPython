#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'krajcovic'

def encapsulate(val, seq):
    if type(seq) == type(""):
        return str(val)
    if type(seq) == type([]):
        return [val]
    return (val,)

def insert_in_middle(val, seq):
    """
    >>> insert_in_middle('c', 'abde')
    'abcde'
    >>> insert_in_middle('c', "abde")
    'abcde'
    >>> insert_in_middle('c', ['a', 'b', 'd', 'e'])
    ['a', 'b', 'c', 'd', 'e']
    >>> insert_in_middle('c', ('a', 'b', 'd', 'e'))
    ('a', 'b', 'c', 'd', 'e')

    :param val:
    :param seq:
    :return:
    """
    middle = int(len(seq) / 2)
    return seq[:middle] + encapsulate(val, seq) + seq[middle:]

def insert_in_middle_lst(val, lst):
    """
    >>> insert_in_middle_lst('c', ['a', 'b', 'd', 'e'])

    :param val:
    :param lst:
    :return:
    """
    middle = int(len(lst) / 2)
    lst[middle:middle] = [val]

def insert_in_middle_tup(val, tup):
    """
    >>> insert_in_middle_tup('c', ('a', 'b', 'd', 'e'))
    ('a', 'b', 'c', 'd', 'e')

    :param val:
    :param tup:
    :return:
    """
    middle = int(len(tup) / 2)
    return tup[:middle] + (val,) + tup[middle:]

if __name__ == "__main__":
    import doctest
    doctest.testmod()