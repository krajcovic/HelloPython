#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'krajcovic'

from sys import argv

nums = argv[1:]

for index, value in enumerate(nums):
    nums[index] = float(value)

print(sum(nums))
