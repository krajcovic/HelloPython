#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'krajcovic'

import pickle

# f=open('/tmp/workfile', 'c')
# f.close()

f=open('/tmp/workfile', 'w')
f.write('This is the first line.')
f.close()

f=open('/tmp/workfile', 'r')
print(f.read())
f.close()

f=open('/tmp/workfile', 'r')
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

x = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
# x = 'Zatracena zkouska'

# f = open('/tmp/pickle.dat', 'w')
with open('/tmp/pickle.dat', 'wb') as f:
    pickle.dump(x, f)
# f.close

with open('/tmp/pickle.dat', 'rb') as f:
    y = pickle.load(f)

for keys, values in y.items():
    print(keys, ' ', values)

# f = open('/tmp/pickle.dat', 'r+')
# y = pickle.load(f)
# f.close()

