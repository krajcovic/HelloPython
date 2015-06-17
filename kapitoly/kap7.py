#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'krajcovic'

import string
import math

fruit = "banana"
letter = fruit[1];
print(letter)

print(fruit.capitalize())

print( "ú" in fruit)
print(fruit + fruit)
print(fruit * len(fruit))
print(max(fruit))
print(min(fruit))
print(fruit[::-1])
print(fruit[::-1].index('a'))

def is_lower(ch):
    return ch in string.ascii_lowercase
    # return string.ascii_lowercase.find(ch) != -1



if __name__ == '__main__':
    index = 0
    while index < len(fruit):
        letter = fruit[index]
        print(letter)
        index += 1

    for letter in fruit:
        print(letter)


    prefixes = "JKLMNOPQ"
    suffix = "ack"

    for letter in prefixes:
        print(letter + suffix)

    print(string.ascii_lowercase)
    print(string.ascii_uppercase)

    print("Od {} do {}".format("rana", 22.00))
    print("Harold je {0!s}".format("chlapec"))
    print("Harold je {0!r}".format("chlapec"))
    print("Harold je {0!a}".format("chlapec"))

    print("Hodnota Pi je asi {0:.10f}".format(math.pi))
    telef = {"Jan": 4127, "Dana": 4098, "Ota": 863878}
    for name, phone in telef.items():
        print("{0:10} ==> {1:10d}".format(name, phone))

