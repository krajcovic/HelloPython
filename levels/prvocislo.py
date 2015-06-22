__author__ = 'krajcovic'


for n in range(2, 100):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'je rovno', x, '*', n/x)
                break;
        else:
            print(n, 'je prvocislo')

def fib(n):
    """
    Vytiskne fibonacciho radu po n
    :param n:
    :return:
    """
    a, b = 0, 1
    while b < n:
        print(b ,)
        a, b = b, a+b


fib(100)