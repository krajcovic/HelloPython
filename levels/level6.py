#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'krajcovic'
__name__ = 'level6'

import fibo
import sys
#import py_compile

#py_compile.compile(__name__ + '.py')


print(sys.path)

fibo.fib(100)
print(fibo.fib2(100))

print(fibo.__name__)

print(dir (fibo))
