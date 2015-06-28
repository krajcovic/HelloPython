#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'krajcovic'

print(sum([1, 3, 5, 8]))
print(sum([3, 5, 8.3]))


def recursive_sum(nested_sum_list):
    sum = 0
    for element in nested_sum_list:
        if type(element) == type([]):
            sum = sum + recursive_sum(element)
        else:
            sum = sum + element

    return sum

def recursive_max(nested_num_list):
    """
    >>> recursive_max([2, 9, [1, 13], 8, 6])
    13
    >>> recursive_max([2, [[100, 7], 90], [1, 13], 8, 6])
    100
    >>> recursive_max([2, [[13, 7], 90], [1, 100], 8, 6])
    100
    >>> recursive_max([[[13, 7], 90], 2, [1, 100], 8, 6])
    100
    """
    largest = nested_num_list[0]
    while type(largest) == type([]):
        largest = largest[0]

    for element in nested_num_list:
        if type(element) == type([]):
            max_of_elem = recursive_max(element)
            if largest < max_of_elem:
                largest = max_of_elem
        else:           # element is not a list
            if largest < element:
                largest =element

    return largest

print(recursive_sum([2, 6, [3, 5], 8]))

def countdown(n):
    if n == 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n-1)

def fibonacci (n):
    # print(n)
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

previous = {0:0, 1:1}
def fibonacci2(n):
    if n in previous:
        return previous[n]
    else:
        previous[n] = fibonacci2(n-1) + fibonacci2(n-2)
        return previous[n]

#
# infinite_recursion.py
#
def recursion_depth(number):
    print("Recursion depth number {}." .format(number))
    recursion_depth(number + 1)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # recursion_depth(0)
    # countdown(20)
    # print(fibonacci(35))
    print(fibonacci2(100))