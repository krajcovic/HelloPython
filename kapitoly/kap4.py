#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2015  <pi@raspberrypi.nitrok.cz>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#

import math


def is_divisible(x, y):
	return x % y == 0

def distance(x1, y1, x2, y2):
    dx = x2 -x1
    dy = y2 - y1
    # dsquared = dx**2 + dy**2

    # print("dx is ", dx)
    # print("dy is ", dy)
    # print("dsquared is ", dsquared)

    return math.sqrt(dx**2 + dy**2)
	
def print_twice(bruce):
    print(bruce, bruce)
    # print(cat)

def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)

def is_divisible_by_2_or_5(n):
    """
    >>> is_divisible_by_2_or_5(8)
    True
    >>> is_divisible_by_2_or_5(7)
    False
    >>> is_divisible_by_2_or_5(5)
    True
    >>> is_divisible_by_2_or_5(9)
    False

    :param n:
    :return:
    """
    return (n % 2 == 0) or (n % 5 == 0)

def main():
    chant1 = "Pie Jesu domine, "
    chant2 = "dona eis requim."
    cat_twice(chant1, chant2)
    print(distance(1,2,4,6))
    print(is_divisible(5, 6))
    print(is_divisible(8, 4))

    return 0

if __name__ == '__main__':
    import doctest
    #import pydevd

    #debugger = pydevd.GetGlobalDebugger()
    #if debugger is None:
    doctest.testmod()

    main()

