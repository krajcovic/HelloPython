#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'krajcovic'

class CountTo:
    def __init__(self, m):
        self.m = m
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= self.m:
            cur, self.n = self.n, self.n + 1
            return cur
        else:
            raise StopIteration()


class Squares(object):
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.stop:
            raise StopIteration
        else:
            current = self.start ** 2
            self.start += 1
            return current


def count_to(m):
    """
    Generatorova funkce, tim yield rikame v kazdem cyklu, ze to ma vratit jako hodnotu (myslim si :))
    :param m:
    :return:
    """
    n = 0
    while n <= m:
        yield n         # Jestli tomu rozumim, tak tim pouze rikame, ze dana funkce je generatorova nemisto normalni
        n += 1


def squares(start, stop):
    for i in range(start, stop):
        yield i ** 2

f = open("test.dat")
print(next(f))
print(next(f))
for i in f: print(i, end="")

print()

li = [1, 2, 3, 4]
ili = iter(li)
print(ili)
print(type(ili))
print(dir(ili))

# print(next(ili))
# print(next(ili))
# print(next(ili))
# print(next(ili))

for i in ili:
    print(i)

# ili = iter(li) # Tohle z nejakeho duvodu nefunguje, melo by mi to obnovit iterator
ili = iter(li)

print(next(ili))
# print(next(ili))
# print(next(ili))
# print(next(ili))

cnt = CountTo(5) # instance tridy a zaroven iterator
print(next(cnt))
for i in cnt:
    print(i, end=" ")

print("")

sqr = Squares(4, 8)
# print(next(sqr))
for i in sqr: print(i, end=" ")
for i in sqr: print(i, end=" ")

print(" ")
st = "akabus"
stv = (i for i in st) # generatorovy objekt, iterator
for i in st: print(i, end=" ")
print(" ")
for i in stv: print(i, end= "-")

print(" ")
ct = count_to(5)
for i in ct: print(i, end="*")

print(" ")
sq = squares(3, 8)
for i in sq: print(i, end=" ")

def fibonnaci():
    a, b, = 0, 1
    while True:
        yield a
        a, b, = b, a+b

def bad_example(number):
    try:
        return number / 0
    except: # slaba klauzule
        print("Mame chybu, nevime jakou")

# Určení přítomnosti či nepřítomnosti souboru

def exists(filename):   # název souboru v uvozovkách
    try:
        f = open(filename)
    except OSError:
        print ("Soubor nenalezen")
    else:
        f.close()
    print ("Soubor existuje a byl zavřen")

print(" ")
f = fibonnaci()
print(type(f))
print(f.__next__())
print(next(f))

for i in range(100): print(next(f), end=" ")
print(f.__next__())

print(" ")
ln = list(range(5))
tp = tuple(range(5))
print(ln, tp)


bad_example("aleš")



