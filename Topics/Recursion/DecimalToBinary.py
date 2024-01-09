import math


def find_binary(decimal: int, result: str):
    if decimal == 0:
        return result

    result = str(decimal % 2) + result
    return find_binary(math.floor(decimal / 2), result)


def test():
    number = 233
    binary = find_binary(number, "")
    print(binary)
