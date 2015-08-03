#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'krajcovic'

eng2sp = {}
eng2sp['one'] = 'uno'
eng2sp['two'] = 'dos'
print(eng2sp)

eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp)

inventory = {'apples': 430, 'bananas': 312, 'pears': 217, 'oranges': 525}
print(inventory)

inventory['pears'] = 0
print(inventory)
print(len(inventory))
print(eng2sp.keys())

def letterCounter(text):
    letter_counter = {}
    for letter in text:
        letter_counter[letter] = letter_counter.get(letter, 0) + 1

    return(sorted(letter_counter.items()))

print(letterCounter("ZatraceneLehke"))


