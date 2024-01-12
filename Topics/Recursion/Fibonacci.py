import math


def fib(n):
    if n == 0 or n == 1:
        return n

    return fib(n-1) + fib(n-2)


def fib_mathematical(n):
    phi = (1 + math.sqrt(5)) / 2
    answer = round((phi ** n - (-phi) ** -n) / math.sqrt(5))
    print('\n' + str(answer))


def fib_range(start, end):
    for i in range(start, end + 1):
        print(fib(i), end=' ')


def test():
    fib_range(1, 10)

    fib_mathematical(10)
