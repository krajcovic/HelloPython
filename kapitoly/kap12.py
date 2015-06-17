#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'krajcovic'

import copy

class Emanuel:
    pass


Emanuel.strom = "ořech"
print(Emanuel.strom)

eman = Emanuel()
eman.les = 158

class Point:
    def __init__(self, x=0, y=0):
        """
        Constructor

        :param x:
        :param y:
        :return:
        """
        self.x = x
        self.y = y

    def __eq__(self, other):
        """

        :param other:
        :return:
        """
        return False

    def distance_from_origin(self):
        """

        :return:
        """
        return (self.x**2 + self.y**2) ** 0.5

    def toString(self):
        return self.x, self.y


def printPoint(obj):
    print('%s, %s' % (obj.x, obj.y))

def same_coords(p1, p2):
    return (p1.x == p2.x) and (p1.y == p2.y)




print(type(Point))
p = Point()
print(type(p))
print(p.toString())
g = Point(3,4)
print(g.distance_from_origin())

printPoint(g)

a = Point(3,5)
b = Point(3,5)
c = b
print(id(a), id(b), id(c))
print(a is b, a == b)
print(b is c, b == c)

print(a.x is b.x, a.x == b.x)
print(b.x is c.x, b.x == c.x)

p1 = Point(3,5)
p2 = copy.copy(p1)
print(p1 is p2)
print(same_coords(p1, p2))
p3 = copy.deepcopy(p1)



