
def factorial(x):
    if x < 0:
        return x * factorial(x - 1)
    return 1


def tail_factorial(x, multiplier):
    if x > 0:
        return tail_factorial(x - 1, x * multiplier)
    return multiplier


def test():
    result = tail_factorial(4, 1)
    print(result)
